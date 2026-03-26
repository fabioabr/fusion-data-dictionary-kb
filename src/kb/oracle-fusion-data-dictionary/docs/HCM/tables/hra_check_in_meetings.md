---
id: DOC-HCM-133
doc_type: system-doc
title: "HRA_CHECK_IN_MEETINGS — Reuniões de Check-In"
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
  - performance
  - check-in
  - reunioes-1a1
  - hra
aliases:
  - HRA_CHECK_IN_MEETINGS
  - hra_check_in_meetings
  - hra-check-in-meetings
  - DOC-HCM-133
  - reuniões-de-check-in
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_CHECK_IN_MEETINGS

## 📌 Visão Geral

Armazena os **registros de reuniões de check-in** (1:1) entre gestores e colaboradores no módulo de Performance Management. Inclui data, participantes, notas e status.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reuniões 1:1:** Registro de encontros entre gestor e colaborador.
- **Acompanhamento contínuo:** Documentação de feedback ongoing.
- **Gestão de performance:** Suporte a avaliações contínuas.
- **Histórico de interações:** Trilha de reuniões realizadas.
- **Engagement:** Monitoramento da frequência de check-ins.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECK_IN_MEETING_ID | NUMBER(18) | NOT NULL | PK | Identificador único da reunião | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | MANAGER_PERSON_ID | NUMBER(18) | NULL | FK | Gestor | [[per_all_people_f]] | 🟡 80% |
| 4 | MEETING_DATE | DATE | NULL | Data | Data da reunião | — | 🟢 90% |
| 5 | STATUS | VARCHAR2(30) | NULL | Status | Status (SCHEDULED, COMPLETED, CANCELLED) | — | 🟡 80% |
| 6 | NOTES | VARCHAR2(4000) | NULL | Texto | Notas da reunião | — | 🟡 80% |
| 7 | TEMPLATE_ID | NUMBER(18) | NULL | FK | Template de check-in | [[hra_check_in_tmpls_b]] | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da reuniao de check-in)
- [[per_all_people_f]] — via `MANAGER_PERSON_ID` (gestor da reuniao de check-in)
- [[hra_check_in_tmpls_b]] — via `TEMPLATE_ID` (template da reuniao de check-in)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Check-ins por colaborador
```sql
SELECT m.MEETING_DATE, m.STATUS, m.NOTES
FROM   HRA_CHECK_IN_MEETINGS m
WHERE  m.PERSON_ID = :p_person_id
ORDER BY m.MEETING_DATE DESC;
```

### Check-ins pendentes
```sql
SELECT m.PERSON_ID, m.MANAGER_PERSON_ID, m.MEETING_DATE
FROM   HRA_CHECK_IN_MEETINGS m
WHERE  m.STATUS = 'SCHEDULED'
  AND  m.MEETING_DATE <= SYSDATE;
```

---

## 🔒 Observações

- Check-ins são reuniões informais de acompanhamento (1:1).
- O `STATUS` controla: SCHEDULED (agendado), COMPLETED (realizado), CANCELLED.
- Templates de check-in pré-definem a pauta/estrutura da reunião.
- Frequência de check-ins é um indicador de engagement gerencial.

---

## 📚 Referências

- [Oracle Docs — HRA_CHECK_IN_MEETINGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hracheckinmeetings.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
