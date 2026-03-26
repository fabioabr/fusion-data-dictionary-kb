---
id: DOC-HCM-015
doc_type: system-doc
title: "ANC_PER_ABS_ENTRIES — Entradas de Ausência por Pessoa"
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
  - absence-management
  - entradas-ausencia
  - absence-entries
  - ferias
  - licenca
  - faltas
aliases:
  - ANC_PER_ABS_ENTRIES
  - anc_per_abs_entries
  - entradas-ausencia-hcm
  - absence-entries
  - anc-per-abs-entries
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_ENTRIES

## 📌 Visão Geral

Armazena as **entradas (registros) de ausência** dos colaboradores. Cada registro representa uma solicitação de ausência com datas de início/fim, tipo, motivo, status de aprovação e duração. É a **tabela transacional principal** do módulo Absence Management.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de ausências:** Tabela central para todas as solicitações de ausência (férias, licenças, faltas, etc.).
- **Workflow de aprovação:** Controle do ciclo de vida da solicitação (submetida, aprovada, rejeitada).
- **Integração com folha:** Base para cálculo de impacto salarial das ausências.
- **Self-service:** Alimenta a visão do colaborador e do gestor.
- **Relatórios de absenteísmo:** Tabela principal para análise de ausências.
- **Compliance trabalhista:** Registro formal de afastamentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da entrada de ausência | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | ABSENCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ausência | [[anc_absence_types_f]] | 🟢 95% |
| 4 | ABSENCE_REASON_ID | NUMBER(18) | NULL | FK | Motivo da ausência | [[anc_absence_reasons_f]] | 🟢 90% |
| 5 | ABSENCE_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status (SUBMITTED, APPROVED, REJECTED, SAVED, CANCELLED) | — | 🟢 90% |
| 6 | START_DATE | DATE | NOT NULL | Data | Data de início da ausência | — | 🟢 95% |
| 7 | END_DATE | DATE | NULL | Data | Data de fim da ausência | — | 🟢 95% |
| 8 | DURATION | NUMBER | NULL | Duração | Duração total da ausência | — | 🟢 90% |
| 9 | DURATION_UOM | VARCHAR2(30) | NULL | Classificação | Unidade de medida (DAYS, HOURS) | — | 🟡 80% |
| 10 | COMMENTS | VARCHAR2(2000) | NULL | Texto livre | Comentários do colaborador | — | 🟢 90% |
| 11 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Workflow | Status de aprovação | — | 🟡 75% |
| 12 | APPROVED_BY | NUMBER(18) | NULL | Workflow | Gestor que aprovou | — | 🟡 70% |
| 13 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Assignment do colaborador | [[per_all_assignments_m]] | 🟡 80% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 18 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da ausencia registrada)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo da ausencia registrada)
- [[anc_absence_reasons_f]] — via `ABSENCE_REASON_ID` (motivo da ausencia registrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio da ausencia)

### Tabelas-filha (FK de saída)
- [[anc_per_abs_daily_dtls]] — via `ABSENCE_ENTRY_ID` (detalhes diários)
- [[anc_per_abs_entry_dtls]] — via `ABSENCE_ENTRY_ID` (detalhes adicionais)
- [[anc_per_abs_certs]] — via `ABSENCE_ENTRY_ID` (certificados medicos da ausencia)
- [[anc_per_abs_maternity]] — via `ABSENCE_ENTRY_ID` (dados de maternidade)

---

## 📎 Uso Típico

### Ausências aprovadas por período
```sql
SELECT e.ABSENCE_ENTRY_ID, e.PERSON_ID, e.START_DATE, e.END_DATE,
       e.DURATION, e.ABSENCE_STATUS, t.ABSENCE_TYPE_NAME
FROM   ANC_PER_ABS_ENTRIES e
JOIN   ANC_ABSENCE_TYPES_F t ON e.ABSENCE_TYPE_ID = t.ABSENCE_TYPE_ID
WHERE  e.ABSENCE_STATUS = 'APPROVED'
  AND  e.START_DATE BETWEEN :start_date AND :end_date
  AND  SYSDATE BETWEEN t.EFFECTIVE_START_DATE AND t.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ABSENCE_STATUS = 'APPROVED'` — Ausências aprovadas
- `ABSENCE_STATUS = 'SUBMITTED'` — Pendentes de aprovação
- `ABSENCE_STATUS = 'CANCELLED'` — Canceladas
- `PERSON_ID = :p_person_id` — Ausências de um colaborador específico

---

## 🔒 Observações

- Tabela transacional principal do módulo de ausências.
- O campo `ABSENCE_STATUS` controla o ciclo de vida da solicitação.
- `DURATION` armazena a duração calculada; os detalhes dia a dia estão em `ANC_PER_ABS_DAILY_DTLS`.
- Ausências canceladas (`CANCELLED`) permanecem no histórico para auditoria.

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_ENTRIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabsentries.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
