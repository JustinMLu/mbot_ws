> This tool is a command-line version of lcm-spy

## Usage
```shell
mbot lcm-spy [-h] [--channels CHANNELS] [--rate RATE] [--module MODULE]
```

### Options
- `-h, --help`: Show this help message and exit
- `--channels CHANNELS`: Comma-separated list of channel names to print decoded messages
- `--rate RATE`: Rate at which data is printed in Hz (default: 1 Hz)
- `--module MODULE`: Module to use for decoding messages (default: "mbot_lcm_msgs")

For example, if you run:

```shell
mbot-lcm-spy --channels MBOT_ENCODERS,MBOT_IMU --rate 5
```
- Note that **DO NOT** put space between 2 channel names like this: `MBOT_ENCODERS, MBOT_IMU`

You will get the output:


#### Channel Information

| Channel          | Type                | Rate  | Msgs Rcvd |
| ---------------- | ------------------- | ----- | --------- |
| MBOT\_ODOMETRY   | pose2D\_t           | 25.00 | 318       |
| MBOT\_IMU        | mbot\_imu\_t        | 25.00 | 318       |
| MBOT\_VEL        | twist2D\_t          | 25.00 | 318       |
| MBOT\_MOTOR\_VEL | mbot\_motor\_vel\_t | 25.00 | 318       |
| MBOT\_MOTOR\_PWM | mbot\_motor\_pwm\_t | 25.00 | 318       |
| MBOT\_ENCODERS   | mbot\_encoders\_t   | 25.00 | 317       |
| MBOT\_TIMESYNC   | timestamp\_t        | 1.00  | 13        |

#### Decoded message on channel MBOT\_ENCODERS:

| Field        | Value            |
| ------------ | ---------------- |
| utime        | 1718035974387383 |
| ticks        | (-1, 276, 0)     |
| delta\_ticks | (0, 0, 0)        |
| delta\_time  | 40453            |

#### Decoded message on channel MBOT\_IMU:

| Field        | Value                               |
| ------------ | ------------------------------------- |
| utime        | 1718035974387383               |
| gyro         | (0.002396918134763837, -0.0005326484679244459, 0.0017311074770987034)  |
| accel        | (-0.7628380656242371, 0.6754170656204224, -10.061798095703125) |
| mag          | (0.25, 0.25, 0.375) |
| angles\_rpy  | (-0.06807039678096771, -0.07631554454565048, -0.12962138652801514)     |
| angles\_quat | (0.99658203125, -0.03643798828125, -0.03594970703125, -0.064697265625) |
| temp         | 0.0                                  |
