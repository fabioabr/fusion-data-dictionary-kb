---
id: DOC-HCM-232
doc_type: system-doc
title: "HRT_CONTENT_ITEMS_B — Itens de Conteudo de Perfil — Base"
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
  - content-items
  - competencias
  - talent
aliases:
  - HRT_CONTENT_ITEMS_B
  - hrt_content_items_b
  - hrt-content-items-b
  - content-items-base
  - itens-conteudo-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_ITEMS_B

## 📌 Visao Geral

Tabela base que armazena os **itens de conteudo** disponiveis para associacao a perfis de talento — competencias, habilidades, certificacoes, graus academicos, idiomas e outros conteudos configuraveis.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Catalogo de conteudos:** Repositorio centralizado de competencias, habilidades e qualificacoes.
- **Perfis de talento:** Itens associaveis a perfis de pessoa ou cargo via HRT_PROFILE_ITEMS.
- **Matching:** Base para comparacao de perfis (gap analysis) em talent management.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do item de conteudo | — | 🟢 100% |
| 2 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo ao qual pertence | [[hrt_content_types_b]] | 🟢 100% |
| 3 | ITEM_KEY | VARCHAR2(30) | NULL | Identificacao | Chave natural do item | — | 🟢 90% |
| 4 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 5 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 6 | ITEM_TEXT_240 | VARCHAR2(240) | NULL | Dados | Texto livre associado ao item | — | 🟡 75% |
| 7 | ITEM_NUMBER_1 | NUMBER | NULL | Dados | Valor numerico generico 1 | — | 🟡 70% |
| 8 | ITEM_DATE_1 | DATE | NULL | Dados | Data generica 1 | — | 🟡 70% |
| 9 | COUNTRY_ID | NUMBER(18) | NULL | FK | Pais associado ao item | — | 🟡 70% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- [[hrt_content_items_tl]] — via `CONTENT_ITEM_ID` (traducoes do item de conteudo)
- [[hrt_profile_items]] — via `CONTENT_ITEM_ID` (itens associados a perfis)

---

## 📎 Uso Tipico

