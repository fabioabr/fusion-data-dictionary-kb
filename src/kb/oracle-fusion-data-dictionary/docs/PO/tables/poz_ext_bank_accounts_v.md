---
id: DOC-PO-083
doc_type: system-doc
title: "POZ_EXT_BANK_ACCOUNTS_V — Contas Bancárias Externas de Fornecedores"
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
  - supplier-bank
  - contas-bancarias
  - pagamentos
aliases:
  - POZ_EXT_BANK_ACCOUNTS_V
  - poz_ext_bank_accounts_v
  - contas-bancarias-fornecedor
  - supplier-bank-accounts
  - bank-accounts-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_EXT_BANK_ACCOUNTS_V

## Visão Geral

View que consolida as **contas bancárias externas** associadas a fornecedores no Oracle Fusion. Apresenta dados bancários utilizados para pagamentos eletrônicos (EFT/ACH), incluindo banco, agência, número da conta, moeda e status. Combina informações do Banking (IBY) com o cadastro de fornecedores (POZ).

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), combinando dados de tabelas do módulo Payments (IBY) com o cadastro de fornecedores.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Pagamentos eletrônicos:** Identificação da conta bancária destino para transferências EFT/ACH/Wire.
- **Validação bancária:** Verificação de dados bancários antes do processamento de pagamentos.
- **Cadastro de fornecedores:** Consulta das contas bancárias associadas a cada fornecedor/site.
- **Conciliação bancária:** Cruzamento de contas bancárias com extratos para reconciliação.
- **Compliance:** Verificação de contas bancárias ativas e válidas para fins regulatórios.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXT_BANK_ACCOUNT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da conta bancária externa | — | 🟡 75% |
| 2 | BANK_ACCOUNT_NUM | VARCHAR2(100) | NULL | Financeiro | Número da conta bancária | — | 🟡 75% |
| 3 | BANK_ACCOUNT_NAME | VARCHAR2(80) | NULL | Financeiro | Nome/descrição da conta bancária | — | 🟡 75% |
| 4 | BANK_NAME | VARCHAR2(360) | NULL | Financeiro | Nome do banco | — | 🟡 70% |
| 5 | BRANCH_NAME | VARCHAR2(360) | NULL | Financeiro | Nome da agência/branch | — | 🟡 70% |
| 6 | BRANCH_NUMBER | VARCHAR2(30) | NULL | Financeiro | Número da agência | — | 🟡 70% |
| 7 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda da conta bancária | [[fnd_currencies]] | 🟡 75% |
| 8 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 9 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Identificador do site do fornecedor | [[poz_supplier_sites_all_m]] | 🟡 70% |
| 10 | PARTY_ID | NUMBER(18) | NULL | FK | Party ID (TCA) do fornecedor | [[hz_parties]] | 🟡 70% |
| 11 | COUNTRY_CODE | VARCHAR2(2) | NULL | Localização | Código do país do banco | — | 🟡 70% |
| 12 | IBAN | VARCHAR2(50) | NULL | Financeiro | Código IBAN (International Bank Account Number) | — | 🟡 70% |
| 13 | ACCOUNT_TYPE | VARCHAR2(25) | NULL | Classificação | Tipo da conta: CHECKING, SAVINGS | — | 🟡 65% |
| 14 | START_DATE | DATE | NULL | Vigência | Data de início de validade da conta | — | 🟡 65% |
| 15 | END_DATE | DATE | NULL | Vigência | Data de fim de validade da conta | — | 🟡 65% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor proprietário da conta)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor associado à conta bancária externa)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA proprietária da conta bancária externa)

### Tabelas relacionadas

---

## Uso Típico

### Contas bancárias ativas de um fornecedor
```sql
SELECT ba.BANK_ACCOUNT_NAME, ba.BANK_ACCOUNT_NUM,
       ba.BANK_NAME, ba.BRANCH_NAME, ba.CURRENCY_CODE
FROM   POZ_EXT_BANK_ACCOUNTS_V ba
WHERE  ba.VENDOR_ID = :p_vendor_id
  AND  (ba.END_DATE IS NULL OR ba.END_DATE > SYSDATE);
```

### Contas bancárias por moeda
```sql
SELECT ba.VENDOR_ID, ba.BANK_ACCOUNT_NAME, ba.BANK_NAME,
       ba.CURRENCY_CODE, ba.IBAN
FROM   POZ_EXT_BANK_ACCOUNTS_V ba
WHERE  ba.CURRENCY_CODE = 'BRL'
  AND  (ba.END_DATE IS NULL OR ba.END_DATE > SYSDATE);
```

---

## Observações

- Por ser uma **view**, não suporta operações DML diretamente; alterações devem ser feitas via APIs de Payments (IBY) ou pelo cadastro de fornecedor.
- Dados bancários são **informações sensíveis** — o número da conta pode ser mascarado dependendo das configurações de segurança.
- O campo `IBAN` é utilizado principalmente para transações internacionais (SEPA/SWIFT).
- A validade da conta é controlada por `START_DATE` e `END_DATE`; contas com `END_DATE` no passado são consideradas inativas.
- Em implementações brasileiras, o `BRANCH_NUMBER` corresponde ao **código da agência** e o `BANK_ACCOUNT_NUM` ao **número da conta corrente**.

---

## Referências

- [Oracle Docs — External Bank Accounts](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/iby-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
