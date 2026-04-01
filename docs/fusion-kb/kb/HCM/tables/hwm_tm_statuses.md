---
id: DOC-HCM-406
doc_type: system-doc
title: "HWM_TM_STATUSES — Status de Time Management"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-management
  - status
  - ciclo-vida
aliases:
  - HWM_TM_STATUSES
  - hwm_tm_statuses
  - hwm-tm-statuses
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_STATUSES

## 📌 Visao Geral

Armazena os **status possiveis** para entradas e registros do modulo Time Management. Define o ciclo de vida dos registros de tempo.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Ciclo de vida:** define os status possiveis para registros de tempo.
- **Workflow:** controla as transicoes validas entre status.
- **Validacao:** garante que apenas status validos sejam atribuidos.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATUS_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do status | — | 🟡 70% |
| 2 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do status | — | 🟡 70% |
| 3 | STATUS_NAME | VARCHAR2(240) | NULL | Identificacao | Nome do status | — | 🟡 65% |
| 4 | STATUS_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de status | — | 🟡 60% |
| 5 | SEQUENCE_NUMBER | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 55% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[hwm_tm_status_def_b]] — via `STATUS_ID` (definicoes de status)

---

## 📎 Uso Tipico

### Listar status ativos
```sql
SELECT s.STATUS_CODE, s.STATUS_NAME, s.STATUS_TYPE
FROM   HWM_TM_STATUSES s
WHERE  s.ENABLED_FLAG = 'Y'
ORDER BY s.SEQUENCE_NUMBER;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Status ativos`
- `STATUS_TYPE = :p_type — Por tipo`

---

## 🔒 Observacoes

- Define o vocabulario de status para time management.
- Status tipicos: DRAFT, SUBMITTED, APPROVED, REJECTED, PROCESSED.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_STATUSES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmstatuses.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TeRdyXfrPjcTimeStatusPEOStatusId | — |
| STATUS_ID | TeRdyXfrPyrTimeStatusPEOStatusId | — |
| STATUS_ID | TeXfrPjcTimeStatusPEOStatusId | — |
| STATUS_ID | TeXfrPyrTimeStatusPEOStatusId | — |
| STATUS_VALUE | TeRdyXfrPjcTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeRdyXfrPyrTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeXfrPjcTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeXfrPyrTimeStatusPEOStatusValue | — |

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATE_FROM | TcUiTimeStatusPEODateFrom | — |
| DATE_FROM | TcUserTimeStatusPEODateFrom | — |
| STATUS_ID | TcUiTimeStatusPEOStatusId | — |
| STATUS_ID | TcUserTimeStatusPEOStatusId | — |
| STATUS_ID | TeAppPjcTimeStatusPEOStatusId | — |
| STATUS_ID | TeAppPyrTimeStatusPEOStatusId | — |
| STATUS_ID | TeCmpTimeStatusPEOStatusId | — |
| STATUS_ID | TeErrTimeStatusPEOStatusId | — |
| STATUS_VALUE | TcUiTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TcUserTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeAppPjcTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeAppPyrTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeCmpTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeErrTimeStatusPEOStatusValue | — |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TeRdyXfrPjcTimeStatusPEOStatusId | — |
| STATUS_ID | TeRdyXfrPyrTimeStatusPEOStatusId | — |
| STATUS_ID | TeXfrPjcTimeStatusPEOStatusId | — |
| STATUS_ID | TeXfrPyrTimeStatusPEOStatusId | — |
| STATUS_VALUE | TeRdyXfrPjcTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeRdyXfrPyrTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeXfrPjcTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeXfrPyrTimeStatusPEOStatusValue | — |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATE_FROM | TcUiTimeStatusPEODateFrom | — |
| DATE_FROM | TcUserTimeStatusPEODateFrom | — |
| STATUS_ID | TcUiTimeStatusPEOStatusId | — |
| STATUS_ID | TcUserTimeStatusPEOStatusId | — |
| STATUS_ID | TeAppPjcTimeStatusPEOStatusId | — |
| STATUS_ID | TeAppPyrTimeStatusPEOStatusId | — |
| STATUS_ID | TeCmpTimeStatusPEOStatusId | — |
| STATUS_ID | TeErrTimeStatusPEOStatusId | — |
| STATUS_VALUE | TcUiTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TcUserTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeAppPjcTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeAppPyrTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeCmpTimeStatusPEOStatusValue | — |
| STATUS_VALUE | TeErrTimeStatusPEOStatusValue | — |

### [[timestatusextractp1|TimeStatusExtractP1]] (HCM · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| STATUS_ID | StatusId | ✅ |
| STATUS_VALUE | StatusValue | ✅ |
| TM_BLDG_BLK_ID | TimeBuildingBlockId | ✅ |
| TM_BLDG_BLK_VERSION | TimeBuildingBlockVersion | ✅ |
| TM_STATUS_DEF_ID | TimeStatusDefId | ✅ |

### [[timestatuspvo|TimeStatusPVO]] (HCM · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| STATUS_ID | StatusId | ✅ |
| STATUS_VALUE | StatusValue | ✅ |
| TM_BLDG_BLK_ID | TimeBuildingBlockId | ✅ |
| TM_BLDG_BLK_VERSION | TimeBuildingBlockVersion | ✅ |
| TM_STATUS_DEF_ID | TimeStatusDefId | ✅ |
