import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="") # adicione sua api key aqui para realizar o teste do código!

st.write("## ChatBot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

if mensagem_usuario:
    st.chat_message("user").write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    resposta_modelo = modelo.chat.completions.create(messages=st.session_state["lista_mensagens"], model="gpt-4o")
    
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
