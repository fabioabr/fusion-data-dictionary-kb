---
id: DOC-GL-019
doc_type: system-doc
title: "GL_JE_BATCHES — Lotes de Lançamentos Contábeis"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - lotes
  - batches
  - journal-batches
aliases:
  - GL_JE_BATCHES
  - gl_je_batches
  - lotes-lancamentos-gl
  - journal-batches
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_BATCHES

## 📌 Visão Geral

Armazena os **lotes (batches) de lançamentos contábeis** do General Ledger. Cada lote agrupa um ou mais journals (cabeçalhos de lançamento) que são submetidos, aprovados e contabilizados como uma unidade. É o nível mais alto da hierarquia de lançamentos: Batch → Header → Lines.

> [!note] Hierarquia de lançamentos
> A estrutura de lançamentos no GL segue três níveis: **GL_JE_BATCHES** (lote) → **GL_JE_HEADERS** (cabeçalho/journal) → **GL_JE_LINES** (linhas/partidas). Um lote pode conter múltiplos journals.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de lançamentos:** Organização de journals em lotes para submissão e aprovação em bloco.
- **Workflow de aprovação:** Controle de status do lote (não postado, postado, em aprovação).
- **Import de subledger:** Lotes criados automaticamente pelo processo de Journal Import.
- **Posting (contabilização):** O processo de posting opera no nível do lote.
- **Reversão:** Lotes podem ser revertidos integralmente.
- **Auditoria:** Rastreamento de quem criou, aprovou e postou o lote.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_BATCH_ID | NUMBER(18) | NOT NULL | PK | Identificador único do lote de lançamento | — | 🟢 100% |
| 2 | NAME | VARCHAR2(100) | NOT NULL | Identificação | Nome do lote (único por ledger/período) | — | 🟢 100% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status do lote: U (Unposted), P (Posted), S (Selected for posting), I (In error) | — | 🟢 100% |
| 5 | STATUS_VERIFIED | VARCHAR2(1) | NULL | Controle | Flag de verificação do status | — | 🟡 70% |
| 6 | ACTUAL_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Tipo: A (Actual), B (Budget), E (Encumbrance) | — | 🟢 100% |
| 7 | DEFAULT_PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Período contábil padrão do lote | — | 🟢 100% |
| 8 | DEFAULT_EFFECTIVE_DATE | DATE | NOT NULL | Data | Data efetiva padrão (GL Date) | — | 🟢 100% |
| 9 | POSTED_DATE | DATE | NULL | Data | Data em que o lote foi contabilizado (posted) | — | 🟢 100% |
| 10 | RUNNING_TOTAL_DR | NUMBER | NULL | Financeiro | Total acumulado a débito de todas as linhas do lote | — | 🟢 95% |
| 11 | RUNNING_TOTAL_CR | NUMBER | NULL | Financeiro | Total acumulado a crédito de todas as linhas do lote | — | 🟢 95% |
| 12 | RUNNING_TOTAL_ACCOUNTED_DR | NUMBER | NULL | Financeiro | Total acumulado a débito — moeda funcional | — | 🟡 80% |
| 13 | RUNNING_TOTAL_ACCOUNTED_CR | NUMBER | NULL | Financeiro | Total acumulado a crédito — moeda funcional | — | 🟡 80% |
| 14 | CONTROL_TOTAL | NUMBER | NULL | Financeiro | Total de controle informado pelo usuário | — | 🟢 95% |
| 15 | APPROVAL_STATUS_CODE | VARCHAR2(1) | NULL | Aprovação | Status de aprovação: A (Approved), J (Rejected), R (Required), Z (Funds checked) | — | 🟢 90% |
| 16 | BUDGETARY_CONTROL_STATUS | VARCHAR2(1) | NULL | Controle | Status do controle orçamentário | — | 🟡 75% |
| 17 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do lote | — | 🟢 100% |
| 18 | AVERAGE_JOURNAL_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é um journal de média (Average Daily Balance) | — | 🟡 75% |
| 19 | POSTING_RUN_ID | NUMBER(18) | NULL | Sistema | ID da execução de posting | — | 🟡 75% |
| 20 | REQUEST_ID | NUMBER(18) | NULL | Sistema | ID do request de processamento concorrente | — | 🟢 90% |
| 21 | PARENT_JE_BATCH_ID | NUMBER(18) | NULL | Referência cruzada | ID do lote pai (em caso de reversão) | [[gl_je_batches]] | 🟢 90% |
| 22 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 80% |
| 23 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 24 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 25 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 26 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 27 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 28 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 29 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_je_batches]] — via `PARENT_JE_BATCH_ID` (lote pai em reversões — auto-referência)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit proprietária do lote de lançamentos)

