# Introdução à Programação com Python

Este repositório reúne material didático para pessoas sem formação prévia em computação ou ciência de dados. O percurso começa com sintaxe, tipos e controle de fluxo, avança para funções e estruturas de dados e, em módulos independentes, introduz estatística, visualização, análise de dados e SQL com DuckDB.

O objetivo não é apresentar Python como uma coleção de comandos a memorizar. Cada notebook deve ser lido como uma aula prática: executar as células na ordem, modificar exemplos, formular hipóteses e verificar os resultados. Algumas aulas básicas contêm erros deliberados para demonstrar exceções da linguagem; esses casos são identificados no próprio texto.

**Aula 1 no YouTube:** [Introdução à programação com Python](https://www.youtube.com/watch?v=oclZGqDb9R0)

## Percurso principal

O curso introdutório está em [`aulas_algoritmos_programacao/`](aulas_algoritmos_programacao/):

1. sintaxe básica;
2. lógica e operações matemáticas;
3. tipos e variáveis;
4. estruturas condicionais;
5. laços `for` e `while`;
6. funções;
7. recursão;
8. funções lambda;
9. funções aninhadas e *closures*;
10. exercícios integradores;
11. cálculos com listas;
12. dicionários.

Consulte [CONTENTS.md](CONTENTS.md) para o catálogo completo dos notebooks.

## Módulos complementares

| Diretório | Conteúdo |
|---|---|
| [`algoritmos_que_educam/`](algoritmos_que_educam/) | Problemas resolvidos, comparação de métodos e pequenos algoritmos |
| [`bibliotecas_python/`](bibliotecas_python/) | Demonstrações de bibliotecas especializadas |
| [`introducao_estatistica/`](introducao_estatistica/) | Estatística descritiva, probabilidade, inferência e estudos de caso |
| [`data_citizen/`](data_citizen/) | Visualização, dados em painel, DuckDB e material de Power BI |
| [`data_analytics_quick_dirty/`](data_analytics_quick_dirty/) | Estudos exploratórios de análise de negócios |

Os conjuntos de dados, tamanhos, licenças conhecidas e limitações estão documentados em [DATASETS.md](DATASETS.md).

## Ambiente

```bash
conda env create -f requirements.yml
conda activate programacao-introducao
jupyter lab
```

Os notebooks que leem arquivos locais presumem que o diretório de trabalho seja a pasta que contém o notebook e os respectivos dados. Por exemplo:

```bash
cd introducao_estatistica
jupyter lab
```

Para o módulo DuckDB:

```bash
cd data_citizen/analise_dados_com_duckdb
jupyter lab analise.ipynb
```

Essa convenção evita caminhos absolutos dependentes de uma máquina específica.

## Verificação estrutural

```bash
python -m unittest discover -s tests -v
```

Os testes verificam se todos os notebooks são documentos JSON válidos, usam o formato Jupyter esperado e possuem células bem formadas. Isso não equivale a executar integralmente todos os cursos: alguns materiais dependem de arquivos grandes, Power BI, `ffmpeg` ou de exemplos que geram exceções de propósito.

## Uso pedagógico de IA

Ferramentas generativas podem auxiliar na explicação de mensagens de erro, criação de exercícios e revisão de código. O resultado deve ser executado, testado e confrontado com a documentação oficial. Código plausível não é necessariamente código correto — uma lição simples que muitos projetos aprendem tarde.

## Referências e dados

- [REFERENCES.md](REFERENCES.md) — bibliografia do curso.
- [DATASETS.md](DATASETS.md) — inventário e proveniência dos dados.
- [CITATION.cff](CITATION.cff) — metadados para citação do repositório.

## Autor

**Dr. Osvaldo L. Santos-Pereira** — [Academic webpage](https://ozsp12.github.io/) · [Lattes](http://lattes.cnpq.br/6730251976463283) · [ORCID](https://orcid.org/0000-0003-2231-517X) · [Google Scholar](https://scholar.google.com/citations?user=HIZp0X8AAAAJ&hl=en) · [ResearchGate](https://www.researchgate.net/profile/Osvaldo-Santos-Pereira) · [GitHub](https://github.com/ozsp12) · [LinkedIn](https://www.linkedin.com/in/ozsp12) · [Substack](https://substack.com/@olsp1982) · [Medium](https://medium.com/@ozsp12) · [YouTube](https://www.youtube.com/@ozlsp12) · [X](https://x.com/ozsp12)

## Licença

O código e a documentação autoral deste repositório são distribuídos sob a [Licença MIT](LICENSE). Dados, artigos, PDFs, arquivos Power BI e outros materiais de terceiros permanecem sujeitos às licenças e aos termos de suas fontes originais.
