---
id: DOC-HCM-108
doc_type: system-doc
title: "HNS_INVESTIGATIONS_SUMMARY — Resumo de Investigações de Incidentes"
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
  - investigacoes
  - causa-raiz
  - hns
aliases:
  - HNS_INVESTIGATIONS_SUMMARY
  - hns_investigations_summary
  - hns-investigations-summary
  - DOC-HCM-108
  - resumo-de-investigações-de-incidentes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INVESTIGATIONS_SUMMARY

## 📌 Visão Geral

Armazena o **resumo das investigações** conduzidas para incidentes de saúde e segurança, incluindo status, responsável, datas e conclusões.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de investigações:** Registro de processos de investigação.
- **Análise de causa raiz:** Documentação de conclusões e causas.
- **Acompanhamento:** Status e prazos das investigações.
- **Compliance:** Documentação para auditorias regulatórias.
- **Relatórios:** Análise de investigações por status e resultado.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVESTIGATION_SUMMARY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | INCIDENT_ID | NUMBER(18) | NOT NULL | FK | Incidente investigado | [[hns_incidents_detail]] | 🟢 90% |
| 3 | INVESTIGATOR_PERSON_ID | NUMBER(18) | NULL | FK | Investigador responsável | [[per_all_people_f]] | 🟡 80% |
| 4 | INVESTIGATION_DATE | DATE | NULL | Data | Data de início da investigação | — | 🟡 80% |
| 5 | COMPLETION_DATE | DATE | NULL | Data | Data de conclusão | — | 🟡 75% |
| 6 | STATUS | VARCHAR2(30) | NULL | Status | Status (IN_PROGRESS, COMPLETED, PENDING) | — | 🟡 80% |
| 7 | ROOT_CAUSE | VARCHAR2(4000) | NULL | Texto | Causa raiz identificada | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_incidents_detail]] — via `INCIDENT_ID` (incidente investigado)
- [[per_all_people_f]] — via `INVESTIGATOR_PERSON_ID` (investigador do incidente)

### Tabelas-filha (FK de saída)
- [[hns_invest_findings]] — via `INVESTIGATION_SUMMARY_ID` (achados da investigacao)
- [[hns_invest_recommends]] — via `INVESTIGATION_SUMMARY_ID` (recomendacoes da investigacao)

---

## 📎 Uso Típico

### Investigações em andamento
```sql
SELECT s.INCIDENT_ID, s.INVESTIGATOR_PERSON_ID,
       s.INVESTIGATION_DATE, s.STATUS
FROM   HNS_INVESTIGATIONS_SUMMARY s
WHERE  s.STATUS = 'IN_PROGRESS';
```

### Causas raiz identificadas
```sql
SELECT s.INCIDENT_ID, s.ROOT_CAUSE, s.COMPLETION_DATE
FROM   HNS_INVESTIGATIONS_SUMMARY s
WHERE  s.STATUS = 'COMPLETED'
  AND  s.ROOT_CAUSE IS NOT NULL;
```

---

## 🔒 Observações

- Cada incidente pode ter uma ou mais investigações.
- O campo `ROOT_CAUSE` é preenchido ao final da investigação.
- Investigações COMPLETED devem gerar achados e recomendações.
- Integra com `HNS_INVEST_FINDINGS` e `HNS_INVEST_RECOMMENDS`.

---

## 🔗 PVOs Relacionados

