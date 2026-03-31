---
id: DOC-PO-076
doc_type: system-doc
title: "POZ_BI_SUP_SITES_AP_INV_DIST_V — View BI de Sites de Fornecedor × Distribuições AP"
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
  - sites
  - accounts-payable
  - bi
  - view
aliases:
  - POZ_BI_SUP_SITES_AP_INV_DIST_V
  - poz_bi_sup_sites_ap_inv_dist_v
  - bi-sites-fornecedor-ap-distribuicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BI_SUP_SITES_AP_INV_DIST_V

## 📌 Visão Geral

View otimizada para **Business Intelligence** que cruza dados de **sites de fornecedores** com **distribuições de faturas do Accounts Payable** (AP Invoice Distributions). Fornece granularidade a nível de site para análises de gastos, permitindo identificar em qual site/localidade do fornecedor a despesa foi incorrida.

> [!note] Prefixo BI
> Views com prefixo `_BI_` são projetadas para consumo por ferramentas de BI (OTBI, BICC).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Análise de spend por site:** Detalhamento de gastos por localidade/site do fornecedor.
- **Gestão de sites:** Identificação de sites mais ativos e volume de transações por site.
- **Relatórios OTBI:** Dashboards de gastos com dimensão geográfica de sites de fornecedores.
- **Otimização de pagamentos:** Análise de condições de pagamento por site.
- **Extração BICC:** Publicação de dados de spend por site para data warehouse.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 80% |
| 2 | VENDOR_SITE_ID | NUMBER(18) | NOT NULL | FK | Identificador do site do fornecedor | [[poz_supplier_sites_all_m]] | 🟡 80% |
| 3 | VENDOR_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor | — | 🟡 75% |
| 4 | VENDOR_SITE_CODE | VARCHAR2(30) | NULL | Identificação | Código do site | — | 🟡 80% |
| 5 | INVOICE_ID | NUMBER(18) | NULL | FK | Fatura AP | [[ap_invoices_all]] | 🟡 75% |
| 6 | INVOICE_DISTRIBUTION_ID | NUMBER(18) | NULL | FK | Distribuição da fatura | [[ap_invoice_distributions_all]] | 🟡 75% |
| 7 | AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição | — | 🟡 75% |
| 8 | ACCOUNTING_DATE | DATE | NULL | Contabilidade | Data contábil | — | 🟡 75% |
| 9 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda da fatura | — | 🟡 70% |
| 10 | PAYMENT_METHOD_CODE | VARCHAR2(30) | NULL | Pagamento | Método de pagamento do site | — | 🟡 65% |
| 11 | PAYMENT_TERMS_NAME | VARCHAR2(50) | NULL | Pagamento | Condição de pagamento do site | — | 🟡 65% |
| 12 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor na view BI de sites e faturas)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura AP na view BI de sites de fornecedor)
- [[ap_invoice_distributions_all]] — via `INVOICE_DISTRIBUTION_ID` (distribuição na view BI de sites de fornecedor)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit na view BI de sites de fornecedor)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta BI)

---

## 📎 Uso Típico

### Spend por site de fornecedor
```sql
SELECT ssd.VENDOR_NAME, ssd.VENDOR_SITE_CODE,
       SUM(ssd.AMOUNT) AS total_spend
FROM   POZ_BI_SUP_SITES_AP_INV_DIST_V ssd
WHERE  ssd.VENDOR_ID = :p_vendor_id
  AND  ssd.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
GROUP BY ssd.VENDOR_NAME, ssd.VENDOR_SITE_CODE;
```

### Top sites por volume de gastos
```sql
SELECT ssd.VENDOR_NAME, ssd.VENDOR_SITE_CODE,
       SUM(ssd.AMOUNT) AS total_spend
FROM   POZ_BI_SUP_SITES_AP_INV_DIST_V ssd
WHERE  ssd.ORG_ID = :p_org_id
  AND  ssd.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
GROUP BY ssd.VENDOR_NAME, ssd.VENDOR_SITE_CODE
ORDER BY total_spend DESC
FETCH FIRST 20 ROWS ONLY;
```

---

## 🔒 Observações

- Esta é uma **view BI**, não uma tabela física — não aceita DML direto.
- Diferencia-se de `POZ_BI_SUPP_AP_INV_DIST_V` por incluir a dimensão de site do fornecedor.
- O `VENDOR_SITE_CODE` identifica a localidade/filial do fornecedor (ex: site de pagamento vs. site de compra).
- Campos de pagamento (`PAYMENT_METHOD_CODE`, `PAYMENT_TERMS_NAME`) podem variar por site do mesmo fornecedor.

---

## 🔗 PVOs Relacionados

### [[suppliersitepvo|SupplierSitePVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AMOUNT | SuppSiteInvDistAmount | ✅ |
| VENDOR_SITE_ID | SuppSiteInvDistVendorSiteId | — |

---

## 📚 Referências

- [Oracle Docs — POZ BI Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
