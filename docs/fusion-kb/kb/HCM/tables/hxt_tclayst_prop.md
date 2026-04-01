---
id: DOC-HCM-421
doc_type: system-doc
title: "HXT_TCLAYST_PROP — Propriedades de Layouts de Time Card"
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
  - propriedades
aliases:
  - HXT_TCLAYST_PROP
  - hxt_tclayst_prop
  - hxt-tclayst-prop
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAYST_PROP

## 📌 Visao Geral

Armazena as **propriedades de configuracao** dos layouts de time card do modulo Time & Labor (HXT). Define caracteristicas comportamentais e visuais de cada layout.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao de layout:** define propriedades como modo de entrada, validacoes, etc.
- **Personalizacao:** permite ajustar comportamento do time card por layout.
- **Regras de negocio:** propriedades que controlam validacoes e comportamento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TCLAYST_PROP_ID | NUMBER(18) | NOT NULL | PK | Identificador da propriedade | — | 🟡 70% |
| 2 | TCLAYST_ID | NUMBER(18) | NOT NULL | FK | Layout associado | HXT_TCLAYST_B | 🟡 70% |
| 3 | PROPERTY_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo da propriedade | — | 🟡 65% |
| 4 | PROPERTY_VALUE | VARCHAR2(240) | NULL | Dados | Valor da propriedade | — | 🟡 65% |
| 5 | PROPERTY_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da propriedade | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_tclayst_b]] — via `TCLAYST_ID` (layout de cartao de ponto da propriedade)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Propriedades de um layout
```sql
SELECT p.PROPERTY_CODE, p.PROPERTY_VALUE, p.PROPERTY_TYPE
FROM   HXT_TCLAYST_PROP p
WHERE  p.TCLAYST_ID = :p_layout_id;
```

### Filtros comuns
- `TCLAYST_ID = :p_layout_id — Por layout`

---

## 🔒 Observacoes

- Contem parametros de configuracao do layout de time card.
- Propriedades controlam comportamento como modo de entrada (diario/semanal), validacoes, etc.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAYST_PROP](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclaystprop.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[timecardlayoutcomppvo|TimecardLayoutCompPVO]] (GL · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANS_SET_ID | TclaystPropPEOAnsSetId | — |
| IND_MGR_FLAG | TclaystPropPEOIndMgrFlag | ✅ |
| IND_TCSMRS_CODE | TclaystPropPEOIndTcsmrsCode | ✅ |
| MEMBERSHIP_FLAG | TclaystPropPEOMembershipFlag | ✅ |
| TCLAYST_PROP_CD | TclaystPropPEOTclaystPropCd | ✅ |
| TCLAYST_PROP_ID | TclaystPropPEOTclaystPropId | ✅ |
| TCLAYST_TE_TYPE | TclaystPropPEOTclaystTeType | — |

### [[timecardlayoutpvo|TimecardLayoutPVO]] (GL · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANS_SET_ID | TclaystPropPEOAnsSetId | — |
| IND_MGR_FLAG | TclaystPropPEOIndMgrFlag | ✅ |
| IND_TCSMRS_CODE | TclaystPropPEOIndTcsmrsCode | ✅ |
| MEMBERSHIP_FLAG | TclaystPropPEOMembershipFlag | ✅ |
| TCLAYST_PROP_CD | TclaystPropPEOTclaystPropCd | ✅ |
| TCLAYST_PROP_ID | TclaystPropPEOTclaystPropId | ✅ |
| TCLAYST_TE_TYPE | TclaystPropPEOTclaystTeType | — |

### [[timecardlayoutregionpvo|TimecardLayoutRegionPVO]] (GL · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANS_SET_ID | TclaystPropPEOAnsSetId | — |
| IND_MGR_FLAG | TclaystPropPEOIndMgrFlag | ✅ |
| IND_TCSMRS_CODE | TclaystPropPEOIndTcsmrsCode | ✅ |
| MEMBERSHIP_FLAG | TclaystPropPEOMembershipFlag | ✅ |
| TCLAYST_PROP_CD | TclaystPropPEOTclaystPropCd | ✅ |
| TCLAYST_PROP_ID | TclaystPropPEOTclaystPropId | ✅ |
| TCLAYST_TE_TYPE | TclaystPropPEOTclaystTeType | — |

### [[timecardlayoutsetpvo|TimecardLayoutSetPVO]] (GL · BICC: 5/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANS_SET_ID | TclaystPropPEOAnsSetId | — |
| IND_MGR_FLAG | TclaystPropPEOIndMgrFlag | ✅ |
| IND_TCSMRS_CODE | TclaystPropPEOIndTcsmrsCode | ✅ |
| MEMBERSHIP_FLAG | TclaystPropPEOMembershipFlag | ✅ |
| TCLAYST_PROP_CD | TclaystPropPEOTclaystPropCd | ✅ |
| TCLAYST_PROP_ID | TclaystPropPEOTclaystPropId | ✅ |
