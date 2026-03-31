---
id: DOC-HCM-152
doc_type: system-doc
title: "FUN_SEQ_VERSIONS — (título a preencher)"
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
  - FUN_SEQ_VERSIONS
  - fun_seq_versions
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_SEQ_VERSIONS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CURRENT_VALUE | — | — | — | — | — | — |
| 2 | DB_SEQUENCE_NAME | — | — | — | — | — | — |
| 3 | END_DATE | — | — | — | — | — | — |
| 4 | HEADER_NAME | — | — | — | — | — | — |
| 5 | INITIAL_VALUE | — | — | — | — | — | — |
| 6 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 7 | SEQ_HEADER_ID | — | — | — | — | — | — |
| 8 | SEQ_VERSION_ID | — | — | — | — | — | — |
| 9 | START_DATE | — | — | — | — | — | — |
| 10 | USE_STATUS_CODE | — | — | — | — | — | — |
| 11 | VERSION_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[journalentrylinepvo|JournalEntryLinePVO]] (GL · BICC: 6/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENT_VALUE | ClActSeqVerCurrentValue | — |
| CURRENT_VALUE | CmActSeqVerCurrentValue | — |
| CURRENT_VALUE | DocSeqVerCurrentValue | — |
| DB_SEQUENCE_NAME | ClActSeqVerDbSequenceName | — |
| DB_SEQUENCE_NAME | CmActSeqVerDbSequenceName | — |
| DB_SEQUENCE_NAME | DocSeqVerDbSequenceName | — |
| END_DATE | ClActSeqVerEndDate | — |
| END_DATE | CmActSeqVerEndDate | — |
| END_DATE | DocSeqVerEndDate | — |
| HEADER_NAME | ClActSeqVerHeaderName | ✅ |
| HEADER_NAME | CmActSeqVerHeaderName | ✅ |
| HEADER_NAME | DocSeqVerHeaderName | ✅ |
| INITIAL_VALUE | ClActSeqVerInitialValue | — |
| INITIAL_VALUE | CmActSeqVerInitialValue | — |
| INITIAL_VALUE | DocSeqVerInitialValue | — |
| OBJECT_VERSION_NUMBER | CmActSeqVerObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SEQ_HEADER_ID | ClActSeqVerSeqHeaderId | — |
| SEQ_HEADER_ID | CmActSeqVerSeqHeaderId | — |
| SEQ_HEADER_ID | DocSeqVerSeqHeaderId | — |
| SEQ_VERSION_ID | ClActSeqVerSeqVersionId | — |
| SEQ_VERSION_ID | CmActSeqVerSeqVersionId | — |
| SEQ_VERSION_ID | DocSeqVerSeqVersionId | — |
| START_DATE | ClActSeqVerStartDate | — |
| START_DATE | CmActSeqVerStartDate | — |
| START_DATE | DocSeqVerStartDate | — |
| USE_STATUS_CODE | ClActSeqVerUseStatusCode | — |
| USE_STATUS_CODE | CmActSeqVerUseStatusCode | — |
| USE_STATUS_CODE | DocSeqVerUseStatusCode | — |
| VERSION_NAME | ClActSeqVerVersionName | ✅ |
| VERSION_NAME | CmActSeqVerVersionName | ✅ |
| VERSION_NAME | DocSeqVerVersionName | ✅ |

### [[journalheaderextractpvo|JournalHeaderExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| HEADER_NAME | CloseAcctSeqVersionsHeaderName | — |
| HEADER_NAME | PostAcctSeqVersionsHeaderName | — |
| SEQ_VERSION_ID | CloseAcctSeqVersionsSeqVersionId | — |
| SEQ_VERSION_ID | PostAcctSeqVersionsSeqVersionId | — |
| VERSION_NAME | CloseAcctSeqVersionsVersionName | — |
| VERSION_NAME | PostAcctSeqVersionsVersionName | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENT_VALUE | FunCloseAcctSeqVersionsCurrentValue | — |
| CURRENT_VALUE | FunPostAcctSeqVersionsCurrentValue | — |
| END_DATE | FunCloseAcctSeqVersionsEndDate | — |
| END_DATE | FunPostAcctSeqVersionsEndDate | — |
| HEADER_NAME | FunCloseAcctSeqVersionsHeaderName | ✅ |
| HEADER_NAME | FunPostAcctSeqVersionsHeaderName | ✅ |
| INITIAL_VALUE | FunCloseAcctSeqVersionsInitialValue | — |
| INITIAL_VALUE | FunPostAcctSeqVersionsInitialValue | — |
| OBJECT_VERSION_NUMBER | FunCloseAcctSeqVersionsObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FunPostAcctSeqVersionsObjectVersionNumber | — |
| SEQ_VERSION_ID | FunCloseAcctSeqVersionsId | — |
| SEQ_VERSION_ID | FunPostAcctSeqVersionsId | — |
| START_DATE | FunCloseAcctSeqVersionsStartDate | — |
| START_DATE | FunPostAcctSeqVersionsStartDate | — |
| USE_STATUS_CODE | FunCloseAcctSeqVersionsUseStatusCode | — |
| USE_STATUS_CODE | FunPostAcctSeqVersionsUseStatusCode | — |
| VERSION_NAME | FunCloseAcctSeqVersionsName | ✅ |
| VERSION_NAME | FunPostAcctSeqVersionsName | ✅ |

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENT_VALUE | FunCloseAcctSeqVersionsCurrentValue | — |
| CURRENT_VALUE | FunPostAcctSeqVersionsCurrentValue | — |
| END_DATE | FunCloseAcctSeqVersionsEndDate | — |
| END_DATE | FunPostAcctSeqVersionsEndDate | — |
| HEADER_NAME | FunCloseAcctSeqVersionsHeaderName | ✅ |
| HEADER_NAME | FunPostAcctSeqVersionsHeaderName | ✅ |
| INITIAL_VALUE | FunCloseAcctSeqVersionsInitialValue | — |
| INITIAL_VALUE | FunPostAcctSeqVersionsInitialValue | — |
| OBJECT_VERSION_NUMBER | FunCloseAcctSeqVersionsObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | FunPostAcctSeqVersionsObjectVersionNumber | — |
| SEQ_VERSION_ID | FunCloseAcctSeqVersionsId | — |
| SEQ_VERSION_ID | FunPostAcctSeqVersionsId | — |
| START_DATE | FunCloseAcctSeqVersionsStartDate | — |
| START_DATE | FunPostAcctSeqVersionsStartDate | — |
| USE_STATUS_CODE | FunCloseAcctSeqVersionsUseStatusCode | — |
| USE_STATUS_CODE | FunPostAcctSeqVersionsUseStatusCode | — |
| VERSION_NAME | FunCloseAcctSeqVersionsName | ✅ |
| VERSION_NAME | FunPostAcctSeqVersionsName | ✅ |

### [[subledgerjournaldistributionpvo|SubledgerJournalDistributionPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CURRENT_VALUE | ClActSeqVerCurrentValue | — |
| CURRENT_VALUE | CmActSeqVerCurrentValue | — |
| CURRENT_VALUE | DocSeqVerCurrentValue | — |
| DB_SEQUENCE_NAME | ClActSeqVerDbSequenceName | — |
| DB_SEQUENCE_NAME | CmActSeqVerDbSequenceName | — |
| DB_SEQUENCE_NAME | DocSeqVerDbSequenceName | — |
| END_DATE | ClActSeqVerEndDate | — |
| END_DATE | CmActSeqVerEndDate | — |
| END_DATE | DocSeqVerEndDate | — |
| HEADER_NAME | ClActSeqVerHeaderName | — |
| HEADER_NAME | CmActSeqVerHeaderName | — |
| HEADER_NAME | DocSeqVerHeaderName | — |
| INITIAL_VALUE | ClActSeqVerInitialValue | — |
| INITIAL_VALUE | CmActSeqVerInitialValue | — |
| INITIAL_VALUE | DocSeqVerInitialValue | — |
| OBJECT_VERSION_NUMBER | CmActSeqVerObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SEQ_HEADER_ID | ClActSeqVerSeqHeaderId | — |
| SEQ_HEADER_ID | CmActSeqVerSeqHeaderId | — |
| SEQ_HEADER_ID | DocSeqVerSeqHeaderId | — |
| SEQ_VERSION_ID | ClActSeqVerSeqVersionId | — |
| SEQ_VERSION_ID | CmActSeqVerSeqVersionId | — |
| SEQ_VERSION_ID | DocSeqVerSeqVersionId | — |
| START_DATE | ClActSeqVerStartDate | — |
| START_DATE | CmActSeqVerStartDate | — |
| START_DATE | DocSeqVerStartDate | — |
| USE_STATUS_CODE | ClActSeqVerUseStatusCode | — |
| USE_STATUS_CODE | CmActSeqVerUseStatusCode | — |
| USE_STATUS_CODE | DocSeqVerUseStatusCode | — |
| VERSION_NAME | ClActSeqVerVersionName | — |
| VERSION_NAME | CmActSeqVerVersionName | — |
| VERSION_NAME | DocSeqVerVersionName | — |

### [[subledgerjournalheaderextractpvo|SubledgerJournalHeaderExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| HEADER_NAME | CloseAcctSeqVersionsHeaderName | — |
| HEADER_NAME | CompAcctSeqVersionsHeaderName | — |
| SEQ_VERSION_ID | CloseAcctSeqVersionsSeqVersionId | — |
| SEQ_VERSION_ID | CompAcctSeqVersionsSeqVersionId | — |
| VERSION_NAME | CloseAcctSeqVersionsVersionName | — |
| VERSION_NAME | CompAcctSeqVersionsVersionName | — |
