---
id: DOC-HCM-363
doc_type: system-doc
title: "HWM_TM_A_ANC_APP_STATUS_V — Status de Aprovação de Ausência Ancestral (View)"
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
  - ausencia
  - aprovacao
  - ancestral
  - view
aliases:
  - HWM_TM_A_ANC_APP_STATUS_V
  - hwm_tm_a_anc_app_status_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_A_ANC_APP_STATUS_V

## 📌 Visão Geral

View que exibe o status de aprovação de ausências no contexto ancestral (hierárquico), permitindo visualizar o fluxo de aprovação em cadeia.

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
FROM   HWM_TM_A_ANC_APP_STATUS_V t
WHERE  t.STATUS_CODE = 'APPROVED'
```

### Filtros comuns
- `STATUS_CODE = 'APPROVED'` — Registros aprovados
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TimEntryAtomicAncAppStatusId | — |
| STATUS_VALUE | TimEntryAtomicAncAppStatusValue | ✅ |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TimEntryAtomicAncAppStatusId | — |
| STATUS_VALUE | TimEntryAtomicAncAppStatusValue | — |

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TmAtomicAbsApprovalStatusPEOStatusId | — |
| STATUS_VALUE | TmAtomicAbsApprovalStatusPEOStatusValue | ✅ |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| STATUS_ID | TmAtomicAbsApprovalStatusPEOStatusId | — |
| STATUS_VALUE | TmAtomicAbsApprovalStatusPEOStatusValue | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_A_ANC_APP_STATUS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_a_anc_app_status_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
