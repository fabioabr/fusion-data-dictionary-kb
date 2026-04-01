---
id: DOC-AP-020
doc_type: system-doc
title: "AP_PAYMENT_SCHEDULES_ALL — Parcelas e Vencimentos de Faturas"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - parcelas
  - vencimentos
  - payment-schedules
aliases:
  - AP_PAYMENT_SCHEDULES_ALL
  - ap_payment_schedules_all
  - parcelas-ap
  - vencimentos-ap
  - payment-schedules-ap
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_PAYMENT_SCHEDULES_ALL

## 📌 Visão Geral

Armazena as **parcelas de pagamento** (payment schedules) de cada fatura do módulo Accounts Payable. Cada registro representa um vencimento (due date) com valor bruto, valor remanescente, descontos disponíveis e status de pagamento. Uma fatura pode ter uma ou mais parcelas, conforme a condição de pagamento (payment terms) aplicada. É a tabela central para gestão de vencimentos e seleção de faturas para pagamento.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de vencimentos:** Cada parcela contém a data de vencimento calculada a partir da condição de pagamento.
- **Seleção de pagamento (PPR):** O Payment Process Request consulta esta tabela para identificar parcelas elegíveis.
- **Aging de contas a pagar:** Base para relatórios de aging (30/60/90/120 dias) por data de vencimento.
- **Descontos financeiros:** Armazena datas e percentuais de desconto por pagamento antecipado.
- **Controle de saldo:** O campo `AMOUNT_REMAINING` é atualizado a cada pagamento parcial ou total.
- **Fluxo de caixa:** Base para projeção de desembolsos futuros por data de vencimento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVOICE_ID | NUMBER(18) | NOT NULL | PK/FK | Fatura à qual pertence a parcela | [[ap_invoices_all]] | 🟢 100% |
| 2 | PAYMENT_NUM | NUMBER | NOT NULL | PK | Número sequencial da parcela | — | 🟢 100% |
| 3 | DUE_DATE | DATE | NOT NULL | Data | Data de vencimento da parcela | — | 🟢 100% |
| 4 | GROSS_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor bruto da parcela | — | 🟢 100% |
| 5 | AMOUNT_REMAINING | NUMBER | NULL | Financeiro | Valor remanescente (não pago) | — | 🟢 100% |
| 6 | PAYMENT_STATUS_FLAG | VARCHAR2(1) | NULL | Status | Status do pagamento (Y=pago/N=pendente/P=parcial) | — | 🟢 100% |
| 7 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Pagamento | Método de pagamento | [[iby_payment_methods_b]] | 🟢 100% |
| 8 | PAYMENT_PRIORITY | NUMBER | NULL | Pagamento | Prioridade de pagamento (1=alta, 99=baixa) | — | 🟢 100% |
| 9 | HOLD_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a parcela está em hold (Y/N) | — | 🟢 100% |
| 10 | DISCOUNT_DATE | DATE | NULL | Desconto | Data limite para desconto (1o nível) | — | 🟢 100% |
| 11 | DISCOUNT_AMOUNT_AVAILABLE | NUMBER | NULL | Desconto | Valor de desconto disponível (1o nível) | — | 🟢 100% |
| 12 | SECOND_DISCOUNT_DATE | DATE | NULL | Desconto | Data limite para desconto (2o nível) | — | 🟢 100% |
| 13 | SECOND_DISC_AMT_AVAILABLE | NUMBER | NULL | Desconto | Valor de desconto disponível (2o nível) | — | 🟢 100% |
| 14 | THIRD_DISCOUNT_DATE | DATE | NULL | Desconto | Data limite para desconto (3o nível) | — | 🟢 100% |
| 15 | THIRD_DISC_AMT_AVAILABLE | NUMBER | NULL | Desconto | Valor de desconto disponível (3o nível) | — | 🟢 100% |
| 16 | DISCOUNT_AMOUNT_REMAINING | NUMBER | NULL | Desconto | Valor de desconto remanescente | — | 🟢 100% |
| 17 | INV_CURR_GROSS_AMOUNT | NUMBER | NULL | Financeiro | Valor bruto na moeda da fatura | — | 🟢 100% |
| 18 | PAYMENT_CROSS_RATE | NUMBER | NULL | Financeiro | Taxa de conversão entre moeda da fatura e pagamento | — | 🟡 75% |
| 19 | FUTURE_PAY_DUE_DATE | DATE | NULL | Data | Data de vencimento para future-dated payment | — | 🟡 75% |
| 20 | EXTERNAL_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária do fornecedor (para EFT) | [[iby_ext_bank_accounts]] | 🟢 100% |
| 21 | IBY_HOLD_REASON | VARCHAR2(2000) | NULL | Controle | Motivo de hold do Oracle Payments | — | 🟡 75% |
| 22 | REMIT_TO_SUPPLIER_NAME | VARCHAR2(240) | NULL | Fornecedor | Nome do fornecedor de remessa | — | 🟡 70% |
| 23 | REMIT_TO_SUPPLIER_SITE | VARCHAR2(15) | NULL | Fornecedor | Site do fornecedor de remessa | — | 🟡 70% |
| 24 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 25 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 26 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 27 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 28 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 29 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 30 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 31 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura à qual a parcela de pagamento pertence)
- [[iby_payment_methods_b]] — via `PAYMENT_METHOD_CODE` (método de pagamento)
- [[iby_ext_bank_accounts]] — via `EXTERNAL_BANK_ACCOUNT_ID` (conta bancária do fornecedor)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da parcela de pagamento)

