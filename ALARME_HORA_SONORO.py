"""
OBJETIVO: criar um alarme sonoro para o horário definido pelo usuário.

"""

from tkinter import * #Responsável pela interface, importamos todas as funções
import datetime
import time
from playsound import playsound #responsável pelo sinal sonóro

root = Tk() #definição do objeto de interface
root.geometry("500x250")  #define o tamanho da interface

def alarme():
    while True:
        fixar_tempo_alarme = f"{hora.get()}:{minuto.get()}:{segundo.get()}" #Tempo escolhido pelo usuário, o get serve
        # para reconhecer a hora escolhida
        tempo_atual = datetime.datetime.now().strftime("%H:%M:%S")    #tempo atual em horas:min:segundos
        time.sleep(1)   #delay para imprimir de 1 em 1 segundo a contagem/hora atual
        print(tempo_atual, fixar_tempo_alarme)  #impressão dos tempos
        #Enquanto está dentro do loop ele irá imprimir o tempo atual a cada segundo até chegar no horário esolhido
        if tempo_atual == fixar_tempo_alarme:
            print('Alarme ativado!')
            playsound('alarme_sonoro2.mp3')  #ativa o sinal sonoro e para o loop
            break

Label(root, text = 'Alarme', font=('Arial, 25'), fg = 'gray').place(x=200,y=0)  #armazena um texto na interface (root)
# com fonte e cor, o place serve para fixar as coordenadas do texto na interface
Label(root, text = 'Defina o horário que o alarme irá tocar!', font =('Arial, 12'),fg='red').place(x=125,y=50)

hora = StringVar(root)  #criação das variáveis em string na interface
horas = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20',
         '21','22','23','24']  #armazena as opções de hora (0 a 24h) como texto na interface
hora.set(horas[0])  #defino a primeira opção como a hora 0, ou seja, a primeira  posição na tupla.
h = OptionMenu(root,hora,*horas)    #armazeno no menu de opções todas as horas
h.place(x=125,y=100)    #posicionando o menu hora

minuto = StringVar(root)
minutos = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20',
           '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41',
           '42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
minuto.set(minutos[0])  #definindo a opção como a primeira posição da tupla.
m = OptionMenu(root, minuto, *minutos)
m.place(x=230, y = 100)

segundo = StringVar(root)
segundos = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20',
           '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41',
           '42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
segundo.set(segundos[0])
s = OptionMenu(root,segundo,*segundos)
s.place(x=330,y = 100)

Button(root, text='Confirmar',font = ('Arial, 12'), fg= 'green', command= alarme).place(x=215,y=150)
#definição do botão de confirmar a hora selecionada pelo usuário
root.mainloop() #mantém o alarme ativado