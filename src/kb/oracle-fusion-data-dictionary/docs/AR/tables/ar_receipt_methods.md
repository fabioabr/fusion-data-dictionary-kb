---
id: DOC-AR-047
doc_type: system-doc
title: "AR_RECEIPT_METHODS — Métodos de Recebimento"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, receipt-method, pagamento, forma-pagamento]
aliases: [AR_RECEIPT_METHODS, ar_receipt_methods, receipt_methods, metodos_recebimento, ar_rcpt_methods]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIPT_METHODS

## 📌 Visão Geral

Tabela de cadastro de **métodos de recebimento** (receipt methods). Define as **formas de pagamento** aceitas pelo AR — boleto, transferência, cartão de crédito, cheque, etc. Cada método está vinculado a uma [[ar_receipt_classes|classe de recebimento]] que governa seu comportamento contábil.

## 🧠 Propósito de Negócio

Os métodos de recebimento representam as **formas de pagamento** que o banco aceita dos clientes. São o elo entre a forma como o dinheiro entra (canal de pagamento) e como é contabilizado (classe de recebimento + contas contábeis).

Casos de uso principais:
- Configuração de boleto bancário com remessa automática
- Recebimento via TED/PIX
- Recebimento via cartão de crédito (com merchant reference)
- Recebimento automático via lockbox

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | RECEIPT_METHOD_ID | NUMBER | PK. Identificador único do método de recebimento. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome do método de recebimento. | Identificação | 🟢 100% |
| 3 | RECEIPT_CLASS_ID | NUMBER | FK para [[ar_receipt_classes]]. Define o comportamento contábil. | Chave Estrangeira | 🟢 100% |
| 4 | START_DATE | DATE | Data de início de vigência do método. | Vigência | 🟢 100% |
| 5 | END_DATE | DATE | Data de fim de vigência do método (nulo = sem expiração). | Vigência | 🟢 100% |
| 6 | AUTO_TRANS_PROGRAM_ID | NUMBER | FK para programa de transmissão automática (remessa). | Automação | 🟢 100% |
| 7 | AUTO_CASH_RULE_ID | NUMBER | FK para regra AutoCash associada. Referencia [[ar_autocash_hierarchies]]. | Automação | 🟢 100% |
| 8 | MERCHANT_REF | VARCHAR2 | Referência do merchant (para recebimentos via cartão). | Pagamento | 🟢 100% |
| 9 | PAYMENT_CHANNEL_CODE | VARCHAR2 | Código do canal de pagamento: `BANK_ACCT_XFER`, `CREDIT_CARD`, `CHECK`, etc. | Pagamento | 🟢 100% |
| 10 | LEAD_DAYS | NUMBER | Dias de antecedência para processamento (lead time bancário). | Operacional | 🟢 100% |
| 11 | PRINTED_NAME | VARCHAR2 | Nome impresso em documentos/remessas. | Identificação | 🟢 100% |
| 12 | MATURITY_DATE_RULE_CODE | VARCHAR2 | Regra para cálculo da data de vencimento. | Configuração | 🟢 100% |
| 13 | BR_MIN_ACCTD_AMOUNT | NUMBER | Valor mínimo para bills receivable (duplicatas). | Configuração | 🟢 100% |
| 14 | BR_MAX_ACCTD_AMOUNT | NUMBER | Valor máximo para bills receivable (duplicatas). | Configuração | 🟢 100% |
| 15 | RECEIPT_INHERIT_INV_NUM_FLAG | VARCHAR2 | Herda número da fatura no receipt: `Y`/`N`. | Configuração | 🟢 100% |
| 16 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 17 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 18 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 19 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 21 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 22 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_receipt_classes]] | RECEIPT_CLASS_ID | FK | Classe de recebimento (comportamento contábil) |
| [[ar_autocash_hierarchies]] | AUTO_CASH_RULE_ID | FK | Regra AutoCash para aplicação automática |
| [[ar_receipt_method_accounts_all]] | RECEIPT_METHOD_ID | Referenciada por | Contas contábeis por BU |
| [[ar_cash_receipts_all]] | RECEIPT_METHOD_ID | Referenciada por | Recebimentos que usam este método |

## 📎 Uso Típico