### Tabelas-filha (FK de saída)
- [[gl_je_headers]] — via `JE_BATCH_ID` (cabeçalhos de lançamento do lote)
- [[gl_import_references]] — via `JE_BATCH_ID` (referências de importação)

---

## 📎 Uso Típico

### Lotes não postados de um período
```sql
SELECT b.JE_BATCH_ID, b.NAME, b.STATUS,
       b.DEFAULT_PERIOD_NAME, b.RUNNING_TOTAL_DR, b.RUNNING_TOTAL_CR
FROM   GL_JE_BATCHES b
WHERE  b.LEDGER_ID = :p_ledger_id
  AND  b.DEFAULT_PERIOD_NAME = 'MAR-26'
  AND  b.STATUS = 'U'
ORDER BY b.CREATION_DATE DESC;
```

### Lotes postados com totais
```sql
SELECT b.NAME, b.POSTED_DATE,
       b.RUNNING_TOTAL_DR, b.RUNNING_TOTAL_CR,
       (b.RUNNING_TOTAL_DR - b.RUNNING_TOTAL_CR) AS net
FROM   GL_JE_BATCHES b
WHERE  b.LEDGER_ID = :p_ledger_id
  AND  b.STATUS = 'P'
  AND  b.POSTED_DATE BETWEEN :start_date AND :end_date
ORDER BY b.POSTED_DATE;
```

### Filtros comuns
- `STATUS = 'U'` — Não postados (Unposted)
- `STATUS = 'P'` — Postados (Posted)
- `STATUS = 'I'` — Com erro (In error)
- `ACTUAL_FLAG = 'A'` — Lançamentos reais
- `APPROVAL_STATUS_CODE = 'A'` — Aprovados

---

## 🔒 Observações

- O `STATUS` controla o ciclo de vida: **U** (não postado) → **S** (selecionado para posting) → **P** (postado). **I** indica erro no posting.
- `PARENT_JE_BATCH_ID` é preenchido quando o lote é uma **reversão** de outro lote.
- `RUNNING_TOTAL_DR` e `RUNNING_TOTAL_CR` devem ser iguais (lote balanceado) antes do posting.
- O `CONTROL_TOTAL` é opcional e serve como controle manual — se informado, é comparado com o total real.
- Lotes importados de subledgers (Journal Import) têm o `NAME` gerado automaticamente pelo processo.

---

## 🔗 PVOs Relacionados

