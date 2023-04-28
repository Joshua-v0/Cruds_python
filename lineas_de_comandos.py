# importar libreria
from pathlib import Path
import calendar
import time
from datetime import datetime


l_arreglo = [] 
l_vendidos= []
path = Path.cwd()

def getNameFuction(ft):
    name = ft. __name__
    print("nombre:", name)

            
def clean_data(_item): 
    temp = _item.strip()
    temp = temp.capitalize()
    return temp

current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
date_time = datetime.fromtimestamp(time_stamp)


print(str(path))
# dir = "c:/Users/jvoitier/Desktop/programa/py.py"
dir =  str(path) + "/data/"
filename = dir + "usuario.txt"
filename_producto = dir + ""


def guardarArchivo(info):
    borrarEspacio = info.strip()
    tam = len(borrarEspacio)

    if tam > 0:
        f = open(filename, "a+")
        temp =  "\n" + info
        temp =  "\n" + info
        temp =  "\n" + info
        f.writelines(temp)
        f.close()
    else:
        print("No se puede almacenar información vacía")


def listadoUser():
    lista_temp = []
    # Leer
    with open(filename, "r+") as f:
        for item in f.readlines():
            borrarEspacio = item.strip()
            tam = len(borrarEspacio) 
            if tam > 0:
                info =  item.split(',')

                # Posicion 0 - usuario
                # Posicion 1 - password
                _nombre = info[0]
                tmp = info[1].split("\n")
                _password = tmp[0]

                # almacenando en lista
                lista_temp.append([_nombre, _password])
    f.close()
    return lista_temp



print("\t == Bienvenido al sistema de apps Internationals ==")
print("\nSign UP") 
usu = input("\nIngrese su usuario: ")
pw = input("\ningrese su password: ")   
hora = str(date_time)
ave = usu + "," + pw + "," + hora
guardarArchivo(ave)    
estado=False
loop = False
loop2 = False
nac = None
ce = None
num = None


print("\n\t == MENU PRINCIPAL == ")
print("\n Home")
input("\nPresione enter!")      
#opcion del uso de "mi perfil" 

