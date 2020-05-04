# Primeira Etapa

Primeira etapa do desafio que consiste em extratir estatísticas de uma base de dados e gerar gráficos.

## Setup
``` terminal
pip install -r requirements.txt
```
## Executando
``` terminal
python primeira_etapa.py
```
Este arquivo aceita os seguintes argumentos:
| Parâmetro        | Significado   | Valor padrão  |
| ---------------- |:-------------:| -----:|
| -o ou --operation| Permite especificar uma das 4 atividades para executar. Caso não seja informado as 4 atividades vão executar em sequência. Os valores aceitos são: pe1, pe2, pe3 e pe4. Estes parâmetros são referentes as atividades 1, 2, 3 e 4 da primeira etapa, respectivamente | não possui |
| -f ou --filename | Nome do arquivo que representa a base de dados | sms_senior.csv |

### Imagens Geradas
As atividades 1 e 2 geram um gráfico de barras e um gráfico de linha. O gráfico para a atividade 1 terá nome de _grafico_barras.png_ e o gráfico da atividade 2 terá o nome de _grafico_linhas.png_.

### Saídas no Console
As atividades 3 e 4 geram saídas no console.
