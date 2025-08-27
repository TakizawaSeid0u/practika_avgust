#Импортируем необходимые библиотеки
from math import pi
from math import sqrt
from math import radians
from math import cos, sin, tan

import matplotlib.pyplot as plt


#Ввод данных
print('Введите длину стороны пентагона:')
side = int(input())


class Pentagon:


    #Конструктор
    def __init__(self, side):
        self.side = side 
        self.fig, self.ax = plt.subplots()
        self.corner = 72  #Угол для пятиугольника (360/5 = 72 градуса)
        self.R = self.side / (2 * sin(pi/5))  #Радиус описанной окружности
        self.r = self.side / (2 * tan(pi/5))  #Радиус вписанной окружности
        

    #Радиус описанной окружности 
    def circum_r(self):
        self_r_c = self.side / (2 * sin(pi/5))
        print(f'Радиус описанной окружности {self_r_c:.2f}')
        return self_r_c
    

    #Рисуем описанную окружность
    def circum_r_ax(self, center, color):
        radius = self.circum_r()
        circum_circle = plt.Circle(center, radius, color=color, fill=False)
        self.ax.add_artist(circum_circle)


    #Площадь описанной окружности
    def circum_s(self):
        self_s_c = pi * (self.circum_r())**2
        print(f'Площадь описанной окружности {self_s_c:.2f}')
        

    #Радиус вписанной окружности
    def inscr_r(self):
        self_r_i = self.side / (2 * tan(pi/5))
        print(f'Радиус вписанной окружности {self_r_i:.2f}')
        return self_r_i


    #Рисуем вписанную окружность
    def inscr_r_ax(self, center, color):
        radius = self.inscr_r()
        inscr_circle = plt.Circle(center, radius, color=color, fill=False)
        self.ax.add_artist(inscr_circle)


    #Площадь вписанной окружности
    def inscr_s(self):
        self_s_i = pi * (self.inscr_r())**2
        print(f'Площадь вписанной окружности {self_s_i:.2f}')
        

    #Площадь пятиугольника
    def pent_s(self):
        self_s_p = (5 * self.side**2) / (4 * tan(pi/5))
        print(f'Площадь пятиугольника {self_s_p:.2f}')   


    #Периметр пятиугольника 
    def pent_p(self):
        self_p_p = 5 * self.side
        print(f'Периметр пятиугольника {self_p_p}')
        return self_p_p


    #Отрисуем пятиугольник
    def draw_pentagon(self, color='blue'):
        vertices = []
        for i in range(5):
            angle = radians(i * self.corner - 90)  #Начнем с верхней вершины
            x = self.R * cos(angle)
            y = self.R * sin(angle)
            vertices.append((x, y))

        #Соеденим вершины
        for i in range(5):
            x_values = [vertices[i][0], vertices[(i + 1) % 5][0]]
            y_values = [vertices[i][1], vertices[(i + 1) % 5][1]]
            self.ax.plot(x_values, y_values, color=color, linewidth=2)


    def show(self):
        self.ax.set_xlim(-40, 40)
        self.ax.set_ylim(-40, 40)
        self.ax.set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.title('Пятиугольник с вп. и оп. окружностями')
        plt.show()


if __name__ == "__main__":
    drawer = Pentagon(side)
    drawer.draw_pentagon(color='red')  #Рисуем пятиугольник
    drawer.inscr_r_ax(center=(0, 0), color='green')  #Вписанная окружность
    drawer.circum_r_ax(center=(0, 0), color='blue')  #Описанная окружность
    
    
    #Выводим все расчеты
    print("=== РАСЧЕТЫ ДЛЯ ПЯТИУГОЛЬНИКА ===")
    drawer.pent_p()
    drawer.pent_s()
    drawer.inscr_r()
    drawer.inscr_s()
    drawer.circum_r()
    drawer.circum_s()
    drawer.show()