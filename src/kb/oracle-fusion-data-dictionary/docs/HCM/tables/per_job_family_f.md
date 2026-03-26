---
id: DOC-HCM-670
doc_type: system-doc
title: "PER_JOB_FAMILY_F — Famílias de Cargos"
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
  - workforce-management
  - familias-cargos
  - job-families
aliases:
  - PER_JOB_FAMILY_F
  - per_job_family_f
  - per-job-family-f
  - famílias-de-cargos
  - per-job-family-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOB_FAMILY_F

## 📌 Visão Geral

Armazena as **famílias de cargos** da organização, com vigência temporal. Famílias agrupam cargos relacionados funcionalmente para fins de classificação, carreira e relatórios.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Agrupamento funcional** — agrupa cargos semelhantes em famílias (TI, Finanças, RH, etc.).
- **Planejamento de carreira** — define as famílias para trilhas de carreira.
- **Relatórios** — análise de workforce por família de cargo.
- **Remuneração** — políticas de compensação podem variar por família.
- **Recrutamento** — perfis de vaga agrupados por família.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_FAMILY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da família | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | JOB_FAMILY_CODE | VARCHAR2(30) | NULL | Identificação | Código da família | — | 🟢 85% |
| 5 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se está ativa (Y/N) | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de famílias de cargos.

### Tabelas-filha (FK de saída)
- [[per_job_family_f_tl]] — via `JOB_FAMILY_ID` (traduÃ§Ãµes da famÃ­lia de cargos)
- [[per_jobs_f]] — via `JOB_FAMILY_ID` (cargos nesta família)

---

## 📎 Uso Típico

### Famílias de cargos ativas
```sql
SELECT pjf.JOB_FAMILY_ID, pjf.JOB_FAMILY_CODE, pjf.ACTIVE_STATUS
FROM   PER_JOB_FAMILY_F pjf
WHERE  pjf.ACTIVE_STATUS = 'Y'
  AND  SYSDATE BETWEEN pjf.EFFECTIVE_START_DATE AND pjf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Famílias ativas
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Famílias agrupam cargos relacionados (ex.: família 'Tecnologia' agrupa Analista, Desenvolvedor, Arquiteto).
- Fundamental para relatórios de headcount e custo por área funcional.
---

## 📚 Referências

- [Oracle Docs — PER_JOB_FAMILY_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobfamilyf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
