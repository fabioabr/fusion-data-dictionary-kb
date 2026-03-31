---
id: DOC-HCM-090
doc_type: system-doc
title: "CMP_SALARY_HISTORY_V — Visão de Histórico Salarial"
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
  - historico-salarial
  - salary-history
  - view
aliases:
  - CMP_SALARY_HISTORY_V
  - cmp_salary_history_v
  - cmp-salary-history-v
  - DOC-HCM-090
  - visão-de-histórico-salarial
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_SALARY_HISTORY_V

## 📌 Visão Geral

**View** que apresenta o **histórico completo de salários** dos colaboradores, consolidando todas as alterações salariais ao longo do tempo com valores, datas, motivos e status.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Análise histórica:** Evolução salarial do colaborador ao longo do tempo.
- **Relatórios de progressão:** Trajetória de crescimento salarial.
- **Auditoria de remuneração:** Trilha completa de todas as alterações.
- **Benchmarking interno:** Comparação de progressão entre colaboradores.
- **Compliance trabalhista:** Documentação de alterações salariais para fins legais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador da pessoa | [[per_all_people_f]] | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟢 90% |
| 3 | SALARY_ID | NUMBER(18) | NULL | FK | Registro de salário | [[cmp_salary]] | 🟢 90% |
| 4 | SALARY_AMOUNT | NUMBER | NULL | Financeiro | Valor do salário | — | 🟢 90% |
| 5 | ANNUAL_SALARY | NUMBER | NULL | Financeiro | Salário anualizado | — | 🟡 80% |
| 6 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda | — | 🟢 90% |
| 7 | DATE_FROM | DATE | NULL | Data | Início de vigência | — | 🟢 90% |
| 8 | DATE_TO | DATE | NULL | Data | Fim de vigência | — | 🟢 90% |
| 9 | ACTION_CODE | VARCHAR2(30) | NULL | Classificação | Código da ação | — | 🟡 80% |
| 10 | CHANGE_PERCENT | NUMBER | NULL | Financeiro | Percentual de mudança | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do historico salarial)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio do historico salarial)
- [[cmp_salary]] — via `SALARY_ID` (registro salarial do historico)

### Tabelas-filha (FK de saída)
- Por ser uma view, não possui tabelas-filha diretas.

---

## 📎 Uso Típico

### Histórico salarial completo
```sql
SELECT sh.SALARY_AMOUNT, sh.ANNUAL_SALARY, sh.DATE_FROM,
       sh.DATE_TO, sh.ACTION_CODE, sh.CHANGE_PERCENT
FROM   CMP_SALARY_HISTORY_V sh
WHERE  sh.PERSON_ID = :p_person_id
ORDER BY sh.DATE_FROM DESC;
```

### Última alteração salarial
```sql
SELECT sh.SALARY_AMOUNT, sh.DATE_FROM, sh.ACTION_CODE
FROM   CMP_SALARY_HISTORY_V sh
WHERE  sh.PERSON_ID = :p_person_id
  AND  sh.DATE_TO IS NULL;
```

---

## 🔒 Observações

- Esta é uma **view** (sufixo `_V`), não uma tabela física.
- Consolida dados de `CMP_SALARY` com informações calculadas de variação.
- O `CHANGE_PERCENT` é calculado automaticamente com base no salário anterior.
- Ideal para relatórios de evolução salarial sem necessidade de self-join.

---

## 🔗 PVOs Relacionados

