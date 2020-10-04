#!/usr/bin/python3

import struct, time, smbus2
import bluepy.btle as btle

bus = smbus2.SMBus(1)
addr = 0x20
a = []

def main():
  global bus_data, x, y
  while True:
    joystick()

def joystick():

  #def sound():
    #if push button, randomly picks and plays sound

  def motor_cmd(a):
    m0=struct.pack("<BB", a[0], a[1])
    m1=struct.pack("<BB", a[2], a[3])
    preamble=struct.pack("<BBBB", 0x29, 0x42, 0x05, 0x46)
    postambl=struct.pack("<BBBB", 0x01, 0x2c, 0x00, 0x00)
    data0=preamble+m0+postambl
    data1=preamble+m1+postambl
    try:
      p = btle.Peripheral()
      p.connect("FA:48:51:02:33:88", btle.ADDR_TYPE_RANDOM)
      p.writeCharacteristic(0x000e, data0)
      p.writeCharacteristic(0x000e, data1)
    except Exception as e:
      print(e)

  def vector(x, y):
    if x < 448:
      if y < 448:
        return [0x00, 0x80, 0x01, 0xff]
      elif y < 576:
        if x < 64:
          return [0x80, 0xff, 0x01, 0xff]
        elif x < 192:
          return [0x80, 0x80, 0x01, 0x80]
        else:
          return [0x80, 0x55, 0x01, 0x55]
      else:
        return [0x80, 0x80, 0x81, 0xff]
    elif x < 576:
      if y < 64:
        return [0x00, 0xff, 0x01, 0xff]
      elif y < 192:
        return [0x00, 0xc0, 0x01, 0xc0]
      elif y < 448:
        return [0x00, 0x80, 0x01, 0x80]
      elif y < 576:
        return [0x00, 0x00, 0x01, 0x00]
      elif y < 832:
        return [0x80, 0x80, 0x81, 0x80]
      elif y < 960:
        return [0x80, 0xc0, 0x81, 0xc0]
      else:
        return [0x80, 0xff, 0x81, 0xff]
    else:
      if y < 448:
        return [0x00, 0xff, 0x01, 80]
      elif y < 576:
        if x < 832:
          return [0x00, 0x55, 0x81, 0x55]
        elif x < 960:
          return [0x00, 0x80, 0x81, 0x80]
        else:
          return [0x00, 0xff, 0x81, 0xff]
      else:
        return [0x80, 0xff, 0x81, 0x80]

  global bus_data, x, y
  bus_data = bus.read_i2c_block_data(addr, 0x03, 5)
  x = (bus_data[0]<<8 | bus_data[1])>>6
  y = (bus_data[2]<<8 | bus_data[3])>>6
#  bttn = bus_data[4]
  a = vector(x, y)
  motor_cmd(a)
  time.sleep(.1)

if __name__ == '__main__':
    main()
