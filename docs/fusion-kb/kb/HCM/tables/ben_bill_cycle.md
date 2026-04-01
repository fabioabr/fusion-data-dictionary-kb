---
id: DOC-HCM-031
doc_type: system-doc
title: "BEN_BILL_CYCLE — Ciclos de Cobrança de Benefícios"
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
  - ciclo-cobranca
  - bill-cycle
aliases:
  - BEN_BILL_CYCLE
  - ben_bill_cycle
  - ciclo-cobranca-beneficios
  - bill-cycle
  - ben-bill-cycle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CYCLE

## 📌 Visão Geral

Armazena os **ciclos de cobrança** (billing cycles) que definem a periodicidade e as regras de processamento de cobranças de benefícios.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Ciclos de Cobrança de Benefícios.
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
| 1 | BILL_CYCLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ciclo | — | 🟢 90% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do ciclo de cobrança | — | 🟢 90% |
| 3 | CYCLE_FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência do ciclo | — | 🟡 80% |
| 4 | CYCLE_STATUS | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta.

### Tabelas-filha (FK de saída)
- [[ben_bill_charges]] — via `BILL_CYCLE_ID` (cobranças do ciclo)

---

## 📎 Uso Típico

### Ciclos ativos
```sql
SELECT bc.BILL_CYCLE_ID, bc.NAME, bc.CYCLE_FREQUENCY
FROM   BEN_BILL_CYCLE bc
WHERE  bc.CYCLE_STATUS = 'ACTIVE';
```

### Filtros comuns
- `CYCLE_STATUS = 'ACTIVE'` — Ciclos ativos

---

## 🔒 Observações

- Define a periodicidade de processamento de cobranças.
- Vinculado ao calendário de cobrança para determinar datas específicas.

---

## 🔗 PVOs Relacionados

### [[billcalendarpvo|BillCalendarPVO]] (HCM · BICC: 9/51)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BCL_ATTRIBUTE1 | BclAttribute1 | — |
| BCL_ATTRIBUTE10 | BclAttribute10 | — |
| BCL_ATTRIBUTE2 | BclAttribute2 | — |
| BCL_ATTRIBUTE3 | BclAttribute3 | — |
| BCL_ATTRIBUTE4 | BclAttribute4 | — |
| BCL_ATTRIBUTE5 | BclAttribute5 | — |
| BCL_ATTRIBUTE6 | BclAttribute6 | — |
| BCL_ATTRIBUTE7 | BclAttribute7 | — |
| BCL_ATTRIBUTE8 | BclAttribute8 | — |
| BCL_ATTRIBUTE9 | BclAttribute9 | — |
| BCL_ATTRIBUTE_CATEGORY | BclAttributeCategory | — |
| BCL_ATTRIBUTE_DATE1 | BclAttributeDate1 | — |
| BCL_ATTRIBUTE_DATE2 | BclAttributeDate2 | — |
| BCL_ATTRIBUTE_DATE3 | BclAttributeDate3 | — |
| BCL_ATTRIBUTE_DATE4 | BclAttributeDate4 | — |
| BCL_ATTRIBUTE_DATE5 | BclAttributeDate5 | — |
| BCL_ATTRIBUTE_NUMBER1 | BclAttributeNumber1 | — |
| BCL_ATTRIBUTE_NUMBER2 | BclAttributeNumber2 | — |
| BCL_ATTRIBUTE_NUMBER3 | BclAttributeNumber3 | — |
| BCL_ATTRIBUTE_NUMBER4 | BclAttributeNumber4 | — |
| BCL_ATTRIBUTE_NUMBER5 | BclAttributeNumber5 | — |
| BILL_CYCLE_ID | BillCyclePEOBillCycleId | ✅ |
| BILL_FREQ | BillFreq | ✅ |
| BILLING_DAY | BillingDay | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
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
| DAYS_OVERDUE | DaysOverdue | ✅ |
| DESCRIPTION | Description | ✅ |
| DUE_DAY | DueDay | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| TYPE | Type | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CYCLE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillcycle.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
