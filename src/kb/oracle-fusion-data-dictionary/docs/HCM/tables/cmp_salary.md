---
id: DOC-HCM-086
doc_type: system-doc
title: "CMP_SALARY — Salários de Compensação"
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
  - salario
  - salary
  - remuneracao
aliases:
  - CMP_SALARY
  - cmp_salary
  - cmp-salary
  - DOC-HCM-086
  - salários-de-compensação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_SALARY

## 📌 Visão Geral

Armazena os **registros de salário** dos colaboradores no módulo de Compensação. Cada registro representa uma proposta ou efetivação salarial, com valor, moeda, base salarial, data de efetividade e status de aprovação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão salarial:** Registro central de todos os salários do colaborador.
- **Histórico salarial:** Manutenção do histórico completo de alterações.
- **Aprovação de salários:** Workflow de aprovação de propostas salariais.
- **Integração com payroll:** Dados salariais enviados para processamento de folha.
- **Relatórios de compensação:** Base para análises de equidade e competitividade.
- **Auditoria:** Rastreamento completo de alterações salariais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SALARY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de salário | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | [[per_all_people_f]] | 🟢 95% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 95% |
| 4 | SALARY_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do salário | — | 🟢 95% |
| 5 | ANNUAL_SALARY | NUMBER | NULL | Financeiro | Salário anualizado | — | 🟢 90% |
| 6 | SALARY_BASIS_ID | NUMBER(18) | NULL | FK | Base salarial | [[cmp_salary_bases]] | 🟢 90% |
| 7 | CURRENCY_CODE | VARCHAR2(30) | NOT NULL | Referência | Moeda do salário | — | 🟢 95% |
| 8 | DATE_FROM | DATE | NOT NULL | Data | Data de início de vigência | — | 🟢 95% |
| 9 | DATE_TO | DATE | NULL | Data | Data de fim de vigência | — | 🟢 90% |
| 10 | ACTION_CODE | VARCHAR2(30) | NULL | Classificação | Código da ação (HIRE, PROMOTION, MERIT) | — | 🟡 80% |
| 11 | ACTION_REASON_CODE | VARCHAR2(30) | NULL | Classificação | Motivo da ação | — | 🟡 80% |
| 12 | STATUS | VARCHAR2(30) | NULL | Status | Status do salário (APPROVED, PENDING, REJECTED) | — | 🟡 80% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do registro salarial)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio do salario)
- [[cmp_salary_bases]] — via `SALARY_BASIS_ID` (base salarial do registro de salario)

### Tabelas-filha (FK de saída)
- [[cmp_salary_components]] — via `SALARY_ID` (componentes do salário)

---

## 📎 Uso Típico

### Salário atual do colaborador
```sql
SELECT s.SALARY_ID, s.SALARY_AMOUNT, s.ANNUAL_SALARY,
       s.CURRENCY_CODE, s.DATE_FROM
FROM   CMP_SALARY s
WHERE  s.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN s.DATE_FROM AND NVL(s.DATE_TO, TO_DATE('4712-12-31','YYYY-MM-DD'));
```

### Histórico de salários por assignment
```sql
SELECT s.SALARY_AMOUNT, s.DATE_FROM, s.DATE_TO,
       s.ACTION_CODE, s.STATUS
FROM   CMP_SALARY s
WHERE  s.ASSIGNMENT_ID = :p_assignment_id
ORDER BY s.DATE_FROM DESC;
```

---

## 🔒 Observações

- Tabela principal de salários no módulo Compensation — cada alteração gera um novo registro.
- O `ACTION_CODE` indica o motivo: HIRE (admissão), PROMOTION (promoção), MERIT (mérito), etc.
- O `ANNUAL_SALARY` é calculado com base no `SALARY_AMOUNT` e na periodicidade da `SALARY_BASIS`.
- Salários com `DATE_TO` nulo são os registros vigentes.
- Integra com payroll para cálculo de folha de pagamento.

---

## 🔗 PVOs Relacionados

