#los errores pueden ser de sintaxis, operaciones que no pueden hacerse (como dividir un numero entre 0)
# mezclar tipos de variables, asignar valores a objetos estaticos como tuplas
#declaracion de variables cuando se necesiten
#errores logicos: se solucionan por depuracion de codigo
#puede ser usar operadores de manera incorrecta
#tambien se incluyen los bucles infinitos
#MANEJO DE EXCEPCIONES
#son indicaciones para manejar los tipos de error
#y pueden ser generales o unicas, su prioridad se define de arriba a abajo

x=9
y=0
try:
    z = x/y
except ZeroDivisionError:
    print("no se permite la division entre cero")
except ValueError:
    print("algun valor es erroneo")
except:
    print("no se realizo la operación")

else:
    print(z,"\nla operacion se realizo")

