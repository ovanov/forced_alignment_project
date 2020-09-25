from pydub import AudioSegment
import math
import sys
from sys import argv


# Arguments: 0 = filename, 1 = split length (5 per default)
file = sys.argv[1]
if len(sys.argv) == 3:
    len_wav = sys.argv[2]

folder = 'C:\\Users\\abram\\OneDrive - uzh.ch\\prog_projekt_HS20\\aeneas\\interviews'

# long_wavs = ['F1.wav', 'F2.wav', 'F3.wav', 'F4.wav', 'F5.wav', 'F6.wav', 'F7.wav',
#            'F8.wav', 'M1.wav', 'M2.wav', 'M3.wav', 'M4.wav', 'M5.wav', 'M6.wav',
#            'M7.wav', 'M8.wav', 'M9.wav', 'M10.wav']



class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")

    def multiple_split(self, min_per_split=5):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splitted successfully')



splitted = SplitWavAudioMubin(folder, file)
if len(sys.argv) == 3:
    splitted.multiple_split(min_per_split=len_wav)
elif len(sys.argv) == 2:
    splitted.multiple_split()
else:
    print("too many arguments.")

# for doc in long_wavs:
#     file = doc
#     splitted = SplitWavAudioMubin(folder, file)
#     if len(sys.argv) == 2:
#         splitted.multiple_split(min_per_split=len_wav)
#     elif len(sys.argv) == 1:
#         splitted.multiple_split()
#     else:
#         print("too many arguments.")
