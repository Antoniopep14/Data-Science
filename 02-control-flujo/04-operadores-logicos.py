# and, or, not
# todas estas se ejecutan de izq a der
# a menos que usemos () si hay varios () va de izq a der
# and es para evaluar que todo cumpla con la comparacion
# or evalua que se cumpla al menos una comparacion
# not evalua que no se cumpla la comparacion, es decir que sea false
gas = True  # cambniar a False para obtener otro resultado
encendido = True
edad = 18

if gas and encendido:
    print("puedes avanzar and")

gas = True  # cambniar a False para obtener otro resultado
encendido = False

if gas or encendido:
    print("puedes avanzar or")

# ahora los combinamos
gas = True  # cambniar a False para obtener otro resultado
encendido = True

if gas and encendido and edad > 17:
    print("puedes avanzar con edad")

gas = False  # cambiar a False para obtener otro resultado
encendido = True

if not gas and (encendido or edad > 17):  # se ponen () para
    # especificar cual va primero, lo de () se evalua primero
    # aun asi lo de afuera se debe de cumplir
    print("puedes avanzar con edad not")


# OPERADOR DE CORTO CIRCUITO
# si usamos mas un operador and y el primer and es falso
# lo que sigue a la derecha ya no lo va a evaluar
# porque arroja false
# lo mismo para varios "or"
# si el primer or da true ya no evalua los siguientes
