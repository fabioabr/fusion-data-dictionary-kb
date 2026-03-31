---
id: DOC-AP-016
doc_type: system-doc
title: "AP_INV_SELECTION_CRITERIA_ALL — Critérios de Seleção de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - selecao-pagamento
  - payment-selection
  - payment-process-request
aliases:
  - AP_INV_SELECTION_CRITERIA_ALL
  - ap_inv_selection_criteria_all
  - criterios-selecao-ap
  - payment-selection-criteria
  - selecao-pagamento-ap
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_INV_SELECTION_CRITERIA_ALL

## 📌 Visão Geral

Armazena os **critérios de seleção** utilizados no Payment Process Request (PPR) do módulo Accounts Payable. Cada registro representa um conjunto de filtros (fornecedor, data de vencimento, grupo de pagamento, moeda, etc.) definidos pelo usuário para selecionar faturas elegíveis para pagamento em lote. É a tabela de configuração das "corridas de pagamento" (payment batches/runs).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Payment Process Request (PPR):** Definição dos critérios para seleção automática de faturas elegíveis a pagamento.
- **Controle de cash flow:** Permite filtrar faturas por data de vencimento para gestão de fluxo de caixa.
- **Segregação de pagamentos:** Critérios separados por grupo de pagamento, moeda ou fornecedor.
- **Auditoria de pagamentos:** Rastreabilidade dos parâmetros usados em cada corrida de pagamento.
- **Reprocessamento:** Possibilidade de consultar e reutilizar critérios de seleções anteriores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INV_SELECTION_CRITERIA_ID | NUMBER(18) | NOT NULL | PK | Identificador único do critério de seleção | — | 🟢 100% |
| 2 | CHECKRUN_NAME | VARCHAR2(100) | NOT NULL | Identificação | Nome da corrida de pagamento (PPR) | — | 🟢 100% |
| 3 | CHECK_DATE | DATE | NULL | Data | Data do pagamento/check | — | 🟢 100% |
| 4 | PAY_THRU_DATE | DATE | NULL | Data | Data limite de vencimento para seleção | — | 🟢 100% |
| 5 | PAY_FROM_DATE | DATE | NULL | Data | Data inicial de vencimento para seleção | — | 🟡 75% |
| 6 | VENDOR_ID_FROM | NUMBER(18) | NULL | Filtro fornecedor | Fornecedor inicial do range | [[poz_suppliers]] | 🟢 100% |
| 7 | VENDOR_ID_TO | NUMBER(18) | NULL | Filtro fornecedor | Fornecedor final do range | [[poz_suppliers]] | 🟢 100% |
| 8 | VENDOR_SITE_ID | NUMBER(18) | NULL | Filtro fornecedor | Site específico do fornecedor | [[poz_supplier_sites_all_m]] | 🟡 75% |
| 9 | PAY_GROUP_LOOKUP_CODE | VARCHAR2(25) | NULL | Filtro | Grupo de pagamento | [[ap_lookup_codes]] | 🟢 100% |
| 10 | PAYMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Filtro | Moeda do pagamento | — | 🟢 100% |
| 11 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Filtro | Método de pagamento | [[iby_payment_methods_b]] | 🟢 100% |
| 12 | INTERNAL_BANK_ACCOUNT_ID | NUMBER(18) | NULL | Bancário | Conta bancária de origem | [[ce_bank_accounts]] | 🟢 100% |
| 13 | PAYMENT_DOCUMENT_ID | NUMBER(18) | NULL | Bancário | Documento de pagamento (talão de cheques) | — | 🟡 75% |
| 14 | PAYMENT_PRIORITY_FROM | NUMBER | NULL | Filtro | Prioridade de pagamento inicial | — | 🟢 100% |
| 15 | PAYMENT_PRIORITY_TO | NUMBER | NULL | Filtro | Prioridade de pagamento final | — | 🟢 100% |
| 16 | ZERO_AMOUNTS_ALLOWED | VARCHAR2(25) | NULL | Controle | Permite faturas com valor zero (Y/N) | — | 🟡 75% |
| 17 | ZERO_INV_ALLOWED | VARCHAR2(25) | NULL | Controle | Permite pagamento zero (Y/N) | — | 🟡 75% |
| 18 | STATUS | VARCHAR2(25) | NULL | Status | Status da corrida de pagamento | — | 🟢 100% |
| 19 | PAYMENT_PROCESS_REQUEST_NAME | VARCHAR2(240) | NULL | Identificação | Nome do Payment Process Request | — | 🟢 100% |
| 20 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | Multi-Org | Entidade legal | [[xle_entity_profiles]] | 🟢 100% |
| 21 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 22 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 23 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 24 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 25 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 26 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID_FROM` / `VENDOR_ID_TO` (range de fornecedores)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[iby_payment_methods_b]] — via `PAYMENT_METHOD_CODE` (método de pagamento)
- [[ce_bank_accounts]] — via `INTERNAL_BANK_ACCOUNT_ID` (conta bancária interna usada no critério de seleção de pagamento)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal do critério de seleção de pagamento)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do critério de seleção de pagamento)

### Tabelas-filha (FK de saída)
- [[ap_selected_invoices_all]] — via `CHECKRUN_NAME` (faturas selecionadas pela corrida) 🟡 75%

---

## 📎 Uso Típico

### Listar corridas de pagamento recentes
```sql
SELECT asc1.CHECKRUN_NAME, asc1.CHECK_DATE,
       asc1.PAY_THRU_DATE, asc1.STATUS,
       asc1.PAYMENT_CURRENCY_CODE
