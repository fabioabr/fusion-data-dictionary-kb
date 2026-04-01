---
id: DOC-PO-PVO-ProcurementBuyersExtractPVO
doc_type: system-doc
title: "ProcurementBuyersExtractPVO — PVO Purchasing"
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
  - ProcurementBuyersExtractPVO
  - procurementbuyersextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcurementBuyersExtractPVO

## 📌 Visão Geral

Extrai dados de compradores e suas atribuições para carga BICC, incluindo unidades de negócio, categorias de item e documentos acessíveis. Alimenta análises de distribuição de workload e cobertura.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.ProcurementBuyersExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 1 | 1 | 12 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]] — 63 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[po_agent_assignments|PO_AGENT_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | AgentId | AGENT_ID | — | ✅ |
| 3 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 4 | Attribute1 | ATTRIBUTE1 | — | — |
| 5 | Attribute10 | ATTRIBUTE10 | — | — |
| 6 | Attribute11 | ATTRIBUTE11 | — | — |
| 7 | Attribute12 | ATTRIBUTE12 | — | — |
| 8 | Attribute13 | ATTRIBUTE13 | — | — |
| 9 | Attribute14 | ATTRIBUTE14 | — | — |
| 10 | Attribute15 | ATTRIBUTE15 | — | — |
| 11 | Attribute16 | ATTRIBUTE16 | — | — |
| 12 | Attribute17 | ATTRIBUTE17 | — | — |
| 13 | Attribute18 | ATTRIBUTE18 | — | — |
| 14 | Attribute19 | ATTRIBUTE19 | — | — |
| 15 | Attribute2 | ATTRIBUTE2 | — | — |
| 16 | Attribute20 | ATTRIBUTE20 | — | — |
| 17 | Attribute3 | ATTRIBUTE3 | — | — |
| 18 | Attribute4 | ATTRIBUTE4 | — | — |
| 19 | Attribute5 | ATTRIBUTE5 | — | — |
| 20 | Attribute6 | ATTRIBUTE6 | — | — |
| 21 | Attribute7 | ATTRIBUTE7 | — | — |
| 22 | Attribute8 | ATTRIBUTE8 | — | — |
| 23 | Attribute9 | ATTRIBUTE9 | — | — |
| 24 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 25 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 26 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 27 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 28 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 29 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 30 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 31 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 32 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 33 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 34 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 35 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 36 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 37 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 38 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 39 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 40 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 41 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 42 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 43 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 44 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 45 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 46 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 47 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 48 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 49 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 50 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 51 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 52 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 53 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 54 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 55 | CreatedBy | CREATED_BY | — | ✅ |
| 56 | CreationDate | CREATION_DATE | — | ✅ |
| 57 | DefaultPrinterName | DEFAULT_PRINTER_NAME | — | ✅ |
| 58 | DefaultReqBuId | DEFAULT_REQ_BU_ID | — | ✅ |
| 59 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 61 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 62 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 63 | PrcBuId | PRC_BU_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
