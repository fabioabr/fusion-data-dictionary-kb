---
id: DOC-HCM-250
doc_type: system-doc
title: "HRT_PROFILE_TP_SC_PRP_TL — Propriedades de Secoes de Tipo de Perfil — Traducoes"
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
  - profile-type-section-properties
aliases:
  - HRT_PROFILE_TP_SC_PRP_TL
  - hrt_profile_tp_sc_prp_tl
  - hrt-profile-tp-sc-prp-tl
  - profile-tp-sc-prp-tl
  - propriedades-secao-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_TP_SC_PRP_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hrt_profile_tp_sc_prp_b]].

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
| 1 | PROFILE_TP_SC_PRP_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hrt_profile_tp_sc_prp_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | DISPLAY_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profile_tp_sc_prp_b]] — via `PROFILE_TP_SC_PRP_ID` (registro base da propriedade de secao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.DISPLAY_NAME
FROM   HRT_PROFILE_TP_SC_PRP_TL tl
WHERE  tl.PROFILE_TP_SC_PRP_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (PROFILE_TP_SC_PRP_ID, LANGUAGE).
- JOIN com [[hrt_profile_tp_sc_prp_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_TP_SC_PRP_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofiletpscprptl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[profiletypesectionpropertypvo|ProfileTypeSectionPropertyPVO]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_LABEL | ProfileTypeSectionPropertyTrPEOAttributeLabel | — |
| BUSINESS_GROUP_ID | ProfileTypeSectionPropertyTrPEOBusinessGroupId | — |
| CREATED_BY | ProfileTypeSectionPropertyTrPEOCreatedBy | — |
| CREATION_DATE | ProfileTypeSectionPropertyTrPEOCreationDate | — |
| LANGUAGE | ProfileTypeSectionPropertyTrPEOLanguage | — |
| LAST_UPDATE_DATE | ProfileTypeSectionPropertyTrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ProfileTypeSectionPropertyTrPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ProfileTypeSectionPropertyTrPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ProfileTypeSectionPropertyTrPEOObjectVersionNumber | — |
| SECTION_PROP_ID | ProfileTypeSectionPropertyTrPEOSectionPropId | — |
| SOURCE_LANG | SourceLang | — |
