---
id: DOC-HCM-655
doc_type: system-doc
title: "OKC_K_HEADERS_VL — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - OKC_K_HEADERS_VL
  - okc_k_headers_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# OKC_K_HEADERS_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COGNOMEN | — | — | — | — | — | — |
| 2 | CONTRACT_NUMBER | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | ID | — | — | — | — | — | — |
| 5 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 6 | LEGAL_ENTITY_ID | — | — | — | — | — | — |
| 7 | MAJOR_VERSION | — | — | — | — | — | — |
| 8 | OWNING_ORG_ID | — | — | — | — | — | — |
| 9 | STS_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[billingeventpvo|BillingEventPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTRACT_NUMBER | ContractHeaderPEOContractNumber | — |
| ID | ContractHeaderPEOId | — |
| MAJOR_VERSION | ContractHeaderPEOMajorVersion | — |
| OWNING_ORG_ID | ContractHeaderPEOOwningOrgId | — |
| STS_CODE | ContractHeaderPEOStsCode | — |

### [[invoicedistributionpvo|InvoiceDistributionPVO]] (AP · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTRACT_NUMBER | ContractHeaderPEOContractNumber | ✅ |
| DESCRIPTION | ContractHeaderPEODescription | ✅ |
| ID | ContractHeaderPEOId | ✅ |
| LEGAL_ENTITY_ID | ContractHeaderPEOLegalEntityId | — |
| MAJOR_VERSION | ContractHeaderPEOMajorVersion | ✅ |
| OWNING_ORG_ID | ContractHeaderPEOOwningOrgId | — |

### [[revenuedistributionpvo|RevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONTRACT_NUMBER | ContractHeaderPEOContractNumber | — |
| DESCRIPTION | ContractHeaderPEODescription | — |
| ID | ContractHeaderPEOId | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| MAJOR_VERSION | ContractHeaderPEOMajorVersion | — |
| OWNING_ORG_ID | ContractHeaderPEOOwningOrgId | — |
