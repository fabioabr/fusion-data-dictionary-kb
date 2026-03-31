---
id: DOC-HCM-417
doc_type: system-doc
title: "HXT_TCLAYFLD_DEFNS_B — Definicoes de Campos de Layout de Time Card (Base)"
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
  - campo-layout
  - base
aliases:
  - HXT_TCLAYFLD_DEFNS_B
  - hxt_tclayfld_defns_b
  - hxt-tclayfld-defns-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAYFLD_DEFNS_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de campos** dos layouts de time card do modulo Time & Labor (HXT). Define quais campos aparecem no formulario de entrada de tempo.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao de UI:** define quais campos aparecem no time card.
- **Personalizacao:** permite customizar o formulario de entrada de tempo.
- **Padronizacao:** garante consistencia na captura de dados de tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TCLAYFLD_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador da definicao do campo | — | 🟡 70% |
| 2 | LAYOUT_ID | NUMBER(18) | NOT NULL | FK | Layout de time card | HXT_TCLAYST_B | 🟡 65% |
| 3 | FIELD_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do campo | — | 🟡 65% |
| 4 | FIELD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do campo (TEXT, NUMBER, LOV) | — | 🟡 60% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Controle | Campo obrigatorio (Y/N) | — | 🟡 60% |
| 6 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 55% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 60% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_tclayst_b]] — via `LAYOUT_ID` (layout do campo de cartao de ponto)

### Tabelas-filha (FK de saida)
- [[hxt_tclayfld_defns_tl]] — via `TCLAYFLD_DEFN_ID` (traducoes da definicao de campo)

---

## 📎 Uso Tipico