### [[journalbatchextractpvo|JournalBatchExtractPVO]] (OTHER · BICC: 33/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | JournalBatchAccountedPeriodType | ✅ |
| ACTUAL_FLAG | JournalBatchActualFlag | ✅ |
| APPROVAL_STATUS_CODE | JournalBatchApprovalStatusCode | ✅ |
| APPROVER_EMPLOYEE_ID | JournalBatchApproverEmployeeId | ✅ |
| ATTRIBUTE1 | JournalBatchAttribute1 | — |
| ATTRIBUTE10 | JournalBatchAttribute10 | — |
| ATTRIBUTE2 | JournalBatchAttribute2 | — |
| ATTRIBUTE3 | JournalBatchAttribute3 | — |
| ATTRIBUTE4 | JournalBatchAttribute4 | — |
| ATTRIBUTE5 | JournalBatchAttribute5 | — |
| ATTRIBUTE6 | JournalBatchAttribute6 | — |
| ATTRIBUTE7 | JournalBatchAttribute7 | — |
| ATTRIBUTE8 | JournalBatchAttribute8 | — |
| ATTRIBUTE9 | JournalBatchAttribute9 | — |
| ATTRIBUTE_CATEGORY | JournalBatchAttributeCategory | — |
| ATTRIBUTE_DATE1 | JournalBatchAttributeDate1 | — |
| ATTRIBUTE_DATE2 | JournalBatchAttributeDate2 | — |
| ATTRIBUTE_DATE3 | JournalBatchAttributeDate3 | — |
| ATTRIBUTE_DATE4 | JournalBatchAttributeDate4 | — |
| ATTRIBUTE_DATE5 | JournalBatchAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | JournalBatchAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | JournalBatchAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | JournalBatchAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | JournalBatchAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | JournalBatchAttributeNumber5 | — |
| AVERAGE_JOURNAL_FLAG | JournalBatchAverageJournalFlag | ✅ |
| CHART_OF_ACCOUNTS_ID | JournalBatchChartOfAccountsId | ✅ |
| CONTROL_TOTAL | JournalBatchControlTotal | ✅ |
| CREATED_BY | JournalBatchCreatedBy | ✅ |
| CREATION_DATE | JournalBatchCreationDate | ✅ |
| DATE_CREATED | JournalBatchDateCreated | ✅ |
| DEFAULT_EFFECTIVE_DATE | JournalBatchDefaultEffectiveDate | ✅ |
| DEFAULT_PERIOD_NAME | JournalBatchDefaultPeriodName | ✅ |
| DESCRIPTION | JournalBatchDescription | ✅ |
| ERROR_MESSAGE | JournalBatchErrorMessage | ✅ |
| FUNDS_STATUS_CODE | JournalBatchFundsStatusCode | ✅ |
| GROUP_ID | JournalBatchGroupId | ✅ |
| JE_BATCH_ID | JournalBatchJeBatchId | ✅ |
| JE_SOURCE | JournalBatchJeSource | ✅ |
| LAST_UPDATE_DATE | JournalBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JournalBatchLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JournalBatchLastUpdatedBy | ✅ |
| NAME | JournalBatchName | ✅ |
| OBJECT_VERSION_NUMBER | JournalBatchObjectVersionNumber | ✅ |
| PARENT_JE_BATCH_ID | JournalBatchParentJeBatchId | ✅ |
| PERIOD_SET_NAME | JournalBatchPeriodSetName | ✅ |
| POSTED_DATE | JournalBatchPostedDate | ✅ |
| POSTING_RUN_ID | JournalBatchPostingRunId | ✅ |
| REQUEST_ID | JournalBatchRequestId | ✅ |
| RUNNING_TOTAL_ACCOUNTED_CR | JournalBatchRunningTotalAccountedCr | ✅ |
| RUNNING_TOTAL_ACCOUNTED_DR | JournalBatchRunningTotalAccountedDr | ✅ |
| RUNNING_TOTAL_CR | JournalBatchRunningTotalCr | ✅ |
| RUNNING_TOTAL_DR | JournalBatchRunningTotalDr | ✅ |
| STATUS | JournalBatchStatus | ✅ |

