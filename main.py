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

    # Función para multiplicar dos números
    def multiplicar(a, b):
        """Función que multiplica dos números"""
        return a * b
    
    # Función para obtener el cuadrado de un número
    def cuadrado(n):
        """Función que calcula el cuadrado de un número"""
        return n ** 2
    
    # Ejemplos adicionales
    print(f"La multiplicación de 5 * 3 es: {multiplicar(5, 3)}")
    print(f"El cuadrado de 4 es: {cuadrado(4)}")