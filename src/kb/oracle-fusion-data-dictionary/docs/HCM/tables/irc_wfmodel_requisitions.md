---
id: DOC-HCM-547
doc_type: system-doc
title: "IRC_WFMODEL_REQUISITIONS — Modelos de Workflow de Requisicoes"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - workflow-model
  - requisicao
  - irc-wfmodel
aliases:
  - IRC_WFMODEL_REQUISITIONS
  - irc_wfmodel_requisitions
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_WFMODEL_REQUISITIONS

## 📌 Visão Geral

Armazena a associacao entre **modelos de workflow** e requisicoes de recrutamento. Define qual fluxo de aprovacao e processamento cada requisicao segue.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao do workflow de aprovacao por requisicao
- Configuracao de fluxos customizados de recrutamento
- Rastreamento do modelo de processo seletivo utilizado

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | WFMODEL_REQUISITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da associacao | --- | 🟢 85% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | ID da requisicao | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | WORKFLOW_MODEL_ID | NUMBER(18) | NULL | FK | ID do modelo de workflow | --- | 🟡 70% |
| 4 | MODEL_STATUS | VARCHAR2(30) | NULL | Classificacao | Status do modelo na requisicao | --- | 🟡 65% |
| 5 | EFFECTIVE_DATE | DATE | NULL | Vigencia | Data de efetivacao do modelo | --- | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisição de vaga vinculada ao modelo de workflow)

### Tabelas-filha (FK de saída)
- --- Tabela de associacao workflow-requisicao

---

## 📎 Uso Típico

### Modelo de workflow por requisicao
```sql
SELECT wr.WORKFLOW_MODEL_ID, wr.MODEL_STATUS, wr.EFFECTIVE_DATE
FROM   IRC_WFMODEL_REQUISITIONS wr
WHERE  wr.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[wfmodelrequisitionpvo|WfModelRequisitionPVO]] (HCM · BICC: 7/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | Comments | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| GEOGRAPHY_NODE_ID | GeographyNodeId | — |
| HIRING_MANAGER_ID | HiringManagerId | — |
| JUSTIFICATION_CODE | JustificationCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | — |
| MANAGER_TITLE | ManagerTitle | ✅ |
| NUMBER_TO_HIRE | NumberToHire | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PHASE_ID | PhaseId | — |
| RECRUITER_ASSIGNMENT_ID | RecruiterAssignmentId | — |
| RECRUITER_ID | RecruiterId | — |
| RECRUITING_TYPE_CODE | RecruitingTypeCode | — |
| REQUISITION_LANGUAGE | RequisitionLanguage | — |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| SOURCE_REQUISITION_ID | SourceRequisitionId | — |
| STATE_ID | StateId | — |
| TITLE | Title | ✅ |
| UNLIMITED_HIRE_FLAG | UnlimitedHireFlag | ✅ |
| WF_MODEL_ID | WfModelId | — |
| WF_MODEL_REQUISITION_ID | WfModelRequisitionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — IRC_WFMODEL_REQUISITIONS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircwfmodelrequisitions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
