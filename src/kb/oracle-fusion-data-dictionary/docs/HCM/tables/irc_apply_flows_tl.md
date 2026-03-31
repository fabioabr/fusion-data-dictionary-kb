---
id: DOC-HCM-437
doc_type: system-doc
title: "IRC_APPLY_FLOWS_TL — Traducoes de Fluxos de Candidatura"
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
  - irc
  - apply-flow
  - fluxo-candidatura
  - traducao
aliases:
  - IRC_APPLY_FLOWS_TL
  - irc_apply_flows_tl
  - irc-apply-flows-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_APPLY_FLOWS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** dos fluxos de candidatura do modulo Recruiting (IRC) em multiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** nomes de fluxos em multiplos idiomas.
- **Administracao multilingual:** gerentes veem nomes de fluxos no seu idioma.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLY_FLOW_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do fluxo | IRC_APPLY_FLOWS_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | FLOW_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome traduzido do fluxo | — | 🟡 65% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_apply_flows_b]] — via `APPLY_FLOW_ID` (registro base do fluxo de candidatura)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de um fluxo de candidatura
```sql
SELECT tl.LANGUAGE, tl.FLOW_NAME, tl.DESCRIPTION
FROM   IRC_APPLY_FLOWS_TL tl
WHERE  tl.APPLY_FLOW_ID = :p_flow_id;
```

### Filtros comuns
- `APPLY_FLOW_ID = :p_flow_id — Por fluxo`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para dados completos.
- Chave composta: APPLY_FLOW_ID + LANGUAGE.

---

## 📚 Referencias

- [Oracle Docs — IRC_APPLY_FLOWS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircapplyflowstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[applyflowpvo|ApplyFlowPVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_FLOW_ID | ApplyFlowTranslationPEOApplyFlowId1 | — |
| APPLY_FLOW_NAME | ApplyFlowTranslationPEOApplyFlowName | ✅ |
| CREATED_BY | ApplyFlowTranslationPEOCreatedBy | — |
| CREATION_DATE | ApplyFlowTranslationPEOCreationDate | — |
| DESCRIPTION | ApplyFlowTranslationPEODescription | ✅ |
| LANGUAGE | ApplyFlowTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ApplyFlowTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApplyFlowTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ApplyFlowTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ApplyFlowTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | ApplyFlowTranslationPEOSourceLang | — |

### [[applyflowversionpvo|ApplyFlowVersionPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_FLOW_ID | ApplyFlowTranslationPEOApplyFlowId | — |
| APPLY_FLOW_NAME | ApplyFlowTranslationPEOApplyFlowName | ✅ |
| DESCRIPTION | ApplyFlowTranslationPEODescription | ✅ |
| LANGUAGE | ApplyFlowTranslationPEOLanguage | — |
| SOURCE_LANG | ApplyFlowTranslationPEOSourceLang | — |
