/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class pose3D_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public float x;
    public float y;
    public float z;
    public float angles_rpy[];
    public float angles_quat[];
 
    public pose3D_t()
    {
        angles_rpy = new float[3];
        angles_quat = new float[4];
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x039971088b9a8678L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.pose3D_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.pose3D_t.class);
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
 
        outs.writeFloat(this.x); 
 
        outs.writeFloat(this.y); 
 
        outs.writeFloat(this.z); 
 
        for (int a = 0; a < 3; a++) {
            outs.writeFloat(this.angles_rpy[a]); 
        }
 
        for (int a = 0; a < 4; a++) {
            outs.writeFloat(this.angles_quat[a]); 
        }
 
    }
 
    public pose3D_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public pose3D_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.pose3D_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.pose3D_t o = new mbot_lcm_msgs.pose3D_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.utime = ins.readLong();
 
        this.x = ins.readFloat();
 
        this.y = ins.readFloat();
 
        this.z = ins.readFloat();
 
        this.angles_rpy = new float[(int) 3];
        for (int a = 0; a < 3; a++) {
            this.angles_rpy[a] = ins.readFloat();
        }
 
        this.angles_quat = new float[(int) 4];
        for (int a = 0; a < 4; a++) {
            this.angles_quat[a] = ins.readFloat();
        }
 
    }
 
    public mbot_lcm_msgs.pose3D_t copy()
    {
        mbot_lcm_msgs.pose3D_t outobj = new mbot_lcm_msgs.pose3D_t();
        outobj.utime = this.utime;
 
        outobj.x = this.x;
 
        outobj.y = this.y;
 
        outobj.z = this.z;
 
        outobj.angles_rpy = new float[(int) 3];
        System.arraycopy(this.angles_rpy, 0, outobj.angles_rpy, 0, 3); 
        outobj.angles_quat = new float[(int) 4];
        System.arraycopy(this.angles_quat, 0, outobj.angles_quat, 0, 4); 
        return outobj;
    }
 
}
