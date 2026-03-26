---
id: DOC-HCM-291
doc_type: system-doc
title: "HWM_ALLOCATIONS_HDR_F — Cabecalhos de Alocacao de Workforce — Date-Effective"
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
  - projetos
aliases:
  - HWM_ALLOCATIONS_HDR_F
  - hwm_allocations_hdr_f
  - hwm-allocations-hdr-f
  - allocations-hdr
  - cabecalhos-alocacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_ALLOCATIONS_HDR_F

## 📌 Visao Geral

Tabela principal que armazena os **cabecalhos de alocacao de workforce** com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Workforce Management:** Registrar alocacoes de recursos.
- **Projetos:** Associar colaboradores a projetos/atividades.
- **Custos:** Controlar alocacao de custos de mao de obra.

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
| 4 | ALLOCATION_NAME | VARCHAR2(240) | NULL | Dados | Nome da alocacao | — | 🟡 80% |
| 5 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador alocado | [[per_all_people_f]] | 🟢 90% |
| 6 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organizacao destino | [[hr_all_organization_units_f]] | 🟡 80% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da alocacao | — | 🟡 80% |
| 8 | ALLOCATION_PERCENT | NUMBER | NULL | Dados | Percentual de alocacao | — | 🟡 80% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular da alocacao de tempo)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao da alocacao de tempo)

### Tabelas-filha (FK de saida)
- [[hwm_allocations_hdr_tl]] — via `ALLOCATION_HDR_ID` (traducoes do cabecalho de alocacao)
- [[hwm_allocation_lines_f]] — via `ALLOCATION_HDR_ID` (traducoes do cabecalho de alocacao)

---

## 📎 Uso Tipico

### Alocacoes ativas
```sql
SELECT ah.ALLOCATION_NAME, ah.ALLOCATION_PERCENT, ah.STATUS
FROM   HWM_ALLOCATIONS_HDR_F ah
WHERE  ah.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN ah.EFFECTIVE_START_DATE AND ah.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective.
- ALLOCATION_PERCENT indica o percentual do tempo dedicado.

---

## 📚 Referencias

- [Oracle Docs — HWM_ALLOCATIONS_HDR_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmallocationshdrf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
