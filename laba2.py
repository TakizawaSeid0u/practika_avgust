class Vehicle:

    def __init__(self,brand, model, year):
        self.brand = brand
        self.model= model
        self.year =year
        
    #Выводим информацию
    def info (self):
        print ("Название бренда", self.brand)
        print ("Название модели ", self.model)
        print ("Год выхода", self.year)

#Создаем дочерний классс
class Car(Vehicle):

    def __init__(self, brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed):
        super().__init__(brand, model, year) 
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        self.engine_capacity = engine_capacity
        self.rotation_speed = rotation_speed

    def info(self):
        super().info()
        print(f"Тип горючего: {self.fuel_type}")
        print(f"Максимальная скорость: {self.max_speed}")
        print(f"Объём двигателя: {self.engine_capacity}")
        print(f"Частота вращения: {self.rotation_speed}")
        
    #P.S. Код работает только с машинами на дизеле и бензине
    def engine_pover_calc(self): #Расчитываем мощность исходя из объема
        if self.fuel_type == 'бензин' : # Если пользователь ввёл бензин
            pe = 0.85
            Ne = self.engine_capacity*pe*self.rotation_speed/120
            print('Мощность по обьёму=', Ne )
        if self.fuel_type == 'дизель': #Если пользователь ввёл дизель
            pe = 1
            Ne = self.engine_capacity*pe*self.rotation_speed/120
            print('Мощность по обьёму=', Ne )


if __name__ == "__main__":

    print('Введите название бренда:')
    brand = input()
    print('Введите название модели:')
    model = input()
    print('Введите год выпуска:')
    year = input()

    print('Введите тип горючего (бензин или дизель):')
    fuel_type = input()
    print('Введите максимальную скорость:')
    max_speed = float(input())
    print('Введите объём двигателя:')
    engine_capacity = float(input())
    print('Введите частоту вращения:')
    rotation_speed = float(input())

    # Создаём объект класса Vehicle
    vehicle = Vehicle(brand, model, year,)
    vehicle.info()

    # Создаём объект класса Car
    car = Car(brand, model, year, fuel_type, max_speed, engine_capacity, rotation_speed)
    car.info()
    car.engine_pover_calc()