```sql
-- Listar métodos de recebimento ativos com suas classes
SELECT rm.receipt_method_id,
       rm.name AS metodo,
       rc.name AS classe,
       rm.payment_channel_code,
       rm.lead_days
  FROM ar_receipt_methods rm
  JOIN ar_receipt_classes rc ON rc.receipt_class_id = rm.receipt_class_id
 WHERE rm.end_date IS NULL
    OR rm.end_date > SYSDATE;
```

```sql
-- Métodos com regra AutoCash configurada
SELECT rm.name,
       ah.hierarchy_name AS regra_autocash
  FROM ar_receipt_methods rm
  JOIN ar_autocash_hierarchies ah ON ah.autocash_hierarchy_id = rm.auto_cash_rule_id
 WHERE rm.auto_cash_rule_id IS NOT NULL;
```

## 🔒 Observações

- O método de recebimento é o **ponto de configuração mais granular** para recebimentos — combina classe (comportamento), contas (contabilização) e automação (AutoCash, transmissão).
- As contas contábeis são definidas em [[ar_receipt_method_accounts_all]], não diretamente no método, pois variam por BU.
- O campo `PAYMENT_CHANNEL_CODE` é usado para integração com gateways de pagamento e lockbox.
- `LEAD_DAYS` é crucial para conciliação: indica quantos dias antes do vencimento o processamento deve ocorrer.

## 🔗 PVOs Relacionados

### [[customeraccountreceiptmethod|CustomerAccountReceiptMethod]] (AR · BICC: 2/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptMethodAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptMethodAutoTransProgramId | — |
| BR_CUST_TRX_TYPE_ID | ReceiptMethodBrCustTrxTypeId | — |
| BR_INHERIT_INV_NUM_FLAG | ReceiptMethodBrInheritInvNumFlag | — |
| BR_MAX_ACCTD_AMOUNT | ReceiptMethodBrMaxAcctdAmount | — |
| BR_MIN_ACCTD_AMOUNT | ReceiptMethodBrMinAcctdAmount | — |
| CREATED_BY | ReceiptMethodCreatedBy | — |
| CREATION_DATE | ReceiptMethodCreationDate | — |
| DM_INHERIT_RECEIPT_NUM_FLAG | ReceiptMethodDmInheritReceiptNumFlag | — |
| END_DATE | ReceiptMethodEndDate | — |
| LAST_UPDATE_DATE | ReceiptMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptMethodLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptMethodLastUpdatedBy | — |
| LEAD_DAYS | ReceiptMethodLeadDays | — |
| MATURITY_DATE_RULE_CODE | ReceiptMethodMaturityDateRuleCode | — |
| MERCHANT_ID | ReceiptMethodMerchantId | — |
| MERCHANT_REF | ReceiptMethodMerchantRef | — |
| NAME | ReceiptMethodName | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptMethodObjectVersionNumber | — |
| PAYMENT_CHANNEL_CODE | ReceiptMethodPaymentChannelCode | — |
| PAYMENT_TYPE_CODE | ReceiptMethodPaymentTypeCode | — |
| PRINTED_NAME | ReceiptMethodPrintedName | — |
| RECEIPT_CLASS_ID | ReceiptMethodReceiptClassId | — |
| RECEIPT_CREATION_RULE_CODE | ReceiptMethodReceiptCreationRuleCode | — |
| RECEIPT_INHERIT_INV_NUM_FLAG | ReceiptMethodReceiptInheritInvNumFlag | — |
| RECEIPT_METHOD_ID | ReceiptMethodReceiptMethodId | — |
| START_DATE | ReceiptMethodStartDate | — |

