---
id: DOC-AR-007
doc_type: system-doc
title: "RA_BATCH_SOURCES_ALL — Origens de Transações AR"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - batch-sources
  - fontes-transacao
  - configuracao
aliases:
  - RA_BATCH_SOURCES_ALL
  - ra_batch_sources_all
  - origens-transacoes-ar
  - transaction-sources
  - batch-sources-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_BATCH_SOURCES_ALL

## 📌 Visão Geral

Define as **origens (sources) de transações** do módulo Accounts Receivable, incluindo faturas, notas de crédito e compromissos. Cada registro contém configurações que controlam a **numeração automática** de transações e lotes, permissões de duplicidade e comportamento padrão de importação.

É uma tabela de **configuração fundamental** — toda transação AR referencia obrigatoriamente um batch source, que determina como o documento será numerado, validado e agrupado.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de fontes de transação:** Define como faturas manuais, importadas (AutoInvoice) e de outros módulos são registradas no AR.
- **Numeração automática:** Controla se o sistema gera números sequenciais para transações e lotes automaticamente.
- **Controle de duplicidade:** Permite ou bloqueia transações com números duplicados dentro da mesma fonte.
- **AutoInvoice:** Fontes do tipo "Imported" alimentam o processo de importação automática de faturas.
- **Integração entre módulos:** Módulos como Projects, Order Management e Subscriptions possuem batch sources dedicados.
- **Auditoria e rastreabilidade:** Permite identificar a origem de cada transação para fins de auditoria.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BATCH_SOURCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da fonte de transação | — | 🟢 100% |
| 2 | NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome da fonte de transação | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição livre da fonte | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status ativo/inativo (A=Active, I=Inactive) | — | 🟢 100% |
| 5 | BATCH_SOURCE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da fonte: INV (manual), IMPORTED (AutoInvoice) | — | 🟢 100% |
| 6 | AUTO_TRX_NUMBERING_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Numeração automática de transações (Y/N) | — | 🟢 100% |
| 7 | AUTO_BATCH_NUMBERING_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Numeração automática de lotes (Y/N) | — | 🟢 100% |
| 8 | LAST_BATCH_NUM | NUMBER(15) | NULL | Controle | Último número de lote gerado automaticamente | — | 🟢 100% |
| 9 | DEFAULT_INV_TRX_TYPE | NUMBER(18) | NULL | Configuração | Tipo de transação padrão para faturas | [[ra_cust_trx_types_all]] | 🟢 100% |
| 10 | ALLOW_DUPLICATE_TRX_NUM_FLAG | VARCHAR2(1) | NULL | Configuração | Permite números de transação duplicados (Y/N) | — | 🟢 100% |
| 11 | COPY_DOC_NUMBER_FLAG | VARCHAR2(1) | NULL | Configuração | Copia número de sequência de documento para TRX_NUMBER (Y/N) | — | 🟢 100% |
| 12 | CREDIT_MEMO_BATCH_SOURCE_ID | NUMBER(18) | NULL | Configuração | Fonte padrão para notas de crédito geradas a partir desta fonte | self | 🟢 100% |
| 13 | INVALID_LINES_FLAG | VARCHAR2(1) | NULL | Configuração | Ação para linhas inválidas no AutoInvoice (REJECT/CREATE) | — | 🟢 100% |
| 14 | INVALID_TAX_RATE_FLAG | VARCHAR2(1) | NULL | Configuração | Ação para taxas de imposto inválidas no AutoInvoice | — | 🟢 100% |
| 15 | DERIVE_DATE_FLAG | VARCHAR2(1) | NULL | Configuração | Derivar data da transação automaticamente (Y/N) | — | 🟢 100% |
| 16 | RECEIPT_HANDLING_OPTION | VARCHAR2(30) | NULL | Configuração | Opção de tratamento de recebimentos | — | 🟢 100% |
| 17 | REV_ACC_ALLOCATION_RULE | VARCHAR2(30) | NULL | Contabilidade | Regra de alocação de receita (AMOUNT/PERCENT) | — | 🟢 100% |
| 18 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |
| 19 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 20 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 21 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 22 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 23 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 24 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 25 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 26 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 27 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_cust_trx_types_all]] — via `DEFAULT_INV_TRX_TYPE` (tipo de transação padrão)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da fonte de transações)
- self — via `CREDIT_MEMO_BATCH_SOURCE_ID` (fonte de credit memo associada)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `BATCH_SOURCE_ID` (transações que utilizam esta fonte)
- [[ra_batches_all]] — via `BATCH_SOURCE_ID` (lotes de transações)
- [[ra_interface_lines_all]] — via `BATCH_SOURCE_ID` (linhas de interface AutoInvoice)

