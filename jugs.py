# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:23:46 2019

@author: jcb877
"""

class Jug(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._volume = 0
        self._temperature = None
        
    def pour_out(self, volume, into_jug=None):
        pass
    
    def _average_temp(self, volume, temperature):
        weights = self._volume*self._temperature + volume*temperature
        return weights / (self._volume + volume)

    def _overflow_temp(self, volume, temperature):
        k = temperature - self._temperature
        return temperature - k*np.exp(-volume/self._capacity)

    def pour_in(self, volume, temperature):
        if self._volume == 0 and self._temperature is None:
            self._volume = volume if volume < self._capacity else self._capacity
            self._temperature = temperature
        elif self._volume + volume <= self._capacity:
            self._temperature = self._average_temp(volume, temperature)
            self._volume += volume
        else:
            new_volume = volume - (self._capacity - self._volume)
            print(new_volume)
            self._temperature = self._average_temp(volume - new_volume, temperature)
            print(self._temperature)
            self._volume = self._capacity
            self._temperature = self._overflow_temp(new_volume, temperature)

    def temperature(self):
        return self._temperature

    def water_volume(self):
        return self._volume

    def capacity(self):
        return self._capacity
