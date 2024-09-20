import math
import numpy as np
from main import *
from scipy.stats import norm


noise = Note(0, 15, signal_type="noise")
noise.export("noise.wav")

voice = Voice()
for x in range(-30, 30):
    y = norm.pdf(x, 0, 10)
    print(y)
    voice += Note(y * 200000 * random.choice((5, 0, 4, 1, 9, 2, 1, 3, 1, 4, 3, 5)), 0.1)

voice.export("gaussian.wav")