---
id: DOC-HCM-134
doc_type: system-doc
title: "HRA_CHECK_IN_TMPLS_B — Templates de Check-In (Base)"
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
  - template
  - avaliacao
  - hra
aliases:
  - HRA_CHECK_IN_TMPLS_B
  - hra_check_in_tmpls_b
  - hra-check-in-tmpls-b
  - DOC-HCM-134
  - templates-de-check-in-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_CHECK_IN_TMPLS_B

## 📌 Visão Geral

Armazena as **definições base** de templates de check-in. Tabela _B (base language) contendo atributos não-traduzíveis como códigos, status e configurações estruturais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de templates de check-in:** Cadastro central de configurações.
- **Configuração estrutural:** Parâmetros base do registro.
- **Controle de versão:** Versionamento via `OBJECT_VERSION_NUMBER`.
- **Base para tradução:** Complementada por `HRA_CHECK_IN_TMPLS_TL`.
- **Governança:** Configurações auditáveis e rastreáveis.

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
| 2 | CODE | VARCHAR2(30) | NULL | Identificação | Código do registro | — | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 4 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início de vigência | — | 🟡 80% |
| 5 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigência | — | 🟡 80% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Número de versão do objeto | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_check_in_tmpls_tl]] — via `CHECK_IN_TMPL_ID` (traducoes multilingue do registro)

---

## 📎 Uso Típico

### Registros ativos
```sql
SELECT b.CHECK_IN_TMPL_ID, b.CODE, b.STATUS_CODE
FROM   HRA_CHECK_IN_TMPLS_B b
WHERE  b.STATUS_CODE = 'ACTIVE';
```

