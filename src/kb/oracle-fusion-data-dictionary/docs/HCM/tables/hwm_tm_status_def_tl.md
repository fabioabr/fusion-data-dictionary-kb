---
id: DOC-HCM-408
doc_type: system-doc
title: "HWM_TM_STATUS_DEF_TL — Traducoes de Definicoes de Status de Time Management"
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
  - status-definition
  - traducao
  - translation
aliases:
  - HWM_TM_STATUS_DEF_TL
  - hwm_tm_status_def_tl
  - hwm-tm-status-def-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_STATUS_DEF_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** das definicoes de status do modulo Time Management em multiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** armazena nomes e descricoes em multiplos idiomas.
- **Interface multilingual:** alimenta a UI com textos no idioma do usuario.
- **Relatorios:** permite gerar relatorios no idioma preferido.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STATUS_DEF_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da definicao | HWM_TM_STATUS_DEF_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | STATUS_DEF_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome traduzido da definicao | — | 🟡 65% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tm_status_def_b]] — via `STATUS_DEF_ID` (registro base da definicao de status)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de uma definicao de status
```sql
SELECT tl.LANGUAGE, tl.STATUS_DEF_NAME, tl.DESCRIPTION
FROM   HWM_TM_STATUS_DEF_TL tl
WHERE  tl.STATUS_DEF_ID = :p_def_id;
```

### Filtros comuns
- `STATUS_DEF_ID = :p_def_id — Traducoes de uma definicao`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para obter dados completos.
- Chave composta: STATUS_DEF_ID + LANGUAGE.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_STATUS_DEF_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmstatusdeftl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[timestatusdeftranslationpvo|TimeStatusDefTranslationPVO]] (GL · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | — |
| ENTERPRISE_ID | EnterpriseId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SOURCE_LANG | SourceLang | — |
| TM_STATUS_DEF_ID | TimeStatusDefId | ✅ |
| TM_STATUS_NAME | TimeStatusName | — |
