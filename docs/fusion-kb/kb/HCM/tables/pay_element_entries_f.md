---
id: DOC-HCM-570
doc_type: system-doc
title: "PAY_ELEMENT_ENTRIES_F — Entradas de Elementos de Folha"
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
  - element-entries
  - entradas
  - pay-elem-entries
aliases:
  - PAY_ELEMENT_ENTRIES_F
  - pay_element_entries_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ELEMENT_ENTRIES_F

## 📌 Visão Geral

Tabela central que armazena as **entradas de elementos** (element entries) da folha de pagamento. Cada entrada vincula um elemento (provento ou desconto) a um colaborador com vigencia temporal. Eh o registro que efetivamente gera valores no calculo de folha.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Lancamento de proventos e descontos por colaborador
- Controle de vigencia de cada entrada de elemento
- Base para o calculo de folha de pagamento
- Historico de alteracoes em entradas

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ELEMENT_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da entrada | --- | 🟢 95% |
| 2 | ELEMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | ID do tipo de elemento | PAY_ELEMENT_TYPES_F | 🟢 95% |
| 3 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 90% |
| 4 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | ID do assignment | PER_ALL_ASSIGNMENTS_M | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | ENTRY_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de entrada (E, D, A, R, B) | --- | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_element_types_f]] --- via `ELEMENT_TYPE_ID` (tipo de elemento da entrada de folha)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha da entrada de elemento)

### Tabelas-filha (FK de saída)
- [[pay_element_entry_values_f]] --- via `ELEMENT_ENTRY_ID` (valores das entradas)

---

## 📎 Uso Típico

