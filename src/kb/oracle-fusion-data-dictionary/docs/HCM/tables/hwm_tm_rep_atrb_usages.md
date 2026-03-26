---
id: DOC-HCM-389
doc_type: system-doc
title: "HWM_TM_REP_ATRB_USAGES — Usos de Atributos Reportados de Tempo"
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
  - reported-attribute-usage
  - uso-atributos-reportados
aliases:
  - HWM_TM_REP_ATRB_USAGES
  - hwm_tm_rep_atrb_usages
  - hwm-tm-rep-atrb-usages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_ATRB_USAGES

## 📌 Visao Geral

Armazena os **usos (usages) dos atributos de entradas reportadas** de tempo. Define o contexto em que cada atributo reportado é utilizado.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuração de atributos:** define como atributos reportados são utilizados.
- **Mapeamento:** associa atributos a contextos de processamento (payroll, GL, projetos).
- **Rastreabilidade:** audita o uso de cada atributo reportado.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_ATRB_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso | — | 🟡 70% |
| 2 | REP_ATRB_ID | NUMBER(18) | NOT NULL | FK | Atributo reportado | HWM_TM_REP_ATRBS | 🟡 70% |
| 3 | USAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de uso | — | 🟡 60% |
| 4 | USAGE_CONTEXT | VARCHAR2(240) | NULL | Dados | Contexto de utilização | — | 🟡 55% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tm_rep_atrbs]] — via `REP_ATRB_ID` (atributo de reporte do uso)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Usos de um atributo reportado
```sql
SELECT u.USAGE_TYPE, u.USAGE_CONTEXT
FROM   HWM_TM_REP_ATRB_USAGES u
WHERE  u.REP_ATRB_ID = :p_atrb_id;
```

### Filtros comuns
- `REP_ATRB_ID = :p_atrb_id — Filtrar por atributo`

---

## 🔒 Observacoes

- Tabela de associação entre atributos reportados e seus contextos de uso.
- Utilizada internamente pelo engine de Time Management.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_REP_ATRB_USAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepatrbusages.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
