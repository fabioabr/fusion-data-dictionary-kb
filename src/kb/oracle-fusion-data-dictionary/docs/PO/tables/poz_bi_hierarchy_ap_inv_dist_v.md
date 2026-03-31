---
id: DOC-PO-073
doc_type: system-doc
title: "POZ_BI_HIERARCHY_AP_INV_DIST_V — View BI de Hierarquia de Fornecedores × Distribuições AP"
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
  - hierarquia
  - accounts-payable
  - bi
  - view
aliases:
  - POZ_BI_HIERARCHY_AP_INV_DIST_V
  - poz_bi_hierarchy_ap_inv_dist_v
  - bi-hierarquia-ap-distribuicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BI_HIERARCHY_AP_INV_DIST_V

## 📌 Visão Geral

View otimizada para **Business Intelligence** que cruza a **hierarquia de fornecedores** (parent-child) com as **distribuições de faturas do Accounts Payable** (AP Invoice Distributions). Permite análises de gastos consolidadas por grupo econômico/hierarquia corporativa de fornecedores.

> [!note] Prefixo BI
> Views com prefixo `_BI_` são projetadas para consumo por ferramentas de BI (OTBI, BICC).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Análise de spend por grupo econômico:** Consolidação de gastos de fornecedores relacionados (parent-child).
- **Relatórios OTBI:** Dashboards de gastos com visão hierárquica de fornecedores.
- **Negociação consolidada:** Base analítica para identificar volume total de compras por grupo econômico.
- **Compliance de concentração:** Identificação de concentração de gastos em um único grupo de fornecedores.
- **Extração BICC:** Publicação de dados consolidados para data warehouse.

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
| 2 | PARENT_VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor-pai na hierarquia | [[poz_suppliers]] | 🟡 75% |
| 3 | VENDOR_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor | — | 🟡 80% |
| 4 | PARENT_VENDOR_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor-pai | — | 🟡 70% |
| 5 | INVOICE_ID | NUMBER(18) | NULL | FK | Fatura AP | [[ap_invoices_all]] | 🟡 75% |
| 6 | INVOICE_DISTRIBUTION_ID | NUMBER(18) | NULL | FK | Distribuição da fatura AP | [[ap_invoice_distributions_all]] | 🟡 75% |
| 7 | AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição | — | 🟡 75% |
| 8 | ACCOUNTING_DATE | DATE | NULL | Contabilidade | Data contábil da distribuição | — | 🟡 75% |
| 9 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda da fatura | — | 🟡 70% |
| 10 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` e `PARENT_VENDOR_ID` (fornecedor e fornecedor-pai)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura AP na view de hierarquia de fornecedor)
- [[ap_invoice_distributions_all]] — via `INVOICE_DISTRIBUTION_ID` (distribuição de fatura na view de hierarquia)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit na view de hierarquia de fornecedor)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta BI)

---

## 📎 Uso Típico

### Spend total por grupo econômico (parent)
```sql
SELECT hv.PARENT_VENDOR_NAME,
       SUM(hv.AMOUNT) AS total_spend,
       COUNT(DISTINCT hv.VENDOR_ID) AS qtd_fornecedores
FROM   POZ_BI_HIERARCHY_AP_INV_DIST_V hv
WHERE  hv.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
GROUP BY hv.PARENT_VENDOR_NAME
ORDER BY total_spend DESC;
```

### Detalhamento por fornecedor dentro de um grupo
```sql
SELECT hv.VENDOR_NAME, SUM(hv.AMOUNT) AS total_spend
FROM   POZ_BI_HIERARCHY_AP_INV_DIST_V hv
WHERE  hv.PARENT_VENDOR_ID = :p_parent_vendor_id
GROUP BY hv.VENDOR_NAME;
```

---

## 🔒 Observações

- Esta é uma **view BI**, não uma tabela física — não aceita DML direto.
- A hierarquia parent-child é baseada no campo `PARENT_PARTY_ID` do cadastro de fornecedores no TCA.
- Fornecedores sem parent terão `PARENT_VENDOR_ID` nulo — representam empresas independentes.
- Para análises de spend precisas, considere filtrar por status da fatura (aprovada/paga) nas tabelas-base.
- Performance pode ser limitada para grandes volumes — considere materializar os dados para reporting intensivo.

---

## 🔗 PVOs Relacionados

### [[supplierpvo|SupplierPVO]] (PO · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| HIERARCHY_AMOUNT | SupplierHierarchyInvDistHierarchyAmount | ✅ |
| VENDOR_ID | SupplierHierarchyInvDistVendorId | ✅ |

---

## 📚 Referências

- [Oracle Docs — POZ BI Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
