#!/usr/bin/env python
# coding=utf-8
# Authors: Petra Abramovic, Luka Jovanovic
## Print out fragments from 5 minute long samples

import os
import sys

from aeneas.exacttiming import TimeValue
from aeneas.executetask import ExecuteTask
from aeneas.language import Language
from aeneas.syncmap import SyncMapFormat
from aeneas.task import Task
from aeneas.task import TaskConfiguration
from aeneas.textfile import TextFileFormat
import aeneas.globalconstants as gc

# This directory holds 2 additional directories, from which one contains the .txt files and the other contains the .wav files
# enter your path to these files
path_to_dir = "/home/jova/Tresors/organic/Uni/Computerlinguistik/HS20/programmierprojekt/5min_clip"
dir_slash = "/"

#print(os.listdir(os.getcwd()))


def get_txt_path():
    os.chdir(path_to_dir)
    dir_list = os.listdir(os.getcwd())
    txt_path = str(os.path.abspath(os.getcwd())) + dir_slash +dir_list[1]

    return txt_path

def get_audio_path():
    os.chdir(path_to_dir)
    dir_list = os.listdir(os.getcwd())
    audio_path = str(os.path.abspath(os.getcwd())) + dir_slash + dir_list[0]

    return audio_path

def find_pairs(filename):
    audio_path = get_audio_path()
    txt_path = get_txt_path()
    dir_list_txt = os.listdir(txt_path)
    dir_list_txt = sorted(dir_list_txt)
    dir_list_audio = os.listdir(audio_path)
    dir_list_audio = sorted(dir_list_audio)
    print(dir_list_audio)
    print(dir_list_txt)

    for num in range(len(dir_list_txt)):
        if filename in dir_list_txt[num]:
            for num2 in range(len(dir_list_audio)):
                if filename in dir_list_audio[num2]:
                    aeneas_txt_path = txt_path + dir_slash + dir_list_txt[num2]
                    aeneas_audio_path = audio_path + dir_slash + dir_list_audio[num]
                    return [aeneas_txt_path, aeneas_audio_path]

def main():

    for filename in sorted(os.listdir(get_txt_path())):
        filename = filename[:-4]
        print(filename)

        pair_list = find_pairs(filename)
        print(pair_list)
        #create Task object
        config = TaskConfiguration()
        config[gc.PPN_TASK_LANGUAGE] = Language.SRP
        config[gc.PPN_TASK_IS_TEXT_FILE_FORMAT] = TextFileFormat.PLAIN
        config[gc.PPN_TASK_OS_FILE_FORMAT] = SyncMapFormat.TXT
        task = Task()
        task.configuration = config
        task.audio_file_path_absolute = pair_list[1]
        task.text_file_path_absolute = pair_list[0]

        #process Task
        ExecuteTask(task).execute()

        #print produced sync map
        print(task.sync_map)


if __name__ == "__main__":
    main()