### [[journalbatchpvo|JournalBatchPVO]] (GL · BICC: 19/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | JournalBatchAccountedPeriodType | ✅ |
| ACTUAL_FLAG | JournalBatchActualFlag | ✅ |
| APPROVAL_STATUS_CODE | JournalBatchApprovalStatusCode | ✅ |
| APPROVER_EMPLOYEE_ID | JournalBatchApproverEmployeeId | — |
| AVERAGE_JOURNAL_FLAG | JournalBatchAverageJournalFlag | — |
| BUDGETARY_CONTROL_STATUS | JournalBatchBudgetaryControlStatus | — |
| CHART_OF_ACCOUNTS_ID | JournalBatchChartOfAccountsId | ✅ |
| CONTROL_TOTAL | JournalBatchControlTotal | ✅ |
| CREATED_BY | JournalBatchCreatedBy | ✅ |
| CREATION_DATE | JournalBatchCreationDate | ✅ |
| DATE_CREATED | JournalBatchDateCreated | — |
| DEFAULT_EFFECTIVE_DATE | JournalBatchDefaultEffectiveDate | ✅ |
| DEFAULT_PERIOD_NAME | JournalBatchDefaultPeriodName | — |
| DESCRIPTION | JournalBatchDescription | ✅ |
| EARLIEST_POSTABLE_DATE | JournalBatchEarliestPostableDate | — |
| GROUP_ID | JournalBatchGroupId | ✅ |
| JE_BATCH_ID | JeBatchId | ✅ |
| JE_SOURCE | JournalBatchJeSource | — |
| LAST_UPDATE_DATE | JournalBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JournalBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | JournalBatchLastUpdatedBy | ✅ |
| NAME | JournalBatchName | ✅ |
| OBJECT_VERSION_NUMBER | JournalBatchObjectVersionNumber | — |
| PACKET_ID | JournalBatchPacketId | — |
| PARENT_JE_BATCH_ID | JournalBatchParentJeBatchId | — |
| PERIOD_SET_NAME | JournalBatchPeriodSetName | — |
| POSTED_DATE | JournalBatchPostedDate | ✅ |
| POSTED_DATE | JournalBatchPostedDateTime | — |
| POSTING_RUN_ID | JournalBatchPostingRunId | — |
| REQUEST_ID | JournalBatchRequestId | — |
| RUNNING_TOTAL_ACCOUNTED_CR | JournalBatchRunningTotalAccountedCr | ✅ |
| RUNNING_TOTAL_ACCOUNTED_DR | JournalBatchRunningTotalAccountedDr | ✅ |
| RUNNING_TOTAL_CR | JournalBatchRunningTotalCr | ✅ |
| RUNNING_TOTAL_DR | JournalBatchRunningTotalDr | ✅ |
| STATUS | JournalBatchStatus | — |
| STATUS_VERIFIED | JournalBatchStatusVerified | — |
| UNRESERVATION_PACKET_ID | JournalBatchUnreservationPacketId | — |