### [[hnsinvestigationpvo|HNSInvestigationPVO]] (HCM · BICC: 33/55)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_REQUIRED_FLAG | HNSInvestigationsSummaryPEOActionRequirdFlag | ✅ |
| ACTUAL_COMPLETION_DATE | HNSInvestigationsSummaryPEOActComDate | ✅ |
| ATTRIBUTE1 | HNSInvestigationsSummaryPEOAttribute1 | — |
| ATTRIBUTE10 | HNSInvestigationsSummaryPEOAttribute10 | — |
| ATTRIBUTE2 | HNSInvestigationsSummaryPEOAttribute2 | — |
| ATTRIBUTE3 | HNSInvestigationsSummaryPEOAttribute3 | — |
| ATTRIBUTE4 | HNSInvestigationsSummaryPEOAttribute4 | — |
| ATTRIBUTE5 | HNSInvestigationsSummaryPEOAttribute5 | — |
| ATTRIBUTE6 | HNSInvestigationsSummaryPEOAttribute6 | — |
| ATTRIBUTE7 | HNSInvestigationsSummaryPEOAttribute7 | — |
| ATTRIBUTE8 | HNSInvestigationsSummaryPEOAttribute8 | — |
| ATTRIBUTE9 | HNSInvestigationsSummaryPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | HNSInvestigationsSummaryPEOAttrCategory | — |
| ATTRIBUTE_NUMBER1 | HNSInvestigationsSummaryPEOAttrNumber1 | — |
| ATTRIBUTE_NUMBER2 | HNSInvestigationsSummaryPEOAttrNumber2 | — |
| ATTRIBUTE_NUMBER3 | HNSInvestigationsSummaryPEOAttrNumber3 | — |
| ATTRIBUTE_NUMBER4 | HNSInvestigationsSummaryPEOAttrNumber4 | — |
| ATTRIBUTE_NUMBER5 | HNSInvestigationsSummaryPEOAttrNumber5 | — |
| ATTRIBUTE_TIMESTAMP1 | HNSInvestigationsSummaryPEOAttrTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP2 | HNSInvestigationsSummaryPEOAttrTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | HNSInvestigationsSummaryPEOAttrTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | HNSInvestigationsSummaryPEOAttrTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | HNSInvestigationsSummaryPEOAttrTimestamp5 | — |
| CASUAL_FACTORS_CODE | HNSInvestigationsSummaryPEOCslFctCd | ✅ |
| COMPLETED_FLAG | HNSInvestigationsSummaryPEOCompletedFlag | ✅ |
| CONTRIBUTING_FACTORS_CODE | HNSInvestigationsSummaryPEOContFctCd | ✅ |
| CREATED_BY | HNSInvestigationsSummaryPEOCreatedBy | ✅ |
| CREATION_DATE | HNSInvestigationsSummaryPEOCreationDate | ✅ |
| DELETED_FLAG | HNSInvestigationsSummaryPEODeletedFlag | ✅ |
| FINDING_COMMENT | HNSInvestigationsSummaryPEOFindingComnt | ✅ |
| FINDING_FINAL_RESPONSE | HNSInvestigationsSummaryPEOFindFinalResp | ✅ |
| IMMEDIATE_CAUSE_CODE | HNSInvestigationsSummaryPEOImdtCseCd | ✅ |
| INCIDENT_DETAIL_ID | HNSInvestigationsSummaryPEOIncdntDetId | ✅ |
| INCIDENT_ID | HNSInvestigationsSummaryPEOIncidentId | ✅ |
| INVEST_APPROVER_EMAIL_FLAG | HNSInvestigationsSummaryPEOInvAprEmlFlg | ✅ |
| INVEST_OWNER_ASSIGN_ID | HNSInvestigationsSummaryPEOInvOwnAsnId | — |
| INVEST_PRECOM_EMAIL_FLAG | HNSInvestigationsSummaryPEOInvPreEmlFlg | ✅ |
| INVEST_REVIEWER_EMAIL_FLAG | HNSInvestigationsSummaryPEOInvRevEmlFlg | ✅ |
| INVEST_STATUS_CODE | HNSInvestigationsSummaryPEOInvestStatCd | ✅ |
| INVESTIGATE_DATE | HNSInvestigationsSummaryPEOInvestigateDt | ✅ |
| INVESTIGATE_DESCRIPTION | HNSInvestigationsSummaryPEOInvestigateDescr | ✅ |
| INVESTIGATE_ID | HNSInvestigationsSummaryPEOInvestigateId | ✅ |
| INVESTIGATE_NO | HNSInvestigationsSummaryPEOInvestigateNo | ✅ |
| INVESTIGATE_OWNER_ID | HNSInvestigationsSummaryPEOInvestOwnerId | ✅ |
| INVESTIGATE_SUMMARY | HNSInvestigationsSummaryPEOInvSummary | ✅ |
| INVESTIGATE_TYPE_CODE | HNSInvestigationsSummaryPEOInvTypeCode | ✅ |
| LAST_UPDATE_DATE | HNSInvestigationsSummaryPEOLastUpdateDt | ✅ |
| LAST_UPDATE_LOGIN | HNSInvestigationsSummaryPEOLastUpdtLog | ✅ |
| LAST_UPDATED_BY | HNSInvestigationsSummaryPEOLastUpdatedBy | ✅ |
| LESSONS_LEARNED | HNSInvestigationsSummaryPEOLsnsLearned | ✅ |
| OBJECT_VERSION_NUMBER | HNSInvestigationsSummaryPEOObjVerNum | ✅ |
| QUESTIONNAIRE_ID | HNSInvestigationsSummaryPEOQuestionId | ✅ |
| ROOT_CAUSE_CODE | HNSInvestigationsSummaryPEORtCseCd | ✅ |
| TARGET_COMPLETION_DATE | HNSInvestigationsSummaryPEOTarCompDate | ✅ |
| UNDERLYING_FACTORS_CODE | HNSInvestigationsSummaryPEOUndFctCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_INVESTIGATIONS_SUMMARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinvestigationssummary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
