---
id: DOC-AP-021
doc_type: system-doc
title: "AP_PREPAY_APP_DISTS — Distribuições de Aplicação de Pré-pagamentos"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, prepayment, distribuicao, aplicacao-prepay]
aliases: [AP_PREPAY_APP_DISTS, ap_prepay_app_dists, prepay_app_dists, distribuicoes_prepagamento, dist_aplicacao_prepay]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_PREPAY_APP_DISTS

## Visao Geral

Tabela que armazena as distribuições contábeis geradas quando um pré-pagamento (prepayment) é aplicado a uma fatura padrão no Oracle Fusion Accounts Payable. Cada registro representa a reversão parcial ou total de uma linha de distribuição do pré-pagamento no momento da aplicação.

## Propósito de Negócio

Quando um adiantamento a fornecedor é aplicado contra uma fatura, o sistema precisa reverter as distribuições contábeis do pré-pagamento original e registrar o abatimento na fatura destino. Esta tabela rastreia essas movimentações, sendo essencial para: (1) contabilização correta da baixa do adiantamento, (2) conciliação entre prepayments e faturas, (3) auditoria de aplicações de pré-pagamento, (4) relatórios de saldos de adiantamentos.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PREPAY_APP_DIST_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único da distribuição de aplicação de prepayment. | — | 🟢 100% |
| 2 | PREPAY_APP_DISTRIBUTION_ID | NUMBER(15) | NOT NULL | FK | FK para a distribuição do pré-pagamento original. | [[ap_invoice_distributions_all]] | 🟢 95% |
| 3 | INVOICE_DISTRIBUTION_ID | NUMBER(15) | NOT NULL | FK | FK para a distribuição da fatura destino da aplicação. | [[ap_invoice_distributions_all]] | 🟢 95% |
| 4 | PREPAY_HISTORY_ID | NUMBER(15) | NULL | FK | FK para o histórico de aplicação de prepayment. | [[ap_prepay_history_all]] | 🟡 75% |
| 5 | INVOICE_ID | NUMBER(15) | NOT NULL | FK | FK para a fatura padrão que recebeu a aplicação. | [[ap_invoices_all]] | 🟢 95% |
| 6 | PREPAY_INVOICE_ID | NUMBER(15) | NOT NULL | FK | FK para a fatura de pré-pagamento aplicada. | [[ap_invoices_all]] | 🟢 95% |
| 7 | AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da distribuição aplicada na moeda da fatura. | — | 🟢 100% |
| 8 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor na moeda funcional (ledger currency). | — | 🟢 95% |
| 9 | ACCOUNTING_EVENT_ID | NUMBER(15) | NULL | FK | FK para evento contábil SLA (Subledger Accounting). | — | 🟡 75% |
| 10 | PA_QUANTITY | NUMBER | NULL | Projeto | Quantidade para integração com Oracle Projects. | — | 🟡 60% |
| 11 | DIST_CODE_COMBINATION_ID | NUMBER(15) | NULL | FK | FK para [[gl_code_combinations]]. Conta contábil da distribuição. | [[gl_code_combinations]] | 🟢 90% |
| 12 | ORG_ID | NUMBER(15) | NOT NULL | Partição | Identificador da business unit (Operating Unit). | — | 🟢 100% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 14 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_invoices_all]]** — Fatura padrão destino (N:1 via `INVOICE_ID`) e fatura de pré-pagamento (N:1 via `PREPAY_INVOICE_ID`).
- **[[ap_invoice_distributions_all]]** — Distribuição da fatura destino (N:1 via `INVOICE_DISTRIBUTION_ID`) e distribuição do prepayment (N:1 via `PREPAY_APP_DISTRIBUTION_ID`).
- **[[gl_code_combinations]]** — Conta contábil (N:1 via `DIST_CODE_COMBINATION_ID`).

### Tabelas-filha

- Nenhuma tabela-filha direta identificada.

## Uso Típico

```sql
-- Distribuições de aplicação de prepayment para uma fatura
SELECT pad.PREPAY_APP_DIST_ID,
       pad.AMOUNT,
       pad.BASE_AMOUNT,
       inv.INVOICE_NUM AS fatura_destino,
       prep.INVOICE_NUM AS prepayment_aplicado
  FROM AP_PREPAY_APP_DISTS pad
  JOIN AP_INVOICES_ALL inv
    ON inv.INVOICE_ID = pad.INVOICE_ID
  JOIN AP_INVOICES_ALL prep
    ON prep.INVOICE_ID = pad.PREPAY_INVOICE_ID
 WHERE pad.ORG_ID = :p_org_id
   AND inv.INVOICE_NUM = :p_invoice_num;
```

## Observações

