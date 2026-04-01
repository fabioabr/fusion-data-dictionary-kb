---
id: DOC-HCM-665
doc_type: system-doc
title: "PER_GRADE_STEPS_F_TL — Steps de Grade Salarial (Traduções)"
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
  - traducoes
  - grade-steps-tl
aliases:
  - PER_GRADE_STEPS_F_TL
  - per_grade_steps_f_tl
  - per-grade-steps-f-tl
  - steps-de-grade-salarial-(traduções)
  - per-grade-steps-f-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADE_STEPS_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes dos steps de grade salarial em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe steps no idioma do usuário.
- **Relatórios localizados** — suporte multilíngue.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_STEP_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do step | PER_GRADE_STEPS_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | STEP_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do step | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_grade_steps_f]] — via `GRADE_STEP_ID` (tabela base do step de grade salarial)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Steps em português
```sql
SELECT tl.GRADE_STEP_ID, tl.STEP_NAME
FROM   PER_GRADE_STEPS_F_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `GRADE_STEP_ID` + `LANGUAGE`.
---

## 🔗 PVOs Relacionados

### [[gradesteppvo|GradeStepPVO]] (GL · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GradeStepTranslationPEOCreatedBy | — |
| CREATION_DATE | GradeStepTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | GradeStepTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GradeStepTranslationPEOEffectiveStartDate | ✅ |
| GRADE_STEP_ID | GradeStepTranslationPEOGradeStepId | — |
| LANGUAGE | GradeStepTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | GradeStepTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradeStepTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradeStepTranslationPEOLastUpdatedBy | — |
| NAME | GradeStepTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | GradeStepTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | GradeStepTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Docs — PER_GRADE_STEPS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradestepsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
