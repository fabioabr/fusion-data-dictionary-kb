---
id: DOC-HCM-PVO-ElementClassificationsTranslation
doc_type: system-doc
title: "ElementClassificationsTranslation — PVO Human Capital Management"
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
  - ElementClassificationsTranslation
  - elementclassificationstranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementClassificationsTranslation

## 📌 Visão Geral

Extrai traduções das classificações de elementos de folha de pagamento. Suporta relatórios multilíngues de proventos e descontos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.ElementClassificationsTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 2 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[pay_ele_classifications_tl|PAY_ELE_CLASSIFICATIONS_TL]] — 11 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[pay_ele_classifications_tl|PAY_ELE_CLASSIFICATIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClassificationId | CLASSIFICATION_ID | 🔑 | ✅ |
| 2 | ElementClassificationTLClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | ElementClassificationTLCreatedBy | CREATED_BY | — | — |
| 4 | ElementClassificationTLCreationDate | CREATION_DATE | — | — |
| 5 | ElementClassificationTLDescription | DESCRIPTION | — | — |
| 6 | ElementClassificationTLLanguage | LANGUAGE | — | — |
| 7 | ElementClassificationTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ElementClassificationTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ElementClassificationTLLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ElementClassificationTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ElementClassificationTLSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
