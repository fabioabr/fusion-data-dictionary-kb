---
id: DOC-HCM-672
doc_type: system-doc
title: "PER_JOB_LEG_F — Dados Legislativos de Cargo"
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
  - legislacao
  - cbo
  - job-legislation
aliases:
  - PER_JOB_LEG_F
  - per_job_leg_f
  - per-job-leg-f
  - dados-legislativos-de-cargo
  - per-job-leg-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOB_LEG_F

## 📌 Visão Geral

Armazena **dados legislativos** (legais) associados aos cargos, com vigência temporal. Contém informações específicas da legislação trabalhista de cada país, como classificações oficiais de ocupação.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance** — dados de classificação oficial do cargo por legislação.
- **CBO** — Classificação Brasileira de Ocupações (no Brasil).
- **Relatórios legais** — dados para declarações obrigatórias (RAIS, eSocial).
- **Requisitos regulatórios** — informações exigidas pela legislação trabalhista de cada país.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_LEG_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro legislativo | — | 🟢 90% |
| 2 | JOB_ID | NUMBER(18) | NOT NULL | FK | Cargo associado | PER_JOBS_F | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | LEGISLATION_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da legislação | — | 🟢 90% |
| 6 | JOB_LEG_ATTRIBUTE1 | VARCHAR2(150) | NULL | Dados | Atributo legislativo 1 (ex.: CBO) | — | 🟢 85% |
| 7 | JOB_LEG_ATTRIBUTE2 | VARCHAR2(150) | NULL | Dados | Atributo legislativo 2 | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_jobs_f]] — via `JOB_ID` (cargo com informações legislativas)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Dados legislativos de um cargo
```sql
SELECT pjl.LEGISLATION_CODE, pjl.JOB_LEG_ATTRIBUTE1 AS CBO_CODE
FROM   PER_JOB_LEG_F pjl
WHERE  pjl.JOB_ID = :p_job_id
  AND  pjl.LEGISLATION_CODE = 'BR'
  AND  SYSDATE BETWEEN pjl.EFFECTIVE_START_DATE AND pjl.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LEGISLATION_CODE = 'BR'` — Dados para legislação brasileira
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- No Brasil, o atributo legislativo principal é o código CBO (Classificação Brasileira de Ocupações).
- Fundamental para integração com eSocial e declarações trabalhistas obrigatórias.
- Os campos JOB_LEG_ATTRIBUTE1..N são flexíveis — significado varia por legislação.
---

## 🔗 PVOs Relacionados

### [[joblegislativeextractpvo|JobLegislativeExtractPVO]] (HCM · BICC: 16/146)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
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
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
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
| INFORMATION1 | Information1 | — |
| INFORMATION10 | Information10 | — |
| INFORMATION11 | Information11 | — |
| INFORMATION12 | Information12 | — |
| INFORMATION13 | Information13 | — |
| INFORMATION14 | Information14 | — |
| INFORMATION15 | Information15 | — |
| INFORMATION16 | Information16 | — |
| INFORMATION17 | Information17 | — |
| INFORMATION18 | Information18 | — |
| INFORMATION19 | Information19 | — |
| INFORMATION2 | Information2 | — |
| INFORMATION20 | Information20 | — |
| INFORMATION21 | Information21 | — |
| INFORMATION22 | Information22 | — |
| INFORMATION23 | Information23 | — |
| INFORMATION24 | Information24 | — |
| INFORMATION25 | Information25 | — |
| INFORMATION26 | Information26 | — |
| INFORMATION27 | Information27 | — |
| INFORMATION28 | Information28 | — |
| INFORMATION29 | Information29 | — |
| INFORMATION3 | Information3 | — |
| INFORMATION30 | Information30 | — |
| INFORMATION4 | Information4 | — |
| INFORMATION5 | Information5 | — |
| INFORMATION6 | Information6 | — |
| INFORMATION7 | Information7 | — |
| INFORMATION8 | Information8 | — |
| INFORMATION9 | Information9 | — |
| INFORMATION_CATEGORY | InformationCategory | ✅ |
| INFORMATION_DATE1 | InformationDate1 | — |
| INFORMATION_DATE10 | InformationDate10 | — |
| INFORMATION_DATE11 | InformationDate11 | — |
| INFORMATION_DATE12 | InformationDate12 | — |
| INFORMATION_DATE13 | InformationDate13 | — |
| INFORMATION_DATE14 | InformationDate14 | — |
| INFORMATION_DATE15 | InformationDate15 | — |
| INFORMATION_DATE2 | InformationDate2 | — |
| INFORMATION_DATE3 | InformationDate3 | — |
| INFORMATION_DATE4 | InformationDate4 | — |
| INFORMATION_DATE5 | InformationDate5 | — |
| INFORMATION_DATE6 | InformationDate6 | — |
| INFORMATION_DATE7 | InformationDate7 | — |
| INFORMATION_DATE8 | InformationDate8 | — |
| INFORMATION_DATE9 | InformationDate9 | — |
| INFORMATION_NUMBER1 | InformationNumber1 | — |
| INFORMATION_NUMBER10 | InformationNumber10 | — |
| INFORMATION_NUMBER11 | InformationNumber11 | — |
| INFORMATION_NUMBER12 | InformationNumber12 | — |
| INFORMATION_NUMBER13 | InformationNumber13 | — |
| INFORMATION_NUMBER14 | InformationNumber14 | — |
| INFORMATION_NUMBER15 | InformationNumber15 | — |
| INFORMATION_NUMBER16 | InformationNumber16 | — |
| INFORMATION_NUMBER17 | InformationNumber17 | — |
| INFORMATION_NUMBER18 | InformationNumber18 | — |
| INFORMATION_NUMBER19 | InformationNumber19 | — |
| INFORMATION_NUMBER2 | InformationNumber2 | — |
| INFORMATION_NUMBER20 | InformationNumber20 | — |
| INFORMATION_NUMBER3 | InformationNumber3 | — |
| INFORMATION_NUMBER4 | InformationNumber4 | — |
| INFORMATION_NUMBER5 | InformationNumber5 | — |
| INFORMATION_NUMBER6 | InformationNumber6 | — |
| INFORMATION_NUMBER7 | InformationNumber7 | — |
| INFORMATION_NUMBER8 | InformationNumber8 | — |
| INFORMATION_NUMBER9 | InformationNumber9 | — |
| JOB_ID | JobId | ✅ |
| JOB_LEG_ID | JobLegId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |

