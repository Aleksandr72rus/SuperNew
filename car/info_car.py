from car.model import Tesla


class InfoCar(Tesla):
    def __init__(self, brand, model, year, km, battery):
        super().__init__(brand, model, year, km)
        self.battery = battery

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")

