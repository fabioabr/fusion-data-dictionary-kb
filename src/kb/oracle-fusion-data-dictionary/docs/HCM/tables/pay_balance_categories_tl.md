---
id: DOC-HCM-552
doc_type: system-doc
title: "PAY_BALANCE_CATEGORIES_TL — Categorias de Saldo (Traducoes)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - balance-categories-tl
  - traducoes
  - pay-bal-cat-tl
aliases:
  - PAY_BALANCE_CATEGORIES_TL
  - pay_balance_categories_tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_CATEGORIES_TL

## 📌 Visão Geral

Armazena as **traducoes** dos nomes das categorias de saldo para multiplos idiomas. Tabela `_TL` vinculada a `PAY_BALANCE_CATEGORIES_F`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Suporte multiidioma para categorias de saldo
- Exibicao localizada em contracheques e relatorios

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da categoria (chave composta) | PAY_BALANCE_CATEGORIES_F | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | --- | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Dados | Idioma de origem | --- | 🟢 85% |
| 4 | CATEGORY_NAME | VARCHAR2(80) | NULL | Identificacao | Nome traduzido da categoria | --- | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_balance_categories_f]] --- via `BALANCE_CATEGORY_ID` (tabela base da categoria de saldo)

### Tabelas-filha (FK de saída)
- --- Tabela de traducao, sem filhas

---

## 📎 Uso Típico

### Traducao da categoria no idioma corrente
```sql
SELECT tl.CATEGORY_NAME
FROM   PAY_BALANCE_CATEGORIES_TL tl
WHERE  tl.BALANCE_CATEGORY_ID = :p_category_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[balancecategory|BalanceCategory]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BALANCE_CATEGORY_ID | BalanceCategoryBaseDPEOBalanceCategoryId | — |
| LANGUAGE | BalanceCategoryBaseDPEOLanguage | ✅ |
| SOURCE_LANG | BalanceCategoryBaseDPEOSourceLang | ✅ |
| USER_CATEGORY_NAME | BalanceCategoryBaseDPEOUserCategoryName | — |

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_CATEGORIES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancecategoriestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
