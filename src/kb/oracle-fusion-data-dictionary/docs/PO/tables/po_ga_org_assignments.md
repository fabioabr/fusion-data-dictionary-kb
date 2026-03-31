---
id: DOC-PO-125
doc_type: system-doc
title: "PO_GA_ORG_ASSIGNMENTS — Atribuicoes de Organizacoes em Global Agreements"
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
  - global-agreements
  - contratos
  - ga
aliases:
  - PO_GA_ORG_ASSIGNMENTS
  - po_ga_org_assignments
  - po-ga-org-assignments
  - po-ga
  - atribuicoes-de-organizacoes-em-glob
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_GA_ORG_ASSIGNMENTS

## 📌 Visão Geral

Armazena as **atribuicoes de organizacoes (BUs) a Global Agreements**. Define quais BUs podem fazer releases contra um Global Blanket Purchase Agreement.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Global Agreements:** Controla quais BUs usam um acordo global.
- **Compras centralizadas:** Releases descentralizados contra contratos centrais.
- **Governance:** Restricao a organizacoes autorizadas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GA_ORG_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | ID da atribuicao | — | 🟡 80% |
| 2 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Global Agreement | [[po_headers_all]] | 🟢 95% |
| 3 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Organizacao | [[hr_all_organization_units_f]] | 🟢 95% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟡 80% |
| 5 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor na BU | [[poz_supplier_sites_all_m]] | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (acordo global ao qual a organização é atribuída)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organização autorizada a usar o acordo global)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor no acordo global)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Orgs atribuidas a um GA
```sql
SELECT ORGANIZATION_ID, ENABLED_FLAG
FROM   PO_GA_ORG_ASSIGNMENTS
WHERE  PO_HEADER_ID = :p_ga_id AND ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- Cada GA pode ser compartilhado entre multiplas BUs.
- Necessario para procurement centralizado com execucao descentralizada.

---

## 🔗 PVOs Relacionados

### [[purchasingagreementbuaccesspvo|PurchasingAgreementBuAccessPVO]] (PO · BICC: 5/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BILL_TO_LOCATION_ID | BillToLocationId | ✅ |
| BILLTO_BU_ID | BilltoBuId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| ENABLED_FLAG | EnabledFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORDERED_LOCALLY_FLAG | PurchasingAgreementBuAccessOrderedLocallyFlag | ✅ |
| ORG_ASSIGNMENT_ID | OrgAssignmentId | ✅ |
| PO_HEADER_ID | PoHeaderId | — |
| PRC_BU_ID | PrcBuId | — |
| REQ_BU_ID | ReqBuId | — |
| SHIP_TO_LOCATION_ID | ShipToLocationId | — |
| VENDOR_SITE_ID | VendorSiteId | — |

### [[purchasinggaorgassignmentsextractpvo|PurchasingGaOrgAssignmentsExtractPVO]] (PO · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BILL_TO_LOCATION_ID | BillToLocationId | ✅ |
| BILLTO_BU_ID | BilltoBuId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENABLED_FLAG | EnabledFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORDERED_LOCALLY_FLAG | OrderedLocallyFlag | ✅ |
| ORG_ASSIGNMENT_ID | OrgAssignmentId | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| SHIP_TO_LOCATION_ID | ShipToLocationId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_GA_ORG_ASSIGNMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
