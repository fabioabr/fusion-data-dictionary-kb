---
id: DOC-HCM-344
doc_type: system-doc
title: "HWM_TC_VERSION_STATUS_V — Status de Versão de Cartão de Ponto (View)"
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
  - time-card
  - versao
  - status
  - view
aliases:
  - HWM_TC_VERSION_STATUS_V
  - hwm_tc_version_status_v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TC_VERSION_STATUS_V

## 📌 Visão Geral

View que exibe o status atual de cada versão de cartão de ponto, incluindo estados como rascunho, submetido, aprovado e transferido.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — objeto somente leitura que consolida dados de uma ou mais tabelas para facilitar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de cartão de ponto:** Controle de registros de horas trabalhadas por colaborador.
- **Consolidação de horas:** Resumo de horas por período para aprovação e processamento.
- **Fluxo de aprovação:** Suporte ao ciclo de submissão, aprovação e transferência.
- **Integração com Payroll:** Base para cálculo de remuneração variável.

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
FROM   HWM_TC_VERSION_STATUS_V t
WHERE  t.STATUS_CODE = 'APPROVED'
```

### Filtros comuns
- `STATUS_CODE = 'APPROVED'` — Registros aprovados
- `PERSON_ID = :p_person_id` — Filtro por trabalhador

---

## 🔒 Observações

- View somente leitura: não permite INSERT, UPDATE ou DELETE direto.
- Área funcional: Time Card dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| MAX_A_USER_STATUS_ID | TimeCardVersionStatusPEOMaxAUserStatusId | — |
| MAX_D_UI_STATUS_ID | TimeCardVersionStatusPEOMaxDUiStatusId | — |
| TM_BLDG_BLK_ID | TimeCardVersionStatusPEOTmBldgBlkId | — |
| TM_BLDG_BLK_VERSION | TimeCardVersionStatusPEOTmBldgBlkVersion | — |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| MAX_A_USER_STATUS_ID | TimeCardVersionStatusPEOMaxAUserStatusId | — |
| MAX_D_UI_STATUS_ID | TimeCardVersionStatusPEOMaxDUiStatusId | — |
| TM_BLDG_BLK_ID | TimeCardVersionStatusPEOTmBldgBlkId | — |
| TM_BLDG_BLK_VERSION | TimeCardVersionStatusPEOTmBldgBlkVersion | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TC_VERSION_STATUS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tc_version_status_v.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
