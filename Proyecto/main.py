import crudElectr
import crudCliente
import crudVentas

#Programa Principal
archivo_productos = r'Proyecto\electro.txt'
archivo_clientes = r'Proyecto\cliente.json'
archivo_ventas = r'Proyecto\ventas.txt'

semaforo_main = True
while semaforo_main:
    semaforo_crud = True
    try:
        ingreso = int(input("1-Stock 2-Clientes 3-Ventas (-1)Salir: "))  # Administrar datos
        if ingreso not in [-1,1,2,3]:
            print("Ingrese una opcion valida")
            continue
    except ValueError:
        print("Ingrse un caracter numerico")
        continue
    except:
        print("Ha ocurrido un error")
        continue

    if ingreso == -1:
        print("Finalizando Programa...")
        semaforo_main = False  # Termina el programa si el usuario ingresa -1
    
    if ingreso == 1:  # Gestión de datos (stock de electrodomésticos)
        while semaforo_crud:
            # C.R.U.D de stock
            print()
            print("1-Ingresar un nuevo stock")
            print("2-Imprimir matriz")
            print("3-Actualizar precio")
            print("4-Eliminar un stock")
            print("5-Ordenar por precio")
            print("6-Agregar nuevo producto")
            print("7-Eliminar producto")
            print("8-Sumar stock")

            try:
                opcion = int(input("(-1) Volver al menú principal "))  # Administrar datos
                print()
                if opcion not in [-1,1,2,3,4,5,6,7,8]:
                    print("Ingrese una opcion valida")
                    continue
            except ValueError:
                print("Ingrse un caracter numerico")
                continue
            except:
                print("Ha ocurrido un error")
                continue

            if opcion == -1:
                semaforo_crud = False  # Volver al menú principal
            if opcion == 1:
                crudElectr.agregar_stock(archivo_productos)
            if opcion == 2:
                crudElectr.leer(archivo_productos) 
            if opcion == 3:
                crudElectr.actualizar_precio(archivo_productos)
            if opcion == 4:
                electrodomesticos = crudElectr.eliminar(archivo_productos)
            if opcion == 5:
                crudElectr.ordenar(archivo_productos)
            if opcion == 6:
                crudElectr.agregar_producto(archivo_productos)
            if opcion == 7:
                crudElectr.eliminar_producto(archivo_productos)
            if opcion == 8:
                total_stock = crudElectr.suma_stock(archivo_productos)
                print(f'El total de stock es {total_stock}')
       
    if ingreso == 2:  # Gestión de clientes
        while semaforo_crud:
            # C.R.U.D de Clientes
            print()
            print("1-Nuevo cliente")
            print("2-Imprimir matriz clientes")
            print("3-Actualizar email-telefono")
            print("4-Eliminar cliente")
            try:
                opcion_cliente = int(input("(-1) Volver al menú principal "))
                print()
                if opcion_cliente not in [-1,1,2,3,4]:
                    print("Ingrese una opcion valida")
                    continue
            except ValueError:
                print("Ingrse un caracter numerico")
                continue
            except:
                print("Ha ocurrido un error")
                continue

            if opcion_cliente == -1:
                semaforo_crud = False  # Volver al menú principal
            if opcion_cliente == 1:
                crudCliente.crear(archivo_clientes)
            if opcion_cliente == 2:
                crudCliente.leer(archivo_clientes)
            if opcion_cliente == 3:
                crudCliente.actualizar_cliente(archivo_clientes)
            if opcion_cliente == 4:
                crudCliente.eliminar(archivo_clientes)
    
    if ingreso == 3:
        while semaforo_crud:
            print()
            print("1-Comprar producto")
            print("2-Mostrar historial por cliente")
            print("3-Mostrar historial de todas las compras")
            try:
                opcion_ventas = int(input("(-1) Salir "))
                print()
                if opcion_ventas not in [-1,1,2,3]:
                    print("Ingrese una opcion valida")
                    continue
            except ValueError:
                print("Ingrse un caracter numerico")
                continue
            except:
                print("Ha ocurrido un error")
                continue
            if opcion_ventas == -1:
                semaforo_crud = False
            if opcion_ventas == 1:
                #Capturar valores
                crudVentas.comprar_producto(archivo_productos, archivo_clientes, archivo_ventas)
            if opcion_ventas == 2:
                ventas_cliente = crudVentas.mostar_compras_cliente(archivo_ventas)
                if len(ventas_cliente) == 0:
                    print("Este DNI no realizo ninguna compra ")
                else:
                    print(f'{"Nombre":^15} {"DNI":^9} {"Producto":^10} {"Cantidad":^10} {"Precio":^8}')
                    for nombre, dni, producto, cantidad, precio_total in ventas_cliente:
                        print(f'{nombre:^15} {dni:^9} {producto:^10} {cantidad:^10} {precio_total:^8}')
            if opcion_ventas == 3:
                crudVentas.mostrar_ventas(archivo_ventas)
