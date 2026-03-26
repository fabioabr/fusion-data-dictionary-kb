---
id: DOC-PO-074
doc_type: system-doc
title: "POZ_BI_SUPP_AP_INV_DIST_V — View BI de Fornecedores × Distribuições de Faturas AP"
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
  - accounts-payable
  - bi
  - view
  - distribuicoes
aliases:
  - POZ_BI_SUPP_AP_INV_DIST_V
  - poz_bi_supp_ap_inv_dist_v
  - bi-fornecedor-ap-distribuicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BI_SUPP_AP_INV_DIST_V

## 📌 Visão Geral

View otimizada para **Business Intelligence** que cruza dados de **fornecedores** (suppliers) com **distribuições de faturas do Accounts Payable** (AP Invoice Distributions). Fornece visão desnormalizada para análises de spend por fornecedor, incluindo dados cadastrais do fornecedor e detalhes contábeis das distribuições.

> [!note] Prefixo BI
> Views com prefixo `_BI_` são projetadas para consumo por ferramentas de BI (OTBI, BICC).

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Análise de spend por fornecedor:** Relatórios de gastos detalhados a nível de distribuição contábil.
- **Dashboards OTBI:** Indicadores de concentração de gastos, top fornecedores, tendências.
- **Reconciliação AP × Procurement:** Cruzamento entre dados de compra e dados contábeis.
- **Extração BICC:** Publicação de dados de gastos por fornecedor para data warehouse.
- **Auditoria de gastos:** Análise de distribuições por conta contábil e fornecedor.

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
| 2 | VENDOR_NAME | VARCHAR2(360) | NULL | Descrição | Nome do fornecedor | — | 🟡 80% |
| 3 | VENDOR_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do fornecedor | — | 🟡 80% |
| 4 | VENDOR_TYPE_LOOKUP_CODE | VARCHAR2(30) | NULL | Classificação | Tipo do fornecedor | — | 🟡 70% |
| 5 | INVOICE_ID | NUMBER(18) | NULL | FK | Fatura AP | [[ap_invoices_all]] | 🟡 75% |
| 6 | INVOICE_NUM | VARCHAR2(50) | NULL | Identificação | Número da fatura | — | 🟡 75% |
| 7 | INVOICE_DISTRIBUTION_ID | NUMBER(18) | NULL | FK | Distribuição da fatura | [[ap_invoice_distributions_all]] | 🟡 75% |
| 8 | DIST_CODE_COMBINATION_ID | NUMBER(18) | NULL | FK | Conta contábil da distribuição | [[gl_code_combinations]] | 🟡 70% |
| 9 | AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição | — | 🟡 75% |
| 10 | ACCOUNTING_DATE | DATE | NULL | Contabilidade | Data contábil | — | 🟡 75% |
| 11 | INVOICE_CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda da fatura | — | 🟡 70% |
| 12 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor na view BI de fornecedores e faturas)
- [[ap_invoices_all]] — via `INVOICE_ID` (fatura AP na view BI de fornecedores)
- [[ap_invoice_distributions_all]] — via `INVOICE_DISTRIBUTION_ID` (distribuição na view BI de fornecedores)
- [[gl_code_combinations]] — via `DIST_CODE_COMBINATION_ID` (conta contábil na view BI de fornecedores)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit na view BI de fornecedores e faturas)

### Tabelas-filha (FK de saída)
- Nenhuma direta (view de consulta BI)

---

## 📎 Uso Típico

### Top 10 fornecedores por valor de gasto
```sql
SELECT sad.VENDOR_NAME, sad.VENDOR_NUMBER,
       SUM(sad.AMOUNT) AS total_spend
FROM   POZ_BI_SUPP_AP_INV_DIST_V sad
WHERE  sad.ACCOUNTING_DATE BETWEEN :start_date AND :end_date
  AND  sad.ORG_ID = :p_org_id
GROUP BY sad.VENDOR_NAME, sad.VENDOR_NUMBER
ORDER BY total_spend DESC
FETCH FIRST 10 ROWS ONLY;
```

### Gastos por conta contábil e fornecedor
```sql
SELECT sad.VENDOR_NAME, sad.DIST_CODE_COMBINATION_ID,
       SUM(sad.AMOUNT) AS total
FROM   POZ_BI_SUPP_AP_INV_DIST_V sad
WHERE  sad.VENDOR_ID = :p_vendor_id
GROUP BY sad.VENDOR_NAME, sad.DIST_CODE_COMBINATION_ID;
```

---

## 🔒 Observações

- Esta é uma **view BI**, não uma tabela física — não aceita DML direto.
- Diferencia-se de `POZ_BI_HIERARCHY_AP_INV_DIST_V` por não incluir a dimensão hierárquica (parent-child).
- Para análises precisas, filtre por status de fatura nas tabelas-base (faturas canceladas ou em disputa podem distorcer totais).
- Campos desnormalizados (`VENDOR_NAME`, `INVOICE_NUM`) facilitam reporting mas podem ficar desatualizados.

---

## 📚 Referências

- [Oracle Docs — POZ BI Views](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