### [[salaryhistorypvo|SalaryHistoryPVO]] (HCM · BICC: 40/71)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | ActionId | — |
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | — |
| ACTION_REASON_ID | ActionReasonId | — |
| AMOUNT_DECIMAL_PRECISION | SbAmountDecimalPrecision | ✅ |
| AMOUNT_ROUNDING_CODE | SbAmountRoundingCode | ✅ |
| ANNUAL_ROUNDING_CODE | SbAnnualRoundingCode | ✅ |
| ANNUALIZED_FULLTIME_SALARY | AnnualizedFulltimeSalary | ✅ |
| ANNUALIZED_HOURS | AnnualizedHours | ✅ |
| ANNUALIZED_SALARY | AnnualizedSalary | ✅ |
| ASSIGNMENT_ID | AssignmentId | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_UNIT_ID | BusinessUnitId1 | — |
| CALCULATION_MODE | CalculationMode | ✅ |
| CODE | Code | ✅ |
| COMPONENT_USAGE | ComponentUsage | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DESCRIPTION | Description | — |
| ELEMENT_ENTRY_ID | ElementEntryId | — |
| ELEMENT_TYPE_ID | ElementTypeId | — |
| FORCED_RANKING | ForcedRanking | — |
| GEOGRAPHY_ID | GeographyId | ✅ |
| GEOGRAPHY_TYPE_ID | GeographyTypeId | ✅ |
| GRADE_ANNUALIZATION_FACTOR | GradeAnnualizationFactor | ✅ |
| GRADE_RATE_ID | GradeRateId | — |
| GRADE_RATE_MINIMUM_LIMIT | GradeRateMinimumLimit | — |
| HISTORY_DATE | HistoryDate | — |
| INPUT_VALUE_ID | InputValueId | — |
| INPUT_VALUE_LANGUAGE | InputValueLanguage | — |
| INPUT_VALUE_NAME | InputValueName | ✅ |
| JOB_ID | JobId1 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| MULTIPLE_COMPONENTS | MultipleComponents | ✅ |
| NEXT_PERF_REVIEW_DATE | NextPerfReviewDate | — |
| NEXT_SAL_REVIEW_DATE | NextSalReviewDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PAYROLL_ANNUAL_FACTOR | PayrollAnnualFactor | ✅ |
| PAYROLL_FREQUENCY_CODE | PayrollFrequencyCode | ✅ |
| PERFORMANCE_RATING | PerformanceRating | — |
| PERFORMANCE_REVIEW_ID | PerformanceReviewId | — |
| RANGE_ERROR_WARNING | RangeErrorWarning | — |
| RANGE_ROUNDING_CODE | SbRangeRoundingCode | ✅ |
| REVIEW_DATE | ReviewDate | — |
| SALARY_AMOUNT | SalaryAmount | ✅ |
| SALARY_ANNUALIZATION_FACTOR | SalaryAnnualizationFactor | ✅ |
| SALARY_APPROVED | SalaryApproved | ✅ |
| SALARY_BASES_NAME | SalaryBasesName | — |
| SALARY_BASIS_CODE | SalaryBasisCode | ✅ |
| SALARY_BASIS_CREATED_BY | SalaryBasisCreatedBy | ✅ |
| SALARY_BASIS_CREATION_DATE | SalaryBasisCreationDate | ✅ |
| SALARY_BASIS_ID | SalaryBasisId | ✅ |
| SALARY_BASIS_LAST_UPDATE_DATE | SalaryBasisLastUpdateDate | ✅ |
| SALARY_BASIS_LAST_UPDATED_BY | SalaryBasisLastUpdatedBy | ✅ |
| SALARY_BASIS_NAME | SalaryBasisName | ✅ |
| SALARY_BASIS_TYPE | SbSalaryBasisType | ✅ |
| SALARY_ID | SalaryId | ✅ |
| SALARY_REASON_CODE | SalaryReasonCode | — |
| SB_BUSINESS_GROUP_ID | SbBusinessGroupId | — |
| SB_LANGUAGE | SbLanguage | — |
| SB_SALARY_BASIS_ID | SbSalaryBasisId | — |
| SB_SOUCE_LANG | SbSouceLang | — |
| SOURCE_LANG | SourceLang | — |
| STATUS | SbStatus | ✅ |
| WORK_AT_HOME | WorkAtHome | ✅ |
| ZONE_GRADE_RATE_ID | ZoneGradeRateId | — |

---

## 📚 Referências

- [Oracle Docs — CMP_SALARY_HISTORY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpsalaryhistoryv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
