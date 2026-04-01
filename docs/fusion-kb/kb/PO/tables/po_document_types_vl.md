---
id: DOC-PO-120
doc_type: system-doc
title: "PO_DOCUMENT_TYPES_VL — Tipos de Documento de Compras (View Multilingue)"
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
  - document-types
  - configuracao
  - po-setup
aliases:
  - PO_DOCUMENT_TYPES_VL
  - po_document_types_vl
  - po-document-types-vl
  - po-document
  - tipos-de-documento-de-compras-(view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_DOCUMENT_TYPES_VL

## 📌 Visão Geral

View que combina `PO_DOCUMENT_TYPES_ALL_B` e `PO_DOCUMENT_TYPES_ALL_TL` para **tipos de documento com nomes traduzidos**.

> [!note] Sufixo _VL
> O sufixo `_VL` combina a tabela base `_B` com traducoes `_TL` em uma view multilingue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta simplificada:** Tipos com traducao em uma unica view.
- **LOVs:** Listas de selecao na interface.
- **Relatorios:** Nomes traduzidos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENT_TYPE_CODE | VARCHAR2(25) | NOT NULL | PK | Codigo do tipo | — | 🟢 95% |
| 2 | DOCUMENT_SUBTYPE | VARCHAR2(25) | NOT NULL | PK | Subtipo | — | 🟢 95% |
| 3 | ORG_ID | NUMBER(18) | NOT NULL | PK | Business unit | — | 🟢 95% |
| 4 | TYPE_NAME | VARCHAR2(80) | NULL | Descritivo | Nome traduzido | — | 🟢 95% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Flag | Habilitado | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Tipos traduzidos habilitados
```sql
SELECT DOCUMENT_TYPE_CODE, DOCUMENT_SUBTYPE, TYPE_NAME
FROM   PO_DOCUMENT_TYPES_VL
WHERE  ORG_ID = :p_org_id AND ENABLED_FLAG = 'Y';
```

---

## 🔒 Observações

- Preferir sobre consultas diretas _B/_TL.
- Retorna traducao do idioma da sessao.

---

## 🔗 PVOs Relacionados

### [[agreementlinepvo|AgreementLinePVO]] (PO · BICC: 2/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | FromBlanketDocumentTypeAttributeCategory | — |
| ATTRIBUTE_CATEGORY | FromContractDocumentTypeAttributeCategory | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromBlanketDocumentTypeCoContTermsLayoutCode | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromContractDocumentTypeCoContTermsLayoutCode | — |
| CO_LAYOUT_TEMPLATE | FromBlanketDocumentTypeCoLayoutTemplate | — |
| CO_LAYOUT_TEMPLATE | FromContractDocumentTypeCoLayoutTemplate | — |
| CO_TEMPLATE_ID | FromBlanketDocumentTypeCoTemplateId | — |
| CO_TEMPLATE_ID | FromContractDocumentTypeCoTemplateId | — |
| CONTRACT_TEMPLATE_CODE | FromBlanketDocumentTypeContractTemplateCode | — |
| CONTRACT_TEMPLATE_CODE | FromContractDocumentTypeContractTemplateCode | — |
| CREATED_BY | FromBlanketDocumentTypeCreatedBy | — |
| CREATED_BY | FromContractDocumentTypeCreatedBy | — |
| CREATION_DATE | FromBlanketDocumentTypeCreationDate | — |
| CREATION_DATE | FromContractDocumentTypeCreationDate | — |
| DOCUMENT_SUBTYPE | FromBlanketDocumentTypeDocumentSubtype | — |
| DOCUMENT_SUBTYPE | FromContractDocumentTypeDocumentSubtype | — |
| DOCUMENT_TEMPLATE_CODE | FromBlanketDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TEMPLATE_CODE | FromContractDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TYPE_CODE | FromBlanketDocumentTypeDocumentTypeCode | — |
| DOCUMENT_TYPE_CODE | FromContractDocumentTypeDocumentTypeCode | — |
| LAST_UPDATE_DATE | FromBlanketDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FromBlanketDocumentTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractDocumentTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FromBlanketDocumentTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractDocumentTypeLastUpdatedBy | — |
| PRC_BU_ID | FromBlanketDocumentTypePrcBuId | — |
| PRC_BU_ID | FromContractDocumentTypePrcBuId | — |
| RESPONSE_TEMPLATE_CODE | FromBlanketDocumentTypeResponseTemplateCode | — |
| RESPONSE_TEMPLATE_CODE | FromContractDocumentTypeResponseTemplateCode | — |
| TYPE_NAME | FromBlanketDocumentTypeTypeName | — |
| TYPE_NAME | FromContractDocumentTypeTypeName | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO · BICC: 2/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | FromBlanketDocumentTypeAttributeCategory | — |
| ATTRIBUTE_CATEGORY | FromContractDocumentTypeAttributeCategory | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromBlanketDocumentTypeCoContTermsLayoutCode | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromContractDocumentTypeCoContTermsLayoutCode | — |
| CO_LAYOUT_TEMPLATE | FromBlanketDocumentTypeCoLayoutTemplate | — |
| CO_LAYOUT_TEMPLATE | FromContractDocumentTypeCoLayoutTemplate | — |
| CO_TEMPLATE_ID | FromBlanketDocumentTypeCoTemplateId | — |
| CO_TEMPLATE_ID | FromContractDocumentTypeCoTemplateId | — |
| CONTRACT_TEMPLATE_CODE | FromBlanketDocumentTypeContractTemplateCode | — |
| CONTRACT_TEMPLATE_CODE | FromContractDocumentTypeContractTemplateCode | — |
| CREATED_BY | FromBlanketDocumentTypeCreatedBy | — |
| CREATED_BY | FromContractDocumentTypeCreatedBy | — |
| CREATION_DATE | FromBlanketDocumentTypeCreationDate | — |
| CREATION_DATE | FromContractDocumentTypeCreationDate | — |
| DOCUMENT_SUBTYPE | FromBlanketDocumentTypeDocumentSubtype | — |
| DOCUMENT_SUBTYPE | FromContractDocumentTypeDocumentSubtype | — |
| DOCUMENT_TEMPLATE_CODE | FromBlanketDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TEMPLATE_CODE | FromContractDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TYPE_CODE | FromBlanketDocumentTypeDocumentTypeCode | — |
| DOCUMENT_TYPE_CODE | FromContractDocumentTypeDocumentTypeCode | — |
| LAST_UPDATE_DATE | FromBlanketDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FromBlanketDocumentTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractDocumentTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FromBlanketDocumentTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractDocumentTypeLastUpdatedBy | — |
| PRC_BU_ID | FromBlanketDocumentTypePrcBuId | — |
| PRC_BU_ID | FromContractDocumentTypePrcBuId | — |
| RESPONSE_TEMPLATE_CODE | FromBlanketDocumentTypeResponseTemplateCode | — |
| RESPONSE_TEMPLATE_CODE | FromContractDocumentTypeResponseTemplateCode | — |
| TYPE_NAME | FromBlanketDocumentTypeTypeName | — |
| TYPE_NAME | FromContractDocumentTypeTypeName | — |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO · BICC: 2/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | FromBlanketDocumentTypeAttributeCategory | — |
| ATTRIBUTE_CATEGORY | FromContractDocumentTypeAttributeCategory | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromBlanketDocumentTypeCoContTermsLayoutCode | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromContractDocumentTypeCoContTermsLayoutCode | — |
| CO_LAYOUT_TEMPLATE | FromBlanketDocumentTypeCoLayoutTemplate | — |
| CO_LAYOUT_TEMPLATE | FromContractDocumentTypeCoLayoutTemplate | — |
| CO_TEMPLATE_ID | FromBlanketDocumentTypeCoTemplateId | — |
| CO_TEMPLATE_ID | FromContractDocumentTypeCoTemplateId | — |
| CONTRACT_TEMPLATE_CODE | FromBlanketDocumentTypeContractTemplateCode | — |
| CONTRACT_TEMPLATE_CODE | FromContractDocumentTypeContractTemplateCode | — |
| CREATED_BY | FromBlanketDocumentTypeCreatedBy | — |
| CREATED_BY | FromContractDocumentTypeCreatedBy | — |
| CREATION_DATE | FromBlanketDocumentTypeCreationDate | — |
| CREATION_DATE | FromContractDocumentTypeCreationDate | — |
| DOCUMENT_SUBTYPE | FromBlanketDocumentTypeDocumentSubtype | — |
| DOCUMENT_SUBTYPE | FromContractDocumentTypeDocumentSubtype | — |
| DOCUMENT_TEMPLATE_CODE | FromBlanketDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TEMPLATE_CODE | FromContractDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TYPE_CODE | FromBlanketDocumentTypeDocumentTypeCode | — |
| DOCUMENT_TYPE_CODE | FromContractDocumentTypeDocumentTypeCode | — |
| LAST_UPDATE_DATE | FromBlanketDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FromBlanketDocumentTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractDocumentTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FromBlanketDocumentTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractDocumentTypeLastUpdatedBy | — |
| PRC_BU_ID | FromBlanketDocumentTypePrcBuId | — |
| PRC_BU_ID | FromContractDocumentTypePrcBuId | — |
| RESPONSE_TEMPLATE_CODE | FromBlanketDocumentTypeResponseTemplateCode | — |
| RESPONSE_TEMPLATE_CODE | FromContractDocumentTypeResponseTemplateCode | — |
| TYPE_NAME | FromBlanketDocumentTypeTypeName | — |
| TYPE_NAME | FromContractDocumentTypeTypeName | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | FromBlanketDocumentTypeAttributeCategory | — |
| ATTRIBUTE_CATEGORY | FromContractDocumentTypeAttributeCategory | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromBlanketDocumentTypeCoContTermsLayoutCode | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromContractDocumentTypeCoContTermsLayoutCode | — |
| CO_LAYOUT_TEMPLATE | FromBlanketDocumentTypeCoLayoutTemplate | — |
| CO_LAYOUT_TEMPLATE | FromContractDocumentTypeCoLayoutTemplate | — |
| CO_TEMPLATE_ID | FromBlanketDocumentTypeCoTemplateId | — |
| CO_TEMPLATE_ID | FromContractDocumentTypeCoTemplateId | — |
| CONTRACT_TEMPLATE_CODE | FromBlanketDocumentTypeContractTemplateCode | — |
| CONTRACT_TEMPLATE_CODE | FromContractDocumentTypeContractTemplateCode | — |
| CREATED_BY | FromBlanketDocumentTypeCreatedBy | — |
| CREATED_BY | FromContractDocumentTypeCreatedBy | — |
| CREATION_DATE | FromBlanketDocumentTypeCreationDate | — |
| CREATION_DATE | FromContractDocumentTypeCreationDate | — |
| DOCUMENT_SUBTYPE | FromBlanketDocumentTypeDocumentSubtype | — |
| DOCUMENT_SUBTYPE | FromContractDocumentTypeDocumentSubtype | — |
| DOCUMENT_TEMPLATE_CODE | FromBlanketDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TEMPLATE_CODE | FromContractDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TYPE_CODE | FromBlanketDocumentTypeDocumentTypeCode | — |
| DOCUMENT_TYPE_CODE | FromContractDocumentTypeDocumentTypeCode | — |
| LAST_UPDATE_DATE | FromBlanketDocumentTypeLastUpdateDate | — |
| LAST_UPDATE_DATE | FromContractDocumentTypeLastUpdateDate | — |
| LAST_UPDATE_LOGIN | FromBlanketDocumentTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractDocumentTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FromBlanketDocumentTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractDocumentTypeLastUpdatedBy | — |
| PRC_BU_ID | FromBlanketDocumentTypePrcBuId | — |
| PRC_BU_ID | FromContractDocumentTypePrcBuId | — |
| RESPONSE_TEMPLATE_CODE | FromBlanketDocumentTypeResponseTemplateCode | — |
| RESPONSE_TEMPLATE_CODE | FromContractDocumentTypeResponseTemplateCode | — |
| TYPE_NAME | FromBlanketDocumentTypeTypeName | — |
| TYPE_NAME | FromContractDocumentTypeTypeName | — |

### [[standardlinepvo|StandardLinePVO]] (PO · BICC: 4/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | FromBlanketDocumentTypeAttributeCategory | — |
| ATTRIBUTE_CATEGORY | FromContractDocumentTypeAttributeCategory | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromBlanketDocumentTypeCoContTermsLayoutCode | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromContractDocumentTypeCoContTermsLayoutCode | — |
| CO_LAYOUT_TEMPLATE | FromBlanketDocumentTypeCoLayoutTemplate | — |
| CO_LAYOUT_TEMPLATE | FromContractDocumentTypeCoLayoutTemplate | — |
| CO_TEMPLATE_ID | FromBlanketDocumentTypeCoTemplateId | — |
| CO_TEMPLATE_ID | FromContractDocumentTypeCoTemplateId | — |
| CONTRACT_TEMPLATE_CODE | FromBlanketDocumentTypeContractTemplateCode | — |
| CONTRACT_TEMPLATE_CODE | FromContractDocumentTypeContractTemplateCode | — |
| CREATED_BY | FromBlanketDocumentTypeCreatedBy | — |
| CREATED_BY | FromContractDocumentTypeCreatedBy | — |
| CREATION_DATE | FromBlanketDocumentTypeCreationDate | — |
| CREATION_DATE | FromContractDocumentTypeCreationDate | — |
| DOCUMENT_SUBTYPE | FromBlanketDocumentTypeDocumentSubtype | — |
| DOCUMENT_SUBTYPE | FromContractDocumentTypeDocumentSubtype | — |
| DOCUMENT_TEMPLATE_CODE | FromBlanketDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TEMPLATE_CODE | FromContractDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TYPE_CODE | FromBlanketDocumentTypeDocumentTypeCode | — |
| DOCUMENT_TYPE_CODE | FromContractDocumentTypeDocumentTypeCode | — |
| LAST_UPDATE_DATE | FromBlanketDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractDocumentTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | FromBlanketDocumentTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractDocumentTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FromBlanketDocumentTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractDocumentTypeLastUpdatedBy | — |
| PRC_BU_ID | FromBlanketDocumentTypePrcBuId | — |
| PRC_BU_ID | FromContractDocumentTypePrcBuId | — |
| RESPONSE_TEMPLATE_CODE | FromBlanketDocumentTypeResponseTemplateCode | — |
| RESPONSE_TEMPLATE_CODE | FromContractDocumentTypeResponseTemplateCode | — |
| TYPE_NAME | FromBlanketDocumentTypeTypeName | ✅ |
| TYPE_NAME | FromContractDocumentTypeTypeName | ✅ |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO · BICC: 2/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | FromBlanketDocumentTypeAttributeCategory | — |
| ATTRIBUTE_CATEGORY | FromContractDocumentTypeAttributeCategory | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromBlanketDocumentTypeCoContTermsLayoutCode | — |
| CO_CONT_TERMS_LAYOUT_CODE | FromContractDocumentTypeCoContTermsLayoutCode | — |
| CO_LAYOUT_TEMPLATE | FromBlanketDocumentTypeCoLayoutTemplate | — |
| CO_LAYOUT_TEMPLATE | FromContractDocumentTypeCoLayoutTemplate | — |
| CO_TEMPLATE_ID | FromBlanketDocumentTypeCoTemplateId | — |
| CO_TEMPLATE_ID | FromContractDocumentTypeCoTemplateId | — |
| CONTRACT_TEMPLATE_CODE | FromBlanketDocumentTypeContractTemplateCode | — |
| CONTRACT_TEMPLATE_CODE | FromContractDocumentTypeContractTemplateCode | — |
| CREATED_BY | FromBlanketDocumentTypeCreatedBy | — |
| CREATED_BY | FromContractDocumentTypeCreatedBy | — |
| CREATION_DATE | FromBlanketDocumentTypeCreationDate | — |
| CREATION_DATE | FromContractDocumentTypeCreationDate | — |
| DOCUMENT_SUBTYPE | FromBlanketDocumentTypeDocumentSubtype | — |
| DOCUMENT_SUBTYPE | FromContractDocumentTypeDocumentSubtype | — |
| DOCUMENT_TEMPLATE_CODE | FromBlanketDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TEMPLATE_CODE | FromContractDocumentTypeDocumentTemplateCode | — |
| DOCUMENT_TYPE_CODE | FromBlanketDocumentTypeDocumentTypeCode | — |
| DOCUMENT_TYPE_CODE | FromContractDocumentTypeDocumentTypeCode | — |
| LAST_UPDATE_DATE | FromBlanketDocumentTypeLastUpdateDate | — |
| LAST_UPDATE_DATE | FromContractDocumentTypeLastUpdateDate | — |
| LAST_UPDATE_LOGIN | FromBlanketDocumentTypeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractDocumentTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | FromBlanketDocumentTypeLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractDocumentTypeLastUpdatedBy | — |
| PRC_BU_ID | FromBlanketDocumentTypePrcBuId | — |
| PRC_BU_ID | FromContractDocumentTypePrcBuId | — |
| RESPONSE_TEMPLATE_CODE | FromBlanketDocumentTypeResponseTemplateCode | — |
| RESPONSE_TEMPLATE_CODE | FromContractDocumentTypeResponseTemplateCode | — |
| TYPE_NAME | FromBlanketDocumentTypeTypeName | ✅ |
| TYPE_NAME | FromContractDocumentTypeTypeName | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_DOCUMENT_TYPES_VL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
