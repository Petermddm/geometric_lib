# Geometric Library

## Общее описание решения
Geometric Library - библиотека с функциями для вычисления площади и периметра различных фигур.

## Описание функций

### [**circle.py**](../circle.py)

#### **area(r)**
    Возвращает площадь окружности с радиусом r
        Параметры:
          -  r (int): радиус окружности
        Возвращаемое значение:
          -  area (float): площадь окружности
**Пример вызова:**
```python
from circle import area
#Вычисление площади окружности с радиусом 5
res = area(5)
print(res)  #78.53981633974483
```
#### **perimeter(r)**
    Возвращает длину окружность с радиусом r
        Параметры:
          -  r (int): радиус окружности
        Возвращаемое значение:
          -  perimeter (float): длина окружности
**Пример вызова:**
```python
from circle import perimeter
#Вычисление длины окружности с радиусом 5
res = perimeter(5)
print(res)  #31.41592653589793
```
## [**rectangle.py**](../rectangle.py)

#### **area(a,b)**
    Возвращает площадь прямоугольника со сторонами a и b
        Параметры:
          -  a (int): первая сторона прямоугольника
          -  b (int): вторая сторона прямоугольника
        Возвращаемое значение:
          -  area (int): площадь прямоугольника
**Пример вызова:**
```python
from rectangle import area
#Вычисление площади прямоугольника со сторонами 5 и 3
res = area(5,3)
print(res)  #15
```
#### **perimeter(a,b)**
    Возвращает периметр прямоугольника со сторонами a и b
        Параметры:
          -  a (int): первая сторона прямоугольника
          -  b (int): вторая сторона прямоугольника
        Возвращаемое значение:
          -  area (int): периметр прямоугольника
**Пример вызова:**
```python
from rectangle import perimeter
#Вычисление периметра прямоугольника со сторонами 5 и 4
res = perimeter(5,3)
print(res)  #16
```
## [**square.py**](../square.py)

#### **area(a)**
    Возвращает площадь квадрата со стороной a
        Параметры:
          -  a (int): сторона квадрата
        Возвращаемое значение:
          -  area (int): площадь квадрата
**Пример вызова:**
```python
from square import area
#Вычисление площади квадрата со стороной 5
res = area(5)
print(res)  #25
```
#### **perimeter(a)**
   Возвращает периметр квадрата со стороной a
        Параметры:
          -  a (int): сторона квадрата
        Возвращаемое значение:
          -  area (int): периметр квадрата
**Пример вызова:**
```python
from square import perimeter
#Вычисление периметра квадрата со стороной 5
res = perimeter(5)
print(res)  #20
```
## [**triangle.py**](../triangle.py)

#### **area(a,h)**
    Возвращает площадь треугольника с основанием a и высотой h
        Параметры:
          -  a (int): основание треугольника
          -  h (int): высота треугольника
        Возвращаемое значение:
          -  area (int): площадь треугольника
**Пример вызова:**
```python
from triangle import area
#Вычисление площади треугольника с основанием 5 и высотой 4
res = area(5,4)
print(res)  #10
```
#### **perimeter(a,b,c)**
    Возвращает периметр треугольника со сторонами a,b,c
        Параметры:
          -  a (int): первая сторона треугольника
          -  b (int): вторая сторона треугольника
          -  c (int): третья сторона треугольника
        Возвращаемое значение:
          -  area (int): периметр треугольника
**Пример вызова:**
```python
from triangle import perimeter
#Вычисление периметра треугольника со сторонам 5,4,3
res = perimeter(5,4,3)
print(res)  #12
```
## История изменения проекта

### commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
    Author: smartiqa <info@smartiqa.ru>
    Date:   Thu Mar 4 14:54:08 2021 +0300
    L-03: Circle and square added
### commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
    Author: smartiqa <info@smartiqa.ru>
    Date:   Thu Mar 4 14:55:29 2021 +0300
    L-03: Docs added
### commit 13f9d58489846f5dde6661114b51a2aa28e4c48c
    Author: Petr Miliukov <allo.pitt@gmail.com>
    Date:   Tue Oct 14 00:10:02 2025 +0300
    add rectangle.py
### commit b979454b8d798fcfdd7f39995432bfad20e78238
    Author: Petr Miliukov <allo.pitt@gmail.com>
    Date:   Tue Oct 14 00:11:04 2025 +0300
    add triangle.py
### commit 92388b740ab44bdd99f797ae3201e74e793b432f
    Author: Petr Miliukov <allo.pitt@gmail.com>
    Date:   Tue Oct 14 00:12:58 2025 +0300
    Fix rectangle.py perimetr calculation
# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle P = a + b + c