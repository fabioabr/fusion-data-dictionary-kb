---
id: DOC-HCM-214
doc_type: system-doc
title: "HRR_TMPL_ANLYT_BOX_RATINGS — Ratings de Box Analítico"
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
  - analytics
  - ratings
aliases:
  - HRR_TMPL_ANLYT_BOX_RATINGS
  - hrr_tmpl_anlyt_box_ratings
  - ratings-de-box-analítico
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_TMPL_ANLYT_BOX_RATINGS

## 📌 Visão Geral

Armazena **ratings associados a caixas** do 9-Box. Mapeamento de classificações para cada caixa.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Mapeamento:** Rating para posição do 9-Box.
- **Configuração:** Critérios de classificação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BOX_RATING_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | BOX_LABEL_ID | NUMBER(18) | NOT NULL | FK | Label da caixa | [[hrr_tmpl_anlyt_box_lbls_b]] | 🟢 85% |
| 3 | ANALYTIC_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo analítico | [[hrr_tmpl_analytic_types_b]] | 🟢 85% |
| 4 | RATING_LEVEL_CODE | VARCHAR2(30) | NULL | Classificação | Nível de rating | — | 🟡 70% |
| 5 | AXIS_TYPE | VARCHAR2(30) | NULL | Classificação | Eixo (X=performance, Y=potential) | — | 🟡 70% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_tmpl_anlyt_box_lbls_b]] — via `BOX_LABEL_ID` (rotulo de box da classificacao)
- [[hrr_tmpl_analytic_types_b]] — via `ANALYTIC_TYPE_ID` (tipo analitico da classificacao de box)

---

## 📎 Uso Típico

### Ratings de um box
```sql
SELECT br.RATING_LEVEL_CODE, br.AXIS_TYPE
FROM   HRR_TMPL_ANLYT_BOX_RATINGS br
WHERE  br.BOX_LABEL_ID = :p_id;
```

---

## 🔒 Observações

- Eixo X = performance; eixo Y = potencial.
- Mapeamento rating -> posição do 9-Box.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
