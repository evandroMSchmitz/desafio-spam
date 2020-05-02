import argparse
import datetime

import matplotlib.pyplot as plt
import pandas as pd

def exercicio_01(dataframe, filename='grafico_barras'):
    words_df = dataframe.iloc[:, 2:-4]
    words = {i: words_df[i].sum() for i in words_df}
    # limpar qualquer figura que exista
    plt.close()
    plt.figure(figsize=(20,25))
    plt.title('Frequência de palavras')
    plt.barh(list(words.keys()), words.values())
    plt.ylabel('Palavra')
    plt.xlabel('Frequência')
    # Exibir o quadriculado no gráfico
    plt.grid(True)
    plt.savefig(f'{filename}.png')

def exercicio_02(dataframe, filename='grafico_linhas'):
    # Adição de coluna extra para representar o mês e o ano. Se a base tiver anos diferentes, ista dá uma certa segurança 
    dataframe['year_month'] = create_year_month_series(dataframe)
    
    # Forma de pegar a contagem de sms agrupada por mes/ano
    sms_count_per_month = dataframe.groupby(['year_month'])['IsSpam'].value_counts().unstack()

    # montagem da lista que vai ser usada para as marcações no eixo X
    xticks = [f'{year_month[1]}/{year_month[0]}' for year_month in sms_count_per_month.index]
    # limpar qualquer figura que exista
    plt.close()
    plt.title('Quantidade de mensagens por mês')
    plt.xlabel('Mês/Ano')
    plt.ylabel('Quantidade')
    plt.plot(xticks, sms_count_per_month['yes'], marker='.', color='red', label='Spam')
    plt.plot(xticks, sms_count_per_month['no'], marker='.', color='blue', label='Mensagem Comum')
    lgd = plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    # Exibir o quadriculado no gráfico
    plt.grid(True)
    # bbox_inches - usado pra printar a legenda sem cortar (https://stackoverflow.com/a/42303455)
    plt.savefig('grafico_linhas.png', bbox_inches='tight')

def exercicio_03(dataframe):
    dataframe['year_month'] = create_year_month_series(dataframe)


    word_count_per_month = dataframe.groupby(['year_month'])['Word_Count'].agg(['min', 'max', 'mean', 'median', 'std', 'var'])
    word_count_per_month.reset_index(inplace=True)
    print('Estatísticas dos dados')
    for row in word_count_per_month.values:
        print(f'Estatísticas mês {row[0][1]} de {row[0][0]}')
        print(f'\tValor mínimo {row[1]}')
        print(f'\tValor máximo: {row[2]}')
        print(f'\tMédia: {row[3]}')
        print(f'\tMediana: {row[4]}')
        print(f'\tDesvio Padrão: {row[5]}')
        print(f'\tVariância: {row[6]}')

def exercicio_04(dataframe):
    dataframe['year_month'] = create_year_month_series(dataframe)

    not_spam = dataframe.loc[dataframe['IsSpam'] == 'no'].copy()
    not_spam['date'] = pd.Series([date.date() for date in dataframe.iloc[:, -3]])

    sms_per_day = not_spam.groupby(['year_month'])['date'].value_counts().to_frame()
    sms_per_day = sms_per_day.rename(columns={'date': 'total_sms'})
    # a ideia pra lidar com esta parte do código veio daqui: https://datascience.stackexchange.com/a/30845
    sms_per_day.reset_index(inplace=True)
    max_msm_day_month = sms_per_day.groupby(['year_month'])['total_sms'].idxmax()
    day_month_more_commun_sms = sms_per_day.loc[max_msm_day_month]
    print('Dias dos messes com mais mensagens comuns')
    for row in day_month_more_commun_sms.values:
        print(f'\tNo mês {row[1].month} de {row[1].year} o dia com mais mensagens foi {row[1].day} com um total de {row[2]} mensagens')

def create_year_month_series(dataframe):
    return pd.Series([(date.year, date.month) for date in dataframe.iloc[:, -2]])

# Argumentos para rodar o exercício
parser = argparse.ArgumentParser()
   
parser.add_argument(
    '-o', 
    '--operation', 
    type=str,
    required=False,
    choices=['pe1', 'pe2', 'pe3', 'pe4'],
    help='Executa um dos 4 exercícios da primeira etapa. Se não for informado, todos os exercícios serão executados')

parser.add_argument(
    '-f', 
    '--filename', 
    type=str,
    default='sms_senior.csv',
    help='Nome do arquivo csv que será usado como base de dados')

args = parser.parse_args()

# função para conversão de data
dateparse = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
dataframe = pd.read_csv(
    args.filename, 
    encoding='latin1', 
    parse_dates=['Date'], 
    date_parser=dateparse)

if args.operation == 'pe1':
    exercicio_01(dataframe.copy())
elif args.operation == 'pe2':
    exercicio_02(dataframe.copy())
elif args.operation == 'pe3':
    exercicio_03(dataframe.copy())
elif args.operation == 'pe4':
    exercicio_04(dataframe.copy())
else:
    exercicio_01(dataframe.copy())
    exercicio_02(dataframe.copy())
    exercicio_03(dataframe.copy())
    exercicio_04(dataframe.copy())
