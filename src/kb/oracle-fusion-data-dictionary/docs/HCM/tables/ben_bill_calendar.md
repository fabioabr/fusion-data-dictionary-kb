---
id: DOC-HCM-027
doc_type: system-doc
title: "BEN_BILL_CALENDAR — Calendário de Cobrança de Benefícios"
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
  - benefits
  - calendario-cobranca
  - bill-calendar
aliases:
  - BEN_BILL_CALENDAR
  - ben_bill_calendar
  - calendario-cobranca-beneficios
  - bill-calendar
  - ben-bill-calendar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CALENDAR

## 📌 Visão Geral

Armazena os **calendários de cobrança** (billing) dos benefícios. Define os períodos e datas de cobrança para premiações e contribuições de benefícios.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Calendário de Cobrança de Benefícios.
- **Controle de cobranças:** Rastreamento de valores devidos e pagos.
- **Reconciliação:** Base para reconciliação financeira de benefícios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BILL_CALENDAR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do calendário | — | 🟢 90% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do calendário de cobrança | — | 🟢 90% |
| 3 | BILLING_FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência (MONTHLY, QUARTERLY, etc.) | — | 🟡 80% |
| 4 | START_DATE | DATE | NULL | Período | Data de início | — | 🟢 85% |
| 5 | END_DATE | DATE | NULL | Período | Data de fim | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta.

### Tabelas-filha (FK de saída)
- [[ben_bill_charges]] — via `BILL_CALENDAR_ID` (cobrancas do calendario de faturamento)
- [[ben_bill_cycle]] — via `BILL_CALENDAR_ID` (ciclos do calendario de faturamento)

---

## 📎 Uso Típico

### Calendários de cobrança ativos
```sql
SELECT bc.BILL_CALENDAR_ID, bc.NAME, bc.BILLING_FREQUENCY
FROM   BEN_BILL_CALENDAR bc
WHERE  bc.END_DATE IS NULL OR bc.END_DATE > SYSDATE;
```

### Filtros comuns
- `END_DATE IS NULL OR END_DATE > SYSDATE` — Calendários ativos

---

## 🔒 Observações

- Define os períodos de cobrança para contribuições de benefícios.
- A frequência de cobrança pode ser mensal, trimestral, semestral ou anual.

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CALENDAR](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillcalendar.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
