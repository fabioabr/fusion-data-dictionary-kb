---
id: DOC-PO-103
doc_type: system-doc
title: "POZ_SUP_PRODUCTS_SERVICES — Produtos e Servicos de Fornecedores"
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
  - supplier-management
  - poz
aliases:
  - POZ_SUP_PRODUCTS_SERVICES
  - poz_sup_products_services
  - poz-sup-products-services
  - poz-sup
  - produtos-e-servicos-de-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUP_PRODUCTS_SERVICES

## 📌 Visão Geral

Armazena os **produtos e servicos oferecidos por fornecedores** cadastrados. Vincula fornecedores a categorias de produto/servico (UNSPSC), permitindo busca por capacidade de fornecimento.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Qualificacao:** Identificacao de fornecedores aptos por categoria.
- **Sourcing estrategico:** Busca de alternativas por segmento.
- **Spend analysis:** Classificacao de gastos por categoria.
- **Onboarding:** Registro de capacidades declaradas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PRODUCT_SERVICE_ID | NUMBER(18) | NOT NULL | PK | ID unico | — | 🟢 90% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 95% |
| 3 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria UNSPSC | [[egp_categories_b]] | 🟡 80% |
| 4 | CATEGORY_NAME | VARCHAR2(400) | NULL | Classificacao | Nome da categoria | — | 🟡 70% |
| 5 | STATUS | VARCHAR2(30) | NULL | Status | ACTIVE/INACTIVE | — | 🟡 75% |
| 6 | PARTY_ID | NUMBER(18) | NULL | FK | Party TCA | [[hz_parties]] | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor que oferece o produto ou serviço)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria do produto ou serviço oferecido)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA do fornecedor de produto ou serviço)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Produtos ativos de um fornecedor
```sql
SELECT VENDOR_ID, CATEGORY_NAME, STATUS
FROM   POZ_SUP_PRODUCTS_SERVICES
WHERE  VENDOR_ID = :p_vendor_id AND STATUS = 'ACTIVE';
```


---

## 🔒 Observações

- Categorizacao segue UNSPSC por padrao; customizavel por implementacao.
- Registros inativos devem ser filtrados.
- Populada durante qualificacao/onboarding.

---

## 📚 Referências

- [Oracle Docs — POZ_SUP_PRODUCTS_SERVICES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
