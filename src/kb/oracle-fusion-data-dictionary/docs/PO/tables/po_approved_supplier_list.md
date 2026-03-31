---
id: DOC-PO-111
doc_type: system-doc
title: "PO_APPROVED_SUPPLIER_LIST — Lista de Fornecedores Aprovados (ASL)"
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
  - approved-supplier-list
  - asl
  - sourcing
aliases:
  - PO_APPROVED_SUPPLIER_LIST
  - po_approved_supplier_list
  - po-approved-supplier-list
  - po-approved
  - lista-de-fornecedores-aprovados-(as
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_APPROVED_SUPPLIER_LIST

## 📌 Visão Geral

Armazena a **lista de fornecedores aprovados (Approved Supplier List — ASL)** por item ou categoria. Define quais fornecedores estao autorizados a fornecer determinados itens.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de sourcing:** Restringe compras a fornecedores qualificados.
- **Validacao de PO:** Impede criacao de POs para fornecedores nao aprovados.
- **Sourcing automatico:** Base para geracao automatica de cotacoes.
- **Compliance:** Evidencia de qualificacao de fornecedores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASL_ID | NUMBER(18) | NOT NULL | PK | ID da entrada ASL | — | 🟢 95% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor aprovado | [[poz_suppliers]] | 🟢 95% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 90% |
| 4 | ITEM_ID | NUMBER(18) | NULL | FK | Item aprovado | [[egp_system_items_b]] | 🟢 95% |
| 5 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria aprovada | [[egp_categories_b]] | 🟢 90% |
| 6 | ASL_STATUS_ID | NUMBER(18) | NULL | FK | Status da ASL | [[po_asl_statuses]] | 🟢 90% |
| 7 | OWNING_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Org proprietaria | [[hr_all_organization_units_f]] | 🟢 85% |
| 8 | USING_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Org que utiliza | [[hr_all_organization_units_f]] | 🟢 85% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor da lista de fornecedores aprovados)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor aprovado)
- [[egp_system_items_b]] — via `ITEM_ID` (item do catálogo na lista de fornecedores aprovados)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de item na lista de fornecedores aprovados)
- [[po_asl_statuses]] — via `ASL_STATUS_ID` (status de aprovação do fornecedor na ASL)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Fornecedores aprovados para um item
```sql
SELECT VENDOR_ID, VENDOR_SITE_ID, ASL_STATUS_ID
FROM   PO_APPROVED_SUPPLIER_LIST
WHERE  ITEM_ID = :p_item_id;
```

---

## 🔒 Observações

- ASL pode ser por item ou por categoria.
- O `ASL_STATUS_ID` define aprovado, desqualificado, etc.
- Pode ser restrita a organizacoes via `USING_ORGANIZATION_ID`.

---

## 🔗 PVOs Relacionados

### [[purchasingaslextractpvo|PurchasingASLExtractPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASL_ID | AslId | ✅ |
| CATEGORY_ID | CategoryId | ✅ |
| CREATED_BY | SupListCreatedBy | ✅ |
| CREATION_DATE | SupListCreationDate | ✅ |
| DISABLE_FLAG | DisableFlag | ✅ |
| ITEM_ID | ItemId | ✅ |
| LAST_UPDATE_DATE | SupListLastUpdateDate | ✅ |
| LAST_UPDATED_BY | SupListLastUpdatedBy | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| USING_ORGANIZATION_ID | SupListUsingOrganizationId | ✅ |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |

### [[purchasingaslpvo|PurchasingASLPVO]] (PO · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASL_ID | AslId | ✅ |
| CATEGORY_ID | CategoryId | ✅ |
| CREATED_BY | SupListCreatedBy | ✅ |
| CREATION_DATE | SupListCreationDate | ✅ |
| DISABLE_FLAG | DisableFlag | ✅ |
| ITEM_ID | ItemId | ✅ |
| LAST_UPDATE_DATE | SupListLastUpdateDate | ✅ |
| LAST_UPDATED_BY | SupListLastUpdatedBy | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| USING_ORGANIZATION_ID | SupListUsingOrganizationId | ✅ |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_APPROVED_SUPPLIER_LIST](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poapprovedsupplierlist-10178.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
