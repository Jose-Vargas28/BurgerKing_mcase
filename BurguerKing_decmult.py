print(" ****** BIENVENIDO AL BURGER KING ********\n")
print("Ingrese los datos para la factura electrónica\n\n")
nombreCliente=input("Ingrese su nombre: ")
numeroCedula=int(input("Ingrese su número de cédula: "))
correo=input("Ingrese su correo: ")
numHamburguesas=int(input("Ingrese el número de hamburguesas a adquirir: "))
print()
print("Ingrese el tipo de hamburgesa que desea adquirir: ")
print("1) sencilla")
print("2) doble")
print("3) triple")
opcion=int(input("Ingrese la opción: "))

match opcion:
    case 1: 
        precio = numHamburguesas * 1.50
        print("Ingrese su forma de pago")
        print("1) Tajeta de crédito")
        print("2) Efectivo")
        pago = int(input("Ingrese la opción: "))
        match pago:
            case 1:
                recargo = precio * 0.05
                pf = precio + recargo
                print()
                print(f"Genial, {nombreCliente} el precio final a pagar es de: ${round(pf,2)}")
                print(f"La factura se enviará a su correo {correo}")
            case 2:
                print()
                print(f"Genial, {nombreCliente} el precio final a pagar es de: ${round(precio,2)}")
                print(f"La factura se enviará a su correo {correo}")
            case _:
                print("No existe esa opción")         
    case 2:
        precio = numHamburguesas * 2.50
        print("Ingrese su forma de pago")
        print("1) Tajeta de crédito")
        print("2) Efectivo")
        pago = int(input("Ingrese la opción: "))
        match pago:
            case 1:
                recargo = precio * 0.05
                pf = precio + recargo
                print()
                print(f"Genial, {nombreCliente} el precio final a pagar es de: ${round(pf,2)}")
                print(f"La factura se enviará a su correo {correo}")
            case 2:
                print()
                print(f"Genial, {nombreCliente} el precio final a pagar es de: ${round(precio,2)}")
                print(f"La factura se enviará a su correo {correo}")
            case _:
                print("No existe esa opcion")
                print("Muchas gracias por visitarnos")      
    case 3:
        precio = numHamburguesas * 3.25
        print("Ingrese su forma de pago")
        print("1) Tajeta de crédito")
        print("2) Efectivo")
        pago = int(input("Ingrese la opción: "))
        match pago:
            case 1:
                recargo = precio * 0.05
                pf = precio + recargo
                print()
                print(f"Genial, {nombreCliente} el precio final a pagar es de: ${round(pf,2)}")
                print(f"La factura se enviará a su correo {correo}")
            case 2:
                print()
                print(f"Genial, {nombreCliente} el precio final a pagar es de: ${round(precio,2)}")
                print(f"La factura se enviará a su correo {correo}")  
            case _:
                print("No existe esa opción")
                print("Muchas gracias por visitarnos")      
    case _:
        print("No existe esa opción")
        print("Muchas gracias por visitarnos")  
       