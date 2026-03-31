---
id: DOC-HCM-628
doc_type: system-doc
title: "PER_ASG_ABSENCE_RECORDING — Registro de Ausências por Assignment"
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
  - ausencias
  - assignment-absence
aliases:
  - PER_ASG_ABSENCE_RECORDING
  - per_asg_absence_recording
  - per-asg-absence-recording
  - registro-de-ausências-por-assignment
  - per-asg-absence-reco
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASG_ABSENCE_RECORDING

## 📌 Visão Geral

Armazena o **registro de ausências vinculado ao assignment** do colaborador. Relaciona cada ausência ao assignment específico, permitindo rastreamento por vínculo empregatício.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento por assignment** — vincula ausências ao assignment correto.
- **Multi-assignment** — suporta colaboradores com múltiplos vínculos.
- **Integração com payroll** — identifica qual assignment será impactado pela ausência.
- **Relatórios** — análise de ausências por assignment/departamento.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASG_ABSENCE_RECORDING_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 90% |
| 3 | ABSENCE_ATTENDANCE_ID | NUMBER(18) | NOT NULL | FK | Ausência registrada | PER_ABSENCE_ATTENDANCES | 🟢 90% |
| 4 | ABSENCE_DAYS | NUMBER | NULL | Cálculo | Dias de ausência para este assignment | — | 🟢 85% |
| 5 | ABSENCE_HOURS | NUMBER | NULL | Cálculo | Horas de ausência para este assignment | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo do registro de ausência)
- [[per_absence_attendances]] — via `ABSENCE_ATTENDANCE_ID` (ausência registrada no vínculo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Ausências por assignment
```sql
SELECT par.ASSIGNMENT_ID, par.ABSENCE_DAYS, par.ABSENCE_HOURS
FROM   PER_ASG_ABSENCE_RECORDING par
WHERE  par.ABSENCE_ATTENDANCE_ID = :p_absence_id;
```

### Filtros comuns
- `ASSIGNMENT_ID = :p_assignment_id` — Ausências de um assignment específico
---

## 🔒 Observações

- Tabela de junção — conecta ausências a assignments específicos.
- Necessária para cenários de multi-assignment onde a ausência impacta um vínculo específico.
- A duração pode diferir entre assignments se o colaborador tem jornadas diferentes.
---

## 📚 Referências

- [Oracle Docs — PER_ASG_ABSENCE_RECORDING](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perasgabsencerecording.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
