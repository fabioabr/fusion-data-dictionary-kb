---
id: DOC-GL-020
doc_type: system-doc
title: "GL_JE_CATEGORIES_B — Categorias de Lançamentos (Base)"
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
  - classificacao
aliases:
  - GL_JE_CATEGORIES_B
  - gl_je_categories_b
  - categorias-lancamento-gl
  - journal-categories-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_CATEGORIES_B

## 📌 Visão Geral

Tabela base que armazena as **categorias de lançamentos contábeis** (journal categories) do General Ledger. Cada categoria classifica o tipo/natureza do lançamento (ex: Provisão, Ajuste, Depreciação, Importação de AP, etc.). É a tabela `_B` (base) que contém os dados não traduzíveis; os nomes e descrições traduzidos ficam em `GL_JE_CATEGORIES_TL`.

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** do padrão Oracle multi-idioma. Contém colunas não traduzíveis (IDs, flags, datas). Para nomes traduzidos, usar a view `_VL` ou a tabela `_TL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de lançamentos:** Toda entrada no GL é categorizada (ex: accrual, adjustment, depreciation).
- **Regras de posting:** Categorias podem ter regras específicas de contabilização.
- **Relatórios por tipo:** Agrupamento de lançamentos por categoria para análise gerencial.
- **Subledger Accounting:** O SLA atribui automaticamente a categoria conforme o tipo de transação do subledger.
- **Controle de acesso:** Políticas de segurança podem restringir quais categorias um usuário pode utilizar.
- **Configuração:** Definição de categorias customizadas para processos específicos da organização.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_CATEGORY_NAME | VARCHAR2(25) | NOT NULL | PK | Nome interno (chave) da categoria de lançamento | — | 🟢 100% |
| 2 | CONSOLIDATION_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a categoria é usada em consolidação (Y/N) | — | 🟢 90% |
| 3 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se a categoria está ativa (Y/N) | — | 🟢 95% |
| 4 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟢 90% |
| 5 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK — tabela de referência (lookup) de nível raiz.

### Tabelas-filha (FK de saída)
- [[gl_je_categories_tl]] — via `JE_CATEGORY_NAME` (traduções da categoria)
- [[gl_je_headers]] — via `JE_CATEGORY` (cabeçalhos de lançamento que referenciam a categoria)

---

## 📎 Uso Típico

### Listar categorias ativas
```sql
SELECT c.JE_CATEGORY_NAME,
       ct.USER_JE_CATEGORY_NAME,
       ct.DESCRIPTION
FROM   GL_JE_CATEGORIES_B c
JOIN   GL_JE_CATEGORIES_TL ct ON ct.JE_CATEGORY_NAME = c.JE_CATEGORY_NAME
  AND  ct.LANGUAGE = USERENV('LANG')
WHERE  c.ENABLED_FLAG = 'Y'
ORDER BY ct.USER_JE_CATEGORY_NAME;
```

### Lançamentos por categoria em um período
```sql
SELECT c.JE_CATEGORY_NAME,
       COUNT(*) AS qtd_journals,
       SUM(h.RUNNING_TOTAL_DR) AS total_debito
FROM   GL_JE_HEADERS h
JOIN   GL_JE_CATEGORIES_B c ON c.JE_CATEGORY_NAME = h.JE_CATEGORY
WHERE  h.LEDGER_ID = :p_ledger_id
  AND  h.PERIOD_NAME = 'MAR-26'
GROUP BY c.JE_CATEGORY_NAME
ORDER BY total_debito DESC;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Categorias ativas
- `CONSOLIDATION_FLAG = 'Y'` — Categorias de consolidação
- Categorias padrão Oracle: 'Adjustment', 'Accrual', 'Revaluation', 'Consolidation', etc.

---

## 🔒 Observações

- A chave primária é `JE_CATEGORY_NAME` (alfanumérica), não um ID numérico — diferente do padrão usual Oracle.
- Categorias **seeded** (pré-definidas pela Oracle) incluem: Adjustment, Accrual, Budget, Closing, Consolidation, Opening, Revaluation, Translation, etc.
- Organizações podem criar categorias customizadas para processos específicos.
- Para obter o nome da categoria no idioma do usuário, fazer JOIN com `GL_JE_CATEGORIES_TL`.
- O `CONSOLIDATION_FLAG` identifica categorias utilizadas no processo de consolidação entre ledgers.

---

## 🔗 PVOs Relacionados

### [[journalcategorybpvo|JournalCategoryBPVO]] (GL · BICC: 3/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CONSOLIDATION_FLAG | JrnlCatConsolidationFlag | — |
| CREATED_BY | JrnlCatCreatedBy | — |
| CREATION_DATE | JrnlCatCreationDate | — |
| JE_CATEGORY_KEY | JrnlCatJeCategoryKey | ✅ |
| JE_CATEGORY_NAME | JeCategoryName | ✅ |
| LAST_UPDATE_DATE | JrnlCatLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlCatLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlCatLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | JrnlCatObjectVersionNumber | — |

### [[journalcategoryextractpvo|JournalCategoryExtractPVO]] (OTHER · BICC: 8/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | JournalCategoryAttribute1 | — |
| ATTRIBUTE2 | JournalCategoryAttribute2 | — |
| ATTRIBUTE3 | JournalCategoryAttribute3 | — |
| ATTRIBUTE4 | JournalCategoryAttribute4 | — |
| ATTRIBUTE5 | JournalCategoryAttribute5 | — |
| ATTRIBUTE_CATEGORY | JournalCategoryAttrCategory | — |
| CREATED_BY | JournalCategoryCreatedBy | ✅ |
| CREATION_DATE | JournalCategoryCreationDate | ✅ |
| JE_CATEGORY_KEY | JournalCategoryJeCategoryKey | ✅ |
| JE_CATEGORY_NAME | JournalCategoryJeCategoryName | ✅ |
| LAST_UPDATE_DATE | JournalCategoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JournalCategoryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JournalCategoryLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | JournalCategoryObjectVerNum | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL_JE_CATEGORIES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljecategories-25720.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