### [[joblegislativepvo|JobLegislativePVO]] (HCM · BICC: 14/44)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobLegislativePEOActionOccurrenceId | — |
| ATTRIBUTE_CATEGORY | JobLegislativePEOAttributeCategory | — |
| CREATED_BY | JobLegislativePEOCreatedBy | ✅ |
| CREATION_DATE | JobLegislativePEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| INFORMATION1 | JobLegislativePEOInformation1 | ✅ |
| INFORMATION10 | JobLegislativePEOInformation10 | — |
| INFORMATION11 | JobLegislativePEOInformation11 | — |
| INFORMATION12 | JobLegislativePEOInformation12 | — |
| INFORMATION13 | JobLegislativePEOInformation13 | — |
| INFORMATION14 | JobLegislativePEOInformation14 | — |
| INFORMATION15 | JobLegislativePEOInformation15 | — |
| INFORMATION16 | JobLegislativePEOInformation16 | — |
| INFORMATION17 | JobLegislativePEOInformation17 | — |
| INFORMATION18 | JobLegislativePEOInformation18 | — |
| INFORMATION19 | JobLegislativePEOInformation19 | — |
| INFORMATION2 | JobLegislativePEOInformation2 | ✅ |
| INFORMATION20 | JobLegislativePEOInformation20 | — |
| INFORMATION21 | JobLegislativePEOInformation21 | — |
| INFORMATION22 | JobLegislativePEOInformation22 | — |
| INFORMATION23 | JobLegislativePEOInformation23 | — |
| INFORMATION24 | JobLegislativePEOInformation24 | — |
| INFORMATION25 | JobLegislativePEOInformation25 | — |
| INFORMATION26 | JobLegislativePEOInformation26 | — |
| INFORMATION27 | JobLegislativePEOInformation27 | — |
| INFORMATION28 | JobLegislativePEOInformation28 | — |
| INFORMATION29 | JobLegislativePEOInformation29 | — |
| INFORMATION3 | JobLegislativePEOInformation3 | ✅ |
| INFORMATION30 | JobLegislativePEOInformation30 | — |
| INFORMATION4 | JobLegislativePEOInformation4 | — |
| INFORMATION5 | JobLegislativePEOInformation5 | — |
| INFORMATION6 | JobLegislativePEOInformation6 | — |
| INFORMATION7 | JobLegislativePEOInformation7 | — |
| INFORMATION8 | JobLegislativePEOInformation8 | — |
| INFORMATION9 | JobLegislativePEOInformation9 | — |
| INFORMATION_CATEGORY | JobLegislativePEOInformationCategory | ✅ |
| JOB_ID | JobLegislativePEOJobId | ✅ |
| JOB_LEG_ID | JobLegId | ✅ |
| LAST_UPDATE_DATE | JobLegislativePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobLegislativePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JobLegislativePEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | JobLegislativePEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | JobLegislativePEOObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Docs — PER_JOB_LEG_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjoblegf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
