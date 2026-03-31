---
id: DOC-HCM-694
doc_type: system-doc
title: "PER_PERSON_TYPES_TL — Traduções de Tipos de Pessoa"
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
  - tipos-pessoa
  - person-types-tl
  - traducao
  - multilanguage
aliases:
  - PER_PERSON_TYPES_TL
  - per_person_types_tl
  - traducao-tipos-pessoa
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_TYPES_TL

## Visão Geral

Armazena as **traduções** dos tipos de pessoa em múltiplos idiomas. Cada registro contém o nome descritivo traduzido de um tipo de pessoa para um idioma específico.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **tradução** — cada registro da tabela base possui N registros nesta tabela, um por idioma configurado.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exibição localizada** — mostrar nomes de tipos de pessoa no idioma do usuário
- **Relatórios multilíngues** — gerar relatórios com nomes traduzidos
- **Interfaces de usuário** — LOVs e dropdowns com valores traduzidos

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_TYPE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do tipo de pessoa | PER_PERSON_TYPES | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | USER_PERSON_TYPE | VARCHAR2(240) | NOT NULL | Tradução | Nome descritivo traduzido do tipo de pessoa | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_person_types]] — via `PERSON_TYPE_ID` (tabela base do tipo de pessoa)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Nome traduzido de um tipo de pessoa
```sql
SELECT tl.USER_PERSON_TYPE
FROM   PER_PERSON_TYPES_TL tl
WHERE  tl.PERSON_TYPE_ID = :p_person_type_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## Observações

- A chave primária é composta por `PERSON_TYPE_ID` + `LANGUAGE`.
- `USER_PERSON_TYPE` contém o nome amigável do tipo (ex: "Empregado", "Contingente").
- `SOURCE_LANG` indica se a tradução é nativa ou herdada.

---

## Referências

- [Oracle Docs — PER_PERSON_TYPES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersontypestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PersonTypesTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | PersonTypesTranslationPEOLastUpdateDate | ✅ |
| PERSON_TYPE_ID | PersonTypesTranslationPEOPersonTypeId | ✅ |
| USER_PERSON_TYPE | PersonTypesTranslationPEOUserPersonType | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PersonTypesTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | PersonTypesTranslationPEOLastUpdateDate | ✅ |
| PERSON_TYPE_ID | PersonTypesTranslationPEOPersonTypeId | — |
| USER_PERSON_TYPE | PersonTypesTranslationPEOUserPersonType | ✅ |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PersonTypesTranslationPEOLanguage | — |
| PERSON_TYPE_ID | PersonTypesTranslationPEOPersonTypeId | — |
| USER_PERSON_TYPE | PersonTypesTranslationPEOUserPersonType | ✅ |

### [[persontypestranslationpvo|PersonTypesTranslationPVO]] (HCM · BICC: 8/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PersonTypesTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | PersonTypesTranslationPEOCreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | PersonTypesTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonTypesTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonTypesTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PersonTypesTranslationPEOObjectVersionNumber | — |
| PERSON_TYPE_ID | PersonTypeId | ✅ |
| SOURCE_LANG | PersonTypesTranslationPEOSourceLang | ✅ |
| USER_PERSON_TYPE | PersonTypesTranslationPEOUserPersonType | ✅ |