### [[journalheaderextractpvo|JournalHeaderExtractPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | GlJeBatchesAccountedPeriodType | — |
| ACTUAL_FLAG | GlJeBatchesActualFlag | — |
| APPROVAL_STATUS_CODE | GlJeBatchesApprovalStatusCode | — |
| APPROVER_EMPLOYEE_ID | GlJeBatchesApproverEmployeeId | — |
| ATTRIBUTE1 | GlJeBatchesAttribute11 | — |
| ATTRIBUTE10 | GlJeBatchesAttribute101 | — |
| ATTRIBUTE2 | GlJeBatchesAttribute21 | — |
| ATTRIBUTE3 | GlJeBatchesAttribute31 | — |
| ATTRIBUTE4 | GlJeBatchesAttribute41 | — |
| ATTRIBUTE5 | GlJeBatchesAttribute51 | — |
| ATTRIBUTE6 | GlJeBatchesAttribute61 | — |
| ATTRIBUTE7 | GlJeBatchesAttribute71 | — |
| ATTRIBUTE8 | GlJeBatchesAttribute81 | — |
| ATTRIBUTE9 | GlJeBatchesAttribute91 | — |
| ATTRIBUTE_CATEGORY | GlJeBatchesAttributeCategory1 | — |
| ATTRIBUTE_CATEGORY2 | GlJeBatchesAttributeCategory21 | — |
| AVERAGE_JOURNAL_FLAG | GlJeBatchesAverageJournalFlag | — |
| BUDGETARY_CONTROL_STATUS | GlJeBatchesBudgetaryControlStatus | — |
| CHART_OF_ACCOUNTS_ID | GlJeBatchesChartOfAccountsId | — |
| CONTROL_TOTAL | GlJeBatchesControlTotal | — |
| CREATED_BY | GlJeBatchesCreatedBy | — |
| CREATION_DATE | GlJeBatchesCreationDate | — |
| DATE_CREATED | GlJeBatchesDateCreated | — |
| DEFAULT_EFFECTIVE_DATE | GlJeBatchesDefaultEffectiveDate | — |
| DEFAULT_PERIOD_NAME | GlJeBatchesDefaultPeriodName | — |
| DESCRIPTION | GlJeBatchesDescription | — |
| EARLIEST_POSTABLE_DATE | GlJeBatchesEarliestPostableDate | — |
| ERROR_MESSAGE | GlJeBatchesErrorMessage | — |
| FUNDS_STATUS_CODE | GlJeBatchesFundsStatusCode | — |
| GROUP_ID | GlJeBatchesGroupId | — |
| JE_BATCH_ID | GlJeBatchesJeBatchId | — |
| JE_SOURCE | GlJeBatchesJeSource | — |
| LAST_UPDATE_DATE | GlJeBatchesLastUpdateDate | — |
| LAST_UPDATE_LOGIN | GlJeBatchesLastUpdateLogin | — |
| LAST_UPDATED_BY | GlJeBatchesLastUpdatedBy | — |
| NAME | GlJeBatchesName | — |
| OBJECT_VERSION_NUMBER | GlJeBatchesObjectVersionNumber | — |
| PACKET_ID | GlJeBatchesPacketId | — |
| PARENT_JE_BATCH_ID | GlJeBatchesParentJeBatchId | — |
| PERIOD_SET_NAME | GlJeBatchesPeriodSetName | — |
| POSTED_DATE | GlJeBatchesPostedDate | — |
| POSTED_DATE | GlJeBatchesPostedDateTime | — |
| POSTING_RUN_ID | GlJeBatchesPostingRunId | — |
| REQUEST_ID | GlJeBatchesRequestId | — |
| RUNNING_TOTAL_ACCOUNTED_CR | GlJeBatchesRunningTotalAccountedCr | — |
| RUNNING_TOTAL_ACCOUNTED_DR | GlJeBatchesRunningTotalAccountedDr | — |
| RUNNING_TOTAL_CR | GlJeBatchesRunningTotalCr | — |
| RUNNING_TOTAL_DR | GlJeBatchesRunningTotalDr | — |
| STATUS | GlJeBatchesStatus | — |
| STATUS_VERIFIED | GlJeBatchesStatusVerified | — |
| UNRESERVATION_PACKET_ID | GlJeBatchesUnreservationPacketId | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL · BICC: 17/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | JrnlBatchAccountedPeriodType | ✅ |
| ACTUAL_FLAG | JrnlBatchActualFlag | ✅ |
| APPROVAL_STATUS_CODE | JrnlBatchApprovalStatusCode | ✅ |
| APPROVER_EMPLOYEE_ID | JrnlBatchApproverEmployeeId | — |
| AVERAGE_JOURNAL_FLAG | JrnlBatchAverageJournalFlag | — |
| BUDGETARY_CONTROL_STATUS | JrnlBatchBudgetaryControlStatus | — |
| CHART_OF_ACCOUNTS_ID | JrnlBatchChartOfAccountsId | ✅ |
| CONTROL_TOTAL | JrnlBatchControlTotal | ✅ |
| CREATED_BY | JrnlBatchCreatedBy | ✅ |
| CREATION_DATE | JrnlBatchCreationDate | ✅ |
| DATE_CREATED | JrnlBatchDateCreated | — |
| DEFAULT_EFFECTIVE_DATE | JrnlBatchDefaultEffectiveDate | ✅ |
| DEFAULT_PERIOD_NAME | JrnlBatchDefaultPeriodName | — |
| DESCRIPTION | JrnlBatchDescription | ✅ |
| EARLIEST_POSTABLE_DATE | JrnlBatchEarliestPostableDate | — |
| GROUP_ID | JrnlBatchGroupId | ✅ |
| JE_BATCH_ID | JrnlBatchJeBatchId | ✅ |
| JE_SOURCE | JrnlBatchJeSource | — |
| LAST_UPDATE_DATE | JrnlBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlBatchLastUpdatedBy | ✅ |
| NAME | JrnlBatchName | ✅ |
| OBJECT_VERSION_NUMBER | JrnlBatchObjectVersionNumber | — |
| PACKET_ID | JrnlBatchPacketId | — |
| PARENT_JE_BATCH_ID | JrnlBatchParentJeBatchId | — |
| PERIOD_SET_NAME | JrnlBatchPeriodSetName | — |
| POSTED_DATE | JrnlBatchPostedDate | ✅ |
| POSTED_DATE | JrnlBatchPostedDateTime | — |
| POSTING_RUN_ID | JrnlBatchPostingRunId | — |
| REQUEST_ID | JrnlBatchRequestId | — |
| RUNNING_TOTAL_ACCOUNTED_CR | JrnlBatchRunningTotalAccountedCr | — |
| RUNNING_TOTAL_ACCOUNTED_DR | JrnlBatchRunningTotalAccountedDr | — |
| RUNNING_TOTAL_CR | JrnlBatchRunningTotalCr | ✅ |
| RUNNING_TOTAL_DR | JrnlBatchRunningTotalDr | ✅ |
| STATUS | JrnlBatchStatus | — |
| STATUS_VERIFIED | JrnlBatchStatusVerified | — |
| UNRESERVATION_PACKET_ID | JrnlBatchUnreservationPacketId | — |

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 20/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTED_PERIOD_TYPE | JrnlBatchAccountedPeriodType | ✅ |
| ACTUAL_FLAG | JrnlBatchActualFlag | ✅ |
| APPROVAL_STATUS_CODE | JrnlBatchApprovalStatusCode | ✅ |
| APPROVER_EMPLOYEE_ID | JrnlBatchApproverEmployeeId | — |
| AVERAGE_JOURNAL_FLAG | JrnlBatchAverageJournalFlag | — |
| BUDGETARY_CONTROL_STATUS | JrnlBatchBudgetaryControlStatus | — |
| CHART_OF_ACCOUNTS_ID | JrnlBatchChartOfAccountsId | ✅ |
| CONTROL_TOTAL | JrnlBatchControlTotal | ✅ |
| CREATED_BY | JrnlBatchCreatedBy | ✅ |
| CREATION_DATE | JrnlBatchCreationDate | ✅ |
| DATE_CREATED | JrnlBatchDateCreated | — |
| DEFAULT_EFFECTIVE_DATE | JrnlBatchDefaultEffectiveDate | ✅ |
| DEFAULT_PERIOD_NAME | JrnlBatchDefaultPeriodName | — |
| DESCRIPTION | JrnlBatchDescription | ✅ |
| EARLIEST_POSTABLE_DATE | JrnlBatchEarliestPostableDate | — |
| GROUP_ID | JrnlBatchGroupId | ✅ |
| JE_BATCH_ID | JrnlBatchJeBatchId | ✅ |
| JE_SOURCE | JrnlBatchJeSource | — |
| LAST_UPDATE_DATE | JrnlBatchLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlBatchLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlBatchLastUpdatedBy | ✅ |
| NAME | JrnlBatchName | ✅ |
| OBJECT_VERSION_NUMBER | JrnlBatchObjectVersionNumber | — |
| PACKET_ID | JrnlBatchPacketId | — |
| PARENT_JE_BATCH_ID | JrnlBatchParentJeBatchId | — |
| PERIOD_SET_NAME | JrnlBatchPeriodSetName | ✅ |
| POSTED_DATE | JrnlBatchPostedDate | ✅ |
| POSTED_DATE | JrnlBatchPostedDateTime | — |
| POSTING_RUN_ID | JrnlBatchPostingRunId | — |
| REQUEST_ID | JrnlBatchRequestId | — |
| RUNNING_TOTAL_ACCOUNTED_CR | JrnlBatchRunningTotalAccountedCr | ✅ |
| RUNNING_TOTAL_ACCOUNTED_DR | JrnlBatchRunningTotalAccountedDr | ✅ |
| RUNNING_TOTAL_CR | JrnlBatchRunningTotalCr | ✅ |
| RUNNING_TOTAL_DR | JrnlBatchRunningTotalDr | ✅ |
| STATUS | JrnlBatchStatus | — |
| STATUS_VERIFIED | JrnlBatchStatusVerified | — |
| UNRESERVATION_PACKET_ID | JrnlBatchUnreservationPacketId | — |

---

## 📚 Referências

- [Oracle Docs — GL_JE_BATCHES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljebatches-25714.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
