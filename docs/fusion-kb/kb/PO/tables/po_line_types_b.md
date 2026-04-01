---
id: DOC-PO-136
doc_type: system-doc
title: "PO_LINE_TYPES_B — Tipos de Linha de PO (Base)"
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
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - PO_LINE_TYPES_B
  - po_line_types_b
  - po-line-types-b
  - po-line
  - tipos-de-linha-de-po-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_LINE_TYPES_B

## 📌 Visão Geral

Armazena os **tipos de linha de PO**: Goods, Services, Fixed Price, Amount, Rate, etc.

> [!note] Sufixo _B
> O sufixo `_B` indica a **tabela base** (idioma base). Traducoes ficam na tabela correspondente `_TL`.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuracao:** Tipos de linha disponiveis.
- **Regras:** Quantidade/preco vs apenas valor.
- **Matching:** Comportamento por tipo de linha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LINE_TYPE_ID | NUMBER(18) | NOT NULL | PK | ID do tipo | — | 🟢 95% |
| 2 | ORDER_TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificacao | QUANTITY, AMOUNT, FIXED PRICE, RATE | — | 🟢 95% |
| 3 | PURCHASE_BASIS | VARCHAR2(25) | NULL | Classificacao | GOODS, SERVICES, TEMP LABOR | — | 🟢 90% |
| 4 | MATCHING_BASIS | VARCHAR2(25) | NULL | Classificacao | QUANTITY ou AMOUNT | — | 🟢 90% |
| 5 | OUTSIDE_OPERATION_FLAG | VARCHAR2(1) | NULL | Flag | Operacao externa | — | 🟡 80% |
| 6 | RECEIVING_FLAG | VARCHAR2(1) | NULL | Flag | Requer recebimento | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta identificada

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Tipos de linha
```sql
SELECT LINE_TYPE_ID, ORDER_TYPE_LOOKUP_CODE, PURCHASE_BASIS, MATCHING_BASIS
FROM   PO_LINE_TYPES_B;
```

---

## 🔒 Observações

- Tabela de configuracao; poucas linhas seeded.
- O `PURCHASE_BASIS` define bens, servicos ou mao de obra.
- O `MATCHING_BASIS` controla matching por quantidade ou valor.

---

## 🔗 PVOs Relacionados

### [[purchasinglinetypebextractpvo|PurchasingLineTypeBExtractPVO]] (PO · BICC: 18/69)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | — |
| CATEGORY_ID | CategoryId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| INACTIVE_DATE | InactiveDate | ✅ |
| INSPECTION_REQUIRED_FLAG | InspectionRequiredFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LINE_TYPE_CODE | LineTypeCode | ✅ |
| LINE_TYPE_ID | LineTypeId | ✅ |
| MATCH_OPTION | MatchOption | ✅ |
| MATCHING_BASIS | MatchingBasis | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PURCHASE_BASIS | PurchaseBasis | ✅ |
| RECEIVE_CLOSE_TOLERANCE | ReceiveCloseTolerance | ✅ |
| RECEIVING_FLAG | ReceivingFlag | ✅ |
| UNIT_OF_MEASURE | UnitOfMeasure | ✅ |
| UOM_CODE | UomCode | ✅ |

### [[purchasinglinetypebp|PurchasingLineTypeBP]] (PO · BICC: 12/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | POLineTypeBCategoryId | — |
| CREATED_BY | POLineTypeBCreatedBy | ✅ |
| CREATION_DATE | POLineTypeBCreationDate | ✅ |
| INACTIVE_DATE | POLineTypeBInactiveDate | ✅ |
| INSPECTION_REQUIRED_FLAG | POLineTypeBInspectionRequiredFlag | ✅ |
| LAST_UPDATE_DATE | POLineTypeBLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | POLineTypeBLastUpdateLogin | — |
| LAST_UPDATED_BY | POLineTypeBLastUpdatedBy | ✅ |
| LINE_TYPE_CODE | POLineTypeBLineTypeCode | ✅ |
| LINE_TYPE_ID | LineTypeId | ✅ |
| MATCH_OPTION | POLineTypeBMatchOption | — |
| MATCHING_BASIS | POLineTypeBMatchingBasis | ✅ |
| OBJECT_VERSION_NUMBER | POLineTypeBObjectVersionNumber | — |
| ORDER_TYPE_LOOKUP_CODE | POLineTypeBOrderTypeLookupCode | ✅ |
| OUTSIDE_OPERATION_FLAG | POLineTypeBOutsideOperationFlag | — |
| PURCHASE_BASIS | POLineTypeBPurchaseBasis | ✅ |
| RECEIVE_CLOSE_TOLERANCE | POLineTypeBReceiveCloseTolerance | ✅ |
| RECEIVING_FLAG | POLineTypeBReceivingFlag | — |
| UNIT_OF_MEASURE | POLineTypeBUnitOfMeasure | — |
| UNIT_PRICE | POLineTypeBUnitPrice | — |
| UOM_CODE | POLineTypeBUomCode | — |

---

## 📚 Referências

- [Oracle Docs — PO_LINE_TYPES_B](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
