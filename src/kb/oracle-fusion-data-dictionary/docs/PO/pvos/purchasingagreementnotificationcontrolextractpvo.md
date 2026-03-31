---
id: DOC-PO-PVO-PurchasingAgreementNotificationControlExtractPVO
doc_type: system-doc
title: "PurchasingAgreementNotificationControlExtractPVO — PVO Purchasing"
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
  - PurchasingAgreementNotificationControlExtractPVO
  - purchasingagreementnotificationcontrolextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingAgreementNotificationControlExtractPVO

## 📌 Visão Geral

Extrai as configurações de notificação de contratos de compra para carga BICC, incluindo alertas de vencimento e limites de consumo. Suporta gestão proativa de contratos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingAgreementNotificationControlExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_notification_controls|PO_NOTIFICATION_CONTROLS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[po_notification_controls|PO_NOTIFICATION_CONTROLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | NotificationAmount | NOTIFICATION_AMOUNT | — | ✅ |
| 8 | NotificationConditionCode | NOTIFICATION_CONDITION_CODE | — | ✅ |
| 9 | NotificationId | NOTIFICATION_ID | 🔑 | ✅ |
| 10 | NotificationQtyPercentage | NOTIFICATION_QTY_PERCENTAGE | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 13 | StartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
