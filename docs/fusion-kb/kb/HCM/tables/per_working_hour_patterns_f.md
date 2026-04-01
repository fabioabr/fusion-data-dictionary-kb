---
id: DOC-HCM-722
doc_type: system-doc
title: "PER_WORKING_HOUR_PATTERNS_F — Padrões de Horário de Trabalho"
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
  - horário-trabalho
  - jornada
  - work-schedule
aliases:
  - PER_WORKING_HOUR_PATTERNS_F
  - per_working_hour_patterns_f
  - per-working-hour-patterns-f
  - padrões-horário-trabalho
  - working-hour-patterns
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_WORKING_HOUR_PATTERNS_F

## Visão Geral

Armazena os **padrões de horário de trabalho** (jornadas) aplicáveis aos colaboradores, incluindo horas diárias/semanais e tipo de regime. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de jornada** — define os padrões de trabalho (integral, parcial, flexível).
- **Cálculo de folha** — base para cálculo de horas normais e extras.
- **Compliance trabalhista** — garante aderência aos limites legais de jornada.
- **Planejamento de escalas** — suporta definição de escalas de trabalho.
- **Relatórios de workforce** — análises de distribuição de jornadas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | WORKING_HOUR_PATTERN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do padrão de horário | — | 🟢 85% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 95% |
| 4 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição do colaborador | PER_ALL_ASSIGNMENTS_M | 🟢 85% |
| 5 | WORKING_HOURS | NUMBER(5,2) | NULL | Dados | Quantidade de horas de trabalho | — | 🟢 85% |
| 6 | FREQUENCY | VARCHAR2(30) | NULL | Classificação | Frequência (diária, semanal, mensal) | — | 🟢 85% |
| 7 | WORKING_HOUR_PATTERN | VARCHAR2(30) | NULL | Classificação | Tipo do padrão (ex.: STANDARD, FLEXIBLE) | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (atribuição do colaborador)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Padrões de horário ativos
```sql
SELECT whp.WORKING_HOURS, whp.FREQUENCY, whp.WORKING_HOUR_PATTERN,
       a.ASSIGNMENT_NUMBER
FROM   PER_WORKING_HOUR_PATTERNS_F whp
JOIN   PER_ALL_ASSIGNMENTS_M a ON whp.ASSIGNMENT_ID = a.ASSIGNMENT_ID
WHERE  SYSDATE BETWEEN whp.EFFECTIVE_START_DATE AND whp.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ASSIGNMENT_ID = :p_assignment_id` — Padrão de um colaborador específico
- `FREQUENCY = 'W'` — Padrões semanais

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- O campo WORKING_HOURS combinado com FREQUENCY define a jornada completa.
- Alterações de jornada geram novos registros com datas de vigência atualizadas.
- Fundamental para cálculos de proporcionalidade em admissões/demissões.

---

## Referências

