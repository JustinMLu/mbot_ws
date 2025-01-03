/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class slam_status_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public int slam_mode;
    public String map_path;
 
    public slam_status_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x522d41eb60d59eebL;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.slam_status_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.slam_status_t.class);
        long hash = LCM_FINGERPRINT_BASE
            ;
        classes.remove(classes.size() - 1);
        return (hash<<1) + ((hash>>63)&1);
    }
 
    public void encode(DataOutput outs) throws IOException
    {
        outs.writeLong(LCM_FINGERPRINT);
        _encodeRecursive(outs);
    }
 
    public void _encodeRecursive(DataOutput outs) throws IOException
    {
        char[] __strbuf = null;
        outs.writeLong(this.utime); 
 
        outs.writeInt(this.slam_mode); 
 
        __strbuf = new char[this.map_path.length()]; this.map_path.getChars(0, this.map_path.length(), __strbuf, 0); outs.writeInt(__strbuf.length+1); for (int _i = 0; _i < __strbuf.length; _i++) outs.write(__strbuf[_i]); outs.writeByte(0); 
 
    }
 
    public slam_status_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public slam_status_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.slam_status_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.slam_status_t o = new mbot_lcm_msgs.slam_status_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        char[] __strbuf = null;
        this.utime = ins.readLong();
 
        this.slam_mode = ins.readInt();
 
        __strbuf = new char[ins.readInt()-1]; for (int _i = 0; _i < __strbuf.length; _i++) __strbuf[_i] = (char) (ins.readByte()&0xff); ins.readByte(); this.map_path = new String(__strbuf);
 
    }
 
    public mbot_lcm_msgs.slam_status_t copy()
    {
        mbot_lcm_msgs.slam_status_t outobj = new mbot_lcm_msgs.slam_status_t();
        outobj.utime = this.utime;
 
        outobj.slam_mode = this.slam_mode;
 
        outobj.map_path = this.map_path;
 
        return outobj;
    }
 
}

