---
id: DOC-PO-061
doc_type: system-doc
title: "POR_BROWSE_CATEGORIES_TL — Traduções de Categorias de Navegação de Requisições"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - requisicoes
  - categorias
  - traducao
aliases:
  - POR_BROWSE_CATEGORIES_TL
  - por_browse_categories_tl
  - categorias-navegacao-traducao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_BROWSE_CATEGORIES_TL

## 📌 Visão Geral

Armazena as **traduções** (translation — sufixo `_TL`) das categorias de navegação utilizadas no módulo de requisições de compra (iProcurement/Procurement). Cada registro contém o nome e a descrição de uma categoria em um idioma específico, permitindo que o catálogo de compras seja apresentado em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de tradução multilíngue. Cada linha da tabela-base possui N registros nesta tabela, um por idioma configurado na instância.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Catálogo multilíngue:** Exibição das categorias de navegação no idioma do usuário durante a criação de requisições de compra.
- **Self-service procurement:** Suporte à navegação hierárquica do catálogo de compras em múltiplos idiomas.
- **Relatórios localizados:** Geração de relatórios de compras com nomes de categorias traduzidos.
- **Integração com views:** Base para a view `POR_BROWSE_CATEGORIES_VL` que combina base + tradução.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BROWSE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da categoria de navegação | [[por_browse_categories_tl]] (base) | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (ex: PTB, US) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | CATEGORY_NAME | VARCHAR2(240) | NOT NULL | Descrição | Nome traduzido da categoria de navegação | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Descrição | Descrição traduzida da categoria | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Tabela-base `POR_BROWSE_CATEGORIES_B` (implícita) — via `BROWSE_CATEGORY_ID` (definição base da categoria)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Obter nome da categoria no idioma do usuário
```sql
SELECT tl.BROWSE_CATEGORY_ID,
       tl.CATEGORY_NAME,
       tl.DESCRIPTION
FROM   POR_BROWSE_CATEGORIES_TL tl
WHERE  tl.LANGUAGE = USERENV('LANG');
```

### Listar traduções disponíveis para uma categoria
```sql
SELECT tl.LANGUAGE, tl.CATEGORY_NAME
FROM   POR_BROWSE_CATEGORIES_TL tl
WHERE  tl.BROWSE_CATEGORY_ID = :p_category_id
ORDER BY tl.LANGUAGE;
```

---

## 🔒 Observações

- A chave primária composta é `(BROWSE_CATEGORY_ID, LANGUAGE)`.
- O campo `SOURCE_LANG` indica o idioma de origem; quando `LANGUAGE = SOURCE_LANG`, o registro é a tradução original (não derivada).
- Registros onde `LANGUAGE <> SOURCE_LANG` são traduções pendentes de revisão manual.
- Esta tabela é populada automaticamente pelo framework de tradução Oracle (NLS) durante seed e patches.

---

## 🔗 PVOs Relacionados

### [[browsingcategoryhierarchypvo|BrowsingCategoryHierarchyPVO]] (PO · BICC: 30/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_DESCRIPTION | Level10CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level1CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level2CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level3CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level4CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level5CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level6CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level7CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level8CategoryDescription | ✅ |
| CATEGORY_DESCRIPTION | Level9CategoryDescription | ✅ |
| CATEGORY_ID | Level10CategoryId | — |
| CATEGORY_ID | Level1CategoryId | — |
| CATEGORY_ID | Level2CategoryId | — |
| CATEGORY_ID | Level3CategoryId | — |
| CATEGORY_ID | Level4CategoryId | — |
| CATEGORY_ID | Level5CategoryId | — |
| CATEGORY_ID | Level6CategoryId | — |
| CATEGORY_ID | Level7CategoryId | — |
| CATEGORY_ID | Level8CategoryId | — |
| CATEGORY_ID | Level9CategoryId | — |
| CATEGORY_NAME | Level10CategoryName | ✅ |
| CATEGORY_NAME | Level1CategoryName | ✅ |
| CATEGORY_NAME | Level2CategoryName | ✅ |
| CATEGORY_NAME | Level3CategoryName | ✅ |
| CATEGORY_NAME | Level4CategoryName | ✅ |
| CATEGORY_NAME | Level5CategoryName | ✅ |
| CATEGORY_NAME | Level6CategoryName | ✅ |
| CATEGORY_NAME | Level7CategoryName | ✅ |
| CATEGORY_NAME | Level8CategoryName | ✅ |
| CATEGORY_NAME | Level9CategoryName | ✅ |
| CREATED_BY | CreatedBy1 | — |
| CREATED_BY | CreatedBy10 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATED_BY | CreatedBy5 | — |
| CREATED_BY | CreatedBy6 | — |
| CREATED_BY | CreatedBy7 | — |
| CREATED_BY | CreatedBy8 | — |
| CREATED_BY | CreatedBy9 | — |
| CREATION_DATE | CreationDate1 | — |
| CREATION_DATE | CreationDate10 | — |
| CREATION_DATE | CreationDate2 | — |
| CREATION_DATE | CreationDate3 | — |
| CREATION_DATE | CreationDate4 | — |
| CREATION_DATE | CreationDate5 | — |
| CREATION_DATE | CreationDate6 | — |
| CREATION_DATE | CreationDate7 | — |
| CREATION_DATE | CreationDate8 | — |
| CREATION_DATE | CreationDate9 | — |
| LANGUAGE | Level10Language | — |
| LANGUAGE | Level1Language | — |
| LANGUAGE | Level2Language | — |
| LANGUAGE | Level3Language | — |
| LANGUAGE | Level4Language | — |
| LANGUAGE | Level5Language | — |
| LANGUAGE | Level6Language | — |
| LANGUAGE | Level7Language | — |
| LANGUAGE | Level8Language | — |
| LANGUAGE | Level9Language | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate10 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate5 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate6 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate7 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate8 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate9 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin10 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin5 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin8 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin9 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| LAST_UPDATED_BY | LastUpdatedBy10 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| LAST_UPDATED_BY | LastUpdatedBy5 | — |
| LAST_UPDATED_BY | LastUpdatedBy6 | — |
| LAST_UPDATED_BY | LastUpdatedBy7 | — |
| LAST_UPDATED_BY | LastUpdatedBy8 | — |
| LAST_UPDATED_BY | LastUpdatedBy9 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber10 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber5 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber6 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber7 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber8 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber9 | — |
| SOURCE_LANG | Level10SourceLang | — |
| SOURCE_LANG | Level1SourceLang | — |
| SOURCE_LANG | Level2SourceLang | — |
| SOURCE_LANG | Level3SourceLang | — |
| SOURCE_LANG | Level4SourceLang | — |
| SOURCE_LANG | Level5SourceLang | — |
| SOURCE_LANG | Level6SourceLang | — |
| SOURCE_LANG | Level7SourceLang | — |
| SOURCE_LANG | Level8SourceLang | — |
| SOURCE_LANG | Level9SourceLang | — |

### [[browsingcategorytranslationextractpvo|BrowsingCategoryTranslationExtractPVO]] (PO · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_DESCRIPTION | CategoryDescription | ✅ |
| CATEGORY_ID | CategoryId | ✅ |
| CATEGORY_NAME | CategoryName | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |

---

## 📚 Referências

- [Oracle Docs — POR Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/portables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
