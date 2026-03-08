import pyautogui as py
import pandas as pd
import time

py.PAUSE = 1
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# abrir o navegador
py.press("win")
py.write("chrome")
py.press("enter")
py.click(x=247, y=640)

# entrar no sistema
py.write(link)
py.press("enter")
time.sleep(5)

# logar
py.click(x=403, y=375)
py.write("python@gmail.com")
py.press("tab")
py.write("senha123")
py.press("tab")
py.press("enter")
time.sleep(5)

# importar a base de dados
tabela = pd.read_csv("aula 1 (automação)\produtos.csv")

# cadastrar produtos
for linha in tabela.index:
    py.click(x=249, y=266)

    codigo = str(tabela.loc[linha, "codigo"])
    py.write(codigo)
    py.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    py.write(marca)
    py.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    py.write(tipo)
    py.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    py.write(categoria)
    py.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    py.write(preco)
    py.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    py.write(custo)
    py.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        py.write(obs)
    py.press("tab")
    py.press("enter")
    py.scroll(1000)
