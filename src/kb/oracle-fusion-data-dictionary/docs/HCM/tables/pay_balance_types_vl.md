---
id: DOC-HCM-556
doc_type: system-doc
title: "PAY_BALANCE_TYPES_VL — Tipos de Saldo (View Localizada)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - balance-types-vl
  - view-localizada
  - pay-bal-types-vl
aliases:
  - PAY_BALANCE_TYPES_VL
  - pay_balance_types_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_TYPES_VL

## 📌 Visão Geral

**View localizada** (`_VL`) que combina a tabela base de tipos de saldo com traducoes no idioma da sessao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de tipos de saldo com traducao
- Uso em LOVs e interfaces de configuracao de folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de saldo | --- | 🟢 95% |
| 2 | BALANCE_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do saldo no idioma da sessao | --- | 🟢 90% |
| 3 | REPORTING_NAME | VARCHAR2(80) | NULL | Identificacao | Nome para relatorios | --- | 🟡 80% |
| 4 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 5 | BALANCE_CATEGORY_ID | NUMBER(18) | NULL | FK | ID da categoria de saldo | PAY_BALANCE_CATEGORIES_F | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela base de tipos de saldo

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Tipos de saldo com nome traduzido
```sql
SELECT vl.BALANCE_TYPE_ID, vl.BALANCE_NAME, vl.REPORTING_NAME
FROM   PAY_BALANCE_TYPES_VL vl
WHERE  vl.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.
- Retorna automaticamente o nome no idioma da sessao do usuario.

---

## 🔗 PVOs Relacionados

### [[balancetypespvo|BalanceTypesPVO]] (GL · BICC: 88/89)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | BalanceTypesPEOApplicationId | ✅ |
| ATTRIBUTE1 | BalanceTypesPEOAttribute1 | ✅ |
| ATTRIBUTE10 | BalanceTypesPEOAttribute10 | ✅ |
| ATTRIBUTE11 | BalanceTypesPEOAttribute11 | ✅ |
| ATTRIBUTE12 | BalanceTypesPEOAttribute12 | ✅ |
| ATTRIBUTE13 | BalanceTypesPEOAttribute13 | ✅ |
| ATTRIBUTE14 | BalanceTypesPEOAttribute14 | ✅ |
| ATTRIBUTE15 | BalanceTypesPEOAttribute15 | ✅ |
| ATTRIBUTE16 | BalanceTypesPEOAttribute16 | ✅ |
| ATTRIBUTE17 | BalanceTypesPEOAttribute17 | ✅ |
| ATTRIBUTE18 | BalanceTypesPEOAttribute18 | ✅ |
| ATTRIBUTE19 | BalanceTypesPEOAttribute19 | ✅ |
| ATTRIBUTE2 | BalanceTypesPEOAttribute2 | ✅ |
| ATTRIBUTE20 | BalanceTypesPEOAttribute20 | ✅ |
| ATTRIBUTE21 | BalanceTypesPEOAttribute21 | ✅ |
| ATTRIBUTE22 | BalanceTypesPEOAttribute22 | ✅ |
| ATTRIBUTE23 | BalanceTypesPEOAttribute23 | ✅ |
| ATTRIBUTE24 | BalanceTypesPEOAttribute24 | ✅ |
| ATTRIBUTE25 | BalanceTypesPEOAttribute25 | ✅ |
| ATTRIBUTE26 | BalanceTypesPEOAttribute26 | ✅ |
| ATTRIBUTE27 | BalanceTypesPEOAttribute27 | ✅ |
| ATTRIBUTE28 | BalanceTypesPEOAttribute28 | ✅ |
| ATTRIBUTE29 | BalanceTypesPEOAttribute29 | ✅ |
| ATTRIBUTE3 | BalanceTypesPEOAttribute3 | ✅ |
| ATTRIBUTE30 | BalanceTypesPEOAttribute30 | ✅ |
| ATTRIBUTE4 | BalanceTypesPEOAttribute4 | ✅ |
| ATTRIBUTE5 | BalanceTypesPEOAttribute5 | ✅ |
| ATTRIBUTE6 | BalanceTypesPEOAttribute6 | ✅ |
| ATTRIBUTE7 | BalanceTypesPEOAttribute7 | ✅ |
| ATTRIBUTE8 | BalanceTypesPEOAttribute8 | ✅ |
| ATTRIBUTE9 | BalanceTypesPEOAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | BalanceTypesPEOAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | BalanceTypesPEOAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | BalanceTypesPEOAttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | BalanceTypesPEOAttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | BalanceTypesPEOAttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | BalanceTypesPEOAttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | BalanceTypesPEOAttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | BalanceTypesPEOAttributeDate15 | ✅ |
| ATTRIBUTE_DATE2 | BalanceTypesPEOAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | BalanceTypesPEOAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | BalanceTypesPEOAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | BalanceTypesPEOAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | BalanceTypesPEOAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | BalanceTypesPEOAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | BalanceTypesPEOAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | BalanceTypesPEOAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | BalanceTypesPEOAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | BalanceTypesPEOAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | BalanceTypesPEOAttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | BalanceTypesPEOAttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | BalanceTypesPEOAttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | BalanceTypesPEOAttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | BalanceTypesPEOAttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | BalanceTypesPEOAttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | BalanceTypesPEOAttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | BalanceTypesPEOAttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | BalanceTypesPEOAttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | BalanceTypesPEOAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | BalanceTypesPEOAttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER3 | BalanceTypesPEOAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | BalanceTypesPEOAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | BalanceTypesPEOAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | BalanceTypesPEOAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | BalanceTypesPEOAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | BalanceTypesPEOAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | BalanceTypesPEOAttributeNumber9 | ✅ |
| BALANCE_CATEGORY_ID | BalanceTypesPEOBalanceCategoryId | ✅ |
| BALANCE_NAME | BalanceTypesPEOBalanceName | ✅ |
| BALANCE_TYPE_ID | BalanceTypesPEOBalanceTypeId | ✅ |
| BALANCE_UOM | BalanceTypesPEOBalanceUom | ✅ |
| BASE_BALANCE_NAME | BalanceTypesPEOBaseBalanceName | ✅ |
| BASE_BALANCE_TYPE_ID | BalanceTypesPEOBaseBalanceTypeId | ✅ |
| COMMENTS | BalanceTypesPEOComments | — |
| CREATED_BY | BalanceTypesPEOCreatedBy | ✅ |
| CREATION_DATE | BalanceTypesPEOCreationDate | ✅ |
| CURRENCY_CODE | BalanceTypesPEOCurrencyCode | ✅ |
| DEDUCTION_TYPE_ID | BalanceTypesPEODeductionTypeId | ✅ |
| ENTERPRISE_ID | BalanceTypesPEOEnterpriseId | ✅ |
| INPUT_VALUE_ID | BalanceTypesPEOInputValueId | ✅ |
| LAST_UPDATE_DATE | BalanceTypesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BalanceTypesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BalanceTypesPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | BalanceTypesPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | BalanceTypesPEOLegislativeDataGroupId | ✅ |
| MODULE_ID | BalanceTypesPEOModuleId | ✅ |
| OBJECT_VERSION_NUMBER | BalanceTypesPEOObjectVersionNumber | ✅ |
| REMUNERATION_FLAG | BalanceTypesPEORemunerationFlag | ✅ |
| REPORTING_NAME | BalanceTypesPEOReportingName | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_TYPES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancetypesvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