---

## 📎 Uso Típico

### Consultar fontes ativas com numeração automática
```sql
SELECT bs.NAME, bs.BATCH_SOURCE_TYPE, bs.AUTO_TRX_NUMBERING_FLAG,
       bs.AUTO_BATCH_NUMBERING_FLAG, bs.ALLOW_DUPLICATE_TRX_NUM_FLAG
FROM   RA_BATCH_SOURCES_ALL bs
WHERE  bs.STATUS = 'A'
  AND  bs.ORG_ID = :p_org_id
ORDER BY bs.NAME;
```

### Identificar fontes do tipo AutoInvoice (importação)
```sql
SELECT bs.BATCH_SOURCE_ID, bs.NAME, bs.DESCRIPTION,
       tt.NAME AS default_trx_type
FROM   RA_BATCH_SOURCES_ALL bs
LEFT JOIN RA_CUST_TRX_TYPES_ALL tt ON tt.CUST_TRX_TYPE_ID = bs.DEFAULT_INV_TRX_TYPE
WHERE  bs.BATCH_SOURCE_TYPE = 'IMPORTED'
  AND  bs.STATUS = 'A'
  AND  bs.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'A'` — Apenas fontes ativas
- `BATCH_SOURCE_TYPE = 'INV'` — Fontes manuais
- `BATCH_SOURCE_TYPE = 'IMPORTED'` — Fontes para AutoInvoice
- `AUTO_TRX_NUMBERING_FLAG = 'Y'` — Com numeração automática

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- O campo `CREDIT_MEMO_BATCH_SOURCE_ID` cria um **auto-relacionamento** (self-reference) que vincula uma fonte de fatura à sua fonte de credit memo padrão.
- Fontes do tipo `IMPORTED` são utilizadas pelo **AutoInvoice** — o processo que converte linhas da `RA_INTERFACE_LINES_ALL` em transações completas.
- Alterações nesta tabela afetam diretamente o comportamento de numeração de **todas as transações futuras** naquela fonte.
- Em implementações multi-org, cada business unit normalmente possui seu próprio conjunto de batch sources.

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 2/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR · BICC: 3/127)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParent1AccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParent1AccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParent1AgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParent1AllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParent1AllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParent1AutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParent1AutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParent1BatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourcePEOBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParent1BatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParent1BatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParent1BillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParent1BillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParent1BillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParent1CmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParent1CopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParent1CopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParent1CreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceParent1CreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceParent1CreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParent1CreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParent1CustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParent1CustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParent1DefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParent1DefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParent1DefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParent1DeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceParent1Description | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceParent1EndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceParent1FobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParent1GlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceParent1GroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceParent1InvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParent1InvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParent1InventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParent1InvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceParent1LastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceParent1LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParent1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceParent1LastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParent1LegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceParent1MemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParent1MemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourcePEOName1 | ✅ |
| NAME | TransactionBatchSourceParent1Name | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourcePEOObjectVersionNumber9 | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParent1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParent1ReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParent1ReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParent1RelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParent1RevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParent1SalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParent1SalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParent1SalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParent1SalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SET_ID | TransactionBatchSourceParent1SetId | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParent1ShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParent1ShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParent1ShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParent1ShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParent1SoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParent1StartDate | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| STATUS | TransactionBatchSourceParent1Status | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| TERM_RULE | TransactionBatchSourceParent1TermRule | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParent1UnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |

