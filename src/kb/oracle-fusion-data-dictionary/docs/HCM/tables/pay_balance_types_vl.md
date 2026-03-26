---
id: DOC-HCM-556
doc_type: system-doc
title: "PAY_BALANCE_TYPES_VL — Tipos de Saldo (View Localizada)"
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
  - balance-types-vl
  - view-localizada
  - pay-bal-types-vl
aliases:
  - PAY_BALANCE_TYPES_VL
  - pay_balance_types_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_TYPES_VL

## 📌 Visão Geral

**View localizada** (`_VL`) que combina a tabela base de tipos de saldo com traducoes no idioma da sessao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de tipos de saldo com traducao
- Uso em LOVs e interfaces de configuracao de folha

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de saldo | --- | 🟢 95% |
| 2 | BALANCE_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do saldo no idioma da sessao | --- | 🟢 90% |
| 3 | REPORTING_NAME | VARCHAR2(80) | NULL | Identificacao | Nome para relatorios | --- | 🟡 80% |
| 4 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NULL | FK | ID do grupo legislativo | --- | 🟢 85% |
| 5 | BALANCE_CATEGORY_ID | NUMBER(18) | NULL | FK | ID da categoria de saldo | PAY_BALANCE_CATEGORIES_F | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela base de tipos de saldo

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Tipos de saldo com nome traduzido
```sql
SELECT vl.BALANCE_TYPE_ID, vl.BALANCE_NAME, vl.REPORTING_NAME
FROM   PAY_BALANCE_TYPES_VL vl
WHERE  vl.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.
- Retorna automaticamente o nome no idioma da sessao do usuario.

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_TYPES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancetypesvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
