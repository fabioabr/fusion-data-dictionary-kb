---
id: DOC-AP-004
doc_type: system-doc
title: "AP_CHECKS_ALL — Pagamentos (Cheques/Transferências) de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, checks, pagamentos, payments, transferencias]
aliases: [AP_CHECKS_ALL, ap_checks_all, checks_ap, pagamentos_ap, cheques_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_CHECKS_ALL

## Visão Geral

Tabela principal de pagamentos emitidos pelo módulo de Contas a Pagar. Apesar do nome legado "checks", armazena todos os tipos de pagamento — cheques, transferências bancárias (wire), boletos e pagamentos eletrônicos. Cada registro representa um instrumento de pagamento individual com valor, data, fornecedor e conta bancária associados. Particionada por `ORG_ID`.

## Propósito de Negócio

Registra cada desembolso realizado a fornecedores, sendo a tabela central para conciliação bancária, auditoria de pagamentos e controle de fluxo de caixa. No Banco Patria, é fundamental para rastrear pagamentos a prestadores de serviço, fornecedores de tecnologia e obrigações regulatórias, além de alimentar relatórios de conciliação com extratos bancários.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECK_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do pagamento. | — | 🟢 100% |
| 2 | CHECK_NUMBER | NUMBER(15) | NOT NULL | Negócio | Número do cheque/pagamento. | — | 🟢 100% |
| 3 | CHECK_DATE | DATE | NOT NULL | Negócio | Data de emissão do pagamento. | — | 🟢 100% |
| 4 | AMOUNT | NUMBER | NOT NULL | Negócio | Valor do pagamento. | — | 🟢 100% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Negócio | Código da moeda do pagamento. | [[fnd_currencies]] | 🟢 100% |
| 6 | VENDOR_ID | NUMBER(15) | NOT NULL | FK | Identificador do fornecedor. | [[poz_suppliers]] | 🟢 100% |
| 7 | VENDOR_SITE_ID | NUMBER(15) | NULL | FK | Identificador do site do fornecedor. | [[poz_supplier_sites_all]] | 🟢 95% |
| 8 | BANK_ACCOUNT_ID | NUMBER(15) | NOT NULL | FK | Conta bancária de origem do pagamento. | [[ce_bank_accounts]] | 🟢 95% |
| 9 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Negócio | Método de pagamento (CHECK, EFT, WIRE, etc.). | — | 🟢 95% |
| 10 | STATUS_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Controle | Status do pagamento (NEGOTIABLE, VOIDED, CLEARED, etc.). | — | 🟢 100% |
| 11 | CLEARED_DATE | DATE | NULL | Negócio | Data de compensação bancária. | — | 🟢 90% |
| 12 | CLEARED_AMOUNT | NUMBER | NULL | Negócio | Valor compensado no banco. | — | 🟢 90% |
| 13 | PAYMENT_TYPE_FLAG | VARCHAR2(1) | NULL | Classificação | Tipo: R (Refund), Q (Quick), A (Regular). | — | 🟡 75% |
| 14 | ORG_ID | NUMBER(15) | NOT NULL | Multiorg | Identificador da organização (business unit). | [[hr_operating_units]] | 🟢 100% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 16 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[poz_suppliers]]** — Fornecedor beneficiário do pagamento (via `VENDOR_ID`).
- **[[poz_supplier_sites_all]]** — Site do fornecedor (via `VENDOR_SITE_ID`).
- **[[ce_bank_accounts]]** — Conta bancária de origem (via `BANK_ACCOUNT_ID`).
- **[[hr_operating_units]]** — Organização/business unit (via `ORG_ID`).
- **[[fnd_currencies]]** — Moeda do pagamento (via `CURRENCY_CODE`).

### Tabelas-filha

- **[[ap_invoice_payments_all]]** — Relação pagamento × fatura (N:N via `CHECK_ID`).

## Uso Típico

```sql
-- Listar pagamentos emitidos nos últimos 30 dias com fornecedor
SELECT c.CHECK_NUMBER,
       c.CHECK_DATE,
       c.AMOUNT,
       c.CURRENCY_CODE,
       c.STATUS_LOOKUP_CODE,
       s.VENDOR_NAME
  FROM AP_CHECKS_ALL c
  JOIN POZ_SUPPLIERS s
    ON s.VENDOR_ID = c.VENDOR_ID
 WHERE c.ORG_ID = :p_org_id
   AND c.CHECK_DATE >= TRUNC(SYSDATE) - 30
 ORDER BY c.CHECK_DATE DESC;
```

## Observações

- O nome "checks" é legado do Oracle E-Business Suite; no Fusion, a tabela armazena todos os tipos de pagamento.
- O campo `STATUS_LOOKUP_CODE` governa o ciclo de vida: NEGOTIABLE → CLEARED → RECONCILED (ou VOIDED).
- Pagamentos voidados (VOIDED) permanecem na tabela para auditoria — não são excluídos fisicamente.
- Sempre filtrar por `ORG_ID` em consultas para performance e segurança multiorg.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Payments Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
