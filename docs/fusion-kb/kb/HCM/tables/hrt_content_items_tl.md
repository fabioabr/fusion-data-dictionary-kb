---
id: DOC-HCM-233
doc_type: system-doc
title: "HRT_CONTENT_ITEMS_TL — Itens de Conteudo de Perfil — Traducoes"
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
  - traducoes
  - nls
  - content-items
aliases:
  - HRT_CONTENT_ITEMS_TL
  - hrt_content_items_tl
  - hrt-content-items-tl
  - content-items-translations
  - itens-conteudo-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_ITEMS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_content_items_b]].

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Multi-idioma:** Nomes e descricoes traduzidos para multiplos idiomas.
- **Exibicao:** Textos traduzidos para interfaces de usuario e relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_content_items_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | CONTENT_ITEM_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | CONTENT_ITEM_DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_content_items_b]] — via `CONTENT_ITEM_ID` (registro base do item de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.CONTENT_ITEM_NAME, tl.CONTENT_ITEM_DESCRIPTION
FROM   HRT_CONTENT_ITEMS_TL tl
WHERE  tl.CONTENT_ITEM_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (CONTENT_ITEM_ID, LANGUAGE).
- JOIN com [[hrt_content_items_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_ITEMS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontentitemstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[certificationcontentitempvo|CertificationContentItemPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[certificationpvo|CertificationPVO]] (HCM · BICC: 3/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EstlBusinessGroupId1 | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| CONTENT_ITEM_ID | EstlContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRIPTION | ESTLItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_DESCRLONG | ESTLItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | EstlLanguage1 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| NAME | ESTCITLEduEstablishmentName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[competencycontentitempvo|CompetencyContentItemPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[competencycontentitemratingpvo|CompetencyContentItemRatingPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[competencyitempvo|CompetencyItemPVO]] (HCM · BICC: 5/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | ✅ |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[contentitemlangpvo|ContentItemLangPVO]] (HCM · BICC: 2/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[contentitempvo|ContentItemPVO]] (HCM · BICC: 7/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | ✅ |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | ✅ |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | ✅ |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[contentitemtranslationpvo|ContentItemTranslationPVO]] (HCM · BICC: 28/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CONTENT_ITEM_ID | ContentItemId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ITEM_DESCRIPTION | ItemDescription | ✅ |
| ITEM_DESCRLONG | ItemDescrlong | ✅ |
| ITEM_TEXT_TL_1 | ItemTextTl1 | ✅ |
| ITEM_TEXT_TL_10 | ItemTextTl10 | ✅ |
| ITEM_TEXT_TL_11 | ItemTextTl11 | ✅ |
| ITEM_TEXT_TL_12 | ItemTextTl12 | ✅ |
| ITEM_TEXT_TL_13 | ItemTextTl13 | ✅ |
| ITEM_TEXT_TL_14 | ItemTextTl14 | ✅ |
| ITEM_TEXT_TL_15 | ItemTextTl15 | ✅ |
| ITEM_TEXT_TL_2 | ItemTextTl2 | ✅ |
| ITEM_TEXT_TL_3 | ItemTextTl3 | ✅ |
| ITEM_TEXT_TL_4 | ItemTextTl4 | ✅ |
| ITEM_TEXT_TL_5 | ItemTextTl5 | ✅ |
| ITEM_TEXT_TL_6 | ItemTextTl6 | ✅ |
| ITEM_TEXT_TL_7 | ItemTextTl7 | ✅ |
| ITEM_TEXT_TL_8 | ItemTextTl8 | ✅ |
| ITEM_TEXT_TL_9 | ItemTextTl9 | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[contentitemvaluepvo|ContentItemValuePVO]] (HCM · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| CREATED_BY | ContentItemTranslationPEOCreatedBy | — |
| CREATION_DATE | ContentItemTranslationPEOCreationDate | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContentItemTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContentItemTranslationPEOLastUpdatedBy | — |
| NAME | ContentItemTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | ContentItemTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | ContentItemTranslationPEOSourceLang | — |

### [[degreecontentitempvo|DegreeContentItemPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[degreepvo|DegreePVO]] (HCM · BICC: 5/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | ESTTLBusinessGroupId5 | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| CONTENT_ITEM_ID | ESTTLContentItemId1 | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | ✅ |
| ITEM_DESCRIPTION | ESTLItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_DESCRLONG | ESTTLItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | ESTTLLanguage4 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| NAME | ESTCITLSchoolName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[honorcontentitempvo|HonorContentItemPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[honorpvo|HonorPVO]] (HCM · BICC: 3/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CITLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EstlBusinessGroupId1 | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| CONTENT_ITEM_ID | EstlContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRIPTION | ESTLItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_DESCRLONG | ESTLItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | EstlLanguage1 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | — |
| NAME | ESTCITLEduEstablishmentName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[languagecontentitempvo|LanguageContentItemPVO]] (HCM · BICC: 4/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | ✅ |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[membershipcontentitempvo|MembershipContentItemPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[membershippvo|MembershipPVO]] (HCM · BICC: 4/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | EstlBusinessGroupId1 | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| CONTENT_ITEM_ID | EstlContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRIPTION | ESTLItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_DESCRLONG | ESTLItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | EstlLanguage1 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| NAME | ESTCITLEduEstablishmentName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[readingratinglevelpvo|ReadingRatingLevelPVO]] (HCM · BICC: 1/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | — |
| SOURCE_LANG | SourceLang | — |

### [[speakingratinglevelpvo|SpeakingRatingLevelPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |
| SOURCE_LANG | SourceLang | — |

### [[specialprojectpvo|SpecialProjectPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CTL_BusinessGroupId1 | — |
| CONTENT_ITEM_ID | CTL_ContentItemId | — |
| LANGUAGE | CTL_Language | — |
| LAST_UPDATE_DATE | CTL_LastUpdateDate1 | ✅ |
| NAME | ContentItemTranslationPEOName | ✅ |

### [[writingratinglevelpvo|WritingRatingLevelPVO]] (HCM · BICC: 1/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ContentItemTranslationPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ContentItemTranslationPEOContentItemId | — |
| ITEM_DESCRIPTION | ContentItemTranslationPEOItemDescription | — |
| ITEM_DESCRLONG | ContentItemTranslationPEOItemDescrlong | — |
| ITEM_TEXT_TL_1 | ItemTextTl1 | — |
| ITEM_TEXT_TL_10 | ItemTextTl10 | — |
| ITEM_TEXT_TL_11 | ItemTextTl11 | — |
| ITEM_TEXT_TL_12 | ItemTextTl12 | — |
| ITEM_TEXT_TL_13 | ItemTextTl13 | — |
| ITEM_TEXT_TL_14 | ItemTextTl14 | — |
| ITEM_TEXT_TL_15 | ItemTextTl15 | — |
| ITEM_TEXT_TL_2 | ItemTextTl2 | — |
| ITEM_TEXT_TL_3 | ItemTextTl3 | — |
| ITEM_TEXT_TL_4 | ItemTextTl4 | — |
| ITEM_TEXT_TL_5 | ItemTextTl5 | — |
| ITEM_TEXT_TL_6 | ItemTextTl6 | — |
| ITEM_TEXT_TL_7 | ItemTextTl7 | — |
| ITEM_TEXT_TL_8 | ItemTextTl8 | — |
| ITEM_TEXT_TL_9 | ItemTextTl9 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | ContentItemTranslationPEOLastUpdateDate | ✅ |
| NAME | ContentItemTranslationPEOName | — |
| SOURCE_LANG | SourceLang | — |
