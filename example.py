from main import *

voice1 = Voice()
voice1 += Note(440, 1, type="tri")
voice1 += Note(420, 1, type="tri")
voice1 += Note(440, 4, type="tri")

voice2 = Voice()
voice2 += Note(550, 1)
voice2 += Note(587.33, 2)
voice2 += Note(550, 3)


voice3 = Voice()
voice3 += Note(220, 1)
voice3 += Note(165, 1)
voice3 += Note(175, 1)
voice3 += Note(165, 3)

voice4 = Voice()
voice4 += Note(554.37, 0.25)
voice4 += Note(659.26, 0.25)
voice4 += Note(622.25, 0.25)
voice4 += Note(659.26, 0.25)

voice4 += Note(493.88, 0.25)
voice4 += Note(659.26, 0.25)
voice4 += Note(622.25, 0.25)
voice4 += Note(659.26, 0.25)

voice4 += Note(698.46, 0.25)
voice4 += Note(659.26, 0.25)
voice4 += Note(698.46, 0.25)
voice4 += Note(830.61, 0.25)

voice4 += Note(880, 3)

chorus = Chorus()
chorus += voice1
chorus += voice2
chorus += voice3
chorus += voice4
chorus.export("hello.wav")