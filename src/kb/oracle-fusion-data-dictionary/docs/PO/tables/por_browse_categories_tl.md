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

## 📚 Referências

- [Oracle Docs — POR Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/portables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
