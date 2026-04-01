---
id: DOC-HCM-374
doc_type: system-doc
title: "HWM_TM_D_XFR_STATUS_PYR_V — Status de Transferência para Payroll — Detalhes (View)"
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
  - transferencia
  - payroll
  - detalhes
  - view
aliases:
  - HWM_TM_D_XFR_STATUS_PYR_V
  - hwm_tm_d_xfr_status_pyr_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_D_XFR_STATUS_PYR_V

## 📌 Visão Geral

View detalhada do status de transferência de registros de tempo para Payroll, incluindo informações de erro e reprocessamento para folha de pagamento.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Monitoramento de status:** Acompanhamento do estado de registros de tempo no fluxo de aprovação.
- **Integração com Payroll:** Controle de registros prontos para transferência à folha de pagamento.
- **Integração com Project Costing:** Controle de registros prontos para alocação em projetos.
- **Gestão de aprovações:** Visibilidade do status de aprovação para gestores e trabalhadores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Referência à pessoa/trabalhador | PER_ALL_PEOPLE_F | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Código do status atual | — | 🟡 75% |
| 4 | STATUS_MEANING | VARCHAR2(240) | NULL | Identificação | Descrição do status | — | 🟡 70% |
| 5 | PERIOD_START_DATE | DATE | NULL | Período | Data de início do período | — | 🟡 75% |
| 6 | PERIOD_END_DATE | DATE | NULL | Período | Data de fim do período | — | 🟡 75% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NULL | Auditoria | Data/hora da última alteração | — | 🟢 90% |
| 8 | PROCESS_DATE | DATE | NULL | Controle | Data do processamento | — | 🟡 70% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.PERSON_ID, t.STATUS_CODE, t.STATUS_MEANING
FROM   HWM_TM_D_XFR_STATUS_PYR_V t
WHERE  t.STATUS_CODE = 'APPROVED'
```

### Filtros comuns
- `STATUS_CODE = 'APPROVED'` — Registros aprovados
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Tabela relacionada a transferência de dados para sistemas externos (Payroll, Project Costing).
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TimeEntryReadyXfrPyrStatusId | — |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TimeEntryReadyXfrPyrStatusId | — |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TimeEntryReadyXfrPyrStatusId | — |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TimeEntryReadyXfrPyrStatusId | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_D_XFR_STATUS_PYR_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_d_xfr_status_pyr_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
