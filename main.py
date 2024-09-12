import numpy as np
import random
import scipy
from scipy.io import wavfile

class Note():
    def __init__(self, _freq, _dur):
        self.frequency = _freq
        self.duration = _dur

    def __str__(self):
        return f"Note(frequency={self.frequency}, duration={self.duration})"

    def __generate(self):

        samples = np.linspace(0, self.duration, int(44100 * self.duration), endpoint=False)

        sig = np.sin(2 * np.pi * self.frequency * samples)

        sig *= 32767

        sig = np.int16(sig)

        return sig

    def export(self, file_name):

        wavfile.write(file_name, 44100, self.__generate())



class Voice():
    def __init__(self, notes=[]):
        self.notes = notes

    def __add__(self, other):
        self.notes.append(other)
        return self

    def __str__(self):
        return "Voice([" + ", ".join([str(note) for note in self.notes]) + "])"


class Chorus():
    def __init__(self, voices=[]):
        self.voices = voices

    def __add__(self, other):
        self.voices.append(other)
        return self

    def __str__(self):
        return "Chorus([\n  " + ", \n  ".join(str(voice) for voice in self.voices) + "\n])"

voice = Voice()
voice += Note(440, 1)
voice += Note(440, 1)
chorus = Chorus()
chorus += voice
chorus += voice
print(chorus)
Note(440, 1).export("hello.wav")