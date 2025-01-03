/* LCM type definition class file
 * This file was automatically generated by lcm-gen
 * DO NOT MODIFY BY HAND!!!!
 */

package mbot_lcm_msgs;
 
import java.io.*;
import java.util.*;
import lcm.lcm.*;
 
public final class occupancy_grid_t implements lcm.lcm.LCMEncodable
{
    public long utime;
    public float origin_x;
    public float origin_y;
    public float meters_per_cell;
    public int width;
    public int height;
    public int num_cells;
    public byte cells[];
 
    public occupancy_grid_t()
    {
    }
 
    public static final long LCM_FINGERPRINT;
    public static final long LCM_FINGERPRINT_BASE = 0x6aa23f24a5336649L;
 
    static {
        LCM_FINGERPRINT = _hashRecursive(new ArrayList<Class<?>>());
    }
 
    public static long _hashRecursive(ArrayList<Class<?>> classes)
    {
        if (classes.contains(mbot_lcm_msgs.occupancy_grid_t.class))
            return 0L;
 
        classes.add(mbot_lcm_msgs.occupancy_grid_t.class);
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
 
        outs.writeFloat(this.origin_x); 
 
        outs.writeFloat(this.origin_y); 
 
        outs.writeFloat(this.meters_per_cell); 
 
        outs.writeInt(this.width); 
 
        outs.writeInt(this.height); 
 
        outs.writeInt(this.num_cells); 
 
        if (this.num_cells > 0)
            outs.write(this.cells, 0, (int) num_cells);
 
    }
 
    public occupancy_grid_t(byte[] data) throws IOException
    {
        this(new LCMDataInputStream(data));
    }
 
    public occupancy_grid_t(DataInput ins) throws IOException
    {
        if (ins.readLong() != LCM_FINGERPRINT)
            throw new IOException("LCM Decode error: bad fingerprint");
 
        _decodeRecursive(ins);
    }
 
    public static mbot_lcm_msgs.occupancy_grid_t _decodeRecursiveFactory(DataInput ins) throws IOException
    {
        mbot_lcm_msgs.occupancy_grid_t o = new mbot_lcm_msgs.occupancy_grid_t();
        o._decodeRecursive(ins);
        return o;
    }
 
    public void _decodeRecursive(DataInput ins) throws IOException
    {
        this.utime = ins.readLong();
 
        this.origin_x = ins.readFloat();
 
        this.origin_y = ins.readFloat();
 
        this.meters_per_cell = ins.readFloat();
 
        this.width = ins.readInt();
 
        this.height = ins.readInt();
 
        this.num_cells = ins.readInt();
 
        this.cells = new byte[(int) num_cells];
        ins.readFully(this.cells, 0, (int) num_cells); 
    }
 
    public mbot_lcm_msgs.occupancy_grid_t copy()
    {
        mbot_lcm_msgs.occupancy_grid_t outobj = new mbot_lcm_msgs.occupancy_grid_t();
        outobj.utime = this.utime;
 
        outobj.origin_x = this.origin_x;
 
        outobj.origin_y = this.origin_y;
 
        outobj.meters_per_cell = this.meters_per_cell;
 
        outobj.width = this.width;
 
        outobj.height = this.height;
 
        outobj.num_cells = this.num_cells;
 
        outobj.cells = new byte[(int) num_cells];
        if (this.num_cells > 0)
            System.arraycopy(this.cells, 0, outobj.cells, 0, (int) this.num_cells); 
        return outobj;
    }
 
}

