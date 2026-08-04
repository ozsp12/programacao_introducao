# Conjuntos de dados

Os arquivos são mantidos próximos aos notebooks que os consomem. Os notebooks usam caminhos relativos; execute-os a partir do respectivo diretório.

| Caminho | Uso | Observação |
|---|---|---|
| `introducao_estatistica/dataset_instrucional.csv` | Exemplos didáticos de estatística | Conjunto instrucional pequeno |
| `introducao_estatistica/carteira_medicina_familia_sintetica.csv` | Estudos de estatística aplicada | Dados declarados como sintéticos pelo nome do arquivo; não tratar como prontuário real |
| `introducao_estatistica/UCI_Credit_Card.csv` | Classificação de inadimplência | Derivado de *Default of Credit Card Clients*, UCI ML Repository, DOI: [10.24432/C55S3H](https://doi.org/10.24432/C55S3H), licença CC BY 4.0 |
| `introducao_estatistica/UCI_Cartao_Credito.csv` | Versão transformada para as aulas | Saída derivada do conjunto UCI; preservar a atribuição original |
| `introducao_estatistica/df_paradoxo_simpson.csv` | Demonstração do paradoxo de Simpson | Material didático |
| `introducao_estatistica/tabela_exercicio_simpson.csv` | Exercício sobre agregação | Material didático |
| `data_citizen/analise_dados_com_duckdb/*.csv` | Eventos, assinaturas e vídeos | Dados instrucionais usados nas consultas DuckDB |
| `data_citizen/fast_track/df_fast_track.csv` | Análise e visualização | Arquivo grande; carregar apenas as colunas necessárias quando possível |
| `data_citizen/fast_track/df_fast_track.parquet` | Versão colunar do *fast track* | Requer `pyarrow`; mais eficiente que CSV para leitura seletiva |
| `data_citizen/fast_track/fast_track.pbix` | Relatório Power BI | Formato binário proprietário; requer Power BI Desktop para edição |

## Limitações

- O repositório não documentava originalmente a origem de todos os arquivos instrucionais. Não se deve presumir licença aberta para dados sem proveniência explícita.
- O arquivo sintético de medicina da família é grande. Operações que carregam todas as colunas podem exigir memória considerável.
- Não inclua dados pessoais, credenciais ou dados clínicos reais em exercícios derivados deste material.