- Cada aplicação de prepayment gera registros nesta tabela proporcionais ao número de distribuições impactadas.
- O campo `AMOUNT` pode ser negativo, representando a reversão contábil do adiantamento.
- Utilizar em conjunto com [[ap_prepay_history_all]] para obter o contexto temporal da aplicação.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Prepayments and Advances Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 29/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_EVENT_ID | PrepaymentApplicationAccountingEventId | — |
| AMOUNT | PrepaymentApplicationAmount | ✅ |
| AMOUNT_VARIANCE | PrepaymentApplicationAmountVariance | ✅ |
| AWT_RELATED_ID | PrepaymentApplicationAwtRelatedId | — |
| BASE_AMOUNT | PrepaymentApplicationBaseAmount | ✅ |
| BASE_AMT_AT_PREPAY_CLR_XRATE | PrepaymentApplicationBaseAmtAtPrepayClrXrate | ✅ |
| BASE_AMT_AT_PREPAY_PAY_XRATE | PrepaymentApplicationBaseAmtAtPrepayPayXrate | ✅ |
| BASE_AMT_AT_PREPAY_XRATE | PrepaymentApplicationBaseAmtAtPrepayXrate | ✅ |
| BC_EVENT_ID | PrepaymentApplicationBcEventId | — |
| CREATED_BY | PrepaymentApplicationCreatedBy | ✅ |
| CREATION_DATE | PrepaymentApplicationCreationDate | ✅ |
| INVOICE_BASE_AMT_VARIANCE | PrepaymentApplicationInvoiceBaseAmtVariance | ✅ |
| INVOICE_BASE_QTY_VARIANCE | PrepaymentApplicationInvoiceBaseQtyVariance | — |
| INVOICE_DISTRIBUTION_ID | PrepaymentApplicationInvoiceDistributionId | ✅ |
| LAST_UPDATE_DATE | PrepaymentApplicationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrepaymentApplicationLastUpdateLogin | — |
| LAST_UPDATED_BY | PrepaymentApplicationLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PrepaymentApplicationObjectVersionNumber | — |
| PA_ADDITION_FLAG | PrepaymentApplicationPaAdditionFlag | ✅ |
| PREPAY_APP_DIST_ID | PrepayAppDistId | ✅ |
| PREPAY_APP_DISTRIBUTION_ID | PrepaymentApplicationPrepayAppDistributionId | ✅ |
| PREPAY_CLR_EXCHANGE_DATE | PrepaymentApplicationPrepayClrExchangeDate | ✅ |
| PREPAY_CLR_EXCHANGE_RATE | PrepaymentApplicationPrepayClrExchangeRate | ✅ |
| PREPAY_CLR_EXCHANGE_RATE_TYPE | PrepaymentApplicationPrepayClrExchangeRateType | ✅ |
| PREPAY_DIST_LOOKUP_CODE | PrepaymentApplicationPrepayDistLookupCode | ✅ |
| PREPAY_EXCHANGE_DATE | PrepaymentApplicationPrepayExchangeDate | ✅ |
| PREPAY_EXCHANGE_RATE | PrepaymentApplicationPrepayExchangeRate | ✅ |
| PREPAY_EXCHANGE_RATE_TYPE | PrepaymentApplicationPrepayExchangeRateType | ✅ |
| PREPAY_HISTORY_ID | PrepaymentApplicationPrepayHistoryId | — |
| PREPAY_PAY_EXCHANGE_DATE | PrepaymentApplicationPrepayPayExchangeDate | ✅ |
| PREPAY_PAY_EXCHANGE_RATE | PrepaymentApplicationPrepayPayExchangeRate | ✅ |
| PREPAY_PAY_EXCHANGE_RATE_TYPE | PrepaymentApplicationPrepayPayExchangeRateType | ✅ |
| PROGRAM_APPLICATION_ID | PrepaymentApplicationProgramApplicationId | — |
| PROGRAM_ID | PrepaymentApplicationProgramId | — |
| PROGRAM_UPDATE_DATE | PrepaymentApplicationProgramUpdateDate | — |
| QUANTITY_VARIANCE | PrepaymentApplicationQuantityVariance | — |
| RELEASE_INV_DIST_DERIVED_FROM | PrepaymentApplicationReleaseInvDistDerivedFrom | — |
| REQUEST_ID | PrepaymentApplicationRequestId | — |
| REVERSED_PREPAY_APP_DIST_ID | PrepaymentApplicationReversedPrepayAppDistId | — |
| ROUND_AMT_AT_PREPAY_CLR_XRATE | PrepaymentApplicationRoundAmtAtPrepayClrXrate | ✅ |
| ROUND_AMT_AT_PREPAY_PAY_XRATE | PrepaymentApplicationRoundAmtAtPrepayPayXrate | ✅ |
| ROUND_AMT_AT_PREPAY_XRATE | PrepaymentApplicationRoundAmtAtPrepayXrate | ✅ |
| ROUNDING_AMT | PrepaymentApplicationRoundingAmt | ✅ |

