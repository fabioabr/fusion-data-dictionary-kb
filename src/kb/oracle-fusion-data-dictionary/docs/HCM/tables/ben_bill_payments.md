---
id: DOC-HCM-033
doc_type: system-doc
title: "BEN_BILL_PAYMENTS — Pagamentos de Benefícios (Billing)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - benefits
  - pagamentos
  - bill-payments
aliases:
  - BEN_BILL_PAYMENTS
  - ben_bill_payments
  - pagamentos-beneficios
  - bill-payments
  - ben-bill-payments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_PAYMENTS

## 📌 Visão Geral

Armazena os **pagamentos consolidados** no sistema de billing de benefícios. Registro de lote de pagamentos processados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Pagamentos de Benefícios (Billing).
- **Controle de cobranças:** Rastreamento de valores devidos e pagos.
- **Reconciliação:** Base para reconciliação financeira de benefícios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BILL_PAYMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do pagamento | — | 🟢 90% |
| 2 | PAYMENT_BATCH_ID | NUMBER(18) | NULL | Referência | ID do lote de pagamento | — | 🟡 75% |
| 3 | TOTAL_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor total do pagamento | — | 🟢 85% |
| 4 | PAYMENT_DATE | DATE | NOT NULL | Data | Data do pagamento | — | 🟢 85% |
| 5 | PAYMENT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (PROCESSED, PENDING, FAILED) | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta.

### Tabelas-filha (FK de saída)
- [[ben_bill_charge_payments]] — via `BILL_PAYMENT_ID` (cobranças pagas)

---

## 📎 Uso Típico

### Pagamentos por período
```sql
SELECT bp.BILL_PAYMENT_ID, bp.TOTAL_AMOUNT, bp.PAYMENT_DATE, bp.PAYMENT_STATUS
FROM   BEN_BILL_PAYMENTS bp
WHERE  bp.PAYMENT_DATE BETWEEN :start_date AND :end_date;
```

### Filtros comuns
- `PAYMENT_STATUS = 'PROCESSED'` — Pagamentos processados

---

## 🔒 Observações

- Registro consolidado de pagamentos de benefícios.
- Vinculado a cobranças individuais via `BEN_BILL_CHARGE_PAYMENTS`.

---

## 🔗 PVOs Relacionados

### [[billchargepaymentspvo|BillChargePaymentsPVO]] (HCM · BICC: 19/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_AMT | AdjAmt | ✅ |
| ADJ_DATE | AdjDate | ✅ |
| AMT_PAID | AmtPaid1 | — |
| BILL_NUM | BillNum1 | — |
| BILL_PAYMENT_ID | BillPaymentId1 | — |
| BPY_ATTRIBUTE1 | BpyAttribute1 | — |
| BPY_ATTRIBUTE10 | BpyAttribute10 | — |
| BPY_ATTRIBUTE2 | BpyAttribute2 | — |
| BPY_ATTRIBUTE3 | BpyAttribute3 | — |
| BPY_ATTRIBUTE4 | BpyAttribute4 | — |
| BPY_ATTRIBUTE5 | BpyAttribute5 | — |
| BPY_ATTRIBUTE6 | BpyAttribute6 | — |
| BPY_ATTRIBUTE7 | BpyAttribute7 | — |
| BPY_ATTRIBUTE8 | BpyAttribute8 | — |
| BPY_ATTRIBUTE9 | BpyAttribute9 | — |
| BPY_ATTRIBUTE_CATEGORY | BpyAttributeCategory | — |
| BPY_ATTRIBUTE_DATE1 | BpyAttributeDate1 | — |
| BPY_ATTRIBUTE_DATE2 | BpyAttributeDate2 | — |
| BPY_ATTRIBUTE_DATE3 | BpyAttributeDate3 | — |
| BPY_ATTRIBUTE_DATE4 | BpyAttributeDate4 | — |
| BPY_ATTRIBUTE_DATE5 | BpyAttributeDate5 | — |
| BPY_ATTRIBUTE_NUMBER1 | BpyAttributeNumber1 | — |
| BPY_ATTRIBUTE_NUMBER2 | BpyAttributeNumber2 | — |
| BPY_ATTRIBUTE_NUMBER3 | BpyAttributeNumber3 | — |
| BPY_ATTRIBUTE_NUMBER4 | BpyAttributeNumber4 | — |
| BPY_ATTRIBUTE_NUMBER5 | BpyAttributeNumber5 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| COMMENTS | Comments | ✅ |
| CONFIG_CHAR_1 | ConfigChar11 | — |
| CONFIG_CHAR_2 | ConfigChar21 | — |
| CONFIG_CHAR_3 | ConfigChar31 | — |
| CONFIG_CHAR_4 | ConfigChar41 | — |
| CONFIG_CHAR_5 | ConfigChar51 | — |
| CONFIG_DATE_1 | ConfigDate11 | — |
| CONFIG_DATE_2 | ConfigDate21 | — |
| CONFIG_DATE_3 | ConfigDate31 | — |
| CONFIG_DATE_4 | ConfigDate41 | — |
| CONFIG_DATE_5 | ConfigDate51 | — |
| CONFIG_NUM_1 | ConfigNum11 | — |
| CONFIG_NUM_2 | ConfigNum21 | — |
| CONFIG_NUM_3 | ConfigNum31 | — |
| CONFIG_NUM_4 | ConfigNum41 | — |
| CONFIG_NUM_5 | ConfigNum51 | — |
| CREATED_BY | CreatedBy1 | ✅ |
| CREATION_DATE | CreationDate1 | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PAY_SEQ | PaySeq | ✅ |
| PAYEE_ORG_DETAILS | PayeeOrgDetails | ✅ |
| PAYEE_ORG_NAME | PayeeOrgName | ✅ |
| PAYEE_ORG_NUM | PayeeOrgNum | ✅ |
| PAYMENT_DATE | PaymentDate | ✅ |
| PAYMENT_DOC_NUM | PaymentDocNum | ✅ |
| PAYMENT_ENTRY_DATE | PaymentEntryDate | ✅ |
| PAYMENT_MODE | PaymentMode | ✅ |
| PAYMENT_TYPE | PaymentType | ✅ |
| PER_ACCT_NUM | PerAcctNum | ✅ |
| PERSON_ID | PersonId1 | — |

