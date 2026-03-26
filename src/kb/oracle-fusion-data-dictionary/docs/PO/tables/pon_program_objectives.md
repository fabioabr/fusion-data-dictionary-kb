---
id: DOC-PO-030
doc_type: system-doc
title: "PON_PROGRAM_OBJECTIVES — Objetivos de Programas de Sourcing"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - objectives
  - programs
  - sourcing
  - strategic-sourcing
aliases:
  - PON_PROGRAM_OBJECTIVES
  - pon_program_objectives
  - objetivos-programas-sourcing
  - program-objectives
  - pon-objectives
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_PROGRAM_OBJECTIVES

## 📌 Visão Geral

Armazena os **objetivos estratégicos** definidos dentro de programas de sourcing. Cada objetivo representa uma meta específica do programa — como "reduzir custos de TI em 15%" ou "consolidar fornecedores de logística" — e serve como contêiner para as negociações que o atendem (via [[pon_objective_negotiations]]).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento estratégico de sourcing:** Define os objetivos mensuráveis que um programa deve alcançar.
- **Estruturação de programas:** Cada programa ([[pon_program_headers]]) é dividido em objetivos com metas individuais.
- **Acompanhamento de progresso:** Permite medir o progresso de cada objetivo separadamente.
- **Metas de economia:** Define savings targets por objetivo, com acompanhamento de valores realizados.
- **Relatórios OTBI:** Alimenta a view [[pon_obj_agg_to_prog_otbi_v]] para análises de portfólio.
- **Alinhamento organizacional:** Vincula objetivos de sourcing a categorias de compra e áreas de negócio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OBJECTIVE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do objetivo | — | 🟢 90% |
| 2 | PROGRAM_ID | NUMBER(18) | NOT NULL | FK | Identificador do programa de sourcing | [[pon_program_headers]] | 🟢 90% |
| 3 | OBJECTIVE_NAME | VARCHAR2(240) | NOT NULL | Descritivo | Nome do objetivo | — | 🟢 85% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Descritivo | Descrição detalhada do objetivo | — | 🟢 85% |
| 5 | OBJECTIVE_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: OPEN, IN_PROGRESS, COMPLETED, CANCELLED | — | 🟢 85% |
| 6 | OBJECTIVE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de objetivo (ex: COST_REDUCTION, SUPPLIER_CONSOLIDATION, QUALITY_IMPROVEMENT) | — | 🟡 65% |
| 7 | PRIORITY | VARCHAR2(30) | NULL | Classificação | Prioridade do objetivo (HIGH, MEDIUM, LOW) | — | 🟡 65% |
| 8 | OWNER_ID | NUMBER(18) | NULL | FK | Responsável pelo objetivo | — | 🟡 70% |
| 9 | START_DATE | DATE | NULL | Data | Data de início planejada | — | 🟢 85% |
| 10 | END_DATE | DATE | NULL | Data | Data de término planejada | — | 🟢 85% |
| 11 | TARGET_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Meta de economia do objetivo | — | 🟡 70% |
| 12 | TARGET_SAVINGS_PERCENTAGE | NUMBER | NULL | Financeiro | Meta de economia percentual | — | 🟡 65% |
| 13 | ACTUAL_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Economia realizada | — | 🟡 65% |
| 14 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 70% |
| 15 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de procurement associada | — | 🟡 65% |
| 16 | ESTIMATED_SPEND | NUMBER | NULL | Financeiro | Gasto estimado coberto pelo objetivo | — | 🟡 60% |
| 17 | COMPLETION_PERCENTAGE | NUMBER | NULL | Métrica | Percentual de conclusão do objetivo | — | 🟡 55% |
| 18 | SEQUENCE_NUMBER | NUMBER | NULL | Ordenação | Número de sequência para ordenação dentro do programa | — | 🟡 60% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 23 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 24 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 90% |
| 25 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_program_headers]] — via `PROGRAM_ID` (programa ao qual o objetivo pertence)

### Tabelas-filha (FK de saída)
- [[pon_objective_negotiations]] — via `OBJECTIVE_ID` (negociações vinculadas ao objetivo)
- [[pon_neg_agg_to_obj_otbi_v]] — via `OBJECTIVE_ID` (view OTBI de negociações por objetivo)
- [[pon_obj_agg_to_prog_otbi_v]] — via `OBJECTIVE_ID` (view OTBI de objetivos por programa)

---

## 📎 Uso Típico

### Objetivos de um programa específico
```sql
SELECT po.OBJECTIVE_ID, po.OBJECTIVE_NAME, po.OBJECTIVE_STATUS,
       po.PRIORITY, po.TARGET_SAVINGS_AMOUNT, po.ACTUAL_SAVINGS_AMOUNT,
       po.COMPLETION_PERCENTAGE
FROM   PON_PROGRAM_OBJECTIVES po
WHERE  po.PROGRAM_ID = :p_program_id
ORDER BY po.SEQUENCE_NUMBER;
```

### Objetivos abertos com meta de economia
```sql
SELECT po.OBJECTIVE_NAME, po.TARGET_SAVINGS_AMOUNT,
       po.ACTUAL_SAVINGS_AMOUNT, po.START_DATE, po.END_DATE,
       ROUND((po.ACTUAL_SAVINGS_AMOUNT / NULLIF(po.TARGET_SAVINGS_AMOUNT, 0)) * 100, 2)
         AS pct_atingida
FROM   PON_PROGRAM_OBJECTIVES po
WHERE  po.OBJECTIVE_STATUS IN ('OPEN', 'IN_PROGRESS')
  AND  po.TARGET_SAVINGS_AMOUNT > 0
ORDER BY po.TARGET_SAVINGS_AMOUNT DESC;
```

### Objetivos com negociações vinculadas
```sql
SELECT po.OBJECTIVE_NAME, po.OBJECTIVE_STATUS,
       COUNT(on2.OBJECTIVE_NEGOTIATION_ID) AS qtd_negociacoes,
       SUM(on2.AWARDED_AMOUNT) AS total_adjudicado
FROM   PON_PROGRAM_OBJECTIVES po
LEFT JOIN PON_OBJECTIVE_NEGOTIATIONS on2 ON on2.OBJECTIVE_ID = po.OBJECTIVE_ID
WHERE  po.PROGRAM_ID = :p_program_id
GROUP BY po.OBJECTIVE_NAME, po.OBJECTIVE_STATUS
ORDER BY po.OBJECTIVE_NAME;
```

---

## 🔒 Observações

- O objetivo é o **nível intermediário** da hierarquia: Programa > Objetivos > Negociações.
- O campo `OBJECTIVE_STATUS` controla o ciclo de vida: **OPEN** (criado, sem negociações ativas), **IN_PROGRESS** (negociações em andamento), **COMPLETED** (todas as negociações concluídas), **CANCELLED** (cancelado).
- A coluna `PRIORITY` pode ser utilizada para priorização na tela de gestão de programas.
- Os campos `TARGET_SAVINGS_AMOUNT` e `ACTUAL_SAVINGS_AMOUNT` são críticos para relatórios de ROI de procurement.
- O `SEQUENCE_NUMBER` define a ordem de exibição dos objetivos na interface do programa.
- Os atributos DFF (`ATTRIBUTE1–15`) podem ser customizados por implementação.
- Um objetivo sem negociações vinculadas ([[pon_objective_negotiations]]) é considerado "não iniciado" nos dashboards OTBI.

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
