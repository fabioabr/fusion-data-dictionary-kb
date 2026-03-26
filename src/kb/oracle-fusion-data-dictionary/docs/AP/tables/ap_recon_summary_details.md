---
id: DOC-AP-023
doc_type: system-doc
title: "AP_RECON_SUMMARY_DETAILS — Resumo da Reconciliação AP vs GL"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, reconciliacao, resumo, ap-gl]
aliases: [AP_RECON_SUMMARY_DETAILS, ap_recon_summary_details, recon_summary_ap, resumo_reconciliacao_ap, summary_details_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_RECON_SUMMARY_DETAILS

## Visão Geral

Tabela que armazena os resultados consolidados de cada execução de reconciliação entre o subledger de Accounts Payable e o General Ledger. Cada registro representa um resumo por conta contábil e período, incluindo os saldos do subledger AP, do GL e a diferença apurada.

## Propósito de Negócio

Fornece a visão macro do resultado de reconciliação AP vs GL, permitindo identificar rapidamente quais contas e períodos apresentam diferenças. É o ponto de partida para drill-down nas diferenças detalhadas. Essencial para: (1) fechamento contábil mensal, (2) identificação rápida de contas com discrepância, (3) auditoria interna e externa, (4) monitoramento contínuo de integridade entre subledger e GL.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RECON_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do resumo de reconciliação. | — | 🟢 100% |
| 2 | RECON_HEADER_ID | NUMBER(15) | NOT NULL | FK | FK para os parâmetros da execução de reconciliação. | [[ap_recon_summary_parameters]] | 🟢 95% |
| 3 | CODE_COMBINATION_ID | NUMBER(15) | NOT NULL | FK | FK para [[gl_code_combinations]]. Conta contábil reconciliada. | [[gl_code_combinations]] | 🟢 100% |
| 4 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Temporal | Nome do período contábil (ex.: MAR-26). | — | 🟢 100% |
| 5 | SUBLEDGER_BALANCE | NUMBER | NULL | Financeiro | Saldo apurado no subledger AP para a conta/período. | — | 🟢 95% |
| 6 | GL_BALANCE | NUMBER | NULL | Financeiro | Saldo apurado no General Ledger para a conta/período. | — | 🟢 95% |
| 7 | DIFFERENCE_AMOUNT | NUMBER | NULL | Financeiro | Diferença entre subledger AP e GL (SUBLEDGER_BALANCE - GL_BALANCE). | — | 🟢 95% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda funcional utilizada na reconciliação. | — | 🟢 90% |
| 9 | LEDGER_ID | NUMBER(15) | NULL | FK | FK para GL_LEDGERS. Ledger da reconciliação. | — | 🟡 80% |
| 10 | STATUS | VARCHAR2(30) | NULL | Status | Status da reconciliação (ex.: RECONCILED, UNRECONCILED). | — | 🟡 75% |
| 11 | ORG_ID | NUMBER(15) | NOT NULL | Partição | Identificador da business unit (Operating Unit). | — | 🟢 100% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 13 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_recon_summary_parameters]]** — Parâmetros da execução (N:1 via `RECON_HEADER_ID`).
- **[[gl_code_combinations]]** — Conta contábil reconciliada (N:1 via `CODE_COMBINATION_ID`).

### Tabelas-filha

- **[[ap_recon_difference_details]]** — Detalhes das diferenças encontradas (1:N via `RECON_ID`).

## Uso Típico

```sql
-- Contas com diferenças de reconciliação AP vs GL no período
SELECT rsd.RECON_ID,
       gcc.CONCATENATED_SEGMENTS,
       rsd.SUBLEDGER_BALANCE,
       rsd.GL_BALANCE,
       rsd.DIFFERENCE_AMOUNT,
       rsd.CURRENCY_CODE
  FROM AP_RECON_SUMMARY_DETAILS rsd
  JOIN GL_CODE_COMBINATIONS gcc
    ON gcc.CODE_COMBINATION_ID = rsd.CODE_COMBINATION_ID
 WHERE rsd.PERIOD_NAME = :p_periodo
   AND rsd.ORG_ID = :p_org_id
   AND rsd.DIFFERENCE_AMOUNT <> 0
 ORDER BY ABS(rsd.DIFFERENCE_AMOUNT) DESC;
```

## Observações

- Para cada registro com diferença, consultar [[ap_recon_difference_details]] para o drill-down transação a transação.
- Estrutura análoga a [[ar_recon_summary_details]] do módulo AR.
- O campo `STATUS` indica se a diferença já foi investigada e resolvida.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Subledger to GL Reconciliation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
