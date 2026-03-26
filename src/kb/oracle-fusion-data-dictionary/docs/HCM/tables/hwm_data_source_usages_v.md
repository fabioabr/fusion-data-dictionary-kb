---
id: DOC-HCM-297
doc_type: system-doc
title: "HWM_DATA_SOURCE_USAGES_V — Usos de Fonte de Dados (View)"
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
  - data-source
  - workforce-management
  - configuracao
aliases:
  - HWM_DATA_SOURCE_USAGES_V
  - hwm_data_source_usages_v
  - hwm-data-source-usages-v
  - data-source-usages
  - usos-fonte-dados
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_DATA_SOURCE_USAGES_V

## 📌 Visao Geral

View que expoe os **usos de fontes de dados** do modulo Workforce Management.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Visualizar mapeamento de fontes de dados.
- **Troubleshooting:** Identificar fontes utilizadas por funcionalidades especificas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DATA_SOURCE_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador do uso | — | 🟡 80% |
| 2 | DATA_SOURCE_CODE | VARCHAR2(30) | NULL | Classificacao | Codigo da fonte de dados | — | 🟡 80% |
| 3 | USAGE_CODE | VARCHAR2(30) | NULL | Classificacao | Codigo do uso/funcionalidade | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao | — | 🟡 70% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificacao | Habilitado (Y/N) | — | 🟡 75% |
| 6 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data de criacao | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Fontes habilitadas
```sql
SELECT dsu.DATA_SOURCE_CODE, dsu.USAGE_CODE, dsu.DESCRIPTION
FROM   HWM_DATA_SOURCE_USAGES_V dsu
WHERE  dsu.ENABLED_FLAG = 'Y';
```

---

## 🔒 Observacoes

- View somente leitura — sufixo `_V`.
- Tabela de metadados de configuracao.

---

## 📚 Referencias

- [Oracle Docs — HWM_DATA_SOURCE_USAGES_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmdatasourceusagesv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
