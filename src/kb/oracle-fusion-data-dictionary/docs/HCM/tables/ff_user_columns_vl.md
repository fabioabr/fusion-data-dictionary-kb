---
id: DOC-HCM-093
doc_type: system-doc
title: "FF_USER_COLUMNS_VL — Colunas de Tabelas de Usuário Fast Formula (View Localized)"
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
  - fast-formula
  - user-columns
  - tabelas-usuario
  - lookup
aliases:
  - FF_USER_COLUMNS_VL
  - ff_user_columns_vl
  - ff-user-columns-vl
  - DOC-HCM-093
  - colunas-de-tabelas-de-usuário-fast-formula-(view-l
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# FF_USER_COLUMNS_VL

## 📌 Visão Geral

**View localizada** que apresenta as **colunas definidas pelo usuário** em tabelas Fast Formula. Cada coluna define um campo de dados que pode ser consultado por fórmulas de cálculo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de dados:** Colunas de tabelas usadas por Fast Formulas.
- **Configuração de lookup:** Mapeamento de colunas para busca de valores.
- **Manutenção de tabelas auxiliares:** Gestão de estrutura de tabelas de referência.
- **Documentação de dados:** Inventário de colunas disponíveis em tabelas FF.
- **Troubleshooting:** Diagnóstico de problemas de referência a colunas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_COLUMN_ID | NUMBER(18) | NOT NULL | PK | Identificador único da coluna | — | 🟢 95% |
| 2 | USER_TABLE_ID | NUMBER(18) | NOT NULL | FK | Tabela de usuário | [[ff_user_tables_vl]] | 🟢 95% |
| 3 | USER_COLUMN_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome da coluna | — | 🟢 95% |
| 4 | FORMULA_ID | NUMBER(18) | NULL | FK | Fórmula de validação | [[ff_formulas_vl]] | 🟡 75% |
| 5 | DATA_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de dado (TEXT, NUMBER, DATE) | — | 🟡 80% |
| 6 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição da coluna | — | 🟡 80% |
| 7 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código de legislação | — | 🟢 90% |
| 8 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 80% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ff_user_tables_vl]] — via `USER_TABLE_ID` (tabela pai)
- [[ff_formulas_vl]] — via `FORMULA_ID` (fórmula de validação)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo empresarial da coluna de usuario)

### Tabelas-filha (FK de saída)
- [[ff_user_column_instances_f]] — via `USER_COLUMN_ID` (instâncias de valores)

---

## 📎 Uso Típico

### Colunas de uma tabela específica
```sql
SELECT uc.USER_COLUMN_ID, uc.USER_COLUMN_NAME, uc.DATA_TYPE, uc.DESCRIPTION
FROM   FF_USER_COLUMNS_VL uc
WHERE  uc.USER_TABLE_ID = :p_table_id;
```

### Todas as colunas com fórmula de validação
```sql
SELECT uc.USER_COLUMN_NAME, uc.FORMULA_ID, uc.DATA_TYPE
FROM   FF_USER_COLUMNS_VL uc
WHERE  uc.FORMULA_ID IS NOT NULL;
```

---

## 🔒 Observações

- Esta é uma **view localizada** (_VL) — combina _B + _TL para o idioma da sessão.
- Cada coluna pertence a uma tabela de usuário (`FF_USER_TABLES_VL`).
- O `DATA_TYPE` define o tipo de dado esperado nos valores da coluna.
- Colunas com `FORMULA_ID` preenchido utilizam fórmula para validação de entrada.

---

## 📚 Referências

- [Oracle Docs — FF_USER_COLUMNS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ffusercolumnsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
