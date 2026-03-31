---
id: DOC-HCM-227
doc_type: system-doc
title: "HRT_BI_PREV_EMPLOYMENT_ITEMS_V — Itens de Emprego Anterior (BI View)"
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
  - emprego-anterior
  - talent
aliases:
  - HRT_BI_PREV_EMPLOYMENT_ITEMS_V
  - hrt_bi_prev_employment_items_v
  - hrt-bi-prev-employment-items-v
  - previous-employment-bi
  - emprego-anterior-bi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_BI_PREV_EMPLOYMENT_ITEMS_V

## 📌 Visao Geral

View BI que expoe os **itens de emprego anterior** dos colaboradores. Permite analise de historico profissional previo para fins de talent management e compliance.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Analise de historico:** Consulta de experiencias profissionais anteriores dos colaboradores.
- **Talent Management:** Avaliacao de experiencia previa em processos de promocao e sucessao.
- **Compliance:** Verificacao de historico profissional para requisitos regulatorios.

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
| 5 | EMPLOYER_NAME | VARCHAR2(240) | NULL | Dados | Nome do empregador anterior | — | 🟡 75% |
| 6 | JOB_TITLE | VARCHAR2(240) | NULL | Dados | Cargo exercido no emprego anterior | — | 🟡 75% |
| 7 | DATE_FROM | DATE | NULL | Data | Data de inicio do emprego anterior | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Data de termino do emprego anterior | — | 🟢 90% |
| 9 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Observacoes sobre o emprego anterior | — | 🟡 70% |
| 10 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Origem do registro | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com historico de emprego anterior)
- [[hrt_profiles_b]] — via `PROFILE_ID` (perfil de talento)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Empregos anteriores de um colaborador
```sql
SELECT pi.EMPLOYER_NAME, pi.JOB_TITLE,
       pi.DATE_FROM, pi.DATE_TO
FROM   HRT_BI_PREV_EMPLOYMENT_ITEMS_V pi
WHERE  pi.PERSON_ID = :p_person_id
ORDER BY pi.DATE_FROM DESC;
```

---

## 🔒 Observacoes

- View somente leitura para BI — dados originam de perfis de talento.
- Sufixo `_V` indica que e uma view (nao tabela fisica).
- Pode incluir empregos informados pelo colaborador via self-service.

---

## 📚 Referencias

