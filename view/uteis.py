def dimensionamento(janela, largura, altura, teto=0):
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela - largura) // 2
    y = (altura_tela - (altura + teto)) // 2
    return largura, altura, x, y


def tit():
    texto = 'GERADOR AUTOMÁTICO DE KITS'
    return texto


def msg():
    texto = '''Como funciona o sistema?
        Muito simples! Você deve clicar no botão "SELECIONAR PASTA" para indicar\n o local no seu computador onde a tabela será salva!\n
        Depois basta clicar no botão "GERAR KITS" e o sistema se encarregará de construir a tabela final!  
    '''
    return texto
