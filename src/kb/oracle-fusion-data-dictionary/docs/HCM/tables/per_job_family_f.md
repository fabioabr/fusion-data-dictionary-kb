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
- [[per_job_family_f_tl]] — via `JOB_FAMILY_ID` (traduções da família de cargos)
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

## 🔗 PVOs Relacionados

### [[careerpreferencepvo|CareerPreferencePVO]] (HCM · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | — |
| ACTIVE_STATUS | ActiveStatus | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_FAMILY_ID | JobFamilyId | — |
| LAST_UPDATE_DATE | JobFamilyPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | JobFamilyPEOLastUpdateDate | ✅ |

### [[jobfamilyextractpvo|JobFamilyExtractPVO]] (HCM · BICC: 13/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| ACTIVE_STATUS | ActiveStatus | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_FAMILY_CODE | JobFamilyCode | ✅ |
| JOB_FAMILY_ID | JobFamilyId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

### [[jobfamilypvo|JobFamilyPVO]] (HCM · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobFamilyPEOActionOccurrenceId | — |
| ACTIVE_STATUS | JobFamilyPEOActiveStatus | — |
| BUSINESS_GROUP_ID | JobFamilyPEOBusinessGroupId | — |
| CREATED_BY | JobFamilyPEOCreatedBy | — |
| CREATION_DATE | JobFamilyPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_FAMILY_CODE | JobFamilyCode | ✅ |
| JOB_FAMILY_ID | JobFamilyId | ✅ |
| LAST_UPDATE_DATE | JobFamilyPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobFamilyPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobFamilyPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | JobFamilyPEOObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Docs — PER_JOB_FAMILY_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobfamilyf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
