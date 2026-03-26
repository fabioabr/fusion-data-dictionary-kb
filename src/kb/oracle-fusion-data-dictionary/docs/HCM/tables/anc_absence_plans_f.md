---
id: DOC-HCM-003
doc_type: system-doc
title: "ANC_ABSENCE_PLANS_F — Planos de Ausência"
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
  - planos-ausencia
  - absence-plans
  - accrual
aliases:
  - ANC_ABSENCE_PLANS_F
  - anc_absence_plans_f
  - planos-ausencia-hcm
  - absence-plans
  - anc-abs-plans
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABSENCE_PLANS_F

## 📌 Visão Geral

Armazena os **planos de ausência** do módulo Absence Management. Um plano define as regras de acumulação, elegibilidade e saldo para um tipo específico de ausência (ex.: plano de férias com 30 dias anuais, plano de licença médica com regras de acúmulo mensal).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de políticas de ausência:** Configura regras de acumulação (accrual), teto de saldo, carência e carry-over.
- **Elegibilidade:** Define critérios de elegibilidade por cargo, departamento, legislação ou antiguidade.
- **Cálculo de saldos:** Base para o cálculo de saldo disponível de ausências por colaborador.
- **Compliance trabalhista:** Atende requisitos legais de férias, licenças e afastamentos por jurisdição.
- **Integração com folha:** Planos vinculados a elementos de folha de pagamento para desconto/pagamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano de ausência | — | 🟢 95% |
| 2 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano de ausência | — | 🟢 90% |
| 3 | PLAN_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do plano (A — ativo, I — inativo) | — | 🟢 90% |
| 4 | ABSENCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de ausência associado ao plano | [[anc_absence_types_f]] | 🟡 75% |
| 5 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 90% |
| 6 | ACCRUAL_FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência de acumulação (MONTHLY, YEARLY, etc.) | — | 🟡 70% |
| 7 | ACCRUAL_RATE | NUMBER | NULL | Configuração | Taxa de acumulação por período | — | 🟡 70% |
| 8 | MAX_CARRYOVER | NUMBER | NULL | Configuração | Máximo de saldo transferível entre períodos | — | 🟡 70% |
| 9 | CEILING_LIMIT | NUMBER | NULL | Configuração | Teto máximo de acumulação | — | 🟡 70% |
| 10 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 11 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo de ausência associado)

### Tabelas-filha (FK de saída)
- [[anc_absence_plans_f_tl]] — via `ABSENCE_PLAN_ID` (traducoes multilingue do registro)
- [[anc_per_plan_enrollment]] — via `ABSENCE_PLAN_ID` (inscrições de colaboradores)
- [[anc_per_abs_plan_entries]] — via `ABSENCE_PLAN_ID` (entradas de plano por pessoa)
- [[anc_accrual_bands_f]] — via `ABSENCE_PLAN_ID` (faixas de acumulação)

---

## 📎 Uso Típico

### Planos de ausência ativos por legislação
```sql
SELECT ap.ABSENCE_PLAN_ID, ap.PLAN_NAME, ap.PLAN_STATUS,
       ap.ACCRUAL_FREQUENCY, ap.CEILING_LIMIT
FROM   ANC_ABSENCE_PLANS_F ap
WHERE  SYSDATE BETWEEN ap.EFFECTIVE_START_DATE AND ap.EFFECTIVE_END_DATE
  AND  ap.PLAN_STATUS = 'A'
  AND  ap.LEGISLATION_CODE = :p_legislation_code;
```

### Filtros comuns
- `PLAN_STATUS = 'A'` — Planos ativos
- `LEGISLATION_CODE = 'BR'` — Planos para legislação brasileira
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência.
- O plano define as regras; a inscrição do colaborador está em `ANC_PER_PLAN_ENROLLMENT`.
- Campos de acumulação (`ACCRUAL_FREQUENCY`, `ACCRUAL_RATE`, `MAX_CARRYOVER`, `CEILING_LIMIT`) podem ter valores nulos se o plano não usar acumulação automática.
- Planos podem ser associados a elementos de folha via integração Payroll.

---

## 📚 Referências

- [Oracle Docs — ANC_ABSENCE_PLANS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabsenceplansf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
