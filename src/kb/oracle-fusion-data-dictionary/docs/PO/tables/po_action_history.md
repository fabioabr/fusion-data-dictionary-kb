---
id: DOC-PO-108
doc_type: system-doc
title: "PO_ACTION_HISTORY — Historico de Acoes em Documentos de Compras"
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
  - historico-acoes
  - workflow
  - approval
aliases:
  - PO_ACTION_HISTORY
  - po_action_history
  - po-action-history
  - po-action
  - historico-de-acoes-em-documentos-de
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_ACTION_HISTORY

## 📌 Visão Geral

Armazena o **historico de acoes realizadas em documentos de compras** (POs, requisicoes, agreements). Cada registro representa uma acao de workflow — submissao, aprovacao, rejeicao, cancelamento — com timestamp, usuario e comentario.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria de aprovacoes:** Rastreamento completo de aprovacoes/rejeicoes.
- **Workflow tracking:** Analise de tempo de ciclo e gargalos.
- **Compliance (SoD):** Segregacao de funcoes em compras.
- **Relatorios:** Tempo medio de aprovacao por tipo de documento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OBJECT_ID | NUMBER(18) | NOT NULL | FK | ID do documento (PO_HEADER_ID, etc.) | [[po_headers_all]] | 🟢 95% |
| 2 | OBJECT_TYPE_CODE | VARCHAR2(25) | NOT NULL | Classificacao | Tipo: PO, PA, RELEASE, REQUISITION | — | 🟢 95% |
| 3 | OBJECT_SUB_TYPE_CODE | VARCHAR2(25) | NULL | Classificacao | Subtipo do objeto | — | 🟢 90% |
| 4 | SEQUENCE_NUM | NUMBER | NOT NULL | PK | Sequencia da acao | — | 🟢 95% |
| 5 | ACTION_CODE | VARCHAR2(25) | NULL | Classificacao | SUBMIT, APPROVE, REJECT, RETURN, CANCEL | — | 🟢 95% |
| 6 | ACTION_DATE | DATE | NULL | Data | Data da acao | — | 🟢 95% |
| 7 | EMPLOYEE_ID | NUMBER(18) | NULL | FK | Funcionario executor | [[per_all_people_f]] | 🟢 90% |
| 8 | NOTE | VARCHAR2(4000) | NULL | Texto livre | Comentario/justificativa | — | 🟢 90% |
| 9 | OBJECT_REVISION_NUM | NUMBER | NULL | Versionamento | Revisao do documento | — | 🟢 85% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `OBJECT_ID` (pedido de compra associado à ação registrada)
- [[per_all_people_f]] — via `EMPLOYEE_ID` (funcionário que executou a ação no PO)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Historico de acoes de um PO
```sql
SELECT SEQUENCE_NUM, ACTION_CODE, ACTION_DATE, EMPLOYEE_ID, NOTE
FROM   PO_ACTION_HISTORY
WHERE  OBJECT_ID = :p_po_header_id
  AND  OBJECT_TYPE_CODE = 'PO'
ORDER BY SEQUENCE_NUM;
```

---

## 🔒 Observações

- PK composta: `OBJECT_ID` + `OBJECT_TYPE_CODE` + `SEQUENCE_NUM`.
- O `OBJECT_TYPE_CODE` determina a tabela-pai (PO, REQUISITION, etc.).
- Acoes automaticas podem ter `EMPLOYEE_ID` nulo.
- Campo `NOTE` contem justificativas obrigatorias em rejeicoes.

---

## 🔗 PVOs Relacionados

### [[agreementheaderpvo|AgreementHeaderPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[agreementlinepvo|AgreementLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| OBJECT_ID | ObjectId | — |
| OBJECT_SUB_TYPE_CODE | ObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | ObjectTypeCode | — |
| SEQUENCE_NUM | SequenceNum | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | ✅ |
| OBJECT_ID | ObjectId | — |
| OBJECT_SUB_TYPE_CODE | ObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | ObjectTypeCode | — |
| SEQUENCE_NUM | SequenceNum | — |

