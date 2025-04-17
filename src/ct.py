import json

import serial

# 配置串口
ser = serial.Serial(
    port="COM7",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

if ser.is_open:
    print("串口已打开:", ser.name)

    # 要发送的 HEX 数据（0x71, 0x72, ...）
    data = {"action": "L1", "param": {"param1": "aa", "param2": "bbb"}}

    # 发送数据
    ser.write(json.dumps(data).encode())
    rp = ser.readline()
    print(rp.decode())
    # 关闭串口
    ser.close()
else:
    print("串口打开失败！")