### Tabelas-filha (FK de saída)
- [[ap_invoice_payments_all]] — via `INVOICE_ID` + `PAYMENT_NUM` (pagamentos aplicados à parcela)

---

## 📎 Uso Típico

### Parcelas pendentes por data de vencimento
```sql
SELECT ai.INVOICE_NUM, aps.PAYMENT_NUM, aps.DUE_DATE,
       aps.GROSS_AMOUNT, aps.AMOUNT_REMAINING
FROM   AP_PAYMENT_SCHEDULES_ALL aps
JOIN   AP_INVOICES_ALL ai ON ai.INVOICE_ID = aps.INVOICE_ID
WHERE  aps.PAYMENT_STATUS_FLAG <> 'Y'
  AND  aps.DUE_DATE <= :p_thru_date
  AND  aps.ORG_ID = :p_org_id
ORDER BY aps.DUE_DATE;
```

### Aging de contas a pagar
```sql
SELECT CASE
         WHEN aps.DUE_DATE >= TRUNC(SYSDATE) THEN 'A Vencer'
         WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 30 THEN '1-30 dias'
         WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 60 THEN '31-60 dias'
         WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 90 THEN '61-90 dias'
         ELSE '90+ dias'
       END AS faixa_aging,
       SUM(aps.AMOUNT_REMAINING) AS total_pendente
FROM   AP_PAYMENT_SCHEDULES_ALL aps
WHERE  aps.PAYMENT_STATUS_FLAG <> 'Y'
  AND  aps.ORG_ID = :p_org_id
GROUP BY CASE
           WHEN aps.DUE_DATE >= TRUNC(SYSDATE) THEN 'A Vencer'
           WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 30 THEN '1-30 dias'
           WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 60 THEN '31-60 dias'
           WHEN TRUNC(SYSDATE) - aps.DUE_DATE <= 90 THEN '61-90 dias'
           ELSE '90+ dias'
         END;
```

### Filtros comuns
- `PAYMENT_STATUS_FLAG = 'N'` — Parcelas não pagas
- `PAYMENT_STATUS_FLAG <> 'Y'` — Pendentes (inclui parcial)
- `DUE_DATE <= SYSDATE` — Vencidas
- `HOLD_FLAG IS NULL OR HOLD_FLAG = 'N'` — Sem hold

---

## 🔒 Observações

- A PK composta é `INVOICE_ID` + `PAYMENT_NUM`.
- O campo `AMOUNT_REMAINING` é atualizado automaticamente a cada pagamento parcial ou total, refletindo o saldo em aberto.
- A tabela suporta até **três níveis de desconto** financeiro com datas e valores específicos (`DISCOUNT_DATE`, `SECOND_DISCOUNT_DATE`, `THIRD_DISCOUNT_DATE`).
- O campo `HOLD_FLAG = 'Y'` impede que a parcela seja selecionada no Payment Process Request.
- A coluna `PAYMENT_PRIORITY` influencia a ordem de seleção no PPR — valores menores = prioridade maior.
- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.

---

## 🔗 PVOs Relacionados

### [[fiscaldocheadersp|FiscalDocHeadersP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | InvoiceHeaderRelationshipId | — |
| REMIT_TO_ADDRESS_ID | InvoiceHeaderRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | InvoiceHeaderRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | InvoiceHeaderRemitToSupplierName | — |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | ✅ |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | — |

