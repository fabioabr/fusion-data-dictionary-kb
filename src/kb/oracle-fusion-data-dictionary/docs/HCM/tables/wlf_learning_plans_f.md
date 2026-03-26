---
id: DOC-HCM-736
doc_type: system-doc
title: "WLF_LEARNING_PLANS_F — Planos de Aprendizado (Learning)"
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
  - learning
  - workforce-learning
  - planos-aprendizado
aliases:
  - WLF_LEARNING_PLANS_F
  - wlf_learning_plans_f
  - wlf-learning-plans-f
  - planos-de-aprendizado
  - learning-plans
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LEARNING_PLANS_F

## Visão Geral

Armazena os **planos de aprendizado**, que agrupam múltiplos itens de aprendizado em programas estruturados de desenvolvimento. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Programas de desenvolvimento** — agrupa cursos e treinamentos em planos coerentes.
- **Trilhas de aprendizado** — define sequências de itens de aprendizado por competência/cargo.
- **Planejamento de carreira** — planos vinculados a progressão profissional.
- **Compliance** — programas obrigatórios compostos por múltiplos treinamentos.
- **Orçamento de capacitação** — consolidação de custos por plano de aprendizado.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEARNING_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano de aprendizado | — | 🟢 85% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | PLAN_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do plano de aprendizado | — | 🟡 80% |
| 5 | PLAN_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do plano (development, compliance, etc.) | — | 🟡 75% |
| 6 | STATUS | VARCHAR2(30) | NULL | Status | Status do plano (active, inactive) | — | 🟡 80% |
| 7 | START_DATE | DATE | NULL | Data | Data de início do plano | — | 🟡 80% |
| 8 | END_DATE | DATE | NULL | Data | Data de término do plano | — | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai identificada (tabela raiz do domínio de planos).

### Tabelas-filha (FK de saída)
- [[wlf_plan_profiles_f]] — via `LEARNING_PLAN_ID` (perfis do plano)
- [[wlf_plan_records_f]] — via `LEARNING_PLAN_ID` (registros de execução do plano)

---

## Uso Típico

### Planos de aprendizado ativos
```sql
SELECT lp.PLAN_NAME, lp.PLAN_TYPE, lp.STATUS, lp.START_DATE, lp.END_DATE
FROM   WLF_LEARNING_PLANS_F lp
WHERE  lp.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN lp.EFFECTIVE_START_DATE AND lp.EFFECTIVE_END_DATE
ORDER BY lp.PLAN_NAME;
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Apenas planos ativos
- `PLAN_TYPE = 'COMPLIANCE'` — Apenas planos de compliance

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Um plano pode conter múltiplos itens de aprendizado via tabelas intermediárias.
- Os perfis de elegibilidade são definidos em WLF_PLAN_PROFILES_F.

---

## Referências

- [Oracle Docs — WLF_LEARNING_PLANS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlflearningplansf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