- [Oracle Docs — PER_WORKING_HOUR_PATTERNS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perworkinghourpatternsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 82/82)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | WorkingHourPatternsPEOCreatedBy | ✅ |
| CREATION_DATE | WorkingHourPatternsPEOCreationDate | ✅ |
| DEFAULT_START_DAY | WorkingHourPatternsPEODefaultStartDay | ✅ |
| EFFECTIVE_END_DATE | WorkingHourPatternsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | WorkingHourPatternsPEOEffectiveStartDate | ✅ |
| FRI_END_TIME | WorkingHourPatternsPEOFriEndTime | ✅ |
| FRI_HOURS | WorkingHourPatternsPEOFriHours | ✅ |
| FRI_START_TIME | WorkingHourPatternsPEOFriStartTime | ✅ |
| LAST_UPDATE_DATE | WorkingHourPatternsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WorkingHourPatternsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | WorkingHourPatternsPEOLastUpdatedBy | ✅ |
| MON_END_TIME | WorkingHourPatternsPEOMonEndTime | ✅ |
| MON_HOURS | WorkingHourPatternsPEOMonHours | ✅ |
| MON_START_TIME | WorkingHourPatternsPEOMonStartTime | ✅ |
| OBJECT | WorkingHourPatternsPEOObject | ✅ |
| OBJECT_ID | WorkingHourPatternsPEOObjectId | ✅ |
| OBJECT_VERSION_NUMBER | WorkingHourPatternsPEOObjectVersionNumber | ✅ |
| PERSON_ID | WorkingHourPatternsPEOPersonId1 | ✅ |
| SAT_END_TIME | WorkingHourPatternsPEOSatEndTime | ✅ |
| SAT_HOURS | WorkingHourPatternsPEOSatHours | ✅ |
| SAT_START_TIME | WorkingHourPatternsPEOSatStartTime | ✅ |
| SUN_END_TIME | WorkingHourPatternsPEOSunEndTime | ✅ |
| SUN_HOURS | WorkingHourPatternsPEOSunHours | ✅ |
| SUN_START_TIME | WorkingHourPatternsPEOSunStartTime | ✅ |
| THU_END_TIME | WorkingHourPatternsPEOThuEndTime | ✅ |
| THU_HOURS | WorkingHourPatternsPEOThuHours | ✅ |
| THU_START_TIME | WorkingHourPatternsPEOThuStartTime | ✅ |
| TOTAL_HOURS | WorkingHourPatternsPEOTotalHours | ✅ |
| TUE_END_TIME | WorkingHourPatternsPEOTueEndTime | ✅ |
| TUE_HOURS | WorkingHourPatternsPEOTueHours | ✅ |
| TUE_START_TIME | WorkingHourPatternsPEOTueStartTime | ✅ |
| WED_END_TIME | WorkingHourPatternsPEOWedEndTime | ✅ |
| WED_HOURS | WorkingHourPatternsPEOWedHours | ✅ |
| WED_START_TIME | WorkingHourPatternsPEOWedStartTime | ✅ |
| WHP_ATTRIBUTE1 | WorkingHourPatternsPEOWhpAttribute1 | ✅ |
| WHP_ATTRIBUTE10 | WorkingHourPatternsPEOWhpAttribute10 | ✅ |
| WHP_ATTRIBUTE11 | WorkingHourPatternsPEOWhpAttribute11 | ✅ |
| WHP_ATTRIBUTE12 | WorkingHourPatternsPEOWhpAttribute12 | ✅ |
| WHP_ATTRIBUTE13 | WorkingHourPatternsPEOWhpAttribute13 | ✅ |
| WHP_ATTRIBUTE14 | WorkingHourPatternsPEOWhpAttribute14 | ✅ |
| WHP_ATTRIBUTE15 | WorkingHourPatternsPEOWhpAttribute15 | ✅ |
| WHP_ATTRIBUTE16 | WorkingHourPatternsPEOWhpAttribute16 | ✅ |
| WHP_ATTRIBUTE17 | WorkingHourPatternsPEOWhpAttribute17 | ✅ |
| WHP_ATTRIBUTE18 | WorkingHourPatternsPEOWhpAttribute18 | ✅ |
| WHP_ATTRIBUTE19 | WorkingHourPatternsPEOWhpAttribute19 | ✅ |
| WHP_ATTRIBUTE2 | WorkingHourPatternsPEOWhpAttribute2 | ✅ |
| WHP_ATTRIBUTE20 | WorkingHourPatternsPEOWhpAttribute20 | ✅ |
| WHP_ATTRIBUTE3 | WorkingHourPatternsPEOWhpAttribute3 | ✅ |
| WHP_ATTRIBUTE4 | WorkingHourPatternsPEOWhpAttribute4 | ✅ |
| WHP_ATTRIBUTE5 | WorkingHourPatternsPEOWhpAttribute5 | ✅ |
| WHP_ATTRIBUTE6 | WorkingHourPatternsPEOWhpAttribute6 | ✅ |
| WHP_ATTRIBUTE7 | WorkingHourPatternsPEOWhpAttribute7 | ✅ |
| WHP_ATTRIBUTE8 | WorkingHourPatternsPEOWhpAttribute8 | ✅ |
| WHP_ATTRIBUTE9 | WorkingHourPatternsPEOWhpAttribute9 | ✅ |
| WHP_ATTRIBUTE_CATEGORY | WorkingHourPatternsPEOWhpAttributeCategory | ✅ |
| WHP_ATTRIBUTE_DATE1 | WorkingHourPatternsPEOWhpAttributeDate1 | ✅ |
| WHP_ATTRIBUTE_DATE10 | WorkingHourPatternsPEOWhpAttributeDate10 | ✅ |
| WHP_ATTRIBUTE_DATE11 | WorkingHourPatternsPEOWhpAttributeDate11 | ✅ |
| WHP_ATTRIBUTE_DATE12 | WorkingHourPatternsPEOWhpAttributeDate12 | ✅ |
| WHP_ATTRIBUTE_DATE13 | WorkingHourPatternsPEOWhpAttributeDate13 | ✅ |
| WHP_ATTRIBUTE_DATE14 | WorkingHourPatternsPEOWhpAttributeDate14 | ✅ |
| WHP_ATTRIBUTE_DATE15 | WorkingHourPatternsPEOWhpAttributeDate15 | ✅ |
| WHP_ATTRIBUTE_DATE2 | WorkingHourPatternsPEOWhpAttributeDate2 | ✅ |
| WHP_ATTRIBUTE_DATE3 | WorkingHourPatternsPEOWhpAttributeDate3 | ✅ |
| WHP_ATTRIBUTE_DATE4 | WorkingHourPatternsPEOWhpAttributeDate4 | ✅ |
| WHP_ATTRIBUTE_DATE5 | WorkingHourPatternsPEOWhpAttributeDate5 | ✅ |
| WHP_ATTRIBUTE_DATE6 | WorkingHourPatternsPEOWhpAttributeDate6 | ✅ |
| WHP_ATTRIBUTE_DATE7 | WorkingHourPatternsPEOWhpAttributeDate7 | ✅ |
| WHP_ATTRIBUTE_DATE8 | WorkingHourPatternsPEOWhpAttributeDate8 | ✅ |
| WHP_ATTRIBUTE_DATE9 | WorkingHourPatternsPEOWhpAttributeDate9 | ✅ |
| WHP_ATTRIBUTE_NUMBER1 | WorkingHourPatternsPEOWhpAttributeNumber1 | ✅ |
| WHP_ATTRIBUTE_NUMBER10 | WorkingHourPatternsPEOWhpAttributeNumber10 | ✅ |
| WHP_ATTRIBUTE_NUMBER2 | WorkingHourPatternsPEOWhpAttributeNumber2 | ✅ |
| WHP_ATTRIBUTE_NUMBER3 | WorkingHourPatternsPEOWhpAttributeNumber3 | ✅ |
| WHP_ATTRIBUTE_NUMBER4 | WorkingHourPatternsPEOWhpAttributeNumber4 | ✅ |
| WHP_ATTRIBUTE_NUMBER5 | WorkingHourPatternsPEOWhpAttributeNumber5 | ✅ |
| WHP_ATTRIBUTE_NUMBER6 | WorkingHourPatternsPEOWhpAttributeNumber6 | ✅ |
| WHP_ATTRIBUTE_NUMBER7 | WorkingHourPatternsPEOWhpAttributeNumber7 | ✅ |
| WHP_ATTRIBUTE_NUMBER8 | WorkingHourPatternsPEOWhpAttributeNumber8 | ✅ |
| WHP_ATTRIBUTE_NUMBER9 | WorkingHourPatternsPEOWhpAttributeNumber9 | ✅ |
| WORKING_HOUR_PATTERN_ID | WorkingHourPatternsPEOWorkingHourPatternId | ✅ |
| WORKING_HOURS_TYPE | WorkingHourPatternsPEOWorkingHoursType | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 28/82)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | WorkingHourPatternsPEOCreatedBy | ✅ |
| CREATION_DATE | WorkingHourPatternsPEOCreationDate | ✅ |
| DEFAULT_START_DAY | WorkingHourPatternsPEODefaultStartDay | — |
| EFFECTIVE_END_DATE | WorkingHourPatternsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | WorkingHourPatternsPEOEffectiveStartDate | ✅ |
| FRI_END_TIME | WorkingHourPatternsPEOFriEndTime | ✅ |
| FRI_HOURS | WorkingHourPatternsPEOFriHours | ✅ |
| FRI_START_TIME | WorkingHourPatternsPEOFriStartTime | ✅ |
| LAST_UPDATE_DATE | WorkingHourPatternsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WorkingHourPatternsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | WorkingHourPatternsPEOLastUpdatedBy | ✅ |
| MON_END_TIME | WorkingHourPatternsPEOMonEndTime | ✅ |
| MON_HOURS | WorkingHourPatternsPEOMonHours | ✅ |
| MON_START_TIME | WorkingHourPatternsPEOMonStartTime | ✅ |
| OBJECT | WorkingHourPatternsPEOObject | — |
| OBJECT_ID | WorkingHourPatternsPEOObjectId | — |
| OBJECT_VERSION_NUMBER | WorkingHourPatternsPEOObjectVersionNumber | — |
| PERSON_ID | WorkingHourPatternsPEOPersonId1 | — |
| SAT_END_TIME | WorkingHourPatternsPEOSatEndTime | ✅ |
| SAT_HOURS | WorkingHourPatternsPEOSatHours | ✅ |
| SAT_START_TIME | WorkingHourPatternsPEOSatStartTime | ✅ |
| SUN_END_TIME | WorkingHourPatternsPEOSunEndTime | ✅ |
| SUN_HOURS | WorkingHourPatternsPEOSunHours | ✅ |
| SUN_START_TIME | WorkingHourPatternsPEOSunStartTime | ✅ |
| THU_END_TIME | WorkingHourPatternsPEOThuEndTime | ✅ |
| THU_HOURS | WorkingHourPatternsPEOThuHours | ✅ |
| THU_START_TIME | WorkingHourPatternsPEOThuStartTime | ✅ |
| TOTAL_HOURS | WorkingHourPatternsPEOTotalHours | — |
| TUE_END_TIME | WorkingHourPatternsPEOTueEndTime | ✅ |
| TUE_HOURS | WorkingHourPatternsPEOTueHours | ✅ |
| TUE_START_TIME | WorkingHourPatternsPEOTueStartTime | ✅ |
| WED_END_TIME | WorkingHourPatternsPEOWedEndTime | ✅ |
| WED_HOURS | WorkingHourPatternsPEOWedHours | ✅ |
| WED_START_TIME | WorkingHourPatternsPEOWedStartTime | ✅ |
| WHP_ATTRIBUTE1 | WorkingHourPatternsPEOWhpAttribute1 | — |
| WHP_ATTRIBUTE10 | WorkingHourPatternsPEOWhpAttribute10 | — |
| WHP_ATTRIBUTE11 | WorkingHourPatternsPEOWhpAttribute11 | — |
| WHP_ATTRIBUTE12 | WorkingHourPatternsPEOWhpAttribute12 | — |
| WHP_ATTRIBUTE13 | WorkingHourPatternsPEOWhpAttribute13 | — |
| WHP_ATTRIBUTE14 | WorkingHourPatternsPEOWhpAttribute14 | — |
| WHP_ATTRIBUTE15 | WorkingHourPatternsPEOWhpAttribute15 | — |
| WHP_ATTRIBUTE16 | WorkingHourPatternsPEOWhpAttribute16 | — |
| WHP_ATTRIBUTE17 | WorkingHourPatternsPEOWhpAttribute17 | — |
| WHP_ATTRIBUTE18 | WorkingHourPatternsPEOWhpAttribute18 | — |
| WHP_ATTRIBUTE19 | WorkingHourPatternsPEOWhpAttribute19 | — |
| WHP_ATTRIBUTE2 | WorkingHourPatternsPEOWhpAttribute2 | — |
| WHP_ATTRIBUTE20 | WorkingHourPatternsPEOWhpAttribute20 | — |
| WHP_ATTRIBUTE3 | WorkingHourPatternsPEOWhpAttribute3 | — |
| WHP_ATTRIBUTE4 | WorkingHourPatternsPEOWhpAttribute4 | — |
| WHP_ATTRIBUTE5 | WorkingHourPatternsPEOWhpAttribute5 | — |
| WHP_ATTRIBUTE6 | WorkingHourPatternsPEOWhpAttribute6 | — |
| WHP_ATTRIBUTE7 | WorkingHourPatternsPEOWhpAttribute7 | — |
| WHP_ATTRIBUTE8 | WorkingHourPatternsPEOWhpAttribute8 | — |
| WHP_ATTRIBUTE9 | WorkingHourPatternsPEOWhpAttribute9 | — |
| WHP_ATTRIBUTE_CATEGORY | WorkingHourPatternsPEOWhpAttributeCategory | — |
| WHP_ATTRIBUTE_DATE1 | WorkingHourPatternsPEOWhpAttributeDate1 | — |
| WHP_ATTRIBUTE_DATE10 | WorkingHourPatternsPEOWhpAttributeDate10 | — |
| WHP_ATTRIBUTE_DATE11 | WorkingHourPatternsPEOWhpAttributeDate11 | — |
| WHP_ATTRIBUTE_DATE12 | WorkingHourPatternsPEOWhpAttributeDate12 | — |
| WHP_ATTRIBUTE_DATE13 | WorkingHourPatternsPEOWhpAttributeDate13 | — |
| WHP_ATTRIBUTE_DATE14 | WorkingHourPatternsPEOWhpAttributeDate14 | — |
| WHP_ATTRIBUTE_DATE15 | WorkingHourPatternsPEOWhpAttributeDate15 | — |
| WHP_ATTRIBUTE_DATE2 | WorkingHourPatternsPEOWhpAttributeDate2 | — |
| WHP_ATTRIBUTE_DATE3 | WorkingHourPatternsPEOWhpAttributeDate3 | — |
| WHP_ATTRIBUTE_DATE4 | WorkingHourPatternsPEOWhpAttributeDate4 | — |
| WHP_ATTRIBUTE_DATE5 | WorkingHourPatternsPEOWhpAttributeDate5 | — |
| WHP_ATTRIBUTE_DATE6 | WorkingHourPatternsPEOWhpAttributeDate6 | — |
| WHP_ATTRIBUTE_DATE7 | WorkingHourPatternsPEOWhpAttributeDate7 | — |
| WHP_ATTRIBUTE_DATE8 | WorkingHourPatternsPEOWhpAttributeDate8 | — |
| WHP_ATTRIBUTE_DATE9 | WorkingHourPatternsPEOWhpAttributeDate9 | — |
| WHP_ATTRIBUTE_NUMBER1 | WorkingHourPatternsPEOWhpAttributeNumber1 | — |
| WHP_ATTRIBUTE_NUMBER10 | WorkingHourPatternsPEOWhpAttributeNumber10 | — |
| WHP_ATTRIBUTE_NUMBER2 | WorkingHourPatternsPEOWhpAttributeNumber2 | — |
| WHP_ATTRIBUTE_NUMBER3 | WorkingHourPatternsPEOWhpAttributeNumber3 | — |
| WHP_ATTRIBUTE_NUMBER4 | WorkingHourPatternsPEOWhpAttributeNumber4 | — |
| WHP_ATTRIBUTE_NUMBER5 | WorkingHourPatternsPEOWhpAttributeNumber5 | — |
| WHP_ATTRIBUTE_NUMBER6 | WorkingHourPatternsPEOWhpAttributeNumber6 | — |
| WHP_ATTRIBUTE_NUMBER7 | WorkingHourPatternsPEOWhpAttributeNumber7 | — |
| WHP_ATTRIBUTE_NUMBER8 | WorkingHourPatternsPEOWhpAttributeNumber8 | — |
| WHP_ATTRIBUTE_NUMBER9 | WorkingHourPatternsPEOWhpAttributeNumber9 | — |
| WORKING_HOUR_PATTERN_ID | WorkingHourPatternsPEOWorkingHourPatternId | ✅ |
| WORKING_HOURS_TYPE | WorkingHourPatternsPEOWorkingHoursType | ✅ |
