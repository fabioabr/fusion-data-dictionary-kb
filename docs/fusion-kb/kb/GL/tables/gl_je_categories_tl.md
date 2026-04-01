---
id: DOC-GL-021
doc_type: system-doc
title: "GL_JE_CATEGORIES_TL — Traduções de Categorias de Lançamentos"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - categorias
  - journal-categories
  - traducoes
  - i18n
aliases:
  - GL_JE_CATEGORIES_TL
  - gl_je_categories_tl
  - categorias-lancamento-traducoes
  - journal-categories-translations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_CATEGORIES_TL

## 📌 Visão Geral

Tabela de **traduções** das categorias de lançamentos contábeis. Armazena o nome do usuário (`USER_JE_CATEGORY_NAME`) e a descrição de cada categoria em múltiplos idiomas. Complementa a tabela base `GL_JE_CATEGORIES_B` no padrão Oracle multi-idioma (_B + _TL).

> [!note] Sufixo _TL
> O sufixo `_TL` indica a **tabela de traduções** (Translation Layer). Contém uma linha por combinação de categoria + idioma. A chave primária é composta: `JE_CATEGORY_NAME` + `LANGUAGE`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exibição multi-idioma:** Apresentação do nome da categoria no idioma do usuário logado.
- **Relatórios internacionais:** Geração de relatórios financeiros em diferentes idiomas.
- **LOV (List of Values):** População de listas de seleção de categorias com nomes traduzidos.
- **Pesquisa:** Permite buscar categorias pelo nome traduzido (USER_JE_CATEGORY_NAME).
- **Integração:** Exportação de dados com labels no idioma adequado ao destino.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_CATEGORY_NAME | VARCHAR2(25) | NOT NULL | PK/FK | Nome interno (chave) da categoria de lançamento | [[gl_je_categories_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK/i18n | Código do idioma da tradução (ex: US, PTB, ESA) | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | i18n | Idioma de origem da tradução | — | 🟢 100% |
| 4 | USER_JE_CATEGORY_NAME | VARCHAR2(25) | NOT NULL | Identificação | Nome da categoria traduzido (visível ao usuário) | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da categoria traduzida | — | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_categories_b]] — via `JE_CATEGORY_NAME` (tabela base da categoria)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de traduções (leaf table).

---

## 📎 Uso Típico

### Categorias com nome traduzido (idioma da sessão)
```sql
SELECT ct.JE_CATEGORY_NAME,
       ct.USER_JE_CATEGORY_NAME,
       ct.DESCRIPTION
FROM   GL_JE_CATEGORIES_TL ct
WHERE  ct.LANGUAGE = USERENV('LANG')
ORDER BY ct.USER_JE_CATEGORY_NAME;
```

### Traduções disponíveis de uma categoria
```sql
SELECT ct.LANGUAGE,
       ct.USER_JE_CATEGORY_NAME,
       ct.DESCRIPTION
FROM   GL_JE_CATEGORIES_TL ct
WHERE  ct.JE_CATEGORY_NAME = 'Adjustment'
ORDER BY ct.LANGUAGE;
```

