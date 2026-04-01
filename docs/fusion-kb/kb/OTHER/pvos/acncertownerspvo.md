---
id: DOC-OTHER-PVO-ACNCertOwnersPVO
doc_type: system-doc
title: "ACNCertOwnersPVO — PVO Cross-Module"
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
  - ACNCertOwnersPVO
  - acncertownerspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ACNCertOwnersPVO

## 📌 Visão Geral

View Object para extração BICC de dados de ACNCert Owners. Acessa as tabelas: GRC_ACN_ROLE_OWNER_USRS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ACNCertOwnersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_acn_role_owner_usrs|GRC_ACN_ROLE_OWNER_USRS]] — 9 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_acn_role_owner_usrs|GRC_ACN_ROLE_OWNER_USRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCertOwnersPEOCertRoleId | CERT_ROLE_ID | 🔑 | ✅ |
| 2 | ACNCertOwnersPEOCreatedBy | CREATED_BY | — | — |
| 3 | ACNCertOwnersPEOCreationDate | CREATION_DATE | — | — |
| 4 | ACNCertOwnersPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ACNCertOwnersPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ACNCertOwnersPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ACNCertOwnersPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 8 | ACNCertOwnersPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ACNCertOwnersPEOUserId | USER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
