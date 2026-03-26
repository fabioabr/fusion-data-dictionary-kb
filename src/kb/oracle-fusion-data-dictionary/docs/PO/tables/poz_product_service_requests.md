---
id: DOC-PO-084
doc_type: system-doc
title: "POZ_PRODUCT_SERVICE_REQUESTS — Solicitações de Produtos e Serviços de Fornecedores"
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
aliases:
  - POZ_PRODUCT_SERVICE_REQUESTS
  - poz_product_service_requests
  - solicitacoes-produtos-servicos
  - product-service-requests
  - classificacao-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_PRODUCT_SERVICE_REQUESTS

## Visão Geral

Armazena as **solicitações de classificação de produtos e serviços** oferecidos por fornecedores no Oracle Procurement. Cada registro representa uma requisição pendente ou processada para associar categorias de produtos/serviços (UNSPSC, categoria de compras) a um fornecedor, tipicamente originada durante o processo de registro ou atualização cadastral.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de fornecedores:** Categorização por tipo de produto/serviço oferecido (UNSPSC ou categorias customizadas).
- **Registro de fornecedores:** Captura das categorias de fornecimento durante o onboarding via Supplier Portal.
- **Qualificação de fornecedores:** Suporte ao processo de qualificação com base nas categorias declaradas.
- **Sourcing:** Identificação de fornecedores aptos a participar de negociações por categoria.
- **Spend Analysis:** Base para análise de gastos por categoria de fornecimento.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROD_SVC_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da solicitação de produto/serviço | — | 🟡 70% |
| 2 | SUPPLIER_REG_ID | NUMBER(18) | NULL | FK | Registro de fornecedor associado | [[poz_supplier_registrations]] | 🟡 70% |
| 3 | VENDOR_ID | NUMBER(18) | NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟡 75% |
| 4 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de compras (purchasing category) | — | 🟡 70% |
| 5 | CATEGORY_NAME | VARCHAR2(250) | NULL | Classificação | Nome da categoria de produto/serviço | — | 🟡 65% |
| 6 | SEGMENT1 | VARCHAR2(40) | NULL | Classificação | Segmento 1 da categoria (ex.: UNSPSC nível 1) | — | 🟡 65% |
| 7 | REQUEST_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da solicitação: PENDING, APPROVED, REJECTED | — | 🟡 75% |
| 8 | REQUEST_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo: NEW, UPDATE, DELETE | — | 🟡 65% |
| 9 | SUPP_REQUEST_ID | NUMBER(18) | NULL | FK | Solicitação principal do fornecedor | [[poz_supp_requests]] | 🟡 65% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor da solicitação de produto ou serviço)
- [[poz_supplier_registrations]] — via `SUPPLIER_REG_ID` (registro de fornecedor)
- [[poz_supp_requests]] — via `SUPP_REQUEST_ID` (solicitação principal)

### Tabelas relacionadas

---

## Uso Típico

### Solicitações pendentes de classificação
```sql
SELECT psr.PROD_SVC_REQUEST_ID, psr.VENDOR_ID,
       psr.CATEGORY_NAME, psr.REQUEST_STATUS
FROM   POZ_PRODUCT_SERVICE_REQUESTS psr
WHERE  psr.REQUEST_STATUS = 'PENDING'
ORDER BY psr.CREATION_DATE DESC;
```

### Categorias solicitadas por fornecedor
```sql
SELECT psr.CATEGORY_NAME, psr.REQUEST_STATUS,
       psr.REQUEST_TYPE, psr.CREATION_DATE
FROM   POZ_PRODUCT_SERVICE_REQUESTS psr
WHERE  psr.VENDOR_ID = :p_vendor_id
ORDER BY psr.CATEGORY_NAME;
```

---

## Observações

- As categorias utilizam tipicamente a hierarquia **UNSPSC** (United Nations Standard Products and Services Code) ou categorias de compras customizadas.
- Solicitações aprovadas são refletidas na view `POZ_SUPP_PROD_SERVICES_ATTR_V`.
- O processo de classificação pode ser iniciado pelo fornecedor no **Supplier Portal** ou pelo comprador internamente.
- A classificação por produto/serviço é fundamental para o **Approved Supplier List (ASL)** e para processos de Sourcing.

---

## Referências

- [Oracle Docs — Supplier Product Service Requests](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
