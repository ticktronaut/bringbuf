#!/usr/bin/env python
#coding=utf-8

from collections import deque
import itertools
import warnings

class bRingBuf(object):
    """bRingBuf is a simple circular buffer to handle byte streams.
 
    It is based on enqueue, which is a efficient way to handle queues in
    Python. The main purpose of this library is to handle bytestreams, 
    like for instance from a serial port.

    Example
    -------
    ::
        from bringbuf import bRingBuf
        
        buf = bRingBuf(5)
        print(buf.is_empty())
        buf.enqueue([0x01, 0x02, 0x03, 0x04, 0x05, 0x06])
        print(buf.is_empty())
        print(buf.read(buf.len))
        print(buf.dequeue(3))
        print(buf.read(buf.len))

    Attributes
    ----------
    _max_size : int
        Maximal number that the ring buffer can carry, before overlfow.
    _b : bytearray
        Private byte container variable. It may be removed in future versions.
    _q : deque
        Python queue object, containing the buffer data.
    len : int
        Number of bytes written to the buffer.
    
    """
    def __init__(self, max_size=100):
        self._max_size = max_size
        #self._b = bytearray(max_size) # bytes vs. bytearray http://ze.phyr.us/bytearray/
        self._q = deque(maxlen=max_size)
        self.len = 0

    def enqueue(self, b):
        """Write bytes to the buffer.

        Parameters
        ----------
        b
            Iterable array of bytes to enqueue to the buffer

        """
        self._q.extend(b)
        self.len = len(self._q)
         

    def dequeue(self, n=1):
        """Read and remove number of bytes from the buffer.

        Parameters
        ----------
        n
            Number of byes to read and remove from the buffer (default is one).
        return
            Bytes read and removed from buffer.
        """
        if n > self.len: 
            message = str(n) + ' bytes requested, but only ' + str(self.len) + ' bytes available.'
            n = self.len 
            warnings.warn(message)
        b = bytearray(n)
        for i in range(n):
            b[i] = self._q.pop()

        self.len = len(self._q)
        return b

    def read(self, n=1, offset=0):
        """Read bytes in the buffer, without removing them from the buffer.

        Parameters
        ----------
        n
            Number of bytes to read from the buffer.
        offset
            Indes offset to start reading bytes.
        return
            Bytes read from buffer.
        """
        if ((n+offset) > self.len):
            message = str(n) + ' bytes requested, but only ' + str( (self.len-offset) ) + ' bytes available.'
            n = self.len - offset
            warnings.warn(message)
        return list( itertools.islice( self._q,offset,( n+offset ) ) )

    def clear(self):
        """Clear all bytes from buffer.
        """
        self.len = 0
        self._q.clear()

    def is_empty(self):
        """Returns true if buffer is empty.

        Parameters
        ----------
        return
            Return is True if buffer is empty, else False.
        """
        return not bool(self.len)

    def contains(self, pattern, offset=0):
        """Returns true if b is available in queue.
        
        Parameters
        ----------
        pattern 
            Pattern to search for (iterable byte sequence).
        return
            Return True if buffer contains pattern, else False.
        """
        if pattern[0] in self.read((self.len-offset), offset):
            index = ( self.read(self.len, offset).index(pattern[0]) ) + offset
            return ( self.read(len(pattern), index) == pattern )
        else:
            return False 

    def index(self, pattern, offset=0):
        """If the buffer includes the pattern, this function returns its index. Otherwise it return -1

        Parameters
        ----------
        pattern
            Pattern to search for (iterable byte sequence).
        return
            Index of occurence of pattern. If buffer does not contain pattern return value is -1.
        """
        if self.contains(pattern, offset):
            return self.read( (self.len-offset), offset ).index(pattern[0]) + offset
        else:
            return -1
