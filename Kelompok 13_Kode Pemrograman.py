import numpy as np
from scipy.interpolate import lagrange
from sympy import symbols, diff, integrate

# Akar (Metode Newton-Raphson):
def akar_kuadrat(x):
    epsilon = 1e-6
    max_iter = 100
    guess = x / 2.0

    for i in range(max_iter):
        guess = (guess + x / guess) / 2.0
        if abs(guess**2 - x) < epsilon:
            return guess

    return guess

# SPL (Sistem Persamaan Linear):
def spl_solver(coefficients, constants):
    solution = np.linalg.solve(coefficients, constants)
    return solution

# Interpolasi (Metode Lagrange):
def lagrange_interpolasi(x_points, y_points):
    polynomial = lagrange(x_points, y_points)
    return polynomial

# Turunan:
def hitung_turunan(expression, variable):
    derivative = diff(expression, variable)
    return derivative

# Integral:
def hitung_integral(expression, variable):
    integral_result = integrate(expression, variable)
    return integral_result

# Contoh penggunaan:
# Akar
angka = 25
akar = akar_kuadrat(angka)
print(f"Akar kuadrat dari {angka} adalah: {akar}")

# SPL
coefficients = np.array([[2, 3], [1, -2]])
constants = np.array([8, -3])
hasil_spl = spl_solver(coefficients, constants)
print("Solusi SPL:")
print(hasil_spl)

# Interpolasi
x_points = [1, 2, 4]
y_points = [3, 5, 2]
polynomial = lagrange_interpolasi(x_points, y_points)
print("Polinomial interpolasi:")
print(polynomial)

# Turunan
x = symbols('x')
expression_turunan = x**2 + 3*x + 2
derivative = hitung_turunan(expression_turunan, x)
print(f"Turunan dari {expression_turunan} adalah: {derivative}")

# Integral
integral_result = hitung_integral(expression_turunan, x)
print(f"Integral dari {expression_turunan} adalah: {integral_result}")
