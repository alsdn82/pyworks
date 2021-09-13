# 마음대로 걷는 거북이

import random
import turtle as t

t.shape("turtle")
t.speed(0)
t.bgcolor("black")
t.color("white")

for x in range(1000):
    angle = random.randint(1, 360)  # 1~360도 랜덤한 각도
    t.setheading(angle)
    t.forward(10)
