---
id: DOC-PO-114
doc_type: system-doc
title: "PO_ATTRIBUTE_VALUES — Valores de Atributos de Itens em POs"
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
  - atributos
  - flexfields
  - customizacao
aliases:
  - PO_ATTRIBUTE_VALUES
  - po_attribute_values
  - po-attribute-values
  - po-attribute
  - valores-de-atributos-de-itens-em-po
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ATTRIBUTE_VALUES

## 📌 Visão Geral

Armazena os **valores de atributos descritivos de itens** em linhas de PO. Permite atributos customizaveis e informacoes de catalogo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Catalogo de itens:** Atributos descritivos (cor, tamanho, especificacao).
- **Punch-out:** Atributos de catalogos externos (cXML/OCI).
- **Busca e filtro:** Atributos para busca no catalogo interno.
- **Integracao:** Interoperabilidade com ERPs/catalogos externos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ATTRIBUTE_VALUES_ID | NUMBER(18) | NOT NULL | PK | ID unico | — | 🟡 80% |
| 2 | PO_LINE_ID | NUMBER(18) | NULL | FK | Linha do PO | [[po_lines_all]] | 🟢 90% |
| 3 | REQ_TEMPLATE_NAME | VARCHAR2(25) | NULL | Classificacao | Template de requisicao | — | 🟡 70% |
| 4 | IP_CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria iProcurement | — | 🟡 65% |
| 5 | MANUFACTURER_NAME | VARCHAR2(240) | NULL | Dados | Fabricante | — | 🟡 75% |
| 6 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descricao do atributo | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_lines_all]] — via `PO_LINE_ID` (linha do PO à qual os atributos se referem)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Atributos de uma linha
```sql
SELECT ATTRIBUTE_VALUES_ID, MANUFACTURER_NAME, DESCRIPTION
FROM   PO_ATTRIBUTE_VALUES
WHERE  PO_LINE_ID = :p_line_id;
```

---

## 🔒 Observações

- Tabela de extensao para catalogo/iProcurement.
- Registros criados automaticamente durante punch-out.
- Complementa `PO_LINES_ALL`.

---

## 🔗 PVOs Relacionados

### [[agreementlinepvo|AgreementLinePVO]] (PO · BICC: 10/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTACHMENT_URL | PurchasingAttributeValueAttachmentUrl | ✅ |
| ATTRIBUTE_VALUES_ID | PurchasingAttributeValueAttributeValuesId | — |
| AVAILABILITY | PurchasingAttributeValueAvailability | ✅ |
| CREATED_BY | PurchasingAttributeValueCreatedBy | — |
| CREATION_DATE | PurchasingAttributeValueCreationDate | — |
| JOB_DEFINITION_NAME | PurchasingAttributeValueJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingAttributeValueJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingAttributeValueLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingAttributeValueLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingAttributeValueLastUpdatedBy | — |
| LAST_UPDATED_PROGRAM | PurchasingAttributeValueLastUpdatedProgram | — |
| LEAD_TIME | PurchasingAttributeValueLeadTime | ✅ |
| MANUFACTURER_PART_NUM | PurchasingAttributeValueManufacturerPartNum | ✅ |
| MANUFACTURER_URL | PurchasingAttributeValueManufacturerUrl | ✅ |
| OBJECT_VERSION_NUMBER | PurchasingAttributeValueObjectVersionNumber | — |
| PICTURE | PurchasingAttributeValuePicture | ✅ |
| PO_HEADER_ID | PurchasingAttributeValuePoHeaderId | — |
| PO_LINE_ID | PurchasingAttributeValuePoLineId | — |
| PRC_BU_ID | PurchasingAttributeValuePrcBuId | — |
| REBUILD_SEARCH_INDEX_FLAG | PurchasingAttributeValueRebuildSearchIndexFlag | — |
| REQUEST_ID | PurchasingAttributeValueRequestId | — |
| SUPPLIER_URL | PurchasingAttributeValueSupplierUrl | ✅ |
| THUMBNAIL_IMAGE | PurchasingAttributeValueThumbnailImage | ✅ |
| UNSPSC | PurchasingAttributeValueUnspsc | ✅ |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO · BICC: 10/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTACHMENT_URL | PurchasingAttributeValueAttachmentUrl | ✅ |
| ATTRIBUTE_VALUES_ID | PurchasingAttributeValueAttributeValuesId | — |
| AVAILABILITY | PurchasingAttributeValueAvailability | ✅ |
| CREATED_BY | PurchasingAttributeValueCreatedBy | — |
| CREATION_DATE | PurchasingAttributeValueCreationDate | — |
| JOB_DEFINITION_NAME | PurchasingAttributeValueJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingAttributeValueJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingAttributeValueLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingAttributeValueLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingAttributeValueLastUpdatedBy | — |
| LAST_UPDATED_PROGRAM | PurchasingAttributeValueLastUpdatedProgram | — |
| LEAD_TIME | PurchasingAttributeValueLeadTime | ✅ |
| MANUFACTURER_PART_NUM | PurchasingAttributeValueManufacturerPartNum | ✅ |
| MANUFACTURER_URL | PurchasingAttributeValueManufacturerUrl | ✅ |
| OBJECT_VERSION_NUMBER | PurchasingAttributeValueObjectVersionNumber | — |
| PICTURE | PurchasingAttributeValuePicture | ✅ |
| PO_HEADER_ID | PurchasingAttributeValuePoHeaderId | — |
| PO_LINE_ID | PurchasingAttributeValuePoLineId | — |
| PRC_BU_ID | PurchasingAttributeValuePrcBuId | — |
| REBUILD_SEARCH_INDEX_FLAG | PurchasingAttributeValueRebuildSearchIndexFlag | — |
| REQUEST_ID | PurchasingAttributeValueRequestId | — |
| SUPPLIER_URL | PurchasingAttributeValueSupplierUrl | ✅ |
| THUMBNAIL_IMAGE | PurchasingAttributeValueThumbnailImage | ✅ |
| UNSPSC | PurchasingAttributeValueUnspsc | ✅ |

