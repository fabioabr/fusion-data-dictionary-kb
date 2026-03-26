---
id: DOC-PO-098
doc_type: system-doc
title: "POZ_SUPP_PROD_SERVICES_ATTR_V — Atributos de Produtos e Serviços de Fornecedores"
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
  - supplier-products
  - supplier-services
  - classificacao
  - atributos
aliases:
  - POZ_SUPP_PROD_SERVICES_ATTR_V
  - poz_supp_prod_services_attr_v
  - atributos-produtos-servicos
  - supplier-product-service-attrs
  - classificacao-fornecedor-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPP_PROD_SERVICES_ATTR_V

## Visão Geral

View que consolida os **atributos de produtos e serviços oferecidos por fornecedores** no Oracle Fusion Procurement. Apresenta as categorias de fornecimento efetivadas (após aprovação das solicitações em `POZ_PRODUCT_SERVICE_REQUESTS`) com seus atributos adicionais, como certificações, capacidades e classificações UNSPSC.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), combinando dados de classificação de fornecedores com atributos.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Classificação de fornecedores:** Consulta das categorias de produto/serviço registradas por fornecedor.
- **Sourcing:** Identificação de fornecedores qualificados por categoria para negociações.
- **Approved Supplier List (ASL):** Base para montagem da lista de fornecedores aprovados por categoria.
- **Spend Analysis:** Análise de gastos por categoria de fornecimento.
- **Qualificação:** Verificação de atributos de qualificação por produto/serviço.
- **Relatórios:** Matriz de capacidades de fornecedores por categoria.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 2 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compras (purchasing category) | [[egp_categories_b]] | 🟡 70% |
| 3 | CATEGORY_NAME | VARCHAR2(250) | NULL | Classificação | Nome da categoria de produto/serviço | — | 🟡 70% |
| 4 | SEGMENT1 | VARCHAR2(40) | NULL | Classificação | Segmento 1 da categoria (UNSPSC nível 1) | — | 🟡 65% |
| 5 | SEGMENT2 | VARCHAR2(40) | NULL | Classificação | Segmento 2 da categoria (UNSPSC nível 2) | — | 🟡 65% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificação | Status da classificação: ACTIVE, INACTIVE | — | 🟡 70% |
| 7 | VENDOR_NAME | VARCHAR2(360) | NULL | Identificação | Nome do fornecedor (denormalizado) | — | 🟡 70% |
| 8 | VENDOR_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do fornecedor (denormalizado) | — | 🟡 70% |
| 9 | CERTIFICATION_FLAG | VARCHAR2(1) | NULL | Qualificação | Fornecedor possui certificação para a categoria (Y/N) | — | 🟡 60% |
| 10 | SMALL_BUSINESS_FLAG | VARCHAR2(1) | NULL | Classificação | Fornecedor é pequena empresa (Y/N) — contexto US | — | 🔴 50% |

---

## Relacionamentos

### Tabelas-base

### Tabelas relacionadas

---

## Uso Típico

### Categorias de um fornecedor
```sql
SELECT pspa.CATEGORY_NAME, pspa.STATUS,
       pspa.CERTIFICATION_FLAG
FROM   POZ_SUPP_PROD_SERVICES_ATTR_V pspa
WHERE  pspa.VENDOR_ID = :p_vendor_id
  AND  pspa.STATUS = 'ACTIVE'
ORDER BY pspa.CATEGORY_NAME;
```

### Fornecedores qualificados por categoria
```sql
SELECT pspa.VENDOR_ID, pspa.VENDOR_NAME,
       pspa.VENDOR_NUMBER, pspa.CERTIFICATION_FLAG
FROM   POZ_SUPP_PROD_SERVICES_ATTR_V pspa
WHERE  pspa.CATEGORY_ID = :p_category_id
  AND  pspa.STATUS = 'ACTIVE'
ORDER BY pspa.VENDOR_NAME;
```

---

## Observações

- Por ser uma **view**, não suporta operações DML; alterações são feitas via solicitações em `POZ_PRODUCT_SERVICE_REQUESTS`.
- As categorias utilizam tipicamente a hierarquia **UNSPSC** ou categorias de compras customizadas configuradas na implementação.
- O campo `CERTIFICATION_FLAG` pode indicar que o fornecedor possui certificação ISO, diversity, ou outra certificação relevante para a categoria.
- Esta view é fundamental para o processo de **Sourcing**, onde fornecedores são filtrados por categorias de produto/serviço.
- Os campos `VENDOR_NAME` e `VENDOR_NUMBER` são **denormalizados** para facilitar consultas sem join adicional.

---

## Referências

- [Oracle Docs — Supplier Products and Services](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
