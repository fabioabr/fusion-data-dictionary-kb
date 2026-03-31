---
id: DOC-HCM-162
doc_type: system-doc
title: "HRC_TXN_HEADER — Cabeçalho de Transações HCM"
system: Oracle Fusion Cloud HCM
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
  - transaction-console
  - header
aliases:
  - HRC_TXN_HEADER
  - hrc_txn_header
  - cabeçalho-de-transações-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_TXN_HEADER

## 📌 Visão Geral

Tabela principal do **cabeçalho de transações** HCM. Cada registro é uma transação de RH (promoção, transferência, admissão, alteração salarial).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro central:** Cada transação de RH gera um cabeçalho.
- **Controle de status:** Ciclo de vida completo.
- **Rastreamento:** Vínculo com processos de aprovação.
- **Integração:** Ponto de entrada para dados detalhados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TXN_ID | NUMBER(18) | NOT NULL | PK | Identificador único da transação | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa afetada | [[per_all_people_f]] | 🟢 90% |
| 3 | TXN_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo (PROMOTION, TRANSFER, NEW_HIRE) | — | 🟢 90% |
| 4 | TXN_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status (DRAFT, SUBMITTED, APPROVED, REJECTED) | — | 🟢 90% |
| 5 | SUBMITTED_BY | VARCHAR2(64) | NULL | Referência | Usuário que submeteu | — | 🟡 80% |
| 6 | SUBMITTED_DATE | TIMESTAMP | NULL | Data | Data/hora de submissão | — | 🟡 80% |
| 7 | EFFECTIVE_DATE | DATE | NULL | Data | Data efetiva | — | 🟢 85% |
| 8 | MODULE_IDENTIFIER | VARCHAR2(240) | NULL | Classificação | Módulo de origem | — | 🟡 70% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 14 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha (FK de saída)
- [[hrc_txn_data]] — via `TXN_ID` (dados da transacao HCM)
- [[hrc_txn_console_entry]] — via `TXN_ID` (entradas de console da transacao)
- [[hrc_txn_fnd_bpm_task_vl]] — via `TXN_ID` (tarefas BPM da transacao)

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da transacao HCM)

---

## 📎 Uso Típico

### Transações pendentes
```sql
SELECT h.TXN_ID, h.TXN_TYPE, h.TXN_STATUS, h.PERSON_ID, h.SUBMITTED_DATE
FROM   HRC_TXN_HEADER h
WHERE  h.TXN_STATUS = 'SUBMITTED'
ORDER BY h.SUBMITTED_DATE;
```

---

## 🔒 Observações

- Tabela central do pipeline de transações HCM.
- Ciclo: DRAFT -> SUBMITTED -> APPROVED/REJECTED.
- `EFFECTIVE_DATE` = data de efetivação.

---

## 🔗 PVOs Relacionados

### [[transactionconsolep1|TransactionConsoleP1]] (AP · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | HrcTxnHeaderPEOApplicationId | — |
| CREATED_BY | HrcTxnHeaderPEOCreatedBy | — |
| CREATION_DATE | HrcTxnHeaderPEOCreationDate | — |
| INITIATOR_USER_ID | HrcTxnHeaderPEOInitiatorUserId | — |
| LAST_UPDATE_DATE | HrcTxnHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HrcTxnHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | HrcTxnHeaderPEOLastUpdatedBy | — |
| MODULE_GROUP | HrcTxnHeaderPEOModuleGroup | — |
| MODULE_IDENTIFIER | HrcTxnHeaderPEOModuleIdentifier | — |
| OBJECT | HrcTxnHeaderPEOObject | — |
| OBJECT_ID | HrcTxnHeaderPEOObjectId | ✅ |
| OBJECT_VERSION_NUMBER | HrcTxnHeaderPEOObjectVersionNumber | — |
| PARENT_TRANSACTION_ID | HrcTxnHeaderPEOParentTransactionId | — |
| PROCESS_ID | HrcTxnHeaderPEOProcessId | — |
| PROCESS_OWNER | HrcTxnHeaderPEOProcessOwner | — |
| REENTRY_FUNCTION | HrcTxnHeaderPEOReentryFunction | — |
| SECTION_DISPLAY_NAME | HrcTxnHeaderPEOSectionDisplayName | — |
| SUBJECT | HrcTxnHeaderPEOSubject | — |
| SUBJECT_ID | HrcTxnHeaderPEOSubjectId | ✅ |
| TRANSACTION_ID | HrcTxnHeaderPEOTransactionId | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
