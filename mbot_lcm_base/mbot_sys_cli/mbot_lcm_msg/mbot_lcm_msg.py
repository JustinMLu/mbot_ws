#!/usr/bin/env python3

import argparse
import importlib

# Command-line argument parsing
parser = argparse.ArgumentParser(description="Displays LCM message's data structure")
parser.add_argument("--module", type=str, default="mbot_lcm_msgs", help="Module to use for decoding messages")

subparsers = parser.add_subparsers(dest='command', help='sub-command help')

# Sub-parser for the "show" command
parser_show = subparsers.add_parser('show', help='Output the message definition')
parser_show.add_argument('msgs', type=str, help='Comma-separated list of message names you want to check')

# Sub-parser for the "list" command
parser_list = subparsers.add_parser('list', help='List all available LCM messages')

args = parser.parse_args()

# Load the module for decoding messages if provided
decode_module = None
if args.module:
    try:
        decode_module = importlib.import_module(args.module)
    except ImportError:
        print(f"Error: Could not import module {args.module}")
        decode_module = None

def read_all_lcm_type():
    lcm_type_dict = dict()
    if decode_module:
        try:
            # Attempt to decode the message to find its type
            for attr in dir(decode_module):
                lcm_type_class = getattr(decode_module, attr)
                if isinstance(lcm_type_class, type) and hasattr(lcm_type_class, 'decode'):
                    try:
                        # lcm_type is the name of the message type
                        lcm_type = lcm_type_class.__name__
                        # lcm_type_dict[lcm_type] is a list of tuple (data type, variable name)
                        lcm_type_dict[lcm_type] = list(zip(lcm_type_class.__typenames__, lcm_type_class.__slots__))
                    except Exception:
                        continue
        except Exception as e:
            lcm_type_dict['Error'] = str(e)

    return lcm_type_dict

def inspect_class_attributes(cls):
    attributes = dir(cls)
    for attr in attributes:
        try:
            value = getattr(cls, attr)
            print(f"{attr}: {value}")
        except AttributeError:
            print(f"{attr}: <unavailable>")

def show_msg_struct(msgs):
    msgs_to_print = msgs.split(',')
    lcm_type_dict = read_all_lcm_type()
    for msg in msgs_to_print:
        if msg not in lcm_type_dict.keys():
            print(f"Error: {msg} is not a valid lcm message type!")
            continue
        print(f"{msg}\n")
        for dtype, vname in lcm_type_dict[msg]:
            print(f"{' ' * 4}{dtype:<10} {vname:<10}")
        print()


def main():
    if args.command == 'list':
        lcm_type_dict = read_all_lcm_type()
        for key in lcm_type_dict.keys():
            print(f"{key}")
    elif args.command == 'show':
        show_msg_struct(args.msgs)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
