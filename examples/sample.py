#!/usr/bin/env python
#coding=utf-8

# The following example shows the basic usage of bRingBuf class

from bringbuf import bRingBuf

# define a ring buffer with the size of 5 bytes
buf = bRingBuf(5)

# the buffers length initially is zero
print(buf.len)

# check if buffer is empty (True)
print(buf.is_empty())

# enqueue 6 bytes to the buffer
# (note that the buffer will overflow)
buf.enqueue([0x01, 0x02, 0x03, 0x04, 0x05, 0x06])

# now five bytes are in the buffer (maximal number of bytes)
print(buf.len)

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

# check whether buffer contains a pattern?
# this might be solved by buf.index, which also returns the index,
# but this is a more descriptive way to check
print(buf.contains([0x02, 0x08]),  buf.contains([0x07, 0x08, 0x09]))

# index of patterns
print(buf.index([0x02, 0x08]), buf.index([0x07, 0x08, 0x09]))

# contains pattern (with offset)?
print(buf.contains([0x02, 0x08], 2), buf.contains([0x07, 0x08, 0x09], offset=2))

# index of patterns (with offset)
print(buf.index([0x02, 0x08], 2), buf.index([0x07, 0x08, 0x09], 2))

# read with offset
print(buf.read(3, 3))

# enqueue a single byte
buf.enqueue_byte(0xff)

print(buf.read(buf.len))

# dequeue a single byte
print(buf.dequeue_byte())
