#!/usr/bin/env python3

import lcm
import time
from collections import defaultdict
from threading import Thread, Event
import argparse
import importlib

# Command-line argument parsing
parser = argparse.ArgumentParser(description="LCM Spy CLI")
parser.add_argument("--channels", type=str, help="Comma-separated list of channel names to print decoded messages")
parser.add_argument("--rate", type=float, default=1, help="Rate at which data is printed in Hz (default: 1 Hz)")
parser.add_argument("--module", type=str, default="mbot_lcm_msgs", help="Module to use for decoding messages")
args = parser.parse_args()

# Parse channels from the --channels argument
channels_to_print = []
if args.channels:
    channels_to_print = args.channels.split(',')

# Load the module for decoding messages if provided
decode_module = None
if args.module:
    try:
        decode_module = importlib.import_module(args.module)
    except ImportError:
        print(f"Error: Could not import module {args.module}")
        decode_module = None

# Data structures to hold message counts, timestamps, and LCM types
message_counts = defaultdict(int)
message_times = defaultdict(list)
channel_types = {}
stop_event = Event()
decoded_message_dict = defaultdict(list)

def message_handler(channel, data):
    global message_counts, message_times, channel_types, decoded_message_dict
    
    lcm_type = "Unknown"
    decoded_message = None
    if decode_module:
        try:
            # Attempt to decode the message to find its type
            for attr in dir(decode_module):
                lcm_type_class = getattr(decode_module, attr)
                if isinstance(lcm_type_class, type) and hasattr(lcm_type_class, 'decode'):
                    try:
                        lcm_type = lcm_type_class.__name__
                        decoded_message = lcm_type_class.decode(data)
                        break
                    except Exception:
                        continue
        except Exception as e:
            lcm_type = f"Error: {e}"

    # Store the decoded message fields if the channel matches any of the specified channels
    if channel in channels_to_print and decoded_message:
        decoded_message_dict[channel] = decode_fields(decoded_message)

    # Update message counts and times
    message_counts[channel] += 1
    message_times[channel].append(time.time())
    channel_types[channel] = lcm_type

# Helper function to truncate long lists
def truncate_array(value):
    try:
        # checks if the value is array-like and if its length > 10
        if hasattr(value, '__len__') and len(value) > 10:
            return tuple(value[:10]) + ("...",)
    except TypeError:
        pass
        # otherwise return the original value
    return value

# Helper function to recursively decode nested messages
def decode_fields(decoded_msg):
    fields = []
    # decoded_msg.__slots__ is a list of components of the decoded message, such as utime
    for field in decoded_msg.__slots__:
        value = getattr(decoded_msg, field)
        # Check if the value is a list or tuple of nested objects
        if isinstance(value, (list, tuple)):
            nested_values = []
            for item in value:
                if hasattr(item, '__slots__'):
                    # Recursively decode each item in the list/tuple if it has __slots__
                    nested_values.append(decode_fields(item))
                else:
                    # Append the item directly if it doesn't have __slots__
                    nested_values.append(truncate_array(item))
            fields.append((field, truncate_array(nested_values)))
        elif hasattr(value, '__slots__'):
            # Recursively decode nested objects
            fields.append((field, decode_fields(value)))
        else:
            fields.append((field, truncate_array(value)))
    return fields

def print_decoded_message(msg, indent=0):
    # print (key, value)
    if isinstance(msg, tuple) and len(msg) == 2 and not hasattr(msg[1], '__len__'):
        key, value = msg
        print(f"{' ' * indent}{key:<20} {str(value):<20}")
    # print (key, [value1, value2, value3])
    elif isinstance(msg, tuple) and len(msg) == 2 and not hasattr(msg[1][0], '__len__'):
        key, value = msg
        print(f"{' ' * indent}{key:<20} {str(value):<20}")
    # print all other cases
    else:
        for item in msg:
            if isinstance(item, tuple) and len(item) == 2:
                key, value = item
                # if the value is singular print them directly
                if not hasattr(value, '__len__'):
                    print(f"{' ' * indent}{key:<20} {str(value):<20}")
                # if the value is a simple list
                elif (len(value) == 0) or (len(value) > 0 and not hasattr(value[0], '__len__')):
                    print(f"{' ' * indent}{key:<20} {str(value):<20}")
                # if the value is a nested array-like structure, recursion    
                else:
                    print(f"{' ' * indent}{key}:")
                    for v in value:
                        print_decoded_message(v, indent + 2)

def print_status():
    while not stop_event.is_set():
        time.sleep(1 / args.rate)  # Update at the specified rate
        print("\033[H\033[J", end="")  # Clear the screen
        print(f"{'Channel':<20} {'Type':<22} {'Rate':<10} {'Msgs Rcvd':<10}")
        print("="*60)
        for channel, times in message_times.items():
            current_time = time.time()
            # Filter times to keep only those within the last second
            times = [t for t in times if current_time - t < 1]
            message_times[channel] = times
            rate = len(times) / 1.0
            total_messages = message_counts[channel]
            lcm_type = channel_types.get(channel, "Unknown")
            print(f"{channel:<20} {lcm_type:<22} {rate:<10.2f} {total_messages:<10}")
        
        for channel in channels_to_print:
            if channel in decoded_message_dict:
                print(f"\nDecoded message on channel {channel}:")
                print(f"{'Field':<20} {'Value':<20}")
                print("="*40)
                # print(decoded_message_dict[channel])
                print_decoded_message(decoded_message_dict[channel]) 

def lcm_handle_loop(lc):
    while not stop_event.is_set():
        try:
            lc.handle_timeout(1000)  # Timeout set to 1000ms
        except Exception as e:
            print(f"Error in LCM handle loop: {e}")

if __name__ == "__main__":
    lc = lcm.LCM()

    # Subscribe to all LCM channels
    subscription = lc.subscribe(".*", message_handler)

    # Start the status printing thread
    status_thread = Thread(target=print_status)
    status_thread.daemon = True
    status_thread.start()

    # Start the LCM handle loop
    lcm_thread = Thread(target=lcm_handle_loop, args=(lc,))
    lcm_thread.daemon = True
    lcm_thread.start()
    
    try:
        while True:
            time.sleep(1)  # Main thread sleep
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        stop_event.set()
        lcm_thread.join()
        status_thread.join()
        lc.unsubscribe(subscription)
        print("Exited cleanly.")