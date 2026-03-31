---
id: DOC-HCM-160
doc_type: system-doc
title: "HRC_TXN_DATA — Dados de Transações HCM"
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
  - data
aliases:
  - HRC_TXN_DATA
  - hrc_txn_data
  - dados-de-transações-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_TXN_DATA

## 📌 Visão Geral

Armazena **dados detalhados de transações** HCM em formato EAV (Entity-Attribute-Value).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Armazenamento flexível:** Dados em formato EAV.
- **Histórico:** Valores propostos e anteriores.
- **Integração:** Dados para sistemas downstream.
- **Auditoria:** Rastreamento de alterações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TXN_DATA_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | TXN_ID | NUMBER(18) | NOT NULL | FK | Transação HCM | [[hrc_txn_header]] | 🟢 90% |
| 3 | SECTION_DISPLAY_TYPE_CODE | VARCHAR2(30) | NULL | Classificação | Tipo de seção | — | 🟡 70% |
| 4 | DATA_ROW_ID | VARCHAR2(240) | NULL | Identificação | ID da linha de dados | — | 🟡 65% |
| 5 | MODULE_IDENTIFIER | VARCHAR2(240) | NULL | Classificação | Módulo de origem | — | 🟡 70% |
| 6 | DATA_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do dado | — | 🟡 70% |
| 7 | DATA_VALUE | VARCHAR2(4000) | NULL | Dados | Valor do campo | — | 🟡 75% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrc_txn_header]] — via `TXN_ID` (cabecalho da transacao dos dados)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Dados de uma transação
```sql
SELECT d.MODULE_IDENTIFIER, d.DATA_TYPE, d.DATA_VALUE
FROM   HRC_TXN_DATA d
WHERE  d.TXN_ID = :p_txn_id;
```

---

## 🔒 Observações

- Formato EAV — cada campo é uma linha.
- `DATA_VALUE` sempre VARCHAR2; conversão pelo consumidor.
- Volume alto: múltiplas linhas por transação.

---

## 🔗 PVOs Relacionados

### [[transactionconsolep1|TransactionConsoleP1]] (AP · BICC: 5/48)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | HrcTxnDataPEOAttribute1 | — |
| ATTRIBUTE10 | HrcTxnDataPEOAttribute10 | — |
| ATTRIBUTE11 | HrcTxnDataPEOAttribute11 | — |
| ATTRIBUTE12 | HrcTxnDataPEOAttribute12 | — |
| ATTRIBUTE13 | HrcTxnDataPEOAttribute13 | — |
| ATTRIBUTE14 | HrcTxnDataPEOAttribute14 | — |
| ATTRIBUTE15 | HrcTxnDataPEOAttribute15 | — |
| ATTRIBUTE16 | HrcTxnDataPEOAttribute16 | — |
| ATTRIBUTE17 | HrcTxnDataPEOAttribute17 | — |
| ATTRIBUTE18 | HrcTxnDataPEOAttribute18 | — |
| ATTRIBUTE19 | HrcTxnDataPEOAttribute19 | — |
| ATTRIBUTE2 | HrcTxnDataPEOAttribute2 | — |
| ATTRIBUTE20 | HrcTxnDataPEOAttribute20 | — |
| ATTRIBUTE21 | HrcTxnDataPEOAttribute21 | — |
| ATTRIBUTE22 | HrcTxnDataPEOAttribute22 | — |
| ATTRIBUTE23 | HrcTxnDataPEOAttribute23 | — |
| ATTRIBUTE24 | HrcTxnDataPEOAttribute24 | — |
| ATTRIBUTE25 | HrcTxnDataPEOAttribute25 | — |
| ATTRIBUTE26 | HrcTxnDataPEOAttribute26 | — |
| ATTRIBUTE27 | HrcTxnDataPEOAttribute27 | — |
| ATTRIBUTE28 | HrcTxnDataPEOAttribute28 | — |
| ATTRIBUTE29 | HrcTxnDataPEOAttribute29 | — |
| ATTRIBUTE3 | HrcTxnDataPEOAttribute3 | — |
| ATTRIBUTE30 | HrcTxnDataPEOAttribute30 | — |
| ATTRIBUTE4 | HrcTxnDataPEOAttribute4 | — |
| ATTRIBUTE5 | HrcTxnDataPEOAttribute5 | — |
| ATTRIBUTE6 | HrcTxnDataPEOAttribute6 | — |
| ATTRIBUTE7 | HrcTxnDataPEOAttribute7 | — |
| ATTRIBUTE8 | HrcTxnDataPEOAttribute8 | — |
| ATTRIBUTE9 | HrcTxnDataPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HrcTxnDataPEOAttributeCategory | — |
| COMPLETED_DATE | HrcTxnDataPEOCompletedDate | ✅ |
| CREATED_BY | HrcTxnDataPEOCreatedBy1 | — |
| CREATION_DATE | HrcTxnDataPEOCreationDate1 | — |
| CURRENT_APPROVER | HrcTxnDataPEOCurrentApprover | — |
| ECID | HrcTxnDataPEOEcid | — |
| ENTERPRISE_ID | HrcTxnDataPEOEnterpriseId | — |
| LAST_UPDATE_DATE | HrcTxnDataPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | HrcTxnDataPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | HrcTxnDataPEOLastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | HrcTxnDataPEOObjectVersionNumber1 | — |
| STATE | HrcTxnDataPEOState | ✅ |
| STATUS | HrcTxnDataPEOStatus | ✅ |
| SUBMITTED_BY | HrcTxnDataPEOSubmittedBy | ✅ |
| SUBMITTED_DATE | HrcTxnDataPEOSubmittedDate | — |
| TASK_ID | HrcTxnDataPEOTaskId | — |
| TRANSACTION_DATA_ID | HrcTxnDataPEOTransactionDataId | — |
| TRANSACTION_ID | HrcTxnDataPEOTransactionId1 | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
