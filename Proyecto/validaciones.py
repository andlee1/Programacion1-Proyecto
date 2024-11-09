import re

def validar_dni(cad):
    '''
    pre: toma por parametro una cadena y determina el patron del xx.xxx.xxx
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "^[0-9]{8}$"
    if re.match(patron,cad):
        return True
    else:
        return False 
    
def validar_email(cad):
    '''
    pre: toma por parametro una cadena y determina un patron de mail
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "^[a-zA-Z0-9.-_+][^@]+@[a-zA-Z0-9]+\.[a-z]+$"
    if re.match(patron,cad):
        return True
    else:
        return False

def validar_telefono(cad):
    '''
    pre: toma por parametro una cadena y determina el patron del xxx-6
    pos: devuelve True si encuentra (match) y False si no
    '''
    patron = "[0-9]{4}-[0-9]{6,}"
    if re.match(patron,cad):
        return True
    else:
        return False

def validar_id():
    while True:
        try:
            num = int(input("ID: "))
            assert (num > 0), "Debe ser un positivo"
            break #Salir del ciclo
        except ValueError:
            print("Valor incorrecto, debe ser un numero")
        except AssertionError as er:
            print(er)
        except:
            print("Ha ocurrido un error")
    return num

def validar_precio(): 
    while True:
        try:
            precio = int(input("Nuevo precio: "))
            assert (precio > 0), "El numero debe ser positivo"
            break #Salir del ciclo
        except ValueError:
            print("El precio tiene que ser un numero")
        except AssertionError as er:
            print(er)
        except:
            print("Ha ocurrido un error")
    return precio

def validar_cantidad():
    while True:
        try:
            num = int(input("Cantidad: "))
            assert (num > 0), "El numero debe ser mayor o igual a 1"
            break #Salir del ciclo si no hay error
        except AssertionError as e:
            print(e)
        except ValueError:
            print("Debe ingresar un numero")
        except:
            print("Ha ocurrido un error")
    return num