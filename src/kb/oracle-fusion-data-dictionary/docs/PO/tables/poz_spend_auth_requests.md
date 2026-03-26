---
id: DOC-PO-087
doc_type: system-doc
title: "POZ_SPEND_AUTH_REQUESTS — Solicitações de Autorização de Gasto"
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
  - spend-authorization
  - aprovacao
  - controle-gastos
aliases:
  - POZ_SPEND_AUTH_REQUESTS
  - poz_spend_auth_requests
  - autorizacao-gasto
  - spend-authorization-requests
  - aprovacao-gasto-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SPEND_AUTH_REQUESTS

## Visão Geral

Armazena as **solicitações de autorização de gasto** associadas a fornecedores no Oracle Procurement. Cada registro representa uma requisição para autorizar gastos com um fornecedor específico, incluindo limites de valor, período de vigência e status de aprovação. Integra o fluxo de controle de spend authorization do Supplier Qualification Management.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de gastos:** Estabelece limites de autorização de gasto por fornecedor/categoria.
- **Qualificação de fornecedores:** Parte do processo de qualificação que define quanto pode ser gasto com cada fornecedor.
- **Workflow de aprovação:** Controla o fluxo de aprovação de novas autorizações ou alterações de limites.
- **Compliance:** Garante que gastos com fornecedores respeitem os limites autorizados.
- **Análise de spend:** Suporta relatórios de utilização versus autorização de gastos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SPEND_AUTH_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da solicitação de autorização | — | 🟡 70% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Identificador do site do fornecedor | [[poz_supplier_sites_all_m]] | 🟡 70% |
| 4 | AUTHORIZED_AMOUNT | NUMBER | NULL | Financeiro | Valor autorizado de gasto | — | 🟡 70% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda do valor autorizado | [[fnd_currencies]] | 🟡 70% |
| 6 | START_DATE | DATE | NULL | Vigência | Data de início da autorização | — | 🟡 70% |
| 7 | END_DATE | DATE | NULL | Vigência | Data de término da autorização | — | 🟡 70% |
| 8 | REQUEST_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: PENDING, APPROVED, REJECTED, EXPIRED | — | 🟡 75% |
| 9 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compras associada | — | 🟡 65% |
| 10 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 70% |
| 11 | JUSTIFICATION | VARCHAR2(2000) | NULL | Texto livre | Justificativa da solicitação de autorização | — | 🟡 65% |
| 12 | APPROVED_BY | NUMBER(18) | NULL | Aprovação | Usuário que aprovou a solicitação | — | 🟡 65% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor da solicitação de autorização de gastos)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da solicitação de autorização de gastos)

### Tabelas relacionadas

---

## Uso Típico

### Autorizações ativas por fornecedor
```sql
SELECT sar.SPEND_AUTH_REQUEST_ID, sar.AUTHORIZED_AMOUNT,
       sar.CURRENCY_CODE, sar.START_DATE, sar.END_DATE
FROM   POZ_SPEND_AUTH_REQUESTS sar
WHERE  sar.VENDOR_ID = :p_vendor_id
  AND  sar.REQUEST_STATUS = 'APPROVED'
  AND  SYSDATE BETWEEN sar.START_DATE AND NVL(sar.END_DATE, SYSDATE);
```

### Total autorizado por BU
```sql
SELECT sar.ORG_ID, SUM(sar.AUTHORIZED_AMOUNT) AS total_autorizado,
       COUNT(*) AS qtd_autorizacoes
FROM   POZ_SPEND_AUTH_REQUESTS sar
WHERE  sar.REQUEST_STATUS = 'APPROVED'
  AND  SYSDATE BETWEEN sar.START_DATE AND NVL(sar.END_DATE, SYSDATE)
GROUP BY sar.ORG_ID;
```

---

## Observações

- As autorizações de gasto são tipicamente vinculadas ao processo de **Supplier Qualification Management (SQM)**.
- O campo `REQUEST_STATUS` controla o ciclo de vida: PENDING → APPROVED/REJECTED; autorizações expiradas são marcadas como EXPIRED.
- O valor `AUTHORIZED_AMOUNT` representa o **limite máximo** de gasto; o gasto real é rastreado nas tabelas de PO e AP.
- Autorizações podem ser por fornecedor (geral) ou por fornecedor + categoria (granular).

---

## Referências

- [Oracle Docs — Spend Authorization](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
