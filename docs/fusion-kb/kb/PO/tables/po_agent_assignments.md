---
id: DOC-PO-110
doc_type: system-doc
title: "PO_AGENT_ASSIGNMENTS — Atribuicoes de Categorias por Comprador"
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
  - compradores
  - buyers
  - agents
aliases:
  - PO_AGENT_ASSIGNMENTS
  - po_agent_assignments
  - po-agent-assignments
  - po-agent
  - atribuicoes-de-categorias-por-compr
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_AGENT_ASSIGNMENTS

## 📌 Visão Geral

Armazena as **atribuicoes de categorias de compras a compradores** (agents). Define quais categorias cada comprador esta autorizado a comprar.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Segregacao:** Especializacao por categoria de produto/servico.
- **Roteamento automatico:** Direciona requisicoes ao comprador correto.
- **Controle de alcada:** Restricoes por categoria alem do limite financeiro.
- **Relatorios de carga:** Distribuicao de trabalho entre compradores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | ID da atribuicao | — | 🟡 80% |
| 2 | AGENT_ID | NUMBER(18) | NOT NULL | FK | Comprador | [[po_agents_v]] | 🟢 95% |
| 3 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[egp_categories_b]] | 🟢 90% |
| 4 | ITEM_ID | NUMBER(18) | NULL | FK | Item especifico (opcional) | [[egp_system_items_b]] | 🟡 75% |
| 5 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_agents_v]] — via `AGENT_ID` (comprador atribuído à designação)
- [[egp_categories_b]] — via `CATEGORY_ID` (categoria de item atribuída ao comprador)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da atribuição do comprador)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Categorias de um comprador
```sql
SELECT AGENT_ID, CATEGORY_ID
FROM   PO_AGENT_ASSIGNMENTS
WHERE  AGENT_ID = :p_agent_id;
```

---

## 🔒 Observações

- Atribuicao por categoria ou item especifico.
- Sem atribuicao, comprador pode ter acesso irrestrito (depende da config).
- Utilizada pelo AutoCreate para roteamento.

---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | BuyerAssignmentActiveFlag | — |
| AGENT_ID | BuyerAssignmentAgentId | — |
| ASSIGNMENT_ID | BuyerAssignmentAssignmentId | — |
| CREATED_BY | BuyerAssignmentCreatedBy | — |
| CREATION_DATE | BuyerAssignmentCreationDate | — |
| DEFAULT_REQ_BU_ID | BuyerAssignmentDefaultReqBuId | — |
| LAST_UPDATE_DATE | BuyerAssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BuyerAssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | BuyerAssignmentLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | BuyerAssignmentObjectVersionNumber | — |
| PRC_BU_ID | BuyerAssignmentPrcBuId | — |

### [[inventoryitemref|InventoryItemRef]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGENT_ID | AgentAssignmentPEOAgentId | — |
| ASSIGNMENT_ID | AgentAssignmentPEOAssignmentId | — |

### [[itemref|ItemRef]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGENT_ID | AgentAssignmentPEOAgentId | — |
| ASSIGNMENT_ID | AgentAssignmentPEOAssignmentId | — |

### [[procurementbuyersextractpvo|ProcurementBuyersExtractPVO]] (PO · BICC: 12/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_FLAG | ActiveFlag | ✅ |
| AGENT_ID | AgentId | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
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
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEFAULT_PRINTER_NAME | DefaultPrinterName | ✅ |
| DEFAULT_REQ_BU_ID | DefaultReqBuId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PO_AGENT_ASSIGNMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
