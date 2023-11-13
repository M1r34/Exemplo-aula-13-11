import streamlit as st
import pandas as pd
import streamlit as st
from PIL import Image

image = Image.open('manom.png')

st.image(image, caption='PCD', channels="RGB")

st.title('Dados Calibração')
st.subheader('Planilha de Registro de dados da calibração')
dados = st.file_uploader('Carregar Planilhacalibracao')


FORMULARIO = st.sidebar.form('Leituras')

with st.form('teste',clear_on_submit = True):
                     V_A_Psi = st.number_input('Valor Aplicado Psi')
                     V_A_pc = st.number_input('Valor Aplicado porcentagem')                     
                     L_A_Psi =st.number_input('Leitura Ascendente Psi')
                     L_A_erro_Psi = L_A_Psi-L_A_Psi
                     st.write(L_A_erro_Psi)
                     #L_A_pc_Span = st.number_input('Leitura Ascendente Porcentagem de span')
                     L_D_Psi = st.number_input('Leitura Descendente Psi')
                     #L_D_erro_Psi = st.number_input('Leitura Descendente Erro Psi')
                     #L_D_pc_Span = st.number_input('Leitura Descendente porcentagem de span')
                     #H_Psi  = st.number_input('Histerese Psi (abs)')
                     #H_pc_Span  = st.number_input('Histerese Porcentagem de span')
                     #H_pc  = st.number_input('Histerese Porcentagem')
                     #H_max  = st.number_input('Histerese máximo')
                     #P_L_max_asc  = st.number_input('Primeira Leitura Ascendente máximo')
                     #P_L_min_asc = st.number_input('Primeira Leitura Ascendente mínimo')
                     #P_L_max_desc  = st.number_input('Primeira Leitura Descendente máximo')
                     #P_L_min_desc  = st.number_input('Primeira Leitura Descendente mínimo')
                     botao = st.form_submit_button('Entrar')


                     


#if df!=[]:
if botao:
    novo = {'Valor Aplicado Psi':V_A_Psi,'Porcentagem Valor Aplicado':V_A_pc,'Leitura Ascendente Psi':L_A_Psi,'Leitura Descendente Psi':L_D_Psi}

    df = df.append(novo, ignore_index = True)
    #st.dataframe(df) #verificar se acrescentou o nome
    #df.to_csv(Planilhacalibracao.name, index = False, sep = ';')






    

