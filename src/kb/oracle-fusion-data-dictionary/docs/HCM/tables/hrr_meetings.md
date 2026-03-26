---
id: DOC-HCM-205
doc_type: system-doc
title: "HRR_MEETINGS — Reuniões de Talent Review"
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
  - HRR_MEETINGS
  - hrr_meetings
  - reuniões-de-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_MEETINGS

## 📌 Visão Geral

Armazena **reuniões de Talent Review**. Sessões agendadas de revisão de talentos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Agendamento:** Reuniões de Talent Review.
- **Registro:** Sessões de revisão.
- **Integração:** Com dashboards e conteúdo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEETING_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | MEETING_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome | — | 🟢 85% |
| 3 | DASHBOARD_ID | NUMBER(18) | NULL | FK | Dashboard | [[hrr_dashboards]] | 🟡 80% |
| 4 | MEETING_DATE | DATE | NULL | Data | Data da reunião | — | 🟡 80% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (SCHEDULED, IN_PROGRESS, COMPLETED) | — | 🟡 75% |
| 6 | ORGANIZER_ID | NUMBER(18) | NULL | FK | Organizador | [[per_all_people_f]] | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboards]] — via `DASHBOARD_ID` (dashboard da reuniao de talent review)

### Tabelas-filha

---

## 📎 Uso Típico

### Reuniões agendadas
```sql
SELECT m.MEETING_ID, m.MEETING_NAME, m.MEETING_DATE, m.STATUS_CODE
FROM   HRR_MEETINGS m
WHERE  m.STATUS_CODE = 'SCHEDULED'
ORDER BY m.MEETING_DATE;
```

---

## 🔒 Observações

- Tabela central de Talent Review meetings.
- Ciclo: SCHEDULED -> IN_PROGRESS -> COMPLETED.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