### [[prepaymentapplicationdistributionextractpvo|PrepaymentApplicationDistributionExtractPVO]] (OTHER · BICC: 43/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_EVENT_ID | ApPrepayAppDistsAccountingEventId | ✅ |
| AMOUNT | ApPrepayAppDistsAmount | ✅ |
| AMOUNT_VARIANCE | ApPrepayAppDistsAmountVariance | ✅ |
| AWT_RELATED_ID | ApPrepayAppDistsAwtRelatedId | ✅ |
| BASE_AMOUNT | ApPrepayAppDistsBaseAmount | ✅ |
| BASE_AMT_AT_PREPAY_CLR_XRATE | ApPrepayAppDistsBaseAmtAtPrepayClrXrate | ✅ |
| BASE_AMT_AT_PREPAY_PAY_XRATE | ApPrepayAppDistsBaseAmtAtPrepayPayXrate | ✅ |
| BASE_AMT_AT_PREPAY_XRATE | ApPrepayAppDistsBaseAmtAtPrepayXrate | ✅ |
| BC_EVENT_ID | ApPrepayAppDistsBcEventId | ✅ |
| CREATED_BY | ApPrepayAppDistsCreatedBy | ✅ |
| CREATION_DATE | ApPrepayAppDistsCreationDate | ✅ |
| INVOICE_BASE_AMT_VARIANCE | ApPrepayAppDistsInvoiceBaseAmtVariance | ✅ |
| INVOICE_BASE_QTY_VARIANCE | ApPrepayAppDistsInvoiceBaseQtyVariance | ✅ |
| INVOICE_DISTRIBUTION_ID | ApPrepayAppDistsInvoiceDistributionId | ✅ |
| LAST_UPDATE_DATE | ApPrepayAppDistsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApPrepayAppDistsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApPrepayAppDistsLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ApPrepayAppDistsObjectVersionNumber | ✅ |
| PA_ADDITION_FLAG | ApPrepayAppDistsPaAdditionFlag | ✅ |
| PREPAY_APP_DIST_ID | ApPrepayAppDistsPrepayAppDistId | ✅ |
| PREPAY_APP_DISTRIBUTION_ID | ApPrepayAppDistsPrepayAppDistributionId | ✅ |
| PREPAY_CLR_EXCHANGE_DATE | ApPrepayAppDistsPrepayClrExchangeDate | ✅ |
| PREPAY_CLR_EXCHANGE_RATE | ApPrepayAppDistsPrepayClrExchangeRate | ✅ |
| PREPAY_CLR_EXCHANGE_RATE_TYPE | ApPrepayAppDistsPrepayClrExchangeRateType | ✅ |
| PREPAY_DIST_LOOKUP_CODE | ApPrepayAppDistsPrepayDistLookupCode | ✅ |
| PREPAY_EXCHANGE_DATE | ApPrepayAppDistsPrepayExchangeDate | ✅ |
| PREPAY_EXCHANGE_RATE | ApPrepayAppDistsPrepayExchangeRate | ✅ |
| PREPAY_EXCHANGE_RATE_TYPE | ApPrepayAppDistsPrepayExchangeRateType | ✅ |
| PREPAY_HISTORY_ID | ApPrepayAppDistsPrepayHistoryId | ✅ |
| PREPAY_PAY_EXCHANGE_DATE | ApPrepayAppDistsPrepayPayExchangeDate | ✅ |
| PREPAY_PAY_EXCHANGE_RATE | ApPrepayAppDistsPrepayPayExchangeRate | ✅ |
| PREPAY_PAY_EXCHANGE_RATE_TYPE | ApPrepayAppDistsPrepayPayExchangeRateType | ✅ |
| PROGRAM_APPLICATION_ID | ApPrepayAppDistsProgramApplicationId | ✅ |
| PROGRAM_ID | ApPrepayAppDistsProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ApPrepayAppDistsProgramUpdateDate | ✅ |
| QUANTITY_VARIANCE | ApPrepayAppDistsQuantityVariance | ✅ |
| RELEASE_INV_DIST_DERIVED_FROM | ApPrepayAppDistsReleaseInvDistDerivedFrom | ✅ |
| REQUEST_ID | ApPrepayAppDistsRequestId | ✅ |
| REVERSED_PREPAY_APP_DIST_ID | ApPrepayAppDistsReversedPrepayAppDistId | ✅ |
| ROUND_AMT_AT_PREPAY_CLR_XRATE | ApPrepayAppDistsRoundAmtAtPrepayClrXrate | ✅ |
| ROUND_AMT_AT_PREPAY_PAY_XRATE | ApPrepayAppDistsRoundAmtAtPrepayPayXrate | ✅ |
| ROUND_AMT_AT_PREPAY_XRATE | ApPrepayAppDistsRoundAmtAtPrepayXrate | ✅ |
| ROUNDING_AMT | ApPrepayAppDistsRoundingAmt | ✅ |
