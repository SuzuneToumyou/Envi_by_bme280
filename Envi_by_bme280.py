#!/usr/bin/env python
#coding: utf-8
import bme280
import ambient

# bme280
bme280.init_bme280()
bme280.read_trimming_parameter()

ambi = ambient.Ambient(ID, "writeKey")
temperature, pressure, humidity = bme280.read_bme280()
print 'temp : %-6.2f' % (temperature) 
print 'pressure : %7.2f hPa' % (pressure)
print 'hum : %6.2f' % (humidity)

r = ambi.send({"d1": temperature, "d2": pressure, "d3": humidity})
r.close()