### Itens de conteudo por tipo
```sql
SELECT ci.CONTENT_ITEM_ID, ci.CONTENT_TYPE_ID,
       ci.DATE_FROM, ci.DATE_TO
FROM   HRT_CONTENT_ITEMS_B ci
WHERE  ci.CONTENT_TYPE_ID = :p_content_type_id
  AND  SYSDATE BETWEEN ci.DATE_FROM AND NVL(ci.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base (sem traducao) — textos traduzidos ficam em [[hrt_content_items_tl]].
- Campos genericos (ITEM_TEXT_240, ITEM_NUMBER_1, ITEM_DATE_1) sao usados conforme configuracao do content type.
- O `OBJECT_VERSION_NUMBER` implementa controle de concorrencia otimista.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_ITEMS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontentitemsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[certificationcontentitempvo|CertificationContentItemPVO]] (HCM · BICC: 4/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[certificationpvo|CertificationPVO]] (HCM · BICC: 1/64)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EstIdBusinessGroupId1 | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_CODE | EstIdContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | — |
| CONTENT_ITEM_ID | EstIdContentItemId | — |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ContentItemBPEOItemDate1 | — |
| ITEM_DATE_10 | ContentItemBPEOItemDate10 | — |
| ITEM_DATE_2 | ContentItemBPEOItemDate2 | — |
| ITEM_DATE_3 | ContentItemBPEOItemDate3 | — |
| ITEM_DATE_4 | ContentItemBPEOItemDate4 | — |
| ITEM_DATE_5 | ContentItemBPEOItemDate5 | — |
| ITEM_DATE_6 | ContentItemBPEOItemDate6 | — |
| ITEM_DATE_7 | ContentItemBPEOItemDate7 | — |
| ITEM_DATE_8 | ContentItemBPEOItemDate8 | — |
| ITEM_DATE_9 | ContentItemBPEOItemDate9 | — |
| ITEM_NUMBER_1 | ContentItemBPEOItemNumber1 | — |
| ITEM_NUMBER_10 | ContentItemBPEOItemNumber10 | — |
| ITEM_NUMBER_2 | ContentItemBPEOItemNumber2 | — |
| ITEM_NUMBER_3 | ContentItemBPEOItemNumber3 | — |
| ITEM_NUMBER_4 | ContentItemBPEOItemNumber4 | — |
| ITEM_NUMBER_5 | ContentItemBPEOItemNumber5 | — |
| ITEM_NUMBER_6 | ContentItemBPEOItemNumber6 | — |
| ITEM_NUMBER_7 | ContentItemBPEOItemNumber7 | — |
| ITEM_NUMBER_8 | ContentItemBPEOItemNumber8 | — |
| ITEM_NUMBER_9 | ContentItemBPEOItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |
| RATING_MODEL_ID | EstIdRatingModelId | — |

### [[competencycontentitempvo|CompetencyContentItemPVO]] (HCM · BICC: 4/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentItemBPEOContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentItemBPEOContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[competencycontentitemratingpvo|CompetencyContentItemRatingPVO]] (HCM · BICC: 3/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentItemBPEOContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[competencyitempvo|CompetencyItemPVO]] (HCM · BICC: 5/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentItemBPEOContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentItemBPEOContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | ✅ |
| DATE_TO | ContentItemBPEODateTo | ✅ |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[contentitemlangpvo|ContentItemLangPVO]] (HCM · BICC: 3/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[contentitempvo|ContentItemPVO]] (HCM · BICC: 15/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | ✅ |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | ✅ |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | ContentItemBPEODateFrom | ✅ |
| DATE_TO | ContentItemBPEODateTo | ✅ |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | ✅ |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | ✅ |

### [[contentitemvaluepvo|ContentItemValuePVO]] (HCM · BICC: 7/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | ContentItemBPEOAttributeCategory | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | ✅ |
| CONTENT_ITEM_ID | ContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentItemBPEOContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentItemBPEOContentSupplierCode | ✅ |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | ContentItemBPEOCreatedBy | — |
| CREATION_DATE | ContentItemBPEOCreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContentItemBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContentItemBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ContentItemBPEOObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | ✅ |

### [[degreecontentitempvo|DegreeContentItemPVO]] (HCM · BICC: 4/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[degreepvo|DegreePVO]] (HCM · BICC: 3/62)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | ESTBusinessGroupId4 | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_ITEM_ID | ESTContentItemId | — |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ContentItemBPEOItemDate1 | — |
| ITEM_DATE_10 | ContentItemBPEOItemDate10 | — |
| ITEM_DATE_2 | ContentItemBPEOItemDate2 | — |
| ITEM_DATE_3 | ContentItemBPEOItemDate3 | — |
| ITEM_DATE_4 | ContentItemBPEOItemDate4 | — |
| ITEM_DATE_5 | ContentItemBPEOItemDate5 | — |
| ITEM_DATE_6 | ContentItemBPEOItemDate6 | — |
| ITEM_DATE_7 | ContentItemBPEOItemDate7 | — |
| ITEM_DATE_8 | ContentItemBPEOItemDate8 | — |
| ITEM_DATE_9 | ContentItemBPEOItemDate9 | — |
| ITEM_NUMBER_1 | ContentItemBPEOItemNumber1 | — |
| ITEM_NUMBER_10 | ContentItemBPEOItemNumber10 | — |
| ITEM_NUMBER_2 | ContentItemBPEOItemNumber2 | — |
| ITEM_NUMBER_3 | ContentItemBPEOItemNumber3 | — |
| ITEM_NUMBER_4 | ContentItemBPEOItemNumber4 | — |
| ITEM_NUMBER_5 | ContentItemBPEOItemNumber5 | — |
| ITEM_NUMBER_6 | ContentItemBPEOItemNumber6 | — |
| ITEM_NUMBER_7 | ContentItemBPEOItemNumber7 | — |
| ITEM_NUMBER_8 | ContentItemBPEOItemNumber8 | — |
| ITEM_NUMBER_9 | ContentItemBPEOItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[goaltargetoutcomeprofilespvo|GoalTargetOutcomeProfilesPVO]] (HCM · BICC: 5/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId1 | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | ✅ |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_SUPPLIER_CODE | ContentItemBPEOContentSupplierCode | ✅ |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId1 | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | ✅ |
| STATE_PROVINCE_ID | ContentItemBPEOStateProvinceId1 | — |

### [[honorcontentitempvo|HonorContentItemPVO]] (HCM · BICC: 5/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | ✅ |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[honorpvo|HonorPVO]] (HCM · BICC: 1/64)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EstIdBusinessGroupId1 | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_CODE | EstIdContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | — |
| CONTENT_ITEM_ID | EstIdContentItemId | — |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ContentItemBPEOItemDate1 | — |
| ITEM_DATE_10 | ContentItemBPEOItemDate10 | — |
| ITEM_DATE_2 | ContentItemBPEOItemDate2 | — |
| ITEM_DATE_3 | ContentItemBPEOItemDate3 | — |
| ITEM_DATE_4 | ContentItemBPEOItemDate4 | — |
| ITEM_DATE_5 | ContentItemBPEOItemDate5 | — |
| ITEM_DATE_6 | ContentItemBPEOItemDate6 | — |
| ITEM_DATE_7 | ContentItemBPEOItemDate7 | — |
| ITEM_DATE_8 | ContentItemBPEOItemDate8 | — |
| ITEM_DATE_9 | ContentItemBPEOItemDate9 | — |
| ITEM_NUMBER_1 | ContentItemBPEOItemNumber1 | — |
| ITEM_NUMBER_10 | ContentItemBPEOItemNumber10 | — |
| ITEM_NUMBER_2 | ContentItemBPEOItemNumber2 | — |
| ITEM_NUMBER_3 | ContentItemBPEOItemNumber3 | — |
| ITEM_NUMBER_4 | ContentItemBPEOItemNumber4 | — |
| ITEM_NUMBER_5 | ContentItemBPEOItemNumber5 | — |
| ITEM_NUMBER_6 | ContentItemBPEOItemNumber6 | — |
| ITEM_NUMBER_7 | ContentItemBPEOItemNumber7 | — |
| ITEM_NUMBER_8 | ContentItemBPEOItemNumber8 | — |
| ITEM_NUMBER_9 | ContentItemBPEOItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |
| RATING_MODEL_ID | EstIdRatingModelId | — |

### [[languagecontentitempvo|LanguageContentItemPVO]] (HCM · BICC: 3/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[membershipcontentitempvo|MembershipContentItemPVO]] (HCM · BICC: 4/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentItemBPEOContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[membershippvo|MembershipPVO]] (HCM · BICC: 1/64)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EstIdBusinessGroupId1 | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_CODE | EstIdContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | — |
| CONTENT_ITEM_ID | EstIdContentItemId | — |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ContentItemBPEOItemDate1 | — |
| ITEM_DATE_10 | ContentItemBPEOItemDate10 | — |
| ITEM_DATE_2 | ContentItemBPEOItemDate2 | — |
| ITEM_DATE_3 | ContentItemBPEOItemDate3 | — |
| ITEM_DATE_4 | ContentItemBPEOItemDate4 | — |
| ITEM_DATE_5 | ContentItemBPEOItemDate5 | — |
| ITEM_DATE_6 | ContentItemBPEOItemDate6 | — |
| ITEM_DATE_7 | ContentItemBPEOItemDate7 | — |
| ITEM_DATE_8 | ContentItemBPEOItemDate8 | — |
| ITEM_DATE_9 | ContentItemBPEOItemDate9 | — |
| ITEM_NUMBER_1 | ContentItemBPEOItemNumber1 | — |
| ITEM_NUMBER_10 | ContentItemBPEOItemNumber10 | — |
| ITEM_NUMBER_2 | ContentItemBPEOItemNumber2 | — |
| ITEM_NUMBER_3 | ContentItemBPEOItemNumber3 | — |
| ITEM_NUMBER_4 | ContentItemBPEOItemNumber4 | — |
| ITEM_NUMBER_5 | ContentItemBPEOItemNumber5 | — |
| ITEM_NUMBER_6 | ContentItemBPEOItemNumber6 | — |
| ITEM_NUMBER_7 | ContentItemBPEOItemNumber7 | — |
| ITEM_NUMBER_8 | ContentItemBPEOItemNumber8 | — |
| ITEM_NUMBER_9 | ContentItemBPEOItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |
| RATING_MODEL_ID | EstIdRatingModelId | — |

### [[nboxdimensionpvo|NBoxDimensionPVO]] (HCM · BICC: 3/134)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | ContentItemBPEOAttribute1 | — |
| ATTRIBUTE10 | ContentItemBPEOAttribute10 | — |
| ATTRIBUTE11 | ContentItemBPEOAttribute11 | — |
| ATTRIBUTE12 | ContentItemBPEOAttribute12 | — |
| ATTRIBUTE13 | ContentItemBPEOAttribute13 | — |
| ATTRIBUTE14 | ContentItemBPEOAttribute14 | — |
| ATTRIBUTE15 | ContentItemBPEOAttribute15 | — |
| ATTRIBUTE16 | ContentItemBPEOAttribute16 | — |
| ATTRIBUTE17 | ContentItemBPEOAttribute17 | — |
| ATTRIBUTE18 | ContentItemBPEOAttribute18 | — |
| ATTRIBUTE19 | ContentItemBPEOAttribute19 | — |
| ATTRIBUTE2 | ContentItemBPEOAttribute2 | — |
| ATTRIBUTE20 | ContentItemBPEOAttribute20 | — |
| ATTRIBUTE21 | ContentItemBPEOAttribute21 | — |
| ATTRIBUTE22 | ContentItemBPEOAttribute22 | — |
| ATTRIBUTE23 | ContentItemBPEOAttribute23 | — |
| ATTRIBUTE24 | ContentItemBPEOAttribute24 | — |
| ATTRIBUTE25 | ContentItemBPEOAttribute25 | — |
| ATTRIBUTE26 | ContentItemBPEOAttribute26 | — |
| ATTRIBUTE27 | ContentItemBPEOAttribute27 | — |
| ATTRIBUTE28 | ContentItemBPEOAttribute28 | — |
| ATTRIBUTE29 | ContentItemBPEOAttribute29 | — |
| ATTRIBUTE3 | ContentItemBPEOAttribute3 | — |
| ATTRIBUTE30 | ContentItemBPEOAttribute30 | — |
| ATTRIBUTE4 | ContentItemBPEOAttribute4 | — |
| ATTRIBUTE5 | ContentItemBPEOAttribute5 | — |
| ATTRIBUTE6 | ContentItemBPEOAttribute6 | — |
| ATTRIBUTE7 | ContentItemBPEOAttribute7 | — |
| ATTRIBUTE8 | ContentItemBPEOAttribute8 | — |
| ATTRIBUTE9 | ContentItemBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | ContentItemBPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | ContentItemBPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | ContentItemBPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | ContentItemBPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | ContentItemBPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | ContentItemBPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | ContentItemBPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | ContentItemBPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | ContentItemBPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ContentItemBPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ContentItemBPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ContentItemBPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | ContentItemBPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | ContentItemBPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | ContentItemBPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | ContentItemBPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | ContentItemBPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | ContentItemBPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | ContentItemBPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | ContentItemBPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | ContentItemBPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | ContentItemBPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | ContentItemBPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | ContentItemBPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | ContentItemBPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | ContentItemBPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | ContentItemBPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | ContentItemBPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | ContentItemBPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | ContentItemBPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ContentItemBPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ContentItemBPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | ContentItemBPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | ContentItemBPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | ContentItemBPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | ContentItemBPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentItemBPEOContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentItemBPEOContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| COUNTRY_ID | ContentItemBPEOCountryId | — |
| CREATED_BY | ContentItemBPEOCreatedBy | — |
| CREATION_DATE | ContentItemBPEOCreationDate | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ContentItemBPEOItemDate1 | — |
| ITEM_DATE_10 | ContentItemBPEOItemDate10 | — |
| ITEM_DATE_2 | ContentItemBPEOItemDate2 | — |
| ITEM_DATE_3 | ContentItemBPEOItemDate3 | — |
| ITEM_DATE_4 | ContentItemBPEOItemDate4 | — |
| ITEM_DATE_5 | ContentItemBPEOItemDate5 | — |
| ITEM_DATE_6 | ContentItemBPEOItemDate6 | — |
| ITEM_DATE_7 | ContentItemBPEOItemDate7 | — |
| ITEM_DATE_8 | ContentItemBPEOItemDate8 | — |
| ITEM_DATE_9 | ContentItemBPEOItemDate9 | — |
| ITEM_NUMBER_1 | ContentItemBPEOItemNumber1 | — |
| ITEM_NUMBER_10 | ContentItemBPEOItemNumber10 | — |
| ITEM_NUMBER_2 | ContentItemBPEOItemNumber2 | — |
| ITEM_NUMBER_3 | ContentItemBPEOItemNumber3 | — |
| ITEM_NUMBER_4 | ContentItemBPEOItemNumber4 | — |
| ITEM_NUMBER_5 | ContentItemBPEOItemNumber5 | — |
| ITEM_NUMBER_6 | ContentItemBPEOItemNumber6 | — |
| ITEM_NUMBER_7 | ContentItemBPEOItemNumber7 | — |
| ITEM_NUMBER_8 | ContentItemBPEOItemNumber8 | — |
| ITEM_NUMBER_9 | ContentItemBPEOItemNumber9 | — |
| ITEM_TEXT_1 | ContentItemBPEOItemText1 | — |
| ITEM_TEXT_10 | ContentItemBPEOItemText10 | — |
| ITEM_TEXT_11 | ContentItemBPEOItemText11 | — |
| ITEM_TEXT_12 | ContentItemBPEOItemText12 | — |
| ITEM_TEXT_13 | ContentItemBPEOItemText13 | — |
| ITEM_TEXT_14 | ContentItemBPEOItemText14 | — |
| ITEM_TEXT_15 | ContentItemBPEOItemText15 | — |
| ITEM_TEXT_16 | ContentItemBPEOItemText16 | — |
| ITEM_TEXT_17 | ContentItemBPEOItemText17 | — |
| ITEM_TEXT_18 | ContentItemBPEOItemText18 | — |
| ITEM_TEXT_19 | ContentItemBPEOItemText19 | — |
| ITEM_TEXT_2 | ContentItemBPEOItemText2 | — |
| ITEM_TEXT_20 | ContentItemBPEOItemText20 | — |
| ITEM_TEXT_21 | ContentItemBPEOItemText21 | — |
| ITEM_TEXT_22 | ContentItemBPEOItemText22 | — |
| ITEM_TEXT_23 | ContentItemBPEOItemText23 | — |
| ITEM_TEXT_24 | ContentItemBPEOItemText24 | — |
| ITEM_TEXT_25 | ContentItemBPEOItemText25 | — |
| ITEM_TEXT_26 | ContentItemBPEOItemText26 | — |
| ITEM_TEXT_27 | ContentItemBPEOItemText27 | — |
| ITEM_TEXT_28 | ContentItemBPEOItemText28 | — |
| ITEM_TEXT_29 | ContentItemBPEOItemText29 | — |
| ITEM_TEXT_3 | ContentItemBPEOItemText3 | — |
| ITEM_TEXT_30 | ContentItemBPEOItemText30 | — |
| ITEM_TEXT_4 | ContentItemBPEOItemText4 | — |
| ITEM_TEXT_5 | ContentItemBPEOItemText5 | — |
| ITEM_TEXT_6 | ContentItemBPEOItemText6 | — |
| ITEM_TEXT_7 | ContentItemBPEOItemText7 | — |
| ITEM_TEXT_8 | ContentItemBPEOItemText8 | — |
| ITEM_TEXT_9 | ContentItemBPEOItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContentItemBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContentItemBPEOLastUpdatedBy | — |
| MODULE_ID | ContentItemBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | ContentItemBPEOObjectVersionNumber | — |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |
| STATE_PROVINCE_ID | ContentItemBPEOStateProvinceId | — |

### [[performancepotentialboxsequencepvo|PerformancePotentialBoxSequencePVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentTypeBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentTypeBPEOContentItemId | ✅ |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |

### [[performancepotentialboxsequencepvo_viewall|PerformancePotentialBoxSequencePVO_Viewall]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentTypeBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentTypeBPEOContentItemId | ✅ |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |

### [[readingratinglevelpvo|ReadingRatingLevelPVO]] (HCM · BICC: 2/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[speakingratinglevelpvo|SpeakingRatingLevelPVO]] (HCM · BICC: 2/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |

### [[specialprojectpvo|SpecialProjectPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CIBPEOBusinessGroupId1 | — |
| CONTENT_ITEM_CODE | CIBPEOContentItemCode | — |
| CONTENT_ITEM_ID | CIBPEOContentItemId | — |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentTypeId | — |
| CREATED_BY | CreatedBy1 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |

### [[talentscoreboxsequencepvo|TalentScoreBoxSequencePVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentTypeBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentTypeBPEOContentItemId | ✅ |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | — |

### [[talentscoreboxsequencepvo_viewall|TalentScoreBoxSequencePVO_Viewall]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentTypeBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentTypeBPEOContentItemId | ✅ |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | — |

### [[writingratinglevelpvo|WritingRatingLevelPVO]] (HCM · BICC: 2/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemBPEOBusinessGroupId | — |
| CONTENT_ITEM_CODE | ContentItemBPEOContentItemCode | — |
| CONTENT_ITEM_ID | ContentItemBPEOContentItemId | ✅ |
| CONTENT_KEYFLEX_ID | ContentKeyflexId | — |
| CONTENT_SUPPLIER_CODE | ContentSupplierCode | — |
| CONTENT_TYPE_ID | ContentItemBPEOContentTypeId | — |
| DATE_FROM | ContentItemBPEODateFrom | — |
| DATE_TO | ContentItemBPEODateTo | — |
| ITEM_DATE_1 | ItemDate1 | — |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT_1 | ItemText1 | — |
| ITEM_TEXT_10 | ItemText10 | — |
| ITEM_TEXT_11 | ItemText11 | — |
| ITEM_TEXT_12 | ItemText12 | — |
| ITEM_TEXT_13 | ItemText13 | — |
| ITEM_TEXT_14 | ItemText14 | — |
| ITEM_TEXT_15 | ItemText15 | — |
| ITEM_TEXT_16 | ItemText16 | — |
| ITEM_TEXT_17 | ItemText17 | — |
| ITEM_TEXT_18 | ItemText18 | — |
| ITEM_TEXT_19 | ItemText19 | — |
| ITEM_TEXT_2 | ItemText2 | — |
| ITEM_TEXT_20 | ItemText20 | — |
| ITEM_TEXT_21 | ItemText21 | — |
| ITEM_TEXT_22 | ItemText22 | — |
| ITEM_TEXT_23 | ItemText23 | — |
| ITEM_TEXT_24 | ItemText24 | — |
| ITEM_TEXT_25 | ItemText25 | — |
| ITEM_TEXT_26 | ItemText26 | — |
| ITEM_TEXT_27 | ItemText27 | — |
| ITEM_TEXT_28 | ItemText28 | — |
| ITEM_TEXT_29 | ItemText29 | — |
| ITEM_TEXT_3 | ItemText3 | — |
| ITEM_TEXT_30 | ItemText30 | — |
| ITEM_TEXT_4 | ItemText4 | — |
| ITEM_TEXT_5 | ItemText5 | — |
| ITEM_TEXT_6 | ItemText6 | — |
| ITEM_TEXT_7 | ItemText7 | — |
| ITEM_TEXT_8 | ItemText8 | — |
| ITEM_TEXT_9 | ItemText9 | — |
| LAST_UPDATE_DATE | ContentItemBPEOLastUpdateDate | ✅ |
| RATING_MODEL_ID | ContentItemBPEORatingModelId | — |
