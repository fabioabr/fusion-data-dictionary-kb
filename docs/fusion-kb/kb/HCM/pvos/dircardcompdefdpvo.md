---
id: DOC-HCM-PVO-DIRCardCompDefDPVO
doc_type: system-doc
title: "DIRCardCompDefDPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
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
  - pvo
  - bicc
aliases:
  - DIRCardCompDefDPVO
  - dircardcompdefdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DIRCardCompDefDPVO

## 📌 Visão Geral

Extrai definições de componentes de cartão de instrução de pagamento direto (direct deposit). Utilizado na configuração de descontos e créditos em folha.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayDeductionSetupAM.DIRCardCompDefDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 3 | 14 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[pay_dir_card_comp_defs_f|PAY_DIR_CARD_COMP_DEFS_F]] — 22 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[pay_dir_card_comp_defs_f|PAY_DIR_CARD_COMP_DEFS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DIRCardCompDefBaseDPEOAssociableTerm | ASSOCIABLE_TERM | — | ✅ |
| 2 | DIRCardCompDefBaseDPEOAssociableTru | ASSOCIABLE_TRU | — | ✅ |
| 3 | DIRCardCompDefBaseDPEOBaseComponentName | BASE_COMPONENT_NAME | — | ✅ |
| 4 | DIRCardCompDefBaseDPEOBreakdownComponentFlag | BREAKDOWN_COMPONENT_FLAG | — | ✅ |
| 5 | DIRCardCompDefBaseDPEOCreatedBy | CREATED_BY | — | — |
| 6 | DIRCardCompDefBaseDPEOCreationDate | CREATION_DATE | — | — |
| 7 | DIRCardCompDefBaseDPEODeductionGroupId | DEDUCTION_GROUP_ID | — | — |
| 8 | DIRCardCompDefBaseDPEODeductionTypeId | DEDUCTION_TYPE_ID | — | ✅ |
| 9 | DIRCardCompDefBaseDPEODefaultingTruCompFlag | DEFAULTING_TRU_COMP_FLAG | — | ✅ |
| 10 | DIRCardCompDefBaseDPEODirCardDefinitionId | DIR_CARD_DEFINITION_ID | — | ✅ |
| 11 | DIRCardCompDefBaseDPEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 12 | DIRCardCompDefBaseDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | DIRCardCompDefBaseDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | DIRCardCompDefBaseDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | DIRCardCompDefBaseDPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 16 | DIRCardCompDefBaseDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 17 | DIRCardCompDefBaseDPEOMultipleAllowed | MULTIPLE_ALLOWED | — | — |
| 18 | DIRCardCompDefBaseDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | DIRCardCompDefBaseDPEORequired | REQUIRED | — | — |
| 20 | DirCardCompDefId | DIR_CARD_COMP_DEF_ID | 🔑 | ✅ |
| 21 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 22 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
