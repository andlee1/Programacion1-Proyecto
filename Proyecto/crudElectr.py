import validaciones
from crudVentas import crear_matriz

def agregar_producto(archivo):
    try:
        with open(archivo, 'r') as arch:
            matriz = [linea.strip().split(';') for linea in arch]
        id = int(matriz[-1][0]) + 1
        producto = input("Ingrese nombre producto: ")
        precio = validaciones.validar_precio()
        stock = validaciones.validar_cantidad()
        matriz.append([str(id),producto,str(precio),str(stock)])
    except FileNotFoundError:
          print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
          print("Ha ocurrido un error")

    try:
        with open(archivo, 'w') as arch:
            for fila in matriz:
                linea = ';'.join(fila) + '\n'
                arch.write(linea)
    except FileNotFoundError:
          print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
          print("Ha ocurrido un error")

def eliminar_producto(archivo):
    try:
        with open(archivo, 'r') as arch:
            matriz = [linea.strip().split(';') for linea in arch]
        lista_id = [int(i[0]) for i in matriz]
        print("Producto a eliminar")
        id = validaciones.validar_id()
        while id not in lista_id:
            id = validaciones.validar_id()
        for i in matriz:
            if str(id) == i[0]:
                matriz.remove(i)
    except FileNotFoundError:
          print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
          print("Ha ocurrido un error")

    try:
        with open(archivo,'w') as arch:
            for i in matriz:
                linea = ';'.join(i) + '\n'
                arch.write(linea)
    except FileNotFoundError:
          print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
          print("Ha ocurrido un error")
    
def agregar_stock(archivo):
    '''
    pre: recibe el nombre del archivo.
    pos: actualiza el archivo incrementando el stock en 1.
    '''
    id = validaciones.validar_id()
    lista_id = []
    lista_linea = []
    try:
        with open(archivo, 'r') as arch: #cierra archivo automaticamente
            for linea in arch:
                datos = linea.strip().split(';') #Elimino \n y separo por ; que encuentre
                lista_id.append(int(datos[0]))
                if int(datos[0]) == id:
                    datos[3] = str(int(datos[3]) + 1)  # Incrementa el stock
                    linea = ';'.join(datos) + '\n' #Vuelvo a agregar lo que elimine
                lista_linea.append(linea)
    except FileNotFoundError:
          print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
    finally:
        print("Stock incrementado" if id in lista_id else "No se encontro el ID")
    try:
        with open(archivo, 'w') as arch:
            for linea in lista_linea:
                arch.write(linea)  # Escribo de nuevo el archivo
    except:
        print("Ha ocurrido un error")

def leer(archivo):
    '''
    pre: recibe el nombre del archivo.
    pos: imprime la información del archivo de manera formateada.
    '''
    print(f'{"ID":^4} {"Nombre":^6} {"Precio":^8} {"Stock":^5}')
    try:
        with open(archivo, 'r') as arch:
            for linea in arch:
                id, nombre, precio, stock = linea.strip().split(';') 
                print(f'{id:^4} {nombre[:5]:^6} {precio:^8} {stock:^5}')
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
        
def actualizar_precio(archivo):
    '''
    pre: recibe el nombre del archivo.
    pos: actualiza el precio de un producto.
    '''
    id = validaciones.validar_id()
    nuevo_precio = validaciones.validar_precio()
    lista_linea = []
    try:
        with open(archivo, 'r') as arch: 
            for linea in arch:
                datos = linea.strip().split(';')
                if int(datos[0]) == id:
                    datos[2] = str(nuevo_precio)  # Actualiza el precio
                    linea = ';'.join(datos) + '\n'
                lista_linea.append(linea)
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
    
    try:
        with open(archivo,"w") as arch:
            for linea in lista_linea:
                arch.write(linea)
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
    finally:
        print("Precio actualizado")
def eliminar(archivo):
    '''
    pre: recibe el nombre del archivo.
    pos: decrementa el stock en 1.
    '''
    id = validaciones.validar_id()
    lista_linea = []
    try:
        with open(archivo, 'r') as arch:
            for linea in arch:
                datos = linea.strip().split(';')
                if int(datos[0]) == id:
                    datos[3] = str(int(datos[3]) - 1)  # Decrementa el stock
                    linea = ';'.join(datos) + '\n'
                lista_linea.append(linea)
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
    
    try:
        with open(archivo, 'w') as arch:
            for linea in lista_linea:
                arch.write(linea)  # Escribo de nuevo el archivo
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")
    finally:
        print("Producto eliminado")

def ordenar(archivo):
    '''
    pre: recibe el nombre del archivo.
    pos: imprime los productos ordenados por precio en orden descendente.
    '''
    try:
        with open(archivo, 'r') as arch:
            lista_linea = [linea.strip().split(';') for linea in arch]
            lista_ordenada = sorted(lista_linea, key=lambda x: int(x[2]), reverse=True)
    except FileNotFoundError:
        print("El archivo no existe")
    except OSError:
        print("No se pudo abrir el archivo")
    except:
        print("Ha ocurrido un error")

    print(f'{"ID":^4} {"Nombre":^6} {"Precio":^8} {"Stock":^5}')
    for id, nombre, precio, stock in lista_ordenada:
        print(f'{id:^4} {nombre[:5]:^6} {precio:^8} {stock:^5}')

def suma_stock(archivo): 
    with open(archivo,'r') as arch:
        matriz = [linea.strip().split(';') for linea in arch]
    lista_int = [int(i[3]) for i in matriz]

    def suma_recursiva(lista):
        # Caso base
        if len(lista) == 0:
            return 0
        # Caso recursivo:
        return lista[0] + suma_recursiva(lista[1:])
    
    return suma_recursiva(lista_int)