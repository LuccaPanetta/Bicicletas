# Alquiler de bicicletas

Plazos_service_dict = {"playera": 60, "MTB": 45, "plegable": 90, "carrera": 30 }
Tipo_bici_set = {"playera", "MTB", "plegable", "carrera"}
Precio_diario = [4, 7.7, 11.2, 14.2, 17, 19.5, 21.7]  

import datetime
import calendar

class Bicicleta():
	def __init__ (self, codigo, tipo, fechacompra, fechaultimoservice):
		self.codigo = codigo
		self.tipo = tipo
		self.fechacompra = fechacompra 
		self.fechaultimoservice = fechaultimoservice
		self.disponible= True
	
	def get_disponibilidad(self):
			return (self.disponible)
			
	def get_tipo(self):
		return(self.tipo)

	def get_codigo(self):
		return(int(self.codigo))

	def get_fecha_ultimo_service(self):
		return(self.fechaultimoservice)

	def set_alquilar(self):
		self.disponible= False

	def set_devolver(self):
		self.disponible= True




Lista_Bicicletas=[]

# Proceso el archivo de bicicletas
bici_file=open("Bicicletas.txt", "r")
bici=bici_file.readline()
while len(bici) > 0:
	a,b,c,d,e = bici.split(';',5)
	c1, c2, c3=c.split("/", 2)
	d1, d2, d3=d.split("/", 2)
	fecha_compra=datetime.date(int(c3),int(c2),int(c1))
	print(fecha_compra)
	fecha_service=datetime.date(int(d3),int(d2),int(d1))
	Lista_Bicicletas.append(Bicicleta(a, b, fecha_compra, fecha_service))
	bici=bici_file.readline()
bici_file.close()

def alquilar_bici():
	cual=int(input("Qué bici querés alquilar? 320 a 384 "))
	orden=0
	while Lista_Bicicletas[orden].get_codigo() != cual:
		orden +=1
	disponible= Lista_Bicicletas[orden].get_disponibilidad()
	if disponible == True:
		Lista_Bicicletas[orden].set_alquilar()
		dias=int(input("Por cuántos días la querés?? "))
		if dias < 7:
			precio= Precio_diario[dias-1]
		else:
			precio=Precio_diario[6] + (dias-7) * 2
		print("Alquilada")
		print(" El importe a pagar es : " + str(precio) + "\n" )
	else:
		print("Esa bici no está disponible")
		
def devolver_bici():
	cual=int(input("Qué bici querés devolver? 320 a 384 "))
	orden=0
	while Lista_Bicicletas[orden].get_codigo() != cual:
		orden +=1
	disponible= Lista_Bicicletas[orden].get_disponibilidad()
	if disponible == False:
		Lista_Bicicletas[orden].set_devolver()
	else:
		print("Esa bici no está prestada!!")
		
def service():
	for i in range (len(Lista_Bicicletas)):
		dias=Plazos_service_dict[Lista_Bicicletas[i].get_tipo()]
		hoy=datetime.date.today()
		print(hoy)
		if (Lista_Bicicletas[i].get_fecha_ultimo_service() + datetime.timedelta(days=dias) ) < hoy:
			print("Service para la " + str( Lista_Bicicletas[i].get_codigo() ))


def disponibles_x_tipo():
	tipo=input("Tipo de bici")
	while tipo not in Tipo_bici_set:
		tipo=input("Ingresar tipo de bici válido")
	for i in range (len(Lista_Bicicletas)):
		if tipo == Lista_Bicicletas[i].get_tipo():
			if Lista_Bicicletas[i].get_disponibilidad() == True:
				print("Bici Disponible: " + str( Lista_Bicicletas[i].get_codigo() ))




# Opciones del programa
print("Qué querés hacer? \n 1- Alquilar bici \n 2 - Devolver bici \n 3 - Analizar service \n 4 - Ver cantidad disponibles por tipo \n  0 - Terminar")
opcion=int(input("Ingresá la opción numérica "))
while opcion != 0:
	if opcion == 1:
		alquilar_bici()
	elif opcion == 2:
		devolver_bici()
	elif opcion == 3:
		service()
	elif opcion == 4:
		disponibles_x_tipo()

	print("\n Qué querés hacer? \n 1- Alquilar bici \n 2 - Devolver bici \n 3 - Analizar service \n 4 - Ver cantidad disponibles por tipo \n  0 - Terminar")
	opcion=int(input("Ingresá la opción numérica "))

print("Terminé")
