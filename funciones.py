import os,time

def limpiar():
    """"Ejecuta un limpiar pantalla"""
    os.system("cls")

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
            pass
        elif opc=="2":
            pass
        elif opc=="3":
            pass
        elif opc=="4":
            print("Programa terminado...")
            break
        else:
            print("Opción incorrecta")
        time.sleep(3)