### [[purchasingattributevaluesextractpvo|PurchasingAttributeValuesExtractPVO]] (PO · BICC: 26/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTACHMENT_URL | AttachmentUrl | ✅ |
| ATTRIBUTE_VALUES_ID | AttributeValuesId | ✅ |
| AVAILABILITY | Availability | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAST_UPDATED_PROGRAM | LastUpdatedProgram | ✅ |
| LEAD_TIME | LeadTime | ✅ |
| MANUFACTURER_PART_NUM | ManufacturerPartNum | ✅ |
| MANUFACTURER_URL | ManufacturerUrl | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PACKAGING_STRING | PackagingString | ✅ |
| PICTURE | Picture | ✅ |
| PO_HEADER_ID | PoHeaderId | ✅ |
| PO_LINE_ID | PoLineId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| REBUILD_SEARCH_INDEX_FLAG | RebuildSearchIndexFlag | ✅ |
| REQUEST_ID | RequestId | ✅ |
| ROUNDING_FACTOR | RoundingFactor | ✅ |
| SUPPLIER_URL | SupplierUrl | ✅ |
| THUMBNAIL_IMAGE | ThumbnailImage | ✅ |
| UNSPSC | Unspsc | ✅ |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO · BICC: 1/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTACHMENT_URL | PurchasingAttributeValueAttachmentUrl | — |
| ATTRIBUTE_VALUES_ID | PurchasingAttributeValueAttributeValuesId | — |
| AVAILABILITY | PurchasingAttributeValueAvailability | — |
| CREATED_BY | PurchasingAttributeValueCreatedBy | — |
| CREATION_DATE | PurchasingAttributeValueCreationDate | — |
| JOB_DEFINITION_NAME | PurchasingAttributeValueJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingAttributeValueJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingAttributeValueLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingAttributeValueLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingAttributeValueLastUpdatedBy | — |
| LAST_UPDATED_PROGRAM | PurchasingAttributeValueLastUpdatedProgram | — |
| LEAD_TIME | PurchasingAttributeValueLeadTime | — |
| MANUFACTURER_PART_NUM | PurchasingAttributeValueManufacturerPartNum | — |
| MANUFACTURER_URL | PurchasingAttributeValueManufacturerUrl | — |
| OBJECT_VERSION_NUMBER | PurchasingAttributeValueObjectVersionNumber | — |
| PICTURE | PurchasingAttributeValuePicture | — |
| PO_HEADER_ID | PurchasingAttributeValuePoHeaderId | — |
| PO_LINE_ID | PurchasingAttributeValuePoLineId | — |
| PRC_BU_ID | PurchasingAttributeValuePrcBuId | — |
| REBUILD_SEARCH_INDEX_FLAG | PurchasingAttributeValueRebuildSearchIndexFlag | — |
| REQUEST_ID | PurchasingAttributeValueRequestId | — |
| SUPPLIER_URL | PurchasingAttributeValueSupplierUrl | — |
| THUMBNAIL_IMAGE | PurchasingAttributeValueThumbnailImage | — |
| UNSPSC | PurchasingAttributeValueUnspsc | — |

