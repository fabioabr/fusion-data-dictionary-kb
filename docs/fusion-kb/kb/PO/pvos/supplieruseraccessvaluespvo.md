---
id: DOC-PO-PVO-SupplierUserAccessValuesPVO
doc_type: system-doc
title: "SupplierUserAccessValuesPVO — PVO Purchasing"
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
  - SupplierUserAccessValuesPVO
  - supplieruseraccessvaluespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierUserAccessValuesPVO

## 📌 Visão Geral

Extrai os valores de acesso configurados para usuários de fornecedores no portal, incluindo entidades e funções acessíveis. Suporta auditoria de segurança e gestão de acessos.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierUserAccessValuesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 3 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pos_user_access_values|POS_USER_ACCESS_VALUES]] — 9 atributos (3 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pos_user_access_values|POS_USER_ACCESS_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessCode | ACCESS_CODE | 🔑 | ✅ |
| 2 | AccessValue | ACCESS_VALUE | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PerPartyId | PER_PARTY_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
