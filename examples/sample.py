#!/usr/bin/env python
#coding=utf-8

# The following example shows the basic usage of bRingBuf class

from bringbuf import bRingBuf

# define a ring buffer with the size of 5 bytes
buf = bRingBuf(5)
# check if buffer is empty (True)
print(buf.is_empty())
# enqueue 6 bytes to the buffer
# (not that the buffer will overflow)
buf.enqueue([0x01, 0x02, 0x03, 0x04, 0x05, 0x06])
# check if buffer is empty (False) 
print(buf.is_empty())
# read content of the whole buffer without removing any bytes
print(buf.read(buf.len))
# read and remove three bytes from the buffer 
print(buf.dequeue(3))
# read content of the whole buffer without removing any bytes
print(buf.read(buf.len))
# enque four new bytes
buf.enqueue([0x07, 0x08, 0x09])
# read content of the whole buffer without removing any bytes
print(buf.read(buf.len))
# contains pattern?
print(buf.contains([0x02, 0x08]), buf.contains([0x07, 0x08, 0x09]))
# index of patterns
print(buf.index([0x02, 0x08]), buf.index([0x07, 0x08, 0x09]))
