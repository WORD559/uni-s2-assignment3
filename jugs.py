# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:23:46 2019

@author: jcb877
"""

import numpy as np

class Jug(object):
    """Jug class. Describes a jug with a capacity where water can be poured in.

    All volumes are in litres. Specific heat capacity of water is assumed to be negligible
    and independent of temperature.

    Methods
    -------
    pour_out(volume, into_jug=None)
        Pour water out of the jug, optionally into another jug.

    pour_in(volume, temperature)
        Pour a volume of water of a given temperature into the jug.

    temperature()
        Get the temperature of the water in the jug

    water_volume()
        Get the volume of water in the jug

    capacity()
        Get the capacity of the jug
    """

    def __init__(self, capacity):
        """Make a new jug with given capacity.

        Parameters
        ----------
        capacity : number
            Capacity of the jug
        """
        self._capacity = capacity
        self._volume = 0
        self._temperature = None

    def pour_out(self, volume, into_jug=None):
        """Pour water out of the jug.

        Parameters
        ----------
        volume : number
            Volume of water to pour out of the jug
        into_jug : Jug object or None
            Optional jug to pour water into. By default, None.
        """
        volume = self._volume if volume == "all" or volume > self._volume else volume
        if isinstance(into_jug, Jug):
            into_jug.pour_in(volume, self._temperature)
        self._volume -= volume
        if self._volume == 0:
            self._temperature = None

    def _average_temp(self, volume, temperature):
        weights = self._volume*self._temperature + volume*temperature
        return weights / (self._volume + volume)

    def _overflow_temp(self, volume, temperature):
        k = temperature - self._temperature
        return temperature - k*np.exp(-volume/self._capacity)

    def pour_in(self, volume, temperature):
        """Pour water into the jug. Water in the jug mixes with added water to reach
        homogenous temperature.

        Parameters
        ----------
        volume : number
            Volume of water to pour into the jug
        temperature : number
            Temperature of water to pour into the jug
        """
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
        """Get temperature of water in the jug."""
        return self._temperature

    def water_volume(self):
        """Get volume of water in the jug"""
        return self._volume

    def capacity(self):
        """Get capacity of the jug"""
        return self._capacity
