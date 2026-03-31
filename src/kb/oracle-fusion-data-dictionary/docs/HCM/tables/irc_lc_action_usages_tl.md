---
id: DOC-HCM-504
doc_type: system-doc
title: "IRC_LC_ACTION_USAGES_TL — Usos de Acoes (Traducoes)"
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
  - lc-action-usages-tl
  - irc-recruiting
aliases:
  - IRC_LC_ACTION_USAGES_TL
  - irc_lc_action_usages_tl
  - lc-action-usages-tl
  - lc-action-hcm
  - irc-lc-action-usages-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_LC_ACTION_USAGES_TL

## Visao Geral

Traducoes dos usos de acoes. Tabela `_TL`.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducao** (Translation) — armazena textos multilingues associados a tabela `_B` correspondente. Chave composta pelo ID base + LANGUAGE.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** Nomes traduzidos.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LC_ACTION_USAGE_ID | NUMBER(18) | NOT NULL | PK/FK | Uso base | IRC_LC_ACTION_USAGES_B | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | USAGE_NAME | VARCHAR2(240) | NULL | Dados | Nome traduzido | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_lc_action_usages_b]] — via `LC_ACTION_USAGE_ID` (registro base do uso de acao do ciclo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Nomes em portugues
```sql
SELECT tl.USAGE_NAME FROM IRC_LC_ACTION_USAGES_TL tl WHERE tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Portugues
---

## Observacoes

- Chave composta: LC_ACTION_USAGE_ID + LANGUAGE.
---

## Referencias

- [Oracle Docs -- IRC_LC_ACTION_USAGES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irclcactionusagestl.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[routingstependactionpvo|RoutingStepEndActionPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DESCRIPTION | ActionUsgTranslatePEOActionDescription | ✅ |
| ACTION_NAME | ActionUsgTranslatePEOActionName | ✅ |
| LANGUAGE | ActionUsgTranslatePEOLanguage | — |
| STEP_ACTION_USAGE_ID | ActionUsgTranslatePEOStepActionUsageId | — |

### [[routingstepstartactionpvo|RoutingStepStartActionPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DESCRIPTION | ActionUsgTranslatePEOActionDescription | ✅ |
| ACTION_NAME | ActionUsgTranslatePEOActionName | ✅ |
| LANGUAGE | ActionUsgTranslatePEOLanguage | — |
| STEP_ACTION_USAGE_ID | ActionUsgTranslatePEOStepActionUsageId | — |

### [[routingstepstateactionpvo|RoutingStepStateActionPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DESCRIPTION | ActionUsgTranslatePEOActionDescription | ✅ |
| ACTION_NAME | ActionUsgTranslatePEOActionName | ✅ |
| LANGUAGE | ActionUsgTranslatePEOLanguage | — |
| STEP_ACTION_USAGE_ID | ActionUsgTranslatePEOStepActionUsageId | — |
