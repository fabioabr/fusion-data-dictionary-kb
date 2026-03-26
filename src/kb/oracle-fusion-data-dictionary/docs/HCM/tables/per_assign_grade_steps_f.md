---
id: DOC-HCM-635
doc_type: system-doc
title: "PER_ASSIGN_GRADE_STEPS_F — Steps de Grade por Assignment"
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
  - compensation
  - grades
  - grade-steps
aliases:
  - PER_ASSIGN_GRADE_STEPS_F
  - per_assign_grade_steps_f
  - per-assign-grade-steps-f
  - steps-de-grade-por-assignment
  - per-assign-grade-ste
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGN_GRADE_STEPS_F

## 📌 Visão Geral

Armazena a associação entre **assignments e steps de grade salarial**, com vigência temporal. Define em qual step da escala salarial o colaborador está posicionado.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Posicionamento salarial** — define o step exato dentro da grade salarial do colaborador.
- **Progressão salarial** — rastreamento de mudanças de step ao longo do tempo.
- **Cálculo de remuneração** — base para determinação do salário por step.
- **Relatórios de compensação** — análise da distribuição de colaboradores por step.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGN_GRADE_STEP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | GRADE_STEP_ID | NUMBER(18) | NOT NULL | FK | Step de grade | PER_GRADE_STEPS_F | 🟢 90% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vÃ­nculo do step de grade salarial)
- [[per_grade_steps_f]] — via `GRADE_STEP_ID` (step de grade salarial atribuÃ­do)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Step de grade atual de um assignment
```sql
SELECT pags.GRADE_STEP_ID, pags.EFFECTIVE_START_DATE
FROM   PER_ASSIGN_GRADE_STEPS_F pags
WHERE  pags.ASSIGNMENT_ID = :p_assignment_id
  AND  SYSDATE BETWEEN pags.EFFECTIVE_START_DATE AND pags.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Step vigente
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- O histórico de steps permite rastrear a progressão salarial do colaborador.
- Integra-se com PER_GRADE_STEPS_F para obter o valor monetário do step.
---

## 📚 Referências

- [Oracle Docs — PER_ASSIGN_GRADE_STEPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassigngradestepsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
