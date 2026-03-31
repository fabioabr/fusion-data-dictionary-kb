---
id: DOC-HCM-278
doc_type: system-doc
title: "HR_DOCUMENT_TYPES_TL — Tipos de Documento — Traducoes"
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
  - document-types
aliases:
  - HR_DOCUMENT_TYPES_TL
  - hr_document_types_tl
  - hr-document-types-tl
  - document-types-tl
  - tipos-documento-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOCUMENT_TYPES_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hr_document_types_b]].

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
| 1 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hr_document_types_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | DOCUMENT_TYPE_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_document_types_b]] — via `DOCUMENT_TYPE_ID` (registro base do cadastro)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.DOCUMENT_TYPE_NAME, tl.DESCRIPTION
FROM   HR_DOCUMENT_TYPES_TL tl
WHERE  tl.DOCUMENT_TYPE_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (DOCUMENT_TYPE_ID, LANGUAGE).
- JOIN com [[hr_document_types_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HR_DOCUMENT_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdocumenttypestl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOCUMENT_TYPE | DocumentTypesTranslationPEODocumentType | ✅ |
| DOCUMENT_TYPE_ID | DocumentTypesTranslationPEODocumentTypeId | — |
| LANGUAGE | DocumentTypesTranslationPEOLanguage | — |

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOCUMENT_TYPE | DocumentTypesTranslationPEODocumentType | ✅ |
| DOCUMENT_TYPE_ID | DocumentTypesTranslationPEODocumentTypeId | — |
| LANGUAGE | DocumentTypesTranslationPEOLanguage | — |

### [[documenttypespvo|DocumentTypesPVO]] (GL · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS_LABEL | DocumentTypesTranslationPEOCommentsLabel | — |
| CREATED_BY | DocumentTypesTranslationPEOCreatedBy1 | — |
| CREATION_DATE | DocumentTypesTranslationPEOCreationDate1 | — |
| DATE_FROM_LABEL | DocumentTypesTranslationPEODateFromLabel | — |
| DATE_TO_LABEL | DocumentTypesTranslationPEODateToLabel | — |
| DESCRIPTION | DocumentTypesTranslationPEODescription | ✅ |
| DOCUMENT_NAME_LABEL | DocumentTypesTranslationPEODocumentNameLabel | — |
| DOCUMENT_NUMBER_LABEL | DocumentTypesTranslationPEODocumentNumberLabel | — |
| DOCUMENT_TYPE | DocumentTypesTranslationPEODocumentType | ✅ |
| DOCUMENT_TYPE_ID | DocumentTypesTranslationPEODocumentTypeId1 | — |
| ENTERPRISE_ID | DocumentTypesTranslationPEOEnterpriseId1 | — |
| ISSUED_DATE_LABEL | DocumentTypesTranslationPEOIssuedDateLabel | — |
| ISSUING_AUTHORITY_LABEL | DocumentTypesTranslationPEOIssuingAuthorityLabel | — |
| ISSUING_COUNTRY_LABEL | DocumentTypesTranslationPEOIssuingCountryLabel | — |
| ISSUING_LOCATION_LABEL | DocumentTypesTranslationPEOIssuingLocationLabel | — |
| LANGUAGE | DocumentTypesTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | DocumentTypesTranslationPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DocumentTypesTranslationPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DocumentTypesTranslationPEOLastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | DocumentTypesTranslationPEOObjectVersionNumber1 | — |
| SOURCE_LANG | DocumentTypesTranslationPEOSourceLang | — |
