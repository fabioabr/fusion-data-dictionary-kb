---
id: DOC-HCM-012
doc_type: system-doc
title: "ANC_ACCRUAL_BANDS_F — Faixas de Acumulação de Ausência"
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
  - faixas-acumulacao
  - accrual-bands
  - escalonamento
aliases:
  - ANC_ACCRUAL_BANDS_F
  - anc_accrual_bands_f
  - faixas-acumulacao-hcm
  - accrual-bands
  - anc-accrual-bands
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ACCRUAL_BANDS_F

## 📌 Visão Geral

Armazena as **faixas de acumulação (accrual bands)** dos planos de ausência. Define as regras de acumulação progressiva baseadas em tempo de serviço, antiguidade ou outros critérios (ex.: colaboradores com 0-5 anos ganham 20 dias/ano; 5-10 anos ganham 25 dias/ano).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Acumulação progressiva:** Permite configurar taxas de acumulação que aumentam com o tempo de serviço.
- **Políticas escalonadas:** Diferentes faixas para diferentes níveis de antiguidade.
- **Compliance:** Atende legislações que exigem ausências proporcionais ao tempo de empresa.
- **Cálculo automático:** Base para o engine de cálculo de saldos de ausência.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCRUAL_BAND_ID | NUMBER(18) | NOT NULL | PK | Identificador único da faixa | — | 🟢 90% |
| 2 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de ausência associado | [[anc_absence_plans_f]] | 🟢 95% |
| 3 | BAND_START | NUMBER | NOT NULL | Configuração | Início da faixa (em meses ou anos de serviço) | — | 🟡 75% |
| 4 | BAND_END | NUMBER | NULL | Configuração | Fim da faixa | — | 🟡 75% |
| 5 | ACCRUAL_RATE | NUMBER | NOT NULL | Configuração | Taxa de acumulação para esta faixa | — | 🟡 75% |
| 6 | CEILING_LIMIT | NUMBER | NULL | Configuração | Teto máximo de acumulação para esta faixa | — | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 8 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (plano de ausência)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Faixas de acumulação por plano
```sql
SELECT ab.ACCRUAL_BAND_ID, ab.BAND_START, ab.BAND_END,
       ab.ACCRUAL_RATE, ab.CEILING_LIMIT
FROM   ANC_ACCRUAL_BANDS_F ab
WHERE  ab.ABSENCE_PLAN_ID = :p_plan_id
  AND  SYSDATE BETWEEN ab.EFFECTIVE_START_DATE AND ab.EFFECTIVE_END_DATE
ORDER BY ab.BAND_START;
```

### Filtros comuns
- `ABSENCE_PLAN_ID = :p_plan_id` — Faixas de um plano específico
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Vigentes

---

## 🔒 Observações

- As faixas são ordenadas por `BAND_START` e não devem ter gaps ou sobreposições.
- `BAND_END` nulo na última faixa indica "de X em diante" (sem limite superior).
- A taxa de acumulação (`ACCRUAL_RATE`) é definida por período conforme o `ACCRUAL_FREQUENCY` do plano.

---

## 📚 Referências

- [Oracle Docs — ANC_ACCRUAL_BANDS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancaccruralbandsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
