---
id: DOC-HCM-378
doc_type: system-doc
title: "HWM_TM_HIS_ENTRY_V — View Histórica de Entradas de Tempo"
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
  - time-management
  - time-entry
  - historico-tempo
  - view
aliases:
  - HWM_TM_HIS_ENTRY_V
  - hwm_tm_his_entry_v
  - hwm-tm-his-entry-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_HIS_ENTRY_V

## 📌 Visão Geral

View que apresenta o **histórico de entradas de tempo** (time entries) no módulo Time Management. Consolida dados de horas trabalhadas, horas extras e outras entradas temporais já processadas.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** — consulta pré-definida sobre tabelas base, somente leitura.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta histórica de time cards:** visualizar entradas de tempo já processadas.
- **Análise de horas trabalhadas:** base para relatórios de produtividade.
- **Auditoria de ponto:** rastreabilidade de registros de tempo anteriores.
- **Integração com folha de pagamento:** dados consolidados para cálculo retroativo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 2 | TIME_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador da entrada de tempo | — | 🟡 65% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Identificador da atribuição | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | START_TIME | TIMESTAMP | NULL | Período | Hora de início | — | 🟡 65% |
| 5 | STOP_TIME | TIMESTAMP | NULL | Período | Hora de término | — | 🟡 65% |
| 6 | MEASURE | NUMBER | NULL | Dados | Quantidade de horas/unidades | — | 🟡 60% |
| 7 | ENTRY_DATE | DATE | NOT NULL | Período | Data da entrada de tempo | — | 🟡 70% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificação | Status da entrada | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (dados do colaborador)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Histórico de entradas de tempo por período
```sql
SELECT v.PERSON_ID, v.ENTRY_DATE, v.MEASURE,
       v.START_TIME, v.STOP_TIME, v.STATUS
FROM   HWM_TM_HIS_ENTRY_V v
WHERE  v.ENTRY_DATE BETWEEN :dt_ini AND :dt_fim
  AND  v.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `ENTRY_DATE BETWEEN :dt_ini AND :dt_fim — Filtrar por período`

---

## 🔒 Observações

- View somente leitura — não suporta DML.
- Para entradas ativas/pendentes, consultar as tabelas base do time card.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_HIS_ENTRY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmhisentryv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
