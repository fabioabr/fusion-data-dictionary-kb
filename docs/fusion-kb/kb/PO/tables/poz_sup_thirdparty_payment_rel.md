---
id: DOC-PO-105
doc_type: system-doc
title: "POZ_SUP_THIRDPARTY_PAYMENT_REL — Relacionamentos de Pagamento a Terceiros"
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
  - POZ_SUP_THIRDPARTY_PAYMENT_REL
  - poz_sup_thirdparty_payment_rel
  - poz-sup-thirdparty-payment-rel
  - poz-sup
  - relacionamentos-de-pagamento-a-terc
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUP_THIRDPARTY_PAYMENT_REL

## 📌 Visão Geral

Armazena os **relacionamentos de pagamento a terceiros** entre fornecedores. Permite que pagamentos devidos a um fornecedor sejam direcionados para outro (terceiro autorizado), cenario de factoring ou cessao de credito.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Third Party Payment:** Direcionar pagamentos para terceiro autorizado.
- **Factoring:** Pagamentos a instituicao financeira (fator).
- **Representacao comercial:** Pagamento a representantes.
- **Compliance financeiro:** Auditoria de redirecionamentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | THIRDPARTY_REL_ID | NUMBER(18) | NOT NULL | PK | ID unico do relacionamento | — | 🟡 75% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor original | [[poz_suppliers]] | 🟢 90% |
| 3 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟢 90% |
| 4 | REMIT_TO_VENDOR_ID | NUMBER(18) | NOT NULL | FK | Terceiro recebedor | [[poz_suppliers]] | 🟡 80% |
| 5 | REMIT_TO_VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do terceiro | [[poz_supplier_sites_all_m]] | 🟡 80% |
| 6 | START_DATE | DATE | NULL | Data | Inicio da vigencia | — | 🟡 75% |
| 7 | END_DATE | DATE | NULL | Data | Termino da vigencia | — | 🟡 75% |
| 8 | STATUS | VARCHAR2(30) | NULL | Status | ACTIVE/INACTIVE | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor original na relação de pagamento a terceiro)
- [[poz_suppliers]] — via `REMIT_TO_VENDOR_ID` (fornecedor terceiro que recebe o pagamento)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID`/`REMIT_TO_VENDOR_SITE_ID` (site do fornecedor na relação de pagamento a terceiro)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Relacionamentos ativos
```sql
SELECT VENDOR_ID, REMIT_TO_VENDOR_ID, START_DATE, END_DATE
FROM   POZ_SUP_THIRDPARTY_PAYMENT_REL
WHERE  VENDOR_ID = :p_vendor_id AND STATUS = 'ACTIVE'
  AND  (END_DATE IS NULL OR END_DATE > SYSDATE);
```

---

## 🔒 Observações

- Relacionamentos sensiveis; requerem aprovacao de compliance.
- Monitorar `END_DATE` para evitar redirecionamentos expirados.
- Verificar redirecionamentos circulares em auditorias.

---

## 🔗 PVOs Relacionados

### [[supplierthirdpartypaymentextractpvo|SupplierThirdPartyPaymentExtractPVO]] (PO · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEFAULT_RELATIONSHIP_FLAG | DefaultRelationshipFlag | ✅ |
| DESCRIPTION | Description | ✅ |
| FROM_DATE | FromDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| REMIT_TO_ADDRESS_ID | RemitToAddressId | ✅ |
| REMIT_TO_SUPPLIER_ID | RemitToSupplierId | ✅ |
| TO_DATE | ToDate | ✅ |
| TPP_RELATIONSHIP_ID | TppRelationshipId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |

### [[supplierthirdpartypaymentpvo|SupplierThirdPartyPaymentPVO]] (PO · BICC: 6/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DEFAULT_RELATIONSHIP_FLAG | DefaultRelationshipFlag | ✅ |
| DESCRIPTION | Description | ✅ |
| FROM_DATE | FromDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| REMIT_TO_ADDRESS_ID | RemitToAddressId | — |
| REMIT_TO_SUPPLIER_ID | RemitToSupplierId | — |
| TO_DATE | ToDate | ✅ |
| TPP_RELATIONSHIP_ID | TppRelationshipId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | — |

---

## 📚 Referências

- [Oracle Docs — POZ_SUP_THIRDPARTY_PAYMENT_REL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
