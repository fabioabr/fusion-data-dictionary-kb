---
id: DOC-HCM-209
doc_type: system-doc
title: "HRR_MEETING_REVW_CONTENT — Conteúdo de Revisão em Talent Review"
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
  - HRR_MEETING_REVW_CONTENT
  - hrr_meeting_revw_content
  - conteúdo-de-revisão-em-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_MEETING_REVW_CONTENT

## 📌 Visão Geral

**Conteúdo** discutido sobre cada revisado. Anotações, decisões e ações.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Documentação:** Discussões e decisões.
- **Ações:** Pós-reunião.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REVW_CONTENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | MEETING_ID | NUMBER(18) | NOT NULL | FK | Reunião | [[hrr_meetings]] | 🟢 90% |
| 3 | MEETING_REVIEWEE_ID | NUMBER(18) | NOT NULL | FK | Revisado | [[hrr_meeting_reviewees]] | 🟢 85% |
| 4 | CONTENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (NOTE, DECISION, ACTION) | — | 🟡 70% |
| 5 | CONTENT_TEXT | VARCHAR2(4000) | NULL | Texto livre | Conteúdo | — | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_meetings]] — via `MEETING_ID` (reuniao do conteudo de avaliacao)
- [[hrr_meeting_reviewees]] — via `MEETING_REVIEWEE_ID` (avaliado do conteudo de talent review)

---

## 📎 Uso Típico

### Consulta típica
```sql
SELECT rc.CONTENT_TYPE, rc.CONTENT_TEXT FROM HRR_MEETING_REVW_CONTENT rc WHERE rc.MEETING_REVIEWEE_ID = :p_id;
```

---

## 🔒 Observações

Documenta decisões e ações de talent review.

---

## 🔗 PVOs Relacionados

### [[meetingrevwcontentpvo|MeetingRevwContentPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MEETING_ID | MeetingId | ✅ |
| METRIC_ID | MetricId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| REVIEW_CONTENT_ID | ReviewContentId | ✅ |
| USE_AS_AXIS_FLAG | UseAsAxisFlag | ✅ |
| USE_AS_UNDERLAY_FLAG | UseAsUnderlayFlag | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
