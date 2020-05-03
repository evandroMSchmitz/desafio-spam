import argparse
import datetime

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Argumentos para rodar o exercício
parser = argparse.ArgumentParser()
   
parser.add_argument(
    '-n', 
    '--neighbors', 
    type=int,
    default=3,
    help='Número de vizinhos para utilizar no KNN para a classificação dos dados')

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

X, y = dataframe.iloc[:, 1:-4].copy(), dataframe.iloc[:, -1].copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knnClassifier = KNeighborsClassifier(n_neighbors=args.neighbors)
knnClassifier.fit(X_train, y_train)

score = knnClassifier.score(X_test, y_test)
print(f'O score de classificação é {score}')