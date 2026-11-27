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
            raise ValueError("Скорость отрицательна")
        self._speed=value

    def accelerate(self, value):
        self.speed=self.speed + value

    def brake(self, value):
        new_speed=self.speed-value
        self.speed=new_speed if new_speed>0 else 0

    def stop(self):
        self.speed = 0

    def get_info(self):
        return (f"{self.brand} {self.model} ({self.year}), "
                f"скорость: {self.speed} км/ч")
