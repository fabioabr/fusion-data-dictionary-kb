---
id: DOC-HCM-659
doc_type: system-doc
title: "PER_GRADES_F — Grades Salariais"
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
  - faixas-salariais
aliases:
  - PER_GRADES_F
  - per_grades_f
  - per-grades-f
  - grades-salariais
  - per-grades-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADES_F

## 📌 Visão Geral

Armazena as **grades (faixas) salariais** da organização, com vigência temporal. Define as faixas de remuneração associadas a cargos e posições.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de remuneração** — define as grades salariais da organização.
- **Equidade salarial** — garante consistência na remuneração por nível.
- **Progressão de carreira** — grades representam níveis na estrutura de carreira.
- **Orçamento** — base para planejamento de custos de pessoal.
- **Compliance** — transparência na política de remuneração.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da grade | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 5 | GRADE_CODE | VARCHAR2(30) | NULL | Identificação | Código da grade | — | 🟢 85% |
| 6 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se está ativa (Y/N) | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de grades salariais.

### Tabelas-filha (FK de saída)
- [[per_grades_f_tl]] — via `GRADE_ID` (traduções da grade salarial)
- [[per_grades_in_ladders_f]] — via `GRADE_ID` (grades em escadas salariais)
- [[per_grade_steps_f]] — via `GRADE_ID` (steps da grade salarial)
- [[per_all_assignments_m]] — via `GRADE_ID` (assignments nesta grade)

---

## 📎 Uso Típico

### Grades salariais ativas
```sql
SELECT pgf.GRADE_ID, pgf.GRADE_CODE, pgf.ACTIVE_STATUS
FROM   PER_GRADES_F pgf
WHERE  pgf.ACTIVE_STATUS = 'Y'
  AND  SYSDATE BETWEEN pgf.EFFECTIVE_START_DATE AND pgf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Grades ativas
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Grades vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Grades são a base da estrutura de remuneração — cada assignment referencia uma grade.
- O código da grade tipicamente reflete o nível hierárquico (ex.: G01, G02, SENIOR, DIRECTOR).
---

## 📚 Referências

- [Oracle Docs — PER_GRADES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
