from .uteis import dimensionamento, msg, tit
from pathlib import Path
from tkinter import filedialog, messagebox
import tkinter as tk


class Janela:
    def __init__(self):
        self.frame = None
        self.diretorio = None
        self.pasta = None

    def tela_base(self, tela):
        self.frame = tela
        largura, altura, x, y = dimensionamento(self.frame, 765, 580, 85)
        self.frame.geometry(f"{largura}x{altura}+{x}+{y}")
        self.frame.title('Gerador de Kits')
        self.frame.config(background='#a1d1d2')
        caminho = Path().absolute()
        logo = caminho / 'img/foto.ico'
        self.frame.wm_iconbitmap(logo)

        frame1 = tk.Frame(self.frame)
        frame1.grid(row=0, column=0, padx=10, pady=35)
        titulo = tit()
        texto1 = tk.Label(frame1, text=titulo, fg='#111f32')
        texto1.config(font=('Nunito', 14, 'bold'), bg='#a1d1d2')
        texto1.grid(row=0, column=0)

        frame2 = tk.Frame(self.frame)
        frame2.grid(row=1, column=0, padx=10, pady=10)
        mensagem = msg()
        texto2 = tk.Label(frame2, text=mensagem, fg='#111f32')
        texto2.config(font=('Nunito', 11, 'bold'), bg='#a1d1d2')
        texto2.grid(row=0, column=0)

        frame3 = tk.Frame(self.frame, bg='#a1d1d2')
        frame3.grid(row=2, column=0, padx=10, pady=50)
        botao1 = tk.Button(frame3, text='Selecionar Pasta', fg='#111f32', command=self.local)
        botao1.config(font=('Nunito', 10, 'bold'), bg='#a1d1d2')
        botao1.grid(row=0, column=0, padx=(20, 0))
        self.pasta = tk.Text(frame3, wrap='word', width=67, height=1)
        self.pasta.config(font=('Nunito', 10, 'bold'), bg='#111f32', fg='#a1d1d2')
        self.pasta.grid(row=0, column=1, padx=(8, 0))

        frame4 = tk.Frame(self.frame)
        frame4.grid(row=3, column=0, pady=50)
        botao2 = tk.Button(frame4, text='GERAR KITS', fg='#111f32', width=20, height=2, command=self.kits)
        botao2.config(font=('Nunito', 12, 'bold'), bg='#a1d1d2')
        botao2.grid(row=0, column=0)
        self.frame.mainloop()

    def local(self):
        self.pasta.config(state=tk.NORMAL)
        self.pasta.delete("1.0", tk.END)
        self.diretorio = filedialog.askdirectory()
        self.pasta.insert(1.0, self.diretorio)
        self.pasta.config(state=tk.DISABLED)

    def kits(self):
        messagebox.showinfo(title='SUCESSO!', message='Tabela Kits gerado com sucesso!')
