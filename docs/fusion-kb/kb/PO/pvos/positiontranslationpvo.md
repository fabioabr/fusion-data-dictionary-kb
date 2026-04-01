---
id: DOC-PO-PVO-PositionTranslationPVO
doc_type: system-doc
title: "PositionTranslationPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PositionTranslationPVO
  - positiontranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PositionTranslationPVO

## 📌 Visão Geral

Extrai traduções de nomes e descrições de posições organizacionais para múltiplos idiomas. Garante consistência terminológica de cargos em organizações multinacionais.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PositionAM.PositionTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 10 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]] — 12 atributos (3 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | PositionId | POSITION_ID | 🔑 | ✅ |
| 5 | PositionTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PositionTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PositionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PositionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | PositionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PositionTranslationPEOName | NAME | — | ✅ |
| 11 | PositionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | PositionTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
