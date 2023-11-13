import streamlit as st
import pandas as pd
#pip install -U scikit-learn
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from PIL import Image

image = Image.open('plantas.png')

st.sidebar.image(image, caption='Classificador', channels="RGB")

citros = pd.read_csv('citros.csv',sep = ';')
x = citros.iloc[:,:2] # dados
y = citros.iloc[:,3] #coluna das classes 0-1-2
nomes = citros.iloc[:,2] #Nomes: 0- laranja, 1- limão

st.title ('Classificador das Folhas de Citros')
st.subheader('Aplicativo p/ identificar se a folha se refere a laranjeira ou limão'
             ' de acordo com os parâmetros de entrada!!')

st.sidebar.header('Parâmetros de Entrada') #sidebar mostra os dados do lado esquerdo da tela


def parametros():
    Comp_Folha = st.sidebar.slider('Comprimento da Folha', 7.3, 10.6, 8.6)
    Larg_Folha = st.sidebar.slider('largura da Folha', 3.2, 6.5, 4.6)       
   
    data = {'Comp_Folha': Comp_Folha,
            'Larg_Folha': Larg_Folha,
            }
    dados = pd.DataFrame(data,index = [0])
    return dados

st.header('Dados do parâmetros de Entrada')
df = parametros()
st.write (df)


clf = RandomForestClassifier() #Criar o classificador
clf.fit(x,y) # Passar os valores de x e y para o classificador

predicao = clf.predict(df)

prob_predicao = clf.predict_proba(df)

st.subheader ('Predição:')
if predicao == 0:
    st.write('Laranja')
else:
    st.write('Limao')
             
st.subheader ('Probabilidades de Predição:')

col1,col2 = st.columns(2)
col1.write('Laranja')
col1.write(prob_predicao[0,0])

col2.write('Limao')
col2.write(prob_predicao[0,1])

