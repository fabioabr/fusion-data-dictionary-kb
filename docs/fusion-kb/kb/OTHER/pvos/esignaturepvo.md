---
id: DOC-OTHER-PVO-ESignaturePVO
doc_type: system-doc
title: "ESignaturePVO — PVO Cross-Module"
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
  - ESignaturePVO
  - esignaturepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ESignaturePVO

## 📌 Visão Geral

View Object para extração BICC de dados de ESignature. Acessa as tabelas: IRC_ESIGNATURES, IRC_JA_SECONDARY_FLOWS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.ESignaturePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 15 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[irc_esignatures|IRC_ESIGNATURES]] — 16 atributos (1 PKs, 14 BICC)
- [[irc_ja_secondary_flows|IRC_JA_SECONDARY_FLOWS]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[irc_esignatures|IRC_ESIGNATURES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | ESignaturePEODiscriminantObjectId | DISCRIMINANT_OBJECT_ID | — | — |
| 4 | ESignaturePEODiscriminantObjectType | DISCRIMINANT_OBJECT_TYPE | — | — |
| 5 | EsignatureId | ESIGNATURE_ID | 🔑 | ✅ |
| 6 | FullName | FULL_NAME | — | ✅ |
| 7 | IpAddress | IP_ADDRESS | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectId | OBJECT_ID | — | ✅ |
| 12 | ObjectType | OBJECT_TYPE | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PersonId | PERSON_ID | — | ✅ |
| 15 | SignatureDate | SIGNATURE_DATE | — | ✅ |
| 16 | ValueHash | VALUE_HASH | — | ✅ |

### [[irc_ja_secondary_flows|IRC_JA_SECONDARY_FLOWS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JASecondaryFlowsPEOAfVersionId | AF_VERSION_ID | — | ✅ |
| 2 | JASecondaryFlowsPEOSecondaryFlowId | SECONDARY_FLOW_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
