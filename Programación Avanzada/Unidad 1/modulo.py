import numpy as np

# Funciones que aceptan listas de valores y devuelven resultados en forma de lista
def f(x_list):
    return [x**2 for x in x_list]  # Función cuadrática para una lista de valores

def g(x_list, y_list):
    return [np.sin(x) * np.cos(y) for x, y in zip(x_list, y_list)]  # Función g(x, y) = sin(x) * cos(y)

def h(x_list, y_list, z_list):
    return [x * y * z for x, y, z in zip(x_list, y_list, z_list)]  # Multiplicación de tres listas (element-wise)

# Clase Funcion
class Funcion:
    def __init__(self, nombre, funcion):
        self.nombre = nombre
        self.funcion = funcion

    def evaluar(self, *valores):
        # Evaluar la función con las listas de valores
        return self.funcion(*valores)

# Ejemplo de uso
if __name__ == "__main__":
    # Definir funciones
    f_func = Funcion("f", f)
    g_func = Funcion("g", g)
    h_func = Funcion("h", h)
    
    # Listas de valores de entrada
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    
    # Evaluar funciones
    print(f_func.evaluar(x))  # f(x) = x^2
    print(g_func.evaluar(x, y))  # g(x, y) = sin(x)*cos(y)
    print(h_func.evaluar(x, y, z))  # h(x, y, z) = x*y*z