### [[creditmemoapplicationpvo|CreditMemoApplicationPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourcePEOBatchSourceSeqId | — |
| NAME | TransactionBatchSourcePEOName | ✅ |
| OBJECT_VERSION_NUMBER | TransactionBatchSourcePEOObjectVersionNumber8 | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 3/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | ✅ |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 3/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | ✅ |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR · BICC: 2/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR · BICC: 2/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 2/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionbatchsourceextractpvo|TransactionBatchSourceExtractPVO]] (OTHER · BICC: 64/111)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | RaBatchSourceAccountingFlexfieldRule | ✅ |
| ACCOUNTING_RULE_RULE | RaBatchSourceAccountingRuleRule | ✅ |
| AGREEMENT_RULE | RaBatchSourceAgreementRule | ✅ |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | RaBatchSourceAllowDuplicateTrxNumFlag | ✅ |
| ALLOW_SALES_CREDIT_FLAG | RaBatchSourceAllowSalesCreditFlag | ✅ |
| ATTRIBUTE1 | RaBatchSourceAttribute1 | — |
| ATTRIBUTE10 | RaBatchSourceAttribute10 | — |
| ATTRIBUTE11 | RaBatchSourceAttribute11 | — |
| ATTRIBUTE12 | RaBatchSourceAttribute12 | — |
| ATTRIBUTE13 | RaBatchSourceAttribute13 | — |
| ATTRIBUTE14 | RaBatchSourceAttribute14 | — |
| ATTRIBUTE15 | RaBatchSourceAttribute15 | — |
| ATTRIBUTE2 | RaBatchSourceAttribute2 | — |
| ATTRIBUTE3 | RaBatchSourceAttribute3 | — |
| ATTRIBUTE4 | RaBatchSourceAttribute4 | — |
| ATTRIBUTE5 | RaBatchSourceAttribute5 | — |
| ATTRIBUTE6 | RaBatchSourceAttribute6 | — |
| ATTRIBUTE7 | RaBatchSourceAttribute7 | — |
| ATTRIBUTE8 | RaBatchSourceAttribute8 | — |
| ATTRIBUTE9 | RaBatchSourceAttribute9 | — |
| ATTRIBUTE_CATEGORY | RaBatchSourceAttributeCategory | — |
| AUTO_BATCH_NUMBERING_FLAG | RaBatchSourceAutoBatchNumberingFlag | ✅ |
| AUTO_TRX_NUMBERING_FLAG | RaBatchSourceAutoTrxNumberingFlag | ✅ |
| BATCH_SOURCE_ID | RaBatchSourceBatchSourceId | ✅ |
| BATCH_SOURCE_SEQ_ID | RaBatchSourceBatchSourceSeqId | ✅ |
| BATCH_SOURCE_TYPE | RaBatchSourceBatchSourceType | ✅ |
| BILL_ADDRESS_RULE | RaBatchSourceBillAddressRule | ✅ |
| BILL_CONTACT_RULE | RaBatchSourceBillContactRule | ✅ |
| BILL_CUSTOMER_RULE | RaBatchSourceBillCustomerRule | ✅ |
| CM_BATCH_SOURCE_SEQ_ID | RaBatchSourceCmBatchSourceSeqId | ✅ |
| CONTROL_TRX_COMPLETION_FLAG | RaBatchSourceControlTrxCompletionFlag | ✅ |
| COPY_DOC_NUMBER_FLAG | RaBatchSourceCopyDocNumberFlag | ✅ |
| COPY_INV_TIDFF_TO_CM_FLAG | RaBatchSourceCopyInvTidffToCmFlag | ✅ |
| CREATE_CLEARING_FLAG | RaBatchSourceCreateClearingFlag | ✅ |
| CREATED_BY | RaBatchSourceCreatedBy | ✅ |
| CREATION_DATE | RaBatchSourceCreationDate | ✅ |
| CREDIT_MEMO_BATCH_SOURCE_ID | RaBatchSourceCreditMemoBatchSourceId | ✅ |
| CUST_TRX_TYPE_RULE | RaBatchSourceCustTrxTypeRule | ✅ |
| CUSTOMER_BANK_ACCOUNT_RULE | RaBatchSourceCustomerBankAccountRule | ✅ |
| DEFAULT_INV_TRX_TYPE | RaBatchSourceDefaultInvTrxType | ✅ |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | RaBatchSourceDefaultInvTrxTypeSeqId | ✅ |
| DEFAULT_REFERENCE | RaBatchSourceDefaultReference | ✅ |
| DERIVE_DATE_FLAG | RaBatchSourceDeriveDateFlag | ✅ |
| DESCRIPTION | RaBatchSourceDescription | ✅ |
| END_DATE | RaBatchSourceEndDate | ✅ |
| FOB_POINT_RULE | RaBatchSourceFobPointRule | ✅ |
| GL_DATE_PERIOD_RULE | RaBatchSourceGlDatePeriodRule | ✅ |
| GLOBAL_ATTRIBUTE1 | RaBatchSourceGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | RaBatchSourceGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | RaBatchSourceGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | RaBatchSourceGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | RaBatchSourceGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | RaBatchSourceGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | RaBatchSourceGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | RaBatchSourceGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | RaBatchSourceGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | RaBatchSourceGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | RaBatchSourceGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | RaBatchSourceGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | RaBatchSourceGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | RaBatchSourceGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | RaBatchSourceGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | RaBatchSourceGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | RaBatchSourceGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | RaBatchSourceGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | RaBatchSourceGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | RaBatchSourceGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | RaBatchSourceGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | RaBatchSourceGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | RaBatchSourceGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | RaBatchSourceGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | RaBatchSourceGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | RaBatchSourceGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | RaBatchSourceGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | RaBatchSourceGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | RaBatchSourceGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | RaBatchSourceGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | RaBatchSourceGlobalAttributeNumber5 | — |
| GROUPING_RULE_ID | RaBatchSourceGroupingRuleId | ✅ |
| INVALID_LINES_RULE | RaBatchSourceInvalidLinesRule | ✅ |
| INVALID_TAX_RATE_RULE | RaBatchSourceInvalidTaxRateRule | ✅ |
| INVENTORY_ITEM_RULE | RaBatchSourceInventoryItemRule | ✅ |
| INVOICING_RULE_RULE | RaBatchSourceInvoicingRuleRule | ✅ |
| LAST_BATCH_NUM | RaBatchSourceLastBatchNum | ✅ |
| LAST_UPDATE_DATE | RaBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RaBatchSourceLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RaBatchSourceLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | RaBatchSourceLegalEntityId | ✅ |
| MEMO_LINE_RULE | RaBatchSourceMemoLineRule | ✅ |
| MEMO_REASON_RULE | RaBatchSourceMemoReasonRule | ✅ |
| NAME | RaBatchSourceName | ✅ |
| OBJECT_VERSION_NUMBER | RaBatchSourceObjectVersionNumber | ✅ |
| RECEIPT_HANDLING_OPTION | RaBatchSourceReceiptHandlingOption | ✅ |
| RECEIPT_METHOD_RULE | RaBatchSourceReceiptMethodRule | ✅ |
| RELATED_DOCUMENT_RULE | RaBatchSourceRelatedDocumentRule | ✅ |
| REV_ACC_ALLOCATION_RULE | RaBatchSourceRevAccAllocationRule | ✅ |
| SALES_CREDIT_RULE | RaBatchSourceSalesCreditRule | ✅ |
| SALES_CREDIT_TYPE_RULE | RaBatchSourceSalesCreditTypeRule | ✅ |
| SALES_TERRITORY_RULE | RaBatchSourceSalesTerritoryRule | ✅ |
| SALESPERSON_RULE | RaBatchSourceSalespersonRule | ✅ |
| SET_ID | RaBatchSourceSetId | ✅ |
| SHIP_ADDRESS_RULE | RaBatchSourceShipAddressRule | ✅ |
| SHIP_CONTACT_RULE | RaBatchSourceShipContactRule | ✅ |
| SHIP_CUSTOMER_RULE | RaBatchSourceShipCustomerRule | ✅ |
| SHIP_VIA_RULE | RaBatchSourceShipViaRule | ✅ |
| SOLD_CUSTOMER_RULE | RaBatchSourceSoldCustomerRule | ✅ |
| START_DATE | RaBatchSourceStartDate | ✅ |
| STATUS | RaBatchSourceStatus | ✅ |
| TERM_RULE | RaBatchSourceTermRule | ✅ |
| UNIT_OF_MEASURE_RULE | RaBatchSourceUnitOfMeasureRule | ✅ |
| USAGE_CATEGORY_CODE | RaBatchSourceUsageCategoryCode | ✅ |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/114)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | ✅ |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 4/127)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | BrTrxBatchSourcesBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | BrTrxBatchSourcesDescription | ✅ |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | BrTrxBatchSourcesName | ✅ |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 4/127)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | BrTrxBatchSourcesBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | BrTrxBatchSourcesDescription | ✅ |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | BrTrxBatchSourcesName | ✅ |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 2/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | — |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 3/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | ✅ |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 3/124)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceAccountingFlexfieldRule | — |
| ACCOUNTING_FLEXFIELD_RULE | TransactionBatchSourceParentAccountingFlexfieldRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceAccountingRuleRule | — |
| ACCOUNTING_RULE_RULE | TransactionBatchSourceParentAccountingRuleRule | — |
| AGREEMENT_RULE | TransactionBatchSourceAgreementRule | — |
| AGREEMENT_RULE | TransactionBatchSourceParentAgreementRule | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceAllowDuplicateTrxNumFlag | — |
| ALLOW_DUPLICATE_TRX_NUM_FLAG | TransactionBatchSourceParentAllowDuplicateTrxNumFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceAllowSalesCreditFlag | — |
| ALLOW_SALES_CREDIT_FLAG | TransactionBatchSourceParentAllowSalesCreditFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceAutoBatchNumberingFlag | — |
| AUTO_BATCH_NUMBERING_FLAG | TransactionBatchSourceParentAutoBatchNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceAutoTrxNumberingFlag | — |
| AUTO_TRX_NUMBERING_FLAG | TransactionBatchSourceParentAutoTrxNumberingFlag | — |
| BATCH_SOURCE_ID | TransactionBatchSourceBatchSourceId | — |
| BATCH_SOURCE_ID | TransactionBatchSourceParentBatchSourceId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceBatchSourceSeqId | — |
| BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentBatchSourceSeqId | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceBatchSourceType | — |
| BATCH_SOURCE_TYPE | TransactionBatchSourceParentBatchSourceType | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceBillAddressRule | — |
| BILL_ADDRESS_RULE | TransactionBatchSourceParentBillAddressRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceBillContactRule | — |
| BILL_CONTACT_RULE | TransactionBatchSourceParentBillContactRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceBillCustomerRule | — |
| BILL_CUSTOMER_RULE | TransactionBatchSourceParentBillCustomerRule | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceCmBatchSourceSeqId | — |
| CM_BATCH_SOURCE_SEQ_ID | TransactionBatchSourceParentCmBatchSourceSeqId | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceCopyDocNumberFlag | — |
| COPY_DOC_NUMBER_FLAG | TransactionBatchSourceParentCopyDocNumberFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceCopyInvTidffToCmFlag | — |
| COPY_INV_TIDFF_TO_CM_FLAG | TransactionBatchSourceParentCopyInvTidffToCmFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceCreateClearingFlag | — |
| CREATE_CLEARING_FLAG | TransactionBatchSourceParentCreateClearingFlag | — |
| CREATED_BY | TransactionBatchSourceCreatedBy | — |
| CREATED_BY | TransactionBatchSourceParentCreatedBy | — |
| CREATION_DATE | TransactionBatchSourceCreationDate | — |
| CREATION_DATE | TransactionBatchSourceParentCreationDate | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceCreditMemoBatchSourceId | — |
| CREDIT_MEMO_BATCH_SOURCE_ID | TransactionBatchSourceParentCreditMemoBatchSourceId | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceCustTrxTypeRule | — |
| CUST_TRX_TYPE_RULE | TransactionBatchSourceParentCustTrxTypeRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceCustomerBankAccountRule | — |
| CUSTOMER_BANK_ACCOUNT_RULE | TransactionBatchSourceParentCustomerBankAccountRule | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE | TransactionBatchSourceParentDefaultInvTrxType | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceDefaultInvTrxTypeSeqId | — |
| DEFAULT_INV_TRX_TYPE_SEQ_ID | TransactionBatchSourceParentDefaultInvTrxTypeSeqId | — |
| DEFAULT_REFERENCE | TransactionBatchSourceDefaultReference | — |
| DEFAULT_REFERENCE | TransactionBatchSourceParentDefaultReference | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceDeriveDateFlag | — |
| DERIVE_DATE_FLAG | TransactionBatchSourceParentDeriveDateFlag | — |
| DESCRIPTION | TransactionBatchSourceDescription | — |
| DESCRIPTION | TransactionBatchSourceParentDescription | — |
| END_DATE | TransactionBatchSourceEndDate | — |
| END_DATE | TransactionBatchSourceParentEndDate | — |
| FOB_POINT_RULE | TransactionBatchSourceFobPointRule | — |
| FOB_POINT_RULE | TransactionBatchSourceParentFobPointRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceGlDatePeriodRule | — |
| GL_DATE_PERIOD_RULE | TransactionBatchSourceParentGlDatePeriodRule | — |
| GROUPING_RULE_ID | TransactionBatchSourceGroupingRuleId | — |
| GROUPING_RULE_ID | TransactionBatchSourceParentGroupingRuleId | — |
| INVALID_LINES_RULE | TransactionBatchSourceInvalidLinesRule | — |
| INVALID_LINES_RULE | TransactionBatchSourceParentInvalidLinesRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceInvalidTaxRateRule | — |
| INVALID_TAX_RATE_RULE | TransactionBatchSourceParentInvalidTaxRateRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceInventoryItemRule | — |
| INVENTORY_ITEM_RULE | TransactionBatchSourceParentInventoryItemRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceInvoicingRuleRule | — |
| INVOICING_RULE_RULE | TransactionBatchSourceParentInvoicingRuleRule | — |
| LAST_BATCH_NUM | TransactionBatchSourceLastBatchNum | — |
| LAST_BATCH_NUM | TransactionBatchSourceParentLastBatchNum | — |
| LAST_UPDATE_DATE | TransactionBatchSourceLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | TransactionBatchSourceParentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionBatchSourceLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | TransactionBatchSourceParentLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionBatchSourceLastUpdatedBy | — |
| LAST_UPDATED_BY | TransactionBatchSourceParentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceLegalEntityId | — |
| LEGAL_ENTITY_ID | TransactionBatchSourceParentLegalEntityId | — |
| MEMO_LINE_RULE | TransactionBatchSourceMemoLineRule | — |
| MEMO_LINE_RULE | TransactionBatchSourceParentMemoLineRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceMemoReasonRule | — |
| MEMO_REASON_RULE | TransactionBatchSourceParentMemoReasonRule | — |
| NAME | TransactionBatchSourceName | ✅ |
| NAME | TransactionBatchSourceParentName | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | TransactionBatchSourceParentObjectVersionNumber | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceParentReceiptHandlingOption | — |
| RECEIPT_HANDLING_OPTION | TransactionBatchSourceReceiptHandlingOption | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceParentReceiptMethodRule | — |
| RECEIPT_METHOD_RULE | TransactionBatchSourceReceiptMethodRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceParentRelatedDocumentRule | — |
| RELATED_DOCUMENT_RULE | TransactionBatchSourceRelatedDocumentRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceParentRevAccAllocationRule | — |
| REV_ACC_ALLOCATION_RULE | TransactionBatchSourceRevAccAllocationRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceParentSalesCreditRule | — |
| SALES_CREDIT_RULE | TransactionBatchSourceSalesCreditRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceParentSalesCreditTypeRule | — |
| SALES_CREDIT_TYPE_RULE | TransactionBatchSourceSalesCreditTypeRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceParentSalesTerritoryRule | — |
| SALES_TERRITORY_RULE | TransactionBatchSourceSalesTerritoryRule | — |
| SALESPERSON_RULE | TransactionBatchSourceParentSalespersonRule | — |
| SALESPERSON_RULE | TransactionBatchSourceSalespersonRule | — |
| SET_ID | TransactionBatchSourceParentSetId | — |
| SET_ID | TransactionBatchSourceSetId | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceParentShipAddressRule | — |
| SHIP_ADDRESS_RULE | TransactionBatchSourceShipAddressRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceParentShipContactRule | — |
| SHIP_CONTACT_RULE | TransactionBatchSourceShipContactRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceParentShipCustomerRule | — |
| SHIP_CUSTOMER_RULE | TransactionBatchSourceShipCustomerRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceParentShipViaRule | — |
| SHIP_VIA_RULE | TransactionBatchSourceShipViaRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceParentSoldCustomerRule | — |
| SOLD_CUSTOMER_RULE | TransactionBatchSourceSoldCustomerRule | — |
| START_DATE | TransactionBatchSourceParentStartDate | — |
| START_DATE | TransactionBatchSourceStartDate | — |
| STATUS | TransactionBatchSourceParentStatus | — |
| STATUS | TransactionBatchSourceStatus | — |
| TERM_RULE | TransactionBatchSourceParentTermRule | — |
| TERM_RULE | TransactionBatchSourceTermRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceParentUnitOfMeasureRule | — |
| UNIT_OF_MEASURE_RULE | TransactionBatchSourceUnitOfMeasureRule | — |

---

## 📚 Referências

- [Oracle Docs — RA_BATCH_SOURCES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/rabatchsourcesall-10044.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