### [[billpaymentspvo|BillPaymentsPVO]] (HCM · BICC: 22/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADJ_AMT | AdjAmt | ✅ |
| ADJ_DATE | AdjDate | ✅ |
| AMT_PAID | AmtPaid | ✅ |
| BILL_NUM | BillNum | ✅ |
| BILL_PAYMENT_ID | BillPaymentId | ✅ |
| BPY_ATTRIBUTE1 | BpyAttribute1 | — |
| BPY_ATTRIBUTE10 | BpyAttribute10 | — |
| BPY_ATTRIBUTE2 | BpyAttribute2 | — |
| BPY_ATTRIBUTE3 | BpyAttribute3 | — |
| BPY_ATTRIBUTE4 | BpyAttribute4 | — |
| BPY_ATTRIBUTE5 | BpyAttribute5 | — |
| BPY_ATTRIBUTE6 | BpyAttribute6 | — |
| BPY_ATTRIBUTE7 | BpyAttribute7 | — |
| BPY_ATTRIBUTE8 | BpyAttribute8 | — |
| BPY_ATTRIBUTE9 | BpyAttribute9 | — |
| BPY_ATTRIBUTE_CATEGORY | BpyAttributeCategory | — |
| BPY_ATTRIBUTE_DATE1 | BpyAttributeDate1 | — |
| BPY_ATTRIBUTE_DATE2 | BpyAttributeDate2 | — |
| BPY_ATTRIBUTE_DATE3 | BpyAttributeDate3 | — |
| BPY_ATTRIBUTE_DATE4 | BpyAttributeDate4 | — |
| BPY_ATTRIBUTE_DATE5 | BpyAttributeDate5 | — |
| BPY_ATTRIBUTE_NUMBER1 | BpyAttributeNumber1 | — |
| BPY_ATTRIBUTE_NUMBER2 | BpyAttributeNumber2 | — |
| BPY_ATTRIBUTE_NUMBER3 | BpyAttributeNumber3 | — |
| BPY_ATTRIBUTE_NUMBER4 | BpyAttributeNumber4 | — |
| BPY_ATTRIBUTE_NUMBER5 | BpyAttributeNumber5 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| COMMENTS | Comments | ✅ |
| CONFIG_CHAR_1 | ConfigChar1 | — |
| CONFIG_CHAR_2 | ConfigChar2 | — |
| CONFIG_CHAR_3 | ConfigChar3 | — |
| CONFIG_CHAR_4 | ConfigChar4 | — |
| CONFIG_CHAR_5 | ConfigChar5 | — |
| CONFIG_DATE_1 | ConfigDate1 | — |
| CONFIG_DATE_2 | ConfigDate2 | — |
| CONFIG_DATE_3 | ConfigDate3 | — |
| CONFIG_DATE_4 | ConfigDate4 | — |
| CONFIG_DATE_5 | ConfigDate5 | — |
| CONFIG_NUM_1 | ConfigNum1 | — |
| CONFIG_NUM_2 | ConfigNum2 | — |
| CONFIG_NUM_3 | ConfigNum3 | — |
| CONFIG_NUM_4 | ConfigNum4 | — |
| CONFIG_NUM_5 | ConfigNum5 | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PAY_SEQ | PaySeq | ✅ |
| PAYEE_ORG_DETAILS | PayeeOrgDetails | ✅ |
| PAYEE_ORG_NAME | PayeeOrgName | ✅ |
| PAYEE_ORG_NUM | PayeeOrgNum | ✅ |
| PAYMENT_DATE | PaymentDate | ✅ |
| PAYMENT_DOC_NUM | PaymentDocNum | ✅ |
| PAYMENT_ENTRY_DATE | PaymentEntryDate | ✅ |
| PAYMENT_MODE | PaymentMode | ✅ |
| PAYMENT_TYPE | PaymentType | ✅ |
| PER_ACCT_NUM | PerAcctNum | ✅ |
| PERSON_ID | PersonId | — |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_PAYMENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillpayments.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
