---
id: DOC-HCM-218
doc_type: system-doc
title: "HRT_BI_CAREER_PRF_ITEMS_V — Itens de Preferência de Carreira — BI View"
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
  - talent-profile
  - bi
  - career-preferences
aliases:
  - HRT_BI_CAREER_PRF_ITEMS_V
  - hrt_bi_career_prf_items_v
  - itens-de-preferência-de-carreirabi-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_CAREER_PRF_ITEMS_V

## 📌 Visão Geral

View de BI com itens de **preferência de carreira** do perfil de talento.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Talent Analytics:** Preferências de mobilidade.
- **Perfil de talento:** Preferências declaradas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAREER_PRF_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | PREFERENCE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de preferência | — | 🟡 70% |
| 4 | PREFERENCE_VALUE | VARCHAR2(240) | NULL | Dados | Valor da preferência | — | 🟡 65% |
| 5 | EFFECTIVE_DATE | DATE | NULL | Data | Data efetiva | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (preferencias de carreira do colaborador)

### Tabelas relacionadas
- Demais views HRT_BI_* do perfil de talento

---

## 📎 Uso Típico

### Itens por colaborador
```sql
SELECT * FROM HRT_BI_CAREER_PRF_ITEMS_V WHERE PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- View de BI (sufixo `_V`) — otimizada para relatórios.
- Parte do conjunto HRT_BI_* do Talent Profile.
- Utilizada pelo Oracle Transactional BI (OTBI).

---

## 🔗 PVOs Relacionados

### [[careerpreferencepvo|CareerPreferencePVO]] (HCM · BICC: 14/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileItemPEOBusinessGroupId | ✅ |
| CONTENT_ITEM_ID | ProfileItemPEOContentItemId | — |
| CONTENT_TYPE_ID | ProfileItemPEOContentTypeId | ✅ |
| CONTEXT_NAME | CareerPrefProfileItemPEOContextName | — |
| COUNTRY_ID | ProfileItemPEOCountryId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ProfileItemPEODateFrom | ✅ |
| DATE_TO | ProfileItemPEODateTo | ✅ |
| IMPORTANCE | Importance | — |
| INTEREST_LEVEL | InterestLevel | — |
| ITEM_CLOB_1 | CareerPrefPIPEOItemClob1 | — |
| ITEM_CLOB_2 | CareerPrefPIPEOItemClob2 | — |
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
| ITEM_DECIMAL_1 | ItemDecimal1 | — |
| ITEM_DECIMAL_2 | ItemDecimal2 | — |
| ITEM_DECIMAL_3 | ItemDecimal3 | — |
| ITEM_DECIMAL_4 | ItemDecimal4 | — |
| ITEM_DECIMAL_5 | ItemDecimal5 | — |
| ITEM_NUMBER_1 | ProfileItemPEOItemNumber1 | — |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ProfileItemPEOItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | ✅ |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT2000_1 | ItemText20001 | ✅ |
| ITEM_TEXT2000_2 | ItemText20002 | ✅ |
| ITEM_TEXT2000_3 | CareerPrefPIPEOItemText20003 | ✅ |
| ITEM_TEXT2000_3 | ItemText20003 | — |
| ITEM_TEXT2000_4 | CareerPrefPIPEOItemText20004 | ✅ |
| ITEM_TEXT2000_4 | ItemText20004 | — |
| ITEM_TEXT2000_5 | ItemText20005 | — |
| ITEM_TEXT240_1 | ItemText2401 | — |
| ITEM_TEXT240_10 | ItemText24010 | — |
| ITEM_TEXT240_11 | ItemText24011 | — |
| ITEM_TEXT240_12 | ItemText24012 | — |
| ITEM_TEXT240_13 | ItemText24013 | — |
| ITEM_TEXT240_14 | ItemText24014 | — |
| ITEM_TEXT240_15 | ItemText24015 | — |
| ITEM_TEXT240_2 | ItemText2402 | — |
| ITEM_TEXT240_3 | ItemText2403 | — |
| ITEM_TEXT240_4 | ItemText2404 | — |
| ITEM_TEXT240_5 | ItemText2405 | — |
| ITEM_TEXT240_6 | ItemText2406 | — |
| ITEM_TEXT240_7 | ItemText2407 | — |
| ITEM_TEXT240_8 | ItemText2408 | — |
| ITEM_TEXT240_9 | ItemText2409 | — |
| ITEM_TEXT30_1 | ItemText301 | ✅ |
| ITEM_TEXT30_10 | ItemText3010 | — |
| ITEM_TEXT30_11 | ItemText3011 | — |
| ITEM_TEXT30_12 | ItemText3012 | — |
| ITEM_TEXT30_13 | ItemText3013 | — |
| ITEM_TEXT30_14 | ItemText3014 | — |
| ITEM_TEXT30_15 | ItemText3015 | — |
| ITEM_TEXT30_2 | ItemText302 | ✅ |
| ITEM_TEXT30_3 | ItemText303 | ✅ |
| ITEM_TEXT30_4 | ItemText304 | — |
| ITEM_TEXT30_5 | ItemText305 | — |
| ITEM_TEXT30_6 | ItemText306 | — |
| ITEM_TEXT30_7 | ItemText307 | — |
| ITEM_TEXT30_8 | ItemText308 | — |
| ITEM_TEXT30_9 | ItemText309 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MANDATORY | Mandatory | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_PROFILE_ITEM_ID | ProfileItemPEOParentProfileItemId | — |
| PROFILE_ID | ProfileItemPEOProfileId | — |
| PROFILE_ITEM_ID | ProfileItemPEOProfileItemId | ✅ |
| QUALIFIER_ID1 | QualifierId1 | — |
| QUALIFIER_ID2 | QualifierId2 | — |
| RATING_LEVEL_ID1 | RatingLevelId1 | — |
| RATING_LEVEL_ID2 | RatingLevelId2 | — |
| RATING_LEVEL_ID3 | RatingLevelId3 | — |
| RATING_MODEL_ID1 | RatingModelId1 | — |
| RATING_MODEL_ID2 | RatingModelId2 | — |
| RATING_MODEL_ID3 | RatingModelId3 | — |
| SECTION_ID | CareerPrefPIPEOSectionId | — |
| SOURCE_ID | SourceId | — |
| SOURCE_KEY1 | SourceKey1 | — |
| SOURCE_KEY2 | SourceKey2 | — |
| SOURCE_KEY3 | SourceKey3 | — |
| SOURCE_TYPE | SourceType | — |
| STATE_PROVINCE_ID | ProfileItemPEOStateProvinceId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
