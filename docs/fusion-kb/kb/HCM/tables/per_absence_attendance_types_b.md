---
id: DOC-HCM-603
doc_type: system-doc
title: "PER_ABSENCE_ATTENDANCE_TYPES_B — Tipos de Ausência (Base)"
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
  - tipos-ausencia
  - absence-types
aliases:
  - PER_ABSENCE_ATTENDANCE_TYPES_B
  - per_absence_attendance_types_b
  - per-absence-attendance-types-b
  - tipos-de-ausência-(base)
  - per-absence-attendan
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ABSENCE_ATTENDANCE_TYPES_B

## 📌 Visão Geral

Armazena a definição dos **tipos de ausência** disponíveis no sistema. Cada tipo define uma categoria de ausência com regras específicas de duração, unidade, elegibilidade e integração com payroll.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de tipos de ausência** — define cada tipo (férias, doença, licença maternidade, etc.).
- **Regras de unidade** — especifica se a ausência é contada em dias ou horas.
- **Integração com planos de acumulação** — associa tipos de ausência a planos de accrual.
- **Controle de elegibilidade** — define quais colaboradores podem usar cada tipo.
- **Base para relatórios** — classificação padronizada de ausências.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_ATTENDANCE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de ausência | — | 🟢 95% |
| 2 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio associado | — | 🟢 90% |
| 3 | INPUT_VALUE_ID | NUMBER(18) | NULL | FK | Valor de entrada para integração com payroll | — | 🟡 75% |
| 4 | ABSENCE_CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria da ausência (VACATION, SICKNESS, etc.) | — | 🟢 85% |
| 5 | HOURS_OR_DAYS | VARCHAR2(1) | NULL | Configuração | Unidade de medida (H=horas, D=dias) | — | 🟢 85% |
| 6 | INCREASING_OR_DECREASING_FLAG | VARCHAR2(1) | NULL | Configuração | Se a ausência incrementa ou decrementa saldo | — | 🟡 75% |
| 7 | DATE_EFFECTIVE | DATE | NULL | Vigência | Data de efetividade do tipo | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta identificada — tabela raiz de configuração de tipos de ausência.

### Tabelas-filha (FK de saída)
- [[per_absence_attendances]] — via `ABSENCE_ATTENDANCE_TYPE_ID` (ausências deste tipo)
- [[per_abs_attendance_types_tl]] — via `ABSENCE_ATTENDANCE_TYPE_ID` (traduções do tipo de ausência/presença)
- [[per_abs_attendance_reasons]] — via `ABSENCE_ATTENDANCE_TYPE_ID` (motivos associados)

---

## 📎 Uso Típico

### Tipos de ausência ativos
```sql
SELECT pat.ABSENCE_ATTENDANCE_TYPE_ID, pat.ABSENCE_CATEGORY,
       pat.HOURS_OR_DAYS
FROM   PER_ABSENCE_ATTENDANCE_TYPES_B pat
WHERE  pat.DATE_EFFECTIVE <= SYSDATE;
```

### Filtros comuns
- `ABSENCE_CATEGORY = 'VACATION'` — Tipos de férias
- `HOURS_OR_DAYS = 'D'` — Tipos contados em dias
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- O campo `HOURS_OR_DAYS` determina a unidade de medida para todas as ausências deste tipo.
- A flag `INCREASING_OR_DECREASING_FLAG` controla se o tipo incrementa ou decrementa o saldo acumulado.
- Tipos de ausência são configurados por business group, permitindo variações por entidade legal.
---

## 🔗 PVOs Relacionados

### [[absenceeventspvo|AbsenceEventsPVO]] (HCM · BICC: 1/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_ATTENDANCE_TYPE_ID | AbsenceTypePEOAbsenceAttendanceTypeId | — |
| ABSENCE_CATEGORY | AbsenceTypePEOAbsenceCategory | — |
| ABSENCE_OVERLAP_FLAG | AbsenceTypePEOAbsenceOverlapFlag | — |
| ASSIGNMENT_STATUS_TYPE_ID | AbsenceTypePEOAssignmentStatusTypeId | — |
| ATTRIBUTE_CATEGORY | AbsenceTypePEOAttributeCategory | — |
| BUSINESS_GROUP_ID | AbsenceTypePEOBusinessGroupId | — |
| CREATED_BY | AbsenceTypePEOCreatedBy | — |
| CREATION_DATE | AbsenceTypePEOCreationDate | — |
| DATE_EFFECTIVE | AbsenceTypePEODateEffective | — |
| DATE_END | AbsenceTypePEODateEnd | — |
| HOURS_OR_DAYS | AbsenceTypePEOHoursOrDays | — |
| INCREASING_OR_DECREASING_FLAG | AbsenceTypePEOIncreasingOrDecreasingFlag | — |
| INPUT_VALUE_ID | AbsenceTypePEOInputValueId | — |
| LAST_UPDATE_DATE | AbsenceTypePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AbsenceTypePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AbsenceTypePEOLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | AbsenceTypePEOLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | AbsenceTypePEOObjectVersionNumber | — |
| OVERRIDE_FLAG | AbsenceTypePEOOverrideFlag | — |
| PER_OR_WORKREL_FLAG | AbsenceTypePEOPerOrWorkrelFlag | — |
| SCH_BASED_DUR | AbsenceTypePEOSchBasedDur | — |

---

## 📚 Referências

- [Oracle Docs — PER_ABSENCE_ATTENDANCE_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perabsenceattendancetypesb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
