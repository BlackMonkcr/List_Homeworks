from voz_Texto import *

ver_fal = [
           ["SI", "Si", "si", "SIU", "Siu", "siu", "SÍ", "Sí", "sí"],
           ["NO", "No", "no", "NOU", "Nou", "nou"]
          ]


interaccion = False
print("¿Quieres realizar alguna acción?")
continuar = reconocimiento_voz(10)

for afirmacion in ver_fal[0]:
    if continuar == afirmacion:
        interaccion = True
        print("¿Que quieres que hagamos por ti?")
        voz_text = reconocimiento_voz(30)

for negacion in ver_fal[1]:
    if continuar == negacion:
        interaccion = True
        print("Entendido, estaremos aqui cuando nos necesites ;)")

if continuar != None and interaccion == False:
    print("(Entrada invalida) Parece que no esta hablando con nosotros 👀...")

continuar.split()
print(continuar)
