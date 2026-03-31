---
id: DOC-HCM-293
doc_type: system-doc
title: "HWM_ALLOCATIONS_HDR_VL — Cabecalhos de Alocacao (View Linguistica)"
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
  - allocations
  - workforce-management
  - view
aliases:
  - HWM_ALLOCATIONS_HDR_VL
  - hwm_allocations_hdr_vl
  - hwm-allocations-hdr-vl
  - allocations-hdr-vl
  - cabecalhos-alocacao-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_ALLOCATIONS_HDR_VL

## 📌 Visao Geral

View linguistica que combina dados base e traducoes dos **cabecalhos de alocacao de workforce**.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Consulta:** Acessar dados de alocacao com nomes traduzidos em uma unica view.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATION_HDR_ID | NUMBER(18) | NOT NULL | PK | Identificador do cabecalho | — | 🟢 90% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 90% |
| 4 | ALLOCATION_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome da alocacao (traduzido) | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao (traduzida) | — | 🟢 85% |
| 6 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 80% |
| 8 | ALLOCATION_PERCENT | NUMBER | NULL | Dados | Percentual de alocacao | — | 🟡 80% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular da alocacao de tempo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Alocacoes com nomes traduzidos
```sql
SELECT vl.ALLOCATION_NAME, vl.ALLOCATION_PERCENT, vl.STATUS
FROM   HWM_ALLOCATIONS_HDR_VL vl
WHERE  vl.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_VL` — View Linguistica.
- Prefer usar esta view em relatorios para obter nomes traduzidos.

---

## 📚 Referencias

- [Oracle Docs — HWM_ALLOCATIONS_HDR_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmallocationshdrvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[ruleinputpvo|RuleInputPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_ID | AllocationsHdrVLPEOAllocationId | — |
| ALLOCATION_NAME | AllocationsHdrVLPEOAllocationName | ✅ |
| EFFECTIVE_END_DATE | AllocationsHdrVLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AllocationsHdrVLPEOEffectiveStartDate | ✅ |

### [[ruleoutputpvo|RuleOutputPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_ID | AllocationsHdrVLPEOAllocationId | — |
| ALLOCATION_NAME | AllocationsHdrVLPEOAllocationName | ✅ |
| EFFECTIVE_END_DATE | AllocationsHdrVLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AllocationsHdrVLPEOEffectiveStartDate | ✅ |

### [[rulepvo|RulePVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_ID | AllocationsHdrVLPEOAllocationId | — |
| ALLOCATION_NAME | AllocationsHdrVLPEOAllocationName | ✅ |
| EFFECTIVE_END_DATE | AllocationsHdrVLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AllocationsHdrVLPEOEffectiveStartDate | ✅ |

### [[ruletemplateinputpvo|RuleTemplateInputPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_ID | AllocationsHdrVLPEOAllocationId | — |
| ALLOCATION_NAME | AllocationsHdrVLPEOAllocationName | ✅ |
| EFFECTIVE_END_DATE | AllocationsHdrVLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AllocationsHdrVLPEOEffectiveStartDate | ✅ |

### [[ruletemplatepvo|RuleTemplatePVO]] (GL · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_ID | AllocationsHdrVLPEOAllocationId | ✅ |
| ALLOCATION_NAME | AllocationsHdrVLPEOAllocationName | ✅ |
| EFFECTIVE_END_DATE | AllocationsHdrVLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AllocationsHdrVLPEOEffectiveStartDate | ✅ |

### [[ruletemplateusagepvo|RuleTemplateUsagePVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_ID | AllocationsHdrVLPEOAllocationId | — |
| ALLOCATION_NAME | AllocationsHdrVLPEOAllocationName | ✅ |
| EFFECTIVE_END_DATE | AllocationsHdrVLPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AllocationsHdrVLPEOEffectiveStartDate | ✅ |
