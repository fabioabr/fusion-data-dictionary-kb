---
id: DOC-HCM-021
doc_type: system-doc
title: "ANC_PER_ACCRUAL_ENTRIES — Entradas de Acumulação por Pessoa"
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
  - absence-management
  - acumulacao
  - accrual
  - saldo
  - credito
  - debito
aliases:
  - ANC_PER_ACCRUAL_ENTRIES
  - anc_per_accrual_entries
  - acumulacao-ausencia
  - accrual-entries
  - anc-per-accrual-entries
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ACCRUAL_ENTRIES

## 📌 Visão Geral

Armazena as **entradas individuais de acumulação (accrual)** de ausência por colaborador. Cada registro representa um evento de acumulação de saldo (crédito) ou consumo (débito).


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento de saldo:** Histórico detalhado de cada movimentação de saldo.
- **Auditoria de acumulação:** Registro de cada crédito e débito de saldo.
- **Reconciliação:** Permite verificar a composição do saldo atual.
- **Cálculo de folha:** Base para integração com elementos de pagamento de férias.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ACCRUAL_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da entrada de acumulação | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de ausência | [[anc_absence_plans_f]] | 🟢 90% |
| 4 | ACCRUAL_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo: ACCRUAL (crédito), USAGE (débito), ADJUSTMENT | — | 🟡 80% |
| 5 | ACCRUAL_VALUE | NUMBER | NOT NULL | Valor | Valor acumulado/consumido | — | 🟢 85% |
| 6 | ACCRUAL_DATE | DATE | NOT NULL | Data | Data da acumulação | — | 🟢 85% |
| 7 | ABSENCE_ENTRY_ID | NUMBER(18) | NULL | FK | Ausência vinculada (para débitos) | [[anc_per_abs_entries]] | 🟡 80% |
| 8 | RUNNING_BALANCE | NUMBER | NULL | Saldo | Saldo acumulado após esta entrada | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do acumulo de ausencia)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (plano de ausencia do acumulo)
- [[anc_per_abs_entries]] — via `ABSENCE_ENTRY_ID` (registro de ausencia do acumulo)

### Tabelas-filha (FK de saída)
- [[anc_per_acrl_entry_dtls]] — via `PER_ACCRUAL_ENTRY_ID` (detalhes da acumulação)

---

## 📎 Uso Típico

### Histórico de acumulação por colaborador
```sql
SELECT ae.ACCRUAL_DATE, ae.ACCRUAL_TYPE, ae.ACCRUAL_VALUE,
       ae.RUNNING_BALANCE
FROM   ANC_PER_ACCRUAL_ENTRIES ae
WHERE  ae.PERSON_ID = :p_person_id
  AND  ae.ABSENCE_PLAN_ID = :p_plan_id
ORDER BY ae.ACCRUAL_DATE;
```

### Filtros comuns
- `ACCRUAL_TYPE = 'ACCRUAL'` — Créditos de saldo
- `ACCRUAL_TYPE = 'USAGE'` — Débitos (uso de saldo)
- `ACCRUAL_TYPE = 'ADJUSTMENT'` — Ajustes manuais

---

## 🔒 Observações

- Cada registro é uma movimentação individual de saldo.
- `RUNNING_BALANCE` mostra o saldo após a operação (similar a extrato bancário).
- Débitos (`USAGE`) são vinculados a ausências específicas via `ABSENCE_ENTRY_ID`.
- Ajustes manuais (`ADJUSTMENT`) permitem correções de saldo pelo RH.

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ACCRUAL_ENTRIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperaccrualentries.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
