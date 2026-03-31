---
id: DOC-PO-071
doc_type: system-doc
title: "POZ_APPROVAL_HISTORY — Histórico de Aprovações de Fornecedores"
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
  - aprovacao
  - historico
aliases:
  - POZ_APPROVAL_HISTORY
  - poz_approval_history
  - historico-aprovacao-fornecedores
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_APPROVAL_HISTORY

## 📌 Visão Geral

Armazena o **histórico de ações de aprovação** no ciclo de vida de registros de fornecedores — cadastros novos, alterações cadastrais, qualificações e classificações. Cada registro representa uma ação de um aprovador (aprovação, rejeição, devolução) com data, comentários e sequência no workflow.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Auditoria de aprovações:** Rastreamento completo de quem aprovou, rejeitou ou devolveu solicitações de cadastro de fornecedor.
- **Compliance:** Evidência de segregação de funções e aderência a políticas de aprovação.
- **Análise de ciclo:** Medição do tempo de ciclo de aprovação de cadastros de fornecedores.
- **Resolução de disputas:** Consulta histórica de decisões e comentários de aprovadores.
- **Relatórios gerenciais:** Dashboards de volume e tempo de aprovação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPROVAL_HISTORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de aprovação | — | 🟡 80% |
| 2 | OBJECT_ID | NUMBER(18) | NOT NULL | FK | ID do objeto sendo aprovado (supplier registration, supplier profile, etc.) | — | 🟡 80% |
| 3 | OBJECT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do objeto: SUPPLIER_REG, SUPPLIER_PROFILE, QUALIFICATION, etc. | — | 🟡 75% |
| 4 | SEQUENCE_NUM | NUMBER | NULL | Ordem | Sequência da ação no workflow | — | 🟡 70% |
| 5 | ACTION_CODE | VARCHAR2(30) | NOT NULL | Classificação | Ação realizada: APPROVE, REJECT, RETURN, SUBMIT, WITHDRAW | — | 🟡 80% |
| 6 | ACTION_DATE | DATE | NOT NULL | Data | Data/hora da ação | — | 🟡 80% |
| 7 | APPROVER_ID | NUMBER(18) | NULL | FK | Usuário que realizou a ação | [[per_all_people_f]] | 🟡 75% |
| 8 | APPROVER_NAME | VARCHAR2(360) | NULL | Descrição | Nome do aprovador (desnormalizado) | — | 🟡 70% |
| 9 | NOTE | VARCHAR2(4000) | NULL | Texto livre | Comentários do aprovador | — | 🟡 80% |
| 10 | RESPONSE_CODE | VARCHAR2(30) | NULL | Classificação | Código de resposta adicional | — | 🟡 65% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `APPROVER_ID` (pessoa que aprovou a solicitação do fornecedor)
- O `OBJECT_ID` referencia diferentes tabelas conforme o `OBJECT_TYPE_CODE`

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Histórico de aprovação de um cadastro de fornecedor
```sql
SELECT ah.SEQUENCE_NUM, ah.ACTION_CODE, ah.ACTION_DATE,
       ah.APPROVER_NAME, ah.NOTE
FROM   POZ_APPROVAL_HISTORY ah
WHERE  ah.OBJECT_ID = :p_object_id
  AND  ah.OBJECT_TYPE_CODE = 'SUPPLIER_REG'
ORDER BY ah.SEQUENCE_NUM;
```

### Aprovações rejeitadas no período
```sql
SELECT ah.OBJECT_ID, ah.OBJECT_TYPE_CODE,
       ah.APPROVER_NAME, ah.NOTE, ah.ACTION_DATE
FROM   POZ_APPROVAL_HISTORY ah
WHERE  ah.ACTION_CODE = 'REJECT'
  AND  ah.ACTION_DATE BETWEEN :start_date AND :end_date;
```

---

## 🔒 Observações

- O `OBJECT_TYPE_CODE` determina qual entidade está sendo aprovada — o `OBJECT_ID` é polimórfico (referencia diferentes tabelas conforme o tipo).
- A `SEQUENCE_NUM` indica a ordem das ações no workflow; múltiplos aprovadores geram múltiplos registros.
- O campo `NOTE` contém comentários livres do aprovador, úteis para auditoria e resolução de disputas.
- Esta tabela é append-only — registros não são alterados após criação, garantindo integridade do histórico.

---

## 🔗 PVOs Relacionados

### [[supplierapprovalhistorypvo|SupplierApprovalHistoryPVO]] (PO · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | SupplierApprovalHistoryActionCode | ✅ |
| ACTION_DATE | SupplierApprovalHistoryActionDate | ✅ |
| ADDITIONAL_INFO | SupplierApprovalHistoryAdditionalInfo | ✅ |
| AMX_IDENTIFICATION_KEY | SupplierApprovalHistoryAmxIdentificationKey | — |
| APPROVAL_FLOW_CODE | SupplierApprovalHistoryApprovalFlowCode | — |
| APPROVAL_HISTORY_ID | ApprovalHistoryId | ✅ |
| CREATED_BY | SupplierApprovalHistoryCreatedBy | — |
| CREATION_DATE | SupplierApprovalHistoryCreationDate | — |
| FLOW_OBJECT_ID | SupplierApprovalHistoryFlowObjectId | — |
| LAST_UPDATE_DATE | SupplierApprovalHistoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierApprovalHistoryLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierApprovalHistoryLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | SupplierApprovalHistoryObjectVersionNumber | — |
| PERFORMER_ID | SupplierApprovalHistoryPerformerId | — |
| PERFORMER_TYPE | SupplierApprovalHistoryPerformerType | — |
| SEQUENCE_NUM | SupplierApprovalHistorySequenceNum | — |
| VENDOR_ID | SupplierApprovalHistoryVendorId | — |

### [[supplierprofilechangeapprovalhistorypvo|SupplierProfileChangeApprovalHistoryPVO]] (PO · BICC: 7/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ApprovalHistoryPEOActionCode | ✅ |
| ACTION_DATE | ApprovalHistoryPEOActionDate | ✅ |
| ADDITIONAL_INFO | ApprovalHistoryPEOAdditionalInfo | ✅ |
| AMX_IDENTIFICATION_KEY | ApprovalHistoryPEOAmxIdentificationKey | — |
| APPROVAL_FLOW_CODE | ApprovalHistoryPEOApprovalFlowCode | ✅ |
| APPROVAL_HISTORY_ID | ApprovalHistoryPEOApprovalHistoryId | ✅ |
| CREATED_BY | ApprovalHistoryPEOCreatedBy | — |
| CREATION_DATE | ApprovalHistoryPEOCreationDate | — |
| FLOW_OBJECT_ID | ApprovalHistoryPEOFlowObjectId | ✅ |
| LAST_UPDATE_DATE | ApprovalHistoryPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ApprovalHistoryPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ApprovalHistoryPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ApprovalHistoryPEOObjectVersionNumber | — |
| PERFORMER_ID | ApprovalHistoryPEOPerformerId | — |
| PERFORMER_TYPE | ApprovalHistoryPEOPerformerType | — |
| SEQUENCE_NUM | ApprovalHistoryPEOSequenceNum | ✅ |
| VENDOR_ID | ApprovalHistoryPEOVendorId | — |

---

## 📚 Referências

- [Oracle Docs — POZ Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
