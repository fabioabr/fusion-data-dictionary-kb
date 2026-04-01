---
id: DOC-HCM-425
doc_type: system-doc
title: "HXT_TM_HEADER — Cabecalho de Time Card HXT"
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
  - time-labor
  - hxt
  - timecard-header
  - cabecalho-time-card
aliases:
  - HXT_TM_HEADER
  - hxt_tm_header
  - hxt-tm-header
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TM_HEADER

## 📌 Visao Geral

Armazena os **cabecalhos de time cards** (folhas de ponto) do modulo Time & Labor (HXT). Cada registro representa um time card com seu periodo, status e colaborador associado.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de time cards:** registro principal de cada folha de ponto.
- **Workflow de aprovacao:** controla o ciclo de vida do time card.
- **Integracao com payroll:** time cards aprovados alimentam a folha de pagamento.
- **Auditoria:** rastreabilidade completa de cada time card.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TM_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador do cabecalho | — | 🟡 70% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | PERIOD_START_DATE | DATE | NOT NULL | Periodo | Inicio do periodo | — | 🟡 70% |
| 5 | PERIOD_END_DATE | DATE | NOT NULL | Periodo | Fim do periodo | — | 🟡 70% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do time card | — | 🟡 70% |
| 7 | SUBMISSION_DATE | TIMESTAMP | NULL | Periodo | Data/hora da submissao | — | 🟡 60% |
| 8 | TOTAL_HOURS | NUMBER | NULL | Dados | Total de horas | — | 🟡 60% |
| 9 | LAYOUT_ID | NUMBER(18) | NULL | FK | Layout utilizado | HXT_TCLAYST_B | 🟡 55% |
| 10 | APPROVER_ID | NUMBER(18) | NULL | FK | Aprovador | PER_ALL_PEOPLE_F | 🟡 55% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular do cartao de ponto)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo do cartao de ponto)
- [[hxt_tclayst_b]] — via `LAYOUT_ID` (layout usado no cartao de ponto)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Time cards por colaborador e periodo
```sql
SELECT h.TM_HEADER_ID, h.PERSON_ID, h.PERIOD_START_DATE,
       h.PERIOD_END_DATE, h.TOTAL_HOURS, h.STATUS
FROM   HXT_TM_HEADER h
WHERE  h.PERSON_ID = :p_person_id
  AND  h.PERIOD_START_DATE >= :dt_ini;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Por colaborador`
- `STATUS = 'APPROVED' — Time cards aprovados`
- `PERIOD_START_DATE >= :dt_ini — A partir de uma data`

---

## 🔒 Observacoes

- Tabela principal de time cards do modulo HXT.
- Status tipicos: DRAFT, SUBMITTED, APPROVED, REJECTED.
- Time cards aprovados sao enviados ao payroll para processamento.

---

## 📚 Referencias

