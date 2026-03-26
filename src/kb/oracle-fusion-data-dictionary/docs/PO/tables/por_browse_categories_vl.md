---
id: DOC-PO-062
doc_type: system-doc
title: "POR_BROWSE_CATEGORIES_VL — View de Categorias de Navegação (Base + Tradução)"
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
  - view
aliases:
  - POR_BROWSE_CATEGORIES_VL
  - por_browse_categories_vl
  - categorias-navegacao-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_BROWSE_CATEGORIES_VL

## 📌 Visão Geral

View que combina a tabela-base de categorias de navegação com suas traduções (sufixo `_VL` — View Language), retornando os dados no idioma da sessão do usuário. Utilizada pelo módulo de requisições de compra (iProcurement) para exibir a hierarquia de categorias de navegação no catálogo de compras.

> [!note] Sufixo _VL
> O sufixo `_VL` indica uma view que faz JOIN entre a tabela-base (`_B`) e a tabela de tradução (`_TL`), filtrando pelo idioma da sessão do usuário (`USERENV('LANG')`).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Navegação no catálogo de compras:** Exibição hierárquica das categorias para seleção durante a criação de requisições.
- **Self-service procurement:** Interface de shopping do iProcurement usa esta view para montar a árvore de categorias.
- **Relatórios de requisições:** Consultas analíticas que precisam do nome da categoria no idioma local.
- **Integrações:** Camada de abstração que simplifica consultas eliminando a necessidade de JOIN manual com `_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BROWSE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da categoria de navegação | — | 🟢 95% |
| 2 | CATEGORY_NAME | VARCHAR2(240) | NOT NULL | Descrição | Nome da categoria no idioma da sessão | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Descrição | Descrição da categoria no idioma da sessão | — | 🟡 75% |
| 4 | PARENT_BROWSE_CATEGORY_ID | NUMBER(18) | NULL | Hierarquia | Categoria-pai na árvore de navegação | — | 🟢 85% |
| 5 | CATEGORY_ID | NUMBER(18) | NULL | FK | Referência à categoria de item do inventário | [[egp_categories_b]] | 🟡 75% |
| 6 | IMAGE_URL | VARCHAR2(2000) | NULL | Apresentação | URL da imagem associada à categoria | — | 🟡 65% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se a categoria está ativa (Y/N) | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Tabela-base `POR_BROWSE_CATEGORIES_B` — dados estruturais da categoria
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de item, se aplicável)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Árvore de categorias de nível superior
```sql
SELECT vl.BROWSE_CATEGORY_ID, vl.CATEGORY_NAME, vl.DESCRIPTION
FROM   POR_BROWSE_CATEGORIES_VL vl
WHERE  vl.PARENT_BROWSE_CATEGORY_ID IS NULL
  AND  vl.ENABLED_FLAG = 'Y'
ORDER BY vl.CATEGORY_NAME;
```

### Subcategorias de uma categoria específica
```sql
SELECT vl.BROWSE_CATEGORY_ID, vl.CATEGORY_NAME
FROM   POR_BROWSE_CATEGORIES_VL vl
WHERE  vl.PARENT_BROWSE_CATEGORY_ID = :p_parent_id
  AND  vl.ENABLED_FLAG = 'Y'
ORDER BY vl.CATEGORY_NAME;
```

---

## 🔒 Observações

- Esta é uma **view**, não uma tabela física — não aceita DML direto.
- O filtro de idioma é aplicado automaticamente pelo Oracle via `USERENV('LANG')`.
- A hierarquia pode ter múltiplos níveis; use queries recursivas (CONNECT BY) para navegar toda a árvore.
- Categorias desabilitadas (`ENABLED_FLAG = 'N'`) não aparecem no catálogo de compras mas permanecem para histórico.

---

## 📚 Referências

- [Oracle Docs — POR Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/portables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
