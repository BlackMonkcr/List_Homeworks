import speech_recognition as sr
import time

def reconocimiento_voz(secconds):
    reconocedor = sr.Recognizer()

    ''' Grabando Audio '''
    with sr.Microphone() as source:
        '''Ajusta el Audio'''
        reconocedor.adjust_for_ambient_noise(source, duration=1)
        print("\nGrabando audio por 5 segundos")
        audio_grabado = reconocedor.listen(source, timeout=int(secconds))

        ''' for second in range(5):
            print(str(second) + "...")
            time.sleep(1) '''

        print("Grabación Exitosa")

    ''' Reconociendo el Audio '''

    try:
        ''' Reconoce el Texto '''
        texto = reconocedor.recognize_google\
                (
            audio_grabado,
            language="es-PE"
                )

        print("\nResultado: {} \n".format(texto))

    except Exception as ex:

        texto = print("\nNo ha dicho nada (Asegurese de tener el microfono encendido)")
        texto = print(ex)

    return texto