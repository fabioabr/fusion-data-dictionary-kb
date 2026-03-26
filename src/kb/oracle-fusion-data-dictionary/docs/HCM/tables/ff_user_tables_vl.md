---
id: DOC-HCM-097
doc_type: system-doc
title: "FF_USER_TABLES_VL — Tabelas de Usuário Fast Formula (View Localized)"
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
  - tabelas-usuario
  - user-tables
  - lookup-config
aliases:
  - FF_USER_TABLES_VL
  - ff_user_tables_vl
  - ff-user-tables-vl
  - DOC-HCM-097
  - tabelas-de-usuário-fast-formula-(view-localized)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# FF_USER_TABLES_VL

## 📌 Visão Geral

**View localizada** que apresenta as **tabelas de usuário** do Fast Formula. Cada tabela define uma estrutura de dados de referência (lookup table) consultável por fórmulas de cálculo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de tabelas de referência:** Cadastro central de tabelas FF.
- **Configuração de lookups:** Tabelas de parâmetros para processamento de folha.
- **Documentação:** Inventário de todas as tabelas de dados auxiliares.
- **Manutenção:** Gestão de tabelas sem necessidade de alterar fórmulas.
- **Classificação:** Identificação de tabelas por legislação e grupo de negócios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_TABLE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tabela | — | 🟢 95% |
| 2 | USER_TABLE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome da tabela | — | 🟢 95% |
| 3 | MATCH_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de match (MATCH, RANGE) | — | 🟢 90% |
| 4 | RANGE_OR_DATA_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de dado do range (TEXT, NUMBER, DATE) | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição da tabela | — | 🟡 80% |
| 6 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código de legislação | — | 🟢 90% |
| 7 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 80% |
| 8 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início de vigência | — | 🟡 80% |
| 9 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigência | — | 🟡 80% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo de negócios)

### Tabelas-filha (FK de saída)
- [[ff_user_columns_vl]] — via `USER_TABLE_ID` (colunas da tabela de usuario)
- [[ff_user_rows_f]] — via `USER_TABLE_ID` (linhas da tabela de usuario)

---

## 📎 Uso Típico

### Todas as tabelas FF ativas
```sql
SELECT t.USER_TABLE_ID, t.USER_TABLE_NAME, t.MATCH_TYPE,
       t.RANGE_OR_DATA_TYPE, t.LEGISLATION_CODE
FROM   FF_USER_TABLES_VL t;
```

### Tabelas por legislação brasileira
```sql
SELECT t.USER_TABLE_NAME, t.DESCRIPTION
FROM   FF_USER_TABLES_VL t
WHERE  t.LEGISLATION_CODE = 'BR';
```

---

## 🔒 Observações

- Esta é uma **view localizada** (_VL) — combina _B + _TL.
- O `MATCH_TYPE` define como as linhas são pesquisadas: MATCH (exato) ou RANGE (por faixa).
- O `RANGE_OR_DATA_TYPE` define o tipo do campo de busca nas linhas.
- Tabelas FF são muito usadas para parametrizar cálculos de payroll e benefits sem programação.

---

## 📚 Referências

- [Oracle Docs — FF_USER_TABLES_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ffusertablesvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
