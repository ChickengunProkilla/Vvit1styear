from models.vehicle import Vehicle


def main():
    v=Vehicle("Dodge", "Chalenger", 2019)

    v.speed=80
    print(v.speed)

    v.accelerate(20)
    print("accelerate(20)", v.speed)
    v.brake(50)
    print("brake(50)", v.speed)
    v.brake(100)
    print("brake(100)", v.speed())  

    try:
        v.speed=-10
    except ValueError as e:
        print("скорость не может быть отрицательной",e)

if __name__ == "__main__":
    main()
