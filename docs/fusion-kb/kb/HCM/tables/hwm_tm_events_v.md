---
id: DOC-HCM-375
doc_type: system-doc
title: "HWM_TM_EVENTS_V — Eventos de Time Management (View)"
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
  - time-management
  - eventos
  - ciclo-vida
  - view
aliases:
  - HWM_TM_EVENTS_V
  - hwm_tm_events_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_EVENTS_V

## 📌 Visão Geral

View que consolida os eventos do módulo de Time Management, incluindo submissões, aprovações, rejeições e transferências, fornecendo uma visão cronológica do ciclo de vida.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de tempo:** Controle centralizado de registros de horas trabalhadas e ausências.
- **Fluxo de aprovação:** Suporte ao ciclo completo de submissão, aprovação e processamento.
- **Compliance:** Conformidade com políticas internas e regulamentações de jornada de trabalho.
- **Integração:** Conexão com Payroll, Project Costing e Absence Management.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | EVENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do evento | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | EVENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do evento (SUBMIT/APPROVE/REJECT/TRANSFER) | — | 🟡 75% |
| 4 | EVENT_DATE | DATE | NULL | Dados | Data do evento | — | 🟡 75% |
| 5 | EVENT_STATUS | VARCHAR2(30) | NULL | Classificação | Status do evento | — | 🟡 70% |
| 6 | SOURCE_TYPE | VARCHAR2(30) | NULL | Referência | Tipo do registro de origem | — | 🟡 65% |
| 7 | SOURCE_ID | NUMBER(18) | NULL | Referência | ID do registro de origem | — | 🟡 65% |
| 8 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data/hora de criação | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.EVENT_TYPE, t.EVENT_DATE, t.EVENT_STATUS
FROM   HWM_TM_EVENTS_V t
WHERE  t.EVENT_DATE >= TRUNC(SYSDATE) - 30
ORDER BY t.EVENT_DATE DESC
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[deviceeventpvo|DeviceEventPVO]] (GL · BICC: 26/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CORR_ASSIGNMENT_ID | DeviceEventPEOCorrAssignmentId | ✅ |
| CORR_BADGE_ID | DeviceEventPEOCorrBadgeId | ✅ |
| CORR_CREATED_BY | DeviceEventPEOCorrCreatedBy | ✅ |
| CORR_CREATION_DATE | DeviceEventPEOCorrCreationDate | ✅ |
| CORR_LAST_UPDATE_DATE | DeviceEventPEOCorrLastUpdateDate | ✅ |
| CORR_LAST_UPDATE_LOGIN | DeviceEventPEOCorrLastUpdateLogin | ✅ |
| CORR_LAST_UPDATED_BY | DeviceEventPEOCorrLastUpdatedBy | ✅ |
| CORR_PERSON_ID | DeviceEventPEOCorrPersonId | ✅ |
| CREATED_BY | DeviceEventPEOCreatedBy | ✅ |
| CREATION_DATE | DeviceEventPEOCreationDate | ✅ |
| DEVICE_ID | DeviceEventPEODeviceId | ✅ |
| EVENT_STATUS | DeviceEventPEOEventStatus | ✅ |
| EVENT_TIME_REAL | DeviceEventPEOEventTimeReal | ✅ |
| EVENT_TIME_STRING | DeviceEventPEOEventTimeString | ✅ |
| EVENT_TYPE | DeviceEventPEOEventType | ✅ |
| LAST_UPDATE_DATE | DeviceEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DeviceEventPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | DeviceEventPEOLastUpdatedBy | ✅ |
| PERSON_ID | DeviceEventPEOPersonId | ✅ |
| REF_TIMEZONE_ID | DeviceEventPEORefTimezoneId | ✅ |
| REPORTER_ID | DeviceEventPEOReporterId | ✅ |
| REPORTER_ID_TYPE | DeviceEventPEOReporterIdType | ✅ |
| RESOURCE_ID | DeviceEventPEOResourceId | ✅ |
| STATUS | DeviceEventPEOStatus | — |
| TIMEZONE_OFFSET | DeviceEventPEOTimezoneOffset | — |
| TM_EVENT_CORRECTION_ID | DeviceEventPEOTmEventCorrectionId | ✅ |
| TM_EVENT_ID | DeviceEventPEOTmEventId | ✅ |
| TM_EVENT_REQ_ID | DeviceEventPEOTmEventReqId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_EVENTS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_events_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
