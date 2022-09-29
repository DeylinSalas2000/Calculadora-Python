from operator import truediv



eleccion=0



while eleccion !=6:
    print("""Indique la operacion que desea realizar:
          1 Suma
          2 Resta
          3 Multiplicacion
          4 Division
          5 Cambio de numeros
          6 Palindromo
          7Salir """)
    
    eleccion = int (input())
    
    
    if eleccion ==1:
        
        numero1=int (input("Ingrese un numero:"))
        numero2=int (input("Ingrese otro numero:"))
        
        print("")
        print("Resultado:", numero1, "+", numero2,"=",  numero1+numero2 )
         
         
         
    if eleccion ==2:
        
        
        numero1=int (input("Ingrese un numero:"))
        numero2=int (input("Ingrese otro numero:"))
        
        print("")
        print("Resultado:", numero1, "-", numero2,"=",  numero1-numero2 )    
         
    if eleccion ==3:
              
         numero1=int (input("Ingrese un numero:"))
         numero2=int (input("Ingrese otro numero:"))
         
         print("")
         print("Resultado:", numero1, "*", numero2,"=",  numero1*numero2 )     
         
         
    if eleccion ==4:
        
         numero1=int (input("Ingrese un numero:"))
         numero2=int (input("Ingrese otro numero:"))
           
        
         print("")
         print("Resultado:", numero1, "/", numero2,"=",  numero1/numero2 )         
         
         
    if eleccion ==5:
          
     numero1=int (input("Ingrese un numero:"))
     numero2=int (input("Ingrese otro numero:")) 
     
     
    if eleccion ==6: 
     
    


     def esPalindromo(palabra):
      return palabra== palabra[:: -1]
     
     print("BIENVENIDO esta palabra es un Palimdromo? -(Escriba quit para salir).")
     palabra= " "
     comparacion= " "
     
    while True:
        
       print()
       palabra= input("Escriba una palabra:" )         
       comparacion = esPalindromo(comparacion )   
       
       
       if palabra =="quit":
         break
     
       if comparacion and palabra!="":
          print("")
          print(palabra.upper()+ "es Palindromo.")         
         
       if not comparacion :
          print("")
          print(palabra.upper()+ "no es Palindromo.")   
     
     
    print("Adios")
             
     
     
     
     


    if eleccion ==7:
     print(" Gracias por usar la calculadora")