---
id: DOC-HCM-085
doc_type: system-doc
title: "CMP_PROFILE_VALUES — Valores de Perfil de Compensação"
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
  - compensation
  - perfil
  - faixa-salarial
  - compa-ratio
aliases:
  - CMP_PROFILE_VALUES
  - cmp_profile_values
  - cmp-profile-values
  - DOC-HCM-085
  - valores-de-perfil-de-compensação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_PROFILE_VALUES

## 📌 Visão Geral

Armazena os **valores de perfil de compensação** associados a colaboradores ou posições. Contém dados de perfis como faixas salariais, targets de bônus, comps ratios e outros indicadores de compensação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Perfis de compensação:** Valores-alvo e faixas por cargo/nível.
- **Compa-ratio:** Cálculo de posicionamento salarial do colaborador.
- **Faixas salariais:** Mínimo, médio e máximo por grade/posição.
- **Targets de bônus:** Percentuais-alvo de bonificação por perfil.
- **Benchmarking:** Comparação com dados de mercado por perfil.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do valor de perfil | — | 🟢 90% |
| 2 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de compensação | — | 🟡 80% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada | [[per_all_people_f]] | 🟡 75% |
| 4 | GRADE_ID | NUMBER(18) | NULL | FK | Grade/nível | [[per_grades_f]] | 🟡 75% |
| 5 | VALUE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do valor (MINIMUM, MIDPOINT, MAXIMUM, TARGET) | — | 🟡 75% |
| 6 | NUMERIC_VALUE | NUMBER | NULL | Financeiro | Valor numérico do perfil | — | 🟡 80% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda do valor | — | 🟢 90% |
| 8 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início de vigência | — | 🟡 80% |
| 9 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigência | — | 🟡 80% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do perfil de compensacao)
- [[per_grades_f]] — via `GRADE_ID` (grade do perfil de compensacao)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Faixa salarial por grade
```sql
SELECT pv.GRADE_ID, pv.VALUE_TYPE, pv.NUMERIC_VALUE, pv.CURRENCY_CODE
FROM   CMP_PROFILE_VALUES pv
WHERE  pv.GRADE_ID = :p_grade_id
  AND  pv.VALUE_TYPE IN ('MINIMUM', 'MIDPOINT', 'MAXIMUM');
```

### Perfis ativos por pessoa
```sql
SELECT pv.PERSON_ID, pv.VALUE_TYPE, pv.NUMERIC_VALUE
FROM   CMP_PROFILE_VALUES pv
WHERE  pv.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN pv.EFFECTIVE_START_DATE AND pv.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- O `VALUE_TYPE` define o significado: MINIMUM (piso), MIDPOINT (referência), MAXIMUM (teto), TARGET (meta).
- Compa-ratio = Salário Atual / MIDPOINT — mede posicionamento na faixa.
- Perfis podem ser vinculados a pessoas individuais ou a grades/posições.
- Tabela central para políticas de remuneração e equidade interna.

---

## 🔗 PVOs Relacionados

### [[stockdetailspvo|StockDetailsPVO]] (HCM · BICC: 2/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CompProfileEOBusinessGroupId1 | — |
| CREATED_BY | CompProfileEOCreatedBy1 | — |
| CREATION_DATE | CompProfileEOCreationDate1 | — |
| ENABLE_MODELING_FLAG | CompProfileEOEnableModelingFlag | — |
| EST_STOCK_PRICE | CompProfileEOEstStockPrice | ✅ |
| EST_STOCK_PRICE_CURRENCY_CD | CompProfileEOEstStockPriceCurrencyCd | — |
| LAST_UPDATE_DATE | CompProfileEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | CompProfileEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | CompProfileEOLastUpdatedBy1 | — |
| MAX_STATEMENT_PERIODS | CompProfileEOMaxStatementPeriods | — |
| MAX_SWITCH_MANAGERS | CompProfileEOMaxSwitchManagers | — |
| NOTIFY_BUDGET_PUBLISH | CompProfileEONotifyBudgetPublish | — |
| NOTIFY_CHANGE_ACCESS | CompProfileEONotifyChangeAccess | — |
| NOTIFY_CHANGE_ELIG | CompProfileEONotifyChangeElig | — |
| NOTIFY_FINAL_APPROVAL | CompProfileEONotifyFinalApproval | — |
| NOTIFY_MANAGER_APPROVAL | CompProfileEONotifyManagerApproval | — |
| NOTIFY_MANAGER_OVERRIDE | CompProfileEONotifyManagerOverride | — |
| NOTIFY_REASSIGN | CompProfileEONotifyReassign | — |
| NOTIFY_WORK_RECALL | CompProfileEONotifyWorkRecall | — |
| NOTIFY_WORK_REJECT | CompProfileEONotifyWorkReject | — |
| NOTIFY_WORK_SUBMIT | CompProfileEONotifyWorkSubmit | — |
| OBJECT_VERSION_NUMBER | CompProfileEOObjectVersionNumber1 | — |
| WATCH_BUDGET_PUBLISH_DAYS | CompProfileEOWatchBudgetPublishDays | — |
| WATCH_BUDGET_PUBLISH_FLAG | CompProfileEOWatchBudgetPublishFlag | — |
| WATCH_NEW_PLANS_DAYS | CompProfileEOWatchNewPlansDays | — |
| WATCH_NEW_PLANS_FLAG | CompProfileEOWatchNewPlansFlag | — |
| WATCH_NUM_PLANS_FLAG | CompProfileEOWatchNumPlansFlag | — |
| WATCH_NUM_POOLS_FLAG | CompProfileEOWatchNumPoolsFlag | — |
| WATCH_STATEMENT_DAYS | CompProfileEOWatchStatementDays | — |
| WATCH_STATEMENT_FLAG | CompProfileEOWatchStatementFlag | — |

---

## 📚 Referências

- [Oracle Docs — CMP_PROFILE_VALUES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpprofilevalues.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
