---
id: DOC-HCM-425
doc_type: system-doc
title: "HXT_TM_HEADER — Cabecalho de Time Card HXT"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-labor
  - hxt
  - timecard-header
  - cabecalho-time-card
aliases:
  - HXT_TM_HEADER
  - hxt_tm_header
  - hxt-tm-header
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TM_HEADER

## 📌 Visao Geral

Armazena os **cabecalhos de time cards** (folhas de ponto) do modulo Time & Labor (HXT). Cada registro representa um time card com seu periodo, status e colaborador associado.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de time cards:** registro principal de cada folha de ponto.
- **Workflow de aprovacao:** controla o ciclo de vida do time card.
- **Integracao com payroll:** time cards aprovados alimentam a folha de pagamento.
- **Auditoria:** rastreabilidade completa de cada time card.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TM_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador do cabecalho | — | 🟡 70% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | PERIOD_START_DATE | DATE | NOT NULL | Periodo | Inicio do periodo | — | 🟡 70% |
| 5 | PERIOD_END_DATE | DATE | NOT NULL | Periodo | Fim do periodo | — | 🟡 70% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do time card | — | 🟡 70% |
| 7 | SUBMISSION_DATE | TIMESTAMP | NULL | Periodo | Data/hora da submissao | — | 🟡 60% |
| 8 | TOTAL_HOURS | NUMBER | NULL | Dados | Total de horas | — | 🟡 60% |
| 9 | LAYOUT_ID | NUMBER(18) | NULL | FK | Layout utilizado | HXT_TCLAYST_B | 🟡 55% |
| 10 | APPROVER_ID | NUMBER(18) | NULL | FK | Aprovador | PER_ALL_PEOPLE_F | 🟡 55% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular do cartao de ponto)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo do cartao de ponto)
- [[hxt_tclayst_b]] — via `LAYOUT_ID` (layout usado no cartao de ponto)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Time cards por colaborador e periodo
```sql
SELECT h.TM_HEADER_ID, h.PERSON_ID, h.PERIOD_START_DATE,
       h.PERIOD_END_DATE, h.TOTAL_HOURS, h.STATUS
FROM   HXT_TM_HEADER h
WHERE  h.PERSON_ID = :p_person_id
  AND  h.PERIOD_START_DATE >= :dt_ini;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Por colaborador`
- `STATUS = 'APPROVED' — Time cards aprovados`
- `PERIOD_START_DATE >= :dt_ini — A partir de uma data`

---

## 🔒 Observacoes

- Tabela principal de time cards do modulo HXT.
- Status tipicos: DRAFT, SUBMITTED, APPROVED, REJECTED.
- Time cards aprovados sao enviados ao payroll para processamento.

---

## 📚 Referencias

- [Oracle Docs — HXT_TM_HEADER](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttmheader.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