### [[invoicepaymentscheduleextractpvo|InvoicePaymentScheduleExtractPVO]] (OTHER · BICC: 40/97)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT_REMAINING | ApPaymentSchedulesAllAmountRemaining | ✅ |
| ATTRIBUTE1 | ApPaymentSchedulesAllAttribute1 | — |
| ATTRIBUTE10 | ApPaymentSchedulesAllAttribute10 | — |
| ATTRIBUTE11 | ApPaymentSchedulesAllAttribute11 | — |
| ATTRIBUTE12 | ApPaymentSchedulesAllAttribute12 | — |
| ATTRIBUTE13 | ApPaymentSchedulesAllAttribute13 | — |
| ATTRIBUTE14 | ApPaymentSchedulesAllAttribute14 | — |
| ATTRIBUTE15 | ApPaymentSchedulesAllAttribute15 | — |
| ATTRIBUTE2 | ApPaymentSchedulesAllAttribute2 | — |
| ATTRIBUTE3 | ApPaymentSchedulesAllAttribute3 | — |
| ATTRIBUTE4 | ApPaymentSchedulesAllAttribute4 | — |
| ATTRIBUTE5 | ApPaymentSchedulesAllAttribute5 | — |
| ATTRIBUTE6 | ApPaymentSchedulesAllAttribute6 | — |
| ATTRIBUTE7 | ApPaymentSchedulesAllAttribute7 | — |
| ATTRIBUTE8 | ApPaymentSchedulesAllAttribute8 | — |
| ATTRIBUTE9 | ApPaymentSchedulesAllAttribute9 | — |
| ATTRIBUTE_CATEGORY | ApPaymentSchedulesAllAttributeCategory | — |
| ATTRIBUTE_DATE1 | ApPaymentSchedulesAllAttributeDate1 | — |
| ATTRIBUTE_DATE2 | ApPaymentSchedulesAllAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ApPaymentSchedulesAllAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ApPaymentSchedulesAllAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ApPaymentSchedulesAllAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | ApPaymentSchedulesAllAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | ApPaymentSchedulesAllAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | ApPaymentSchedulesAllAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ApPaymentSchedulesAllAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ApPaymentSchedulesAllAttributeNumber5 | — |
| BATCH_ID | ApPaymentSchedulesAllBatchId | ✅ |
| CHECKRUN_ID | ApPaymentSchedulesAllCheckrunId | ✅ |
| CREATED_BY | ApPaymentSchedulesAllCreatedBy | ✅ |
| CREATION_DATE | ApPaymentSchedulesAllCreationDate | ✅ |
| DISCOUNT_AMOUNT_AVAILABLE | ApPaymentSchedulesAllDiscountAmountAvailable | ✅ |
| DISCOUNT_AMOUNT_REMAINING | ApPaymentSchedulesAllDiscountAmountRemaining | ✅ |
| DISCOUNT_DATE | ApPaymentSchedulesAllDiscountDate | ✅ |
| DUE_DATE | ApPaymentSchedulesAllDueDate | ✅ |
| EXTERNAL_BANK_ACCOUNT_ID | ApPaymentSchedulesAllExternalBankAccountId | ✅ |
| GLOBAL_ATTRIBUTE1 | ApPaymentSchedulesAllGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | ApPaymentSchedulesAllGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | ApPaymentSchedulesAllGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | ApPaymentSchedulesAllGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | ApPaymentSchedulesAllGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | ApPaymentSchedulesAllGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | ApPaymentSchedulesAllGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | ApPaymentSchedulesAllGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | ApPaymentSchedulesAllGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | ApPaymentSchedulesAllGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | ApPaymentSchedulesAllGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | ApPaymentSchedulesAllGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | ApPaymentSchedulesAllGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | ApPaymentSchedulesAllGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | ApPaymentSchedulesAllGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | ApPaymentSchedulesAllGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | ApPaymentSchedulesAllGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | ApPaymentSchedulesAllGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | ApPaymentSchedulesAllGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | ApPaymentSchedulesAllGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | ApPaymentSchedulesAllGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | ApPaymentSchedulesAllGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | ApPaymentSchedulesAllGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | ApPaymentSchedulesAllGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | ApPaymentSchedulesAllGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | ApPaymentSchedulesAllGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | ApPaymentSchedulesAllGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | ApPaymentSchedulesAllGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | ApPaymentSchedulesAllGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | ApPaymentSchedulesAllGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | ApPaymentSchedulesAllGlobalAttributeNumber5 | — |
| GROSS_AMOUNT | ApPaymentSchedulesAllGrossAmount | ✅ |
| HELD_BY | ApPaymentSchedulesAllHeldBy | ✅ |
| HOLD_DATE | ApPaymentSchedulesAllHoldDate | ✅ |
| HOLD_FLAG | ApPaymentSchedulesAllHoldFlag | ✅ |
| IBY_HOLD_REASON | ApPaymentSchedulesAllIbyHoldReason | ✅ |
| INV_CURR_GROSS_AMOUNT | ApPaymentSchedulesAllInvCurrGrossAmount | ✅ |
| INVOICE_ID | ApPaymentSchedulesAllInvoiceId | ✅ |
| LAST_UPDATE_DATE | ApPaymentSchedulesAllLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApPaymentSchedulesAllLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApPaymentSchedulesAllLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ApPaymentSchedulesAllObjectVersionNumber | ✅ |
| ORG_ID | ApPaymentSchedulesAllOrgId | ✅ |
| PAYMENT_CROSS_RATE | ApPaymentSchedulesAllPaymentCrossRate | ✅ |
| PAYMENT_METHOD_CODE | ApPaymentSchedulesAllPaymentMethodCode | ✅ |
| PAYMENT_METHOD_LOOKUP_CODE | ApPaymentSchedulesAllPaymentMethodLookupCode | ✅ |
| PAYMENT_NUM | ApPaymentSchedulesAllPaymentNum | ✅ |
| PAYMENT_PRIORITY | ApPaymentSchedulesAllPaymentPriority | ✅ |
| PAYMENT_STATUS_FLAG | ApPaymentSchedulesAllPaymentStatusFlag | ✅ |
| RELATIONSHIP_ID | ApPaymentSchedulesAllRelationshipId | ✅ |
| REMIT_TO_ADDRESS_ID | ApPaymentSchedulesAllRemitToAddressId | ✅ |
| REMIT_TO_ADDRESS_NAME | ApPaymentSchedulesAllRemitToAddressName | ✅ |
| REMIT_TO_SUPPLIER_ID | ApPaymentSchedulesAllRemitToSupplierId | ✅ |
| REMIT_TO_SUPPLIER_NAME | ApPaymentSchedulesAllRemitToSupplierName | ✅ |
| REMITTANCE_MESSAGE1 | ApPaymentSchedulesAllRemittanceMessage1 | ✅ |
| REMITTANCE_MESSAGE2 | ApPaymentSchedulesAllRemittanceMessage2 | ✅ |
| REMITTANCE_MESSAGE3 | ApPaymentSchedulesAllRemittanceMessage3 | ✅ |
| SECOND_DISC_AMT_AVAILABLE | ApPaymentSchedulesAllSecondDiscAmtAvailable | ✅ |
| SECOND_DISCOUNT_DATE | ApPaymentSchedulesAllSecondDiscountDate | ✅ |
| THIRD_DISC_AMT_AVAILABLE | ApPaymentSchedulesAllThirdDiscAmtAvailable | ✅ |
| THIRD_DISCOUNT_DATE | ApPaymentSchedulesAllThirdDiscountDate | ✅ |

