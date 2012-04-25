#!/usr/bin/env python
# Time-stamp: <2012-04-25 11:17:56 Tao Liu>

"""Description

Setup script for MACS -- Model Based Analysis for ChIP-Seq data

Copyright (c) 2008,2009,2010,2011 Tao Liu <taoliu@jimmy.harvard.edu>

This code is free software; you can redistribute it and/or modify it
under the terms of the Artistic License (see the file COPYING included
with the distribution).

@status:  beta
@version: $Revision$
@author:  Tao Liu
@contact: taoliu@jimmy.harvard.edu
"""

import os
import sys
from distutils.core import setup, Extension

# Use build_ext from Cython if found
command_classes = {}

try: 
    from numpy import get_include as numpy_get_include 
    numpy_include_dir = [numpy_get_include()] 
except: 
    numpy_include_dir = []
    sys.stderr.write("CRITICAL:Numpy must be installed!\n")
    sys.exit(1)



def main():
    if float(sys.version[:3])<2.7 or float(sys.version[:3])>=2.8:
        sys.stderr.write("CRITICAL: Python version must be 2.7!\n")
        sys.exit(1)

    ext_modules = [Extension("MACS2.cProb", ["MACS2/cProb.pyx"], libraries=["m"]),
                   Extension("MACS2.IO.cParser",["MACS2/IO/cParser.pyx"]),
                   Extension("MACS2.cPileup", ["MACS2/cPileup.pyx"], include_dirs=numpy_include_dir ),
                   Extension("MACS2.cArray", ["MACS2/cArray.pyx"]),                       
                   Extension("MACS2.cPeakModel", ["MACS2/cPeakModel.pyx"], include_dirs=numpy_include_dir),                   
                   Extension("MACS2.cPeakDetect", ["MACS2/cPeakDetect.pyx"]),
                   Extension("MACS2.IO.cPeakIO", ["MACS2/IO/cPeakIO.pyx"],),
                   Extension("MACS2.IO.cBedGraphIO", ["MACS2/IO/cBedGraphIO.pyx"],),                   
                   Extension("MACS2.IO.cFixWidthTrack", ["MACS2/IO/cFixWidthTrack.pyx"], include_dirs=numpy_include_dir),
                   Extension("MACS2.IO.cBedGraph", ["MACS2/IO/cBedGraph.pyx"], libraries=["m"]),
                   Extension("MACS2.IO.cScoreTrack", ["MACS2/IO/cScoreTrack.pyx"], include_dirs=numpy_include_dir ),
                   Extension("MACS2.IO.cCompositeScoreTrack", ["MACS2/IO/cCompositeScoreTrack.pyx"],),
                   Extension("MACS2.hashtable", ["MACS2/hashtable.pyx"],include_dirs=["MACS2/",numpy_get_include()]),
                   ]
    
    setup(name="MACS",
          version="2.0.10",
          description="Model Based Analysis for ChIP-Seq data",
          author='Tao Liu',
          author_email='vladimir.liu@gmail.com',
          url='http://github.com/taoliu/MACS/',
          package_dir={'MACS2' : 'MACS2'},
          packages=['MACS2', 'MACS2.IO', 'MACS2.data'],
          package_data={'MACS2': ['data/*.dat']},          
          scripts=['bin/macs2',
                   'bin/MLEPostPoisRatios',
                   'bin/MCMCPostPoisRatios',                   
                   ],
          classifiers=[
              'Development Status :: 4 - experimental',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: Artistic License',
              'Operating System :: MacOS :: MacOS X',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Programming Language :: Python',
              ],
          cmdclass = command_classes,
          ext_modules = ext_modules
          )

if __name__ == '__main__':
    main()
