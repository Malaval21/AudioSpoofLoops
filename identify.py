# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 00:52:52 2017

@author: Ankous"""

import os
import glob
import thinkdsp
import thinkplot
import wave
import contextlib
import numpy
import subprocess
import winsound

def iden(chars, machine):
    return machine.predict([[chars]])[0]