### [[offersalarypvo|OfferSalaryPVO]] (HCM · BICC: 4/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | SalaryPEOActionId | — |
| ACTION_OCCURRENCE_ID | SalaryPEOActionOccurrenceId | — |
| ACTION_REASON_ID | SalaryPEOActionReasonId | — |
| ASSIGNMENT_ID | SalaryPEOAssignmentId | — |
| BUSINESS_GROUP_ID | SalaryPEOBusinessGroupId | — |
| CREATED_BY | SalaryPEOCreatedBy | — |
| CREATION_DATE | SalaryPEOCreationDate | — |
| DATE_FROM | SalaryEffectiveStartDate | — |
| DATE_FROM | SalaryPEODateFrom | — |
| DATE_TO | SalaryEffectiveEndDate | — |
| DATE_TO | SalaryPEODateTo | — |
| ELEMENT_ENTRY_ID | SalaryPEOElementEntryId | — |
| LAST_UPDATE_DATE | SalaryPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SalaryPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | SalaryPEOLastUpdatedBy | — |
| MULTIPLE_COMPONENTS | SalaryPEOMultipleComponents | ✅ |
| NEXT_SAL_REVIEW_DATE | SalaryPEONextSalReviewDate | — |
| OBJECT_VERSION_NUMBER | SalaryPEOObjectVersionNumber | — |
| SALARY_AMOUNT | SalaryPEOSalaryAmount | ✅ |
| SALARY_APPROVED | SalaryPEOSalaryApproved | — |
| SALARY_BASIS_ID | SalaryPEOSalaryBasisId | — |
| SALARY_ID | SalaryId | ✅ |

### [[salaryextractpvo|SalaryExtractPVO]] (HCM · BICC: 90/160)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | ActionId | ✅ |
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| ACTION_REASON_ID | ActionReasonId | ✅ |
| ADJUSTMENT_AMOUNT | AdjustmentAmount | ✅ |
| ADJUSTMENT_AMOUNT_SCALE | AdjustmentAmountScale | ✅ |
| ADJUSTMENT_PERCENT | AdjustmentPercent | ✅ |
| ADJUSTMENT_PERCENT_SCALE | AdjustmentPercentScale | ✅ |
| AMOUNT_ROUNDING_CODE | AmountRoundingCode | ✅ |
| ANNUAL_FT_SALARY | AnnualFtSalary | ✅ |
| ANNUAL_ROUNDING_CODE | AnnualRoundingCode | ✅ |
| ANNUAL_SALARY | AnnualSalary | ✅ |
| ASSIG_GRADE_LADDER_ID | AssigGradeLadderId | ✅ |
| ASSIG_GRADE_STEP_ID | AssigGradeStepId | ✅ |
| ASSIG_LOCATION_ID | AssigLocationId | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_TYPE | AssignmentType | ✅ |
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
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
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
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| COMPA_RATIO | CompaRatio | ✅ |
| COMPA_RATIO_SCALE | CompaRatioScale | ✅ |
| COMPONENT_USAGE | ComponentUsage | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENCY_CODE | CurrencyCode | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_FROM | SalaryEffectiveStartDate | ✅ |
| DATE_TO | DateTo | ✅ |
| DATE_TO | SalaryEffectiveEndDate | ✅ |
| DISABLE_COMPA_RATIO | DisableCompaRatio | ✅ |
| DISABLE_QUARTILE | DisableQuartile | ✅ |
| DISABLE_QUINTILE | DisableQuintile | ✅ |
| DISABLE_RANGE_POSITION | DisableRangePosition | ✅ |
| ELEMENT_ENTRY_ID | ElementEntryId | ✅ |
| ELEMENT_TYPE_ID | ElementTypeId | ✅ |
| ELEMENT_USAGE_LEVEL | ElementUsageLevel | ✅ |
| FORCED_RANKING | ForcedRanking | ✅ |
| FTE_IMPACT | FteImpact | ✅ |
| FTE_VALUE | FteValue | ✅ |
| GEOGRAPHY_ID | GeographyId | ✅ |
| GEOGRAPHY_TYPE_ID | GeographyTypeId | ✅ |
| GRADE_ID | GradeId | ✅ |
| GRADE_RATE_MINIMUM_LIMIT | GradeRateMinimumLimit | ✅ |
| INPUT_VALUE_ID | InputValueId | ✅ |
| JOB_ID | JobId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| MISC_COMMENT1 | MiscComment1 | — |
| MISC_COMMENT2 | MiscComment2 | — |
| MISC_COMMENT3 | MiscComment3 | — |
| MISC_COMMENT4 | MiscComment4 | — |
| MULTIPLE_COMPONENTS | MultipleComponents | ✅ |
| NEXT_PERF_REVIEW_DATE | NextPerfReviewDate | ✅ |
| NEXT_SAL_REVIEW_DATE | NextSalReviewDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PAYROLL_FACTOR | PayrollFactor | ✅ |
| PAYROLL_FREQUENCY_CODE | PayrollFrequencyCode | ✅ |
| PERFORMANCE_RATING | PerformanceRating | ✅ |
| PERFORMANCE_REVIEW_ID | PerformanceReviewId | ✅ |
| PERSON_ID | PersonId | ✅ |
| QUARTILE | Quartile | ✅ |
| QUINTILE | Quintile | ✅ |
| RANGE_ANALYTICS_FOR_EMP | RangeAnalyticsForEmp | ✅ |
| RANGE_ANALYTICS_FOR_MGR | RangeAnalyticsForMgr | ✅ |
| RANGE_ERROR_WARNING | RangeErrorWarning | ✅ |
| RANGE_POSITION | RangePosition | ✅ |
| RANGE_POSITION_SCALE | RangePositionScale | ✅ |
| RANGE_ROUNDING_CODE | RangeRoundingCode | ✅ |
| RATE_DEFAULT_AMOUNT | RateDefaultAmount | ✅ |
| RATE_FACTOR | RateFactor | ✅ |
| RATE_ID | RateId | ✅ |
| RATE_MAX_AMOUNT | RateMaxAmount | ✅ |
| RATE_MID_AMOUNT | RateMidAmount | ✅ |
| RATE_MIN_AMOUNT | RateMinAmount | ✅ |
| REVIEW_DATE | ReviewDate | ✅ |
| SALARY_AMOUNT | SalaryAmount | ✅ |
| SALARY_AMOUNT_SCALE | SalaryAmountScale | ✅ |
| SALARY_APPROVED | SalaryApproved | ✅ |
| SALARY_BASIS_CODE | SalaryBasisCode | ✅ |
| SALARY_BASIS_ID | SalaryBasisId | ✅ |
| SALARY_BASIS_TYPE | SalaryBasisType | ✅ |
| SALARY_FACTOR | SalaryFactor | ✅ |
| SALARY_ID | SalaryId | ✅ |
| SALARY_JUSTIFICATION | SalaryJustification | ✅ |
| SALARY_RANGE_SCALE | SalaryRangeScale | ✅ |
| SALARY_REASON_CODE | SalaryReasonCode | ✅ |
| SALARY_TRANSACTION_STATUS | SalaryTransactionStatus | ✅ |
| TOTAL_BASE_PAY | TotalBasePay | ✅ |
| TOTAL_COMPONENT_ADJ_AMT | TotalComponentAdjAmt | ✅ |
| TOTAL_COMPONENT_ADJ_PERCENT | TotalComponentAdjPercent | ✅ |
| WORK_AT_HOME | WorkAtHome | ✅ |
| ZONE_GRADE_RATE_ID | ZoneGradeRateId | ✅ |