loop = True
while loop == True:
    print("\n\t == Bienvenido a su perfil == ")
    print("\n1. Mi perfil")
    print("2. vender")
    print("3. comprar")
    print("4. Acerca de") 
    opc = int(input("\nEliga su opcion por favor: "))
    if opc == 1:
        print("\n\tBienvenido a su perfil")   
        print("\n1. Nacionalidad")
        print("2. Numero de telefono")
        print("3. Genero")
        print("4. Estado")
        print("5. Salir")
        op = int(input("\nIngrese una opcion: "))   
        #opcion para ingresar su nacionalidad 
        if op == 1 :
            if nac == None :
                nac = input("\ningrese su nacionalidad: ")
                ce = input("ingrese su cedula o pasaporte: ")     
                print("\nNacionalidad: ", nac)
                print("Cedula o Pasaporte: ", ce)
                input("\nPresione enter para continuar... ")  
            else: 
                print("\nNacionalidad: ", nac)
                print("Cedula o Pasaporte: ", ce) 
                
        #opcion para ingresar su numero de telefono
        elif op == 2:
            if num == None:
                num = input("\nIgrese su numero de telefono: ")
                print("Telefono: ", num)
                input("\nPresione enter para continuar") 
            else:
                print("Numero de telefono: ", num) 

        #opcion para ingresar su tipo de genero
        elif op == 3: 
            A = ""
            B = ""
            C = ""
            opc = ""
            gen = input("\nSexo: \n\nA. masculino \nB. Femenino \nC. Es personal \n\n( eleccione una letra por favor: ) \n-->: ") 
            if opc == A:
                print("Muchas gracias.") 
                input("\nPresione enter para continuar")
            elif opc == B:
                print("Perfecto.")
                input("\nPresione enter para continuar") 
            elif opc == C:
                print("Perfecto.")
                input("\nPresione enter para continuar")

        #opcion para ingresar su estado civil 
        elif op == 4:
            est = int(input("\nEstado civil: \n\n1. Soltero \n2. en una relacion \n3. Prefiero reservarmelo \n\nIngrese una opcion por favor.  \n-->: ")) 
            if est == 1:
                print("Soltero!")
                input("\nEnter para continuar")  
            elif est == 2:
                print("En una relacion!")
                input("\nEnter para continuar:", )
            elif est == 3: 
                print("Muchas gracias, respetamos su decision, que tenga buen dia.")
                input("\nPresione enter para continuar")

        elif op == 5:
            print("saliendo")

                

    #condicion y crud para la opcion vender 
    elif opc == 2:
        l_arreglo = [] 

        #funcion para crear producto 
        def add(_item):
            temp = _item.strip()
            temp = _item.capitalize() 
            l_arreglo.append(temp) 
            print("\nel producto se creo con éxito")  

        #funcion para editar un producto
        def editar_producto(producto):
            temp = producto.strip()
            temp = producto.capitalize()
            if temp in l_arreglo:
                l_arreglo.remove(temp)
                producto = input("Nuevo producto: ")  
                temp2 = producto.strip()
                temp2 = producto.capitalize()
                l_arreglo.append(temp2)   
                print("\nel producto se edito con exito!")  
            else:
                print("\nproducto no existe en la lista de productos")  
                    
                
        #funcion para listar un producto 
        def get(): 
            for _item in l_arreglo:
                print("_item")

        #funcion para consultar el producto 
        def update(_item): 
            getNameFuction(update) 
            if _item in l_arreglo:
                print("El producto si existe.")
            else:
                print("este producto no exite.")  

        #funcion para eliminar un producto
        def delete_comprar(_item):
            val = input("\nEsta seguro que desea eliminar el producto: SI O NO? ")
            temp = clean_data(val)
            if temp != "si":
                s_delete = clean_data(_item)
                if s_delete in l_arreglo:
                    l_arreglo.remove(s_delete)
                    print("eliminando..", s_delete)
                    get() 
                
        #partida en pyhton
        loop2 = True
        while loop2 == True:
            print("\n\t == Poductos a crear, listar, editar y eliminar == ")   
            print("\n1. Crear un producto.")
            print("2. Listar Productos.")
            print("3. editar un producto.")
            print("4. eliminar un producto.")
            print("5. Salir")
            opc = input("\n Eliga su opcion: ") 

            #creacion de producto
            if opc == "1":
                producto = ""
                cant_pro = 0
                contar = 0 
                cant_pro = int(input("\nIngrese la cantidad de productos a crear: ")) 
                for x in range(cant_pro):
                    contar = contar +1 
                    print("\nproducto #:", str(contar))
                    nom = input("Ingrese el nombre del producto: ")  
                    print("Nombre del producto: ", nom)   
                    add(nom)    
                    print("\nProductos creados con exito.")

            elif opc =="2":
                print(l_arreglo)

            elif opc=="3":
                producto = input("Producto que desea editar: ")
                editar_producto(producto)

            elif opc=="4":
                producto = input("Producto que desea eliminar: ")
                delete_comprar(producto)
            elif opc == "5":
                print("saliendo..")
                loop2 = False
            



            
        
    #funcion o opciones de compra del usuario
    elif opc == 3:
        l_compras = []
  
        
        #funcion para crear producto 
        def add(_item):
            temp = _item.strip()
            temp = _item.capitalize() 
            l_arreglo.append(temp) 
            print("\nel producto se creo con éxito")  

        #funcion para vender un producto 
        def editar_producto(producto):
            temp = producto.strip()
            temp = producto.capitalize()
            if temp in l_arreglo:
                l_arreglo.remove(temp)
                producto = input("nuevo producto: ")   
                temp2 = producto.strip()
                temp2 = producto.capitalize()
                l_arreglo.append(temp2)   
                print("\nel producto se modifico con exito!")    
            else:
                print("\nproducto no existe en la lista de productos")  
         
            
        
        #funcion para eliminar producto de la lista
        def delete_comprar(_item):
            val = input("\nEsta seguro que desea eliminar el producto: SI O NO? ")
            temp = clean_data(val)
            if temp != "si":
                s_delete = clean_data(_item)
                if s_delete in l_arreglo:
                    l_arreglo.remove(s_delete)
                    print("eliminando..", s_delete)
                    get() 

            
        #punto de partia 
        if __name__ == "__main__":
            print("\n == Productos de compras == ")
            print("\n1. Listar productos") 
            print("2. vender productos")
            print("3. modificar producto")
            print("4. eliminar producto")  
            print("5. Salir") 
            op = input("\nEliga su opcion: ")

            if op == "1":
                contar = 0
                nom = ""
                cant = 0
                num = int(input("\ningrese cantidad de productos a crear: ")) 
                for x in range(num):
                    contar = contar +1  
                    print("\nproducto #", str(contar))
                    nom = input("ingrese nombre del producto: ")
                    print("nombre del producto:",nom)
                    add(nom)  


            elif op == 3:
                vender = input("\nProducto que desea vender.")
                editar_producto(vender) 
 
            elif op == 4:
                producto = input("\nProducto que desea eliminar: ")
                delete_comprar(producto)


                     
                        

                    
    elif opc == 4:
        print("\n \t == Interfaz de lineas de comando ==")  
        print("\n 1. decripcion aprendida en clases: ")
        print("2. Mis datos.")
        print("3. lecciones aprendidas.")
        op = int(input("\n Ingrese una opcion: ")) 
        #uso de condicionales
        if op == 1:
            print("\n En este curso he aprendido el entendimiento logico al uso de la programacion, ser social, empatico, honesto, sincero conmigo mismo.")
        elif op == 2:
            print("\n \t  == datos == ")
            print("\n 1. Nombre: Joshua Voitier \n2. cedula: 8981689 \n3. Nacionalidad: Panama")
        elif op == 3:
            print(" \n \t == Lecciones Aprendidas ==")
            print("\n Vimos diferentes tipos de lecciones tales como: funciones, condicionales, repetitive, crud, bucles")


            

        
            

            


          
            
           




                
       



        
    

      
                    





            


    










    






        

    


          
    

























