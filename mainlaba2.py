from laba2 import Vehicle, Car

if __name__ == "__main__":

    # класс Vehicle
    print('Введите название бренда:')
    brand = input()
    print('Введите название модели:')
    model = input()
    print('Введите год выпуска:')
    year = input()

    # класс Car
    print('Введите тип горючего (бензин или дизель):')
    fuel_type = input()
    print('Введите максимальную скорость:')
    max_speed = float(input())
    print('Введите объём двигателя:')
    engine_capacity = float(input())
    print('Введите частоту вращения:')
    rotation_speed = float(input())

    vehicle = Vehicle(brand, model, year)
    vehicle.info()

    car = Car(brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed)
    car.info()

    # Расчёт мощности двигателя
    print("Рассчёт мощности двигателя:")
    car.engine_pover_calc()