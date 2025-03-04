from math import sqrt, pi

print("Введите радиус круга (см):")
radius_cm = float(input())
diagonal_cm = radius_cm * 2

circle_length_cm = 2 * pi * radius_cm
circle_length_m = circle_length_cm / 100
print("Длина окружности (см):", circle_length_cm)
print("Длина окружности (м):", circle_length_m)

circle_area_cm = pi * radius_cm * radius_cm
circle_area_m = circle_area_cm / 10000
print("Площадь круга (см^2):", circle_area_cm)
print("Площадь круга (м^2):", circle_area_m)

square_side_cm = diagonal_cm / sqrt(2) # d = a * sqrt(2)
square_side_m = square_side_cm / 100
print("Сторона вписанного квадрата (см):", square_side_cm)
print("Сторона вписанного квадрата (м):", square_side_m)

triangle_side_cm = radius_cm * 3 / sqrt(3) # R = a * sqrt(3) / 3
triangle_side_m = triangle_side_cm / 100
print("Сторона вписанного правильного треугольника (см):", triangle_side_cm)
print("Сторона вписанного правильного треугольника (м):", triangle_side_m)

diagonal_m = diagonal_cm / 100
print("Сторона описанного квадрата (см):", diagonal_cm)
print("Сторона описанного квадрата (м):", diagonal_m)

print("Сторона правильного треугольника, описывающего окружность (см):", triangle_side_cm / 2) # r = a * sqrt(3) / 6
print("Сторона правильного треугольника, описывающего окружность (м):", triangle_side_m / 2)

regular_octagon_side_cm = radius_cm * 2 / (1 + sqrt(2)) # r = a / 2 * (1 + sqrt(2))
regular_octagon_side_m = regular_octagon_side_cm / 100
print("Сторона Правильного восьмиугольника, описывающего окружность (см):", regular_octagon_side_cm)
print("Сторона Правильного восьмиугольника, описывающего окружность (м):", regular_octagon_side_m)