---
id: DOC-HCM-206
doc_type: system-doc
title: "HRR_MEETING_FACILITATORS — Facilitadores de Talent Review"
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
  - talent-review
  - meetings
aliases:
  - HRR_MEETING_FACILITATORS
  - hrr_meeting_facilitators
  - facilitadores-de-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_MEETING_FACILITATORS

## 📌 Visão Geral

**Facilitadores** de reuniões de Talent Review.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Designação:** Facilitadores de reuniões.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEETING_FACILITATOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | MEETING_ID | NUMBER(18) | NOT NULL | FK | Reunião | [[hrr_meetings]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Facilitador | [[per_all_people_f]] | 🟢 90% |
| 4 | FACILITATOR_ROLE | VARCHAR2(30) | NULL | Classificação | Papel | — | 🟡 70% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_meetings]] — via `MEETING_ID` (reuniao de talent review do facilitador)
- [[per_all_people_f]] — via `PERSON_ID` (facilitador da reuniao de talent review)

---

## 📎 Uso Típico

### Consulta típica
```sql
SELECT f.PERSON_ID, f.FACILITATOR_ROLE FROM HRR_MEETING_FACILITATORS f WHERE f.MEETING_ID = :p_id;
```

---

## 🔒 Observações

Facilitadores conduzem a reunião.

---

## 🔗 PVOs Relacionados

### [[meetingfacilitatorpvo|MeetingFacilitatorPVO]] (HCM · BICC: 5/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| FACILITATOR_PERSON_ID | FacilitatorPersonId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MEETING_FACILITATOR_ID | MeetingFacilitatorId | ✅ |
| MEETING_ID | MeetingId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[meetingfactpvo|MeetingFactPVO]] (HCM · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | MeetingFacilitatorPEOCreatedBy | — |
| CREATION_DATE | MeetingFacilitatorPEOCreationDate | — |
| ENTERPRISE_ID | MeetingFacilitatorPEOEnterpriseId | — |
| FACILITATOR_PERSON_ID | MeetingFacilitatorPEOFacilitatorPersonId | ✅ |
| LAST_UPDATE_DATE | MeetingFacilitatorPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MeetingFacilitatorPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | MeetingFacilitatorPEOLastUpdatedBy | — |
| MEETING_FACILITATOR_ID | MeetingFacilitorPEOMeetingFacilitatorId | — |
| MEETING_ID | MeetingFacilitatorPEOMeetingId | — |
| OBJECT_VERSION_NUMBER | MeetingFacilitatorPEOObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