### [[purchaseorderhistorypvo|PurchaseOrderHistoryPVO]] (PO · BICC: 10/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | PurchasingActionHistoryActionCode | ✅ |
| ACTION_DATE | PurchasingActionHistoryActionDate | ✅ |
| ACTION_LEVEL | PurchasingActionHistoryActionLevel | — |
| ASSIGNMENT_DATE | PurchasingActionHistoryAssignmentDate | ✅ |
| CREATED_BY | PurchasingActionHistoryCreatedBy | — |
| CREATION_DATE | PurchasingActionHistoryCreationDate | — |
| IDENTIFICATION_KEY | PurchasingActionHistoryIdentificationKey | — |
| LAST_UPDATE_DATE | PurchasingActionHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingActionHistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingActionHistoryLastUpdatedBy | — |
| NOTE | PurchasingActionHistoryNote | ✅ |
| OBJECT_ID | ObjectId | ✅ |
| OBJECT_REVISION_NUM | PurchasingActionHistoryObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | ObjectSubTypeCode | ✅ |
| OBJECT_TYPE_CODE | ObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | PurchasingActionHistoryObjectVersionNumber | — |
| OFFLINE_CODE | PurchasingActionHistoryOfflineCode | — |
| PERFORMER_ID | PurchasingActionHistoryPerformerId | — |
| PO_VERSION_ID | PurchasingActionHistoryPoVersionId | — |
| PROGRAM_DATE | PurchasingActionHistoryProgramDate | — |
| ROLE_CODE | PurchasingActionHistoryRoleCode | ✅ |
| SEQUENCE_NUM | SequenceNum | ✅ |
| SUPPLIER_ACCESSIBLE_FLAG | PurchasingActionHistorySupplierAccessibleFlag | — |

