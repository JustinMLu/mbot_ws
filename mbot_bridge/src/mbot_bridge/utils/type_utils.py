import importlib
import mbot_lcm_msgs
import base64


class BadMessageError(Exception):
    pass


def str_to_lcm_type(dtype):
    """Accesses the message type by string. Raises AttributeError if the class type is invalid."""
    # Check whether the dtype is a full path to the package.
    if "." in dtype:
        pkg, msg_type = dtype.split(".")  # The data type should be pkg.msg_type_t.
        pkg = importlib.import_module(pkg)
        return getattr(pkg, msg_type)

    # By default, try to load the type from mbot_lcm_msgs.
    return getattr(mbot_lcm_msgs, dtype)


def find_lcm_type(data, pkgs):
    """Tries to determine the LCM message type of the given data in the list of
    packages given.

    Args:
        data: Raw LCM message data to attempt to decode.
        pkgs: List of strings containing the names of message packages to
        search in. These must be installed as Python packages in the current
        environment.
    """
    for pkg_name in pkgs:
        pkg_module = importlib.import_module(pkg_name)
        for attr in dir(pkg_module):
            lcm_type_class = getattr(pkg_module, attr)
            if isinstance(lcm_type_class, type) and hasattr(lcm_type_class, 'decode'):
                lcm_type = lcm_type_class.__name__
                try:
                    # Try to decode the message with this type.
                    lcm_type_class.decode(data)
                    # If the decode succeeds, return this as the type.
                    return lcm_type
                except ValueError as e:
                    # If the decode fails, it throws a ValueError and we know this is the wrong type.
                    continue

    raise BadMessageError(f"Could not parse message type in packages: {[p for p in pkgs]}")


def decode(data, dtype):
    """Decode raw data from LCM channel to type based on type string."""
    try:
        lcm_obj = str_to_lcm_type(dtype)
    except (ValueError, AttributeError, ModuleNotFoundError) as e:
        raise BadMessageError(f"Could not parse dtype {dtype}: {e}")
    return lcm_obj.decode(data)


def occupancy_grid_to_byte_dict(data):
    """A special case utility for decoding the occupancy grid, but keeping the
    cell data as bytes."""
    decoded_data = mbot_lcm_msgs.occupancy_grid_t.decode(data)  # Decode the data.
    cell_bytes = data[-decoded_data.num_cells:]  # Extract the cells as bytes.
    data_d = {
        "utime": decoded_data.utime,
        "origin_x": decoded_data.origin_x ,
        "origin_y": decoded_data.origin_y,
        "meters_per_cell": decoded_data.meters_per_cell,
        "width": decoded_data.width,
        "height": decoded_data.height,
        "num_cells": decoded_data.num_cells,
        "cells": base64.b64encode(cell_bytes).decode('utf-8'),  # The cells should remain as bytes.
    }
    return data_d


def lcm_type_to_dict(data):
    """LCM types, once decoded"""
    data_d = {}
    for att, type_name in zip(data.__slots__, data.__typenames__):
        val = getattr(data, att)
        if "." in type_name:
            # This is an LCM type. Decode it first.
            if isinstance(val, list):
                # This is a list of types.
                val = [lcm_type_to_dict(v) for v in val]

            else:
                val = lcm_type_to_dict(val)
        data_d.update({att: val})
    return data_d


def dict_to_lcm_type(data, dtype):
    try:
        lcm_msg = str_to_lcm_type(dtype)()
    except (ValueError, AttributeError, ModuleNotFoundError) as e:
        raise BadMessageError(f"Could not parse dtype {dtype}: {e}")

    for k, v in data.items():
        # If one of the values is a list, we must check for types that need to be converted recursively.
        if isinstance(v, list):
            val_dtype = lcm_msg.__typenames__[lcm_msg.__slots__.index(k)]
            if val_dtype.startswith("mbot_lcm_msgs"):
                val_dtype = val_dtype.replace("mbot_lcm_msgs.", "")
                # Recursively convert to the correct data type.
                v = [dict_to_lcm_type(val, val_dtype) for val in v]

        setattr(lcm_msg, k, v)

    return lcm_msg
