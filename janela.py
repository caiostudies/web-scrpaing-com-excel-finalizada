from tkinter import * #biblioteca nativa
from tkinter import ttk
from conect import produtos_banco, pesquisaBanco
import tkinter
import pandas as pd
import os

janela = Tk()


class Aplicacao:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.dropdown()
        self.botoes()
        self.lista_frame2()
        self.select_list()
        self.label()


        janela.mainloop() #a janela fica carregada na tela até ser fechada

    def tela(self):
        self.janela.title('MAGALU') #título
        self.janela.configure(background='#0000FF') #cor de fundo
        self.janela.geometry('700x500') #tamanho da tela
        self.janela.resizable(True, True) #deixar responsivo
        self.janela.wm_maxsize(width=700, height=500) #trava nessa medida

    def frames(self):
        self.frame0 = Frame(self.janela, bg='#0b090a') #uma característica de frame, usado para editá-lo
        self.frame0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame1 = Frame(self.janela, bg='#0b090a')  # uma característica de frame, usado para editá-lo
        self.frame1.place(relx=0.03, rely=0.2, relwidth=0.94, relheight=0.11) #relheight altura da sombra

        self.frame2 = Frame(self.janela, bg='#0f0')  # uma característica de frame, usado para editá-lo
        self.frame2.place(relx=0.03, rely=0.5, relwidth=0.94, relheight=0.45)

        self.frame3 = Frame(self.janela, bg='#0b090a')  # uma característica de frame, usado para editá-lo
        self.frame3.place(relx=0.03, rely=0.35, relwidth=0.94, relheight=0.11)

    def botoes(self):
        self.btBuscar = Button(self.frame1, text='Pesquisar', bg='#d3d3d3', foreground='black', command=self.pesquisa ) #criando o botão
        self.btBuscar.place(relx=0.55, rely=0.1, relwidth=0.5, relheight=0.8) #dimensionando o botão

        self.btcriar_excel = Button(self.frame3, text='xlsx', bg='#d3d3d3', foreground='black', command=self.gerar_excel )
        self.btcriar_excel.place(relx=0.75, rely=0.1, relwidth=0.2, relheight=0.8)  # dimensionando o botão

        self.btcriar_csv = Button(self.frame3, text='csv', bg='#d3d3d3', foreground='black', command=self.gerar_csv)
        self.btcriar_csv.place(relx=0.05, rely=0.1, relwidth=0.2, relheight=0.8)

        self.excluir_csv = Button(self.frame3, text='excluir csv', bg='#d3d3d3', foreground='black', command=self.excluir_csv)
        self.excluir_csv.place(relx=0.30, rely=0.1, relwidth=0.2, relheight=0.8)

        self.excluir_excel = Button(self.frame3, text='excluir xlsx', bg='#d3d3d3', foreground='black', command=self.excluir_excel)
        self.excluir_excel.place(relx=0.52, rely=0.1, relwidth=0.2, relheight=0.8)


    def label(self):
        self.lbTitulo = Label(self.frame0, text="Notebooks Magalu", bg='#99B2DD', foreground='black', font=40, background='white')
        self.lbTitulo.place(relx=0.27, rely=0.25, relwidth=0.5, relheight=0.5)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=('col1', #criando as colunas
                                                                     'col2',
                                                                     'col3',
                                                                     'col4')) #faixa de cima da tabela


        self.listaCli.heading('#0', text='') #dando nome as colunas
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Modelo')
        self.listaCli.heading('#3', text='Preço')
        self.listaCli.heading('#4', text='Marca')

        self.listaCli.column('#0', width=0, stretch=NO) #largura das colunas
        self.listaCli.column('#1', width=1)
        self.listaCli.column('#2', width=392)
        self.listaCli.column('#3', width=40)
        self.listaCli.column('#4', width=40)


        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)


    def select_list(self):
        self.listaCli.delete(*self.listaCli.get_children())
        for i in produtos_banco():
            self.listaCli.insert(parent='', index=0, values=i)


    def dropdown(self):
        self.options = ["acer", "asus", "dell", "lenovo", "samsung", '']
        self.clicked = StringVar()
        self.clicked.set(self.options[5])

        self.drop = OptionMenu(self.frame1, self.clicked, *self.options)
        self.drop.place(relx=0.04, rely=0.1, relwidth=0.5, relheight=0.8)

    def pesquisa(self):
        self.listaCli.delete(*self.listaCli.get_children())

        a = self.clicked.get()
        listaCelulares = pesquisaBanco(a)

        for celular in listaCelulares:
            self.listaCli.insert("", tkinter.END, values=celular)

    def gerar_csv(self):

        df = pd.DataFrame(produtos_banco())
        df.to_csv('somativa.csv', index=False)

    def gerar_excel(self):

        df = pd.DataFrame(produtos_banco())
        df.to_excel('excel.xlsx')

    def excluir_excel(self):

        os.remove("excel.xlsx")

    def excluir_csv(self):

        os.remove("somativa.csv")








