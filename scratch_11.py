import requests
from tkinter import *
janela = Tk()
janela.title("Cabinet Maker")
janela.iconbitmap("images/icone.ico")
#dimensoes da janela
largura = 800
altura = 350
#tamanho da screen
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
# posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
img = PhotoImage(file="images/logo.png")
label_imagem = Label(janela, image=img, bd=0, relief="flat")
label_imagem.pack(expand=True)
def btn_click():
    label_imagem.pack_forget()
    btn.pack_forget()
    from tkinter import ttk
    tabControl = ttk.Notebook(janela)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab1, text='Bancada')
    tabControl.add(tab2, text='Estante')
    tabControl.add(tab3, text='Gaveteiro')
    tabControl.pack(expand=1, fill="both")
    #ABA GAVETEIRO
    ttk.Label(tab3,
              text="Configurador de Medidas").grid(column=0,
                                                   row=0,
                                                   padx=30,
                                                   pady=1)
    ttk.Label(tab3,
              text="Altura").grid(column=0, row=1, padx=10, pady=1, sticky=S)
    ttk.Label(tab3,
              text="Largura").grid(column=0, row=2, padx=10, pady=1, sticky=S)
    ttk.Label(tab3,
              text="Profundidade").grid(column=0, row=3, padx=10, pady=1, sticky=S)
    ttk.Label(tab3,
              text="Expessura da Chapa").grid(column=0, row=4, padx=10, pady=1, sticky=S)
    ttk.Label(tab3,
              text="Quantidade de Gavetas").grid(column=0, row=5, padx=10, pady=1, sticky=S)

    text_usuario0 = Entry(tab3)
    text_usuario0.grid(row=1, column=1)
    text_usuario1 = Entry(tab3)
    text_usuario1.grid(row=2, column=1)
    text_usuario2 = Entry(tab3)
    text_usuario2.grid(row=3, column=1)
    text_usuario3 = Entry(tab3)
    text_usuario3.grid(row=4, column=1)
    text_usuario4 = Entry(tab3)
    text_usuario4.grid(row=5, column=1)

    def btn3_click():
        A = 0.0
        L = 0.0
        P = 0.0
        EC = 0.0
        QG = 0.0
        try:
            A = float(text_usuario0.get())
            L = float(text_usuario1.get())
            P = float(text_usuario2.get())
            EC = float(text_usuario3.get())
            QG = float(text_usuario4.get())
        except:

            return
        #CALCULANDO MEDIDAS
        larg_frgav = L - 2.6 - (EC*2)
        alt_frgav = A - 2 - (QG - 1) / QG
        alt_frgav1 = (A - 2 - (QG - 1) / QG) - 2
        prof_frgav = EC
        larg_latgav = P - 2 - (EC * 3)
        larg_cfrgav = L - 2.6 - (EC * 2)
        fundo_gav = L - 2.6 - (EC * 2)
        prof_fundogav = P - EC - 2

        lat_direita = (str(P) + "x" + str(A) + "x" + str(EC))
        lat_esquerda = (str(P) + "x" + str(A) + "x" + str(EC))
        b_superior = (str(L) + "x" + str(EC) + "x" + str(P))
        b_inferior = (str(L) + "x" + str(EC) + "x" + str(P))
        frente_gaveta = (str(larg_frgav) + "x" + str(alt_frgav) + "x" + str(prof_frgav))
        posterior_gaveta = (str(larg_cfrgav) + "x" + str(alt_frgav1) + "x" + str(prof_frgav))
        fundo_gaveta = (str(fundo_gav) + "x" + str(prof_frgav) + "x" + str(prof_fundogav))
        lateral_gaveta = (str(larg_latgav) + "x" + str(alt_frgav1) + "x" + str(prof_frgav))
        cfrente_gaveta = (str(larg_frgav) + "x" + str(alt_frgav1) + "x" + str(prof_frgav))

        # CALCULANDO QUANTIDADE DE PEÇAS
        Qlat = QG * 2

        Qlat_direita = 1
        Qlat_esquerda = 1
        Qb_superior = 1
        Qb_inferior = 1
        Qfr_gav = (str(QG))
        Qlat_gav = (str(Qlat))

        # SALVANDO AS PEÇAS E SUAS RESPECTIVAS MEDIDAS
        ttk.Label(tab3,
                  text="Quantidade").grid(column=0, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Peças").grid(column=1, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Tamanho (LxAxP)").grid(column=2, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Lateral Esquerda").grid(column=1, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Lateral Direita").grid(column=1, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Base Superior").grid(column=1, row=11, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Base Inferior").grid(column=1, row=12, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Frente de Gaveta").grid(column=1, row=13, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Contra Frente de Gaveta").grid(column=1, row=14, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Posterior de Gaveta").grid(column=1, row=15, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Lateral de Gaveta").grid(column=1, row=16, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text="Fundo de Gaveta").grid(column=1, row=17, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=lat_esquerda).grid(column=2, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=lat_direita).grid(column=2, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=b_superior).grid(column=2, row=11, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=b_inferior).grid(column=2, row=12, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=frente_gaveta).grid(column=2, row=13, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=cfrente_gaveta).grid(column=2, row=14, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=posterior_gaveta).grid(column=2, row=15, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=lateral_gaveta).grid(column=2, row=16, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=fundo_gaveta).grid(column=2, row=17, padx=11, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qlat_esquerda).grid(column=0, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qlat_direita).grid(column=0, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qb_superior).grid(column=0, row=11, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qb_inferior).grid(column=0, row=12, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qfr_gav).grid(column=0, row=13, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qfr_gav).grid(column=0, row=14, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qlat_gav).grid(column=0, row=15, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qfr_gav).grid(column=0, row=16, padx=10, pady=1, sticky=S)
        ttk.Label(tab3,
                  text=Qfr_gav).grid(column=0, row=17, padx=10, pady=1, sticky=S)



    btn3 = Button(tab3, text="Calcular Medidas", command=btn3_click)
    btn3.grid(column=0, row=7, padx=10, pady=1, sticky=S)

    # ABA ESTANTE
    ttk.Label(tab2,
              text="Configurador de Medidas").grid(column=0,
                                                   row=0,
                                                   padx=30,
                                                   pady=1)
    ttk.Label(tab2,

    text = "Altura").grid(column=0, row=1, padx=10, pady=1, sticky=S)
    ttk.Label(tab2,
    text = "Largura").grid(column=0, row=2, padx=10, pady=1, sticky=S)
    ttk.Label(tab2,
    text = "Profundidade").grid(column=0, row=3, padx=10, pady=1, sticky=S)
    ttk.Label(tab2,
    text = "Expessura da Chapa").grid(column=0, row=4, padx=10, pady=1, sticky=S)
    ttk.Label(tab2,
    text = "Quantidade de Divisórias").grid(column=0, row=5, padx=10, pady=1, sticky=S)
    text_usuario0 = Entry(tab2)
    text_usuario0.grid(row=1, column=1)
    text_usuario1 = Entry(tab2)
    text_usuario1.grid(row=2, column=1)
    text_usuario2 = Entry(tab2)
    text_usuario2.grid(row=3, column=1)
    text_usuario3 = Entry(tab2)
    text_usuario3.grid(row=4, column=1)
    text_usuario4 = Entry(tab2)
    text_usuario4.grid(row=5, column=1)


    def btn2_click():
        A = 0.0
        L = 0.0
        P = 0.0
        EC = 0.0
        QD = 0.0
        try:
            A = float(text_usuario0.get())
            L = float(text_usuario1.get())
            P = float(text_usuario2.get())
            EC = float(text_usuario3.get())
            QD = float(text_usuario4.get())
        except:

            return
        # CALCULANDO TAMANHO DAS PEÇAS
        larg_prat = L - (EC * 2)

        lat_direita = (str(P) + "x" + str(A) + "x" + str(EC))
        lat_esquerda = (str(P) + "x" + str(A) + "x" + str(EC))
        b_superior = (str(L) + "x" + str(EC) + "x" + str(P))
        b_inferior = (str(L) + "x" + str(EC) + "x" + str(P))
        prat_linear = (str(larg_prat) + "x" + str(EC) + "x" + str(P))
        # CALCULANDO QUANTIDADE DE PEÇAS
        Qlat_direita = 1
        Qlat_esquerda = 1
        Qb_superior = 1
        Qb_inferior = 1
        Qprat_linear = (str(QD))

        # SALVANDO AS PEÇAS E SUAS RESPECTIVAS MEDIDAS
        ttk.Label(tab2,
                  text="Quantidade").grid(column=0, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Peças").grid(column=1, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Tamanho (LxAxP)").grid(column=2, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Lateral Esquerda").grid(column=1, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Lateral Direita").grid(column=1, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Base Superior").grid(column=1, row=11, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Base Inferior").grid(column=1, row=12, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text="Prateleira Linear").grid(column=1, row=13, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=lat_esquerda).grid(column=2, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=lat_direita).grid(column=2, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=b_superior).grid(column=2, row=11, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=b_inferior).grid(column=2, row=12, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=prat_linear).grid(column=2, row=13, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=Qlat_esquerda).grid(column=0, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=Qlat_direita).grid(column=0, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=Qb_superior).grid(column=0, row=11, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=Qb_inferior).grid(column=0, row=12, padx=10, pady=1, sticky=S)
        ttk.Label(tab2,
                  text=Qprat_linear).grid(column=0, row=13, padx=10, pady=1, sticky=S)

    btn2 = Button(tab2, text="Calcular Medidas", command=btn2_click)
    btn2.grid(column=0, row=7, padx=10, pady=1, sticky=S)

    #ABA BANCADA
    ttk.Label(tab1,
              text="Configurador de Medidas").grid(column=0,
                                   row=0,
                                   padx=30,
                                   pady=1)
    ttk.Label(tab1,
              text="Altura").grid(column=0,row=1,padx=10,pady=1,sticky=S)
    ttk.Label(tab1,
              text="Largura").grid(column=0, row=2, padx=10, pady=1, sticky=S)
    ttk.Label(tab1,
              text="Profundidade").grid(column=0, row=3, padx=10, pady=1, sticky=S)
    ttk.Label(tab1,
              text="Expessura da Chapa").grid(column=0, row=4, padx=10, pady=1, sticky=S)
    text_usuario0 = Entry(tab1)
    text_usuario0.grid(row=1, column=1)
    text_usuario1 = Entry(tab1)
    text_usuario1.grid(row=2,column=1)
    text_usuario2 = Entry(tab1)
    text_usuario2.grid(row=3, column=1)
    text_usuario3 = Entry(tab1)
    text_usuario3.grid(row=4, column=1)


    def btn1_click():
        A = 0.0
        L = 0.0
        P = 0.0
        EC = 0.0
        try:
            #CALCULANDO TAMANHO DAS PEÇAS
            A = float(text_usuario0.get())
            L = float(text_usuario1.get())
            P = float(text_usuario2.get())
            EC = float(text_usuario3.get())
        except:

            return

        lat_direita = (str(P) + "x" + str(A) + "x" + str(EC))
        tampo = (str(L) + "x" + str(EC) + "x" + str(P))

        #SALVANDO AS PEÇAS E SUAS RESPECTIVAS MEDIDAS
        ttk.Label(tab1,
                    text="Peças").grid(column=0, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text="Tamanho (LxAxP)").grid(column=1, row=8, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text="Lateral Esquerda").grid(column=0, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text="Lateral Direita").grid(column=0, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text="Tampo Superior").grid(column=0, row=12, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text=lat_direita).grid(column=1, row=9, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text=lat_direita).grid(column=1, row=10, padx=10, pady=1, sticky=S)
        ttk.Label(tab1,
                    text=tampo).grid(column=1, row=12, padx=10, pady=1, sticky=S)


    btn1 = Button(tab1, text="Calcular Medidas", command=btn1_click)
    btn1.grid(column=0, row=7, padx=10, pady=1, sticky=S)


btn = Button(janela, text="Projetar", width=20, height=2,font="Arial 15", command=btn_click)
btn.pack(expand=True)
janela.mainloop()