- [Oracle Docs — HRT_BI_PREV_EMPLOYMENT_ITEMS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtbiprevemploymentitemsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[previousemploymentprofilepvo|PreviousEmploymentProfilePVO]] (HCM · BICC: 35/99)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ProfileItemPEOBusinessGroupId | — |
| CONTENT_ITEM_ID | ProfileItemPEOContentItemId | — |
| CONTENT_TYPE_ID | ProfileItemPEOContentTypeId | ✅ |
| COUNTRY_CODE | CountryCode | — |
| COUNTRY_ID | ProfileItemPEOCountryId | — |
| COUNTRY_NAME | CountryName | ✅ |
| DATE_FROM | ProfileItemPEODateFrom | ✅ |
| DATE_TO | ProfileItemPEODateTo | ✅ |
| IMPORTANCE | Importance | — |
| INTEREST_LEVEL | InterestLevel | — |
| ITEM_CLOB_1 | ItemClob1 | — |
| ITEM_CLOB_2 | ItemClob2 | — |
| ITEM_CLOB_3 | ItemClob3 | — |
| ITEM_CLOB_4 | ItemClob4 | — |
| ITEM_CLOB_5 | ItemClob5 | — |
| ITEM_DATE_1 | ItemDate1 | ✅ |
| ITEM_DATE_10 | ItemDate10 | — |
| ITEM_DATE_2 | ItemDate2 | ✅ |
| ITEM_DATE_3 | ItemDate3 | — |
| ITEM_DATE_4 | ItemDate4 | — |
| ITEM_DATE_5 | ItemDate5 | — |
| ITEM_DATE_6 | ItemDate6 | — |
| ITEM_DATE_7 | ItemDate7 | — |
| ITEM_DATE_8 | ItemDate8 | — |
| ITEM_DATE_9 | ItemDate9 | — |
| ITEM_DECIMAL_1 | ItemDecimal1 | ✅ |
| ITEM_DECIMAL_2 | ItemDecimal2 | ✅ |
| ITEM_DECIMAL_3 | ItemDecimal3 | — |
| ITEM_DECIMAL_4 | ItemDecimal4 | — |
| ITEM_DECIMAL_5 | ItemDecimal5 | — |
| ITEM_NUMBER_1 | ItemNumber1 | ✅ |
| ITEM_NUMBER_10 | ItemNumber10 | — |
| ITEM_NUMBER_2 | ItemNumber2 | — |
| ITEM_NUMBER_3 | ItemNumber3 | — |
| ITEM_NUMBER_4 | ItemNumber4 | — |
| ITEM_NUMBER_5 | ItemNumber5 | — |
| ITEM_NUMBER_6 | ItemNumber6 | — |
| ITEM_NUMBER_7 | ItemNumber7 | — |
| ITEM_NUMBER_8 | ItemNumber8 | ✅ |
| ITEM_NUMBER_9 | ItemNumber9 | — |
| ITEM_TEXT2000_1 | ItemText20001 | ✅ |
| ITEM_TEXT2000_2 | ItemText20002 | ✅ |
| ITEM_TEXT2000_3 | ItemText20003 | — |
| ITEM_TEXT2000_4 | ItemText20004 | — |
| ITEM_TEXT2000_5 | ItemText20005 | — |
| ITEM_TEXT240_1 | ItemText2401 | ✅ |
| ITEM_TEXT240_10 | ItemText24010 | ✅ |
| ITEM_TEXT240_11 | ItemText24011 | ✅ |
| ITEM_TEXT240_12 | ItemText24012 | ✅ |
| ITEM_TEXT240_13 | ItemText24013 | ✅ |
| ITEM_TEXT240_14 | ItemText24014 | ✅ |
| ITEM_TEXT240_15 | ItemText24015 | — |
| ITEM_TEXT240_2 | ItemText2402 | ✅ |
| ITEM_TEXT240_3 | ItemText2403 | ✅ |
| ITEM_TEXT240_4 | ItemText2404 | ✅ |
| ITEM_TEXT240_5 | ItemText2405 | — |
| ITEM_TEXT240_6 | ItemText2406 | ✅ |
| ITEM_TEXT240_7 | ItemText2407 | ✅ |
| ITEM_TEXT240_8 | ItemText2408 | ✅ |
| ITEM_TEXT240_9 | ItemText2409 | ✅ |
| ITEM_TEXT30_1 | ItemText301 | ✅ |
| ITEM_TEXT30_10 | ItemText3010 | — |
| ITEM_TEXT30_11 | ItemText3011 | — |
| ITEM_TEXT30_12 | ItemText3012 | — |
| ITEM_TEXT30_13 | ItemText3013 | — |
| ITEM_TEXT30_14 | ItemText3014 | — |
| ITEM_TEXT30_15 | ItemText3015 | — |
| ITEM_TEXT30_2 | ItemText302 | ✅ |
| ITEM_TEXT30_3 | ItemText303 | — |
| ITEM_TEXT30_4 | ItemText304 | — |
| ITEM_TEXT30_5 | ItemText305 | ✅ |
| ITEM_TEXT30_6 | ItemText306 | — |
| ITEM_TEXT30_7 | ItemText307 | ✅ |
| ITEM_TEXT30_8 | ItemText308 | ✅ |
| ITEM_TEXT30_9 | ItemText309 | ✅ |
| LAST_UPDATE_DATE | ProfileItemPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileItemPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileItemPEOLastUpdatedBy | — |
| MANDATORY | Mandatory | — |
| PARENT_PROFILE_ITEM_ID | ProfileItemPEOParentProfileItemId | — |
| PROFILE_ID | ProfileItemPEOProfileId | — |
| PROFILE_ITEM_ID | ProfileItemPEOProfileItemId | ✅ |
| QUALIFIER_ID1 | QualifierId1 | — |
| QUALIFIER_ID2 | QualifierId2 | — |
| RATING_LEVEL_ID1 | ProfileItemPEORatingLevelId1 | — |
| RATING_LEVEL_ID2 | ProfileItemPEORatingLevelId2 | — |
| RATING_LEVEL_ID3 | ProfileItemPEORatingLevelId3 | — |
| RATING_MODEL_ID1 | ProfileItemPEORatingModelId1 | — |
| RATING_MODEL_ID2 | ProfileItemPEORatingModelId2 | — |
| RATING_MODEL_ID3 | ProfileItemPEORatingModelId3 | — |
| SECTION_ID | SectionId | ✅ |
| SOURCE_ID | SourceId | — |
| SOURCE_KEY1 | SourceKey1 | — |
| SOURCE_KEY2 | SourceKey2 | — |
| SOURCE_KEY3 | SourceKey3 | — |
| SOURCE_TYPE | SourceType | — |
| STATE_PROVINCE_CODE | StateProvinceCode | — |
| STATE_PROVINCE_ID | ProfileItemPEOStateProvinceId | — |
| STATE_PROVINCE_NAME | StateProvinceName | ✅ |
