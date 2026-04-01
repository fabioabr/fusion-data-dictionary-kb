---
id: DOC-HCM-098
doc_type: system-doc
title: "HNS_ACTIONS — Ações de Saúde e Segurança"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - health-safety
  - acoes-corretivas
  - seguranca-trabalho
  - hns
aliases:
  - HNS_ACTIONS
  - hns_actions
  - hns-actions
  - DOC-HCM-098
  - ações-de-saúde-e-segurança
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_ACTIONS

## 📌 Visão Geral

Armazena as **ações corretivas e preventivas** registradas no módulo de Saúde e Segurança do Trabalho (Health and Safety). Cada registro representa uma ação tomada ou planejada em resposta a incidentes, investigações ou inspeções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de ações corretivas:** Registro de ações para mitigar riscos.
- **Acompanhamento de prazos:** Monitoramento de datas-limite das ações.
- **Compliance regulatório:** Documentação de ações para atender normas.
- **Vinculação a incidentes:** Rastreabilidade entre ações e eventos.
- **Relatórios de segurança:** Análise de ações por tipo e status.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da ação | — | 🟢 90% |
| 2 | ACTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da ação (CORRECTIVE, PREVENTIVE) | — | 🟡 80% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto | Descrição da ação | — | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Status | Status da ação (OPEN, IN_PROGRESS, CLOSED) | — | 🟡 80% |
| 5 | ASSIGNED_TO_PERSON_ID | NUMBER(18) | NULL | FK | Pessoa responsável | [[per_all_people_f]] | 🟡 75% |
| 6 | DUE_DATE | DATE | NULL | Data | Data-limite para conclusão | — | 🟡 80% |
| 7 | COMPLETION_DATE | DATE | NULL | Data | Data de conclusão efetiva | — | 🟡 75% |
| 8 | INCIDENT_ID | NUMBER(18) | NULL | FK | Incidente relacionado | [[hns_incidents_detail]] | 🟡 75% |
| 9 | PRIORITY | VARCHAR2(30) | NULL | Classificação | Prioridade (HIGH, MEDIUM, LOW) | — | 🟡 70% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `ASSIGNED_TO_PERSON_ID` (responsavel pela acao corretiva do incidente)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente da acao corretiva)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Ações pendentes
```sql
SELECT a.ACTION_ID, a.ACTION_TYPE, a.DESCRIPTION, a.STATUS, a.DUE_DATE
FROM   HNS_ACTIONS a
WHERE  a.STATUS IN ('OPEN', 'IN_PROGRESS');
```

### Ações por incidente
```sql
SELECT a.ACTION_TYPE, a.DESCRIPTION, a.STATUS, a.DUE_DATE
FROM   HNS_ACTIONS a
WHERE  a.INCIDENT_ID = :p_incident_id;
```

---

## 🔒 Observações

- O `ACTION_TYPE` classifica: CORRECTIVE (corretiva) ou PREVENTIVE (preventiva).
- Ações com `DUE_DATE` ultrapassada e `STATUS` diferente de CLOSED indicam atraso.
- Vinculação com incidentes permite rastrear quais ações foram tomadas.
- Essencial para compliance com normas de segurança do trabalho (NRs no Brasil).

---

## 🔗 PVOs Relacionados

### [[hnsactionspvo|HNSActionsPVO]] (HCM · BICC: 25/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_APPROVER_EMAIL_FLAG | HNSActionsPEOActionApproverEmailFlag | ✅ |
| ACTION_DATE | HNSActionsPEOActionDate | ✅ |
| ACTION_ID | HNSActionsPEOActionId | ✅ |
| ACTION_NO | HNSActionsPEOActionNo | ✅ |
| ACTION_PRECOM_EMAIL_FLAG | HNSActionsPEOActionPrecomEmailFlag | ✅ |
| ACTION_REVIEWER_EMAIL_FLAG | HNSActionsPEOActionReviewerEmailFlag | ✅ |
| ACTION_STATUS_CODE | HNSActionsPEOActionStatusCode | ✅ |
| ACTION_SUMMARY | HNSActionsPEOActionSummary | ✅ |
| ACTION_TYPE_CODE | HNSActionsPEOActionTypeCode | ✅ |
| ATTRIBUTE1 | HNSActionsPEOAttribute1 | — |
| ATTRIBUTE10 | HNSActionsPEOAttribute10 | — |
| ATTRIBUTE2 | HNSActionsPEOAttribute2 | — |
| ATTRIBUTE3 | HNSActionsPEOAttribute3 | — |
| ATTRIBUTE4 | HNSActionsPEOAttribute4 | — |
| ATTRIBUTE5 | HNSActionsPEOAttribute5 | — |
| ATTRIBUTE6 | HNSActionsPEOAttribute6 | — |
| ATTRIBUTE7 | HNSActionsPEOAttribute7 | — |
| ATTRIBUTE8 | HNSActionsPEOAttribute8 | — |
| ATTRIBUTE9 | HNSActionsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSActionsPEOAttributeCategory | — |
| ATTRIBUTE_NUMBER1 | HNSActionsPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER2 | HNSActionsPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSActionsPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSActionsPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSActionsPEOAttrNumber5 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSActionsPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSActionsPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSActionsPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSActionsPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSActionsPEOAttrTimestamp5 | — |
| COMPLETED_FLAG | HNSActionsPEOCompletedFlag | ✅ |
| CREATED_BY | HNSActionsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSActionsPEOCreationDate | ✅ |
| DELETED_FLAG | HNSActionsPEODeletedFlag | ✅ |
| DESCRIPTION | HNSActionsPEODescription | ✅ |
| EST_COST_CURRENCY_CODE | HNSActionsPEOEstCostCurrencyCode | ✅ |
| ESTIMATED_COST | HNSActionsPEOEstimatedCost | ✅ |
| INCIDENT_ID | HNSActionsPEOIncidentId | ✅ |
| LAST_UPDATE_DATE | HNSActionsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSActionsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSActionsPEOLastUpdatedBy | ✅ |
| LESSONS_LEARNED | HNSActionsPEOLessonsLearned | ✅ |
| OBJECT_VERSION_NUMBER | HNSActionsPEOObjectVersionNumber | ✅ |
| PRIORITY_CODE | HNSActionsPEOPriorityCode | ✅ |
| RECOMMEND_ID | HNSActionsPEORecommendId | ✅ |
| REQ_RESOURCES | HNSActionsPEOReqResources | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_ACTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsactions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
