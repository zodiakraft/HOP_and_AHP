import matplotlib.pyplot as plt

R = 8.31446261815324

class Isoprocess(object):
    """docstring"""
 
    def __init__(self, pressure = 0, volume = 0, temperature = 0, weight = 0, molar_weight = 0):
        """Constructor"""
        self.x = []
        self.y = []

        self.pressure = pressure * 100
        self.volume = volume * 100
        self.temperature = temperature * 100
        self.weight = weight
        self.molar_weight = molar_weight

        if self.weight > 100:
            self.const_weight()
        else:
            self.not_const_weight()

    
    def const_weight(self):
        for j in range(10, 100, 10):
            self.x = []
            self.y = []
            for i in range(1, 100):
                self.volume = j/i
                self.x.append(i)
                self.y.append(self.volume)
        # plt.subplot(2, 2, 1)
            plt.plot(self.x, self.y)
        # plt.subplot(2, 2, 3)
        # plt.plot(self.x, self.y)
        plt.show()

    def not_const_weight(self):
        # self.weight = (self.pressure * self.volume * self.molar_weight) / (self.temperature * R)
        # self.temperature = (self.pressure * self.volume * self.molar_weight) / (self.weight * R)
        # self.pressure = (self.weight * R * self.temperature) / (self.volume * self.molar_weight)
        # self.volume = (self.weight * R * self.temperature) / (self.pressure * self.molar_weight)
        if self.weight == 0:
            self.weight = (self.pressure * self.volume * self.molar_weight) / (self.temperature * R)
            print(self.weight)
        elif self.temperature == 0:
            self.temperature = (self.pressure * self.volume * self.molar_weight) / (self.weight * R)
            print(self.temperature)
        elif self.pressure == 0:
            self.pressure = (self.weight * R * self.temperature) / (self.volume * self.molar_weight)
            print(self.pressure)
        elif self.volume == 0:
            self.volume = (self.weight * R * self.temperature) / (self.pressure * self.molar_weight)
            print(self.volume * 1000)

process = Isoprocess(temperature = 293, pressure = 15680000, weight = 6.4, molar_weight = 0.032)