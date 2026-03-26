---
id: DOC-HCM-407
doc_type: system-doc
title: "HWM_TM_STATUS_DEF_B — Definicoes de Status de Time Management (Base)"
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
  - time-management
  - status-definition
  - definicao-status
  - base
aliases:
  - HWM_TM_STATUS_DEF_B
  - hwm_tm_status_def_b
  - hwm-tm-status-def-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_STATUS_DEF_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de status** do modulo Time Management. Contem os dados primarios de cada definicao de status sem traducoes.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Definicao de status:** configura as propriedades de cada status.
- **Transicoes:** define quais transicoes entre status sao permitidas.
- **Configuracao:** parametriza o comportamento de cada status no workflow.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATUS_DEF_ID | NUMBER(18) | NOT NULL | PK | Identificador da definicao | — | 🟡 70% |
| 2 | STATUS_ID | NUMBER(18) | NOT NULL | FK | Status associado | HWM_TM_STATUSES | 🟡 70% |
| 3 | DEFINITION_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da definicao | — | 🟡 65% |
| 4 | ALLOW_EDIT_FLAG | VARCHAR2(1) | NULL | Controle | Permite edicao neste status | — | 🟡 60% |
| 5 | ALLOW_DELETE_FLAG | VARCHAR2(1) | NULL | Controle | Permite exclusao neste status | — | 🟡 55% |
| 6 | NEXT_STATUS_ID | NUMBER(18) | NULL | FK | Proximo status permitido | HWM_TM_STATUSES | 🟡 55% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tm_statuses]] — via `STATUS_ID` (status base da definicao de status de tempo)

### Tabelas-filha (FK de saida)
- [[hwm_tm_status_def_tl]] — via `STATUS_DEF_ID` (traducoes da definicao de status)

---

## 📎 Uso Tipico

### Definicoes de status com transicoes
```sql
SELECT d.DEFINITION_CODE, d.ALLOW_EDIT_FLAG,
       d.ALLOW_DELETE_FLAG, d.NEXT_STATUS_ID
FROM   HWM_TM_STATUS_DEF_B d
WHERE  d.STATUS_ID = :p_status_id;
```

### Filtros comuns
- `STATUS_ID = :p_status_id — Definicoes de um status especifico`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes armazenadas em HWM_TM_STATUS_DEF_TL.
- Define regras de comportamento para cada status no ciclo de vida.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_STATUS_DEF_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmstatusdefb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
