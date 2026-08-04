# Introdução à Programação com Python

Material didático para pessoas sem formação prévia em computação. O curso apresenta os fundamentos da programação com Python por meio de notebooks executáveis, exercícios e videoaulas.

O objetivo é desenvolver raciocínio algorítmico, leitura de código e autonomia para construir pequenos programas. Estatística, análise de dados, inteligência artificial e coleções de algoritmos foram separados em repositórios próprios para preservar o foco deste curso.

## Conteúdo

O percurso principal está em [`aulas_algoritmos_programacao/`](aulas_algoritmos_programacao/):

1. sintaxe e primeiros comandos;
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

O catálogo detalhado está em [CONTENTS.md](CONTENTS.md). A sequência pedagógica recomendada e as melhorias planejadas estão em [COURSE.md](COURSE.md).

## Videoaulas publicadas

| Vídeo | Link | Material relacionado |
|---:|---|---|
| 1 | [YouTube](https://www.youtube.com/watch?v=oaKXsIK8768) | A relacionar |
| 2 | [YouTube](https://www.youtube.com/watch?v=dLDmXewxwpA) | A relacionar |
| 3 | [YouTube](https://www.youtube.com/watch?v=Vn45DCpdXNw) | A relacionar |
| 4 | [Introdução à programação com Python](https://www.youtube.com/watch?v=oclZGqDb9R0) | [`01_intro_sintaxe_python.ipynb`](aulas_algoritmos_programacao/01_intro_sintaxe_python.ipynb) |
| 5 | [YouTube](https://www.youtube.com/watch?v=Etwy8F1cmzA) | A relacionar |

A lista contém apenas vídeos distintos; o endereço da aula introdutória havia sido informado duas vezes.

## Como executar

```bash
conda env create -f requirements.yml
conda activate programacao-introducao
jupyter lab
```

Os notebooks devem ser executados na ordem das células. Exemplos que produzem erros deliberados são usados para discutir exceções e devem estar identificados no próprio material.

## Verificação

```bash
python -m unittest discover -s tests -v
```

Os testes atuais verificam a integridade estrutural dos notebooks. A execução automatizada completa ainda é uma melhoria planejada.

## Repositórios relacionados

- [`stats_elementary`](https://github.com/ozsp12/stats_elementary) — estatística elementar;
- [`algoritmos_educam`](https://github.com/ozsp12/algoritmos_educam) — problemas e algoritmos comentados;
- [`ai_data_citizen`](https://github.com/ozsp12/ai_data_citizen) — alfabetização em dados e inteligência artificial;
- [`data_analytics_excel`](https://github.com/ozsp12/data_analytics_excel) — análise de dados aplicada com Excel.

## Referências

- [REFERENCES.md](REFERENCES.md) — bibliografia;
- [CITATION.cff](CITATION.cff) — metadados para citação;
- [LICENSE](LICENSE) — licença MIT.

## Autor

**Dr. Osvaldo L. Santos-Pereira** — [Webpage](https://ozsp12.github.io/) · [Lattes](http://lattes.cnpq.br/6730251976463283) · [ORCID](https://orcid.org/0000-0003-2231-517X) · [GitHub](https://github.com/ozsp12) · [YouTube](https://www.youtube.com/@ozlsp12)
