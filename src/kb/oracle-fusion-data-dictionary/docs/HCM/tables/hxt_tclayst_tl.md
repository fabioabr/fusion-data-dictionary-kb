---
id: DOC-HCM-422
doc_type: system-doc
title: "HXT_TCLAYST_TL — Traducoes de Layouts de Time Card"
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
  - time-labor
  - hxt
  - timecard-layout
  - traducao
  - translation
aliases:
  - HXT_TCLAYST_TL
  - hxt_tclayst_tl
  - hxt-tclayst-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAYST_TL

## 📌 Visao Geral

Tabela de traducoes que armazena os **textos traduzidos** dos layouts de time card do modulo Time & Labor (HXT) em multiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traducoes** (Translation) — armazena textos em multiplos idiomas.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Internacionalizacao:** nomes de layouts traduzidos para multiplos idiomas.
- **Interface multilingual:** exibe nomes de layouts no idioma do usuario.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TCLAYST_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do layout | HXT_TCLAYST_B | 🟡 70% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 85% |
| 4 | LAYOUT_NAME | VARCHAR2(240) | NOT NULL | Identificacao | Nome traduzido do layout | — | 🟡 65% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_tclayst_b]] — via `TCLAYST_ID` (registro base do layout de cartao de ponto)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Traducoes de um layout de time card
```sql
SELECT tl.LANGUAGE, tl.LAYOUT_NAME, tl.DESCRIPTION
FROM   HXT_TCLAYST_TL tl
WHERE  tl.TCLAYST_ID = :p_layout_id;
```

### Filtros comuns
- `TCLAYST_ID = :p_layout_id — Por layout`
- `LANGUAGE = USERENV('LANG') — Idioma da sessao`

---

## 🔒 Observacoes

- Tabela de traducoes (_TL) — join com _B para dados completos.
- Chave composta: TCLAYST_ID + LANGUAGE.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAYST_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclaysttl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[timecardlayoutcomppvo|TimecardLayoutCompPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TclaystTLPEODescription | ✅ |
| LANGUAGE | TclaystTLPEOLanguage | — |
| NAME | TclaystTLPEOName | ✅ |
| TCLAYST_ID | TclaystTLPEOTimecardLayoutSetId | — |

### [[timecardlayoutpvo|TimecardLayoutPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TclaystTLPEODescription | ✅ |
| LANGUAGE | TclaystTLPEOLanguage | — |
| NAME | TclaystTLPEOName | ✅ |
| TCLAYST_ID | TclaystTLPEOTimecardLayoutSetId | — |

### [[timecardlayoutregionpvo|TimecardLayoutRegionPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TclaystTLPEODescription | ✅ |
| LANGUAGE | TclaystTLPEOLanguage | — |
| NAME | TclaystTLPEOName | ✅ |
| TCLAYST_ID | TclaystTLPEOTimecardLayoutSetId | — |

### [[timecardlayoutsetpvo|TimecardLayoutSetPVO]] (GL · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TclaystTLPEOCreatedBy | ✅ |
| CREATION_DATE | TclaystTLPEOCreationDate | ✅ |
| DESCRIPTION | TclaystTLPEODescription | ✅ |
| ENTERPRISE_ID | TclaystTLPEOEnterpriseId | ✅ |
| LANGUAGE | TclaystTLPEOLanguage | ✅ |
| LAST_UPDATE_DATE | TclaystTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TclaystTLPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TclaystTLPEOLastUpdatedBy | ✅ |
| NAME | TclaystTLPEOName | ✅ |
| OBJECT_VERSION_NUMBER | TclaystTLPEOObjectVersionNumber | ✅ |
| SOURCE_LANG | TclaystTLPEOSourceLang | ✅ |
| TCLAYST_ID | TclaystTLPEOTimecardLayoutSetId | ✅ |
