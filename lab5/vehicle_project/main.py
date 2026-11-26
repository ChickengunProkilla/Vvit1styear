from models.vehicle import Vehicle


def main():
    v=Vehicle("Dodge", "Chalenger", 2019)

    print(v.get_info())
    v.accelerate(60)
    print("accelerate(60)", v.get_info())
    v.brake(20)
    print("brake(20)", v.get_info())
    v.brake(100)
    print("brake(100)", v.get_info())  
    v.stop()
    print("stop()", v.get_info())


if __name__ == "__main__":
    main()
