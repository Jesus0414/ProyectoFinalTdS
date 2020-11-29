from tkinter import *

import pyaudio 
import numpy as np  
import wave 

principal = Tk()
principal.title("Afinador de Guitarra")
principal.geometry("350x300")

strCuerda = StringVar()
strCuerda.set("")

strFreqActual = StringVar()
strFreqActual.set("")

strFrecuencia = StringVar()
strFrecuencia.set("")

strAfinacion = StringVar()
strAfinacion.set("")

#formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100

SEGUNDOS_GRABACION = 1

#Tamaño de CHUNK
CHUNK = 2048

window = np.blackman(CHUNK)

def iniciar():
    FreqActual = "Frecuencia actual"

    def analizar(stream):
        data = stream.read(CHUNK, exception_on_overflow=False)
        #"2048h"
        waveData = wave.struct.unpack("%dh"%(CHUNK), data)
        npData = np.array(waveData)

        dataEntrada = npData * window

        fftData = np.abs(np.fft.rfft(dataEntrada))

        indiceFrecuenciaDominante = fftData[1:].argmax() + 1

        #Cambio de indice Hz
        y0,y1,y2 = np.log(fftData[indiceFrecuenciaDominante-1:indiceFrecuenciaDominante+2])
        x1 = (y2-y0) * 0.5 / (2 * y1 - y2 - y0)
        frecuenciaDominante = (indiceFrecuenciaDominante+x1) * FRECUENCIA_MUESTREO / CHUNK
        Frecuencia = str(frecuenciaDominante)
        print("Frecuencia Dominante: " + str(frecuenciaDominante) + " Hz", end='\r')
        strFrecuencia.set(Frecuencia)

        #frecuenciasLetrasDTMF = [82.4, 110.0, 146.83, 196.0, 246.94, 329.63]

        tolerancia = 13.0
        toleranciaAfi = 1.3
        
        if  frecuenciaDominante > 82.4 - tolerancia and frecuenciaDominante < 82.4 + tolerancia :
            Cuerda = "6ta Mi(E) 82.4 Hz"
            if  frecuenciaDominante > 82.4 - toleranciaAfi and frecuenciaDominante < 82.4 + toleranciaAfi :
                Afinacion = "La Afinacion es correcta"
            elif  frecuenciaDominante < 82.4 + toleranciaAfi :
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        elif  frecuenciaDominante > 110.0 - tolerancia and frecuenciaDominante < 110.0 + tolerancia :
            Cuerda = "5ta La(A) 110.00 Hz"
            if  frecuenciaDominante > 110.0 - toleranciaAfi and frecuenciaDominante < 110.0 + toleranciaAfi :
                Afinacion = "La Afinacion es correcta"
            elif  frecuenciaDominante < 110.0 + toleranciaAfi :
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        elif  frecuenciaDominante > 146.83 - tolerancia and frecuenciaDominante < 146.83 + tolerancia :
            Cuerda = "4ta Re(D) 146.83 Hz"
            if  frecuenciaDominante > 146.83 - toleranciaAfi and frecuenciaDominante < 146.83 + toleranciaAfi :
                Afinacion = "La Afinacion es correcta"
            elif  frecuenciaDominante < 146.83 + toleranciaAfi :
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        elif  frecuenciaDominante > 196.0 - tolerancia and frecuenciaDominante < 196.0 + tolerancia :
            Cuerda = "3ra Sol(G) 196.0 Hz"
            if  frecuenciaDominante > 196.0 - toleranciaAfi and frecuenciaDominante < 196.0 + toleranciaAfi :
                Afinacion = "La Afinacion es correcta"
            elif  frecuenciaDominante < 196.0 + toleranciaAfi :
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        elif  frecuenciaDominante > 246.94 - tolerancia and frecuenciaDominante < 246.94 + tolerancia :
            Cuerda = "2da Si(B) 246.94 Hz"
            if  frecuenciaDominante > 246.94 - toleranciaAfi and frecuenciaDominante < 246.94 + toleranciaAfi :
                Afinacion = "La Afinacion es correcta"
            elif  frecuenciaDominante < 246.94 + toleranciaAfi :
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        elif  frecuenciaDominante > 329.63 - tolerancia and frecuenciaDominante < 329.63 + tolerancia :
            Cuerda = "1ra Mi(E2) 329.63 Hz"
            if  frecuenciaDominante > 329.63- toleranciaAfi and frecuenciaDominante < 329.63 + toleranciaAfi :
                Afinacion = "La Afinacion es correcta"
            elif  frecuenciaDominante < 329.63 + toleranciaAfi :
                Afinacion = "Es necesario apretar la cuerda"
            else:
                Afinacion = "Es necesario aflojar la cuerda"
        else:
            Cuerda = "Cuerda no identificada"
            Afinacion = "Presione el botón 'Iniciar' otra vez"

        
        strCuerda.set(Cuerda)
        strFreqActual.set(FreqActual)
        strAfinacion.set(Afinacion)

    if __name__ == "__main__":
        p = pyaudio.PyAudio()
        stream = p.open(format=PROFUNDIDAD_BITS, channels=CANALES, rate=FRECUENCIA_MUESTREO, input=True, frames_per_buffer=CHUNK)
        
        for i in range(0, int(FRECUENCIA_MUESTREO * SEGUNDOS_GRABACION / CHUNK)):
            analizar(stream)
        
        stream.stop_stream()
        stream.close()
        p.terminate()

strSecuencia = StringVar()
strSecuencia.set("Número contenido en el audio")

btnIniciar = Button(principal, text = "Iniciar", command = iniciar) 
btnIniciar.pack()

lblcuerda = Label(principal, textvariable = strCuerda)
lblcuerda.pack()

lblFreqActual = Label(principal, textvariable = strFreqActual)
lblFreqActual.pack()

lblFrecuencia = Label(principal, textvariable = strFrecuencia)
lblFrecuencia.pack()

lblAfinacion = Label(principal, textvariable = strAfinacion)
lblAfinacion.pack()

principal.mainloop()