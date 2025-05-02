import streamlit as st 
st.title("cadastro de clientes")

nome = st.text_input("Nome do cliente")
endereco = st.text_input("digite o endereço")
data_nacimento = st.date_input("data de nacimento")
tipo_client = st.selectbox("tipo de cliente", ["pessoa fisica", "pessoa juridica"])
cadastrar = st.button("cadastrar cliente")

if cadastrar:
    with open("clientes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome}, {endereco}, {data_nacimento}, {tipo_client},\n")
        st.success("cliente cadastrado com sucesso")

