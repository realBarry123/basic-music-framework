import numpy as np
import random
import scipy
from scipy.io import wavfile


class Note:
    def __init__(self, _freq, _dur, signal_type="sin"):
        self.frequency = _freq
        self.duration = _dur
        self.signal_type = signal_type

    def __str__(self):
        return f"Note(frequency={self.frequency}, duration={self.duration})"

    def _generate(self):

        """
        Convert the note into a signal.
        :return: numpy.ndarray generated signal
        """

        samples = np.linspace(0, self.duration, int(44100 * self.duration), endpoint=False)

        if self.signal_type == "sin":
            sig = np.sin(2 * np.pi * self.frequency * samples)

        elif self.signal_type == "sqr":
            sig = scipy.signal.square(2 * np.pi * self.frequency * samples)

        elif self.signal_type == "tri":
            sig = scipy.signal.sawtooth(2 * np.pi * self.frequency * samples, 0.5)

        elif self.signal_type == "saw":
            sig = scipy.signal.sawtooth(2 * np.pi * self.frequency * samples, 1)

        else:
            raise ValueError(
                f"Unrecognized signal type '{self.signal_type}'. "
                f"Try one these instead: 'sin', 'sqr', 'tri', 'saw'."
            )

        sig *= 32767

        sig = np.int16(sig)

        return sig

    def export(self, file_name):
        """
        Export note as .wav file.
        :param file_name: name of the file
        """
        wavfile.write(file_name, 44100, self._generate())


class Voice:
    def __init__(self, notes=[]):
        self.notes = notes.copy()

    def __add__(self, other):
        self.notes.append(other)
        return self

    def __str__(self):
        return "Voice([" + ", ".join([str(note) for note in self.notes]) + "])"

    def _generate(self):
        """
        Convert each note into a signal and concatenate them.
        :return: numpy.ndarray concatenated signal
        """
        combined = [note._generate() for note in self.notes]
        concated = np.concatenate(combined)
        return concated * 0.1 / np.max(concated)

    def export(self, file_name):
        """
        Export voice as .wav file.
        :param file_name: name of the file
        """
        wavfile.write(file_name, 44100, self._generate())


class Chorus:
    def __init__(self, voices=[]):
        self.voices = voices.copy()

    def __add__(self, other):
        self.voices.append(other)
        return self

    def __str__(self):
        return "Chorus([\n  " + ", \n  ".join(str(voice) for voice in self.voices) + "\n])"

    def _generate(self):
        """
        Convert each voice into a signal and add them with normalization
        :return: numpy.ndarray added signal
        """
        voices = [voice._generate() for voice in self.voices]

        max_len = 0
        for voice in voices:
            if len(voice) > max_len:
                max_len = len(voice)

        combined = np.zeros(max_len)

        for voice in voices:
            zeros = np.zeros(max_len - len(voice))  # fill in the zeros
            combined = np.add(combined, np.concatenate((voice, zeros)))

        return combined

    def export(self, file_name):
        """
        Export chorus as .wav file.
        :param file_name: name of the file
        """
        wavfile.write(file_name, 44100, self._generate())
