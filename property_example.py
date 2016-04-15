# class celsius(object):
#     def __init__(self, t=0):
#         self._temp = t
#
#     def to_fahrenheit(self):
#         return  self._temp * (9 / 5) + 32
#
#     @property
#     def t(self):
#         print "inside get value"
#         return self._temp
#
#     @t.setter
#     def t(self, v):
#         print "inside set value"
#         if v > 230 :
#             raise ValueError("value should not exceed the value fo 230")
#         else:
#             self._temp = v
#
# c = celsius()
#
#
#


class Celsius(object):
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius(10)
