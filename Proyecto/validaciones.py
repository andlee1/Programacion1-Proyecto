import re

def validar_dni(cad):
    '''
    pre: toma por parametro una cadena y determina el patron del xx.xxx.xxx
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "^[0-9]{8}$"
    return re.match(patron,cad) 
    
def validar_email(cad):
    '''
    pre: toma por parametro una cadena y determina un patron de mail
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "^[a-zA-Z0-9.-_+][^@]+@[a-zA-Z0-9]+\.[a-z]+$"
    return re.match(patron,cad)

def validar_telefono(cad):
    '''
    pre: toma por parametro una cadena y determina el patron del xxx-6
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "[0-9]{4}-[0-9]{6,}"
    return re.match(patron,cad)

def validar_id():
    flag = True
    while flag:
        try:
            num = int(input("ID: "))
            assert (num > 0), "Debe ser un numero entre 1 y 6"
            assert (num < 7), "Debe ser un numero entre 1 y 6"
            break
        except ValueError:
            print("Valor incorrecto, debe ser un numero entre 1 y 6")
        except AssertionError as er:
            print(er)
        except:
            print("Ha ocurrido un error")
    return num

def validar_precio(): 
    flag = True
    while flag:
        try:
            precio = int(input("Nuevo precio: "))
            assert (precio > 0), "El numero debe ser positivo"
            break
        except ValueError:
            print("El precio tiene que ser un numero entero positivo")
        except AssertionError as er:
            print(er)
        except:
            print("Ha ocurrido un error")
    return precio