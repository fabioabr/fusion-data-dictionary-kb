---
id: DOC-HCM-019
doc_type: system-doc
title: "ANC_PER_ABS_PLN_SUMM_ENT — Sumário de Plano de Ausência por Pessoa"
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
  - sumario-plano
  - plan-summary
  - saldo-ausencia
aliases:
  - ANC_PER_ABS_PLN_SUMM_ENT
  - anc_per_abs_pln_summ_ent
  - sumario-plano-ausencia
  - absence-plan-summary
  - anc-per-abs-pln-summ
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_PLN_SUMM_ENT

## 📌 Visão Geral

Armazena o **sumário consolidado** de utilização de planos de ausência por colaborador. Contém totais de saldo acumulado, consumido e remanescente.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Visão consolidada:** Resumo de saldo por plano para cada colaborador.
- **Self-service:** Alimenta a tela de saldos no portal do colaborador.
- **Gestão de pessoas:** Visão rápida de saldos para gestores.
- **Relatórios de RH:** Dashboard de saldos de ausência por equipe/departamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_PLN_SUMM_ID | NUMBER(18) | NOT NULL | PK | Identificador único do sumário | — | 🟢 85% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de ausência | [[anc_absence_plans_f]] | 🟢 90% |
| 4 | ACCRUED_BALANCE | NUMBER | NULL | Saldo | Saldo acumulado total | — | 🟡 75% |
| 5 | CONSUMED_BALANCE | NUMBER | NULL | Saldo | Saldo consumido | — | 🟡 75% |
| 6 | REMAINING_BALANCE | NUMBER | NULL | Saldo | Saldo remanescente | — | 🟡 75% |
| 7 | PERIOD_START_DATE | DATE | NULL | Período | Início do período de acumulação | — | 🟡 70% |
| 8 | PERIOD_END_DATE | DATE | NULL | Período | Fim do período de acumulação | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do resumo do plano de ausencia)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (plano de ausencia do resumo)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Saldo de ausência por colaborador
```sql
SELECT s.PERSON_ID, p.PLAN_NAME,
       s.ACCRUED_BALANCE, s.CONSUMED_BALANCE, s.REMAINING_BALANCE
FROM   ANC_PER_ABS_PLN_SUMM_ENT s
JOIN   ANC_ABSENCE_PLANS_F p ON s.ABSENCE_PLAN_ID = p.ABSENCE_PLAN_ID
WHERE  s.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN p.EFFECTIVE_START_DATE AND p.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `REMAINING_BALANCE > 0` — Colaboradores com saldo disponível

---

## 🔒 Observações

- Tabela de sumário recalculada periodicamente ou após cada transação.
- `REMAINING_BALANCE = ACCRUED_BALANCE - CONSUMED_BALANCE`.
- Pode conter múltiplos registros por colaborador (um por plano e período).

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_PLN_SUMM_ENT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabsplnsumment.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
