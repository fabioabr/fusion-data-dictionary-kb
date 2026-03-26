# Passo 02 — Extrair Dados de PVOs

## Objetivo

Extrair dados de PVOs (Public View Objects) do Excel BICC e gerar arquivos .json por PVO com estrutura padronizada.

## DOR (Definition of Ready)

- Arquivos Excel BICC disponiveis em `src/raw-files/`
- Python 3.12+ com openpyxl instalado

## DOD (Definition of Done)

- Um arquivo .json por PVO no diretorio do modulo correspondente
- Cada .json contem: meta (name, module, description:null), attributes[]
- Todos os PVOs do Excel foram extraidos sem erro

## Entrada

- `scripts/config/modules.json` (fontes Excel)
- `src/raw-files/Rel13_25A_BICC_FSCM_Database_Mapping_with_ViewObjects.xlsx`
- `src/raw-files/Rel13_25A_BICC_HCM_Database_Mapping_with_ViewObjects.xlsx`

## Saida

- `src/kb/oracle-fusion-data-dictionary/docs/{MODULE}/pvos/{PVO_NAME}.json`

## Requer LLM

Nao.

## Uso

```bash
python scripts/02-extract-pvos/extract_pvos.py
python scripts/02-extract-pvos/extract_pvos.py --module HCM
python scripts/02-extract-pvos/extract_pvos.py --dry-run
```

## Notas

- O campo `meta.description` e gerado como null; sera preenchido no passo 04
- Atributos incluem: name, type, nullable, description
- O modulo e inferido a partir do nome do PVO ou aba do Excel
- Re-execucao e segura: sobrescreve apenas se conteudo mudou
