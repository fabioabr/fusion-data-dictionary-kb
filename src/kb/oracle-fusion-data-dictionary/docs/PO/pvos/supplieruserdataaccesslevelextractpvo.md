---
id: DOC-PO-PVO-SupplierUserDataAccessLevelExtractPVO
doc_type: system-doc
title: "SupplierUserDataAccessLevelExtractPVO — PVO Purchasing"
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
  - SupplierUserDataAccessLevelExtractPVO
  - supplieruserdataaccesslevelextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierUserDataAccessLevelExtractPVO

## 📌 Visão Geral

Extrai os níveis de acesso a dados dos contatos de fornecedores, definindo quais informações cada usuário pode visualizar. Essencial para segurança de dados e segregação de acessos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierUserDataAccessLevelExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_contact_attributes|POZ_CONTACT_ATTRIBUTES]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[poz_contact_attributes|POZ_CONTACT_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessLevel | ACCESS_LEVEL | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PerPartyId | PER_PARTY_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
