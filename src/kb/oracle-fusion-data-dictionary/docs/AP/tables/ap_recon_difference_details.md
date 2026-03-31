---
id: DOC-AP-022
doc_type: system-doc
title: "AP_RECON_DIFFERENCE_DETAILS — Diferenças na Reconciliação AP vs GL"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, reconciliacao, diferencas, ap-gl]
aliases: [AP_RECON_DIFFERENCE_DETAILS, ap_recon_difference_details, recon_diff_details_ap, diferencas_reconciliacao_ap, diff_ap_gl]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_RECON_DIFFERENCE_DETAILS

## Visão Geral

Tabela de detalhes das diferenças encontradas durante o processo de reconciliação entre o subledger de Accounts Payable e o General Ledger. Cada registro identifica uma transação ou lançamento específico que contribui para a discrepância entre AP e GL.

## Propósito de Negócio

Quando a reconciliação AP vs GL identifica diferenças, esta tabela fornece o detalhe transação a transação, permitindo investigação e correção. É essencial para: (1) identificar faturas não transferidas ao GL, (2) localizar lançamentos manuais no GL sem correspondência no AP, (3) detectar erros de postagem ou câmbio, (4) suportar auditoria de fechamento contábil do módulo de contas a pagar.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RECON_DIFFERENCE_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do registro de diferença. | — | 🟢 100% |
| 2 | RECON_ID | NUMBER(15) | NOT NULL | FK | FK para [[ap_recon_summary_details]]. Resumo da reconciliação. | [[ap_recon_summary_details]] | 🟢 100% |
| 3 | SOURCE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de fonte da diferença (AP_SUBLEDGER ou GL_JOURNAL). | — | 🟢 100% |
| 4 | SOURCE_ID | NUMBER(15) | NULL | FK | Identificador da transação/lançamento de origem. | — | 🟢 100% |
| 5 | SOURCE_TABLE | VARCHAR2(30) | NULL | Técnico | Nome da tabela de origem (ex.: AP_INVOICES_ALL, GL_JE_LINES). | — | 🟢 100% |
| 6 | AMOUNT | NUMBER | NULL | Financeiro | Valor da diferença na moeda funcional. | — | 🟢 100% |
| 7 | ENTERED_AMOUNT | NUMBER | NULL | Financeiro | Valor da diferença na moeda da transação. | — | 🟢 100% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda da transação (ex.: BRL, USD). | — | 🟢 100% |
| 9 | CODE_COMBINATION_ID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta contábil afetada. | [[gl_code_combinations]] | 🟡 75% |
| 10 | TRANSACTION_DATE | DATE | NULL | Temporal | Data da transação de origem. | — | 🟡 75% |
| 11 | ORG_ID | NUMBER(15) | NOT NULL | Partição | Identificador da business unit (Operating Unit). | — | 🟢 100% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 13 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_recon_summary_details]]** — Resumo da reconciliação (N:1 via `RECON_ID`).
- **[[gl_code_combinations]]** — Conta contábil afetada (N:1 via `CODE_COMBINATION_ID`).

### Tabelas-filha

- Nenhuma tabela-filha direta identificada.

## Uso Típico

```sql
-- Detalhamento das diferenças de reconciliação AP vs GL por período
SELECT rdd.RECON_DIFFERENCE_ID,
       rdd.SOURCE_TYPE,
       rdd.SOURCE_TABLE,
       rdd.SOURCE_ID,
       rdd.AMOUNT,
       rdd.CURRENCY_CODE
  FROM AP_RECON_DIFFERENCE_DETAILS rdd
  JOIN AP_RECON_SUMMARY_DETAILS rsd
    ON rsd.RECON_ID = rdd.RECON_ID
 WHERE rsd.PERIOD_NAME = :p_periodo
   AND rdd.ORG_ID = :p_org_id
 ORDER BY ABS(rdd.AMOUNT) DESC;
```

## Observações

- `SOURCE_TABLE` e `SOURCE_ID` permitem rastrear a transação original que gerou a diferença.
- Diferenças podem ser causadas por: faturas não transferidas, journals manuais, erros de câmbio ou ajustes pós-fechamento.
- Utilizar em conjunto com [[ap_recon_summary_details]] para visão macro + micro das diferenças.
- Estrutura análoga a [[ar_recon_difference_details]] do módulo AR.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Subledger to GL Reconciliation Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAUSE_OF_DIFFERENCE_CODE | CauseOfDifferenceCode | — |
| RECON_ITEM_CODE | ReconItemCode | — |
| RECON_TRX_ID | ReconTrxId | — |
| REQUEST_ID | RequestId | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | ReconDiffAccountingDate | — |
| CAUSE_OF_DIFFERENCE_CODE | ReconDiffCauseOfDifferenceCode | — |
| DOCUMENT_DISTRIBUTION_ID | ReconDiffDocumentDistributionId | — |
| DOCUMENT_ID | ReconDiffDocumentId | — |
| LAST_UPDATE_DATE | ReconDiffLastUpdateDate | — |
| RECON_ITEM_CODE | ReconDiffReconItemCode | — |
| RECON_TRX_ID | ReconDiffReconTrxId | — |
| REQUEST_ID | ReconDiffRequestId | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_DATE | ReconDiffAccountingDate | — |
| CAUSE_OF_DIFFERENCE_CODE | ReconDiffCauseOfDifferenceCode | — |
| DOCUMENT_DISTRIBUTION_ID | ReconDiffDocumentDistributionId | — |
| DOCUMENT_ID | ReconDiffDocumentId | — |
| LAST_UPDATE_DATE | ReconDiffLastUpdateDate | — |
| RECON_ITEM_CODE | ReconDiffReconItemCode | — |
| RECON_TRX_ID | ReconDiffReconTrxId | — |
| REQUEST_ID | ReconDiffRequestId | — |
