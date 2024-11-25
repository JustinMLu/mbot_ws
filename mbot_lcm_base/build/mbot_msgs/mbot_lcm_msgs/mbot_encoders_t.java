/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class mbot_encoders_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public long ticks[];
    public int delta_ticks[];
    public int delta_time;
 
    public mbot_encoders_t()
    {
        ticks = new long[3];
        delta_ticks = new int[3];
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0xd77d05e6cf1b1040L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.mbot_encoders_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.mbot_encoders_t.class);
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
        outs.writeLong(this.utime); 
 
        for (int a = 0; a < 3; a++) {
            outs.writeLong(this.ticks[a]); 
        }
 
        for (int a = 0; a < 3; a++) {
            outs.writeInt(this.delta_ticks[a]); 
        }
 
        outs.writeInt(this.delta_time); 
 
    }
 
    public mbot_encoders_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public mbot_encoders_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.mbot_encoders_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.mbot_encoders_t o = new mbot_lcm_msgs.mbot_encoders_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.utime = ins.readLong();
 
        this.ticks = new long[(int) 3];
        for (int a = 0; a < 3; a++) {
            this.ticks[a] = ins.readLong();
        }
 
        this.delta_ticks = new int[(int) 3];
        for (int a = 0; a < 3; a++) {
            this.delta_ticks[a] = ins.readInt();
        }
 
        this.delta_time = ins.readInt();
 
    }
 
    public mbot_lcm_msgs.mbot_encoders_t copy()
    {
        mbot_lcm_msgs.mbot_encoders_t outobj = new mbot_lcm_msgs.mbot_encoders_t();
        outobj.utime = this.utime;
 
        outobj.ticks = new long[(int) 3];
        System.arraycopy(this.ticks, 0, outobj.ticks, 0, 3); 
        outobj.delta_ticks = new int[(int) 3];
        System.arraycopy(this.delta_ticks, 0, outobj.delta_ticks, 0, 3); 
        outobj.delta_time = this.delta_time;
 
        return outobj;
    }
 
}

