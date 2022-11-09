from csianim import Animator
from csianim import Circle

import numpy as np
from vidgear.gears import CamGear

import cv2


animation = Animator()
animation.at(0, attributes = {'radius': 0})
animation.at(24, attributes = {'radius': 50})
animation.at(32, attributes = {'radius': 50})
animation.at(56, attributes = {'radius': 0})
animation.repeat()

circles = [
    Circle(position = (i * 10, 250), radius = 5, color = (255, 0, 0))
    for i in range(50)
] + [
    Circle(position = (250, i * 10), radius = 5, color = (255, 255, 0))
    for i in range(50)
] + [
    Circle(position = (i * 10, i * 10), radius = 5, color = (0, 255, 0))
    for i in range(50)
] + [
    Circle(position = (i * 10, 500 - i * 10), radius = 5, color = (0, 0, 255))
    for i in range(50)
]

anims = [animation.apply_to(c) for c in circles]

idx = 0
while True:
    frame = np.zeros((500, 500, 3)).astype(np.uint8)

    for c in anims:
        c.step()
        frame = c.draw(frame)

    cv2.imshow('frame', frame)
    cv2.waitKey(24)
    idx += 1
