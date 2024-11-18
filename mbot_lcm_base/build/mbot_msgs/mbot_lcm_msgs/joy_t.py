"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class joy_t(object):
    __slots__ = ["timestamp", "left_analog_X", "left_analog_Y", "right_analog_X", "right_analog_Y", "right_trigger", "left_trigger", "dpad_X", "dpad_Y", "button_A", "button_B", "button_2", "button_X", "button_Y", "button_5", "button_l1", "button_r1", "button_l2", "button_r2", "button_select", "button_start", "button_12", "button_left_analog", "button_right_analog", "button_15"]

    __typenames__ = ["int64_t", "float", "float", "float", "float", "float", "float", "float", "float", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t", "int8_t"]

    __dimensions__ = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    def __init__(self):
        self.timestamp = 0
        self.left_analog_X = 0.0
        self.left_analog_Y = 0.0
        self.right_analog_X = 0.0
        self.right_analog_Y = 0.0
        self.right_trigger = 0.0
        self.left_trigger = 0.0
        self.dpad_X = 0.0
        self.dpad_Y = 0.0
        self.button_A = 0
        self.button_B = 0
        self.button_2 = 0
        self.button_X = 0
        self.button_Y = 0
        self.button_5 = 0
        self.button_l1 = 0
        self.button_r1 = 0
        self.button_l2 = 0
        self.button_r2 = 0
        self.button_select = 0
        self.button_start = 0
        self.button_12 = 0
        self.button_left_analog = 0
        self.button_right_analog = 0
        self.button_15 = 0

    def encode(self):
        buf = BytesIO()
        buf.write(joy_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qffffffffbbbbbbbbbbbbbbbb", self.timestamp, self.left_analog_X, self.left_analog_Y, self.right_analog_X, self.right_analog_Y, self.right_trigger, self.left_trigger, self.dpad_X, self.dpad_Y, self.button_A, self.button_B, self.button_2, self.button_X, self.button_Y, self.button_5, self.button_l1, self.button_r1, self.button_l2, self.button_r2, self.button_select, self.button_start, self.button_12, self.button_left_analog, self.button_right_analog, self.button_15))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != joy_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return joy_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = joy_t()
        self.timestamp, self.left_analog_X, self.left_analog_Y, self.right_analog_X, self.right_analog_Y, self.right_trigger, self.left_trigger, self.dpad_X, self.dpad_Y, self.button_A, self.button_B, self.button_2, self.button_X, self.button_Y, self.button_5, self.button_l1, self.button_r1, self.button_l2, self.button_r2, self.button_select, self.button_start, self.button_12, self.button_left_analog, self.button_right_analog, self.button_15 = struct.unpack(">qffffffffbbbbbbbbbbbbbbbb", buf.read(56))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if joy_t in parents: return 0
        tmphash = (0x411d5cfa5f4fa383) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if joy_t._packed_fingerprint is None:
            joy_t._packed_fingerprint = struct.pack(">Q", joy_t._get_hash_recursive([]))
        return joy_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", joy_t._get_packed_fingerprint())[0]

