---
id: DOC-HCM-028
doc_type: system-doc
title: "BEN_BILL_CHARGES — Cobranças de Benefícios"
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
  - cobrancas
  - bill-charges
  - premium
aliases:
  - BEN_BILL_CHARGES
  - ben_bill_charges
  - cobrancas-beneficios
  - bill-charges
  - ben-bill-charges
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CHARGES

## 📌 Visão Geral

Armazena as **cobranças individuais** de benefícios. Cada registro representa um valor cobrado de um participante referente a um plano de benefício em um período específico.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Cobranças de Benefícios.
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
| 1 | BILL_CHARGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da cobrança | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador cobrado | [[per_all_people_f]] | 🟢 90% |
| 3 | PL_ID | NUMBER(18) | NULL | FK | Plano de benefício | [[ben_pl_f]] | 🟡 80% |
| 4 | CHARGE_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor da cobrança | — | 🟢 85% |
| 5 | CHARGE_STATUS | VARCHAR2(30) | NULL | Classificação | Status (PENDING, PAID, CANCELLED) | — | 🟡 80% |
| 6 | CHARGE_DATE | DATE | NOT NULL | Data | Data da cobrança | — | 🟢 85% |
| 7 | DUE_DATE | DATE | NULL | Data | Data de vencimento | — | 🟡 80% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da cobranca de beneficio)
- [[ben_pl_f]] — via `PL_ID` (plano de beneficio da cobranca)

### Tabelas-filha (FK de saída)
- [[ben_bill_charge_details]] — via `BILL_CHARGE_ID` (detalhes da cobranca de beneficio)
- [[ben_bill_charge_payments]] — via `BILL_CHARGE_ID` (pagamentos da cobranca de beneficio)

---

## 📎 Uso Típico

### Cobranças pendentes
```sql
SELECT bc.BILL_CHARGE_ID, bc.PERSON_ID, bc.CHARGE_AMOUNT,
       bc.CHARGE_STATUS, bc.DUE_DATE
FROM   BEN_BILL_CHARGES bc
WHERE  bc.CHARGE_STATUS = 'PENDING';
```

### Filtros comuns
- `CHARGE_STATUS = 'PENDING'` — Cobranças pendentes
- `CHARGE_STATUS = 'PAID'` — Cobranças pagas

---

## 🔒 Observações

- Cada cobrança está vinculada a um plano e um colaborador.
- Detalhes da composição do valor estão em `BEN_BILL_CHARGE_DETAILS`.

---

## 🔗 PVOs Relacionados

### [[billchargedetailspvo|BillChargeDetailsPVO]] (HCM · BICC: 24/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BCH_ATTRIBUTE1 | BchAttribute1 | — |
| BCH_ATTRIBUTE10 | BchAttribute10 | — |
| BCH_ATTRIBUTE2 | BchAttribute2 | — |
| BCH_ATTRIBUTE3 | BchAttribute3 | — |
| BCH_ATTRIBUTE4 | BchAttribute4 | — |
| BCH_ATTRIBUTE5 | BchAttribute5 | — |
| BCH_ATTRIBUTE6 | BchAttribute6 | — |
| BCH_ATTRIBUTE7 | BchAttribute7 | — |
| BCH_ATTRIBUTE8 | BchAttribute8 | — |
| BCH_ATTRIBUTE9 | BchAttribute9 | — |
| BCH_ATTRIBUTE_CATEGORY | BchAttributeCategory | — |
| BCH_ATTRIBUTE_DATE1 | BchAttributeDate1 | — |
| BCH_ATTRIBUTE_DATE2 | BchAttributeDate2 | — |
| BCH_ATTRIBUTE_DATE3 | BchAttributeDate3 | — |
| BCH_ATTRIBUTE_DATE4 | BchAttributeDate4 | — |
| BCH_ATTRIBUTE_DATE5 | BchAttributeDate5 | — |
| BCH_ATTRIBUTE_NUMBER1 | BchAttributeNumber1 | — |
| BCH_ATTRIBUTE_NUMBER2 | BchAttributeNumber2 | — |
| BCH_ATTRIBUTE_NUMBER3 | BchAttributeNumber3 | — |
| BCH_ATTRIBUTE_NUMBER4 | BchAttributeNumber4 | — |
| BCH_ATTRIBUTE_NUMBER5 | BchAttributeNumber5 | ✅ |
| BILL_CAL_ID | BillCalId | — |
| BILL_CHARGE_ID | BillChargeId1 | ✅ |
| BILL_GENERATED | BillGenerated | ✅ |
| BILL_GENERATED_DATE | BillGeneratedDate | ✅ |
| BILL_NUM | BillNum | ✅ |
| BILL_PERIOD | BillPeriod | ✅ |
| BILL_REASON | BillReason | ✅ |
| BILL_SOURCE | BillSource | ✅ |
| BILL_YEAR | BillYear | ✅ |
| BILLING_DATE | BillingDate | ✅ |
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
| CURRENT_BILL_AMT | CurrentBillAmt | ✅ |
| HOLD_BILL_FLAG | HoldBillFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| OTHER_AMT_DUE | OtherAmtDue | ✅ |
| PAST_AMT_DUE | PastAmtDue | ✅ |
| PER_ACCT_NUM | PerAcctNum | — |
| PER_BILL_INFO_ID | PerBillInfoId | — |
| PERSON_ID | PersonId | — |
| STATUS | Status1 | ✅ |
| TOTAL_BILL_AMT | TotalBillAmt | ✅ |
| TOTAL_TAX_AMT | TotalTaxAmt | ✅ |

