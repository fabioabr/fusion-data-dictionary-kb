---
id: DOC-HCM-PVO-ChangeAuditPVO
doc_type: system-doc
title: "ChangeAuditPVO — PVO Human Capital Management"
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
  - ChangeAuditPVO
  - changeauditpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeAuditPVO

## 📌 Visão Geral

Registra auditorias de alteracao no repositorio de tempo com tipo de acao e responsavel. Fundamental para compliance e rastreamento de mudancas em time tracking.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.ChangeAuditPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 11 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_audits|HWM_TM_AUDITS]] — 18 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_audits|HWM_TM_AUDITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionType | ACTION_TYPE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | OrigAuditId | ORIG_AUDIT_ID | — | — |
| 10 | ReasonCode | REASON_CODE | — | ✅ |
| 11 | RefDate | REF_DATE | — | ✅ |
| 12 | TmAuditId | TM_AUDIT_ID | 🔑 | ✅ |
| 13 | TmBlkId | TM_BLK_ID | — | ✅ |
| 14 | TmBlkVersion | TM_BLK_VERSION | — | — |
| 15 | TmNewBlkId | TM_NEW_BLK_ID | — | — |
| 16 | TmNewBlkVersion | TM_NEW_BLK_VERSION | — | — |
| 17 | TmRecordGrpId | TM_RECORD_GRP_ID | — | ✅ |
| 18 | UsagesType | USAGES_TYPE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
