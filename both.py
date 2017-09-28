import sys
import os
import time

def bien(entrada, nombre):
    if(estas=="bien"):
        print("Que bueno que te encuentres bien, me haces feliz a mi :)")
        return 1
    elif(estas=="mal"):
        resp=raw_input("Por que te sientes mal? ")
        print("Que mal que te encuentres asi, me siento triste :(")
        print("Animo "+nombre)
        return 1
    else:
        print("No entendi a tu respuesta, podrias reponder bien o mal :/")
        return 2


#main
sigue="si"
while (sigue=="si"):
    nombre = raw_input("Hola, mi nombre es Both, cual es tu nombre? ")
    print("Hola "+nombre)
    estas=raw_input("Como estas? ")
    while(bien(estas, nombre)==2):
        estas=raw_input("Como estas? ")
    edad=raw_input("Cuantos anios tienes? ")
    while(edad.isdigit()==False):
        print("Esa no es una edad, vuelve a intentarlo.")
        edad=raw_input("Cuantos anios tienes? ")

    lugar=raw_input("Donde vives? ")
    print("Bonito Lugar.")
    bandera=1
    while(bandera==1):
        gusta=raw_input("Te gusta alguien? ")
        if (gusta=="si"):
            crush=raw_input("Y como se llama? ")
            print("awww :3")
            bandera=2
        elif(gusta=="no"):
            crush=raw_input("Por que no te gusta nadie? ")
            bandera=2
        else:
            print("soy muy tonto, no entiendi lo que me escribiste, podrias reponder si o no.")
            bandera=1

    resumen=raw_input("Te gustaria que te de un resumen? ")
    if(resumen=="si"):
        print("Bien, pensare en lo que me contastes... \n\n")
        time.sleep(3)
        print("Tu nombre es: "+nombre+", tienes: "+edad+" anios.")
        print("Vives en: "+ lugar)
        if(gusta=="si"):
            print("Te gusta algien y se llama: "+crush)
        elif(gusta=="no"):
            print("No te gusta nadie y los motivos no te los dire.")
        cierto=raw_input("\nEstoy en lo cierto? ")
        if(cierto=="si"):
            print("soy un genio :)")
        elif(cierto=="no"):
            print("\nComo que estoy mal, un both nunca se equivoca, solamente se equivoca si el programador hizo un error")
            print("si se equivoco, dale un golpe al programador XD\n")
        
        #imprime todo
    else:
        print("Ok, no te dire nada")

    sigue=raw_input("Deseas continuar? ")
    if(sigue=="si"):
        os.system("cls")

    elif(sigue=="no"):
        print("adios")
        time.sleep(3)
        sys.exit(1)




    
