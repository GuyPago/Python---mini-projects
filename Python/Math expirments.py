class car:
    def __init__(self, color, km):
        self.color = color
        self.km = km

    def color_km(self):
        pass


blue_car = ca3r('blue', 20000)
red_car = car('red', 30000)

print(f'The {blue_car.color} car has {blue_car.km} kms')
print(f'The {red_car.color} car has {red_car.km} kms')