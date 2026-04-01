---
id: DOC-OTHER-PVO-AwardOrganizationPVO
doc_type: system-doc
title: "AwardOrganizationPVO — PVO Cross-Module"
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
  - AwardOrganizationPVO
  - awardorganizationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardOrganizationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Organization. Acessa as tabelas: GMS_ORGANIZATIONS_ALL_V.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardOrganizationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 5 | 1 | 1 | 5 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]] — 5 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[gms_organizations_all_v|GMS_ORGANIZATIONS_ALL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardOwningOrganizationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | AwardOwningOrganizationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | AwardOwningOrganizationPEOName | NAME | — | ✅ |
| 4 | AwardOwningOrganizationPEOStatus | STATUS | — | ✅ |
| 5 | OrganizationId | ORGANIZATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
