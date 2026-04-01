---
id: DOC-HCM-403
doc_type: system-doc
title: "HWM_TM_REP_S_SEC_ATRBS_V — View de Atributos Seguranca (SEC) de Sumario Reportado"
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
  - time-management
  - reported-summary-attributes
  - sumario-sec
  - view
aliases:
  - HWM_TM_REP_S_SEC_ATRBS_V
  - hwm_tm_rep_s_sec_atrbs_v
  - hwm-tm-rep-s-sec-atrbs-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_S_SEC_ATRBS_V

## 📌 Visao Geral

View que consolida os **atributos de seguranca (sec)** no nivel de sumario das entradas reportadas de tempo. Foco em atributos de seguranca e controle de acesso no sumario reportado.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Consulta sumarizada:** atributos de seguranca (sec) consolidados por sumario.
- **Relatorios gerenciais:** visao agregada de atributos reportados.
- **Integracao:** fonte para sistemas consumidores de dados sumarizados.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada reportada | — | 🟡 65% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟡 65% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 60% |
| 4 | ENTRY_DATE | DATE | NULL | Periodo | Data da entrada | — | 🟡 65% |
| 5 | SUMMARY_MEASURE | NUMBER | NULL | Dados | Medida sumarizada | — | 🟡 55% |
| 6 | ATTRIBUTE_1 | VARCHAR2(240) | NULL | Dados | Atributo especifico 1 | — | 🟡 55% |
| 7 | ATTRIBUTE_2 | VARCHAR2(240) | NULL | Dados | Atributo especifico 2 | — | 🟡 55% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa dos atributos de seguranca de tempo)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Consultar atributos de sumario seguranca (sec)
```sql
SELECT v.PERSON_ID, v.ENTRY_DATE, v.SUMMARY_MEASURE,
       v.ATTRIBUTE_1, v.STATUS
FROM   HWM_TM_REP_S_SEC_ATRBS_V v
WHERE  v.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Por colaborador`
- `ENTRY_DATE BETWEEN :dt_ini AND :dt_fim — Periodo`

---

## 🔒 Observacoes

- View somente leitura — nao suporta DML.
- Especifica para atributos de seguranca (sec) no nivel de sumario.
- Nomes de colunas podem variar; validar no ambiente.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_REP_S_SEC_ATRBS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepssecatrbsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SecurityOrganizationId | ✅ |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SecurityOrganizationId | ✅ |

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SecurityOrganizationId | ✅ |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SecurityOrganizationId | ✅ |

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SimpleSecurityAttributePEOSecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SimpleSecurityAttributePEOSecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SimpleSecurityAttributePEOSecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SimpleSecurityAttributePEOSecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SimpleSecurityAttributePEOSecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SimpleSecurityAttributePEOSecurityOrganizationId | ✅ |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SecurityOrganizationId | ✅ |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SecurityOrganizationId | ✅ |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEC_ATTRIBUTE_CATEGORY | SimpleSecurityAttributePEOSecAttributeCategory | — |
| SEC_TIME_REPOS_ATRB_ID | SimpleSecurityAttributePEOSecurityTimeRepositoryAttributeId | — |
| SECURITY_BUSINESS_UNIT | SimpleSecurityAttributePEOSecurityBusinessUnit | ✅ |
| SECURITY_ENTERPRISE_ID | SimpleSecurityAttributePEOSecurityEnterpriseId | ✅ |
| SECURITY_LEG_DATA_GROUP | SimpleSecurityAttributePEOSecurityLegislativeDataGroup | ✅ |
| SECURITY_ORGANIZATION_ID | SimpleSecurityAttributePEOSecurityOrganizationId | ✅ |
