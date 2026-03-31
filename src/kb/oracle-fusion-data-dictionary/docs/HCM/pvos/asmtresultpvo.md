---
id: DOC-HCM-PVO-AsmtResultPVO
doc_type: system-doc
title: "AsmtResultPVO — PVO Human Capital Management"
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
  - AsmtResultPVO
  - asmtresultpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AsmtResultPVO

## 📌 Visão Geral

Extrai resultados individuais de avaliacoes com comentarios e status. Base para analise de desempenho de candidatos em testes e assessments.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecAssessmentsAM.AsmtResultPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 3 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[irc_asmt_results|IRC_ASMT_RESULTS]] — 10 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_asmt_results|IRC_ASMT_RESULTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsmtResultPEOAssessmentConfigId | ASSESSMENT_CONFIG_ID | — | — |
| 2 | AsmtResultPEOComments | COMMENTS | — | ✅ |
| 3 | AsmtResultPEOCreatedBy | CREATED_BY | — | — |
| 4 | AsmtResultPEOCreationDate | CREATION_DATE | — | — |
| 5 | AsmtResultPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AsmtResultPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AsmtResultPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | AsmtResultPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | AsmtResultPEOSubmissionId | SUBMISSION_ID | — | — |
| 10 | ResultId | RESULT_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
