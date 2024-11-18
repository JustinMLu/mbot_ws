/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class mbot_apriltag_t implements lcm.lcm.LCMEncodable
{
    public int tag_id;
    public mbot_lcm_msgs.pose3D_t pose;
 
    public mbot_apriltag_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x5211181edd780e73L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.mbot_apriltag_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.mbot_apriltag_t.class);
        long hash = LCM_FINGERPRINT_BASE
             + mbot_lcm_msgs.pose3D_t._hashRecursive(classes)
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
        outs.writeInt(this.tag_id); 
 
        this.pose._encodeRecursive(outs); 
 
    }
 
    public mbot_apriltag_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public mbot_apriltag_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.mbot_apriltag_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.mbot_apriltag_t o = new mbot_lcm_msgs.mbot_apriltag_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.tag_id = ins.readInt();
 
        this.pose = mbot_lcm_msgs.pose3D_t._decodeRecursiveFactory(ins);
 
    }
 
    public mbot_lcm_msgs.mbot_apriltag_t copy()
    {
        mbot_lcm_msgs.mbot_apriltag_t outobj = new mbot_lcm_msgs.mbot_apriltag_t();
        outobj.tag_id = this.tag_id;
 
        outobj.pose = this.pose.copy();
 
        return outobj;
    }
 
}

