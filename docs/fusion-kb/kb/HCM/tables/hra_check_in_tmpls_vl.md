---
id: DOC-HCM-136
doc_type: system-doc
title: "HRA_CHECK_IN_TMPLS_VL — Templates de Check-In (View Localized)"
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
  - performance-management
  - template-vl
  - avaliacao
  - hra
aliases:
  - HRA_CHECK_IN_TMPLS_VL
  - hra_check_in_tmpls_vl
  - hra-check-in-tmpls-vl
  - DOC-HCM-136
  - templates-de-check-in-(view-localized)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_CHECK_IN_TMPLS_VL

## 📌 Visão Geral

**View localizada** que apresenta view localizada de templates de check-in, combinando dados base (`HRA_CHECK_IN_TMPLS_B`) com traduções no idioma da sessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta localizada:** Dados com tradução automática para o idioma da sessão.
- **Interface do usuário:** Base para LOVs e telas.
- **Relatórios:** Nomes traduzidos sem necessidade de join manual.
- **Simplificação:** Abstrai a complexidade do join _B + _TL.
- **Padronização:** Abordagem consistente Oracle para multilinguismo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECK_IN_TMPL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome no idioma da sessão | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Descrição | Descrição no idioma da sessão | — | 🟡 80% |
| 4 | CODE | VARCHAR2(30) | NULL | Identificação | Código do registro | — | 🟡 80% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status do registro | — | 🟡 75% |
| 6 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início de vigência | — | 🟡 80% |
| 7 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigência | — | 🟡 80% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hra_check_in_tmpls_b]] — via `CHECK_IN_TMPL_ID` (registro base do template de check-in)

### Tabelas-filha (FK de saída)
- Por ser uma view, não possui tabelas-filha diretas.

---

## 📎 Uso Típico

### Consulta geral
```sql
SELECT v.CHECK_IN_TMPL_ID, v.NAME, v.DESCRIPTION, v.CODE
FROM   HRA_CHECK_IN_TMPLS_VL v;
```

### Filtro por status ativo
```sql
SELECT v.CHECK_IN_TMPL_ID, v.NAME
FROM   HRA_CHECK_IN_TMPLS_VL v
WHERE  v.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Esta é uma **view localizada** (_VL) — combina _B + _TL para o idioma da sessão.
- Não possui dados próprios — lê de `HRA_CHECK_IN_TMPLS_B` + `HRA_CHECK_IN_TMPLS_TL`.
- Performance pode ser ligeiramente inferior ao join direto em queries complexas.
- Ideal para LOVs (List of Values) e consultas de interface.

---

## 🔗 PVOs Relacionados

### [[checkinspvo|CheckinsPVO]] (HCM · BICC: 18/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | TemplateCheckInPEOBusinessGroupId | — |
| CHECK_IN_TEMPLATE_ID | TemplateCheckInPEOCheckInTemplateId | — |
| COMMENTS | TemplateCheckInPEOComments | ✅ |
| CREATED_BY | TemplateCheckInPEOCreatedBy | ✅ |
| CREATION_DATE | TemplateCheckInPEOCreationDate | ✅ |
| DATE_FROM | TemplateCheckInPEODateFrom | ✅ |
| DATE_TO | TemplateCheckInPEODateTo | ✅ |
| DEV_GOALS_AUTO_POPULATE_FLAG | TemplateCheckInPEODevGoalsAutoPopulateFlag | ✅ |
| DEVELOPMENT_GOALS_FLAG | TemplateCheckInPEODevelopmentGoalsFlag | ✅ |
| FREE_FORM_NOTES_FLAG | TemplateCheckInPEOFreeFormNotesFlag | — |
| GENERAL_DISCUSSION_TOPIC_FLAG | TemplateCheckInPEOGeneralDiscussionTopicFlag | ✅ |
| LAST_UPDATE_DATE | TemplateCheckInPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TemplateCheckInPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TemplateCheckInPEOLastUpdatedBy | ✅ |
| MANAGER_QUESTIONNAIRE_ID | TemplateCheckInPEOManagerQuestionnaireId | ✅ |
| NAME | TemplateCheckInPEOName | ✅ |
| PERF_GOALS_AUTO_POPULATE_FLAG | TemplateCheckInPEOPerfGoalsAutoPopulateFlag | ✅ |
| PERFORMANCE_GOALS_FLAG | TemplateCheckInPEOPerformanceGoalsFlag | ✅ |
| QUESTIONNAIRE_FLAG | TemplateCheckInPEOQuestionnaireFlag | ✅ |
| STATUS_CODE | TemplateCheckInPEOStatusCode | ✅ |
| WORKER_QUESTIONNAIRE_ID | TemplateCheckInPEOWorkerQuestionnaireId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_CHECK_IN_TMPLS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hracheckintmplsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
