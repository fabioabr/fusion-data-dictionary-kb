---
id: DOC-PO-075
doc_type: system-doc
title: "POZ_BI_SUPP_REG_BANK_ACCOUNT_V — View BI de Contas Bancárias de Registro de Fornecedores"
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
  - fornecedores
  - contas-bancarias
  - registro
  - bi
  - view
aliases:
  - POZ_BI_SUPP_REG_BANK_ACCOUNT_V
  - poz_bi_supp_reg_bank_account_v
  - bi-contas-bancarias-registro
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BI_SUPP_REG_BANK_ACCOUNT_V

## 📌 Visão Geral

View otimizada para **Business Intelligence** que expõe informações de **contas bancárias** informadas durante o processo de **registro de fornecedores** (supplier registration). Combina dados do cadastro bancário com informações do fornecedor para análises de completude cadastral e compliance bancário.

> [!note] Prefixo BI
> Views com prefixo `_BI_` são projetadas para consumo por ferramentas de BI (OTBI, BICC).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Completude cadastral:** Verificação de quais fornecedores em registro informaram dados bancários.
- **Compliance bancário:** Validação de dados bancários durante o processo de onboarding de fornecedores.
- **Relatórios de registro:** Análise do pipeline de registro de fornecedores com status de dados bancários.
- **Auditoria:** Rastreamento de informações bancárias submetidas durante o registro.
- **Extração BICC:** Publicação de dados de registro para data warehouse.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUPPLIER_REG_ID | NUMBER(18) | NOT NULL | FK | Registro de fornecedor | — | 🟡 75% |
| 2 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor (se já criado) | [[poz_suppliers]] | 🟡 70% |
| 3 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor | — | 🟡 75% |
| 4 | BANK_NAME | VARCHAR2(360) | NULL | Bancário | Nome do banco | — | 🟡 75% |
| 5 | BANK_BRANCH_NAME | VARCHAR2(360) | NULL | Bancário | Nome da agência/filial | — | 🟡 70% |
| 6 | BANK_ACCOUNT_NUMBER | VARCHAR2(100) | NULL | Bancário | Número da conta bancária | — | 🟡 75% |
| 7 | BANK_ACCOUNT_NAME | VARCHAR2(240) | NULL | Bancário | Nome/titular da conta | — | 🟡 70% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda da conta | — | 🟡 70% |
| 9 | COUNTRY_CODE | VARCHAR2(2) | NULL | Endereço | País do banco (ISO) | — | 🟡 65% |
| 10 | IBAN | VARCHAR2(50) | NULL | Bancário | IBAN (International Bank Account Number) | — | 🟡 70% |
| 11 | REGISTRATION_STATUS | VARCHAR2(30) | NULL | Status | Status do registro: DRAFT, PENDING_APPROVAL, APPROVED, REJECTED | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor, se criado)
- Tabelas de supplier registration (staging) — via `SUPPLIER_REG_ID`

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta BI)

---

## 📎 Uso Típico

### Registros pendentes com dados bancários
```sql
SELECT srb.SUPPLIER_NAME, srb.BANK_NAME,
       srb.BANK_ACCOUNT_NUMBER, srb.CURRENCY_CODE,
       srb.REGISTRATION_STATUS
FROM   POZ_BI_SUPP_REG_BANK_ACCOUNT_V srb
WHERE  srb.REGISTRATION_STATUS = 'PENDING_APPROVAL';
```

### Fornecedores registrados sem conta bancária
```sql
SELECT srb.SUPPLIER_NAME, srb.REGISTRATION_STATUS
FROM   POZ_BI_SUPP_REG_BANK_ACCOUNT_V srb
WHERE  srb.BANK_ACCOUNT_NUMBER IS NULL
  AND  srb.REGISTRATION_STATUS = 'APPROVED';
```

---

## 🔒 Observações

- Esta é uma **view BI**, não uma tabela física — não aceita DML direto.
- Dados bancários são **informações sensíveis** — o acesso a esta view deve ser controlado por data security policies.
- O `BANK_ACCOUNT_NUMBER` pode estar mascarado dependendo das configurações de segurança da instância.
- Após aprovação do registro, os dados bancários são transferidos para as tabelas de Cash Management (`CE_BANK_ACCOUNTS`, `IBY_EXT_BANK_ACCOUNTS`).
- O IBAN é relevante para pagamentos internacionais e pode não estar preenchido para contas domésticas.

---

## 🔗 PVOs Relacionados

### [[supplierregistrationbankaccountspvo|SupplierRegistrationBankAccountsPVO]] (PO · BICC: 21/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTREQUESTID | SupplierRegBankAccountAccountrequestid | — |
| ACCOUNTSUFFIX | SupplierRegBankAccountAccountsuffix | ✅ |
| AGENCYLOCATIONCODE | SupplierRegBankAccountAgencylocationcode | ✅ |
| BANK | SupplierRegBankAccountBank | ✅ |
| BANKACCOUNTNAME | SupplierRegBankAccountBankaccountname | ✅ |
| BANKACCOUNTNAMEALT | SupplierRegBankAccountBankaccountnamealt | ✅ |
| BANKACCOUNTNUM | SupplierRegBankAccountBankaccountnum | ✅ |
| BANKACCOUNTTYPE | SupplierRegBankAccountBankaccounttype | ✅ |
| BANKID | SupplierRegBankAccountBankid | — |
| BANKNUMBER | SupplierRegBankAccountBanknumber | ✅ |
| BRANCH | SupplierRegBankAccountBranch | ✅ |
| BRANCHID | SupplierRegBankAccountBranchid | — |
| BRANCHNUMBER | SupplierRegBankAccountBranchnumber | ✅ |
| CHECKDIGITS | SupplierRegBankAccountCheckdigits | ✅ |
| COUNTRY | SupplierRegBankAccountCountry | ✅ |
| COUNTRYCODE | SupplierRegBankAccountCountrycode | — |
| CREATEDBY | SupplierRegBankAccountCreatedby | ✅ |
| CREATIONDATE | SupplierRegBankAccountCreationdate | ✅ |
| CURRENCY | SupplierRegBankAccountCurrency | ✅ |
| CURRENCYCODE | SupplierRegBankAccountCurrencycode | — |
| DESCRIPTION | SupplierRegBankAccountDescription | ✅ |
| IBAN | SupplierRegBankAccountIban | ✅ |
| LASTUPDATEDATE | SupplierRegBankAccountLastupdatedate | ✅ |
| LASTUPDATEDBY | SupplierRegBankAccountLastupdatedby | ✅ |
| LASTUPDATELOGIN | SupplierRegBankAccountLastupdatelogin | — |
| NOTE | SupplierRegBankAccountNote | ✅ |
| OBJECTVERSIONNUMBER | SupplierRegBankAccountObjectversionnumber | — |
| SECONDARYACCOUNTREFERENCE | SecondaryAccountReference | — |
| SUPPLIERREGID | SupplierRegBankAccountSupplierregid | — |
| TEMPEXTBANKACCTID | Tempextbankacctid | ✅ |

---

## 📚 Referências

- [Oracle Docs — POZ BI Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