### [[purchasingdocumentactionhistoryextractpvo|PurchasingDocumentActionHistoryExtractPVO]] (PO · BICC: 22/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionCode | ✅ |
| ACTION_DATE | ActionDate | ✅ |
| ASSIGNMENT_DATE | AssignmentDate | ✅ |
| CORRELATION_ID | CorrelationId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| IDENTIFICATION_KEY | IdentificationKey | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NOTE | Note | ✅ |
| OBJECT_ID | ObjectId | ✅ |
| OBJECT_REVISION_NUM | ObjectRevisionNum | ✅ |
| OBJECT_SUB_TYPE_CODE | ObjectSubTypeCode | ✅ |
| OBJECT_TYPE_CODE | ObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OFFLINE_CODE | OfflineCode | ✅ |
| PERFORMER_ID | PerformerId | ✅ |
| PO_VERSION_ID | PoVersionId | ✅ |
| ROLE_CODE | RoleCode | ✅ |
| SEQUENCE_NUM | SequenceNum | ✅ |
| SUPPLIER_ACCESSIBLE_FLAG | SupplierAccessibleFlag | ✅ |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[requisitionactionhistorypvo|RequisitionActionHistoryPVO]] (PO · BICC: 10/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | PurchasingActionHistoryActionCode | ✅ |
| ACTION_DATE | PurchasingActionHistoryActionDate | ✅ |
| ACTION_LEVEL | PurchasingActionHistoryActionLevel | — |
| ASSIGNMENT_DATE | PurchasingActionHistoryAssignmentDate | ✅ |
| CREATED_BY | PurchasingActionHistoryCreatedBy | — |
| CREATION_DATE | PurchasingActionHistoryCreationDate | — |
| IDENTIFICATION_KEY | PurchasingActionHistoryIdentificationKey | — |
| LAST_UPDATE_DATE | PurchasingActionHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingActionHistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingActionHistoryLastUpdatedBy | — |
| NOTE | PurchasingActionHistoryNote | ✅ |
| OBJECT_ID | ObjectId | ✅ |
| OBJECT_REVISION_NUM | PurchasingActionHistoryObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | ObjectSubTypeCode | ✅ |
| OBJECT_TYPE_CODE | ObjectTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | PurchasingActionHistoryObjectVersionNumber | — |
| OFFLINE_CODE | PurchasingActionHistoryOfflineCode | — |
| PERFORMER_ID | PurchasingActionHistoryPerformerId | — |
| PO_VERSION_ID | PurchasingActionHistoryPoVersionId | — |
| PROGRAM_DATE | PurchasingActionHistoryProgramDate | — |
| ROLE_CODE | PurchasingActionHistoryRoleCode | ✅ |
| SEQUENCE_NUM | SequenceNum | ✅ |
| SUPPLIER_ACCESSIBLE_FLAG | PurchasingActionHistorySupplierAccessibleFlag | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | PurchasingDocumentActionHistActionCode | — |
| ACTION_DATE | RequisitionHeaderCanceledDate | ✅ |
| NOTE | RequisitionHeaderCanceledReason | ✅ |
| OBJECT_ID | PurchasingDocumentActionHistObjectId | — |
| OBJECT_SUB_TYPE_CODE | PurchasingDocumentActionHistObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | PurchasingDocumentActionHistObjectTypeCode | — |
| SEQUENCE_NUM | PurchasingDocumentActionHistSequenceNum | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | PurchasingDocumentActionHistActionCode | — |
| ACTION_DATE | RequisitionHeaderCanceledDate | ✅ |
| NOTE | RequisitionHeaderCanceledReason | ✅ |
| OBJECT_ID | PurchasingDocumentActionHistObjectId | — |
| OBJECT_SUB_TYPE_CODE | PurchasingDocumentActionHistObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | PurchasingDocumentActionHistObjectTypeCode | — |
| SEQUENCE_NUM | PurchasingDocumentActionHistSequenceNum | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | PurchasingDocumentActionHistActionCode | — |
| ACTION_DATE | RequisitionHeaderCanceledDate | ✅ |
| NOTE | RequisitionHeaderCanceledReason | ✅ |
| OBJECT_ID | PurchasingDocumentActionHistObjectId | — |
| OBJECT_SUB_TYPE_CODE | PurchasingDocumentActionHistObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | PurchasingDocumentActionHistObjectTypeCode | — |
| SEQUENCE_NUM | PurchasingDocumentActionHistSequenceNum | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[standardheaderpvo|StandardHeaderPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[standardlinepvo|StandardLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | DocumentCancelActionActionCode | — |
| ACTION_DATE | DocumentCancelActionActionDate | — |
| ACTION_LEVEL | DocumentCancelActionActionLevel | — |
| IDENTIFICATION_KEY | DocumentCancelActionIdentificationKey | — |
| NOTE | DocumentCancelActionNote | — |
| OBJECT_ID | DocumentCancelActionObjectId | — |
| OBJECT_REVISION_NUM | DocumentCancelActionObjectRevisionNum | — |
| OBJECT_SUB_TYPE_CODE | DocumentCancelActionObjectSubTypeCode | — |
| OBJECT_TYPE_CODE | DocumentCancelActionObjectTypeCode | — |
| OFFLINE_CODE | DocumentCancelActionOfflineCode | — |
| PERFORMER_ID | DocumentCancelActionPerformerId | — |
| PO_VERSION_ID | DocumentCancelActionPoVersionId | — |
| PROGRAM_DATE | DocumentCancelActionProgramDate | — |
| ROLE_CODE | DocumentCancelActionRoleCode | — |
| SEQUENCE_NUM | DocumentCancelActionSequenceNum | — |
| SUPPLIER_ACCESSIBLE_FLAG | DocumentCancelActionSupplierAccessibleFlag | — |

---

## 📚 Referências

- [Oracle Docs — PO_ACTION_HISTORY](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poactionhistory-25428.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