### [[standardlinepvo|StandardLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTACHMENT_URL | PurchasingAttributeValueAttachmentUrl | — |
| ATTRIBUTE_VALUES_ID | PurchasingAttributeValueAttributeValuesId | — |
| AVAILABILITY | PurchasingAttributeValueAvailability | — |
| CREATED_BY | PurchasingAttributeValueCreatedBy | — |
| CREATION_DATE | PurchasingAttributeValueCreationDate | — |
| JOB_DEFINITION_NAME | PurchasingAttributeValueJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingAttributeValueJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingAttributeValueLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchasingAttributeValueLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingAttributeValueLastUpdatedBy | — |
| LAST_UPDATED_PROGRAM | PurchasingAttributeValueLastUpdatedProgram | — |
| LEAD_TIME | PurchasingAttributeValueLeadTime | — |
| MANUFACTURER_PART_NUM | PurchasingAttributeValueManufacturerPartNum | — |
| MANUFACTURER_URL | PurchasingAttributeValueManufacturerUrl | — |
| OBJECT_VERSION_NUMBER | PurchasingAttributeValueObjectVersionNumber | — |
| PICTURE | PurchasingAttributeValuePicture | — |
| PO_HEADER_ID | PurchasingAttributeValuePoHeaderId | — |
| PO_LINE_ID | PurchasingAttributeValuePoLineId | — |
| PRC_BU_ID | PurchasingAttributeValuePrcBuId | — |
| REBUILD_SEARCH_INDEX_FLAG | PurchasingAttributeValueRebuildSearchIndexFlag | — |
| REQUEST_ID | PurchasingAttributeValueRequestId | — |
| SUPPLIER_URL | PurchasingAttributeValueSupplierUrl | — |
| THUMBNAIL_IMAGE | PurchasingAttributeValueThumbnailImage | — |
| UNSPSC | PurchasingAttributeValueUnspsc | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTACHMENT_URL | PurchasingAttributeValueAttachmentUrl | — |
| ATTRIBUTE_VALUES_ID | PurchasingAttributeValueAttributeValuesId | — |
| AVAILABILITY | PurchasingAttributeValueAvailability | — |
| CREATED_BY | PurchasingAttributeValueCreatedBy | — |
| CREATION_DATE | PurchasingAttributeValueCreationDate | — |
| JOB_DEFINITION_NAME | PurchasingAttributeValueJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingAttributeValueJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingAttributeValueLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchasingAttributeValueLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingAttributeValueLastUpdatedBy | — |
| LAST_UPDATED_PROGRAM | PurchasingAttributeValueLastUpdatedProgram | — |
| LEAD_TIME | PurchasingAttributeValueLeadTime | — |
| MANUFACTURER_PART_NUM | PurchasingAttributeValueManufacturerPartNum | — |
| MANUFACTURER_URL | PurchasingAttributeValueManufacturerUrl | — |
| OBJECT_VERSION_NUMBER | PurchasingAttributeValueObjectVersionNumber | — |
| PICTURE | PurchasingAttributeValuePicture | — |
| PO_HEADER_ID | PurchasingAttributeValuePoHeaderId | — |
| PO_LINE_ID | PurchasingAttributeValuePoLineId | — |
| PRC_BU_ID | PurchasingAttributeValuePrcBuId | — |
| REBUILD_SEARCH_INDEX_FLAG | PurchasingAttributeValueRebuildSearchIndexFlag | — |
| REQUEST_ID | PurchasingAttributeValueRequestId | — |
| SUPPLIER_URL | PurchasingAttributeValueSupplierUrl | — |
| THUMBNAIL_IMAGE | PurchasingAttributeValueThumbnailImage | — |
| UNSPSC | PurchasingAttributeValueUnspsc | — |

---

## 📚 Referências

- [Oracle Docs — PO_ATTRIBUTE_VALUES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
