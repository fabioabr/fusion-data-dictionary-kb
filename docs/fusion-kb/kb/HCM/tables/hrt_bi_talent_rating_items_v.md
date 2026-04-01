---
id: DOC-HCM-230
doc_type: system-doc
title: "HRT_BI_TALENT_RATING_ITEMS_V — Itens de Rating de Talento (BI View)"
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
  - bi-view
  - talent-rating
  - potencial
  - 9-box
aliases:
  - HRT_BI_TALENT_RATING_ITEMS_V
  - hrt_bi_talent_rating_items_v
  - hrt-bi-talent-rating-items-v
  - talent-rating-bi
  - rating-talento-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_TALENT_RATING_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **ratings de talento** (potencial) dos colaboradores. Complementa o rating de desempenho para compor a matriz 9-box (desempenho x potencial).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Review:** Construcao da matriz 9-box combinando performance e potencial.
- **Sucessao:** Identificacao de colaboradores de alto potencial (HiPo).
- **BI/Analytics:** Dashboards de distribuicao de talentos.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do item de conteudo | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de talento associado | [[hrt_profiles_b]] | 🟢 90% |
| 4 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo | [[hrt_content_types_b]] | 🟢 90% |
| 5 | RATING_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de rating de talento | [[hrt_rating_models_b]] | 🟢 90% |
| 6 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nivel de talento atribuido | [[hrt_rating_levels_b]] | 🟢 90% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da avaliacao | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de fim da avaliacao | — | 🟢 90% |
| 9 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do rating | — | 🟡 75% |
| 10 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentarios sobre o rating | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com avaliacao de talento registrada)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)
- [[hrt_rating_models_b]] — via `RATING_MODEL_ID` (modelo de rating)
- [[hrt_rating_levels_b]] — via `RATING_LEVEL_ID` (nivel de talento)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Ratings de talento para matriz 9-box
```sql
SELECT tr.PERSON_ID, tr.RATING_LEVEL_ID,
       tr.DATE_FROM, tr.DATE_TO
FROM   HRT_BI_TALENT_RATING_ITEMS_V tr
WHERE  tr.PERSON_ID = :p_person_id
ORDER BY tr.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Talent rating representa o **potencial** do colaborador, diferente do performance rating.
- Usada em conjunto com HRT_BI_PERF_RATING_ITEMS_V para matriz 9-box.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_TALENT_RATING_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbitalentratingitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 7/165)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PiAttribute1 | — |
| ATTRIBUTE10 | PiAttribute10 | — |
| ATTRIBUTE11 | PiAttribute11 | — |
| ATTRIBUTE12 | PiAttribute12 | — |
| ATTRIBUTE13 | PiAttribute13 | — |
| ATTRIBUTE14 | PiAttribute14 | — |
| ATTRIBUTE15 | PiAttribute15 | — |
| ATTRIBUTE16 | PiAttribute16 | — |
| ATTRIBUTE17 | PiAttribute17 | — |
| ATTRIBUTE18 | PiAttribute18 | — |
| ATTRIBUTE19 | PiAttribute19 | — |
| ATTRIBUTE2 | PiAttribute2 | — |
| ATTRIBUTE20 | PiAttribute20 | — |
| ATTRIBUTE21 | PiAttribute21 | — |
| ATTRIBUTE22 | PiAttribute22 | — |
| ATTRIBUTE23 | PiAttribute23 | — |
| ATTRIBUTE24 | PiAttribute24 | — |
| ATTRIBUTE25 | PiAttribute25 | — |
| ATTRIBUTE26 | PiAttribute26 | — |
| ATTRIBUTE27 | PiAttribute27 | — |
| ATTRIBUTE28 | PiAttribute28 | — |
| ATTRIBUTE29 | PiAttribute29 | — |
| ATTRIBUTE3 | PiAttribute3 | — |
| ATTRIBUTE30 | PiAttribute30 | — |
| ATTRIBUTE4 | PiAttribute4 | — |
| ATTRIBUTE5 | PiAttribute5 | — |
| ATTRIBUTE6 | PiAttribute6 | — |
| ATTRIBUTE7 | PiAttribute7 | — |
| ATTRIBUTE8 | PiAttribute8 | — |
| ATTRIBUTE9 | PiAttribute9 | — |
| ATTRIBUTE_CATEGORY | PiAttributeCategory | — |
| ATTRIBUTE_DATE1 | PiAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PiAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PiAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PiAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PiAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PiAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PiAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PiAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PiAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PiAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PiAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PiAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PiAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PiAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PiAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PiAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PiAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PiAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PiAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PiAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PiAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PiAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PiAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PiAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PiAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PiAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PiAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PiAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PiAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PiAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PiAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PiAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PiAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PiAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PiAttributeNumber9 | — |
| BUSINESS_GROUP_ID | PiBusinessGroupId1 | — |
| CONTENT_ITEM_ID | PiContentItemId | — |
| CONTENT_TYPE_ID | PiContentTypeId | ✅ |
| CONTEXT_NAME | ContextName | — |
| COUNTRY_ID | PiCountryId | — |
| CREATED_BY | PiCreatedBy1 | — |
| CREATION_DATE | PiCreationDate1 | — |
| DATE_FROM | PiDateFrom | ✅ |
| DATE_TO | PiDateTo | ✅ |
| IMPORTANCE | PiImportance | — |
| INTEREST_LEVEL | PiInterestLevel | — |
| ITEM_CLOB_1 | TSPIItemClob1 | — |
| ITEM_CLOB_2 | TSPIItemClob2 | — |
| ITEM_CLOB_3 | TSPIItemClob3 | — |
| ITEM_CLOB_4 | TSPIItemClob4 | — |
| ITEM_CLOB_5 | TSPIItemClob5 | — |
| ITEM_DATE_1 | PiItemDate1 | — |
| ITEM_DATE_10 | PiItemDate10 | — |
| ITEM_DATE_2 | PiItemDate2 | — |
| ITEM_DATE_3 | PiItemDate3 | — |
| ITEM_DATE_4 | PiItemDate4 | — |
| ITEM_DATE_5 | PiItemDate5 | — |
| ITEM_DATE_6 | PiItemDate6 | — |
| ITEM_DATE_7 | PiItemDate7 | — |
| ITEM_DATE_8 | PiItemDate8 | — |
| ITEM_DATE_9 | PiItemDate9 | — |
| ITEM_DECIMAL_1 | PiItemDecimal1 | — |
| ITEM_DECIMAL_2 | PiItemDecimal2 | — |
| ITEM_DECIMAL_3 | PiItemDecimal3 | — |
| ITEM_DECIMAL_4 | PiItemDecimal4 | — |
| ITEM_DECIMAL_5 | PiItemDecimal5 | — |
| ITEM_NUMBER_1 | PiItemNumber1 | — |
| ITEM_NUMBER_10 | PiItemNumber10 | — |
| ITEM_NUMBER_2 | PiItemNumber2 | — |
| ITEM_NUMBER_3 | PiItemNumber3 | — |
| ITEM_NUMBER_4 | PiItemNumber4 | — |
| ITEM_NUMBER_5 | PiItemNumber5 | — |
| ITEM_NUMBER_6 | PiItemNumber6 | — |
| ITEM_NUMBER_7 | PiItemNumber7 | — |
| ITEM_NUMBER_8 | PiItemNumber8 | — |
| ITEM_NUMBER_9 | PiItemNumber9 | — |
| ITEM_TEXT2000_1 | PiItemText20001 | ✅ |
| ITEM_TEXT2000_2 | PiItemText20002 | — |
| ITEM_TEXT2000_3 | PiItemText20003 | — |
| ITEM_TEXT2000_4 | PiItemText20004 | — |
| ITEM_TEXT2000_5 | PiItemText20005 | — |
| ITEM_TEXT240_1 | PiItemText2401 | — |
| ITEM_TEXT240_10 | PiItemText24010 | — |
| ITEM_TEXT240_11 | PiItemText24011 | — |
| ITEM_TEXT240_12 | PiItemText24012 | — |
| ITEM_TEXT240_13 | PiItemText24013 | — |
| ITEM_TEXT240_14 | PiItemText24014 | — |
| ITEM_TEXT240_15 | PiItemText24015 | — |
| ITEM_TEXT240_2 | PiItemText2402 | — |
| ITEM_TEXT240_3 | PiItemText2403 | — |
| ITEM_TEXT240_4 | PiItemText2404 | — |
| ITEM_TEXT240_5 | PiItemText2405 | — |
| ITEM_TEXT240_6 | PiItemText2406 | — |
| ITEM_TEXT240_7 | PiItemText2407 | — |
| ITEM_TEXT240_8 | PiItemText2408 | — |
| ITEM_TEXT240_9 | PiItemText2409 | — |
| ITEM_TEXT30_1 | PiItemText301 | — |
| ITEM_TEXT30_10 | PiItemText3010 | — |
| ITEM_TEXT30_11 | PiItemText3011 | — |
| ITEM_TEXT30_12 | PiItemText3012 | — |
| ITEM_TEXT30_13 | PiItemText3013 | — |
| ITEM_TEXT30_14 | PiItemText3014 | — |
| ITEM_TEXT30_15 | PiItemText3015 | — |
| ITEM_TEXT30_2 | PiItemText302 | — |
| ITEM_TEXT30_3 | PiItemText303 | — |
| ITEM_TEXT30_4 | PiItemText304 | — |
| ITEM_TEXT30_5 | PiItemText305 | — |
| ITEM_TEXT30_6 | PiItemText306 | — |
| ITEM_TEXT30_7 | PiItemText307 | — |
| ITEM_TEXT30_8 | PiItemText308 | — |
| ITEM_TEXT30_9 | PiItemText309 | — |
| LAST_UPDATE_DATE | PiLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | PiLastUpdateLogin1 | — |
| LAST_UPDATED_BY | PiLastUpdatedBy1 | — |
| MANDATORY | PiMandatory | — |
| OBJECT_VERSION_NUMBER | PiObjectVersionNumber1 | — |
| PARENT_PROFILE_ITEM_ID | PiParentProfileItemId | — |
| PROFILE_ID | PiProfileId1 | — |
| PROFILE_ITEM_ID | PiProfileItemId | ✅ |
| QUALIFIER_ID1 | PiQualifierId1 | — |
| QUALIFIER_ID2 | PiQualifierId2 | — |
| RATING_LEVEL_ID1 | PiRatingLevelId1 | — |
| RATING_LEVEL_ID2 | PiRatingLevelId2 | — |
| RATING_LEVEL_ID3 | PiRatingLevelId3 | — |
| RATING_MODEL_ID1 | PiRatingModelId1 | — |
| RATING_MODEL_ID2 | PiRatingModelId2 | — |
| RATING_MODEL_ID3 | PiRatingModelId3 | — |
| SECTION_ID | SectionId | ✅ |
| SOURCE_ID | PiSourceId | — |
| SOURCE_KEY1 | PiSourceKey1 | — |
| SOURCE_KEY2 | PiSourceKey2 | — |
| SOURCE_KEY3 | PiSourceKey3 | — |
| SOURCE_TYPE | PiSourceType | — |
| STATE_PROVINCE_ID | PiStateProvinceId | — |
