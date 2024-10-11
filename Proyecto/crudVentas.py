import validaciones
def comprar_producto(diccionario, matriz_e,matriz_v):#Matriz de electrodomesticos y matriz de ventas
	'''
	pre: recibe diccionario, matriz y matriz vacia. pide mas datos
	pos: agrega listas a la matriz vacia y retorna multiples parametros
	'''
	#Datos y validaciones
	producto = validaciones.validar_id()
	cantidad = validaciones.validar_cantidad()
	conjunto_clientes = set(diccionario.keys())
	dni = input("DNI (XXXXXXXX): ")

	while not validaciones.validar_dni(dni) or dni not in conjunto_clientes:
		if dni not in conjunto_clientes:
			dni = input("Ingrese un dni existente: ")
		else:
			dni = input("Ingrese el formato correcto(XXXXXXXX): ")

	#Buscar la fila del producto por id
	for fila in matriz_e:
		if fila[0] == producto:			
			#Controlar stock
			if cantidad > fila[3]:
				print(f'No hay sufieciente stock solo quedan {fila[3]} unidades')
			else:
				fila[3] -= cantidad #Restar stock
				precio_total = fila[2] * cantidad

				matriz_v.append([
					diccionario[dni]['nombre'][:15],
					dni,
					fila[1][:8],
					cantidad,
					precio_total])
	
	return diccionario,matriz_e,matriz_v

def mostar_compras_cliente(matriz):
	'''
	pre: recibe matriz de ventas y pide clave dni
	pos: retorna matriz recortada cuando coincide la clave con elemento de la fila 
	'''
	dni = input("Ingrse su DNI:")
	while not validaciones.validar_dni(dni):
		print("Ingese un dni valido (XXXXXXXX): ")

	matriz_recortada = [] 
	for fila in matriz:
		if dni == fila[1]:
			matriz_recortada.append(fila)
	return matriz_recortada

def mostrar_ventas(matriz):
	'''
	pre: recibe una matriz
	pos: imprime de manera ordenada
	'''
	print(f'{"Nombre":^16} {"DNI" :^9} {"Producto" :^8} {"Cantidad" :^8} {"Precio":^7}')
	for nombre,dni,producto,cantidad,precio in matriz:
		print(f'{nombre:^16} {dni :^9} {producto :^8} {cantidad :^8} {precio:^7}')