class Vehicle:
    def __init__(self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
        self._speed=0

    def speed(self):
        return self._speed

    def speed(self, value):
        if value<0:
            raise ValueError("Отрицательная скорость")
        self._speed=value

    def accelerate(self, value):
        self._speed+=value

    def brake(self, value):
        self._speed -= value
        if self._speed < 0:
            self._speed = 0

    def stop(self):
        self._speed = 0

    def get_info(self):
        return (f"{self.brand} {self.model} ({self.year}), "
                f"скорость: {self._speed} км/ч")
