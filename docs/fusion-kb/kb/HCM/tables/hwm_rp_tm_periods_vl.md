---
id: DOC-HCM-310
doc_type: system-doc
title: "HWM_RP_TM_PERIODS_VL — Períodos de Tempo para Relatórios (View Consolidada)"
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
  - view-consolidada
aliases:
  - HWM_RP_TM_PERIODS_VL
  - hwm_rp_tm_periods_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RP_TM_PERIODS_VL

## 📌 Visão Geral

Visão consolidada que combina dados base e traduções dos períodos de tempo para relatórios de workforce management.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view consolidada** que combina automaticamente a tabela `_B` (dados base) com a `_TL` (traduções) para o idioma da sessão.

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
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do registro | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida | — | 🟡 80% |
| 4 | CODE | VARCHAR2(30) | NULL | Classificação | Código identificador | — | 🟡 75% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 75% |
| 6 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma da tradução | — | 🟢 90% |
| 7 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma de origem da tradução | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.NAME, t.DESCRIPTION, t.CODE
FROM   HWM_RP_TM_PERIODS_VL t
WHERE  t.LANGUAGE = USERENV('LANG')
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Tradução no idioma da sessão
- `LANGUAGE = 'PTB'` — Tradução em português brasileiro

---

## 🔒 Observações

- View consolidada: combina automaticamente dados base (`_B`) e traduções (`_TL`). Preferir em consultas de leitura.
- Área funcional: Time and Reporting dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | HxtResolvedPeriodMeaning | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodId | ✅ |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | HxtResolvedPeriodMeaning | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTimePeriodId | ✅ |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | HxtResolvedPeriodMeaning | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTmPeriodId | ✅ |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | HxtResolvedPeriodMeaning | ✅ |
| REPEATING_TM_PERIOD_ID | RepeatingTmPeriodId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_RP_TM_PERIODS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rp_tm_periods_vl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
