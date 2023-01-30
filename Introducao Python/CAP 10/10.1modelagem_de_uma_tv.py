#MOdelagem de uma televisão

class televisão:
    def __init__(self):
        self.ligada = False
        self.canal = 2

tv = televisão()

print(tv.ligada)
print(tv.canal)

tv_sala = televisão()

tv_sala.ligada = True

tv_sala.canal = 4


print(tv.canal)
print(tv_sala.canal)

