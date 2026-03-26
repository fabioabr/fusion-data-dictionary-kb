---
id: DOC-HCM-509
doc_type: system-doc
title: "IRC_LC_SETTING_ITEMS — Configuracoes do Ciclo de Vida"
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
  - recruiting
  - lc-settings
  - irc-recruiting
aliases:
  - IRC_LC_SETTING_ITEMS
  - irc_lc_setting_items
  - lc-setting-items
  - lc-setting-hcm
  - irc-lc-setting-items
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_LC_SETTING_ITEMS

## Visao Geral

**Itens de configuracao** do ciclo de vida do candidato.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Parametros que controlam o workflow.
- **Personalizacao:** Ajustar comportamento por organizacao.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LC_SETTING_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | SETTING_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo da configuracao | — | 🟡 80% |
| 3 | SETTING_VALUE | VARCHAR2(240) | NULL | Dados | Valor | — | 🟡 70% |
| 4 | PROCESS_ID | NUMBER(18) | NULL | FK | Processo | IRC_PROCESSES_B | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_processes_b]] — via `PROCESS_ID` (processo seletivo da configuracao do ciclo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Configuracoes de um processo
```sql
SELECT si.SETTING_CODE, si.SETTING_VALUE
FROM   IRC_LC_SETTING_ITEMS si WHERE si.PROCESS_ID = :p_id;
```

### Filtros comuns
- `PROCESS_ID = :id` — Por processo
---

## Observacoes

- Parametros configuraveis por processo.
---

## Referencias

- [Oracle Docs -- IRC_LC_SETTING_ITEMS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irclcsettingitems.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM
