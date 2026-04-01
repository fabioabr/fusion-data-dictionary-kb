---
id: DOC-HCM-606
doc_type: system-doc
title: "PER_ACCRUAL_BANDS — Faixas de Acumulação"
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
  - faixas-acumulacao
aliases:
  - PER_ACCRUAL_BANDS
  - per_accrual_bands
  - per-accrual-bands
  - faixas-de-acumulação
  - per-accrual-bands
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACCRUAL_BANDS

## 📌 Visão Geral

Armazena as **faixas (bandas) de acumulação** utilizadas nos planos de accrual de ausências. Define regras de acumulação progressiva baseadas em tempo de serviço ou outros critérios.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Acumulação progressiva** — define diferentes taxas de acumulação por faixa de tempo de serviço.
- **Políticas de férias** — colaboradores com mais tempo de serviço podem acumular mais dias.
- **Configuração flexível** — permite múltiplas faixas por plano de acumulação.
- **Compliance trabalhista** — atendimento a regras legais de acumulação por antiguidade.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCRUAL_BAND_ID | NUMBER(18) | NOT NULL | PK | Identificador único da faixa de acumulação | — | 🟢 90% |
| 2 | ACCRUAL_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de acumulação associado | PER_ACCRUAL_PLANS_B | 🟢 90% |
| 3 | LOWER_LIMIT | NUMBER | NOT NULL | Configuração | Limite inferior da faixa (em meses/anos de serviço) | — | 🟢 85% |
| 4 | UPPER_LIMIT | NUMBER | NULL | Configuração | Limite superior da faixa | — | 🟢 85% |
| 5 | ACCRUAL_RATE | NUMBER | NOT NULL | Configuração | Taxa de acumulação para esta faixa | — | 🟢 85% |
| 6 | CEILING | NUMBER | NULL | Configuração | Teto máximo de acumulação na faixa | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_accrual_plans_b]] — via `ACCRUAL_PLAN_ID` (plano de acumulação pai)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Faixas de acumulação de um plano
```sql
SELECT pab.LOWER_LIMIT, pab.UPPER_LIMIT, pab.ACCRUAL_RATE, pab.CEILING
FROM   PER_ACCRUAL_BANDS pab
WHERE  pab.ACCRUAL_PLAN_ID = :p_accrual_plan_id
ORDER BY pab.LOWER_LIMIT;
```

### Filtros comuns
- `ACCRUAL_PLAN_ID = :p_plan_id` — Faixas de um plano específico
---

## 🔒 Observações

- As faixas são definidas por intervalos de tempo de serviço (ex.: 0-5 anos, 5-10 anos).
- O `ACCRUAL_RATE` define quantos dias/horas são acumulados por período dentro desta faixa.
- O `CEILING` limita o saldo máximo acumulável — útil para políticas de 'use it or lose it'.
---

## 🔗 PVOs Relacionados

### [[accrualplanbandpvo|AccrualPlanBandPVO]] (GL · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_BAND_ID | AccrualBandId | — |
| ACCRUAL_PLAN_ID | AccrualBandPEOAccrualPlanId | — |
| BAND_GROUP_CODE | AccrualBandPEOBandGroupCode | — |
| BAND_RANGE_END | AccrualBandPEOBandRangeEnd | — |
| BAND_RANGE_START | AccrualBandPEOBandRangeStart | — |
| CREATED_BY | AccrualBandPEOCreatedBy | — |
| CREATION_DATE | AccrualBandPEOCreationDate | — |
| LAST_UPDATE_DATE | AccrualBandPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AccrualBandPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AccrualBandPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AccrualBandPEOObjectVersionNumber | — |
| TERM_ACCRUAL_RATE | AccrualBandPEOTermAccrualRate | — |
| TERM_CEILING_VALUE | AccrualBandPEOTermCeilingValue | — |
| TERM_MAX_CARRY_OVER | AccrualBandPEOTermMaxCarryOver | — |

---

## 📚 Referências

- [Oracle Docs — PER_ACCRUAL_BANDS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peraccrualband.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
