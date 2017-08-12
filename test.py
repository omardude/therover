#!/usr/bin/env python


import explorerhat
from time import sleep
from random import randint

try:
    while True:
        duration = randint(1,5)
        explorerhat.motor.one.forward(20)
        explorerhat.motor.two.forward(20)
        sleep(duration)
        explorerhat.motor.one.backward(20)
        explorerhat.motor.two.forward(20)
        sleep(duration)
except KeyboardInterrupt:
    explorerhat.motor.stop()
    explorerhat.output.one.off()