FROM   AP_INV_SELECTION_CRITERIA_ALL asc1
WHERE  asc1.CREATION_DATE >= SYSDATE - 30
  AND  asc1.ORG_ID = :p_org_id
ORDER BY asc1.CREATION_DATE DESC;
```

### Critérios de uma corrida específica
```sql
SELECT asc1.CHECKRUN_NAME, asc1.PAY_FROM_DATE, asc1.PAY_THRU_DATE,
       asc1.PAY_GROUP_LOOKUP_CODE, asc1.PAYMENT_METHOD_CODE,
       ps.VENDOR_NAME AS fornecedor_de
FROM   AP_INV_SELECTION_CRITERIA_ALL asc1
LEFT JOIN POZ_SUPPLIERS ps ON ps.VENDOR_ID = asc1.VENDOR_ID_FROM
WHERE  asc1.CHECKRUN_NAME = :p_checkrun_name;
```

### Filtros comuns
- `STATUS = 'FORMATTED'` — Corridas já formatadas (checks emitidos)
- `CHECK_DATE BETWEEN :start AND :end` — Período de data dos checks
- `PAYMENT_CURRENCY_CODE = 'BRL'` — Pagamentos em Real

---

## 🔒 Observações

- O campo `CHECKRUN_NAME` é o nome dado pelo usuário à corrida de pagamento (Payment Process Request) e funciona como identificador de negócio.
- A coluna `PAY_THRU_DATE` define a data limite de vencimento: faturas com vencimento até esta data serão consideradas elegíveis.
- O campo `STATUS` controla o ciclo de vida da corrida: seleção, revisão, formatação e confirmação.
- A combinação de filtros (`VENDOR_ID_FROM/TO`, `PAY_GROUP`, `PAYMENT_METHOD`, `PAYMENT_CURRENCY`) define o escopo da seleção automática.
- Em Oracle Fusion, o PPR integra-se ao Oracle Payments (IBY) para emissão efetiva dos pagamentos.

---

## 🔗 PVOs Relacionados

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHECKRUN_ID | PmtProcReqInvCheckrunId | — |
| LAST_UPDATE_DATE | PmtProcReqInvLastUpdateDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — AP_INV_SELECTION_CRITERIA_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/apinvselectioncriteriaall-25718.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