### [[salarypvo|SalaryPVO]] (HCM · BICC: 19/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | SalaryPEOActionId | — |
| ACTION_OCCURRENCE_ID | SalaryPEOActionOccurrenceId | ✅ |
| ACTION_REASON_ID | SalaryPEOActionReasonId | — |
| ASSIGNMENT_ID | SalaryPEOAssignmentId | ✅ |
| BUSINESS_GROUP_ID | SalaryPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | SalaryPEOBusinessUnitId | — |
| CREATED_BY | SalaryPEOCreatedBy | ✅ |
| CREATION_DATE | SalaryPEOCreationDate | ✅ |
| DATE_FROM | SalaryEffectiveStartDate | — |
| DATE_FROM | SalaryPEODateFrom | ✅ |
| DATE_TO | SalaryEffectiveEndDate | — |
| DATE_TO | SalaryPEODateTo | ✅ |
| ELEMENT_ENTRY_ID | SalaryPEOElementEntryId | — |
| GEOGRAPHY_ID | SalaryPEOGeographyId | ✅ |
| GEOGRAPHY_TYPE_ID | SalaryPEOGeographyTypeId | ✅ |
| GRADE_RATE_MINIMUM_LIMIT | SalaryPEOGradeRateMinimumLimit | — |
| JOB_ID | SalaryPEOJobId | — |
| LAST_UPDATE_DATE | SalaryPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SalaryPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SalaryPEOLastUpdatedBy | ✅ |
| MULTIPLE_COMPONENTS | SalaryPEOMultipleComponents | ✅ |
| NEXT_SAL_REVIEW_DATE | SalaryPEONextSalReviewDate | ✅ |
| OBJECT_VERSION_NUMBER | SalaryPEOObjectVersionNumber | — |
| SALARY_AMOUNT | SalaryPEOSalaryAmount | ✅ |
| SALARY_APPROVED | SalaryPEOSalaryApproved | ✅ |
| SALARY_BASIS_ID | SalaryPEOSalaryBasisId | ✅ |
| SALARY_ID | SalaryId | ✅ |
| WORK_AT_HOME | SalaryPEOWorkAtHome | ✅ |
| ZONE_GRADE_RATE_ID | SalaryPEOZoneGradeRateId | — |

---

## 📚 Referências

- [Oracle Docs — CMP_SALARY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpsalary.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
