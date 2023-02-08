#teste com metodos magicos (underscorees(__))

class Binario:
    def __init__(self, num_dec):
        self.num_dec = num_dec
        self.num_bin = bin(self.num_dec)
    def __str__(self):
        return ("%s " % (self.num_bin))
 

