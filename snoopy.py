from tkinter import *
from tkinter.filedialog import askopenfilename

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import sys 
sys.path.insert(1, 'dsp-modulo')
from thinkdsp import read_wave
import numpy

principal = Tk()
principal.title("Análisis audio")
principal.geometry("500x400")

strCuerda = StringVar()
strCuerda.set("")

strFreqActual = StringVar()
strFreqActual.set("")

strFreq1 = StringVar()
strFreq1.set("")

strFreq2 = StringVar()
strFreq2.set("")

strFreq3 = StringVar()
strFreq3.set("")

strAfi1 = StringVar()
strAfi1.set("")

strAfi2 = StringVar()
strAfi2.set("")

strAfi3 = StringVar()
strAfi3.set("")


def iniciar():
    Cuerda = "5ta La(A) 110.00 Hz"
    FreqActual = "Frecuencia actual"
    Freq1 = "79.99 hz"
    Freq2 = "110.80 hz"
    Freq3 = "319.01 hz"
    Afi1 = "necesitas apretar la cuerda->"
    Afi2 = "La afinacion es correcta"
    Afi3 = "<-necesitas aflojar la cuerda"

    strCuerda.set(Cuerda)
    strFreqActual.set(FreqActual)
    strFreq1.set(Freq1)
    strFreq2.set(Freq2)
    strFreq3.set(Freq3)
    strAfi1.set(Afi1)
    strAfi2.set(Afi2)
    strAfi3.set(Afi3)



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


lblcuerda = Label(principal, textvariable = strCuerda)
lblcuerda.pack()

lblFreqActual = Label(principal, textvariable = strFreqActual)
lblFreqActual.pack()

lblFreq2 = Label(principal, textvariable = strFreq2)
lblFreq2.pack()

lblAfi2 = Label(principal, textvariable = strAfi2)
lblAfi2.pack()


lblcuerda = Label(principal, textvariable = strCuerda)
lblcuerda.pack()

lblFreqActual = Label(principal, textvariable = strFreqActual)
lblFreqActual.pack()

lblFreq3 = Label(principal, textvariable = strFreq3)
lblFreq3.pack()

lblAfi3 = Label(principal, textvariable = strAfi3)
lblAfi3.pack()

mainloop()