import streamlit as st
import requests
import pandas as pd

st.title('DADOS BRUTOS')

url = 'https://labdados.com/produtos'

response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())
dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format = '%d/%m/%Y')

with st.expander('Colunas'):
	colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))

st.sidebar.title('Filtros')
with st.sidebar.expander('Nome do produto'):
	produtos = st.multiselect('Selecione os produtos', dados['Produto'].unique(), dados['Produto'])
with st.sidebar.expander('Preço do produto'):
	preco = st.slider('Selecione o preço', 0, 5000, (0,5000))
with st.sidebar.expander('Data da compra'):
	data_compra = st.date_input('Selecione a data', (dados['Data da Compra'].min(), dados['Data da Compra'].max()))
with st.sidebar.expander('Vendedor'):
	data_compra = st.date_input('Selecione os vendedores', (dados['Vendedor'].unique(), dados['Vendedor'].max()))
with st.sidebar.expander('Local da compra'):
	data_compra = st.date_input('Selecione o local da compra', (dados['Local da compra'].unique(), dados['Local da compra'].max()))
with st.sidebar.expander('Avaliação da compra'):
	data_compra = st.date_input('Selecione a avaliação da compra', 1, 5, value = (1,5))
with st.sidebar.expander('Tipo de pagamento'):
	data_compra = st.date_input('Selecione o tipo de pagamento', (dados['Tipo de pagamento'].unique(), dados['Tipo de pagamento'].max()))
with st.sidebar.expander('Quantidade de parcelas'):
	data_compra = st.date_input('Selecione a quantidade de parcelas', 1, 24, (1,24))

query = '''
Produto in @produtos and \
@preco[0] <= Preço <= @preco[1] and \
@data_compra[0] <= `Data de compra` <= @data_compra[1]
'''

dados_filtrados = dados.query(query)
dados_filtrados = dados_filtrados[colunas]

st.dataframe(dados_filtrados)

st.markdown(f'A tabela possui :blue[{dados_filtrados.shape[0]}] linhas e :blue[{dados_filtrados.shape[1]}] colunas')
