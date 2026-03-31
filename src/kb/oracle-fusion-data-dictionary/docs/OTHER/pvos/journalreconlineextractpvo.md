---
id: DOC-OTHER-PVO-JournalReconLineExtractPVO
doc_type: system-doc
title: "JournalReconLineExtractPVO — PVO Cross-Module"
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
  - JournalReconLineExtractPVO
  - journalreconlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalReconLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Recon Line Extract. Acessa as tabelas: GL_JE_LINES_RECON.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalReconLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_lines_recon|GL_JE_LINES_RECON]] — 14 atributos (2 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[gl_je_lines_recon|GL_JE_LINES_RECON]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlJeLinesReconCreatedBy | CREATED_BY | — | ✅ |
| 2 | GlJeLinesReconCreationDate | CREATION_DATE | — | ✅ |
| 3 | GlJeLinesReconJeHeaderId | JE_HEADER_ID | 🔑 | ✅ |
| 4 | GlJeLinesReconJeLineNum | JE_LINE_NUM | 🔑 | ✅ |
| 5 | GlJeLinesReconJgzzReconDate | JGZZ_RECON_DATE | — | ✅ |
| 6 | GlJeLinesReconJgzzReconId | JGZZ_RECON_ID | — | ✅ |
| 7 | GlJeLinesReconJgzzReconRef | JGZZ_RECON_REF | — | ✅ |
| 8 | GlJeLinesReconJgzzReconStatus | JGZZ_RECON_STATUS | — | ✅ |
| 9 | GlJeLinesReconLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | GlJeLinesReconLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | GlJeLinesReconLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | GlJeLinesReconLedgerId | LEDGER_ID | — | ✅ |
| 13 | GlJeLinesReconObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | GlJeLinesReconReconRuleId | RECON_RULE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
