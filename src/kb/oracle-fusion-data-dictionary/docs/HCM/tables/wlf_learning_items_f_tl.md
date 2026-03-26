---
id: DOC-HCM-735
doc_type: system-doc
title: "WLF_LEARNING_ITEMS_F_TL — Itens de Aprendizado (Traduções)"
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
  - learning
  - workforce-learning
  - traduções
aliases:
  - WLF_LEARNING_ITEMS_F_TL
  - wlf_learning_items_f_tl
  - wlf-learning-items-f-tl
  - itens-aprendizado-traduções
  - learning-items-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LEARNING_ITEMS_F_TL

## Visão Geral

Armazena as **traduções** dos itens de aprendizado, incluindo nome, descrição e objetivos em múltiplos idiomas. Tabela de tradução (_TL).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — suporta catálogo de treinamentos em múltiplos idiomas.
- **Interface localizada** — exibe itens de aprendizado no idioma do colaborador.
- **Catálogo multilíngue** — permite busca e navegação em diferentes idiomas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do item de aprendizado | WLF_LEARNING_ITEMS_F | 🟢 85% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: PT, EN, ES) | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 85% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do item | — | 🟢 85% |
| 5 | DESCRIPTION | VARCHAR2(4000) | NULL | Identificação | Descrição traduzida | — | 🟡 80% |
| 6 | OBJECTIVES | VARCHAR2(4000) | NULL | Dados | Objetivos de aprendizado traduzidos | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Traduções de um item de aprendizado
```sql
SELECT tl.NAME, tl.DESCRIPTION, tl.OBJECTIVES, tl.LANGUAGE
FROM   WLF_LEARNING_ITEMS_F_TL tl
WHERE  tl.LEARNING_ITEM_ID = :p_learning_item_id
ORDER BY tl.LANGUAGE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Filtrar por idioma português
- `LEARNING_ITEM_ID = :p_id` — Traduções de um item específico

---

## Observações

- Tabela de tradução (_TL) — PK composta: LEARNING_ITEM_ID + LANGUAGE.
- SOURCE_LANG indica o idioma original da tradução.
- Faz parte do módulo Workforce Learning (prefixo WLF_).

---

## Referências

- [Oracle Docs — WLF_LEARNING_ITEMS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlflearningitemsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
