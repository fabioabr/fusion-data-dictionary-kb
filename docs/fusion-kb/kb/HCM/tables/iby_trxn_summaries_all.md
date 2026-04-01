---
id: DOC-HCM-523
doc_type: system-doc
title: "IBY_TRXN_SUMMARIES_ALL — (título a preencher)"
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
  - IBY_TRXN_SUMMARIES_ALL
  - iby_trxn_summaries_all
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_TRXN_SUMMARIES_ALL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATUS | — | — | — | — | — | — |
| 2 | TRXNMID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS | IbyTrxnSummaryStatus | ✅ |
| TRXNMID | IbyTrxnSummaryTrxnmid | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS | IbyTrxnSummaryStatus | ✅ |
| TRXNMID | IbyTrxnSummaryTrxnmid | — |
