---
id: DOC-HCM-379
doc_type: system-doc
title: "HWM_TM_HIS_RPT_ENTRY_V — View Histórica de Entradas Reportadas de Tempo"
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
  - time-management
  - reported-entry
  - historico-reportado
  - view
aliases:
  - HWM_TM_HIS_RPT_ENTRY_V
  - hwm_tm_his_rpt_entry_v
  - hwm-tm-his-rpt-entry-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_HIS_RPT_ENTRY_V

## 📌 Visão Geral

View que apresenta o **histórico de entradas reportadas** de tempo. Focada em entradas que já foram submetidas e reportadas para processamento de folha de pagamento.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** — consulta pré-definida sobre tabelas base, somente leitura.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta de entradas reportadas:** visualizar time entries já submetidas ao payroll.
- **Reconciliação:** verificar consistência entre entradas reportadas e folha processada.
- **Auditoria:** rastrear entradas de tempo que geraram custos de mão de obra.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 2 | RPT_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador da entrada reportada | — | 🟡 65% |
| 3 | TIME_ENTRY_ID | NUMBER(18) | NULL | FK | Entrada de tempo original | — | 🟡 65% |
| 4 | ENTRY_DATE | DATE | NOT NULL | Período | Data da entrada reportada | — | 🟡 70% |
| 5 | MEASURE | NUMBER | NULL | Dados | Quantidade reportada (horas) | — | 🟡 60% |
| 6 | REPORTED_STATUS | VARCHAR2(30) | NULL | Classificação | Status do reporte | — | 🟡 60% |
| 7 | PAYROLL_PERIOD_ID | NUMBER(18) | NULL | FK | Período de folha associado | — | 🟡 55% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do historico de registro de tempo)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Entradas reportadas por período
```sql
SELECT v.PERSON_ID, v.ENTRY_DATE, v.MEASURE, v.REPORTED_STATUS
FROM   HWM_TM_HIS_RPT_ENTRY_V v
WHERE  v.ENTRY_DATE BETWEEN :dt_ini AND :dt_fim;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `ENTRY_DATE BETWEEN :dt_ini AND :dt_fim — Período`

---

## 🔒 Observações

- View somente leitura — não suporta DML.
- Foco em entradas já reportadas ao payroll.

---

## 🔗 PVOs Relacionados

### [[historicrptabstimerecordpvo|HistoricRptAbsTimeRecordPVO]] (HCM · BICC: 9/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DAY_TM_REC_GRP_ID | DayTmRecGrpId | — |
| DAY_TM_REC_GRP_VERSION | DayTmRecGrpVersion | — |
| GROUP_TYPE_ID | GroupTypeId | — |
| HISTORIC_CHANGE_DATE_FROM | HistoricChangeDateFrom | ✅ |
| HISTORIC_CHANGE_DATE_TO | HistoricChangeDateTo | ✅ |
| HISTORIC_CHANGE_TIME | HistoricChangeTime | ✅ |
| TC_APPROVED_TIMESTAMP | TcApprovedTimestamp | ✅ |
| TC_SUBMITTED_TIMESTAMP | TcSubmittedTimestamp | ✅ |
| TC_UI_STATUS_VALUE | TcUiStatusValue | ✅ |
| TC_USER_STATUS_VALUE | TcUserStatusValue | ✅ |
| TIME_CARD_TM_REC_GRP_ID | TimeCardTmRecGrpId | — |
| TIME_CARD_TM_REC_GRP_VERSION | TimeCardTmRecGrpVersion | — |
| TIME_RECORD_ID | TimeRecordId | ✅ |
| TIME_RECORD_LAYER_CODE | TimeRecordLayerCode | — |
| TIME_RECORD_VERSION | TimeRecordVersion | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_HIS_RPT_ENTRY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmhisrptentryv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
