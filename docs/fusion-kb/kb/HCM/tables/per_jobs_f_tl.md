---
id: DOC-HCM-667
doc_type: system-doc
title: "PER_JOBS_F_TL — Cargos (Traduções)"
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
  - traducoes
  - jobs-tl
aliases:
  - PER_JOBS_F_TL
  - per_jobs_f_tl
  - per-jobs-f-tl
  - cargos-(traduções)
  - per-jobs-f-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOBS_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes dos cargos em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe cargos no idioma do usuário.
- **Relatórios localizados** — suporte multilíngue para relatórios organizacionais.
- **Self-service** — interface traduzida.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do cargo | PER_JOBS_F | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | JOB_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do cargo | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_jobs_f]] — via `JOB_ID` (tabela base do cargo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Cargos em português
```sql
SELECT tl.JOB_ID, tl.JOB_NAME
FROM   PER_JOBS_F_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `JOB_ID` + `LANGUAGE`.
---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | JobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | JobTranslationPEOJobId | — |
| LANGUAGE | JobTranslationPEOLanguage | — |
| NAME | JobTranslationPEOName | ✅ |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 6/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | JobMgrTranslationPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | JobMgrTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | JobMgrTranslationPEOJobId | ✅ |
| LANGUAGE | JobMgrTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | JobMgrTranslationPEOLastUpdateDate | ✅ |
| NAME | JobMgrTranslationPEOName | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 3/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | JobMgrTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobMgrTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | JobMgrTranslationPEOJobId | — |
| LANGUAGE | JobMgrTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | JobMgrTranslationPEOLastUpdateDate | ✅ |
| NAME | JobMgrTranslationPEOName | ✅ |

### [[jobextractpvo|JobExtractPVO]] (HCM · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JobTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | JobTranslationPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | JobTranslationPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | JobTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | JobTranslationPEOJobId | ✅ |
| LANGUAGE | JobTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | JobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JobTranslationPEOLastUpdatedBy | ✅ |
| NAME | JobTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | JobTranslationPEOObjectVersionNumber | ✅ |
| SOURCE_LANG | JobTranslationPEOSourceLang | ✅ |

### [[jobpvo|JobPVO]] (HCM · BICC: 10/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JobTranslationPEOCreatedBy | — |
| CREATION_DATE | JobTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | BenchmarkJobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | JobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ProgressionJobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BenchmarkJobTranslationPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobTranslationPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ProgressionJobTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | BenchmarkJobTranslationPEOJobId | — |
| JOB_ID | JobTranslationPEOJobId | — |
| JOB_ID | ProgressionJobTranslationPEOJobId | — |
| LANGUAGE | BenchmarkJobTranslationPEOLanguage | — |
| LANGUAGE | JobTranslationPEOLanguage | ✅ |
| LANGUAGE | ProgressionJobTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | BenchmarkJobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | JobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ProgressionJobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobTranslationPEOLastUpdatedBy | — |
| NAME | BenchmarkJobTranslationPEOName | ✅ |
| NAME | JobTranslationPEOName | ✅ |
| NAME | ProgressionJobTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | JobTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | JobTranslationPEOSourceLang | — |

### [[jobpvoviewall|JobPVOViewAll]] (HCM · BICC: 7/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JobTranslationPEOCreatedBy | — |
| CREATION_DATE | JobTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | BenchmarkJobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | JobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | ProgressionJobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BenchmarkJobTranslationPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobTranslationPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ProgressionJobTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | BenchmarkJobTranslationPEOJobId | — |
| JOB_ID | JobTranslationPEOJobId | — |
| JOB_ID | ProgressionJobTranslationPEOJobId | — |
| LANGUAGE | BenchmarkJobTranslationPEOLanguage | — |
| LANGUAGE | JobTranslationPEOLanguage | — |
| LANGUAGE | ProgressionJobTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | BenchmarkJobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | JobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ProgressionJobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobTranslationPEOLastUpdatedBy | — |
| NAME | BenchmarkJobTranslationPEOName | — |
| NAME | JobTranslationPEOName | ✅ |
| NAME | ProgressionJobTranslationPEOName | — |
| OBJECT_VERSION_NUMBER | JobTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | JobTranslationPEOSourceLang | — |

### [[jobrefpvo|JobRefPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JobTranslationPEOCreatedBy | — |
| CREATION_DATE | JobTranslationPEOCreationDate | — |
| EFFECTIVE_END_DATE | JobTranslationPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobTranslationPEOEffectiveStartDate | ✅ |
| JOB_ID | JobTranslationPEOJobId | — |
| LANGUAGE | JobTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | JobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobTranslationPEOLastUpdatedBy | — |
| NAME | JobTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | JobTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | JobTranslationPEOSourceLang | — |

### [[jobtranslationpvo|JobTranslationPVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JobTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | JobTranslationPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_ID | JobId | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | JobTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobTranslationPEOLastUpdatedBy | ✅ |
| NAME | JobTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | JobTranslationPEOObjectVersionNumber | — |
| SOURCE_LANG | JobTranslationPEOSourceLang | ✅ |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | JobTranslationMgrPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobTranslationMgrPEOEffectiveStartDate | ✅ |
| JOB_ID | JobTranslationMgrPEOJobId | — |
| LANGUAGE | JobTranslationMgrPEOLanguage | — |
| NAME | JobTranslationMgrPEOName | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_JOBS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
