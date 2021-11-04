import random

def numero_aleatorio():
    aleatorio = random.randint(1, 100)
    return aleatorio

def verificador(numero, aleatorio):
    if numero == aleatorio:
        return True
    else:
        return False

def run():
    aleatorio = numero_aleatorio()
    bienvenida = """
    
    Bienvenido al juego, competirás contra la máquina, debes adivinar un número del 1 al 100 para poder ganar ¡mucha suerte!

    
    """
    print(bienvenida)
    numero = int(input("Ingrese el número que usted crea que es correcto: "))
    if verificador(numero, aleatorio) == True:
        print("Usted ha ganado, el número es: " + str(aleatorio))
    else:
        print("Usted ha perdido, el número correcto era: " + str(aleatorio) + ", gracias por participar.")



if __name__ == '__main__':
    run()