---
id: DOC-HCM-608
doc_type: system-doc
title: "PER_ACCRUAL_PLANS_B — Planos de Acumulação (Base)"
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
  - accrual
  - planos-acumulacao
aliases:
  - PER_ACCRUAL_PLANS_B
  - per_accrual_plans_b
  - per-accrual-plans-b
  - planos-de-acumulação-(base)
  - per-accrual-plans-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACCRUAL_PLANS_B

## 📌 Visão Geral

Armazena a definição dos **planos de acumulação (accrual plans)** de ausências. Cada plano define as regras gerais de acumulação de saldos de ausência (férias, folgas, etc.).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de saldos** — define como os colaboradores acumulam direitos de ausência ao longo do tempo.
- **Políticas de férias** — configura planos de férias com regras específicas de acumulação.
- **Carry-over** — define regras de transporte de saldo entre períodos (anos).
- **Elegibilidade** — define critérios de quem participa do plano.
- **Compliance trabalhista** — garante conformidade com legislação de férias e licenças.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCRUAL_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano de acumulação | — | 🟢 95% |
| 2 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 3 | ACCRUAL_CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria do accrual (VACATION, SICK, etc.) | — | 🟢 85% |
| 4 | ACCRUAL_PLAN_ELEMENT_TYPE_ID | NUMBER(18) | NULL | FK | Elemento de payroll associado | — | 🟡 75% |
| 5 | ACCRUAL_START | VARCHAR2(30) | NULL | Configuração | Ponto de início do accrual | — | 🟢 80% |
| 6 | ACCRUAL_UNITS_OF_MEASURE | VARCHAR2(30) | NULL | Configuração | Unidade de medida (DAYS, HOURS) | — | 🟢 85% |
| 7 | INELIGIBLE_PERIOD_TYPE | VARCHAR2(30) | NULL | Configuração | Tipo de período de inelegibilidade | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta identificada — tabela raiz de configuração de planos de accrual.

### Tabelas-filha (FK de saída)
- [[per_accrual_bands]] — via `ACCRUAL_PLAN_ID` (faixas de acumulação)
- [[per_accrual_calc_rules]] — via `ACCRUAL_PLAN_ID` (regras de cálculo)
- [[per_accrual_plans_tl]] — via `ACCRUAL_PLAN_ID` (traduÃ§Ãµes do plano de acÃºmulo de fÃ©rias/licenÃ§as)

---

## 📎 Uso Típico

### Planos de acumulação ativos
```sql
SELECT pap.ACCRUAL_PLAN_ID, pap.ACCRUAL_CATEGORY,
       pap.ACCRUAL_UNITS_OF_MEASURE
FROM   PER_ACCRUAL_PLANS_B pap
WHERE  pap.BUSINESS_GROUP_ID = :p_bg_id;
```

### Filtros comuns
- `ACCRUAL_CATEGORY = 'VACATION'` — Planos de férias
- `ACCRUAL_UNITS_OF_MEASURE = 'DAYS'` — Planos em dias
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Cada plano pode ter múltiplas faixas de acumulação (bandas) e regras de cálculo.
- O `ACCRUAL_CATEGORY` classifica o plano (férias, licença médica, etc.).
- O período de inelegibilidade controla quando novos colaboradores começam a acumular.
---

## 📚 Referências

- [Oracle Docs — PER_ACCRUAL_PLANS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peraccrualplansb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
