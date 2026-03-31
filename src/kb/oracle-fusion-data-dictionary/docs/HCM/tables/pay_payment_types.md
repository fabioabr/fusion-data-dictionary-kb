---
id: DOC-HCM-586
doc_type: system-doc
title: "PAY_PAYMENT_TYPES — Tipos de Pagamento"
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
  - payment-types
  - tipos-pagamento
  - pay-payment-types
aliases:
  - PAY_PAYMENT_TYPES
  - pay_payment_types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAYMENT_TYPES

## 📌 Visão Geral

Armazena os **tipos de pagamento** disponiveis no sistema (ex.: Check, Direct Deposit, Wire Transfer, Cash). Define as modalidades de pagamento suportadas pela legislacao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao de modalidades de pagamento por legislacao
- Base para configuracao de metodos de pagamento organizacionais
- Configuracao de regras de pagamento por tipo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do tipo de pagamento | --- | 🟢 95% |
| 2 | PAYMENT_TYPE_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do tipo de pagamento | --- | 🟢 90% |
| 3 | CATEGORY | VARCHAR2(30) | NULL | Classificacao | Categoria (Check, Wire, Direct Deposit) | --- | 🟢 85% |
| 4 | TERRITORY_CODE | VARCHAR2(2) | NULL | Classificacao | Codigo do pais | --- | 🟡 80% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | --- | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de configuracao raiz

### Tabelas-filha (FK de saída)
- [[pay_org_pay_methods_f]] --- via `PAYMENT_TYPE_ID` (métodos de pagamento do tipo)
- [[pay_payment_types_tl]] --- via `PAYMENT_TYPE_ID` (traduções do tipo de pagamento)

---

## 📎 Uso Típico

### Tipos de pagamento para legislacao brasileira
```sql
SELECT pt.PAYMENT_TYPE_ID, pt.PAYMENT_TYPE_NAME, pt.CATEGORY
FROM   PAY_PAYMENT_TYPES pt
WHERE  pt.TERRITORY_CODE = 'BR';
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_PAYMENT_TYPES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypaymenttypes.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
