---
id: DOC-HCM-553
doc_type: system-doc
title: "PAY_BALANCE_CATEGORIES_VL — Categorias de Saldo (View Localizada)"
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
  - balance-categories-vl
  - view-localizada
  - pay-bal-cat-vl
aliases:
  - PAY_BALANCE_CATEGORIES_VL
  - pay_balance_categories_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_CATEGORIES_VL

## 📌 Visão Geral

**View localizada** (`_VL`) que combina `PAY_BALANCE_CATEGORIES_F` com `PAY_BALANCE_CATEGORIES_TL` no idioma da sessao do usuario. Facilita consultas sem necessidade de join explicito com a tabela de traducao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de categorias de saldo com traducao
- Uso em LOVs (List of Values) de interfaces
- Relatorios no idioma do usuario

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_CATEGORY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da categoria | --- | 🟢 95% |
| 2 | CATEGORY_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome da categoria no idioma da sessao | --- | 🟢 90% |
| 3 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NOT NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Categorias de saldo com nome traduzido
```sql
SELECT vl.BALANCE_CATEGORY_ID, vl.CATEGORY_NAME
FROM   PAY_BALANCE_CATEGORIES_VL vl
WHERE  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.
- Retorna automaticamente o nome no idioma da sessao do usuario.
- Preferir esta view para consultas que necessitem nome traduzido.

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_CATEGORIES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancecategoriesvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