### [[invoicepaymentschedulepvo|InvoicePaymentSchedulePVO]] (AP · BICC: 38/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT_REMAINING | PaymentScheduleAmountRemaining | ✅ |
| APR_DISCOUNT_RATE | DiscountAPR | — |
| ASSIGNMENT_TYPE_CODE | DiscountOffersTransNameType | — |
| CAMPAIGN_NAME | DiscountOffersTranslationName | — |
| CREATED_BY | PaymentScheduleCreatedBy | ✅ |
| CREATION_DATE | PaymentScheduleCreationDate | ✅ |
| DISCOUNT_AMOUNT_AVAILABLE | PaymentScheduleDiscountAmountAvailable | ✅ |
| DISCOUNT_AMOUNT_REMAINING | PaymentScheduleDiscountAmountRemaining | ✅ |
| DISCOUNT_DATE | PaymentScheduleDiscountDate | ✅ |
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| EXTERNAL_BANK_ACCOUNT_ID | PaymentScheduleExternalBankAccountId | ✅ |
| GROSS_AMOUNT | PaymentScheduleGrossAmount | ✅ |
| HOLD_DATE | PaymentScheduleHoldDate | ✅ |
| HOLD_FLAG | PaymentScheduleHoldFlag | ✅ |
| IBY_HOLD_REASON | PaymentScheduleIbyHoldReason | ✅ |
| INV_CURR_GROSS_AMOUNT | PaymentScheduleInvCurrGrossAmount | ✅ |
| INVOICE_ID | InvoiceId | ✅ |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| LAST_UPDATED_BY | PaymentScheduleLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PaymentScheduleObjectVersionNumber | — |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_CROSS_RATE | PaymentSchedulePaymentCrossRate | ✅ |
| PAYMENT_METHOD_CODE | PaymentSchedulePaymentMethodCode | ✅ |
| PAYMENT_NUM | PaymentNum | ✅ |
| PAYMENT_PRIORITY | PaymentSchedulePaymentPriority | ✅ |
| PAYMENT_STATUS_FLAG | PaymentSchedulePaymentStatusFlag | ✅ |
| RELATIONSHIP_ID | InvoiceHeaderRelationshipId | ✅ |
| RELATIONSHIP_ID | PaymentScheduleRelationshipId | ✅ |
| REMIT_TO_ADDRESS_ID | InvoiceHeaderRemitToAddressId | ✅ |
| REMIT_TO_ADDRESS_ID | PaymentScheduleRemitToAddressId | ✅ |
| REMIT_TO_ADDRESS_NAME | InvoiceHeaderRemitToAddressName | ✅ |
| REMIT_TO_ADDRESS_NAME | PaymentScheduleRemitToAddressName | ✅ |
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | ✅ |
| REMIT_TO_SUPPLIER_ID | PaymentScheduleRemitToSupplierId | ✅ |
| REMIT_TO_SUPPLIER_NAME | InvoiceHeaderRemitToSupplierName | ✅ |
| REMIT_TO_SUPPLIER_NAME | PaymentScheduleRemitToSupplierName | ✅ |
| REMITTANCE_MESSAGE1 | PaymentScheduleRemittanceMessage1 | ✅ |
| REMITTANCE_MESSAGE2 | PaymentScheduleRemittanceMessage2 | ✅ |
| REMITTANCE_MESSAGE3 | PaymentScheduleRemittanceMessage3 | ✅ |
| SECOND_DISC_AMT_AVAILABLE | PaymentScheduleSecondDiscAmtAvailable | ✅ |
| SECOND_DISCOUNT_DATE | PaymentScheduleSecondDiscountDate | ✅ |
| THIRD_DISC_AMT_AVAILABLE | PaymentScheduleThirdDiscAmtAvailable | ✅ |
| THIRD_DISCOUNT_DATE | PaymentScheduleThirdDiscountDate | ✅ |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| INVOICE_ID | PaymentScheduleInvoiceId | — |
| PAYMENT_NUM | PaymentSchedulePaymentNum | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 6/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DUE_DATE | PaymentScheduleDueDate | ✅ |
| INVOICE_ID | PaymentScheduleInvoiceId | — |
| LAST_UPDATE_DATE | PaymentScheduleLastUpdateDate | ✅ |
| ORG_ID | PaymentScheduleOrgId | — |
| PAYMENT_METHOD_CODE | PaymentSchedulePaymentMethodCode | ✅ |
| PAYMENT_NUM | PaymentSchedulePaymentNum | ✅ |
| PAYMENT_STATUS_FLAG | PaymentSchedulePaymentStatusFlag | ✅ |
| REMIT_TO_SUPPLIER_ID | InvoiceHeaderRemitToSupplierId | ✅ |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| RELATIONSHIP_ID | ApInvoicesAllRelationshipId | — |
| REMIT_TO_ADDRESS_ID | ApInvoicesAllRemitToAddressId | — |
| REMIT_TO_ADDRESS_NAME | ApInvoicesAllRemitToAddressName | — |
| REMIT_TO_SUPPLIER_ID | ApInvoicesAllRemitToSupplierId | — |
| REMIT_TO_SUPPLIER_NAME | ApInvoicesAllRemitToSupplierName | — |

---

## 📚 Referências

- [Oracle Docs — AP_PAYMENT_SCHEDULES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/appaymentschedulesall-10047.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
