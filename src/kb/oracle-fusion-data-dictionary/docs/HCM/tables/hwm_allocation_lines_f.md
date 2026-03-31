---
id: DOC-HCM-294
doc_type: system-doc
title: "HWM_ALLOCATION_LINES_F — Linhas de Alocacao de Workforce"
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
  - allocation-lines
  - workforce-management
  - detalhamento
aliases:
  - HWM_ALLOCATION_LINES_F
  - hwm_allocation_lines_f
  - hwm-allocation-lines-f
  - allocation-lines
  - linhas-alocacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_ALLOCATION_LINES_F

## 📌 Visao Geral

Armazena as **linhas de alocacao** de workforce com versionamento date-effective. Cada linha detalha uma parcela da alocacao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Detalhamento:** Quebrar alocacao em linhas detalhadas.
- **Custos:** Distribuir custos por projeto/atividade.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATION_LINE_ID | NUMBER(18) | NOT NULL | PK | Identificador da linha | — | 🟢 90% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 90% |
| 4 | ALLOCATION_HDR_ID | NUMBER(18) | NOT NULL | FK | Cabecalho de alocacao | [[hwm_allocations_hdr_f]] | 🟢 95% |
| 5 | LINE_PERCENT | NUMBER | NULL | Dados | Percentual desta linha | — | 🟡 80% |
| 6 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto destino | — | 🟡 75% |
| 7 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | — | 🟡 70% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_allocations_hdr_f]] — via `ALLOCATION_HDR_ID` (cabecalho da alocacao de tempo)

### Tabelas-filha (FK de saida)
- [[hwm_allocation_ln_atrbs_f]] — via `ALLOCATION_LINE_ID` (atributos da linha de alocacao)

---

## 📎 Uso Tipico

### Linhas de uma alocacao
```sql
SELECT al.LINE_PERCENT, al.PROJECT_ID, al.TASK_ID
FROM   HWM_ALLOCATION_LINES_F al
WHERE  al.ALLOCATION_HDR_ID = :p_hdr_id
  AND  SYSDATE BETWEEN al.EFFECTIVE_START_DATE AND al.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective.
- A soma dos LINE_PERCENT deve igualar o ALLOCATION_PERCENT do cabecalho.

---

## 📚 Referencias

- [Oracle Docs — HWM_ALLOCATION_LINES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmallocationlinesf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[allocationlinespvo|AllocationLinesPVO]] (GL · BICC: 11/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_LINE_ID | AllocLinesPEOAllocationLineId | ✅ |
| ALLOCATION_LINE_PRIORITY | AllocLinesPEOAllocationLinePriority | ✅ |
| ALLOCATION_RULE_ID | AllocLinesPEOAllocationRuleId | ✅ |
| ALLOCATION_VALUE | AllocLinesPEOAllocationValue | ✅ |
| CREATED_BY | AllocLinesPEOCreatedBy | ✅ |
| CREATION_DATE | AllocLinesPEOCreationDate | ✅ |
| DATA_LEVEL | AllocLinesPEODataLevel | — |
| EFFECTIVE_END_DATE | AllocLinesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | AllocLinesPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | AllocLinesPEOEnterpriseId | — |
| LAST_UPDATE_DATE | AllocLinesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AllocLinesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AllocLinesPEOLastUpdatedBy | ✅ |
| MODULE_ID | AllocLinesPEOModuleId | — |
| OBJECT_VERSION_NUMBER | AllocLinesPEOObjectVersionNumber | — |
