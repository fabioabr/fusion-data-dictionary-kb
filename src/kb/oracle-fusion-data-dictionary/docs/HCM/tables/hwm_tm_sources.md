---
id: DOC-HCM-405
doc_type: system-doc
title: "HWM_TM_SOURCES — Fontes de Dados de Time Management"
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
  - sources
  - fontes-dados
aliases:
  - HWM_TM_SOURCES
  - hwm_tm_sources
  - hwm-tm-sources
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_SOURCES

## 📌 Visao Geral

Armazena as **fontes de dados** (sources) do modulo Time Management. Define de onde as entradas de tempo sao originadas (ex.: relogio de ponto, web, dispositivo movel).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreabilidade de origem:** identifica a fonte de cada entrada de tempo.
- **Configuracao de integracao:** define fontes validas para entrada de dados.
- **Auditoria:** permite verificar a origem dos registros de tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SOURCE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da fonte | — | 🟡 70% |
| 2 | SOURCE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da fonte | — | 🟡 65% |
| 3 | SOURCE_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da fonte | — | 🟡 65% |
| 4 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da fonte (CLOCK, WEB, MOBILE) | — | 🟡 60% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[hwm_tm_rec]] — via `SOURCE_ID` (registros de tempo por fonte)

---

## 📎 Uso Tipico

### Listar fontes ativas de tempo
```sql
SELECT s.SOURCE_ID, s.SOURCE_CODE, s.SOURCE_NAME, s.SOURCE_TYPE
FROM   HWM_TM_SOURCES s
WHERE  s.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Fontes ativas`
- `SOURCE_TYPE = :p_type — Por tipo de fonte`

---

## 🔒 Observacoes

- Define as origens validas para entradas de tempo.
- Fontes comuns: relogio de ponto, entrada web, dispositivo movel, importacao em lote.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_SOURCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmsources.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
