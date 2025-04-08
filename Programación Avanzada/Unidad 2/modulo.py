import time
import matplotlib.pyplot as plt
import math

class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'({self.x},{self.y})'
    
    def __call__(self, escalar):
        return Punto2D(self.x * escalar, self.y * escalar)
    
    def __add__(self, other):
        return Punto2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Punto2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, escalar):
        return Punto2D(self.x * escalar, self.y * escalar)
    
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def grafica(self):
        plt.scatter(self.x, self.y, color='red', label=f'P({self.x},{self.y})')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.title('Gráfica del Punto')
        plt.legend()
        plt.show()
    
    @staticmethod
    def tiempo_de_ejecucion(func):
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fin = time.time()
            print(f'Tiempo de ejecución: {fin - inicio:.6f} segundos')
            return resultado
        return wrapper
    
    @tiempo_de_ejecucion
    def distancia(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
