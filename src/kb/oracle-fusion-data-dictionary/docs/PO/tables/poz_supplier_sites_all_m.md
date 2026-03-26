---
id: DOC-PO-095
doc_type: system-doc
title: "POZ_SUPPLIER_SITES_ALL_M — Sites (Endereços Operacionais) de Fornecedores"
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
  - supplier-sites
  - enderecos
  - multi-org
aliases:
  - POZ_SUPPLIER_SITES_ALL_M
  - poz_supplier_sites_all_m
  - sites-fornecedor
  - supplier-sites
  - enderecos-operacionais
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_SITES_ALL_M

## Visão Geral

Tabela que armazena os **sites (endereços operacionais)** de fornecedores no Oracle Fusion Procurement. Cada site representa uma localização física do fornecedor (matriz, filial, fábrica, depósito) com configurações específicas de pagamento, impostos, moeda e condições comerciais. É a segunda tabela mais importante do cadastro de fornecedores, depois de `POZ_SUPPLIERS`.

> [!note] Sufixos _ALL_M
> O sufixo `_ALL` indica dados de **todas as business units** (multi-org). O sufixo `_M` indica tabela **merge** (suporta operações de merge/upsert no ETL).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro de sites:** Registro de todas as localizações operacionais do fornecedor (matriz, filiais, fábricas).
- **Pedidos de compra:** Referência obrigatória — cada PO é associado a um site específico do fornecedor.
- **Contas a pagar:** Configurações de pagamento (termos, moeda, método) são definidas por site.
- **Impostos:** Configurações fiscais por site (regime tributário, retenções).
- **Recebimento:** Endereço de origem (Ship-From) para recebimento de materiais.
- **Multi-org:** Permite configurações diferentes do mesmo fornecedor por business unit.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do site do fornecedor | — | 🟢 95% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 95% |
| 3 | VENDOR_SITE_CODE | VARCHAR2(15) | NOT NULL | Identificação | Código do site (visível ao usuário, ex.: SEDE, FILIAL-SP) | — | 🟢 90% |
| 4 | PARTY_SITE_ID | NUMBER(18) | NULL | FK | Party site no TCA | [[hz_party_sites]] | 🟢 85% |
| 5 | LOCATION_ID | NUMBER(18) | NULL | FK | Localização (TCA) | [[hz_locations]] | 🟡 80% |
| 6 | PURCHASING_SITE_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Site habilitado para compras (Y/N) | — | 🟢 90% |
| 7 | PAY_SITE_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Site habilitado para pagamento (Y/N) | — | 🟢 90% |
| 8 | RFQ_ONLY_SITE_FLAG | VARCHAR2(1) | NULL | Configuração | Site apenas para cotações/RFQ (Y/N) | — | 🟡 75% |
| 9 | PAYMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda de pagamento padrão | [[fnd_currencies]] | 🟢 85% |
| 10 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda de faturamento padrão | [[fnd_currencies]] | 🟢 85% |
| 11 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Pagamento | Método de pagamento padrão (CHECK, EFT, WIRE) | — | 🟡 80% |
| 12 | PAY_GROUP_LOOKUP_CODE | VARCHAR2(30) | NULL | Pagamento | Grupo de pagamento | — | 🟡 75% |
| 13 | TERMS_ID | NUMBER(18) | NULL | FK | Condição de pagamento padrão | [[ap_terms_b]] | 🟢 85% |
| 14 | INACTIVE_DATE | DATE | NULL | Vigência | Data de inativação do site | — | 🟢 85% |
| 15 | COUNTRY_OF_ORIGIN_CODE | VARCHAR2(2) | NULL | Localização | País de origem (ISO) | — | 🟡 75% |
| 16 | PCARD_SITE_FLAG | VARCHAR2(1) | NULL | Configuração | Site aceita Procurement Card (Y/N) | — | 🟡 65% |
| 17 | MATCH_OPTION | VARCHAR2(30) | NULL | Configuração | Opção de match: P (Purchase Order), R (Receipt) | — | 🟡 75% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor proprietário)
- [[hz_party_sites]] — via `PARTY_SITE_ID` (localização TCA)
- [[hz_locations]] — via `LOCATION_ID` (endereço TCA do site do fornecedor)
- [[ap_terms_b]] — via `TERMS_ID` (condição de pagamento)

### Tabelas-filha (FK de saída)

### Views

---

## Uso Típico

### Sites ativos de um fornecedor
```sql
SELECT ss.VENDOR_SITE_ID, ss.VENDOR_SITE_CODE,
       ss.PURCHASING_SITE_FLAG, ss.PAY_SITE_FLAG,
       ss.PAYMENT_CURRENCY_CODE
FROM   POZ_SUPPLIER_SITES_ALL_M ss
WHERE  ss.VENDOR_ID = :p_vendor_id
  AND  (ss.INACTIVE_DATE IS NULL OR ss.INACTIVE_DATE > SYSDATE);
```

### Sites habilitados para compras e pagamento
```sql
SELECT ss.VENDOR_SITE_ID, ss.VENDOR_SITE_CODE,
       s.VENDOR_NAME, ss.PAYMENT_METHOD_CODE
FROM   POZ_SUPPLIER_SITES_ALL_M ss
JOIN   POZ_SUPPLIERS s ON ss.VENDOR_ID = s.VENDOR_ID
WHERE  ss.PURCHASING_SITE_FLAG = 'Y'
  AND  ss.PAY_SITE_FLAG = 'Y'
  AND  (ss.INACTIVE_DATE IS NULL OR ss.INACTIVE_DATE > SYSDATE);
```

### Filtros comuns
- `PURCHASING_SITE_FLAG = 'Y'` — Sites habilitados para compras
- `PAY_SITE_FLAG = 'Y'` — Sites habilitados para pagamento
- `RFQ_ONLY_SITE_FLAG = 'Y'` — Sites apenas para cotação
- `MATCH_OPTION = 'P'` — Match por Purchase Order

---

## Observações

- Cada fornecedor deve ter **pelo menos um site** para ser utilizado em transações.
- O `VENDOR_SITE_CODE` é o identificador visível ao usuário (ex.: "SEDE", "FILIAL-SP", "DEPOSITO-RJ").
- As flags `PURCHASING_SITE_FLAG` e `PAY_SITE_FLAG` controlam se o site pode ser usado em POs e/ou pagamentos.
- O `MATCH_OPTION` define se a validação de faturas é feita contra o **PO** (P) ou contra o **recebimento** (R).
- O campo `TERMS_ID` define a condição de pagamento **padrão** do site; pode ser sobrescrito na transação individual.
- A atribuição do site a BUs é feita via `POZ_SITE_ASSIGNMENTS_ALL_M`; sem atribuição, o site não é utilizável na BU.
- Sites com `INACTIVE_DATE` preenchido não são elegíveis para novas transações.

---

## Referências

- [Oracle Docs — POZ_SUPPLIER_SITES_ALL_M](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pozsuppliersitesallm-25319.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
