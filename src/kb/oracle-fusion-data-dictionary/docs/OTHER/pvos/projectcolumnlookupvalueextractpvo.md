---
id: DOC-OTHER-PVO-ProjectColumnLookupValueExtractPVO
doc_type: system-doc
title: "ProjectColumnLookupValueExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ProjectColumnLookupValueExtractPVO
  - projectcolumnlookupvalueextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectColumnLookupValueExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Column Lookup Value Extract. Acessa as tabelas: PJT_COLUMN_LKP_VALUES_B, PJT_COLUMN_LKP_VALUES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectColumnLookupValueExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_column_lkp_values_b|PJT_COLUMN_LKP_VALUES_B]] — 12 atributos (1 PKs, 12 BICC)
- [[pjt_column_lkp_values_tl|PJT_COLUMN_LKP_VALUES_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[pjt_column_lkp_values_b|PJT_COLUMN_LKP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtColumnLkpValuesBasePEOCodeValueId | CODE_VALUE_ID | 🔑 | ✅ |
| 2 | PjtColumnLkpValuesBasePEOColumnMapId | COLUMN_MAP_ID | — | ✅ |
| 3 | PjtColumnLkpValuesBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PjtColumnLkpValuesBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PjtColumnLkpValuesBasePEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 6 | PjtColumnLkpValuesBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | PjtColumnLkpValuesBasePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | PjtColumnLkpValuesBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | PjtColumnLkpValuesBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | PjtColumnLkpValuesBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | PjtColumnLkpValuesBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PjtColumnLkpValuesBasePEOUserLanguage | USER_LANGUAGE | — | ✅ |

### [[pjt_column_lkp_values_tl|PJT_COLUMN_LKP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtColumnLkpValuesTranslatio1CodeValueId | CODE_VALUE_ID | — | ✅ |
| 2 | PjtColumnLkpValuesTranslatio1CreatedBy | CREATED_BY | — | ✅ |
| 3 | PjtColumnLkpValuesTranslatio1CreationDate | CREATION_DATE | — | ✅ |
| 4 | PjtColumnLkpValuesTranslatio1Language | LANGUAGE | — | ✅ |
| 5 | PjtColumnLkpValuesTranslatio1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PjtColumnLkpValuesTranslatio1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PjtColumnLkpValuesTranslatio1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PjtColumnLkpValuesTranslatio1Meaning | MEANING | — | ✅ |
| 9 | PjtColumnLkpValuesTranslatio1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PjtColumnLkpValuesTranslatio1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
