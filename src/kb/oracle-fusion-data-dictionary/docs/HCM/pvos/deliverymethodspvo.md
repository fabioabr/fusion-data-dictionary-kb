---
id: DOC-HCM-PVO-DeliveryMethodsPVO
doc_type: system-doc
title: "DeliveryMethodsPVO — PVO Human Capital Management"
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
  - DeliveryMethodsPVO
  - deliverymethodspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeliveryMethodsPVO

## 📌 Visão Geral

Extrai metodos de entrega de comunicacao por pessoa (e-mail, SMS, etc.). Suporta configuracao de canais de notificacao e preferencias de contato.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.DeliveryMethodsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 12 | 80% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_dlvry_methods|PER_PERSON_DLVRY_METHODS]] — 15 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[per_person_dlvry_methods|PER_PERSON_DLVRY_METHODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryMethodId | DELIVERY_METHOD_ID | 🔑 | ✅ |
| 2 | DeliveryMethodsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | DeliveryMethodsPEOCommDlvryAddress | COMM_DLVRY_ADDRESS | — | ✅ |
| 4 | DeliveryMethodsPEOCommDlvryFkId | COMM_DLVRY_FK_ID | — | ✅ |
| 5 | DeliveryMethodsPEOCommDlvryMethod | COMM_DLVRY_METHOD | — | ✅ |
| 6 | DeliveryMethodsPEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | DeliveryMethodsPEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | DeliveryMethodsPEODateEnd | DATE_END | — | ✅ |
| 9 | DeliveryMethodsPEODateStart | DATE_START | — | ✅ |
| 10 | DeliveryMethodsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DeliveryMethodsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | DeliveryMethodsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | DeliveryMethodsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | DeliveryMethodsPEOPersonId | PERSON_ID | — | ✅ |
| 15 | DeliveryMethodsPEOPreferredOrder | PREFERRED_ORDER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