### [[customeraccountsitereceiptmethod|CustomerAccountSiteReceiptMethod]] (AR · BICC: 2/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptMethodAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptMethodAutoTransProgramId | — |
| BR_CUST_TRX_TYPE_ID | ReceiptMethodBrCustTrxTypeId | — |
| BR_INHERIT_INV_NUM_FLAG | ReceiptMethodBrInheritInvNumFlag | — |
| BR_MAX_ACCTD_AMOUNT | ReceiptMethodBrMaxAcctdAmount | — |
| BR_MIN_ACCTD_AMOUNT | ReceiptMethodBrMinAcctdAmount | — |
| CREATED_BY | ReceiptMethodCreatedBy | — |
| CREATION_DATE | ReceiptMethodCreationDate | — |
| DM_INHERIT_RECEIPT_NUM_FLAG | ReceiptMethodDmInheritReceiptNumFlag | — |
| END_DATE | ReceiptMethodEndDate | — |
| LAST_UPDATE_DATE | ReceiptMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptMethodLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptMethodLastUpdatedBy | — |
| LEAD_DAYS | ReceiptMethodLeadDays | — |
| MATURITY_DATE_RULE_CODE | ReceiptMethodMaturityDateRuleCode | — |
| MERCHANT_ID | ReceiptMethodMerchantId | — |
| MERCHANT_REF | ReceiptMethodMerchantRef | — |
| NAME | ReceiptMethodName | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptMethodObjectVersionNumber | — |
| PAYMENT_CHANNEL_CODE | ReceiptMethodPaymentChannelCode | — |
| PAYMENT_TYPE_CODE | ReceiptMethodPaymentTypeCode | — |
| PRINTED_NAME | ReceiptMethodPrintedName | — |
| RECEIPT_CLASS_ID | ReceiptMethodReceiptClassId | — |
| RECEIPT_CREATION_RULE_CODE | ReceiptMethodReceiptCreationRuleCode | — |
| RECEIPT_INHERIT_INV_NUM_FLAG | ReceiptMethodReceiptInheritInvNumFlag | — |
| RECEIPT_METHOD_ID | ReceiptMethodReceiptMethodId | — |
| START_DATE | ReceiptMethodStartDate | — |

### [[receiptmethodextractpvo|ReceiptMethodExtractPVO]] (OTHER · BICC: 29/66)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | ArReceiptMethodAttribute1 | — |
| ATTRIBUTE10 | ArReceiptMethodAttribute10 | — |
| ATTRIBUTE11 | ArReceiptMethodAttribute11 | — |
| ATTRIBUTE12 | ArReceiptMethodAttribute12 | — |
| ATTRIBUTE13 | ArReceiptMethodAttribute13 | — |
| ATTRIBUTE14 | ArReceiptMethodAttribute14 | — |
| ATTRIBUTE15 | ArReceiptMethodAttribute15 | — |
| ATTRIBUTE2 | ArReceiptMethodAttribute2 | — |
| ATTRIBUTE3 | ArReceiptMethodAttribute3 | — |
| ATTRIBUTE4 | ArReceiptMethodAttribute4 | — |
| ATTRIBUTE5 | ArReceiptMethodAttribute5 | — |
| ATTRIBUTE6 | ArReceiptMethodAttribute6 | — |
| ATTRIBUTE7 | ArReceiptMethodAttribute7 | — |
| ATTRIBUTE8 | ArReceiptMethodAttribute8 | — |
| ATTRIBUTE9 | ArReceiptMethodAttribute9 | — |
| ATTRIBUTE_CATEGORY | ArReceiptMethodAttributeCategory | — |
| AUTO_PRINT_PROGRAM_ID | ArReceiptMethodAutoPrintProgramId | ✅ |
| AUTO_TRANS_PROGRAM_ID | ArReceiptMethodAutoTransProgramId | ✅ |
| BR_CUST_TRX_TYPE_ID | ArReceiptMethodBrCustTrxTypeId | ✅ |
| BR_INHERIT_INV_NUM_FLAG | ArReceiptMethodBrInheritInvNumFlag | ✅ |
| BR_MAX_ACCTD_AMOUNT | ArReceiptMethodBrMaxAcctdAmount | ✅ |
| BR_MIN_ACCTD_AMOUNT | ArReceiptMethodBrMinAcctdAmount | ✅ |
| CREATED_BY | ArReceiptMethodCreatedBy | ✅ |
| CREATION_DATE | ArReceiptMethodCreationDate | ✅ |
| DM_INHERIT_RECEIPT_NUM_FLAG | ArReceiptMethodDmInheritReceiptNumFlag | ✅ |
| END_DATE | ArReceiptMethodEndDate | ✅ |
| GLOBAL_ATTRIBUTE1 | ArReceiptMethodGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ArReceiptMethodGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ArReceiptMethodGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ArReceiptMethodGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ArReceiptMethodGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ArReceiptMethodGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ArReceiptMethodGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ArReceiptMethodGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ArReceiptMethodGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ArReceiptMethodGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ArReceiptMethodGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ArReceiptMethodGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ArReceiptMethodGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ArReceiptMethodGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ArReceiptMethodGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ArReceiptMethodGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ArReceiptMethodGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ArReceiptMethodGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ArReceiptMethodGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ArReceiptMethodGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ArReceiptMethodGlobalAttributeCategory | — |
| ISO20022_DIRECT_DEBIT_FLAG | ArReceiptMethodIso20022DirectDebitFlag | ✅ |
| LAST_UPDATE_DATE | ArReceiptMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArReceiptMethodLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArReceiptMethodLastUpdatedBy | ✅ |
| LEAD_DAYS | ArReceiptMethodLeadDays | ✅ |
| MATURITY_DATE_RULE_CODE | ArReceiptMethodMaturityDateRuleCode | ✅ |
| MERCHANT_ID | ArReceiptMethodMerchantId | ✅ |
| MERCHANT_REF | ArReceiptMethodMerchantRef | ✅ |
| NAME | ArReceiptMethodName | ✅ |
| OBJECT_VERSION_NUMBER | ArReceiptMethodObjectVersionNumber | ✅ |
| PAYMENT_CHANNEL_CODE | ArReceiptMethodPaymentChannelCode | ✅ |
| PAYMENT_TYPE_CODE | ArReceiptMethodPaymentTypeCode | ✅ |
| PRINTED_NAME | ArReceiptMethodPrintedName | ✅ |
| RECEIPT_CLASS_ID | ArReceiptMethodReceiptClassId | ✅ |
| RECEIPT_CREATION_RULE_CODE | ArReceiptMethodReceiptCreationRuleCode | ✅ |
| RECEIPT_INHERIT_INV_NUM_FLAG | ArReceiptMethodReceiptInheritInvNumFlag | ✅ |
| RECEIPT_METHOD_ID | ArReceiptMethodReceiptMethodId | ✅ |
| SEED_DATA_SOURCE | ArReceiptMethodSeedDataSource | ✅ |
| START_DATE | ArReceiptMethodStartDate | ✅ |

