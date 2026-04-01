---
id: DOC-HCM-604
doc_type: system-doc
title: "PER_ABS_ATTENDANCE_REASONS — Motivos de Ausência"
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
  - motivos-ausencia
  - absence-reasons
aliases:
  - PER_ABS_ATTENDANCE_REASONS
  - per_abs_attendance_reasons
  - per-abs-attendance-reasons
  - motivos-de-ausência
  - per-abs-attendance-r
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ABS_ATTENDANCE_REASONS

## 📌 Visão Geral

Armazena os **motivos (razões)** associados aos tipos de ausência. Permite detalhar a causa específica de uma ausência além do tipo genérico.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento de motivos** — permite especificar a razão exata da ausência (ex.: consulta médica, cirurgia).
- **Análise de absenteísmo** — segmentação por motivo para análises mais granulares.
- **Compliance** — rastreabilidade de motivos para atender requisitos legais.
- **Políticas de RH** — diferentes motivos podem ter regras distintas de aprovação.
- **Integração com payroll** — motivos podem impactar o cálculo de remuneração.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABS_ATTENDANCE_REASON_ID | NUMBER(18) | NOT NULL | PK | Identificador único do motivo de ausência | — | 🟢 90% |
| 2 | ABSENCE_ATTENDANCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ausência associado | PER_ABSENCE_ATTENDANCE_TYPES_B | 🟢 90% |
| 3 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do motivo de ausência | — | 🟢 85% |
| 4 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_absence_attendance_types_b]] — via `ABSENCE_ATTENDANCE_TYPE_ID` (tipo de ausência pai)

### Tabelas-filha (FK de saída)
- [[per_absence_attendances]] — via `ABS_ATTENDANCE_REASON_ID` (ausências que usam este motivo)

---

## 📎 Uso Típico

### Motivos por tipo de ausência
```sql
SELECT par.NAME, pat.ABSENCE_CATEGORY
FROM   PER_ABS_ATTENDANCE_REASONS par
JOIN   PER_ABSENCE_ATTENDANCE_TYPES_B pat
  ON   par.ABSENCE_ATTENDANCE_TYPE_ID = pat.ABSENCE_ATTENDANCE_TYPE_ID
ORDER BY pat.ABSENCE_CATEGORY, par.NAME;
```

### Filtros comuns
- `ABSENCE_ATTENDANCE_TYPE_ID = :p_type_id` — Motivos de um tipo específico
---

## 🔒 Observações

- Cada motivo está vinculado a um tipo de ausência específico.
- Um tipo de ausência pode ter vários motivos associados.
- A granularidade do motivo permite relatórios mais detalhados de absenteísmo.
---

## 🔗 PVOs Relacionados

### [[absenceeventspvo|AbsenceEventsPVO]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_ATTENDANCE_REASON_ID | AbsenceReasonPEOAbsAttendanceReasonId | — |
| ABSENCE_ATTENDANCE_TYPE_ID | AbsenceReasonPEOAbsenceAttendanceTypeId | — |
| BUSINESS_GROUP_ID | AbsenceReasonPEOBusinessGroupId | — |
| CREATED_BY | AbsenceReasonPEOCreatedBy | — |
| CREATION_DATE | AbsenceReasonPEOCreationDate | — |
| LAST_UPDATE_DATE | AbsenceReasonPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AbsenceReasonPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AbsenceReasonPEOLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | AbsenceReasonPEOLegislativeDataGroupId | — |
| NAME | AbsenceReasonPEOName | — |
| OBJECT_VERSION_NUMBER | AbsenceReasonPEOObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Docs — PER_ABS_ATTENDANCE_REASONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perabsattendancereasons.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
