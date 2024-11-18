"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

import mbot_lcm_msgs.pose2D_t

class path2D_t(object):
    __slots__ = ["utime", "path_length", "path"]

    __typenames__ = ["int64_t", "int32_t", "mbot_lcm_msgs.pose2D_t"]

    __dimensions__ = [None, None, ["path_length"]]

    def __init__(self):
        self.utime = 0
        self.path_length = 0
        self.path = []

    def encode(self):
        buf = BytesIO()
        buf.write(path2D_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">qi", self.utime, self.path_length))
        for i0 in range(self.path_length):
            assert self.path[i0]._get_packed_fingerprint() == mbot_lcm_msgs.pose2D_t._get_packed_fingerprint()
            self.path[i0]._encode_one(buf)

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != path2D_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return path2D_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = path2D_t()
        self.utime, self.path_length = struct.unpack(">qi", buf.read(12))
        self.path = []
        for i0 in range(self.path_length):
            self.path.append(mbot_lcm_msgs.pose2D_t._decode_one(buf))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if path2D_t in parents: return 0
        newparents = parents + [path2D_t]
        tmphash = (0xd8a57fd0b3392990+ mbot_lcm_msgs.pose2D_t._get_hash_recursive(newparents)) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if path2D_t._packed_fingerprint is None:
            path2D_t._packed_fingerprint = struct.pack(">Q", path2D_t._get_hash_recursive([]))
        return path2D_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", path2D_t._get_packed_fingerprint())[0]