### [[billchargespvo|BillChargesPVO]] (HCM · BICC: 24/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BCH_ATTRIBUTE1 | BchAttribute1 | — |
| BCH_ATTRIBUTE10 | BchAttribute10 | — |
| BCH_ATTRIBUTE2 | BchAttribute2 | — |
| BCH_ATTRIBUTE3 | BchAttribute3 | — |
| BCH_ATTRIBUTE4 | BchAttribute4 | — |
| BCH_ATTRIBUTE5 | BchAttribute5 | — |
| BCH_ATTRIBUTE6 | BchAttribute6 | — |
| BCH_ATTRIBUTE7 | BchAttribute7 | — |
| BCH_ATTRIBUTE8 | BchAttribute8 | — |
| BCH_ATTRIBUTE9 | BchAttribute9 | — |
| BCH_ATTRIBUTE_CATEGORY | BchAttributeCategory | — |
| BCH_ATTRIBUTE_DATE1 | BchAttributeDate1 | — |
| BCH_ATTRIBUTE_DATE2 | BchAttributeDate2 | — |
| BCH_ATTRIBUTE_DATE3 | BchAttributeDate3 | — |
| BCH_ATTRIBUTE_DATE4 | BchAttributeDate4 | — |
| BCH_ATTRIBUTE_DATE5 | BchAttributeDate5 | — |
| BCH_ATTRIBUTE_NUMBER1 | BchAttributeNumber1 | — |
| BCH_ATTRIBUTE_NUMBER2 | BchAttributeNumber2 | — |
| BCH_ATTRIBUTE_NUMBER3 | BchAttributeNumber3 | — |
| BCH_ATTRIBUTE_NUMBER4 | BchAttributeNumber4 | — |
| BCH_ATTRIBUTE_NUMBER5 | BchAttributeNumber5 | — |
| BILL_CAL_ID | BillCalId | — |
| BILL_CHARGE_ID | BillChargeId | ✅ |
| BILL_GENERATED | BillGenerated | ✅ |
| BILL_GENERATED_DATE | BillGeneratedDate | ✅ |
| BILL_NUM | BillNum | ✅ |
| BILL_PERIOD | BillPeriod | ✅ |
| BILL_REASON | BillReason | ✅ |
| BILL_SOURCE | BillSource | ✅ |
| BILL_YEAR | BillYear | ✅ |
| BILLING_DATE | BillingDate | ✅ |
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
| CURRENT_BILL_AMT | CurrentBillAmt | ✅ |
| HOLD_BILL_FLAG | HoldBillFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OTHER_AMT_DUE | OtherAmtDue | ✅ |
| PAST_AMT_DUE | PastAmtDue | ✅ |
| PER_ACCT_NUM | PerAcctNum | ✅ |
| PER_BILL_INFO_ID | PerBillInfoId | — |
| PERSON_ID | PersonId | — |
| STATUS | Status | ✅ |
| TOTAL_BILL_AMT | TotalBillAmt | ✅ |
| TOTAL_TAX_AMT | TotalTaxAmt | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CHARGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillcharges.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