### Campos de um layout de time card
```sql
SELECT d.FIELD_CODE, d.FIELD_TYPE, d.REQUIRED_FLAG,
       d.DISPLAY_SEQUENCE
FROM   HXT_TCLAYFLD_DEFNS_B d
WHERE  d.LAYOUT_ID = :p_layout_id
  AND  d.ENABLED_FLAG = 'Y'
ORDER BY d.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `LAYOUT_ID = :p_layout_id — Por layout`
- `ENABLED_FLAG = 'Y' — Campos ativos`
- `REQUIRED_FLAG = 'Y' — Campos obrigatorios`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em HXT_TCLAYFLD_DEFNS_TL.
- Define a estrutura de campos do formulario de time card.
- Campos podem ser do tipo texto, numerico, LOV (lista de valores), etc.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAYFLD_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclayflddefnsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[templatelayoutcompdisplayvaluepvo|TemplateLayoutCompDisplayValuePVO]] (GL · BICC: 50/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TclayfldBPEOCreatedBy | ✅ |
| CREATION_DATE | TclayfldBPEOCreationDate | ✅ |
| DISPLAY_SEQUENCE | TclayfldBPEODisplaySequence | ✅ |
| ENTERPRISE_ID | TclayfldBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TclayfldBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TclayfldBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TclayfldBPEOLastUpdatedBy | ✅ |
| MODULE_ID | TclayfldBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TclayfldBPEOObjectVersionNumber | — |
| P_TCLAYFLD_DEFNS_ID | TclayfldBPEOPTclayfldDefnsId | ✅ |
| SEED_DATA_SOURCE | TclayfldBPEOSeedDataSource | — |
| SGUID | TclayfldBPEOSguid | — |
| TCLAY_ID | TclayfldBPEOTclayId | ✅ |
| TCLAYFLD_ATTRIBUTE_CATEGORY | TclayfldBPEOTclayfldAttributeCategory | — |
| TCLAYFLD_ATTRIBUTE_CHAR1 | TclayfldBPEOTclayfldAttributeChar1 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR10 | TclayfldBPEOTclayfldAttributeChar10 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR11 | TclayfldBPEOTclayfldAttributeChar11 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR12 | TclayfldBPEOTclayfldAttributeChar12 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR13 | TclayfldBPEOTclayfldAttributeChar13 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR14 | TclayfldBPEOTclayfldAttributeChar14 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR15 | TclayfldBPEOTclayfldAttributeChar15 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR16 | TclayfldBPEOTclayfldAttributeChar16 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR17 | TclayfldBPEOTclayfldAttributeChar17 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR18 | TclayfldBPEOTclayfldAttributeChar18 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR19 | TclayfldBPEOTclayfldAttributeChar19 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR2 | TclayfldBPEOTclayfldAttributeChar2 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR20 | TclayfldBPEOTclayfldAttributeChar20 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR21 | TclayfldBPEOTclayfldAttributeChar21 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR22 | TclayfldBPEOTclayfldAttributeChar22 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR23 | TclayfldBPEOTclayfldAttributeChar23 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR24 | TclayfldBPEOTclayfldAttributeChar24 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR25 | TclayfldBPEOTclayfldAttributeChar25 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR26 | TclayfldBPEOTclayfldAttributeChar26 | — |
| TCLAYFLD_ATTRIBUTE_CHAR27 | TclayfldBPEOTclayfldAttributeChar27 | — |
| TCLAYFLD_ATTRIBUTE_CHAR28 | TclayfldBPEOTclayfldAttributeChar28 | — |
| TCLAYFLD_ATTRIBUTE_CHAR29 | TclayfldBPEOTclayfldAttributeChar29 | — |
| TCLAYFLD_ATTRIBUTE_CHAR3 | TclayfldBPEOTclayfldAttributeChar3 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR30 | TclayfldBPEOTclayfldAttributeChar30 | — |
| TCLAYFLD_ATTRIBUTE_CHAR4 | TclayfldBPEOTclayfldAttributeChar4 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR5 | TclayfldBPEOTclayfldAttributeChar5 | — |
| TCLAYFLD_ATTRIBUTE_CHAR6 | TclayfldBPEOTclayfldAttributeChar6 | — |
| TCLAYFLD_ATTRIBUTE_CHAR7 | TclayfldBPEOTclayfldAttributeChar7 | — |
| TCLAYFLD_ATTRIBUTE_CHAR8 | TclayfldBPEOTclayfldAttributeChar8 | — |
| TCLAYFLD_ATTRIBUTE_CHAR9 | TclayfldBPEOTclayfldAttributeChar9 | — |
| TCLAYFLD_ATTRIBUTE_DATE1 | TclayfldBPEOTclayfldAttributeDate1 | ✅ |
| TCLAYFLD_ATTRIBUTE_DATE10 | TclayfldBPEOTclayfldAttributeDate10 | — |
| TCLAYFLD_ATTRIBUTE_DATE11 | TclayfldBPEOTclayfldAttributeDate11 | — |
| TCLAYFLD_ATTRIBUTE_DATE12 | TclayfldBPEOTclayfldAttributeDate12 | — |
| TCLAYFLD_ATTRIBUTE_DATE13 | TclayfldBPEOTclayfldAttributeDate13 | — |
| TCLAYFLD_ATTRIBUTE_DATE14 | TclayfldBPEOTclayfldAttributeDate14 | — |
| TCLAYFLD_ATTRIBUTE_DATE15 | TclayfldBPEOTclayfldAttributeDate15 | — |
| TCLAYFLD_ATTRIBUTE_DATE2 | TclayfldBPEOTclayfldAttributeDate2 | — |
| TCLAYFLD_ATTRIBUTE_DATE3 | TclayfldBPEOTclayfldAttributeDate3 | — |
| TCLAYFLD_ATTRIBUTE_DATE4 | TclayfldBPEOTclayfldAttributeDate4 | — |
| TCLAYFLD_ATTRIBUTE_DATE5 | TclayfldBPEOTclayfldAttributeDate5 | — |
| TCLAYFLD_ATTRIBUTE_DATE6 | TclayfldBPEOTclayfldAttributeDate6 | — |
| TCLAYFLD_ATTRIBUTE_DATE7 | TclayfldBPEOTclayfldAttributeDate7 | — |
| TCLAYFLD_ATTRIBUTE_DATE8 | TclayfldBPEOTclayfldAttributeDate8 | — |
| TCLAYFLD_ATTRIBUTE_DATE9 | TclayfldBPEOTclayfldAttributeDate9 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER1 | TclayfldBPEOTclayfldAttributeNumber1 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER10 | TclayfldBPEOTclayfldAttributeNumber10 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER11 | TclayfldBPEOTclayfldAttributeNumber11 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER12 | TclayfldBPEOTclayfldAttributeNumber12 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER13 | TclayfldBPEOTclayfldAttributeNumber13 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER14 | TclayfldBPEOTclayfldAttributeNumber14 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER15 | TclayfldBPEOTclayfldAttributeNumber15 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER16 | TclayfldBPEOTclayfldAttributeNumber16 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER17 | TclayfldBPEOTclayfldAttributeNumber17 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER18 | TclayfldBPEOTclayfldAttributeNumber18 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER19 | TclayfldBPEOTclayfldAttributeNumber19 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER2 | TclayfldBPEOTclayfldAttributeNumber2 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER20 | TclayfldBPEOTclayfldAttributeNumber20 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER3 | TclayfldBPEOTclayfldAttributeNumber3 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER4 | TclayfldBPEOTclayfldAttributeNumber4 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER5 | TclayfldBPEOTclayfldAttributeNumber5 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER6 | TclayfldBPEOTclayfldAttributeNumber6 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER7 | TclayfldBPEOTclayfldAttributeNumber7 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER8 | TclayfldBPEOTclayfldAttributeNumber8 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER9 | TclayfldBPEOTclayfldAttributeNumber9 | ✅ |
| TCLAYFLD_DEFNS_CD | TclayfldBPEOTclayfldDefnsCd | ✅ |
| TCLAYFLD_DEFNS_ID | TclayfldBPEOTclayfldDefnsId | ✅ |
| TCLAYFLD_DEFNS_INSTANCE_FLAG | TclayfldBPEOTclayfldDefnsInstanceFlag | ✅ |
| TCLAYFLD_TMPL_ID | TclayfldBPEOTclayfldTmplId | — |

### [[templatelayoutcomponentpvo|TemplateLayoutComponentPVO]] (GL · BICC: 50/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TclayfldBPEOCreatedBy | ✅ |
| CREATION_DATE | TclayfldBPEOCreationDate | ✅ |
| DISPLAY_SEQUENCE | TclayfldBPEODisplaySequence | ✅ |
| ENTERPRISE_ID | TclayfldBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TclayfldBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TclayfldBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TclayfldBPEOLastUpdatedBy | ✅ |
| MODULE_ID | TclayfldBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TclayfldBPEOObjVersionNumber | — |
| P_TCLAYFLD_DEFNS_ID | TclayfldBPEOPTclayfldDefnsId | ✅ |
| SEED_DATA_SOURCE | TclayfldBPEOSeedDataSource | — |
| SGUID | TclayfldBPEOSguid | — |
| TCLAY_ID | TclayfldBPEOTclayId | ✅ |
| TCLAYFLD_ATTRIBUTE_CATEGORY | TclayfldBPEOTclayfldAtrbCat | — |
| TCLAYFLD_ATTRIBUTE_CHAR1 | TclayfldBPEOTclayfldAtrbChar1 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR10 | TclayfldBPEOTclayfldAtrbChar10 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR11 | TclayfldBPEOTclayfldAtrbChar11 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR12 | TclayfldBPEOTclayfldAtrbChar12 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR13 | TclayfldBPEOTclayfldAtrbChar13 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR14 | TclayfldBPEOTclayfldAtrbChar14 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR15 | TclayfldBPEOTclayfldAtrbChar15 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR16 | TclayfldBPEOTclayfldAtrbChar16 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR17 | TclayfldBPEOTclayfldAtrbChar17 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR18 | TclayfldBPEOTclayfldAtrbChar18 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR19 | TclayfldBPEOTclayfldAtrbChar19 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR2 | TclayfldBPEOTclayfldAtrbChar2 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR20 | TclayfldBPEOTclayfldAtrbChar20 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR21 | TclayfldBPEOTclayfldAtrbChar21 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR22 | TclayfldBPEOTclayfldAtrbChar22 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR23 | TclayfldBPEOTclayfldAtrbChar23 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR24 | TclayfldBPEOTclayfldAtrbChar24 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR25 | TclayfldBPEOTclayfldAtrbChar25 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR26 | TclayfldBPEOTclayfldAtrbChar26 | — |
| TCLAYFLD_ATTRIBUTE_CHAR27 | TclayfldBPEOTclayfldAtrbChar27 | — |
| TCLAYFLD_ATTRIBUTE_CHAR28 | TclayfldBPEOTclayfldAtrbChar28 | — |
| TCLAYFLD_ATTRIBUTE_CHAR29 | TclayfldBPEOTclayfldAtrbChar29 | — |
| TCLAYFLD_ATTRIBUTE_CHAR3 | TclayfldBPEOTclayfldAtrbChar3 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR30 | TclayfldBPEOTclayfldAtrbChar30 | — |
| TCLAYFLD_ATTRIBUTE_CHAR4 | TclayfldBPEOTclayfldAtrbChar4 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR5 | TclayfldBPEOTclayfldAtrbChar5 | — |
| TCLAYFLD_ATTRIBUTE_CHAR6 | TclayfldBPEOTclayfldAtrbChar6 | — |
| TCLAYFLD_ATTRIBUTE_CHAR7 | TclayfldBPEOTclayfldAtrbChar7 | — |
| TCLAYFLD_ATTRIBUTE_CHAR8 | TclayfldBPEOTclayfldAtrbChar8 | — |
| TCLAYFLD_ATTRIBUTE_CHAR9 | TclayfldBPEOTclayfldAtrbChar9 | — |
| TCLAYFLD_ATTRIBUTE_DATE1 | TclayfldBPEOTclayfldAtrbDate1 | ✅ |
| TCLAYFLD_ATTRIBUTE_DATE10 | TclayfldBPEOTclayfldAtrbDate10 | — |
| TCLAYFLD_ATTRIBUTE_DATE11 | TclayfldBPEOTclayfldAtrbDate11 | — |
| TCLAYFLD_ATTRIBUTE_DATE12 | TclayfldBPEOTclayfldAtrbDate12 | — |
| TCLAYFLD_ATTRIBUTE_DATE13 | TclayfldBPEOTclayfldAtrbDate13 | — |
| TCLAYFLD_ATTRIBUTE_DATE14 | TclayfldBPEOTclayfldAtrbDate14 | — |
| TCLAYFLD_ATTRIBUTE_DATE15 | TclayfldBPEOTclayfldAtrbDate15 | — |
| TCLAYFLD_ATTRIBUTE_DATE2 | TclayfldBPEOTclayfldAtrbDate2 | — |
| TCLAYFLD_ATTRIBUTE_DATE3 | TclayfldBPEOTclayfldAtrbDate3 | — |
| TCLAYFLD_ATTRIBUTE_DATE4 | TclayfldBPEOTclayfldAtrbDate4 | — |
| TCLAYFLD_ATTRIBUTE_DATE5 | TclayfldBPEOTclayfldAtrbDate5 | — |
| TCLAYFLD_ATTRIBUTE_DATE6 | TclayfldBPEOTclayfldAtrbDate6 | — |
| TCLAYFLD_ATTRIBUTE_DATE7 | TclayfldBPEOTclayfldAtrbDate7 | — |
| TCLAYFLD_ATTRIBUTE_DATE8 | TclayfldBPEOTclayfldAtrbDate8 | — |
| TCLAYFLD_ATTRIBUTE_DATE9 | TclayfldBPEOTclayfldAtrbDate9 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER1 | TclayfldBPEOTclayfldAtrbNum1 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER10 | TclayfldBPEOTclayfldAtrbNum10 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER11 | TclayfldBPEOTclayfldAtrbNum11 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER12 | TclayfldBPEOTclayfldAtrbNum12 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER13 | TclayfldBPEOTclayfldAtrbNum13 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER14 | TclayfldBPEOTclayfldAtrbNum14 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER15 | TclayfldBPEOTclayfldAtrbNum15 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER16 | TclayfldBPEOTclayfldAtrbNum16 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER17 | TclayfldBPEOTclayfldAtrbNum17 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER18 | TclayfldBPEOTclayfldAtrbNum18 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER19 | TclayfldBPEOTclayfldAtrbNum19 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER2 | TclayfldBPEOTclayfldAtrbNum2 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER20 | TclayfldBPEOTclayfldAtrbNum20 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER3 | TclayfldBPEOTclayfldAtrbNum3 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER4 | TclayfldBPEOTclayfldAtrbNum4 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER5 | TclayfldBPEOTclayfldAtrbNum5 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER6 | TclayfldBPEOTclayfldAtrbNum6 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER7 | TclayfldBPEOTclayfldAtrbNum7 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER8 | TclayfldBPEOTclayfldAtrbNum8 | ✅ |
| TCLAYFLD_ATTRIBUTE_NUMBER9 | TclayfldBPEOTclayfldAtrbNum9 | ✅ |
| TCLAYFLD_DEFNS_CD | TclayfldBPEOTclayfldDefnsCd | ✅ |
| TCLAYFLD_DEFNS_ID | TclayfldBPEOTclayfldDefnsId | ✅ |
| TCLAYFLD_DEFNS_INSTANCE_FLAG | TclayfldBPEOTclayfldDefInsFlag | ✅ |
| TCLAYFLD_TMPL_ID | TclayfldBPEOTclayfldTmplId | — |

### [[timecardlayoutcomppvo|TimecardLayoutCompPVO]] (GL · BICC: 6/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TclayfldBPEOCreatedBy | — |
| CREATION_DATE | TclayfldBPEOCreationDate | — |
| DISPLAY_SEQUENCE | TclayfldBPEODisplaySequence | ✅ |
| ENTERPRISE_ID | TclayfldBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TclayfldBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TclayfldBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TclayfldBPEOLastUpdatedBy | — |
| MODULE_ID | TclayfldBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TclayfldBPEOObjVersionNumber | — |
| P_TCLAYFLD_DEFNS_ID | TclayfldBPEOPTclayfldDefnsId | — |
| SEED_DATA_SOURCE | TclayfldBPEOSeedDataSource | — |
| SGUID | TclayfldBPEOSguid | — |
| TCLAY_ID | TclayfldBPEOTclayId | — |
| TCLAYFLD_ATTRIBUTE_CATEGORY | TclayfldBPEOTclayfldAtrbCat | — |
| TCLAYFLD_ATTRIBUTE_CHAR1 | TclayfldBPEOTclayfldAtrbChar1 | — |
| TCLAYFLD_ATTRIBUTE_CHAR10 | TclayfldBPEOTclayfldAtrbChar10 | — |
| TCLAYFLD_ATTRIBUTE_CHAR11 | TclayfldBPEOTclayfldAtrbChar11 | — |
| TCLAYFLD_ATTRIBUTE_CHAR12 | TclayfldBPEOTclayfldAtrbChar12 | — |
| TCLAYFLD_ATTRIBUTE_CHAR13 | TclayfldBPEOTclayfldAtrbChar13 | — |
| TCLAYFLD_ATTRIBUTE_CHAR14 | TclayfldBPEOTclayfldAtrbChar14 | — |
| TCLAYFLD_ATTRIBUTE_CHAR15 | TclayfldBPEOTclayfldAtrbChar15 | — |
| TCLAYFLD_ATTRIBUTE_CHAR16 | TclayfldBPEOTclayfldAtrbChar16 | — |
| TCLAYFLD_ATTRIBUTE_CHAR17 | TclayfldBPEOTclayfldAtrbChar17 | — |
| TCLAYFLD_ATTRIBUTE_CHAR18 | TclayfldBPEOTclayfldAtrbChar18 | — |
| TCLAYFLD_ATTRIBUTE_CHAR19 | TclayfldBPEOTclayfldAtrbChar19 | — |
| TCLAYFLD_ATTRIBUTE_CHAR2 | TclayfldBPEOTclayfldAtrbChar2 | — |
| TCLAYFLD_ATTRIBUTE_CHAR20 | TclayfldBPEOTclayfldAtrbChar20 | — |
| TCLAYFLD_ATTRIBUTE_CHAR21 | TclayfldBPEOTclayfldAtrbChar21 | — |
| TCLAYFLD_ATTRIBUTE_CHAR22 | TclayfldBPEOTclayfldAtrbChar22 | — |
| TCLAYFLD_ATTRIBUTE_CHAR23 | TclayfldBPEOTclayfldAtrbChar23 | — |
| TCLAYFLD_ATTRIBUTE_CHAR24 | TclayfldBPEOTclayfldAtrbChar24 | — |
| TCLAYFLD_ATTRIBUTE_CHAR25 | TclayfldBPEOTclayfldAtrbChar25 | — |
| TCLAYFLD_ATTRIBUTE_CHAR26 | TclayfldBPEOTclayfldAtrbChar26 | ✅ |
| TCLAYFLD_ATTRIBUTE_CHAR27 | TclayfldBPEOTclayfldAtrbChar27 | — |
| TCLAYFLD_ATTRIBUTE_CHAR28 | TclayfldBPEOTclayfldAtrbChar28 | — |
| TCLAYFLD_ATTRIBUTE_CHAR29 | TclayfldBPEOTclayfldAtrbChar29 | — |
| TCLAYFLD_ATTRIBUTE_CHAR3 | TclayfldBPEOTclayfldAtrbChar3 | — |
| TCLAYFLD_ATTRIBUTE_CHAR30 | TclayfldBPEOTclayfldAtrbChar30 | — |
| TCLAYFLD_ATTRIBUTE_CHAR4 | TclayfldBPEOTclayfldAtrbChar4 | — |
| TCLAYFLD_ATTRIBUTE_CHAR5 | TclayfldBPEOTclayfldAtrbChar5 | — |
| TCLAYFLD_ATTRIBUTE_CHAR6 | TclayfldBPEOTclayfldAtrbChar6 | — |
| TCLAYFLD_ATTRIBUTE_CHAR7 | TclayfldBPEOTclayfldAtrbChar7 | — |
| TCLAYFLD_ATTRIBUTE_CHAR8 | TclayfldBPEOTclayfldAtrbChar8 | — |
| TCLAYFLD_ATTRIBUTE_CHAR9 | TclayfldBPEOTclayfldAtrbChar9 | — |
| TCLAYFLD_ATTRIBUTE_DATE1 | TclayfldBPEOTclayfldAtrbDate1 | — |
| TCLAYFLD_ATTRIBUTE_DATE10 | TclayfldBPEOTclayfldAtrbDate10 | — |
| TCLAYFLD_ATTRIBUTE_DATE11 | TclayfldBPEOTclayfldAtrbDate11 | — |
| TCLAYFLD_ATTRIBUTE_DATE12 | TclayfldBPEOTclayfldAtrbDate12 | — |
| TCLAYFLD_ATTRIBUTE_DATE13 | TclayfldBPEOTclayfldAtrbDate13 | — |
| TCLAYFLD_ATTRIBUTE_DATE14 | TclayfldBPEOTclayfldAtrbDate14 | — |
| TCLAYFLD_ATTRIBUTE_DATE15 | TclayfldBPEOTclayfldAtrbDate15 | — |
| TCLAYFLD_ATTRIBUTE_DATE2 | TclayfldBPEOTclayfldAtrbDate2 | — |
| TCLAYFLD_ATTRIBUTE_DATE3 | TclayfldBPEOTclayfldAtrbDate3 | — |
| TCLAYFLD_ATTRIBUTE_DATE4 | TclayfldBPEOTclayfldAtrbDate4 | — |
| TCLAYFLD_ATTRIBUTE_DATE5 | TclayfldBPEOTclayfldAtrbDate5 | — |
| TCLAYFLD_ATTRIBUTE_DATE6 | TclayfldBPEOTclayfldAtrbDate6 | — |
| TCLAYFLD_ATTRIBUTE_DATE7 | TclayfldBPEOTclayfldAtrbDate7 | — |
| TCLAYFLD_ATTRIBUTE_DATE8 | TclayfldBPEOTclayfldAtrbDate8 | — |
| TCLAYFLD_ATTRIBUTE_DATE9 | TclayfldBPEOTclayfldAtrbDate9 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER1 | TclayfldBPEOTclayfldAtrbNum1 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER10 | TclayfldBPEOTclayfldAtrbNum10 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER11 | TclayfldBPEOTclayfldAtrbNum11 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER12 | TclayfldBPEOTclayfldAtrbNum12 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER13 | TclayfldBPEOTclayfldAtrbNum13 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER14 | TclayfldBPEOTclayfldAtrbNum14 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER15 | TclayfldBPEOTclayfldAtrbNum15 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER16 | TclayfldBPEOTclayfldAtrbNum16 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER17 | TclayfldBPEOTclayfldAtrbNum17 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER18 | TclayfldBPEOTclayfldAtrbNum18 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER19 | TclayfldBPEOTclayfldAtrbNum19 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER2 | TclayfldBPEOTclayfldAtrbNum2 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER20 | TclayfldBPEOTclayfldAtrbNum20 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER3 | TclayfldBPEOTclayfldAtrbNum3 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER4 | TclayfldBPEOTclayfldAtrbNum4 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER5 | TclayfldBPEOTclayfldAtrbNum5 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER6 | TclayfldBPEOTclayfldAtrbNum6 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER7 | TclayfldBPEOTclayfldAtrbNum7 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER8 | TclayfldBPEOTclayfldAtrbNum8 | — |
| TCLAYFLD_ATTRIBUTE_NUMBER9 | TclayfldBPEOTclayfldAtrbNum9 | — |
| TCLAYFLD_DEFNS_CD | TclayfldBPEOTclayfldDefnsCd | ✅ |
| TCLAYFLD_DEFNS_ID | TclayfldBPEOTclayfldDefnsId | ✅ |
| TCLAYFLD_DEFNS_INSTANCE_FLAG | TclayfldBPEOTclayfldDefInsFlag | — |
| TCLAYFLD_TMPL_ID | TclayfldBPEOTclayfldTmplId | ✅ |
