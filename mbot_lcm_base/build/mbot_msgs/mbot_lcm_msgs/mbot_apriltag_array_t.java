/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class mbot_apriltag_array_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public int array_size;
    public mbot_lcm_msgs.mbot_apriltag_t detections[];
 
    public mbot_apriltag_array_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x8e24a47d2dab6b9bL;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.mbot_apriltag_array_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.mbot_apriltag_array_t.class);
        long hash = LCM_FINGERPRINT_BASE
             + mbot_lcm_msgs.mbot_apriltag_t._hashRecursive(classes)
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
 
        outs.writeInt(this.array_size); 
 
        for (int a = 0; a < this.array_size; a++) {
            this.detections[a]._encodeRecursive(outs); 
        }
 
    }
 
    public mbot_apriltag_array_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public mbot_apriltag_array_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.mbot_apriltag_array_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.mbot_apriltag_array_t o = new mbot_lcm_msgs.mbot_apriltag_array_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.utime = ins.readLong();
 
        this.array_size = ins.readInt();
 
        this.detections = new mbot_lcm_msgs.mbot_apriltag_t[(int) array_size];
        for (int a = 0; a < this.array_size; a++) {
            this.detections[a] = mbot_lcm_msgs.mbot_apriltag_t._decodeRecursiveFactory(ins);
        }
 
    }
 
    public mbot_lcm_msgs.mbot_apriltag_array_t copy()
    {
        mbot_lcm_msgs.mbot_apriltag_array_t outobj = new mbot_lcm_msgs.mbot_apriltag_array_t();
        outobj.utime = this.utime;
 
        outobj.array_size = this.array_size;
 
        outobj.detections = new mbot_lcm_msgs.mbot_apriltag_t[(int) array_size];
        for (int a = 0; a < this.array_size; a++) {
            outobj.detections[a] = this.detections[a].copy();
        }
 
        return outobj;
    }
 
}

