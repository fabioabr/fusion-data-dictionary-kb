---
id: DOC-AR-033
doc_type: system-doc
title: "AR_AGING_BUCKET_LINES_TL — Traduções das Linhas de Aging"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, aging, traducao, multi-idioma]
aliases: [AR_AGING_BUCKET_LINES_TL, ar_aging_bucket_lines_tl, aging_lines_tl, traducoes_aging, bucket_lines_tl]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_AGING_BUCKET_LINES_TL

## 📌 Visão Geral

Tabela de tradução (Translation Layer) das linhas de faixas de aging. Armazena descrições e cabeçalhos traduzidos para cada idioma instalado na instância Oracle Fusion. Chave composta por `AGING_BUCKET_LINE_ID` + `LANGUAGE`.

## 🧠 Propósito de Negócio

Em ambientes multi-idioma, os nomes e descrições das faixas de aging precisam ser exibidos no idioma do usuário. Esta tabela permite que relatórios de aging e telas de consulta apresentem informações localizadas, essencial para operações internacionais ou ambientes bilíngues.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | AGING_BUCKET_LINE_ID | NUMBER(15) | NOT NULL | PK/FK. Referência à linha base em [[ar_aging_bucket_lines_b]]. | PK/FK | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | Código do idioma (ex.: US, PTBR). Compõe a PK. | PK | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Idioma de origem da tradução. | Controle | 🟢 100% |
| 4 | BUCKET_LINE_DESCRIPTION | VARCHAR2(240) | NULL | Descrição traduzida da linha de aging. | Negócio | 🟢 100% |
| 5 | REPORT_HEADING1 | VARCHAR2(15) | NULL | Cabeçalho traduzido do relatório (linha 1). | Apresentação | 🟡 75% |
| 6 | REPORT_HEADING2 | VARCHAR2(15) | NULL | Cabeçalho traduzido do relatório (linha 2). | Apresentação | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 8 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_aging_bucket_lines_b]]** — Linha base da tradução (N:1 via `AGING_BUCKET_LINE_ID`).
- **[[ar_aging_buckets]]** — Bucket pai (via join com `ar_aging_bucket_lines_b`).

## 📎 Uso Típico

```sql
-- Obter descrições traduzidas das linhas de aging em pt-BR
SELECT bl.BUCKET_SEQUENCE_NUM,
       tl.BUCKET_LINE_DESCRIPTION,
       tl.REPORT_HEADING1
  FROM AR_AGING_BUCKET_LINES_B bl
  JOIN AR_AGING_BUCKET_LINES_TL tl
    ON tl.AGING_BUCKET_LINE_ID = bl.AGING_BUCKET_LINE_ID
   AND tl.LANGUAGE = 'PTBR'
 WHERE bl.AGING_BUCKET_ID = :p_bucket_id
 ORDER BY bl.BUCKET_SEQUENCE_NUM;
```

## 🔒 Observações

- A chave primária é composta: (`AGING_BUCKET_LINE_ID`, `LANGUAGE`).
- Quando `SOURCE_LANG` difere de `LANGUAGE`, indica que a tradução não foi fornecida e o sistema utiliza o idioma base.
- Padrão Oracle MLS (Multi-Language Support): toda tabela `_TL` segue esta estrutura.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle MLS Architecture — Translation Layer Pattern.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
