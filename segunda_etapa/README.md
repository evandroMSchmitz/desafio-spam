# Segunda Etapa
Segunda etapa do desafio que consiste em escolher avaliar um método para classificar automáticamente as mensagens em spam ou não. O método usado foi um KNN.

## Setup
``` terminal
pip install -r requirements.txt
```
## Executando
``` terminal
python segunda_etapa.py
```
Este arquivo aceita os seguintes argumentos:
| Parâmetro        | Significado   | Valor padrão  |
| ---------------- |:-------------:| -----:|
| -n ou --neighbors| Permite especificar o número de vizinhos utilizado como argumento para o algoritmo KNN | 3 |
| -f ou --filename | Nome do arquivo que representa a base de dados | sms_senior.csv |

### Saídas no Console
Ao final da execução é exibido no console uma mensagem com o _score_ de acerto do algoritmo.
