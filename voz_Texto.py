import speech_recognition as sr

def reconocimiento_voz():
    r = sr.Recognizer()  #recognizer

    with sr.Microphone() as source:

        #Ajusta el Audio
        r.adjust_for_ambient_noise(source, duration=1)

        #Inicia la grabacion
        print("Puedes hablar:")
        audio = r.listen(source)
        print("-")


    #Pasar de audio a texto
    try:
        texto = r.recognize_google(audio,language="es-PE")

        print("\nResultado: {} \n".format(texto))

    except sr.UnknownValueError:
        print("No ha dicho nada o no se le entendió")
        texto = "E-UKV"
    except sr.RequestError as e:
        print("Google no respondió")
        texto = "E-NR"


    #retorna el texto
    return texto