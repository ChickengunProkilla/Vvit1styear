from models.vehicle import Vehicle

def main():
    v=Vehicle("Dodge", "Chalenger", 2019)
    v.accelerate(45)
    print(v)          
    print(str(v))     

if __name__ == "__main__":
    main()
