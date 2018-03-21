"""
bringbuf is a simple circular buffer to handle byte streams (for instance from a serial port), heavily based on enque.
"""

from bringbuf.bringbuf import bRingBuf 

version_info = (0, 1, 0)
__version__ = '%d.%d.%s' % version_info

__all__ = ['bringbuf']
