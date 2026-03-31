---
id: DOC-HCM-585
doc_type: system-doc
title: "PAY_PAYMENT_COSTS — Custos de Pagamento"
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
  - payment-costs
  - custos-pagamento
  - pay-payment-costs
aliases:
  - PAY_PAYMENT_COSTS
  - pay_payment_costs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAYMENT_COSTS

## 📌 Visão Geral

Armazena os **custos de pagamento** gerados durante o processamento de pre-pagamento. Registra a distribuicao contabil especifica para os pagamentos efetivos (vs. custos gerais em `PAY_COSTS`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Distribuicao contabil de custos de pagamento efetivos
- Reconciliacao entre custos de calculo e pagamento
- Integracao com contabilidade geral (GL)

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_COST_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do custo de pagamento | --- | 🟢 85% |
| 2 | PRE_PAYMENT_ID | NUMBER(18) | NOT NULL | FK | ID do pre-pagamento | PAY_PRE_PAYMENTS | 🟢 85% |
| 3 | COST_ID | NUMBER(18) | NULL | FK | ID do custo original | PAY_COSTS | 🟡 75% |
| 4 | COSTED_VALUE | NUMBER | NULL | Dados | Valor do custo de pagamento | --- | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | --- | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_pre_payments]] --- via `PRE_PAYMENT_ID` (pré-pagamento que gerou o custo)
- [[pay_costs]] --- via `COST_ID` (custo de folha vinculado ao pagamento)

### Tabelas-filha (FK de saída)
- --- Tabela de custo, sem filhas conhecidas

---

## 📎 Uso Típico

### Custos de um pre-pagamento
```sql
SELECT pc.PAYMENT_COST_ID, pc.COSTED_VALUE
FROM   PAY_PAYMENT_COSTS pc
WHERE  pc.PRE_PAYMENT_ID = :p_pre_payment_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_PAYMENT_COSTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypaymentcosts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
