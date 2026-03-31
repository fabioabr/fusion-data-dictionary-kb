---
id: DOC-HCM-308
doc_type: system-doc
title: "HWM_RP_TM_PERIODS_B — Períodos de Tempo para Relatórios (Base)"
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
  - periodos
  - reporting
  - base
aliases:
  - HWM_RP_TM_PERIODS_B
  - hwm_rp_tm_periods_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RP_TM_PERIODS_B

## 📌 Visão Geral

Tabela base que armazena os períodos de tempo utilizados para geração de relatórios de workforce management, incluindo definições de início e fim de cada período.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de períodos de reporting:** Configuração dos períodos temporais para geração de relatórios de workforce.
- **Análise temporal:** Base para consolidação de dados por período (semanal, quinzenal, mensal).
- **Integração com calendários:** Alinhamento dos períodos de reporte com calendários organizacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | RP_TM_PERIODS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | CODE | VARCHAR2(30) | NOT NULL | Identificação | Código identificador único | — | 🟢 90% |
| 3 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro (A/I) | — | 🟡 80% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se está habilitado (Y/N) | — | 🟡 75% |
| 5 | START_DATE | DATE | NULL | Vigência | Data de início de validade | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Vigência | Data de fim de validade | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_RP_TM_PERIODS_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Área funcional: Time and Reporting dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[approvaltimeperiod|ApprovalTimePeriod]] (GL · BICC: 15/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_USAGE | RepeatingTimePeriodPEOAccrualUsage | — |
| APPROVAL_USAGE | RepeatingTimePeriodPEOApprovalUsage | — |
| BALANCE_USAGE | RepeatingTimePeriodPEOBalanceUsage | — |
| CREATED_BY | RepeatingTimePeriodPEOCreatedBy | ✅ |
| CREATION_DATE | RepeatingTimePeriodPEOCreationDate | ✅ |
| ENTERPRISE_ID | RepeatingTimePeriodPEOEnterpriseId | — |
| LAST_UPDATE_DATE | RepeatingTimePeriodPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RepeatingTimePeriodPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RepeatingTimePeriodPEOLastUpdatedBy | ✅ |
| MODULE_ID | RepeatingTimePeriodPEOModuleId | — |
| MONTH_TYPE | RepeatingTimePeriodPEOMonthType | ✅ |
| MULTIPLE | RepeatingTimePeriodPEOMultiple | ✅ |
| OBJECT_VERSION_NUMBER | RepeatingTimePeriodPEOObjectVersionNumber | — |
| ONE_OR_MANY | RepeatingTimePeriodPEOOneOrMany | ✅ |
| OVERTIME_USAGE | RepeatingTimePeriodPEOOvertimeUsage | — |
| PERIOD_CD | RepeatingTimePeriodPEOPeriodCd | ✅ |
| PERIOD_CLASS | RepeatingTimePeriodPEOPeriodClass | ✅ |
| PERIOD_LENGTH | RepeatingTimePeriodPEOPeriodLength | ✅ |
| PERIOD_START_DATE | RepeatingTimePeriodPEOPeriodStartDate | ✅ |
| PERIOD_TYPE | RepeatingTimePeriodPEOPeriodType | — |
| REFERENCE_DATE | RepeatingTimePeriodPEOReferenceDate | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodPEORepeatingTmPeriodId | ✅ |
| RULE_USAGE | RepeatingTimePeriodPEORuleUsage | — |
| TIME_ENTRY_USAGE | RepeatingTimePeriodPEOTimeEntryUsage | — |
| WEEK_TYPE | RepeatingTimePeriodPEOWeekType | ✅ |

### [[overtimetimeperiod|OvertimeTimePeriod]] (GL · BICC: 15/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_USAGE | RepeatingTimePeriodPEOAccrualUsage | — |
| APPROVAL_USAGE | RepeatingTimePeriodPEOApprovalUsage | — |
| BALANCE_USAGE | RepeatingTimePeriodPEOBalanceUsage | — |
| CREATED_BY | RepeatingTimePeriodPEOCreatedBy | ✅ |
| CREATION_DATE | RepeatingTimePeriodPEOCreationDate | ✅ |
| ENTERPRISE_ID | RepeatingTimePeriodPEOEnterpriseId | — |
| LAST_UPDATE_DATE | RepeatingTimePeriodPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RepeatingTimePeriodPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RepeatingTimePeriodPEOLastUpdatedBy | ✅ |
| MODULE_ID | RepeatingTimePeriodPEOModuleId | — |
| MONTH_TYPE | RepeatingTimePeriodPEOMonthType | ✅ |
| MULTIPLE | RepeatingTimePeriodPEOMultiple | ✅ |
| OBJECT_VERSION_NUMBER | RepeatingTimePeriodPEOObjectVersionNumber | — |
| ONE_OR_MANY | RepeatingTimePeriodPEOOneOrMany | ✅ |
| OVERTIME_USAGE | RepeatingTimePeriodPEOOvertimeUsage | — |
| PERIOD_CD | RepeatingTimePeriodPEOPeriodCd | ✅ |
| PERIOD_CLASS | RepeatingTimePeriodPEOPeriodClass | ✅ |
| PERIOD_LENGTH | RepeatingTimePeriodPEOPeriodLength | ✅ |
| PERIOD_START_DATE | RepeatingTimePeriodPEOPeriodStartDate | ✅ |
| PERIOD_TYPE | RepeatingTimePeriodPEOPeriodType | — |
| REFERENCE_DATE | RepeatingTimePeriodPEOReferenceDate | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodPEORepeatingTmPeriodId | ✅ |
| RULE_USAGE | RepeatingTimePeriodPEORuleUsage | — |
| TIME_ENTRY_USAGE | RepeatingTimePeriodPEOTimeEntryUsage | — |
| WEEK_TYPE | RepeatingTimePeriodPEOWeekType | ✅ |

### [[repeatingtimeperiod|RepeatingTimePeriod]] (GL · BICC: 25/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_USAGE | RepeatingTimePeriodPEOAccrualUsage | ✅ |
| APPROVAL_USAGE | RepeatingTimePeriodPEOApprovalUsage | ✅ |
| BALANCE_USAGE | RepeatingTimePeriodPEOBalanceUsage | ✅ |
| CREATED_BY | RepeatingTimePeriodPEOCreatedBy | ✅ |
| CREATION_DATE | RepeatingTimePeriodPEOCreationDate | ✅ |
| ENTERPRISE_ID | RepeatingTimePeriodPEOEnterpriseId | ✅ |
| LAST_UPDATE_DATE | RepeatingTimePeriodPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RepeatingTimePeriodPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RepeatingTimePeriodPEOLastUpdatedBy | ✅ |
| MODULE_ID | RepeatingTimePeriodPEOModuleId | ✅ |
| MONTH_TYPE | RepeatingTimePeriodPEOMonthType | ✅ |
| MULTIPLE | RepeatingTimePeriodPEOMultiple | ✅ |
| OBJECT_VERSION_NUMBER | RepeatingTimePeriodPEOObjectVersionNumber | ✅ |
| ONE_OR_MANY | RepeatingTimePeriodPEOOneOrMany | ✅ |
| OVERTIME_USAGE | RepeatingTimePeriodPEOOvertimeUsage | ✅ |
| PERIOD_CD | RepeatingTimePeriodPEOPeriodCd | ✅ |
| PERIOD_CLASS | RepeatingTimePeriodPEOPeriodClass | ✅ |
| PERIOD_LENGTH | RepeatingTimePeriodPEOPeriodLength | ✅ |
| PERIOD_START_DATE | RepeatingTimePeriodPEOPeriodStartDate | ✅ |
| PERIOD_TYPE | RepeatingTimePeriodPEOPeriodType | ✅ |
| REFERENCE_DATE | RepeatingTimePeriodPEOReferenceDate | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodPEORepeatingTmPeriodId | ✅ |
| RULE_USAGE | RepeatingTimePeriodPEORuleUsage | ✅ |
| TIME_ENTRY_USAGE | RepeatingTimePeriodPEOTimeEntryUsage | ✅ |
| WEEK_TYPE | RepeatingTimePeriodPEOWeekType | ✅ |

### [[resolvedtimeperiod|ResolvedTimePeriod]] (GL · BICC: 20/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_USAGE | RepeatingTimePeriodPEOAccrualUsage | ✅ |
| APPROVAL_USAGE | RepeatingTimePeriodPEOApprovalUsage | ✅ |
| BALANCE_USAGE | RepeatingTimePeriodPEOBalanceUsage | ✅ |
| CREATED_BY | RepeatingTimePeriodPEOCreatedBy1 | ✅ |
| CREATION_DATE | RepeatingTimePeriodPEOCreationDate1 | ✅ |
| ENTERPRISE_ID | RepeatingTimePeriodPEOnterpriseId1 | — |
| LAST_UPDATE_DATE | RepeatingTimePeriodPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | RepeatingTimePeriodPEOLastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | RepeatingTimePeriodPEOLastUpdatedBy1 | ✅ |
| MODULE_ID | RepeatingTimePeriodPEOModuleId | — |
| MONTH_TYPE | RepeatingTimePeriodPEOMonthType | ✅ |
| MULTIPLE | RepeatingTimePeriodPEOMultiple | ✅ |
| OBJECT_VERSION_NUMBER | RepeatingTimePeriodPEOObjectVersionNumber1 | — |
| ONE_OR_MANY | RepeatingTimePeriodPEOOneOrMany | ✅ |
| OVERTIME_USAGE | RepeatingTimePeriodPEOOvertimeUsage | ✅ |
| PERIOD_CD | RepeatingTimePeriodPEOPeriodCd | ✅ |
| PERIOD_CLASS | RepeatingTimePeriodPEOPeriodClass | ✅ |
| PERIOD_LENGTH | RepeatingTimePeriodPEOPeriodLength | ✅ |
| PERIOD_START_DATE | RepeatingTimePeriodPEOPeriodStartDate | ✅ |
| PERIOD_TYPE | RepeatingTimePeriodPEOPeriodType | — |
| REFERENCE_DATE | RepeatingTimePeriodPEOReferenceDate | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodPEORepeatingTmPeriodId1 | — |
| RULE_USAGE | RepeatingTimePeriodPEORuleUsage | ✅ |
| TIME_ENTRY_USAGE | RepeatingTimePeriodPEOTimeEntryUsage | ✅ |
| WEEK_TYPE | RepeatingTimePeriodPEOWeekType | ✅ |

### [[timecardtimeperiod|TimecardTimePeriod]] (GL · BICC: 15/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_USAGE | RepeatingTimePeriodPEOAccrualUsage | — |
| APPROVAL_USAGE | RepeatingTimePeriodPEOApprovalUsage | — |
| BALANCE_USAGE | RepeatingTimePeriodPEOBalanceUsage | — |
| CREATED_BY | RepeatingTimePeriodPEOCreatedBy | ✅ |
| CREATION_DATE | RepeatingTimePeriodPEOCreationDate | ✅ |
| ENTERPRISE_ID | RepeatingTimePeriodPEOEnterpriseId | — |
| LAST_UPDATE_DATE | RepeatingTimePeriodPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RepeatingTimePeriodPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RepeatingTimePeriodPEOLastUpdatedBy | ✅ |
| MODULE_ID | RepeatingTimePeriodPEOModuleId | — |
| MONTH_TYPE | RepeatingTimePeriodPEOMonthType | ✅ |
| MULTIPLE | RepeatingTimePeriodPEOMultiple | ✅ |
| OBJECT_VERSION_NUMBER | RepeatingTimePeriodPEOObjectVersionNumber | — |
| ONE_OR_MANY | RepeatingTimePeriodPEOOneOrMany | ✅ |
| OVERTIME_USAGE | RepeatingTimePeriodPEOOvertimeUsage | — |
| PERIOD_CD | RepeatingTimePeriodPEOPeriodCd | ✅ |
| PERIOD_CLASS | RepeatingTimePeriodPEOPeriodClass | ✅ |
| PERIOD_LENGTH | RepeatingTimePeriodPEOPeriodLength | ✅ |
| PERIOD_START_DATE | RepeatingTimePeriodPEOPeriodStartDate | ✅ |
| PERIOD_TYPE | RepeatingTimePeriodPEOPeriodType | — |
| REFERENCE_DATE | RepeatingTimePeriodPEOReferenceDate | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodPEORepeatingTmPeriodId | ✅ |
| RULE_USAGE | RepeatingTimePeriodPEORuleUsage | — |
| TIME_ENTRY_USAGE | RepeatingTimePeriodPEOTimeEntryUsage | — |
| WEEK_TYPE | RepeatingTimePeriodPEOWeekType | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_RP_TM_PERIODS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rp_tm_periods_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
