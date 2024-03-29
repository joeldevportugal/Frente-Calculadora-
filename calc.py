from tkinter import *





# defenir as cores a Usar neste Projecto ----------------------------------------
co1='#ffffff' # branco para O fundo 
co2='#f5feff' # azul mar para Os Butoes
co3='#000000' # cor preta para Os butões 
co4='#0000ff' # Azul painel Butões
co5='#c5bbc8' # ecra
#--------------------------------------------------------------------------------
# configurar a nossa janela -----------------------------------------------------
janela = Tk()
janela.title('Calculadora dev Joel 2024 ©')
janela.geometry('300x340+100+100')
janela.resizable(False, False)
janela.configure(bg=co1)
#--------------------------------------------------------------------------------

Eecra = Entry(janela, bg=co5, width=25, font=('arial 15'))
Eecra.place(x=10, y=10)

controles = Label(janela, bg=co4, width=39, height=18)
controles.place(x=10, y=45)

BtnZero = Button (controles, text='0', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnZero.place(x=0, y=225)
Btnigual = Button (controles, text='=', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
Btnigual.place(x=70, y=225)
BtnVirgula = Button (controles, text=',', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnVirgula.place(x=140, y=225)
BtnSoma = Button (controles, text='+', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5, height=3)
BtnSoma.place(x=210, y=180)
BtnUM = Button (controles, text='1', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnUM.place(x=0, y=180)
Btndois = Button (controles, text='2', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
Btndois.place(x=70, y=180)
BtnTês = Button (controles, text='3', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnTês.place(x=140, y=180)
BtnQuatro = Button (controles, text='4', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnQuatro.place(x=0, y=135)
BtnCinco = Button (controles, text='5', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnCinco.place(x=70, y=135)
BtnSeis = Button (controles, text='6', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnSeis.place(x=140, y=135)
BtnSub = Button (controles, text='-', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnSub.place(x=210, y=135)
Btnsete = Button (controles, text='7', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
Btnsete.place(x=0, y=90)
BtnOito = Button (controles, text='8', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnOito.place(x=70, y=90)
BtnOito = Button (controles, text='9', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnOito.place(x=140, y=90)
BtnMUL = Button (controles, text='X', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnMUL.place(x=210, y=90)
Btnclear = Button (controles, text='C', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=11)
Btnclear.place(x=0, y=45)
BtnModulo = Button (controles, text='%', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnModulo.place(x=140, y=45)
BtnDiv = Button (controles, text='/', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=5)
BtnDiv.place(x=210, y=45)
BtnMem = Button (controles, text='Mem', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=11)
BtnMem.place(x=0, y=0)
BtnBack = Button (controles, text='<', font=('arial 14'), bg=co2, relief=RAISED, overrelief=RIDGE, width=11)
BtnBack.place(x=143, y=0)

janela.mainloop()