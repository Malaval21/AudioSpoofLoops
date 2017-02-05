# Real Time Audio Manipulator
from __future__ import print_function, division
import pydub
import os
import glob
import thinkdsp
import thinkplot
import wave
import contextlib
import numpy
import subprocess
import winsound
import time
from pydub import AudioSegment
from sklearn import tree  
pydub.AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"



def ConvertToWav(): #change this later to video to extract the audio track from video.                
                
    sound = pydub.AudioSegment.from_mp3("C:\\Users\\shrun\\Documents\\Hackathon_2017\\Haunted.mp3")
    sound.export("C:\\Users\\shrun\\Documents\\Hackathon_2017\\Haunted.wav", format="wav")
                
             

def PlayBack():
    fname = "C:\\Users\\shrun\\Documents\\Hackathon_2017\\Haunted.wav"
    duration = 0
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        audioLength = int(frames / float(rate))
        #print(duration) # get the size of audio track
    horror = thinkdsp.read_wave("C:\\Users\\shrun\\Documents\\Hackathon_2017\\Haunted.wav")
    funny = thinkdsp.read_wave("C:\\Users\\shrun\\Documents\\Hackathon_2017\\funnyNoise.wav")
    
    horror.play('C:\\Users\\shrun\\Documents\\Hackathon_2017\\temp.wav')
    #winsound.PlaySound('temp.wav', winsound.SND_FILENAME)
    #thinkdsp.play_wave(filename ='temp.wav',player='vlc')
    #wave1.play('C:\\Users\\shrun\\Documents\\Hackathon_2017\\tem.wav')
    #wave1.play('temp.wav')
    
   #now send small chunks to the analyzer
    start = 0.0
    end = 5.0
    while (end<=audioLength):
       
       chunk = horror.segment(start,end-start+1)
       flag = 1 #CHANGE THIS
       
       if(flag==0):
           #time.sleep(0.5)
           chunk.play('temp.wav')
           winsound.PlaySound('temp.wav', winsound.SND_FILENAME)           
           
       
       else:
           funny.play('temp.wav')
           winsound.PlaySound('temp.wav', winsound.SND_FILENAME) 
       
       start = end
       end +=5.20
   
   
    



          
def main():
   PlayBack()
    
    
if __name__ == "__main__": main()