try:
     
     c = int(input("Ingrese un valor: "))
     c/0 
except ValueError:
     print("ERROR  INGRESE UN NUMERO")       
except Exception as c:
    print(type(c).__name__) #CON ESTO MOSTRAMOS EL NOMBRE DEL ERROR