### Entradas vigentes por relacionamento de folha
```sql
SELECT ee.ELEMENT_ENTRY_ID, ee.ELEMENT_TYPE_ID, ee.ENTRY_TYPE
FROM   PAY_ELEMENT_ENTRIES_F ee
WHERE  ee.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN ee.EFFECTIVE_START_DATE AND ee.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Os valores efetivos de cada entrada estao em `PAY_ELEMENT_ENTRY_VALUES_F`.
- Tipos de entrada: E=Regular, D=Deducao adicional, A=Ajuste, R=Retroativo, B=Saldo inicial.

---

## 🔗 PVOs Relacionados

### [[bielemententriespvo|BIElementEntriesPVO]] (HCM · BICC: 155/155)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | BIElementEntriesPEOAttribute1 | ✅ |
| ATTRIBUTE10 | BIElementEntriesPEOAttribute10 | ✅ |
| ATTRIBUTE11 | BIElementEntriesPEOAttribute11 | ✅ |
| ATTRIBUTE12 | BIElementEntriesPEOAttribute12 | ✅ |
| ATTRIBUTE13 | BIElementEntriesPEOAttribute13 | ✅ |
| ATTRIBUTE14 | BIElementEntriesPEOAttribute14 | ✅ |
| ATTRIBUTE15 | BIElementEntriesPEOAttribute15 | ✅ |
| ATTRIBUTE16 | BIElementEntriesPEOAttribute16 | ✅ |
| ATTRIBUTE17 | BIElementEntriesPEOAttribute17 | ✅ |
| ATTRIBUTE18 | BIElementEntriesPEOAttribute18 | ✅ |
| ATTRIBUTE19 | BIElementEntriesPEOAttribute19 | ✅ |
| ATTRIBUTE2 | BIElementEntriesPEOAttribute2 | ✅ |
| ATTRIBUTE20 | BIElementEntriesPEOAttribute20 | ✅ |
| ATTRIBUTE21 | BIElementEntriesPEOAttribute21 | ✅ |
| ATTRIBUTE22 | BIElementEntriesPEOAttribute22 | ✅ |
| ATTRIBUTE23 | BIElementEntriesPEOAttribute23 | ✅ |
| ATTRIBUTE24 | BIElementEntriesPEOAttribute24 | ✅ |
| ATTRIBUTE25 | BIElementEntriesPEOAttribute25 | ✅ |
| ATTRIBUTE26 | BIElementEntriesPEOAttribute26 | ✅ |
| ATTRIBUTE27 | BIElementEntriesPEOAttribute27 | ✅ |
| ATTRIBUTE28 | BIElementEntriesPEOAttribute28 | ✅ |
| ATTRIBUTE29 | BIElementEntriesPEOAttribute29 | ✅ |
| ATTRIBUTE3 | BIElementEntriesPEOAttribute3 | ✅ |
| ATTRIBUTE30 | BIElementEntriesPEOAttribute30 | ✅ |
| ATTRIBUTE4 | BIElementEntriesPEOAttribute4 | ✅ |
| ATTRIBUTE5 | BIElementEntriesPEOAttribute5 | ✅ |
| ATTRIBUTE6 | BIElementEntriesPEOAttribute6 | ✅ |
| ATTRIBUTE7 | BIElementEntriesPEOAttribute7 | ✅ |
| ATTRIBUTE8 | BIElementEntriesPEOAttribute8 | ✅ |
| ATTRIBUTE9 | BIElementEntriesPEOAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | BIElementEntriesPEOAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | BIElementEntriesPEOAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | BIElementEntriesPEOAttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | BIElementEntriesPEOAttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | BIElementEntriesPEOAttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | BIElementEntriesPEOAttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | BIElementEntriesPEOAttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | BIElementEntriesPEOAttributeDate15 | ✅ |
| ATTRIBUTE_DATE2 | BIElementEntriesPEOAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | BIElementEntriesPEOAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | BIElementEntriesPEOAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | BIElementEntriesPEOAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | BIElementEntriesPEOAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | BIElementEntriesPEOAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | BIElementEntriesPEOAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | BIElementEntriesPEOAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | BIElementEntriesPEOAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | BIElementEntriesPEOAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | BIElementEntriesPEOAttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | BIElementEntriesPEOAttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | BIElementEntriesPEOAttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | BIElementEntriesPEOAttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | BIElementEntriesPEOAttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | BIElementEntriesPEOAttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | BIElementEntriesPEOAttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | BIElementEntriesPEOAttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | BIElementEntriesPEOAttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | BIElementEntriesPEOAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | BIElementEntriesPEOAttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER3 | BIElementEntriesPEOAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | BIElementEntriesPEOAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | BIElementEntriesPEOAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | BIElementEntriesPEOAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | BIElementEntriesPEOAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | BIElementEntriesPEOAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | BIElementEntriesPEOAttributeNumber9 | ✅ |
| BALANCE_ADJ_COST_FLAG | BIElementEntriesPEOBalanceAdjCostFlag | ✅ |
| BATCH_ACTION_ID | BIElementEntriesPEOBatchActionId | ✅ |
| BATCH_ID | BIElementEntriesPEOBatchId | ✅ |
| CREATED_BY | BIElementEntriesPEOCreatedBy | ✅ |
| CREATION_DATE | BIElementEntriesPEOCreationDate | ✅ |
| CREATOR_ID | BIElementEntriesPEOCreatorId | ✅ |
| CREATOR_TYPE | BIElementEntriesPEOCreatorType | ✅ |
| DATE_EARNED | BIElementEntriesPEODateEarned | ✅ |
| EFFECTIVE_END_DATE | BIElementEntriesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | BIElementEntriesPEOEffectiveStartDate | ✅ |
| ELEMENT_ENTRY_ID | BIElementEntriesPEOElementEntryId | ✅ |
| ELEMENT_TYPE_ID | BIElementEntriesPEOElementTypeId | ✅ |
| ENTERPRISE_ID | BIElementEntriesPEOEnterpriseId | ✅ |
| ENTRY_INFORMATION1 | BIElementEntriesPEOEntryInformation1 | ✅ |
| ENTRY_INFORMATION10 | BIElementEntriesPEOEntryInformation10 | ✅ |
| ENTRY_INFORMATION11 | BIElementEntriesPEOEntryInformation11 | ✅ |
| ENTRY_INFORMATION12 | BIElementEntriesPEOEntryInformation12 | ✅ |
| ENTRY_INFORMATION13 | BIElementEntriesPEOEntryInformation13 | ✅ |
| ENTRY_INFORMATION14 | BIElementEntriesPEOEntryInformation14 | ✅ |
| ENTRY_INFORMATION15 | BIElementEntriesPEOEntryInformation15 | ✅ |
| ENTRY_INFORMATION16 | BIElementEntriesPEOEntryInformation16 | ✅ |
| ENTRY_INFORMATION17 | BIElementEntriesPEOEntryInformation17 | ✅ |
| ENTRY_INFORMATION18 | BIElementEntriesPEOEntryInformation18 | ✅ |
| ENTRY_INFORMATION19 | BIElementEntriesPEOEntryInformation19 | ✅ |
| ENTRY_INFORMATION2 | BIElementEntriesPEOEntryInformation2 | ✅ |
| ENTRY_INFORMATION20 | BIElementEntriesPEOEntryInformation20 | ✅ |
| ENTRY_INFORMATION21 | BIElementEntriesPEOEntryInformation21 | ✅ |
| ENTRY_INFORMATION22 | BIElementEntriesPEOEntryInformation22 | ✅ |
| ENTRY_INFORMATION23 | BIElementEntriesPEOEntryInformation23 | ✅ |
| ENTRY_INFORMATION24 | BIElementEntriesPEOEntryInformation24 | ✅ |
| ENTRY_INFORMATION25 | BIElementEntriesPEOEntryInformation25 | ✅ |
| ENTRY_INFORMATION26 | BIElementEntriesPEOEntryInformation26 | ✅ |
| ENTRY_INFORMATION27 | BIElementEntriesPEOEntryInformation27 | ✅ |
| ENTRY_INFORMATION28 | BIElementEntriesPEOEntryInformation28 | ✅ |
| ENTRY_INFORMATION29 | BIElementEntriesPEOEntryInformation29 | ✅ |
| ENTRY_INFORMATION3 | BIElementEntriesPEOEntryInformation3 | ✅ |
| ENTRY_INFORMATION30 | BIElementEntriesPEOEntryInformation30 | ✅ |
| ENTRY_INFORMATION4 | BIElementEntriesPEOEntryInformation4 | ✅ |
| ENTRY_INFORMATION5 | BIElementEntriesPEOEntryInformation5 | ✅ |
| ENTRY_INFORMATION6 | BIElementEntriesPEOEntryInformation6 | ✅ |
| ENTRY_INFORMATION7 | BIElementEntriesPEOEntryInformation7 | ✅ |
| ENTRY_INFORMATION8 | BIElementEntriesPEOEntryInformation8 | ✅ |
| ENTRY_INFORMATION9 | BIElementEntriesPEOEntryInformation9 | ✅ |
| ENTRY_INFORMATION_CATEGORY | BIElementEntriesPEOEntryInformationCategory | ✅ |
| ENTRY_INFORMATION_DATE1 | BIElementEntriesPEOEntryInformationDate1 | ✅ |
| ENTRY_INFORMATION_DATE10 | BIElementEntriesPEOEntryInformationDate10 | ✅ |
| ENTRY_INFORMATION_DATE11 | BIElementEntriesPEOEntryInformationDate11 | ✅ |
| ENTRY_INFORMATION_DATE12 | BIElementEntriesPEOEntryInformationDate12 | ✅ |
| ENTRY_INFORMATION_DATE13 | BIElementEntriesPEOEntryInformationDate13 | ✅ |
| ENTRY_INFORMATION_DATE14 | BIElementEntriesPEOEntryInformationDate14 | ✅ |
| ENTRY_INFORMATION_DATE15 | BIElementEntriesPEOEntryInformationDate15 | ✅ |
| ENTRY_INFORMATION_DATE2 | BIElementEntriesPEOEntryInformationDate2 | ✅ |
| ENTRY_INFORMATION_DATE3 | BIElementEntriesPEOEntryInformationDate3 | ✅ |
| ENTRY_INFORMATION_DATE4 | BIElementEntriesPEOEntryInformationDate4 | ✅ |
| ENTRY_INFORMATION_DATE5 | BIElementEntriesPEOEntryInformationDate5 | ✅ |
| ENTRY_INFORMATION_DATE6 | BIElementEntriesPEOEntryInformationDate6 | ✅ |
| ENTRY_INFORMATION_DATE7 | BIElementEntriesPEOEntryInformationDate7 | ✅ |
| ENTRY_INFORMATION_DATE8 | BIElementEntriesPEOEntryInformationDate8 | ✅ |
| ENTRY_INFORMATION_DATE9 | BIElementEntriesPEOEntryInformationDate9 | ✅ |
| ENTRY_INFORMATION_NUMBER1 | BIElementEntriesPEOEntryInformationNumber1 | ✅ |
| ENTRY_INFORMATION_NUMBER10 | BIElementEntriesPEOEntryInformationNumber10 | ✅ |
| ENTRY_INFORMATION_NUMBER11 | BIElementEntriesPEOEntryInformationNumber11 | ✅ |
| ENTRY_INFORMATION_NUMBER12 | BIElementEntriesPEOEntryInformationNumber12 | ✅ |
| ENTRY_INFORMATION_NUMBER13 | BIElementEntriesPEOEntryInformationNumber13 | ✅ |
| ENTRY_INFORMATION_NUMBER14 | BIElementEntriesPEOEntryInformationNumber14 | ✅ |
| ENTRY_INFORMATION_NUMBER15 | BIElementEntriesPEOEntryInformationNumber15 | ✅ |
| ENTRY_INFORMATION_NUMBER16 | BIElementEntriesPEOEntryInformationNumber16 | ✅ |
| ENTRY_INFORMATION_NUMBER17 | BIElementEntriesPEOEntryInformationNumber17 | ✅ |
| ENTRY_INFORMATION_NUMBER18 | BIElementEntriesPEOEntryInformationNumber18 | ✅ |
| ENTRY_INFORMATION_NUMBER19 | BIElementEntriesPEOEntryInformationNumber19 | ✅ |
| ENTRY_INFORMATION_NUMBER2 | BIElementEntriesPEOEntryInformationNumber2 | ✅ |
| ENTRY_INFORMATION_NUMBER20 | BIElementEntriesPEOEntryInformationNumber20 | ✅ |
| ENTRY_INFORMATION_NUMBER3 | BIElementEntriesPEOEntryInformationNumber3 | ✅ |
| ENTRY_INFORMATION_NUMBER4 | BIElementEntriesPEOEntryInformationNumber4 | ✅ |
| ENTRY_INFORMATION_NUMBER5 | BIElementEntriesPEOEntryInformationNumber5 | ✅ |
| ENTRY_INFORMATION_NUMBER6 | BIElementEntriesPEOEntryInformationNumber6 | ✅ |
| ENTRY_INFORMATION_NUMBER7 | BIElementEntriesPEOEntryInformationNumber7 | ✅ |
| ENTRY_INFORMATION_NUMBER8 | BIElementEntriesPEOEntryInformationNumber8 | ✅ |
| ENTRY_INFORMATION_NUMBER9 | BIElementEntriesPEOEntryInformationNumber9 | ✅ |
| ENTRY_TYPE | BIElementEntriesPEOEntryType | ✅ |
| LAST_UPDATE_DATE | BIElementEntriesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BIElementEntriesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BIElementEntriesPEOLastUpdatedBy | ✅ |
| MULTIPLE_ENTRY_COUNT | BIElementEntriesPEOMultipleEntryCount | ✅ |
| OBJECT_VERSION_NUMBER | BIElementEntriesPEOObjectVersionNumber | ✅ |
| PERSON_ID | BIElementEntriesPEOPersonId | ✅ |
| REASON | BIElementEntriesPEOReason | ✅ |
| SUBPRIORITY | BIElementEntriesPEOSubpriority | ✅ |
| TARGET_ENTRY_ID | BIElementEntriesPEOTargetEntryId | ✅ |

### [[retroelemententry|RetroElementEntry]] (HCM · BICC: 6/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | ElementEntryAttributeCategory | — |
| BALANCE_ADJ_COST_FLAG | ElementEntryBalanceAdjCostFlag | ✅ |
| BATCH_ID | ElementEntryBatchId | — |
| CREATOR_ID | ElementEntryCreatorId | — |
| CREATOR_TYPE | ElementEntryCreatorType | ✅ |
| DATE_EARNED | ElementEntryDateEarned | ✅ |
| EFFECTIVE_END_DATE | ElementEntryEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ElementEntryEffectiveStartDate | ✅ |
| ELEMENT_ENTRY_ID | ElementEntryElementEntryId | — |
| ELEMENT_TYPE_ID | ElementEntryElementTypeId | — |
| ENTRY_INFORMATION_CATEGORY | ElementEntryEntryInformationCategory | — |
| ENTRY_TYPE | ElementEntryEntryType | ✅ |
| PERSON_ID | ElementEntryPersonId | — |
| REASON | ElementEntryReason | ✅ |
| SUBPRIORITY | ElementEntrySubpriority | — |
| TARGET_ENTRY_ID | ElementEntryTargetEntryId | — |

---

## 📚 Referências

- [Oracle Docs — PAY_ELEMENT_ENTRIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payelemententriesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
