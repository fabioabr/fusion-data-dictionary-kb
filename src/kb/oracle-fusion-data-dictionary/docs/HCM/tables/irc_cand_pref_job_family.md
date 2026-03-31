---
id: DOC-HCM-465
doc_type: system-doc
title: "IRC_CAND_PREF_JOB_FAMILY — Familias de Cargo Preferidas"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - candidate-job-family
  - irc-recruiting
aliases:
  - IRC_CAND_PREF_JOB_FAMILY
  - irc_cand_pref_job_family
  - cand-pref-job-family
  - cand-pref-hcm
  - irc-cand-pref-job-family
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAND_PREF_JOB_FAMILY

## Visao Geral

Armazena **familias de cargo** preferidas por candidatos. Vincula preferencias a categorias funcionais.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Matching funcional:** Filtrar candidatos por familia de cargo.
- **Recomendacao de vagas:** Sugerir vagas alinhadas.
- **Analise de mercado:** Areas funcionais mais atrativas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAND_PREF_JOB_FAMILY_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | CAND_PREFERENCE_ID | NUMBER(18) | NOT NULL | FK | Preferencia | IRC_CAND_PREFERENCES | 🟢 85% |
| 3 | JOB_FAMILY_ID | NUMBER(18) | NOT NULL | FK | Familia de cargo | — | 🟢 80% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_cand_preferences]] — via `CAND_PREFERENCE_ID` (preferencia do candidato por familia de cargo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Familias de cargo preferidas
```sql
SELECT pjf.JOB_FAMILY_ID
FROM   IRC_CAND_PREF_JOB_FAMILY pjf
JOIN   IRC_CAND_PREFERENCES cp ON cp.CAND_PREFERENCE_ID = pjf.CAND_PREFERENCE_ID
WHERE  cp.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `JOB_FAMILY_ID = :id` — Por familia
---

## Observacoes

- Tabela associativa entre preferencias e familias de cargo.
---

## Referencias

- [Oracle Docs -- IRC_CAND_PREF_JOB_FAMILY](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccandprefjobfamily.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[candidatepreferencespvo|CandidatePreferencesPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CAND_PREF_ID | CandPrefJobFamilyPEOCandPrefId | — |
| CREATED_BY | CandPrefJobFamilyPEOCreatedBy | — |
| CREATION_DATE | CandPrefJobFamilyPEOCreationDate | — |
| JOB_FAMILY_ID | CandPrefJobFamilyPEOJobFamilyId | ✅ |
| LAST_UPDATE_DATE | CandPrefJobFamilyPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CandPrefJobFamilyPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CandPrefJobFamilyPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | CandPrefJobFamilyPEOObjectVersionNumber | — |
| PREF_JOB_FAMILY_ID | PrefJobFamilyId | — |
