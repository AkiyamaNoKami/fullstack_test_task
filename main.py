import math
"""1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список,
 содержащий только уникальные элементы из исходного списка."""
def unique_elements(lst):
    return list(set(lst))

"""2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум)
 и возвращает список всех простых чисел в заданном диапазоне."""

def simple_number(minimum, maximum):
    return [i for i in range(minimum, maximum+1)]

"""3. Создать класс Point, который представляет собой точку в двумерном пространстве.
 Класс должен иметь методы для инициализации координат точки,
  вычисления расстояния до другой точки, а также для получения и изменения координат."""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_another_point(self, another_point):
        return math.sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

"""4. Написать программу, которая сортирует список строк по длине,
 сначала по возрастанию, а затем по убыванию."""

def string_sort(lst):
    increase = sorted(lst, key=len)
    decrease = sorted(lst, key=len, reverse=True)
    return increase, decrease
