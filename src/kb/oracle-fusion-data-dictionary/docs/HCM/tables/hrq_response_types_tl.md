---
id: DOC-HCM-199
doc_type: system-doc
title: "HRQ_RESPONSE_TYPES_TL — Traduções de Tipos de Resposta"
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
  - questionnaires
  - response-types
  - translation
aliases:
  - HRQ_RESPONSE_TYPES_TL
  - hrq_response_types_tl
  - traduções-de-tipos-de-resposta
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_RESPONSE_TYPES_TL

## 📌 Visão Geral

Tabela de **traduções** de tipos de resposta de questionários (base). Padrão Oracle MLS.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Traduções em múltiplos idiomas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador | [[hrq_response_types_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrq_response_types_b]] — via `RESPONSE_TYPE_ID` (registro base do cadastro)

---

## 📎 Uso Típico

### Traduções
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   HRQ_RESPONSE_TYPES_TL tl
WHERE  tl.RESPONSE_TYPE_ID = :p_id AND tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `RESPONSE_TYPE_ID` + `LANGUAGE`.

---

## 🔗 PVOs Relacionados

### [[responsetypepvo|ResponseTypePVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ResponseTypeTranslationPEOBusinessGroupId | — |
| CREATED_BY | ResponseTypeTranslationPEOCreatedBy | — |
| CREATION_DATE | ResponseTypeTranslationPEOCreationDate | — |
| LANGUAGE | ResponseTypeTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ResponseTypeTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseTypeTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResponseTypeTranslationPEOLastUpdatedBy | — |
| NAME | ResponseTypeTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ResponseTypeTranslationPEOObjectVersionNumber | — |
| RESPONSE_TYPE_ID | ResponseTypeTranslationPEOResponseTypeId | — |
| SEED_DATA_SOURCE | ResponseTypeTranslationPEOSeedDataSource | — |
| SOURCE_LANG | ResponseTypeTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
