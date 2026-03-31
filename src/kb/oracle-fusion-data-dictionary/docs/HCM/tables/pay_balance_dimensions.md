---
id: DOC-HCM-554
doc_type: system-doc
title: "PAY_BALANCE_DIMENSIONS — Dimensoes de Saldo de Folha"
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
  - balance-dimensions
  - dimensoes-saldo
  - pay-bal-dimensions
aliases:
  - PAY_BALANCE_DIMENSIONS
  - pay_balance_dimensions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_BALANCE_DIMENSIONS

## 📌 Visão Geral

Armazena as **dimensoes de saldo** que definem o escopo temporal ou contextual de acumulacao de saldos (ex.: PTD - Period to Date, MTD - Month to Date, YTD - Year to Date, LTD - Lifetime to Date).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de escopos de acumulacao de saldos
- Configuracao de periodos de reset de saldos
- Base para calculo de saldos acumulados em diferentes horizontes

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BALANCE_DIMENSION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da dimensao | --- | 🟢 90% |
| 2 | DIMENSION_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome da dimensao de saldo | --- | 🟢 85% |
| 3 | DIMENSION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo (PTD, MTD, QTD, YTD, LTD) | --- | 🟢 85% |
| 4 | LEGISLATIVE_DATA_GROUP_ID | NUMBER(18) | NULL | FK | ID do grupo legislativo | --- | 🟢 80% |
| 5 | DATABASE_ITEM_SUFFIX | VARCHAR2(80) | NULL | Dados | Sufixo para database items | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz

### Tabelas-filha (FK de saída)
- [[pay_balance_validation]] --- via `BALANCE_DIMENSION_ID` (validações da dimensão de saldo)

---

## 📎 Uso Típico

### Dimensoes de saldo por grupo legislativo
```sql
SELECT bd.BALANCE_DIMENSION_ID, bd.DIMENSION_NAME, bd.DIMENSION_TYPE
FROM   PAY_BALANCE_DIMENSIONS bd
WHERE  bd.LEGISLATIVE_DATA_GROUP_ID = :p_ldg_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_BALANCE_DIMENSIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paybalancedimensions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
