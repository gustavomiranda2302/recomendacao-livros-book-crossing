# Sistema de Recomendação de Livros — Book-Crossing

Este projeto foi desenvolvido com o objetivo de aplicar técnicas de mineração de dados e aprendizado de máquina na construção de um sistema de recomendação de livros, utilizando a base de dados Book-Crossing.

A proposta é analisar as avaliações realizadas pelos usuários, identificar padrões de comportamento e desenvolver modelos capazes de prever a nota que um usuário poderia atribuir a determinado livro.

## Objetivos

- Explorar e compreender a base de dados Book-Crossing.
- Realizar a limpeza e o tratamento dos dados.
- Analisar padrões de comportamento dos usuários e avaliações dos livros.
- Desenvolver e comparar diferentes modelos de recomendação.
- Avaliar os modelos utilizando métricas de erro.
- Selecionar o modelo com melhor desempenho.

## Base de dados

O projeto utiliza o dataset Book-Crossing, composto por três conjuntos principais:

| Arquivo | Descrição |
|---|---|
| `Books.csv` | Informações sobre os livros, como ISBN, título, autor e ano de publicação. |
| `Users.csv` | Informações dos usuários, como identificador, idade e país. |
| `Ratings.csv` | Avaliações realizadas pelos usuários para os livros. |

As avaliações representam as interações entre usuários e livros e são utilizadas na construção dos modelos de recomendação.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Jupyter Notebook
- FastAPI

## Estrutura do projeto

```text
recomendacao-livros-book-crossing/
│
├── models/
│   ├── data/
│   │   ├── original/
│   │   └── clean/
│   │
│   └── notebooks/
│       ├── 01_exploracao.ipynb
│       ├── 02_limpeza.ipynb
│       ├── 03_visualizacao.ipynb
│       └── 04_modelagem.ipynb
│
├── download.py
└── README.md
```

## Etapas do projeto

### 1. Exploração dos dados

Nesta etapa, foi realizada uma análise inicial das bases, buscando compreender sua estrutura, identificar características importantes e observar a distribuição das avaliações e dos usuários.

Notebook: `01_exploracao.ipynb`

### 2. Limpeza e preparação dos dados

Foram realizadas as etapas de tratamento e organização dos dados, incluindo a identificação de inconsistências e a preparação das informações para utilização nos modelos.

Os dados tratados foram organizados e armazenados no formato Parquet.

Notebook: `02_limpeza.ipynb`

### 3. Análise e visualização

Foram desenvolvidas visualizações para compreender melhor a distribuição das avaliações, as características dos usuários e dos livros e possíveis padrões presentes na base.

Notebook: `03_visualizacao.ipynb`

### 4. Modelagem

Nesta etapa, foram desenvolvidos e comparados diferentes modelos para prever as avaliações dos usuários.

Entre as abordagens utilizadas estão:

- Média global;
- Média por usuário;
- Média por livro;
- KNN Item-Item com similaridade de cosseno;
- KNN com correção pelas médias de usuários e livros;
- TruncatedSVD;
- Random Forest Regressor.

Notebook: `04_modelagem.ipynb`

## Resultados dos modelos

Para comparar os modelos, foram utilizadas duas métricas:

- **RMSE (Root Mean Squared Error):** calcula a raiz do erro quadrático médio, atribuindo maior peso a erros mais elevados.
- **MAE (Mean Absolute Error):** calcula a média dos erros absolutos entre as avaliações reais e previstas.

Os resultados obtidos foram:

| Modelo | RMSE | MAE |
|---|---:|---:|
| Random Forest | **1,563** | **1,198** |
| TruncatedSVD | 1,599 | 1,234 |
| Média por usuário | 1,601 | 1,237 |
| KNN com médias | 1,620 | 1,220 |
| KNN simples | 1,634 | 1,209 |
| Média global | 1,788 | 1,426 |
| Média por livro | 1,828 | 1,437 |

### Modelo selecionado: Random Forest

Entre os modelos avaliados, o Random Forest Regressor apresentou os melhores resultados, considerando tanto RMSE quanto MAE.

O modelo foi configurado com os seguintes parâmetros:

- `n_estimators=200`
- `max_depth=12`
- `min_samples_leaf=20`
- `random_state=42`

Para realizar as previsões, foram utilizadas informações relacionadas aos usuários e aos livros, como médias e quantidades de avaliações, idade do usuário, país e década de publicação do livro.

Com base nos resultados, o Random Forest foi escolhido como o modelo principal do projeto.

## API

A disponibilização do sistema por meio de uma API REST utilizando FastAPI está em desenvolvimento.

## Considerações finais

O desenvolvimento deste projeto permitiu explorar diferentes técnicas de mineração de dados e aprendizado de máquina aplicadas a sistemas de recomendação.

A comparação entre os modelos mostrou que o Random Forest apresentou o melhor desempenho entre as abordagens testadas, demonstrando bons resultados na previsão das avaliações dos usuários.

O projeto também proporcionou a oportunidade de trabalhar com diferentes etapas de um processo de ciência de dados, desde a exploração e preparação dos dados até a construção e avaliação dos modelos.

---

**Desenvolvido por:** [Gustavo Miranda](https://github.com/gustavomiranda2302)

**Repositório:** [recomendacao-livros-book-crossing](https://github.com/gustavomiranda2302/recomendacao-livros-book-crossing)