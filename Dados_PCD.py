import streamlit as st
import pandas as pd

st.title('Dados PCD')
st.subheader('Para elaboração de Política Públicas')
dados = st.file_uploader('Carregar Dados')

if dados is not None:
    df = pd.read_csv(dados, sep = ';')

else:
    df = []

st.dataframe(df)

st.sidebar.header('Dados a serem coletados e inseridos')

FORMULARIO = st.sidebar.form('Alterações')

with st.sidebar.form('teste',clear_on_submit = True):
                     cidade = st.text_input('Cidade')
                     bairro = st.text_input('Bairro')
                     rua =st.text_input('Rua')
                     nome = st.text_input('Nome')
                     idade = st.text_input('Idade')
                     tipo_de_deficiencia = st.text_input('Tipo de Deficiência')
                     mobilidade = st.text_input('Como é a Mobilidade? Ótimo, Boa, Ruim')
                     dificultadores = st.text_input('Dificultadores')
                     facilitadores = st.text_input('Facilitadores')
                     botao = st.form_submit_button('Entra')


if botao:
    novo = {'Cidade':cidade,'Bairro':bairro,'Rua':rua,'Nome':nome,'Idade':idade,'Tipo de Deficiência':tipo_de_deficiencia,'Mobilidade':mobilidade,'Dificultadores':dificultadores,'Facilitadores':facilitadores}
    df = df.append(novo, ignore_index = True)
    #st.dataframe(df) #verificar se acrescentou o nome
    df.to_csv(dados.name, index = False, sep = ';')




    
# Outra forma de fazer
##def limpar ():
##    st.session_state['cidade'] = ''
##    st.session_state['bairro'] = ''
##    st.session_state['rua'] = ''
##    st.session_state['nome'] = ''
##    st.session_state['idade'] = ''
##    st.session_state['tipo_deficiencia'] = ''
##    st.session_state['dificultadores'] = ''
##    st.session_state['facilitadores'] = ''
##
##
##C = st.text_input('Cidade', key = 'cidade')
##B = st.text_input('Bairro', key = 'bairro')
##R = st.text_input('Rua', key = 'rua')
##NM = st.text_input('Nome', key = 'nome')
##I = st.text_input('Idade', key = 'idade')
##TD = st.text_input('Tipo de Deficiência', key 'tipo_deficiencia')
##M = st.text_input('Como é a Mobilidade? Ótimo, Boa, Ruim', key = 'mobilidade')
##D = ('Dificultadores', key = 'dificultadores')
##F = ('Facilitadores', key = 'facilitadores')
##                     
##st.write(C)
##st.write(B)
##st.write(R)
##st.write(NM)
##st.write(I)
##st.write(TD)
##st.write(M)
##st.write(D)
##st.write(F)
##
##bt = st.button('Limpar',on_click = limpar)