- [Oracle Docs — HXT_TM_HEADER](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttmheader.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardLayoutSetId | — |
| TM_HEADER_ID | TimecardHeaderId | — |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardLayoutSetId | — |
| TM_HEADER_ID | TimecardHeaderId | — |

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardLayoutSetId | — |
| TM_HEADER_ID | TimecardHeaderId | — |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardLayoutSetId | — |
| TM_HEADER_ID | TimecardHeaderId | — |

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardHeaderPEOTclaystId | — |
| TM_HEADER_ID | TimecardHeaderPEOTimecardHeaderId | — |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardLayoutSetId | — |
| TM_HEADER_ID | TimecardHeaderId | — |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardLayoutSetId | — |
| TM_HEADER_ID | TimecardHeaderId | — |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TCLAYST_ID | TimecardHeaderPEOTclaystId | — |
| TM_HEADER_ID | TimecardHeaderPEOTimecardHeaderId | — |

### [[timecardheaderpvo|TimecardHeaderPVO]] (GL · BICC: 147/147)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_CHAR1 | AttributeChar1 | ✅ |
| ATTRIBUTE_CHAR10 | AttributeChar10 | ✅ |
| ATTRIBUTE_CHAR11 | AttributeChar11 | ✅ |
| ATTRIBUTE_CHAR12 | AttributeChar12 | ✅ |
| ATTRIBUTE_CHAR13 | AttributeChar13 | ✅ |
| ATTRIBUTE_CHAR14 | AttributeChar14 | ✅ |
| ATTRIBUTE_CHAR15 | AttributeChar15 | ✅ |
| ATTRIBUTE_CHAR16 | AttributeChar16 | ✅ |
| ATTRIBUTE_CHAR17 | AttributeChar17 | ✅ |
| ATTRIBUTE_CHAR18 | AttributeChar18 | ✅ |
| ATTRIBUTE_CHAR19 | AttributeChar19 | ✅ |
| ATTRIBUTE_CHAR2 | AttributeChar2 | ✅ |
| ATTRIBUTE_CHAR20 | AttributeChar20 | ✅ |
| ATTRIBUTE_CHAR21 | AttributeChar21 | ✅ |
| ATTRIBUTE_CHAR22 | AttributeChar22 | ✅ |
| ATTRIBUTE_CHAR23 | AttributeChar23 | ✅ |
| ATTRIBUTE_CHAR24 | AttributeChar24 | ✅ |
| ATTRIBUTE_CHAR25 | AttributeChar25 | ✅ |
| ATTRIBUTE_CHAR26 | AttributeChar26 | ✅ |
| ATTRIBUTE_CHAR27 | AttributeChar27 | ✅ |
| ATTRIBUTE_CHAR28 | AttributeChar28 | ✅ |
| ATTRIBUTE_CHAR29 | AttributeChar29 | ✅ |
| ATTRIBUTE_CHAR3 | AttributeChar3 | ✅ |
| ATTRIBUTE_CHAR30 | AttributeChar30 | ✅ |
| ATTRIBUTE_CHAR4 | AttributeChar4 | ✅ |
| ATTRIBUTE_CHAR5 | AttributeChar5 | ✅ |
| ATTRIBUTE_CHAR6 | AttributeChar6 | ✅ |
| ATTRIBUTE_CHAR7 | AttributeChar7 | ✅ |
| ATTRIBUTE_CHAR8 | AttributeChar8 | ✅ |
| ATTRIBUTE_CHAR9 | AttributeChar9 | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | AttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | AttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | AttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | AttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | AttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | AttributeDate15 | ✅ |
| ATTRIBUTE_DATE2 | AttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | AttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | AttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | AttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | AttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | AttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | AttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | AttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | ✅ |
| CALCULATED_TIME_HEADER_ID | CalculatedTimeHeaderId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| END_DATE | EndDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_COMMIT_TIME | LastCommitTime | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_TYPE | ObjectType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RESOURCE_ID | ResourceId | ✅ |
| RESOURCE_TYPE | ResourceType | ✅ |
| START_DATE | StartDate | ✅ |
| TCLAYST_ID | TimecardLayoutSetId | ✅ |
| TIME_BLDG_BLK_ID | TimeBuildingBlockId | ✅ |
| TIME_BLDG_BLK_VERSION | TimeBuildingBlockVersion | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_BLDG_BLK_DAY_ID1 | TimeBuildingBlockDayId1 | ✅ |
| TM_BLDG_BLK_DAY_ID10 | TimeBuildingBlockDayId10 | ✅ |
| TM_BLDG_BLK_DAY_ID11 | TimeBuildingBlockDayId11 | ✅ |
| TM_BLDG_BLK_DAY_ID12 | TimeBuildingBlockDayId12 | ✅ |
| TM_BLDG_BLK_DAY_ID13 | TimeBuildingBlockDayId13 | ✅ |
| TM_BLDG_BLK_DAY_ID14 | TimeBuildingBlockDayId14 | ✅ |
| TM_BLDG_BLK_DAY_ID15 | TimeBuildingBlockDayId15 | ✅ |
| TM_BLDG_BLK_DAY_ID16 | TimeBuildingBlockDayId16 | ✅ |
| TM_BLDG_BLK_DAY_ID17 | TimeBuildingBlockDayId17 | ✅ |
| TM_BLDG_BLK_DAY_ID18 | TimeBuildingBlockDayId18 | ✅ |
| TM_BLDG_BLK_DAY_ID19 | TimeBuildingBlockDayId19 | ✅ |
| TM_BLDG_BLK_DAY_ID2 | TimeBuildingBlockDayId2 | ✅ |
| TM_BLDG_BLK_DAY_ID20 | TimeBuildingBlockDayId20 | ✅ |
| TM_BLDG_BLK_DAY_ID21 | TimeBuildingBlockDayId21 | ✅ |
| TM_BLDG_BLK_DAY_ID22 | TimeBuildingBlockDayId22 | ✅ |
| TM_BLDG_BLK_DAY_ID23 | TimeBuildingBlockDayId23 | ✅ |
| TM_BLDG_BLK_DAY_ID24 | TimeBuildingBlockDayId24 | ✅ |
| TM_BLDG_BLK_DAY_ID25 | TimeBuildingBlockDayId25 | ✅ |
| TM_BLDG_BLK_DAY_ID26 | TimeBuildingBlockDayId26 | ✅ |
| TM_BLDG_BLK_DAY_ID27 | TimeBuildingBlockDayId27 | ✅ |
| TM_BLDG_BLK_DAY_ID28 | TimeBuildingBlockDayId28 | ✅ |
| TM_BLDG_BLK_DAY_ID29 | TimeBuildingBlockDayId29 | ✅ |
| TM_BLDG_BLK_DAY_ID3 | TimeBuildingBlockDayId3 | ✅ |
| TM_BLDG_BLK_DAY_ID30 | TimeBuildingBlockDayId30 | ✅ |
| TM_BLDG_BLK_DAY_ID4 | TimeBuildingBlockDayId4 | ✅ |
| TM_BLDG_BLK_DAY_ID5 | TimeBuildingBlockDayId5 | ✅ |
| TM_BLDG_BLK_DAY_ID6 | TimeBuildingBlockDayId6 | ✅ |
| TM_BLDG_BLK_DAY_ID7 | TimeBuildingBlockDayId7 | ✅ |
| TM_BLDG_BLK_DAY_ID8 | TimeBuildingBlockDayId8 | ✅ |
| TM_BLDG_BLK_DAY_ID9 | TimeBuildingBlockDayId9 | ✅ |
| TM_BLDG_BLK_DAY_VERSION1 | TimeBuildingBlockDayVersion1 | ✅ |
| TM_BLDG_BLK_DAY_VERSION10 | TimeBuildingBlockDayVersion10 | ✅ |
| TM_BLDG_BLK_DAY_VERSION11 | TimeBuildingBlockDayVersion11 | ✅ |
| TM_BLDG_BLK_DAY_VERSION12 | TimeBuildingBlockDayVersion12 | ✅ |
| TM_BLDG_BLK_DAY_VERSION13 | TimeBuildingBlockDayVersion13 | ✅ |
| TM_BLDG_BLK_DAY_VERSION14 | TimeBuildingBlockDayVersion14 | ✅ |
| TM_BLDG_BLK_DAY_VERSION15 | TimeBuildingBlockDayVersion15 | ✅ |
| TM_BLDG_BLK_DAY_VERSION16 | TimeBuildingBlockDayVersion16 | ✅ |
| TM_BLDG_BLK_DAY_VERSION17 | TimeBuildingBlockDayVersion17 | ✅ |
| TM_BLDG_BLK_DAY_VERSION18 | TimeBuildingBlockDayVersion18 | ✅ |
| TM_BLDG_BLK_DAY_VERSION19 | TimeBuildingBlockDayVersion19 | ✅ |
| TM_BLDG_BLK_DAY_VERSION2 | TimeBuildingBlockDayVersion2 | ✅ |
| TM_BLDG_BLK_DAY_VERSION20 | TimeBuildingBlockDayVersion20 | ✅ |
| TM_BLDG_BLK_DAY_VERSION21 | TimeBuildingBlockDayVersion21 | ✅ |
| TM_BLDG_BLK_DAY_VERSION22 | TimeBuildingBlockDayVersion22 | ✅ |
| TM_BLDG_BLK_DAY_VERSION23 | TimeBuildingBlockDayVersion23 | ✅ |
| TM_BLDG_BLK_DAY_VERSION24 | TimeBuildingBlockDayVersion24 | ✅ |
| TM_BLDG_BLK_DAY_VERSION25 | TimeBuildingBlockDayVersion25 | ✅ |
| TM_BLDG_BLK_DAY_VERSION26 | TimeBuildingBlockDayVersion26 | ✅ |
| TM_BLDG_BLK_DAY_VERSION27 | TimeBuildingBlockDayVersion27 | ✅ |
| TM_BLDG_BLK_DAY_VERSION28 | TimeBuildingBlockDayVersion28 | ✅ |
| TM_BLDG_BLK_DAY_VERSION29 | TimeBuildingBlockDayVersion29 | ✅ |
| TM_BLDG_BLK_DAY_VERSION3 | TimeBuildingBlockDayVersion3 | ✅ |
| TM_BLDG_BLK_DAY_VERSION30 | TimeBuildingBlockDayVersion30 | ✅ |
| TM_BLDG_BLK_DAY_VERSION4 | TimeBuildingBlockDayVersion4 | ✅ |
| TM_BLDG_BLK_DAY_VERSION5 | TimeBuildingBlockDayVersion5 | ✅ |
| TM_BLDG_BLK_DAY_VERSION6 | TimeBuildingBlockDayVersion6 | ✅ |
| TM_BLDG_BLK_DAY_VERSION7 | TimeBuildingBlockDayVersion7 | ✅ |
| TM_BLDG_BLK_DAY_VERSION8 | TimeBuildingBlockDayVersion8 | ✅ |
| TM_BLDG_BLK_DAY_VERSION9 | TimeBuildingBlockDayVersion9 | ✅ |
| TM_HEADER_ID | TimecardHeaderId | ✅ |
