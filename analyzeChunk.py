# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 23:04:59 2017

@author: Ankous
"""

from __future__ import print_function, division


def analyzeChunk(chunk, classifier):
    
    
    import thinkdsp
    import thinkplot
    import identify
    import numpy
    from identify import iden

    import matplotlib.pyplot as plt
    
    #debugging----------
    
    #segment = chunk.segment(0, 10)
    #segment.plot()
    #thinkplot.config(xlabel='Time (s)')
    
    #-------------------
    
    #Creates spectrum to analyze
    spectrum = chunk.make_spectrum()
    spectrum.plot()
    
    thinkplot.config(xlable = 'frequency (Hz)', legend = False)
    
    #number of smapled maximum amplitudes
    rng = 25
    
    #values of most prominent frequencies and their amplitudes
    pks = spectrum.peaks()[:rng]
    
    #calculating average of sampled frequencies' amplitudes
    for n in range(0,rng):
        avg =+ (pks[n])[1]
    
    #average smplitude value for sampled frequency peaks
    avg = avg/rng
    
    #3 most dominant frequencies and their respective amplitudes
    a = spectrum.peaks()[:3]
    
    #picking out frequency values
    b = a[0]
    c = a[1]
    d = a[2]

    e = [b[1], c[1], d[1]]    
    
    #passing chunk's identifying frequency characteristics and the machine 
    #into identifying function
    
    return    iden(e, classifier)
    
    
    