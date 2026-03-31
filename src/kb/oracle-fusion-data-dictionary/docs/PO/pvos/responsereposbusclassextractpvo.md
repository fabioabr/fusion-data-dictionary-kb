---
id: DOC-PO-PVO-ResponseReposBusClassExtractPVO
doc_type: system-doc
title: "ResponseReposBusClassExtractPVO — PVO Purchasing"
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
  - ResponseReposBusClassExtractPVO
  - responsereposbusclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResponseReposBusClassExtractPVO

## 📌 Visão Geral

Extrai classificações de negócio (porte, diversidade) do repositório de respostas de qualificação para carga BICC. Suporta análise de diversidade e categorização de fornecedores.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.ResponseReposBusClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_resp_repos_bus_class|POQ_RESP_REPOS_BUS_CLASS]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[poq_resp_repos_bus_class|POQ_RESP_REPOS_BUS_CLASS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CertificateNumber | CERTIFICATE_NUMBER | — | ✅ |
| 2 | CertifyingAgencyId | CERTIFYING_AGENCY_ID | — | ✅ |
| 3 | ClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 4 | ClassificationId | CLASSIFICATION_ID | — | ✅ |
| 5 | ConfirmedOn | CONFIRMED_ON | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | ExpirationDate | EXPIRATION_DATE | — | ✅ |
| 9 | ExtAttr1 | EXT_ATTR_1 | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | Notes | NOTES | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | OtherCertifyingAgency | OTHER_CERTIFYING_AGENCY | — | ✅ |
| 16 | PozVersionNumber | POZ_VERSION_NUMBER | — | ✅ |
| 17 | ProvidedByContactId | PROVIDED_BY_CONTACT_ID | — | ✅ |
| 18 | RespReposBusClassId | RESP_REPOS_BUS_CLASS_ID | 🔑 | ✅ |
| 19 | ResponseRepositoryId | RESPONSE_REPOSITORY_ID | — | ✅ |
| 20 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
