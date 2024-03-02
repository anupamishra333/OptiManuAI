# coding=utf-8
from __future__ import print_function
from __future__ import division
import numpy as np


class EffectiveAction(object):

    def __init__(self, velocity,gain, setpoint):
        self.setpoint = setpoint
        self.effectiveVelocity = self.calcEffectiveVelocity(velocity, gain, setpoint)
        self.effectiveGain = self.calcEffectiveGain(gain, setpoint)

    def calcEffectiveVelocity(self, a, b, setpoint):
        minAlphaUnscaled = self.calcEffectiveVelocityUnscaled(self.calcEffectiveA(100, setpoint), self.calcEffectiveB(0, setpoint))
        maxAlphaUnscaled = self.calcEffectiveVelocityUnscaled(self.calcEffectiveA(0, setpoint), self.calcEffectiveB(100, setpoint))
        alphaUnscaled = self.calcEffectiveVelocityUnscaled(self.calcEffectiveA(a, setpoint), self.calcEffectiveB(b, setpoint))
        return (alphaUnscaled - minAlphaUnscaled) / (maxAlphaUnscaled - minAlphaUnscaled)

    def calcEffectiveGain(self, b, setpoint):
        minBetaUnscaled = self.calcEffectiveGainUnscaled(self.calcEffectiveB(100, setpoint))
        maxBetaUnscaled = self.calcEffectiveGainUnscaled(self.calcEffectiveB(0, setpoint))
        betaUnscaled = self.calcEffectiveGainUnscaled(self.calcEffectiveB(b, setpoint))
        return (betaUnscaled - minBetaUnscaled) / (maxBetaUnscaled - minBetaUnscaled)

    def calcEffectiveA(self, a, setpoint):
        return a + 101. - setpoint

    def calcEffectiveB(self, b, setpoint):
        return b + 1. + setpoint

    def calcEffectiveVelocityUnscaled(self, effectiveA, effectiveB):
        return (effectiveB + 1.0) / effectiveA

    def calcEffectiveGainUnscaled(self, effectiveB):
        return 1.0 / effectiveB

    def getEffectiveVelocity(self):
        return self.effectiveVelocity

    def getEffectiveGain(self):
        return self.effectiveGain