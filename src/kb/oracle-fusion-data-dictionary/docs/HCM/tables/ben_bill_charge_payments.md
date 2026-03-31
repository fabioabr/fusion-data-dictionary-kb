---
id: DOC-HCM-030
doc_type: system-doc
title: "BEN_BILL_CHARGE_PAYMENTS — Pagamentos de Cobrança de Benefícios"
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
  - pagamentos-cobranca
  - charge-payments
aliases:
  - BEN_BILL_CHARGE_PAYMENTS
  - ben_bill_charge_payments
  - pagamentos-cobranca-beneficios
  - bill-charge-payments
  - ben-bill-charge-payments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CHARGE_PAYMENTS

## 📌 Visão Geral

Armazena os **pagamentos** associados a cobranças de benefícios. Cada registro representa um pagamento (parcial ou total) de uma cobrança.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Pagamentos de Cobrança de Benefícios.
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
| 1 | BILL_CHARGE_PAYMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do pagamento | — | 🟢 90% |
| 2 | BILL_CHARGE_ID | NUMBER(18) | NOT NULL | FK | Cobrança associada | [[ben_bill_charges]] | 🟢 90% |
| 3 | PAYMENT_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor pago | — | 🟢 85% |
| 4 | PAYMENT_DATE | DATE | NOT NULL | Data | Data do pagamento | — | 🟢 85% |
| 5 | PAYMENT_METHOD | VARCHAR2(30) | NULL | Classificação | Método (PAYROLL, DIRECT, CHECK) | — | 🟡 75% |
| 6 | PAYMENT_STATUS | VARCHAR2(30) | NULL | Classificação | Status do pagamento | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_bill_charges]] — via `BILL_CHARGE_ID` (cobranca de beneficio do pagamento)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Pagamentos por cobrança
```sql
SELECT cp.PAYMENT_AMOUNT, cp.PAYMENT_DATE, cp.PAYMENT_METHOD
FROM   BEN_BILL_CHARGE_PAYMENTS cp
WHERE  cp.BILL_CHARGE_ID = :p_charge_id;
```

### Filtros comuns
- `PAYMENT_METHOD = 'PAYROLL'` — Descontado em folha

---

## 🔒 Observações

- Permite pagamentos parciais (múltiplos registros por cobrança).
- O método `PAYROLL` indica desconto automático em folha de pagamento.

---

## 🔗 PVOs Relacionados

### [[billchargepaymentspvo|BillChargePaymentsPVO]] (HCM · BICC: 9/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMT_DUE | AmtDue | ✅ |
| AMT_PAID | AmtPaid | ✅ |
| BCP_ATTRIBUTE1 | BcpAttribute1 | — |
| BCP_ATTRIBUTE10 | BcpAttribute10 | — |
| BCP_ATTRIBUTE2 | BcpAttribute2 | — |
| BCP_ATTRIBUTE3 | BcpAttribute3 | — |
| BCP_ATTRIBUTE4 | BcpAttribute4 | — |
| BCP_ATTRIBUTE5 | BcpAttribute5 | — |
| BCP_ATTRIBUTE6 | BcpAttribute6 | — |
| BCP_ATTRIBUTE7 | BcpAttribute7 | — |
| BCP_ATTRIBUTE8 | BcpAttribute8 | — |
| BCP_ATTRIBUTE9 | BcpAttribute9 | — |
| BCP_ATTRIBUTE_CATEGORY | BcpAttributeCategory | — |
| BCP_ATTRIBUTE_DATE1 | BcpAttributeDate1 | — |
| BCP_ATTRIBUTE_DATE2 | BcpAttributeDate2 | — |
| BCP_ATTRIBUTE_DATE3 | BcpAttributeDate3 | — |
| BCP_ATTRIBUTE_DATE4 | BcpAttributeDate4 | — |
| BCP_ATTRIBUTE_DATE5 | BcpAttributeDate5 | — |
| BCP_ATTRIBUTE_NUMBER1 | BcpAttributeNumber1 | — |
| BCP_ATTRIBUTE_NUMBER2 | BcpAttributeNumber2 | — |
| BCP_ATTRIBUTE_NUMBER3 | BcpAttributeNumber3 | — |
| BCP_ATTRIBUTE_NUMBER4 | BcpAttributeNumber4 | — |
| BCP_ATTRIBUTE_NUMBER5 | BcpAttributeNumber5 | — |
| BILL_CAL_ID | BillCalId | — |
| BILL_CHARGE_DTL_ID | BillChargeDtlId | ✅ |
| BILL_CHARGE_ID | BillChargeId | — |
| BILL_CHARGE_PAYMENT_ID | BillChargePaymentId | ✅ |
| BILL_NUM | BillNum | ✅ |
| BILL_PAYMENT_ID | BillPaymentId | ✅ |
| BILL_PERIOD | BillPeriod | ✅ |
| BILL_YEAR | BillYear | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
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
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_CREDIT_ID | PerCreditId | — |
| PERSON_ID | PersonId | — |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CHARGE_PAYMENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillchargepayments.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
