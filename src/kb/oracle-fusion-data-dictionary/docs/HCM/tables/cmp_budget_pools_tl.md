---
id: DOC-HCM-066
doc_type: system-doc
title: "CMP_BUDGET_POOLS_TL — Traduções de Pools de Orçamento"
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
  - compensation
  - traducoes
  - translations
  - budget-pools-tl
aliases:
  - CMP_BUDGET_POOLS_TL
  - cmp_budget_pools_tl
  - pools-orcamento-tl
  - budget-pools-tl
  - cmp-budget-pools-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_BUDGET_POOLS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes e descrições dos pools de orçamento de compensação em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Nomes de pools no idioma do gestor.
- **Interface multilíngue:** Suporte a gestores em múltiplos países.
- **Relatórios localizados:** Nomes traduzidos em relatórios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUDGET_POOL_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do pool | [[cmp_budget_pools_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do pool | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_budget_pools_b]] — via `BUDGET_POOL_ID` (registro base do cadastro)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Nomes de pools em português
```sql
SELECT bp.BUDGET_POOL_ID, tl.NAME, tl.DESCRIPTION
FROM   CMP_BUDGET_POOLS_B bp
JOIN   CMP_BUDGET_POOLS_TL tl ON bp.BUDGET_POOL_ID = tl.BUDGET_POOL_ID
WHERE  tl.LANGUAGE = 'PT';
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Traduções em português

---

## 🔒 Observações

- Tabela de traduções vinculada à tabela base `CMP_BUDGET_POOLS_B`.
- Sempre fazer JOIN com a tabela base para obter dados técnicos.

---

## 🔗 PVOs Relacionados

### [[budgetpoolpvo|BudgetPoolPVO]] (HCM · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | BudgetPoolTLPEOCreatedBy | ✅ |
| CREATION_DATE | BudgetPoolTLPEOCreationDate | ✅ |
| LANGUAGE | BudgetPoolTLPEOLanguage | ✅ |
| LAST_UPDATE_DATE | BudgetPoolTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BudgetPoolTLPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BudgetPoolTLPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | BudgetPoolTLPEOObjectVersionNumber | ✅ |
| PLAN_ID | PlanId | ✅ |
| POOL_ID | BudgetPoolTLPEOPoolId1 | ✅ |
| POOL_NAME | BudgetPoolTLPEOPoolName | ✅ |
| SOURCE_LANG | BudgetPoolTLPEOSourceLang | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_BUDGET_POOLS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpbudgetpoolstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
