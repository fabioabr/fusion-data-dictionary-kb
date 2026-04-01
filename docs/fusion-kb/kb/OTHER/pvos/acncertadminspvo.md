---
id: DOC-OTHER-PVO-ACNCertAdminsPVO
doc_type: system-doc
title: "ACNCertAdminsPVO — PVO Cross-Module"
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
  - ACNCertAdminsPVO
  - acncertadminspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ACNCertAdminsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de ACNCert Admins. Acessa as tabelas: GRC_ACN_CERT_ADMIN_USRS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ACNCertAdminsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_acn_cert_admin_usrs|GRC_ACN_CERT_ADMIN_USRS]] — 9 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_acn_cert_admin_usrs|GRC_ACN_CERT_ADMIN_USRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCertAdminsPEOCertificationId | CERTIFICATION_ID | 🔑 | ✅ |
| 2 | ACNCertAdminsPEOCreatedBy | CREATED_BY | — | — |
| 3 | ACNCertAdminsPEOCreationDate | CREATION_DATE | — | — |
| 4 | ACNCertAdminsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ACNCertAdminsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ACNCertAdminsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ACNCertAdminsPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 8 | ACNCertAdminsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ACNCertAdminsPEOUserId | USER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
