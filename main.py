# Ejemplo básico en Python

def saludar(nombre):
    """Función que saluda a una persona"""
    return f"¡Hola, {nombre}!"

def sumar(a, b):
    """Función que suma dos números"""
    return a + b

if __name__ == "__main__":
    # Ejemplo de uso
    print(saludar("Mundo"))
    resultado = sumar(5, 3)
    print(f"La suma de 5 + 3 es: {resultado}")