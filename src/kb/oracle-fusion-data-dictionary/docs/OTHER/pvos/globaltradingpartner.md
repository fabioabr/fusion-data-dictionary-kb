---
id: DOC-OTHER-PVO-GlobalTradingPartner
doc_type: system-doc
title: "GlobalTradingPartner — PVO Cross-Module"
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
  - GlobalTradingPartner
  - globaltradingpartner
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GlobalTradingPartner

## 📌 Visão Geral

View Object para extração BICC de dados de Global Trading Partner. Acessa as tabelas: MSC_GLOBAL_TRADING_PARTNERS.

**Caminho:** `FscmTopModelAM.DooTopAM.GlobalTradingPartner`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 3 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[msc_global_trading_partners|MSC_GLOBAL_TRADING_PARTNERS]] — 17 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[msc_global_trading_partners|MSC_GLOBAL_TRADING_PARTNERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CompanyId | COMPANY_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | CustomerClassCode | CUSTOMER_CLASS_CODE | — | — |
| 5 | CustomerType | CUSTOMER_TYPE | — | — |
| 6 | DisableDate | DISABLE_DATE | — | — |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ModellingOrgId | MODELLING_ORG_ID | — | — |
| 11 | PartnerName | PARTNER_NAME | — | ✅ |
| 12 | PartnerNumber | PARTNER_NUMBER | — | — |
| 13 | PartnerType | PARTNER_TYPE | — | — |
| 14 | PartyId | PARTY_ID | — | — |
| 15 | RefreshNumber | REFRESH_NUMBER | — | — |
| 16 | Status | STATUS | — | — |
| 17 | TpId | TP_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
