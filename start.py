#!/usr/bin/env python

from glass.HTTPServer import test


try:
    print "Use Control-C to exit.  In Windows, use Control-Break."
    test()
except KeyboardInterrupt:
    pass