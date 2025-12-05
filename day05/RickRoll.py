import time
from machine import Pin, PWM

buzzer = PWM(Pin(13))

notes = [["rest",100],["A0",220],["C1",261],["C#1",277],["D1",294],["D#1",211],["E1",329],["F1",349],["F#1",370],["G1",391],["G#1",415],["A1",440],["A#1",466],["B1",494],["C2",523],["C#2",554],["D2",587],["D#2",622],["E2",659],["F2",698],["F#2",740],["G2",784],["G#2",830],["A2",880],["A#2",932]]

tempo = 114

def playtone(pitch, length=4, vol=1000):
    freq = 440
    for i in notes:
        if i[0] == pitch:
            freq = i[1]
        continue
    print("pitch: " + pitch + " | freq: " + str(freq) + " | vol: " + str(vol) + " | note length: " + str(length))
    buzzer.freq(freq)
    buzzer.duty_u16(vol)
    time.sleep((60/tempo) * (1/length) * 3.5)

playtone("C1",16)
playtone("D1",16)
playtone("F1",16)
playtone("D1",16)
playtone("A1",8)
playtone("rest",16,0)
playtone("A1",8)
playtone("rest",16,0)
playtone("G1",8)
playtone("rest",4,0)

playtone("C1",16)
playtone("D1",16)
playtone("F1",16)
playtone("D1",16)
playtone("G1",8)
playtone("rest",16,0)
playtone("G1",8)
playtone("rest",16,0)
playtone("F1",8)
playtone("rest",4,0)

playtone("C1",16)
playtone("D1",16)
playtone("F1",16)
playtone("D1",16)
playtone("F1",4)
playtone("G1",8)
playtone("E1",12)
playtone("D1",16)
playtone("C1",8)
playtone("rest",8,0)
playtone("C1",8)
playtone("G1",4)
playtone("F1",4)
playtone("rest",2,0)

playtone("C1",16)
playtone("D1",16)
playtone("F1",16)
playtone("D1",16)
playtone("A1",8)
playtone("rest",16,0)
playtone("A1",8)
playtone("rest",16,0)
playtone("G1",8)
playtone("rest",4,0)

playtone("C1",16)
playtone("D1",16)
playtone("F1",16)
playtone("D1",16)
playtone("C2",8)
playtone("rest",16,0)
playtone("E1",8)
playtone("rest",16,0)
playtone("F1",8)
playtone("rest",4,0)

playtone("C1",16)
playtone("D1",16)
playtone("F1",16)
playtone("D1",16)
playtone("F1",4)
playtone("G1",8)
playtone("E1",12)
playtone("D1",16)
playtone("C1",8)
playtone("rest",8,0)
playtone("C1",8)
playtone("G1",4)
playtone("F1",4)

buzzer.duty_u16(0)
