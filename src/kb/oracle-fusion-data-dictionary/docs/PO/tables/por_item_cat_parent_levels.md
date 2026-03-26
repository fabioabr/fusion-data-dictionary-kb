---
id: DOC-PO-063
doc_type: system-doc
title: "POR_ITEM_CAT_PARENT_LEVELS — Níveis Hierárquicos de Categorias de Itens"
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
  - categorias
  - hierarquia
  - itens
aliases:
  - POR_ITEM_CAT_PARENT_LEVELS
  - por_item_cat_parent_levels
  - niveis-hierarquia-categorias
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_ITEM_CAT_PARENT_LEVELS

## 📌 Visão Geral

Armazena a **estrutura hierárquica de níveis** das categorias de itens no módulo de Procurement. Esta tabela mapeia cada categoria ao seu nível na árvore hierárquica e seus respectivos pais, facilitando a navegação e agrupamento de categorias de compras em múltiplos níveis.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Navegação hierárquica:** Suporte à exibição em árvore das categorias de itens no catálogo de compras.
- **Roll-up de gastos:** Agregação de gastos por nível hierárquico (ex: categoria pai → subcategoria).
- **Relatórios analíticos:** Dimensão hierárquica para análises de spend by category em BI/OTBI.
- **Controle de acesso:** Definição de permissões por nível de categoria (ex: aprovações por grupo de categorias).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CATEGORY_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da categoria de item | [[egp_categories_b]] | 🟡 80% |
| 2 | PARENT_CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria-pai na hierarquia | [[egp_categories_b]] | 🟡 80% |
| 3 | LEVEL_NUM | NUMBER | NOT NULL | Hierarquia | Nível na hierarquia (1 = raiz, 2 = filho, etc.) | — | 🟡 75% |
| 4 | CATEGORY_SET_ID | NUMBER(18) | NULL | FK | Conjunto de categorias associado | [[egp_category_sets_b]] | 🟡 70% |
| 5 | STRUCTURE_ID | NUMBER(18) | NULL | FK | Estrutura flexfield da categoria | — | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria do item)
- [[egp_categories_b]] — via `PARENT_CATEGORY_ID` (categoria-pai)
- [[egp_category_sets_b]] — via `CATEGORY_SET_ID` (conjunto de categorias)

### Tabelas-filha (FK de saída)
- Utilizada indiretamente por views de navegação de catálogo de compras

---

## 📎 Uso Típico

### Obter hierarquia completa de uma categoria
```sql
SELECT pcpl.CATEGORY_ID,
       pcpl.PARENT_CATEGORY_ID,
       pcpl.LEVEL_NUM,
       cat.CATEGORY_NAME
FROM   POR_ITEM_CAT_PARENT_LEVELS pcpl
JOIN   EGP_CATEGORIES_VL cat ON cat.CATEGORY_ID = pcpl.CATEGORY_ID
WHERE  pcpl.CATEGORY_SET_ID = :p_category_set_id
ORDER BY pcpl.LEVEL_NUM;
```

### Categorias de nível superior (raiz)
```sql
SELECT pcpl.CATEGORY_ID, cat.CATEGORY_NAME
FROM   POR_ITEM_CAT_PARENT_LEVELS pcpl
JOIN   EGP_CATEGORIES_VL cat ON cat.CATEGORY_ID = pcpl.CATEGORY_ID
WHERE  pcpl.LEVEL_NUM = 1
  AND  pcpl.PARENT_CATEGORY_ID IS NULL;
```

---

## 🔒 Observações

- A estrutura hierárquica é desnormalizada nesta tabela para otimizar consultas de navegação (evita recursive queries).
- `LEVEL_NUM = 1` indica categorias raiz; cada incremento representa um nível mais profundo na árvore.
- Alterações na hierarquia de categorias em EGP são refletidas nesta tabela via processos batch de sincronização.
- Utilizada principalmente pelo iProcurement para montar a árvore de shopping categories.

---

## 📚 Referências

- [Oracle Docs — POR Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/portables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
