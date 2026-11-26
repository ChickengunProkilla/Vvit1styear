from models.vehicle import vehicle
def main():
    v1=vehicle("Dodge", "Charger", 2019)
    v2=vehicle("Subaru", "Impreza", 2021)

    v1._speed=250
    print(v1.brand, v1.model, v1.year, v1._speed)
    print(v2.brand, v2.model, v2.year, v2._speed)

if __name__ == "__main__":
    main()
