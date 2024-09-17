import numpy as np
import random
import scipy
from scipy.io import wavfile

class Note():
    def __init__(self, _freq, _dur, type="sin"):
        self.frequency = _freq
        self.duration = _dur
        self.type = type

    def __str__(self):
        return f"Note(frequency={self.frequency}, duration={self.duration})"

    def _generate(self):

        samples = np.linspace(0, self.duration, int(44100 * self.duration), endpoint=False)

        if self.type == "sin":
            sig = np.sin(2 * np.pi * self.frequency * samples)

        elif self.type == "sqr":
            sig = scipy.signal.square(2 * np.pi * self.frequency * samples)

        elif self.type == "tri":
            sig = scipy.signal.sawtooth(2 * np.pi * self.frequency * samples, 0.5)

        elif self.type == "saw":
            sig = scipy.signal.sawtooth(2 * np.pi * self.frequency * samples, 1)

        sig *= 32767

        sig = np.int16(sig)

        return sig

    def export(self, file_name):

        wavfile.write(file_name, 44100, self._generate())


class Voice():
    def __init__(self, notes=[]):
        self.notes = notes.copy()

    def __add__(self, other):
        self.notes.append(other)
        return self

    def __str__(self):
        return "Voice([" + ", ".join([str(note) for note in self.notes]) + "])"

    def _generate(self):

        combined = [note._generate() for note in self.notes]
        for i in combined:
            print(len(i))

        concated = np.concatenate(combined)
        return concated * 0.1 / np.max(concated)


    def export(self, file_name):

        wavfile.write(file_name, 44100, self._generate())

class Chorus():
    def __init__(self, voices=[]):
        self.voices = voices.copy()

    def __add__(self, other):
        self.voices.append(other)
        return self

    def __str__(self):
        return "Chorus([\n  " + ", \n  ".join(str(voice) for voice in self.voices) + "\n])"

    def _generate(self):

        voices = [voice._generate() for voice in self.voices]

        max_len = 0
        for voice in voices:
            if len(voice) > max_len:
                max_len = len(voice)

        combined = np.zeros(max_len)

        for voice in voices:
            zeros = np.zeros(max_len-len(voice))  # fill in the zeros
            combined = np.add(combined, np.concatenate((voice, zeros)))

        return combined

    def export(self, file_name):

        wavfile.write(file_name, 44100, self._generate())
