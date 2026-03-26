---
id: DOC-HCM-208
doc_type: system-doc
title: "HRR_MEETING_REVIEWEES — Revisados em Talent Review"
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
  - HRR_MEETING_REVIEWEES
  - hrr_meeting_reviewees
  - revisados-em-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_MEETING_REVIEWEES

## 📌 Visão Geral

**Revisados (reviewees)** em reuniões. Colaboradores sendo avaliados/discutidos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Pool de revisados:** Colaboradores avaliados.
- **9-Box:** Classificações de performance e potencial.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEETING_REVIEWEE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | MEETING_ID | NUMBER(18) | NOT NULL | FK | Reunião | [[hrr_meetings]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Revisado | [[per_all_people_f]] | 🟢 90% |
| 4 | PERFORMANCE_RATING | VARCHAR2(30) | NULL | Classificação | Performance | — | 🟡 70% |
| 5 | POTENTIAL_RATING | VARCHAR2(30) | NULL | Classificação | Potencial | — | 🟡 70% |
| 6 | RISK_OF_LOSS | VARCHAR2(30) | NULL | Classificação | Risco de perda (HIGH, MEDIUM, LOW) | — | 🟡 65% |
| 7 | IMPACT_OF_LOSS | VARCHAR2(30) | NULL | Classificação | Impacto da perda | — | 🟡 65% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_meetings]] — via `MEETING_ID` (reuniao de talent review do avaliado)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador avaliado no talent review)

### Tabelas-filha

---

## 📎 Uso Típico

### Consulta típica
```sql
SELECT r.PERSON_ID, r.PERFORMANCE_RATING, r.POTENTIAL_RATING, r.RISK_OF_LOSS FROM HRR_MEETING_REVIEWEES r WHERE r.MEETING_ID = :p_id;
```

---

## 🔒 Observações

Performance + potencial = 9-Box.
- `RISK_OF_LOSS` e `IMPACT_OF_LOSS` informam retenção.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
