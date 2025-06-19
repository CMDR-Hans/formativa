#agregar import necesarios
import os,time

def limpiar():
    """"Ejecuta un limpiar pantalla"""
    os.system("cls")

#Variables por usar
compras=[]
tipos=('G','V')
    
def menu():
    menu="""MENU PRINCIPAL
1. Comprar entrada
2. Consultar comprador
3. Cancelar compra
4. Salir"""
    while True:
        limpiar()
        print(menu)
        opc=input("Ingrese opción: ")
        limpiar()

        if opc=="1":
            comprar_entrada()
        elif opc=="2":
            consultar_compra()
        elif opc=="3":
            cancelar_compra()
        elif opc=="4":
            print("Programa terminado...")
            break
        else:
            print("Opción incorrecta")
        time.sleep(3)


def comprar_entrada():
    print("COMPRAR ENTRADA")
    nombre=validar_nombre("Ingrese nombre del comprador: ")
    tipoE=validar_tipo()
    codigo=input("Ingrese código: ")

    compra={
        "nombre":nombre,
        "tipo":tipoE,
        "codigo":codigo
    }
    compras.append(compra)
    print("¡Entrada registrada con éxito!")

def consultar_compra():
    print("CONSULTAR COMPRADOR")
    nombre=validar_nombre("Ingrese nombre del comprador a buscar: ")
    for c in compras:
        if nombre==c["nombre"]:
            print(f"Tipo de entrada: {c["tipo"]}, Código: {c["codigo"]}")
            return
    print("Nombre no registrado")        

def cancelar_compra():
    print("CANCELAR COMPRA")
    nombre=validar_nombre("Ingrese nombre del comprador a cancelar compra: ")
    for c in compras:
        if nombre==c["nombre"]:
            compras.remove(c)
            print("¡Compra cancelada!")
            return
    print("Nombre no encontrado")


#validaciones: nombre, codigo, tipo, lista no vacia
    
def validar_nombre(mensaje: str):
    while True:
        nombre=input(mensaje).strip().title()
        if len(nombre)>=3 and nombre.isalpha():
            return nombre
        print("Error! el nombre mínimo 3 letras!")


def validar_tipo():
    while True:
        tipo=input("Ingrese tio de entrada (G:general, V:Vip): ").upper()
        if tipo in tipos:
            return tipo
        print("Error! El tipo de debe ser G(general) o V(vip)!")


def validar_codigo():
    pass
def validar_lista_vacia():
    pass
def validar_nombre_existente():
    pass

