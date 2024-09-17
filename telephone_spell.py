import math
from main import *

tempo = 0.4

voice1 = Voice()
voice2 = Voice()
voice3 = Voice()

for i in range(100):
    number = 250 - math.cos(i / 100 * math.pi * 2) * 250
    print(number)

    if number < 480:
        voice1 += Note(number * random.randint(1, 8)/2, tempo)
    else:
        voice1 += Note(1, tempo)

    if number < 495:
        for j in range(2):
            voice2 += Note(number * random.randint(9, 16)/2, tempo/2, "sin")
    else:
        for j in range(2):
            voice2 += Note(1, tempo/2, "sin")

    for j in range(4):
        voice3 += Note(number * random.randint(17, 24)/2, tempo/4, "sin")

chorus = Chorus(voices=[voice1, voice2, voice3])
chorus.export("telephone_spell.wav")