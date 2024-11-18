"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class mbot_motor_pwm_t(object):
    __slots__ = ["utime", "pwm"]

    __typenames__ = ["int64_t", "float"]

    __dimensions__ = [None, [3]]

    def __init__(self):
        self.utime = 0
        self.pwm = [ 0.0 for dim0 in range(3) ]

    def encode(self):
        buf = BytesIO()
        buf.write(mbot_motor_pwm_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.utime))
        buf.write(struct.pack('>3f', *self.pwm[:3]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != mbot_motor_pwm_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return mbot_motor_pwm_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = mbot_motor_pwm_t()
        self.utime = struct.unpack(">q", buf.read(8))[0]
        self.pwm = struct.unpack('>3f', buf.read(12))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if mbot_motor_pwm_t in parents: return 0
        tmphash = (0xbb40043a6ca9d8f4) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if mbot_motor_pwm_t._packed_fingerprint is None:
            mbot_motor_pwm_t._packed_fingerprint = struct.pack(">Q", mbot_motor_pwm_t._get_hash_recursive([]))
        return mbot_motor_pwm_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", mbot_motor_pwm_t._get_packed_fingerprint())[0]

