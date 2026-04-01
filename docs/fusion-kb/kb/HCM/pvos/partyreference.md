---
id: DOC-HCM-PVO-PartyReference
doc_type: system-doc
title: "PartyReference — PVO Human Capital Management"
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
  - PartyReference
  - partyreference
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartyReference

## 📌 Visão Geral

Extrai referências de sistemas de origem para entidades party (pessoas/organizações). Permite rastreabilidade de migração e reconciliação de cadastros entre sistemas legados e Fusion.

**Caminho:** `FscmTopModelAM.PartiesAnalyticsAM.PartyReference`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 3 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[hz_orig_sys_references|HZ_ORIG_SYS_REFERENCES]] — 17 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hz_orig_sys_references|HZ_ORIG_SYS_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | EndDateActive | END_DATE_ACTIVE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | OldOrigSystemReference | OLD_ORIG_SYSTEM_REFERENCE | — | — |
| 9 | OrigSystem | ORIG_SYSTEM | — | ✅ |
| 10 | OrigSystemRefId | ORIG_SYSTEM_REF_ID | 🔑 | ✅ |
| 11 | OrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 12 | OwnerTableId | OWNER_TABLE_ID | — | — |
| 13 | OwnerTableName | OWNER_TABLE_NAME | — | — |
| 14 | PartyId | PARTY_ID | — | — |
| 15 | ReasonCode | REASON_CODE | — | — |
| 16 | StartDateActive | START_DATE_ACTIVE | — | — |
| 17 | Status | STATUS | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
