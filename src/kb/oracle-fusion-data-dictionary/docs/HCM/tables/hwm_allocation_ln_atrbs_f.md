---
id: DOC-HCM-295
doc_type: system-doc
title: "HWM_ALLOCATION_LN_ATRBS_F — Atributos de Linhas de Alocacao"
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
  - allocation-attributes
  - workforce-management
  - eav
aliases:
  - HWM_ALLOCATION_LN_ATRBS_F
  - hwm_allocation_ln_atrbs_f
  - hwm-allocation-ln-atrbs-f
  - allocation-ln-atrbs
  - atributos-linhas-alocacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_ALLOCATION_LN_ATRBS_F

## 📌 Visao Geral

Armazena **atributos adicionais** das linhas de alocacao em formato flexivel, com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Extensibilidade:** Adicionar atributos customizados a linhas de alocacao.
- **Integracao:** Armazenar dados de dimensoes adicionais.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATION_LN_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador do atributo | — | 🟢 85% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 85% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 85% |
| 4 | ALLOCATION_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha de alocacao | [[hwm_allocation_lines_f]] | 🟢 90% |
| 5 | ATTRIBUTE_NAME | VARCHAR2(240) | NULL | Dados | Nome do atributo | — | 🟡 75% |
| 6 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_allocation_lines_f]] — via `ALLOCATION_LINE_ID` (linha de alocacao do atributo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Atributos de uma linha
```sql
SELECT a.ATTRIBUTE_NAME, a.ATTRIBUTE_VALUE
FROM   HWM_ALLOCATION_LN_ATRBS_F a
WHERE  a.ALLOCATION_LINE_ID = :p_line_id
  AND  SYSDATE BETWEEN a.EFFECTIVE_START_DATE AND a.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective.
- Estrutura EAV para extensibilidade.

---

## 📚 Referencias

- [Oracle Docs — HWM_ALLOCATION_LN_ATRBS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmallocationlnatrbsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