### [[receiptmethodpvo|ReceiptMethodPVO]] (AR · BICC: 9/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_PRINT_PROGRAM_ID | ReceiptMethodAutoPrintProgramId | — |
| AUTO_TRANS_PROGRAM_ID | ReceiptMethodAutoTransProgramId | — |
| BR_CUST_TRX_TYPE_ID | ReceiptMethodBrCustTrxTypeId | — |
| BR_INHERIT_INV_NUM_FLAG | ReceiptMethodBrInheritInvNumFlag | — |
| BR_MAX_ACCTD_AMOUNT | ReceiptMethodBrMaxAcctdAmount | — |
| BR_MIN_ACCTD_AMOUNT | ReceiptMethodBrMinAcctdAmount | — |
| CREATED_BY | ReceiptMethodCreatedBy | ✅ |
| CREATION_DATE | ReceiptMethodCreationDate | ✅ |
| DM_INHERIT_RECEIPT_NUM_FLAG | ReceiptMethodDmInheritReceiptNumFlag | — |
| END_DATE | ReceiptMethodEndDate | ✅ |
| LAST_UPDATE_DATE | ReceiptMethodLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ReceiptMethodLastUpdateLogin | — |
| LAST_UPDATED_BY | ReceiptMethodLastUpdatedBy | ✅ |
| LEAD_DAYS | ReceiptMethodLeadDays | — |
| MATURITY_DATE_RULE_CODE | ReceiptMethodMaturityDateRuleCode | — |
| MERCHANT_ID | ReceiptMethodMerchantId | — |
| MERCHANT_REF | ReceiptMethodMerchantRef | — |
| NAME | ReceiptMethodName | ✅ |
| OBJECT_VERSION_NUMBER | ReceiptMethodObjectVersionNumber | — |
| PAYMENT_CHANNEL_CODE | ReceiptMethodPaymentChannelCode | — |
| PAYMENT_TYPE_CODE | ReceiptMethodPaymentTypeCode | ✅ |
| PRINTED_NAME | ReceiptMethodPrintedName | ✅ |
| RECEIPT_CLASS_ID | ReceiptMethodReceiptClassId | — |
| RECEIPT_CREATION_RULE_CODE | ReceiptMethodReceiptCreationRuleCode | — |
| RECEIPT_INHERIT_INV_NUM_FLAG | ReceiptMethodReceiptInheritInvNumFlag | — |
| RECEIPT_METHOD_ID | ReceiptMethodId | ✅ |
| START_DATE | ReceiptMethodStartDate | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Receipt Methods View Object
- Oracle Fusion Cloud — Setting Up Receipt Classes and Methods (Configuration Guide)
