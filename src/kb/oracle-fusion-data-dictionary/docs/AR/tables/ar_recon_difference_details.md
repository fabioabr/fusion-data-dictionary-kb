---
id: DOC-AR-061
doc_type: system-doc
title: "AR_RECON_DIFFERENCE_DETAILS — Diferenças na Reconciliação AR vs GL"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, reconciliacao, diferencas, ar-gl]
aliases: [AR_RECON_DIFFERENCE_DETAILS, ar_recon_difference_details, recon_differences, diferencas_reconciliacao, diff_ar_gl]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECON_DIFFERENCE_DETAILS

## 📌 Visão Geral

Tabela de detalhes das diferenças encontradas durante o processo de reconciliação entre o subledger de Accounts Receivable e o General Ledger. Cada registro identifica uma transação ou lançamento específico que contribui para a discrepância entre AR e GL.

## 🧠 Propósito de Negócio

Quando a reconciliação AR vs GL identifica diferenças, esta tabela fornece o detalhe transação a transação, permitindo investigação e correção. É essencial para: (1) identificar transações não transferidas ao GL, (2) localizar lançamentos manuais no GL sem correspondência no AR, (3) detectar erros de postagem, (4) suportar auditoria de fechamento contábil.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | RECON_DIFFERENCE_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do registro de diferença. | PK | 🟢 100% |
| 2 | RECON_ID | NUMBER(15) | NOT NULL | FK para [[ar_recon_summary_details]]. Resumo da reconciliação. | FK | 🟢 100% |
| 3 | SOURCE_TYPE | VARCHAR2(30) | NOT NULL | Tipo de fonte da diferença (AR_SUBLEDGER ou GL_JOURNAL). | Classificação | 🟢 100% |
| 4 | SOURCE_ID | NUMBER(15) | NULL | Identificador da transação/lançamento de origem. | FK | 🟢 100% |
| 5 | SOURCE_TABLE | VARCHAR2(30) | NULL | Nome da tabela de origem do registro (ex.: RA_CUSTOMER_TRX_ALL). | Técnico | 🟢 100% |
| 6 | AMOUNT | NUMBER | NULL | Valor da diferença na moeda funcional. | Financeiro | 🟢 100% |
| 7 | ENTERED_AMOUNT | NUMBER | NULL | Valor da diferença na moeda da transação. | Financeiro | 🟢 100% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NULL | Código da moeda da transação. | Financeiro | 🟢 100% |
| 9 | CODE_COMBINATION_ID | NUMBER(15) | NULL | FK para GL_CODE_COMBINATIONS. Conta contábil afetada. | FK | 🟡 75% |
| 10 | TRANSACTION_DATE | DATE | NULL | Data da transação de origem. | Temporal | 🟡 75% |
| 11 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 13 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 15 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **[[ar_recon_summary_details]]** — Resumo da reconciliação (N:1 via `RECON_ID`).
- **[[ar_recon_summary_parameters]]** — Parâmetros da execução (via join com `ar_recon_summary_details`).
- **GL_CODE_COMBINATIONS** — Conta contábil afetada (N:1 via `CODE_COMBINATION_ID`).

## 📎 Uso Típico

```sql
-- Detalhamento das diferenças de reconciliação por período
SELECT rdd.RECON_DIFFERENCE_ID,
       rdd.SOURCE_TYPE,
       rdd.SOURCE_TABLE,
       rdd.SOURCE_ID,
       rdd.AMOUNT,
       rdd.CURRENCY_CODE
  FROM AR_RECON_DIFFERENCE_DETAILS rdd
  JOIN AR_RECON_SUMMARY_DETAILS rsd
    ON rsd.RECON_ID = rdd.RECON_ID
 WHERE rsd.PERIOD_NAME = :p_periodo
   AND rdd.ORG_ID = :p_org_id
 ORDER BY ABS(rdd.AMOUNT) DESC;
```

## 🔒 Observações

- `SOURCE_TABLE` e `SOURCE_ID` permitem rastrear a transação original que gerou a diferença.
- Diferenças podem ser causadas por: transações não transferidas, journals manuais, erros de câmbio ou ajustes pós-fechamento.
- Utilizar em conjunto com [[ar_recon_summary_details]] para visão macro + micro das diferenças.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Subledger to GL Reconciliation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
