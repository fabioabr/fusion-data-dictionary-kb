---
id: DOC-HCM-207
doc_type: system-doc
title: "HRR_MEETING_PARTICIPANTS — Participantes de Talent Review"
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
  - HRR_MEETING_PARTICIPANTS
  - hrr_meeting_participants
  - participantes-de-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_MEETING_PARTICIPANTS

## 📌 Visão Geral

**Participantes** de reuniões (gestores, convidados).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro:** Participantes e presença.
- **Permissões:** Acesso à reunião.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEETING_PARTICIPANT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | MEETING_ID | NUMBER(18) | NOT NULL | FK | Reunião | [[hrr_meetings]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Participante | [[per_all_people_f]] | 🟢 90% |
| 4 | PARTICIPANT_ROLE | VARCHAR2(30) | NULL | Classificação | Papel (MANAGER, HR_PARTNER) | — | 🟡 70% |
| 5 | ATTENDANCE_STATUS | VARCHAR2(30) | NULL | Classificação | Presença (CONFIRMED, DECLINED) | — | 🟡 65% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_meetings]] — via `MEETING_ID` (reuniao de talent review do participante)
- [[per_all_people_f]] — via `PERSON_ID` (participante da reuniao de talent review)

---

## 📎 Uso Típico

### Consulta típica
```sql
SELECT p.PERSON_ID, p.PARTICIPANT_ROLE, p.ATTENDANCE_STATUS FROM HRR_MEETING_PARTICIPANTS p WHERE p.MEETING_ID = :p_id;
```

---

## 🔒 Observações

Participantes discutem os revisados.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
