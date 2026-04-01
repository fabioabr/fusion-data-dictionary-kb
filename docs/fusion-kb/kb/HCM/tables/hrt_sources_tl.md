---
id: DOC-HCM-270
doc_type: system-doc
title: "HRT_SOURCES_TL — Fontes de Conteudo — Traducoes"
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
  - sources
aliases:
  - HRT_SOURCES_TL
  - hrt_sources_tl
  - hrt-sources-tl
  - sources-tl
  - fontes-conteudo-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_SOURCES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_sources_b]].

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
| 1 | SOURCE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_sources_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | SOURCE_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_sources_b]] — via `SOURCE_ID` (registro base da fonte de conteudo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.SOURCE_NAME, tl.DESCRIPTION
FROM   HRT_SOURCES_TL tl
WHERE  tl.SOURCE_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (SOURCE_ID, LANGUAGE).
- JOIN com [[hrt_sources_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_SOURCES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtsourcestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[advancementreadinesspvo|AdvancementReadinessPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | STLSourceDescription | ✅ |
| SOURCE_ID | STLSourceId1 | — |

### [[advancementreadinesspvo_viewall|AdvancementReadinessPVO_Viewall]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | STLSourceDescription | ✅ |
| SOURCE_ID | STLSourceId1 | — |

### [[certificationpvo|CertificationPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| LANGUAGE | Language1 | — |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourceId2 | — |

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId7 | — |
| LANGUAGE | Language2 | — |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourceId2 | — |

### [[contentsourcerelpvo|ContentSourceRelPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SourcesTranslationPEOBusinessGroupId | — |
| LANGUAGE | SourcesTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | SourcesTranslationPEOSourceDescription | — |
| SOURCE_ID | SourcesTransalationPEOSourceId | — |
| SOURCE_LANG | SourceLang | — |

### [[criticalityprofileitempvo|CriticalityProfileItemPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| LANGUAGE | Language1 | — |
| SOURCE_DESCRIPTION | STLSourceDescription | ✅ |
| SOURCE_ID | SourceId1 | — |

### [[degreepvo|DegreePVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| LANGUAGE | Language2 | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | SourceDescription | — |
| SOURCE_ID | SourceId1 | — |

### [[honorpvo|HonorPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| LANGUAGE | Language2 | — |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourceId2 | — |

### [[languagepvo|LanguagePVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| LANGUAGE | Language1 | — |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourceId2 | — |

### [[membershippvo|MembershipPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| LANGUAGE | Language2 | — |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourceId2 | — |

### [[personprofileperformanceratingpvo|PersonProfilePerformanceRatingPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId1 | — |
| LANGUAGE | STLLanguage2 | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | STLSourceDescription | ✅ |
| SOURCE_ID | STLSourceId1 | — |

### [[planreadinesspvo|PlanReadinessPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | — |
| SOURCE_DESCRIPTION | STLSourceDescription | — |
| SOURCE_ID | STLSourceId1 | — |

### [[sourcesallpvo|SourcesAllPVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | SourcesTranslationPEOBusinessGroupId | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourcesTranslationPEOSourceId | — |
| SOURCE_LANG | SourceLang | — |

### [[sourcesalltranslationpvo|SourcesAllTranslationPVO]] (HCM · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_DESCRIPTION | SourceDescription | ✅ |
| SOURCE_ID | SourceId | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

### [[workrequirementdatecheckpvo|WorkRequirementDateCheckPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | — |
| SOURCE_DESCRIPTION | SourceDescription | — |
| SOURCE_ID | SourceId2 | — |

### [[workrequirementpvo|WorkRequirementPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| SOURCE_DESCRIPTION | SourceDescription | — |
| SOURCE_ID | SourceId2 | — |
