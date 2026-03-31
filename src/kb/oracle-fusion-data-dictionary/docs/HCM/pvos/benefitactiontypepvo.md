---
id: DOC-HCM-PVO-BenefitActionTypePVO
doc_type: system-doc
title: "BenefitActionTypePVO — PVO Human Capital Management"
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
  - BenefitActionTypePVO
  - benefitactiontypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BenefitActionTypePVO

## 📌 Visão Geral

Cataloga tipos de acao de beneficios com nome, nivel e descricao. Tabela de referencia para classificacao de eventos de life events e enrollment.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BenefitActionTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 78 | 1 | 1 | 6 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[ben_actn_typ_vl|BEN_ACTN_TYP_VL]] — 78 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[ben_actn_typ_vl|BEN_ACTN_TYP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTypeName | NAME | — | ✅ |
| 2 | ActnTypId | ACTN_TYP_ID | 🔑 | ✅ |
| 3 | ActnTypLvlCd | ACTN_TYP_LVL_CD | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | CreatedBy | CREATED_BY | — | — |
| 6 | CreationDate | CREATION_DATE | — | — |
| 7 | Description | DESCRIPTION | — | ✅ |
| 8 | EatAttribute1 | EAT_ATTRIBUTE1 | — | — |
| 9 | EatAttribute10 | EAT_ATTRIBUTE10 | — | — |
| 10 | EatAttribute11 | EAT_ATTRIBUTE11 | — | — |
| 11 | EatAttribute12 | EAT_ATTRIBUTE12 | — | — |
| 12 | EatAttribute13 | EAT_ATTRIBUTE13 | — | — |
| 13 | EatAttribute14 | EAT_ATTRIBUTE14 | — | — |
| 14 | EatAttribute15 | EAT_ATTRIBUTE15 | — | — |
| 15 | EatAttribute16 | EAT_ATTRIBUTE16 | — | — |
| 16 | EatAttribute17 | EAT_ATTRIBUTE17 | — | — |
| 17 | EatAttribute18 | EAT_ATTRIBUTE18 | — | — |
| 18 | EatAttribute19 | EAT_ATTRIBUTE19 | — | — |
| 19 | EatAttribute2 | EAT_ATTRIBUTE2 | — | — |
| 20 | EatAttribute20 | EAT_ATTRIBUTE20 | — | — |
| 21 | EatAttribute21 | EAT_ATTRIBUTE21 | — | — |
| 22 | EatAttribute22 | EAT_ATTRIBUTE22 | — | — |
| 23 | EatAttribute23 | EAT_ATTRIBUTE23 | — | — |
| 24 | EatAttribute24 | EAT_ATTRIBUTE24 | — | — |
| 25 | EatAttribute25 | EAT_ATTRIBUTE25 | — | — |
| 26 | EatAttribute26 | EAT_ATTRIBUTE26 | — | — |
| 27 | EatAttribute27 | EAT_ATTRIBUTE27 | — | — |
| 28 | EatAttribute28 | EAT_ATTRIBUTE28 | — | — |
| 29 | EatAttribute29 | EAT_ATTRIBUTE29 | — | — |
| 30 | EatAttribute3 | EAT_ATTRIBUTE3 | — | — |
| 31 | EatAttribute30 | EAT_ATTRIBUTE30 | — | — |
| 32 | EatAttribute4 | EAT_ATTRIBUTE4 | — | — |
| 33 | EatAttribute5 | EAT_ATTRIBUTE5 | — | — |
| 34 | EatAttribute6 | EAT_ATTRIBUTE6 | — | — |
| 35 | EatAttribute7 | EAT_ATTRIBUTE7 | — | — |
| 36 | EatAttribute8 | EAT_ATTRIBUTE8 | — | — |
| 37 | EatAttribute9 | EAT_ATTRIBUTE9 | — | — |
| 38 | EatAttributeCategory | EAT_ATTRIBUTE_CATEGORY | — | — |
| 39 | EatAttributeDate1 | EAT_ATTRIBUTE_DATE1 | — | — |
| 40 | EatAttributeDate10 | EAT_ATTRIBUTE_DATE10 | — | — |
| 41 | EatAttributeDate11 | EAT_ATTRIBUTE_DATE11 | — | — |
| 42 | EatAttributeDate12 | EAT_ATTRIBUTE_DATE12 | — | — |
| 43 | EatAttributeDate13 | EAT_ATTRIBUTE_DATE13 | — | — |
| 44 | EatAttributeDate14 | EAT_ATTRIBUTE_DATE14 | — | — |
| 45 | EatAttributeDate15 | EAT_ATTRIBUTE_DATE15 | — | — |
| 46 | EatAttributeDate2 | EAT_ATTRIBUTE_DATE2 | — | — |
| 47 | EatAttributeDate3 | EAT_ATTRIBUTE_DATE3 | — | — |
| 48 | EatAttributeDate4 | EAT_ATTRIBUTE_DATE4 | — | — |
| 49 | EatAttributeDate5 | EAT_ATTRIBUTE_DATE5 | — | — |
| 50 | EatAttributeDate6 | EAT_ATTRIBUTE_DATE6 | — | — |
| 51 | EatAttributeDate7 | EAT_ATTRIBUTE_DATE7 | — | — |
| 52 | EatAttributeDate8 | EAT_ATTRIBUTE_DATE8 | — | — |
| 53 | EatAttributeDate9 | EAT_ATTRIBUTE_DATE9 | — | — |
| 54 | EatAttributeNumber1 | EAT_ATTRIBUTE_NUMBER1 | — | — |
| 55 | EatAttributeNumber10 | EAT_ATTRIBUTE_NUMBER10 | — | — |
| 56 | EatAttributeNumber11 | EAT_ATTRIBUTE_NUMBER11 | — | — |
| 57 | EatAttributeNumber12 | EAT_ATTRIBUTE_NUMBER12 | — | — |
| 58 | EatAttributeNumber13 | EAT_ATTRIBUTE_NUMBER13 | — | — |
| 59 | EatAttributeNumber14 | EAT_ATTRIBUTE_NUMBER14 | — | — |
| 60 | EatAttributeNumber15 | EAT_ATTRIBUTE_NUMBER15 | — | — |
| 61 | EatAttributeNumber16 | EAT_ATTRIBUTE_NUMBER16 | — | — |
| 62 | EatAttributeNumber17 | EAT_ATTRIBUTE_NUMBER17 | — | — |
| 63 | EatAttributeNumber18 | EAT_ATTRIBUTE_NUMBER18 | — | — |
| 64 | EatAttributeNumber19 | EAT_ATTRIBUTE_NUMBER19 | — | — |
| 65 | EatAttributeNumber2 | EAT_ATTRIBUTE_NUMBER2 | — | — |
| 66 | EatAttributeNumber20 | EAT_ATTRIBUTE_NUMBER20 | — | — |
| 67 | EatAttributeNumber3 | EAT_ATTRIBUTE_NUMBER3 | — | — |
| 68 | EatAttributeNumber4 | EAT_ATTRIBUTE_NUMBER4 | — | — |
| 69 | EatAttributeNumber5 | EAT_ATTRIBUTE_NUMBER5 | — | — |
| 70 | EatAttributeNumber6 | EAT_ATTRIBUTE_NUMBER6 | — | — |
| 71 | EatAttributeNumber7 | EAT_ATTRIBUTE_NUMBER7 | — | — |
| 72 | EatAttributeNumber8 | EAT_ATTRIBUTE_NUMBER8 | — | — |
| 73 | EatAttributeNumber9 | EAT_ATTRIBUTE_NUMBER9 | — | — |
| 74 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 75 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 76 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 77 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 78 | TypeCd | TYPE_CD | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
