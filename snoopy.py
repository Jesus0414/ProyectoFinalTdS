from tkinter import *

import pyaudio 
import numpy as np  
import wave 

principal = Tk()
principal.title("Análisis audio")
principal.geometry("500x400")

strCuerda = StringVar()
strCuerda.set("")

strFreqActual = StringVar()
strFreqActual.set("")

strFreq1 = StringVar()
strFreq1.set("")

strAfi1 = StringVar()
strAfi1.set("")

#formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100

SEGUNDOS_GRABACION = 1

#Tamaño de CHUNK
CHUNK = 2048

window = np.blackman(CHUNK)




def iniciar():
    Cuerda = "5ta La(A) 110.00 Hz"
    FreqActual = "Frecuencia actual"
    Afi1 = "necesitas apretar la cuerda->"

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
        Freq1 = str(frecuenciaDominante)

        


        strCuerda.set(Cuerda)
        strFreqActual.set(FreqActual)
        strFreq1.set(Freq1)
        strAfi1.set(Afi1)

        print("Frecuencia Dominante: " + str(frecuenciaDominante) + " Hz", end='\r')

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

lblFreq1 = Label(principal, textvariable = strFreq1)
lblFreq1.pack()

lblAfi1 = Label(principal, textvariable = strAfi1)
lblAfi1.pack()

principal.mainloop()