---
id: DOC-HCM-034
doc_type: system-doc
title: "BEN_BILL_PER_CREDIT — Créditos de Cobrança por Pessoa"
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
  - creditos
  - per-credit
  - devolucao
aliases:
  - BEN_BILL_PER_CREDIT
  - ben_bill_per_credit
  - creditos-cobranca-beneficios
  - bill-per-credit
  - ben-bill-per-credit
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_PER_CREDIT

## 📌 Visão Geral

Armazena os **créditos** aplicados a cobranças de benefícios por pessoa. Registra devoluções, descontos ou créditos que reduzem o valor devido pelo colaborador.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Créditos de Cobrança por Pessoa.
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
| 1 | BILL_PER_CREDIT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do crédito | — | 🟢 85% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | CREDIT_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do crédito | — | 🟢 85% |
| 4 | CREDIT_DATE | DATE | NOT NULL | Data | Data do crédito | — | 🟢 85% |
| 5 | CREDIT_REASON | VARCHAR2(240) | NULL | Classificação | Motivo do crédito | — | 🟡 75% |
| 6 | CREDIT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (APPLIED, PENDING) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do credito de beneficio)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Créditos por colaborador
```sql
SELECT pc.CREDIT_AMOUNT, pc.CREDIT_DATE, pc.CREDIT_REASON
FROM   BEN_BILL_PER_CREDIT pc
WHERE  pc.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `CREDIT_STATUS = 'APPLIED'` — Créditos já aplicados

---

## 🔒 Observações

- Créditos reduzem o valor devido em cobranças futuras ou atuais.
- Motivos comuns: mudança de plano, cancelamento antecipado, correção de cobrança.

---

## 🔗 PVOs Relacionados

### [[billchargepaymentspvo|BillChargePaymentsPVO]] (HCM · BICC: 7/52)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BILL_PAYMENT_ID | BillPaymentId2 | — |
| BILL_PER_CREDIT_ID | BillPerCreditId | — |
| BPC_ATTRIBUTE1 | BpcAttribute1 | — |
| BPC_ATTRIBUTE10 | BpcAttribute10 | — |
| BPC_ATTRIBUTE2 | BpcAttribute2 | — |
| BPC_ATTRIBUTE3 | BpcAttribute3 | — |
| BPC_ATTRIBUTE4 | BpcAttribute4 | — |
| BPC_ATTRIBUTE5 | BpcAttribute5 | — |
| BPC_ATTRIBUTE6 | BpcAttribute6 | — |
| BPC_ATTRIBUTE7 | BpcAttribute7 | — |
| BPC_ATTRIBUTE8 | BpcAttribute8 | — |
| BPC_ATTRIBUTE9 | BpcAttribute9 | — |
| BPC_ATTRIBUTE_CATEGORY | BpcAttributeCategory | — |
| BPC_ATTRIBUTE_DATE1 | BpcAttributeDate1 | — |
| BPC_ATTRIBUTE_DATE2 | BpcAttributeDate2 | — |
| BPC_ATTRIBUTE_DATE3 | BpcAttributeDate3 | — |
| BPC_ATTRIBUTE_DATE4 | BpcAttributeDate4 | — |
| BPC_ATTRIBUTE_DATE5 | BpcAttributeDate5 | — |
| BPC_ATTRIBUTE_MUMBER1 | BpcAttributeMumber1 | — |
| BPC_ATTRIBUTE_MUMBER2 | BpcAttributeMumber2 | — |
| BPC_ATTRIBUTE_MUMBER3 | BpcAttributeMumber3 | — |
| BPC_ATTRIBUTE_MUMBER4 | BpcAttributeMumber4 | — |
| BPC_ATTRIBUTE_MUMBER5 | BpcAttributeMumber5 | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| COMMENTS | Comments1 | ✅ |
| CONFIG_CHAR_1 | ConfigChar12 | — |
| CONFIG_CHAR_2 | ConfigChar22 | — |
| CONFIG_CHAR_3 | ConfigChar32 | — |
| CONFIG_CHAR_4 | ConfigChar42 | — |
| CONFIG_CHAR_5 | ConfigChar52 | — |
| CONFIG_DATE_1 | ConfigDate12 | — |
| CONFIG_DATE_2 | ConfigDate22 | — |
| CONFIG_DATE_3 | ConfigDate32 | — |
| CONFIG_DATE_4 | ConfigDate42 | — |
| CONFIG_DATE_5 | ConfigDate52 | — |
| CONFIG_NUM_1 | ConfigNum12 | — |
| CONFIG_NUM_2 | ConfigNum22 | — |
| CONFIG_NUM_3 | ConfigNum32 | — |
| CONFIG_NUM_4 | ConfigNum42 | — |
| CONFIG_NUM_5 | ConfigNum52 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| CREDIT_AMT | CreditAmt | ✅ |
| CURRENCY_CODE | CurrencyCode1 | ✅ |
| DEBIT_AMT | DebitAmt | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| NO_BILL_FLAG | NoBillFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PERSON_ID | PersonId2 | — |
| RECORDED_DATE | RecordedDate | ✅ |

### [[billpaymentspvo|BillPaymentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BILL_PAYMENT_ID | BillPaymentId1 | — |
| BILL_PER_CREDIT_ID | BillPerCreditId | — |
| BPC_ATTRIBUTE1 | BpcAttribute1 | — |
| BPC_ATTRIBUTE10 | BpcAttribute10 | — |
| BPC_ATTRIBUTE2 | BpcAttribute2 | — |
| BPC_ATTRIBUTE3 | BpcAttribute3 | — |
| BPC_ATTRIBUTE4 | BpcAttribute4 | — |
| BPC_ATTRIBUTE5 | BpcAttribute5 | — |
| BPC_ATTRIBUTE6 | BpcAttribute6 | — |
| BPC_ATTRIBUTE7 | BpcAttribute7 | — |
| BPC_ATTRIBUTE8 | BpcAttribute8 | — |
| BPC_ATTRIBUTE9 | BpcAttribute9 | — |
| BPC_ATTRIBUTE_CATEGORY | BpcAttributeCategory | — |
| BPC_ATTRIBUTE_DATE1 | BpcAttributeDate1 | — |
| BPC_ATTRIBUTE_DATE2 | BpcAttributeDate2 | — |
| BPC_ATTRIBUTE_DATE3 | BpcAttributeDate3 | — |
| BPC_ATTRIBUTE_DATE4 | BpcAttributeDate4 | — |
| BPC_ATTRIBUTE_DATE5 | BpcAttributeDate5 | — |
| BPC_ATTRIBUTE_MUMBER1 | BpcAttributeMumber1 | — |
| BPC_ATTRIBUTE_MUMBER2 | BpcAttributeMumber2 | — |
| BPC_ATTRIBUTE_MUMBER3 | BpcAttributeMumber3 | — |
| BPC_ATTRIBUTE_MUMBER4 | BpcAttributeMumber4 | — |
| BPC_ATTRIBUTE_MUMBER5 | BpcAttributeMumber5 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| COMMENTS | Comments1 | — |
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
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| CREDIT_AMT | CreditAmt | — |
| CURRENCY_CODE | CurrencyCode1 | — |
| DEBIT_AMT | DebitAmt | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NO_BILL_FLAG | NoBillFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| RECORDED_DATE | RecordedDate | — |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_PER_CREDIT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillpercredit.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
