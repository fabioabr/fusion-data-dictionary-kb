# Passo 01 — Extrair Metadados de Tabelas

## Objetivo

Extrair metadados de tabelas (nome, colunas, tipos, nullable) dos arquivos Excel BICC do Oracle Fusion e gerar esqueletos .md por tabela.

## DOR (Definition of Ready)

- Arquivos Excel BICC disponiveis em `src/raw-files/`
- Arquivo `table-mappings.txt` preenchido com mapeamento tabela → modulo
- Python 3.12+ com openpyxl instalado

## DOD (Definition of Done)

- Um arquivo .md por tabela no diretorio do modulo correspondente
- Cada .md contem: nome, colunas, tipos, nullable, flags (PK/FK/DFF/WHO)
- Nenhuma tabela do mapeamento ficou sem arquivo gerado
- Front matter basico presente (id, title, doc_type, status: draft)

## Entrada

- `scripts/config/modules.json` (fontes Excel)
- `src/raw-files/Rel13_25A_BICC_FSCM_Database_Mapping_with_ViewObjects.xlsx`
- `src/raw-files/Rel13_25A_BICC_HCM_Database_Mapping_with_ViewObjects.xlsx`
- `src/kb/oracle-fusion-data-dictionary/docs/table-mappings.txt`

## Saida

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/tables/{TABLE_NAME}.md`

## Requer LLM

Nao.

## Uso

```bash
python scripts/01-extract-tables/extract_tables.py
python scripts/01-extract-tables/extract_tables.py --module GL
python scripts/01-extract-tables/extract_tables.py --dry-run
```

## Notas

- O script le as abas do Excel que contem mapeamento de colunas
- O `table-mappings.txt` define quais tabelas pertencem a qual modulo
- Tabelas nao mapeadas sao ignoradas com aviso no log
- Re-execucao e segura: sobrescreve apenas se conteudo mudou
