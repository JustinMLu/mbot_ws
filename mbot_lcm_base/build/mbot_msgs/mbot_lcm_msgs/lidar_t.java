/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class lidar_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public int num_ranges;
    public float ranges[];
    public float thetas[];
    public long times[];
    public float intensities[];
 
    public lidar_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0xc4ee2dc3cd282b67L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.lidar_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.lidar_t.class);
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
 
        outs.writeInt(this.num_ranges); 
 
        for (int a = 0; a < this.num_ranges; a++) {
            outs.writeFloat(this.ranges[a]); 
        }
 
        for (int a = 0; a < this.num_ranges; a++) {
            outs.writeFloat(this.thetas[a]); 
        }
 
        for (int a = 0; a < this.num_ranges; a++) {
            outs.writeLong(this.times[a]); 
        }
 
        for (int a = 0; a < this.num_ranges; a++) {
            outs.writeFloat(this.intensities[a]); 
        }
 
    }
 
    public lidar_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public lidar_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.lidar_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.lidar_t o = new mbot_lcm_msgs.lidar_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.utime = ins.readLong();
 
        this.num_ranges = ins.readInt();
 
        this.ranges = new float[(int) num_ranges];
        for (int a = 0; a < this.num_ranges; a++) {
            this.ranges[a] = ins.readFloat();
        }
 
        this.thetas = new float[(int) num_ranges];
        for (int a = 0; a < this.num_ranges; a++) {
            this.thetas[a] = ins.readFloat();
        }
 
        this.times = new long[(int) num_ranges];
        for (int a = 0; a < this.num_ranges; a++) {
            this.times[a] = ins.readLong();
        }
 
        this.intensities = new float[(int) num_ranges];
        for (int a = 0; a < this.num_ranges; a++) {
            this.intensities[a] = ins.readFloat();
        }
 
    }
 
    public mbot_lcm_msgs.lidar_t copy()
    {
        mbot_lcm_msgs.lidar_t outobj = new mbot_lcm_msgs.lidar_t();
        outobj.utime = this.utime;
 
        outobj.num_ranges = this.num_ranges;
 
        outobj.ranges = new float[(int) num_ranges];
        if (this.num_ranges > 0)
            System.arraycopy(this.ranges, 0, outobj.ranges, 0, (int) this.num_ranges); 
        outobj.thetas = new float[(int) num_ranges];
        if (this.num_ranges > 0)
            System.arraycopy(this.thetas, 0, outobj.thetas, 0, (int) this.num_ranges); 
        outobj.times = new long[(int) num_ranges];
        if (this.num_ranges > 0)
            System.arraycopy(this.times, 0, outobj.times, 0, (int) this.num_ranges); 
        outobj.intensities = new float[(int) num_ranges];
        if (this.num_ranges > 0)
            System.arraycopy(this.intensities, 0, outobj.intensities, 0, (int) this.num_ranges); 
        return outobj;
    }
 
}

