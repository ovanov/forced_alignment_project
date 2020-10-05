#!/usr/bin/env python
# coding=utf-8
# Authors: Petra Abramovic, Luka Jovanovic
## cut wavs in portions of 5 min

from pydub import AudioSegment
import math
import sys
from sys import argv
import os


path_from = sys.argv[1]
filename = sys.argv[2]
path_to = sys.argv[3]
# Arguments: 1 = directory of file to be cut; 2 = filename (to be cut); 3 = directory where the cut file goes; 4 = len_wav(optional)

# file = sys.argv[1]
if len(sys.argv) == 3:
    len_wav = sys.argv[4]



filepath = path_from + '\\' + filename

folder = 'C:\\Users\\abram\\OneDrive - uzh.ch\\prog_projekt_HS20\\programmierprojekt_HS20\\cut_wavs_full_length'
cut_folder = 'C:\\Users\\abram\\OneDrive - uzh.ch\\prog_projekt_HS20\\programmierprojekt_HS20\\wav_5min'





class SplitWavAudioMubin():
    def __init__(self, path_from, filename, path_to):
        self.path_from = path_from
        self.filename = filename
        self.path_to = path_to
        self.filepath = self.path_from + '\\' + self.filename



        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.path_to + '\\' + split_filename, format="wav")

    def multiple_split(self, min_per_split=5):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splitted successfully')



splitted = SplitWavAudioMubin(path_from, filename, path_to)
if len(sys.argv) == 5:
    splitted.multiple_split(min_per_split=len_wav)
elif len(sys.argv) == 4:
    splitted.multiple_split()
else:
    print("too many arguments.")