### Join com tabela base para categorias ativas
```sql
SELECT c.JE_CATEGORY_NAME,
       ct.USER_JE_CATEGORY_NAME,
       ct.DESCRIPTION
FROM   GL_JE_CATEGORIES_B c
JOIN   GL_JE_CATEGORIES_TL ct ON ct.JE_CATEGORY_NAME = c.JE_CATEGORY_NAME
  AND  ct.LANGUAGE = 'PTB'
WHERE  c.ENABLED_FLAG = 'Y'
ORDER BY ct.USER_JE_CATEGORY_NAME;
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Idioma da sessão do usuário
- `LANGUAGE = 'PTB'` — Português brasileiro
- `LANGUAGE = 'US'` — Inglês americano
- `SOURCE_LANG = LANGUAGE` — Tradução nativa (não herdada)

---

## 🔒 Observações

- A chave primária é composta: `JE_CATEGORY_NAME` + `LANGUAGE`.
- Quando `SOURCE_LANG <> LANGUAGE`, a tradução foi herdada do idioma de origem e pode não ter sido traduzida manualmente.
- O `USER_JE_CATEGORY_NAME` é o que aparece na interface do Oracle Fusion — difere do `JE_CATEGORY_NAME` interno.
- Cada instalação do Oracle Fusion tem, no mínimo, traduções em `US` (inglês). Idiomas adicionais dependem da configuração.
- Para queries de relatório, preferir a view `GL_JE_CATEGORIES_VL` (se disponível) que faz o join automaticamente.

---

## 🔗 PVOs Relacionados

### [[journalcategorybpvo|JournalCategoryBPVO]] (GL · BICC: 5/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JrnlCatTranslatedCreatedBy | — |
| CREATED_BY | JrnlCatTranslatedLangCreatedBy | — |
| CREATION_DATE | JrnlCatTranslatedCreationDate | — |
| CREATION_DATE | JrnlCatTranslatedLangCreationDate | — |
| DESCRIPTION | JrnlCatTranslatedDescription | ✅ |
| DESCRIPTION | JrnlCatTranslatedLangDescription | — |
| JE_CATEGORY_NAME | JrnlCatTranslatedJeCategoryName | ✅ |
| JE_CATEGORY_NAME | JrnlCatTranslatedLangJeCategoryName | — |
| LANGUAGE | JrnlCatTranslatedLangLanguage | — |
| LANGUAGE | JrnlCatTranslatedLanguage | ✅ |
| LAST_UPDATE_DATE | JrnlCatTranslatedLangLastUpdateDate | — |
| LAST_UPDATE_DATE | JrnlCatTranslatedLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlCatTranslatedLangLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | JrnlCatTranslatedLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlCatTranslatedLangLastUpdatedBy | — |
| LAST_UPDATED_BY | JrnlCatTranslatedLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | JrnlCatTranslatedLangObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | JrnlCatTranslatedObjectVersionNumber | — |
| SOURCE_LANG | JrnlCatTranslatedLangSourceLang | — |
| SOURCE_LANG | JrnlCatTranslatedSourceLang | — |
| USER_JE_CATEGORY_NAME | JrnlCatTranslatedLangUserJeCategoryName | — |
| USER_JE_CATEGORY_NAME | JrnlCatTranslatedUserJeCategoryName | ✅ |

### [[journalcategoryextractpvo|JournalCategoryExtractPVO]] (OTHER · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JrnlCatTransLangCreatedBy | ✅ |
| CREATION_DATE | JrnlCatTransLangCreationDate | ✅ |
| DESCRIPTION | JrnlCatTransLangDescription | ✅ |
| JE_CATEGORY_NAME | JrnlCatTransLangJeCategoryName | ✅ |
| LANGUAGE | JrnlCatTransLangLanguage | ✅ |
| LAST_UPDATE_DATE | JrnlCatTransLangLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlCatTransLangLastUpdateLogn | ✅ |
| LAST_UPDATED_BY | JrnlCatTransLangLastUpdatedBy | ✅ |
| SOURCE_LANG | JrnlCatTransLangSourceLang | ✅ |
| USER_JE_CATEGORY_NAME | JrnlCatTransLangUserJeCatName | ✅ |

### [[journalcategorytlextractpvo|JournalCategoryTLExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JrnlCatTranslationCreatedBy | ✅ |
| CREATION_DATE | JrnlCatTranslationCreationDate | ✅ |
| DESCRIPTION | JrnlCatTranslationDescription | ✅ |
| JE_CATEGORY_NAME | JrnlCatTranslationJeCategoryName | ✅ |
| LANGUAGE | JrnlCatTranslationLanguage | ✅ |
| LAST_UPDATE_DATE | JrnlCatTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlCatTranslationLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JrnlCatTranslationLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | JrnlCatTranslationObjectVersionNumber | ✅ |
| SOURCE_LANG | JrnlCatTranslationSourceLang | ✅ |
| USER_JE_CATEGORY_NAME | JrnlCatTranslationUserJeCategoryName | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL_JE_CATEGORIES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljecategories-25720.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
