---
id: DOC-HCM-229
doc_type: system-doc
title: "HRT_BI_SPECIAL_PRJ_ITEMS_V — Itens de Projetos Especiais (BI View)"
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
  - projetos-especiais
  - talent
aliases:
  - HRT_BI_SPECIAL_PRJ_ITEMS_V
  - hrt_bi_special_prj_items_v
  - hrt-bi-special-prj-items-v
  - special-projects-bi
  - projetos-especiais-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_SPECIAL_PRJ_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **itens de projetos especiais** associados aos perfis de talento dos colaboradores. Registra participacoes em projetos estrategicos e iniciativas especiais.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Talent Management:** Rastrear participacao em projetos estrategicos.
- **Desenvolvimento:** Avaliar exposicao a projetos de alto impacto.
- **BI/Analytics:** Relatorios de alocacao de talentos em iniciativas especiais.

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
| 5 | PROJECT_NAME | VARCHAR2(240) | NULL | Dados | Nome do projeto especial | — | 🟡 75% |
| 6 | PROJECT_ROLE | VARCHAR2(240) | NULL | Dados | Papel do colaborador no projeto | — | 🟡 70% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio da participacao | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de termino da participacao | — | 🟢 90% |
| 9 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Observacoes sobre o projeto | — | 🟡 70% |
| 10 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do registro | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa participante do projeto especial)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Projetos especiais de um colaborador
```sql
SELECT sp.PROJECT_NAME, sp.PROJECT_ROLE,
       sp.DATE_FROM, sp.DATE_TO
FROM   HRT_BI_SPECIAL_PRJ_ITEMS_V sp
WHERE  sp.PERSON_ID = :p_person_id
ORDER BY sp.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Projetos especiais sao informados manualmente no perfil do colaborador.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_SPECIAL_PRJ_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbispecialprjitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[specialprojectpvo|SpecialProjectPVO]] (HCM · BICC: 18/106)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileItemPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ProfileItemPEOContentItemId | — |
| CONTENT_TYPE_ID | ProfileItemPEOContentTypeId | ✅ |
| CONTEXT_NAME | ContextName | — |
| COUNTRY_ID | ProfileItemPEOCountryId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | ProfileItemPEODateFrom | ✅ |
| DATE_TO | ProfileItemPEODateTo | ✅ |
| IMPORTANCE | Importance | — |
| INTEREST_LEVEL | InterestLevel | — |
| ITEM_CLOB_1 | SpecialPrjPIPEOItemClob1 | — |
| ITEM_CLOB_2 | SpecialPrjPIPEOItemClob2 | — |
| ITEM_CLOB_3 | ItemClob3 | — |
| ITEM_CLOB_4 | ItemClob4 | — |
| ITEM_CLOB_5 | ItemClob5 | — |
| ITEM_DATE_1 | ItemDate1 | ✅ |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | — |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | ✅ |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_DECIMAL_1 | ItemDecimal1 | — |
| ITEM_DECIMAL_2 | ItemDecimal2 | — |
| ITEM_DECIMAL_3 | ItemDecimal3 | — |
| ITEM_DECIMAL_4 | ItemDecimal4 | — |
| ITEM_DECIMAL_5 | ItemDecimal5 | — |
| ITEM_NUMBER_1 | ItemNumber1 | — |
| ITEM_NUMBER_10 | ProfileItemPEOItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | — |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT2000_1 | ItemText20001 | ✅ |
| ITEM_TEXT2000_2 | ItemText20002 | — |
| ITEM_TEXT2000_2 | SpecialPrjPEOPEOItemText20002 | ✅ |
| ITEM_TEXT2000_3 | ItemText20003 | — |
| ITEM_TEXT2000_4 | ItemText20004 | — |
| ITEM_TEXT2000_5 | ItemText20005 | — |
| ITEM_TEXT240_1 | ItemText2401 | ✅ |
| ITEM_TEXT240_10 | ItemText24010 | — |
| ITEM_TEXT240_10 | SpecialPrjPIPEOItemText24010 | ✅ |
| ITEM_TEXT240_11 | ItemText24011 | — |
| ITEM_TEXT240_12 | ItemText24012 | — |
| ITEM_TEXT240_13 | ItemText24013 | — |
| ITEM_TEXT240_14 | ItemText24014 | — |
| ITEM_TEXT240_15 | ItemText24015 | — |
| ITEM_TEXT240_2 | ItemText2402 | — |
| ITEM_TEXT240_2 | SpecialPrjPIPEOItemText2402 | ✅ |
| ITEM_TEXT240_3 | ItemText2403 | — |
| ITEM_TEXT240_3 | SpecialPrjPIPEOItemText2403 | ✅ |
| ITEM_TEXT240_4 | ItemText2404 | — |
| ITEM_TEXT240_4 | SpecialPrjPIPEOItemText2404 | ✅ |
| ITEM_TEXT240_5 | ItemText2405 | — |
| ITEM_TEXT240_6 | ItemText2406 | ✅ |
| ITEM_TEXT240_7 | ItemText2407 | — |
| ITEM_TEXT240_7 | SpecialPrjPIPEOItemText2407 | ✅ |
| ITEM_TEXT240_8 | ItemText2408 | — |
| ITEM_TEXT240_9 | ItemText2409 | — |
| ITEM_TEXT30_1 | ItemText301 | — |
| ITEM_TEXT30_10 | ItemText3010 | — |
| ITEM_TEXT30_11 | ItemText3011 | — |
| ITEM_TEXT30_12 | ItemText3012 | — |
| ITEM_TEXT30_13 | ItemText3013 | — |
| ITEM_TEXT30_14 | ItemText3014 | — |
| ITEM_TEXT30_15 | ItemText3015 | — |
| ITEM_TEXT30_2 | ItemText302 | — |
| ITEM_TEXT30_2 | SpecialPrjPIPEOItemText302 | ✅ |
| ITEM_TEXT30_3 | ItemText303 | — |
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
| SECTION_ID | SectionId | ✅ |
| SOURCE_ID | SourceId | — |
| SOURCE_KEY1 | SourceKey1 | — |
| SOURCE_KEY2 | SourceKey2 | — |
| SOURCE_KEY3 | SourceKey3 | — |
| SOURCE_TYPE | SourceType | — |
| STATE_PROVINCE_ID | ProfileItemPEOStateProvinceId | — |
