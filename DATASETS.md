# Datasets

Files are kept close to the notebooks that consume them. The notebooks use relative paths; run them from their respective directories.

| Path | Use | Notes |
|---|---|---|
| `introducao_estatistica/dataset_instrucional.csv` | Instructional statistics examples | Small instructional dataset |
| `introducao_estatistica/carteira_medicina_familia_sintetica.csv` | Applied statistics studies | Data declared synthetic by the filename; do not treat as real medical records |
| `introducao_estatistica/UCI_Credit_Card.csv` | Default classification | Derived from *Default of Credit Card Clients*, UCI ML Repository, DOI: [10.24432/C55S3H](https://doi.org/10.24432/C55S3H), CC BY 4.0 |
| `introducao_estatistica/UCI_Cartao_Credito.csv` | Transformed version for lessons | Derived output from the UCI dataset; preserve the original attribution |
| `introducao_estatistica/df_paradoxo_simpson.csv` | Simpson's paradox demonstration | Teaching material |
| `introducao_estatistica/tabela_exercicio_simpson.csv` | Aggregation exercise | Teaching material |
| `data_citizen/analise_dados_com_duckdb/*.csv` | Events, subscriptions, and videos | Instructional data used in DuckDB queries |
| `data_citizen/fast_track/df_fast_track.csv` | Analysis and visualization | Large file; load only the required columns when possible |
| `data_citizen/fast_track/df_fast_track.parquet` | Columnar version of *fast track* | Requires `pyarrow`; more efficient than CSV for selective reads |
| `data_citizen/fast_track/fast_track.pbix` | Power BI report | Proprietary binary format; requires Power BI Desktop for editing |

## Limitations

- The repository did not originally document the provenance of all instructional files. Do not assume an open license for data without explicit provenance.
- The synthetic family-medicine file is large. Operations that load all columns may require substantial memory.
- Do not include personal data, credentials, or real clinical data in exercises derived from this material.
