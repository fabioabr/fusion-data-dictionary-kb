---
id: DOC-HCM-002
doc_type: system-doc
title: "ANC_ABSENCE_CATEGORIES_F_TL — Traduções de Categorias de Ausência"
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
  - absence-management
  - traducoes
  - translations
  - categorias-ausencia-tl
aliases:
  - ANC_ABSENCE_CATEGORIES_F_TL
  - anc_absence_categories_f_tl
  - categorias-ausencia-tl
  - absence-categories-tl
  - anc-abs-categories-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_CATEGORIES_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições das categorias de ausência. Vinculada à tabela base `ANC_ABSENCE_CATEGORIES_F` pelo ID da categoria + idioma (`LANGUAGE`).

> [!note] Sufixos _F_TL
> Combina **date-effective** (`_F`) e **traduções** (`_TL`). Cada registro possui vigência temporal e idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Permite exibir nomes de categorias de ausência no idioma do usuário.
- **Self-service multilíngue:** Suporte a interfaces em múltiplos idiomas para funcionários globais.
- **Relatórios localizados:** Geração de relatórios no idioma local de cada unidade de negócio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da categoria de ausência | [[anc_absence_categories_f]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução (ex.: PT, EN, ES) | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 4 | ABSENCE_CATEGORY_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da categoria | — | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_categories_f]] — via `ABSENCE_CATEGORY_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Tradução de categorias em pt-BR
```sql
SELECT cat.ABSENCE_CATEGORY_ID, tl.ABSENCE_CATEGORY_NAME
FROM   ANC_ABSENCE_CATEGORIES_F cat
JOIN   ANC_ABSENCE_CATEGORIES_F_TL tl
  ON   cat.ABSENCE_CATEGORY_ID = tl.ABSENCE_CATEGORY_ID
WHERE  tl.LANGUAGE = 'PT'
  AND  SYSDATE BETWEEN cat.EFFECTIVE_START_DATE AND cat.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Traduções em português
- `LANGUAGE = USERENV('LANG')` — Idioma da sessão do usuário

---

## 🔒 Observações

- Sempre fazer JOIN com a tabela base `_F` para obter registros vigentes.
- O campo `SOURCE_LANG` indica o idioma de origem; se `SOURCE_LANG <> LANGUAGE`, a tradução pode ser automática.
- Registros com `LANGUAGE = SOURCE_LANG` são as traduções originais (inseridas manualmente).

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_CATEGORIES_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsencecategoriesftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