### Com tradução
```sql
SELECT b.CHECK_IN_TMPL_ID, b.CODE, tl.NAME
FROM   HRA_CHECK_IN_TMPLS_B b
JOIN   HRA_CHECK_IN_TMPLS_TL tl ON b.CHECK_IN_TMPL_ID = tl.CHECK_IN_TMPL_ID
WHERE  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- Para nomes traduzidos, juntar com `HRA_CHECK_IN_TMPLS_TL` via `CHECK_IN_TMPL_ID`.
- O `OBJECT_VERSION_NUMBER` é usado para controle de concorrência otimista.
- Views _VL unem _B + _TL automaticamente para o idioma da sessão.

---

## 🔗 PVOs Relacionados

### [[checkintemplatepvo|CheckInTemplatePVO]] (HCM · BICC: 18/87)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | CheckInTemplatePEOAttribute1 | — |
| ATTRIBUTE10 | CheckInTemplatePEOAttribute10 | — |
| ATTRIBUTE11 | CheckInTemplatePEOAttribute11 | — |
| ATTRIBUTE12 | CheckInTemplatePEOAttribute12 | — |
| ATTRIBUTE13 | CheckInTemplatePEOAttribute13 | — |
| ATTRIBUTE14 | CheckInTemplatePEOAttribute14 | — |
| ATTRIBUTE15 | CheckInTemplatePEOAttribute15 | — |
| ATTRIBUTE16 | CheckInTemplatePEOAttribute16 | — |
| ATTRIBUTE17 | CheckInTemplatePEOAttribute17 | — |
| ATTRIBUTE18 | CheckInTemplatePEOAttribute18 | — |
| ATTRIBUTE19 | CheckInTemplatePEOAttribute19 | — |
| ATTRIBUTE2 | CheckInTemplatePEOAttribute2 | — |
| ATTRIBUTE20 | CheckInTemplatePEOAttribute20 | — |
| ATTRIBUTE21 | CheckInTemplatePEOAttribute21 | — |
| ATTRIBUTE22 | CheckInTemplatePEOAttribute22 | — |
| ATTRIBUTE23 | CheckInTemplatePEOAttribute23 | — |
| ATTRIBUTE24 | CheckInTemplatePEOAttribute24 | — |
| ATTRIBUTE25 | CheckInTemplatePEOAttribute25 | — |
| ATTRIBUTE26 | CheckInTemplatePEOAttribute26 | — |
| ATTRIBUTE27 | CheckInTemplatePEOAttribute27 | — |
| ATTRIBUTE28 | CheckInTemplatePEOAttribute28 | — |
| ATTRIBUTE29 | CheckInTemplatePEOAttribute29 | — |
| ATTRIBUTE3 | CheckInTemplatePEOAttribute3 | — |
| ATTRIBUTE30 | CheckInTemplatePEOAttribute30 | — |
| ATTRIBUTE4 | CheckInTemplatePEOAttribute4 | — |
| ATTRIBUTE5 | CheckInTemplatePEOAttribute5 | — |
| ATTRIBUTE6 | CheckInTemplatePEOAttribute6 | — |
| ATTRIBUTE7 | CheckInTemplatePEOAttribute7 | — |
| ATTRIBUTE8 | CheckInTemplatePEOAttribute8 | — |
| ATTRIBUTE9 | CheckInTemplatePEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | CheckInTemplatePEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | CheckInTemplatePEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | CheckInTemplatePEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | CheckInTemplatePEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | CheckInTemplatePEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | CheckInTemplatePEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | CheckInTemplatePEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | CheckInTemplatePEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | CheckInTemplatePEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | CheckInTemplatePEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | CheckInTemplatePEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | CheckInTemplatePEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | CheckInTemplatePEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | CheckInTemplatePEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | CheckInTemplatePEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | CheckInTemplatePEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | CheckInTemplatePEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | CheckInTemplatePEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | CheckInTemplatePEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | CheckInTemplatePEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | CheckInTemplatePEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | CheckInTemplatePEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | CheckInTemplatePEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | CheckInTemplatePEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | CheckInTemplatePEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | CheckInTemplatePEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | CheckInTemplatePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | CheckInTemplatePEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | CheckInTemplatePEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | CheckInTemplatePEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | CheckInTemplatePEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | CheckInTemplatePEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | CheckInTemplatePEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | CheckInTemplatePEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | CheckInTemplatePEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | CheckInTemplatePEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | CheckInTemplatePEOBusinessGroupId | — |
| CHECK_IN_TEMPLATE_ID | CheckInTemplatePEOCheckInTemplateId | ✅ |
| CREATED_BY | CheckInTemplatePEOCreatedBy | ✅ |
| CREATION_DATE | CheckInTemplatePEOCreationDate | ✅ |
| DATE_FROM | CheckInTemplatePEODateFrom | ✅ |
| DATE_TO | CheckInTemplatePEODateTo | ✅ |
| DEV_GOALS_AUTO_POPULATE_FLAG | CheckInTemplatePEODevGoalsAutoPopulateFlag | ✅ |
| DEVELOPMENT_GOALS_FLAG | CheckInTemplatePEODevelopmentGoalsFlag | ✅ |
| FREE_FORM_NOTES_FLAG | CheckInTemplatePEOFreeFormNotesFlag | — |
| GENERAL_DISCUSSION_TOPIC_FLAG | CheckInTemplatePEOGeneralDiscussionTopicFlag | ✅ |
| INCLUDE_IN_PERF_DOC_FLAG | CheckInTemplatePEOIncludeInPerfDocFlag | ✅ |
| LAST_UPDATE_DATE | CheckInTemplatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CheckInTemplatePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CheckInTemplatePEOLastUpdatedBy | ✅ |
| MANAGER_QUESTIONNAIRE_ID | CheckInTemplatePEOManagerQuestionnaireId | ✅ |
| OBJECT_VERSION_NUMBER | CheckInTemplatePEOObjectVersionNumber | — |
| PERF_GOALS_AUTO_POPULATE_FLAG | CheckInTemplatePEOPerfGoalsAutoPopulateFlag | ✅ |
| PERFORMANCE_GOALS_FLAG | CheckInTemplatePEOPerformanceGoalsFlag | ✅ |
| QUESTIONNAIRE_FLAG | CheckInTemplatePEOQuestionnaireFlag | ✅ |
| STATUS_CODE | CheckInTemplatePEOStatusCode | ✅ |
| WORKER_QUESTIONNAIRE_ID | CheckInTemplatePEOWorkerQuestionnaireId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HRA_CHECK_IN_TMPLS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hracheckintmplsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
