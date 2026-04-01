---
id: DOC-HCM-257
doc_type: system-doc
title: "HRT_QUALIFIERS_TL — Qualificadores — Traducoes"
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
  - qualifiers
aliases:
  - HRT_QUALIFIERS_TL
  - hrt_qualifiers_tl
  - hrt-qualifiers-tl
  - qualifiers-translations
  - qualificadores-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_QUALIFIERS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_qualifiers_b]].

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
| 1 | QUALIFIER_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_qualifiers_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | QUALIFIER_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_qualifiers_b]] — via `QUALIFIER_ID` (registro base do qualificador)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.QUALIFIER_NAME
FROM   HRT_QUALIFIERS_TL tl
WHERE  tl.QUALIFIER_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (QUALIFIER_ID, LANGUAGE).
- JOIN com [[hrt_qualifiers_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_QUALIFIERS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtqualifierstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[competencypvo|CompetencyPVO]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QualifierTLPEOBusinessGroup | — |
| DESCRIPTION | QualifiersTLPEODescription | ✅ |
| LANGUAGE | QualifiersTLPEOLanguage1 | ✅ |
| LAST_UPDATE_DATE | QualifiersTLPEOLastUpdateDate | ✅ |
| QUALIFIER_ID | QualifiersTLPEOQualifierId | — |
| SOURCE_LANG | QualifiersTLPEOSourceLang | — |

### [[potentialpvo|PotentialPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| DESCRIPTION | STLSourceDescription | ✅ |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| QUALIFIER_ID | STLSourceId2 | — |

### [[potentialpvo_viewall|PotentialPVO_Viewall]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| DESCRIPTION | STLSourceDescription | ✅ |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| QUALIFIER_ID | STLSourceId2 | — |

### [[qualifierspvo|QualifiersPVO]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QualifiersTranslationPEOBusinessGroupId | — |
| CREATED_BY | QualifiersTranslationPEOCreatedBy | — |
| CREATION_DATE | QualifiersTranslationPEOCreationDate | — |
| DESCRIPTION | QualifiersTranslationPEODescription | ✅ |
| LANGUAGE | QualifiersTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | QualifiersTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QualifiersTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QualifiersTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QualifiersTranslationPEOObjectVersionNumber | — |
| QUALIFIER_ID | QualifiersTranslationPEOQualifierId | — |
| SOURCE_LANG | SourceLang | — |

### [[riskpvo|RiskPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| DESCRIPTION | STLSourceDescription | ✅ |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| QUALIFIER_ID | STLSourceId2 | — |

### [[riskpvo_viewall|RiskPVO_Viewall]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| DESCRIPTION | STLSourceDescription | ✅ |
| LANGUAGE | STLLanguage | — |
| LAST_UPDATE_DATE | SourcesTranslationPEOLastUpdateDate | ✅ |
| QUALIFIER_ID | STLSourceId2 | — |

### [[talentscorepvo|TalentScorePVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QTLBusinessGroupId1 | — |
| BUSINESS_GROUP_ID | STLBusinessGroupId | — |
| DESCRIPTION | QualifiersTLPEODescription | ✅ |
| DESCRIPTION | STLSourceDescription | ✅ |
| LANGUAGE | QTLLanguage | — |
| LANGUAGE | STLLanguage | — |
| QUALIFIER_ID | QTLQualifierId1 | — |
| QUALIFIER_ID | STLSourceId | — |
| SOURCE_LANG | STLSourceLang | — |
