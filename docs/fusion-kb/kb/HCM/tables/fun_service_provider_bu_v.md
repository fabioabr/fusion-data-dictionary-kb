---
id: DOC-HCM-153
doc_type: system-doc
title: "FUN_SERVICE_PROVIDER_BU_V — (título a preencher)"
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
  - FUN_SERVICE_PROVIDER_BU_V
  - fun_service_provider_bu_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_SERVICE_PROVIDER_BU_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLIENT_BU_ID | — | — | — | — | — | — |
| 2 | DOWNSTREAM_FUNCTION_ID | — | — | — | — | — | — |
| 3 | SERVICE_PROVIDER_BU_ID | — | — | — | — | — | — |
| 4 | UPSTREAM_FUNCTION_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[purchasingaslextractpvo|PurchasingASLExtractPVO]] (PO · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLIENT_BU_ID | ClientBusinessUnitId | ✅ |
| DOWNSTREAM_FUNCTION_ID | DownstreamFunctionId | ✅ |
| SERVICE_PROVIDER_BU_ID | ServiceProviderBusinessUnitId | ✅ |
| UPSTREAM_FUNCTION_ID | UpstreamFunctionId | ✅ |

### [[purchasingaslpvo|PurchasingASLPVO]] (PO · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLIENT_BU_ID | ClientBusinessUnitId | ✅ |
| DOWNSTREAM_FUNCTION_ID | DownstreamFunctionId | — |
| SERVICE_PROVIDER_BU_ID | ServiceProviderBusinessUnitId | ✅ |
| UPSTREAM_FUNCTION_ID | UpstreamFunctionId | — |
