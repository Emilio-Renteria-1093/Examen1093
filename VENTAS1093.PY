print("\n")
print("EXAMEN 29/09/2024")
print("EMILIO GALE RENTERIA RAYO MTL: 22308051281093")

#CLASS ZONE
class ventas1093:
    # ATRIBUTE ZONE
    def __init__(self):
        self.id_ventas=0
        self.id_cliente=0
        self.fecha_venta=0
        self.id_empleado=0
        self.total=0
        self.impuesto=0
        self.producto_vendido=0
        self.cantidad_productos=0
        self.id_producto=0
        self.sucursal=0
        self.id_sucursal=0
        self.id_proveedor=0

    def mostrar_datos(self):
        print(f"id ventas: {self.id_ventas}")
        print(f"id clientes: {self.id_cliente}")
        print(f"fecha de ventas: {self.fecha_venta}")
        print(f"ID EMPLEADO: {self.id_empleado}")
        print(f"TOTAL: {self.total}")
        print(f"IMPUESTO: {self.impuesto}")
        print(f"PRODUCTOS VENDIDOS: {self.producto_vendido}")
        print(f"CANTIDAD DE PRODUCTOS: {self.cantidad_productos}")
        print(f"ID PRODUCTOS: {self.id_producto}")
        print(f"SUCURSAL: {self.sucursal}")
        print(f"ID SUCURSAL: {self.id_sucursal}")
        print(f"ID PROVEEDOR: {self.id_proveedor}")




    def mi_lista(self):
            listar_ventas =["telefono","camaras","televicion","computadoras","asistentes inteligentes"]
            for x in listar_ventas:
                print(x)

    def mi_tupla(self):
            tupla_ventas =("control","teCLado","mouse","monitor","cpu")
            for x in tupla_ventas:
                print(x)

    def mi_diccionario(self):
            diccionario_productos_cantidad ={
            "computadoras":100,
            "celulares":9,
            "tablets":10,
            "mouse":7,
            "teclados":8
            }
            for x,y in diccionario_productos_cantidad.items():
                print(x,y)

    def alta(self):
        print("la operacio de alta se realizo correctamente")


    def baja(self):
        print("la operacio de baja se realizo correctamente")



datos = ventas1093()

print("\n""-----------------------------------------""\n")
print("LISTADO DE NOMBRES DE OBJETOS A VENDER")
datos.mi_lista()

print("\n""-----------------------------------------""\n")
print("TUPLA DE NOMBRES DE VENTAS")
datos.mi_tupla()

print("\n""-----------------------------------------""\n")
print("DICCIONARIO DE INVENTARIO DE OBJETOS")
datos.mi_diccionario()

print("\n""-----------------------------------------""\n")
obj=ventas1093()
emilio=ventas1093()

obj.id_ventas= 10000
obj.id_cliente= 213
obj.fecha_venta= "24/09/2024"
obj.id_empleado= 4659
obj.total= 4552.20
obj.impuesto= "15%"
obj.producto_vendido= "uso comun"
obj.cantidad_productos= 20
obj.id_producto= 466213
obj.sucursal= "centro"
obj.id_sucursal= 4646966
obj.id_proveedor= 5549188

obj.mostrar_datos()

print("\n""-----------------------------------------""\n")
emilio.alta()
emilio.baja()

