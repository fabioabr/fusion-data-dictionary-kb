---
id: DOC-HCM-669
doc_type: system-doc
title: "PER_JOB_EXTRA_INFO_F — Informações Extras de Cargo"
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
  - flexfields
  - job-extra-info
aliases:
  - PER_JOB_EXTRA_INFO_F
  - per_job_extra_info_f
  - per-job-extra-info-f
  - informações-extras-de-cargo
  - per-job-extra-info-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOB_EXTRA_INFO_F

## 📌 Visão Geral

Armazena **informações adicionais** (flexfields) associadas aos cargos, com vigência temporal. Permite armazenar dados customizados que não cabem na estrutura padrão do cargo.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Dados customizados** — informações específicas da organização por cargo.
- **Flexfields** — suporte a campos descritivos flexíveis (DFF) do Oracle.
- **Extensibilidade** — permite adicionar dados sem alterar a estrutura da tabela principal.
- **Requisitos legais** — campos específicos por legislação (ex.: CBO no Brasil).
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_EXTRA_INFO_ID | NUMBER(18) | NOT NULL | PK | Identificador único da informação extra | — | 🟢 90% |
| 2 | JOB_ID | NUMBER(18) | NOT NULL | FK | Cargo associado | PER_JOBS_F | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | INFORMATION_TYPE | VARCHAR2(40) | NOT NULL | Classificação | Tipo/categoria da informação | — | 🟢 85% |
| 6 | JEI_ATTRIBUTE1 | VARCHAR2(150) | NULL | Dados | Atributo flexível 1 | — | 🟢 85% |
| 7 | JEI_ATTRIBUTE2 | VARCHAR2(150) | NULL | Dados | Atributo flexível 2 | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_jobs_f]] — via `JOB_ID` (cargo das informações extras)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Informações extras de um cargo
```sql
SELECT pjei.INFORMATION_TYPE, pjei.JEI_ATTRIBUTE1, pjei.JEI_ATTRIBUTE2
FROM   PER_JOB_EXTRA_INFO_F pjei
WHERE  pjei.JOB_ID = :p_job_id
  AND  SYSDATE BETWEEN pjei.EFFECTIVE_START_DATE AND pjei.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `INFORMATION_TYPE = :p_info_type` — Informações de um tipo específico
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Os campos JEI_ATTRIBUTE1..N são genéricos — significado depende do `INFORMATION_TYPE`.
- No Brasil, pode armazenar o código CBO (Classificação Brasileira de Ocupações).
- Suporta até 30 atributos flexíveis.
---

## 🔗 PVOs Relacionados

### [[jobextrainfoextractpvo|JobExtraInfoExtractPVO]] (HCM · BICC: 15/75)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| INFORMATION_TYPE | InformationType | ✅ |
| JEI_ATTRIBUTE1 | JeiAttribute1 | — |
| JEI_ATTRIBUTE10 | JeiAttribute10 | — |
| JEI_ATTRIBUTE11 | JeiAttribute11 | — |
| JEI_ATTRIBUTE12 | JeiAttribute12 | — |
| JEI_ATTRIBUTE13 | JeiAttribute13 | — |
| JEI_ATTRIBUTE14 | JeiAttribute14 | — |
| JEI_ATTRIBUTE15 | JeiAttribute15 | — |
| JEI_ATTRIBUTE16 | JeiAttribute16 | — |
| JEI_ATTRIBUTE17 | JeiAttribute17 | — |
| JEI_ATTRIBUTE18 | JeiAttribute18 | — |
| JEI_ATTRIBUTE19 | JeiAttribute19 | — |
| JEI_ATTRIBUTE2 | JeiAttribute2 | — |
| JEI_ATTRIBUTE20 | JeiAttribute20 | — |
| JEI_ATTRIBUTE21 | JeiAttribute21 | — |
| JEI_ATTRIBUTE22 | JeiAttribute22 | — |
| JEI_ATTRIBUTE23 | JeiAttribute23 | — |
| JEI_ATTRIBUTE24 | JeiAttribute24 | — |
| JEI_ATTRIBUTE25 | JeiAttribute25 | — |
| JEI_ATTRIBUTE26 | JeiAttribute26 | — |
| JEI_ATTRIBUTE27 | JeiAttribute27 | — |
| JEI_ATTRIBUTE28 | JeiAttribute28 | — |
| JEI_ATTRIBUTE29 | JeiAttribute29 | — |
| JEI_ATTRIBUTE3 | JeiAttribute3 | — |
| JEI_ATTRIBUTE30 | JeiAttribute30 | — |
| JEI_ATTRIBUTE4 | JeiAttribute4 | — |
| JEI_ATTRIBUTE5 | JeiAttribute5 | — |
| JEI_ATTRIBUTE6 | JeiAttribute6 | — |
| JEI_ATTRIBUTE7 | JeiAttribute7 | — |
| JEI_ATTRIBUTE8 | JeiAttribute8 | — |
| JEI_ATTRIBUTE9 | JeiAttribute9 | — |
| JEI_ATTRIBUTE_CATEGORY | JeiAttributeCategory | ✅ |
| JEI_INFORMATION1 | JeiInformation1 | — |
| JEI_INFORMATION10 | JeiInformation10 | — |
| JEI_INFORMATION11 | JeiInformation11 | — |
| JEI_INFORMATION12 | JeiInformation12 | — |
| JEI_INFORMATION13 | JeiInformation13 | — |
| JEI_INFORMATION14 | JeiInformation14 | — |
| JEI_INFORMATION15 | JeiInformation15 | — |
| JEI_INFORMATION16 | JeiInformation16 | — |
| JEI_INFORMATION17 | JeiInformation17 | — |
| JEI_INFORMATION18 | JeiInformation18 | — |
| JEI_INFORMATION19 | JeiInformation19 | — |
| JEI_INFORMATION2 | JeiInformation2 | — |
| JEI_INFORMATION20 | JeiInformation20 | — |
| JEI_INFORMATION21 | JeiInformation21 | — |
| JEI_INFORMATION22 | JeiInformation22 | — |
| JEI_INFORMATION23 | JeiInformation23 | — |
| JEI_INFORMATION24 | JeiInformation24 | — |
| JEI_INFORMATION25 | JeiInformation25 | — |
| JEI_INFORMATION26 | JeiInformation26 | — |
| JEI_INFORMATION27 | JeiInformation27 | — |
| JEI_INFORMATION28 | JeiInformation28 | — |
| JEI_INFORMATION29 | JeiInformation29 | — |
| JEI_INFORMATION3 | JeiInformation3 | — |
| JEI_INFORMATION30 | JeiInformation30 | — |
| JEI_INFORMATION4 | JeiInformation4 | — |
| JEI_INFORMATION5 | JeiInformation5 | — |
| JEI_INFORMATION6 | JeiInformation6 | — |
| JEI_INFORMATION7 | JeiInformation7 | — |
| JEI_INFORMATION8 | JeiInformation8 | — |
| JEI_INFORMATION9 | JeiInformation9 | — |
| JEI_INFORMATION_CATEGORY | JeiInformationCategory | ✅ |
| JOB_EXTRA_INFO_ID | JobExtraInfoId | ✅ |
| JOB_ID | JobId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_JOB_EXTRA_INFO_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobextrainfof.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
