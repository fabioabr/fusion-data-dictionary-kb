---
id: DOC-OTHER-PVO-ACNCertAuditorsPVO
doc_type: system-doc
title: "ACNCertAuditorsPVO — PVO Cross-Module"
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
  - ACNCertAuditorsPVO
  - acncertauditorspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ACNCertAuditorsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de ACNCert Auditors. Acessa as tabelas: GRC_ACN_ROLE_AUDIT_USRS.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ACNCertAuditorsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[grc_acn_role_audit_usrs|GRC_ACN_ROLE_AUDIT_USRS]] — 9 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[grc_acn_role_audit_usrs|GRC_ACN_ROLE_AUDIT_USRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ACNCertAuditorsPEOCertRoleId | CERT_ROLE_ID | 🔑 | ✅ |
| 2 | ACNCertAuditorsPEOCreatedBy | CREATED_BY | — | — |
| 3 | ACNCertAuditorsPEOCreationDate | CREATION_DATE | — | — |
| 4 | ACNCertAuditorsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ACNCertAuditorsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ACNCertAuditorsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ACNCertAuditorsPEOObjectTypeCode | OBJECT_TYPE_CODE | — | — |
| 8 | ACNCertAuditorsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ACNCertAuditorsPEOUserId | USER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
