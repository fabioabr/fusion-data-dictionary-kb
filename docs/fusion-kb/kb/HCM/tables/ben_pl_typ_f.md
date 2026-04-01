---
id: DOC-HCM-056
doc_type: system-doc
title: "BEN_PL_TYP_F — Tipos de Plano de Benefício"
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
  - benefits
  - tipos-plano
  - plan-types
aliases:
  - BEN_PL_TYP_F
  - ben_pl_typ_f
  - tipos-plano-beneficios
  - benefit-plan-types
  - ben-pl-typ
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PL_TYP_F

## 📌 Visão Geral

Armazena os **tipos de plano de benefício** (ex.: Médico, Dental, Vida, Previdência). Categoriza os planos em tipos para organização e relatórios.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Categorização:** Agrupa planos por tipo.
- **Relatórios:** Análise por categoria de benefício.
- **Configuração:** Regras comuns por tipo de plano.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de tipos de plano de benefício
```sql
SELECT * FROM BEN_PL_TYP_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Tipos de Plano de Benefício).

---

## 🔗 PVOs Relacionados

### [[plantypepvo|PlanTypePVO]] (HCM · BICC: 21/59)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADMIN_CATEGORY_CD | AdminCategoryCd | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CARRIER_PLAN_TYPE_NAME | CarrierPlanTypeName | ✅ |
| COMP_TYP_CD | CompTypCd | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GLOBAL_FLAG | GlobalFlag | ✅ |
| IVR_IDENT | IvrIdent | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LEGISLATION_SUBGROUP | LegislationSubgroup | ✅ |
| MN_ENRL_RQD_NUM | MnEnrlRqdNum | ✅ |
| MX_ENRL_ALWD_NUM | MxEnrlAlwdNum | ✅ |
| NAME | Name | ✅ |
| NO_MN_ENRL_NUM_DFND_FLAG | NoMnEnrlNumDfndFlag | ✅ |
| NO_MX_ENRL_NUM_DFND_FLAG | NoMxEnrlNumDfndFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPT_DSPLY_FMT_CD | OptDsplyFmtCd | — |
| OPT_TYP_CD | OptTypCd | ✅ |
| PL_TYP_ID | PlTypId | ✅ |
| PL_TYP_STAT_CD | PlTypStatCd | ✅ |
| PTP_ATTRIBUTE1 | PtpAttribute1 | — |
| PTP_ATTRIBUTE10 | PtpAttribute10 | — |
| PTP_ATTRIBUTE11 | PtpAttribute11 | — |
| PTP_ATTRIBUTE12 | PtpAttribute12 | — |
| PTP_ATTRIBUTE13 | PtpAttribute13 | — |
| PTP_ATTRIBUTE14 | PtpAttribute14 | — |
| PTP_ATTRIBUTE15 | PtpAttribute15 | — |
| PTP_ATTRIBUTE16 | PtpAttribute16 | — |
| PTP_ATTRIBUTE17 | PtpAttribute17 | — |
| PTP_ATTRIBUTE18 | PtpAttribute18 | — |
| PTP_ATTRIBUTE19 | PtpAttribute19 | — |
| PTP_ATTRIBUTE2 | PtpAttribute2 | — |
| PTP_ATTRIBUTE20 | PtpAttribute20 | — |
| PTP_ATTRIBUTE21 | PtpAttribute21 | — |
| PTP_ATTRIBUTE22 | PtpAttribute22 | — |
| PTP_ATTRIBUTE23 | PtpAttribute23 | — |
| PTP_ATTRIBUTE24 | PtpAttribute24 | — |
| PTP_ATTRIBUTE25 | PtpAttribute25 | — |
| PTP_ATTRIBUTE26 | PtpAttribute26 | — |
| PTP_ATTRIBUTE27 | PtpAttribute27 | — |
| PTP_ATTRIBUTE28 | PtpAttribute28 | — |
| PTP_ATTRIBUTE29 | PtpAttribute29 | — |
| PTP_ATTRIBUTE3 | PtpAttribute3 | — |
| PTP_ATTRIBUTE30 | PtpAttribute30 | — |
| PTP_ATTRIBUTE4 | PtpAttribute4 | — |
| PTP_ATTRIBUTE5 | PtpAttribute5 | — |
| PTP_ATTRIBUTE6 | PtpAttribute6 | — |
| PTP_ATTRIBUTE7 | PtpAttribute7 | — |
| PTP_ATTRIBUTE8 | PtpAttribute8 | — |
| PTP_ATTRIBUTE9 | PtpAttribute9 | — |
| PTP_ATTRIBUTE_CATEGORY | PtpAttributeCategory | ✅ |
| SHORT_CODE | ShortCode | — |
| SHORT_NAME | ShortName | — |
| SS_CATEGORY_CD | SsCategoryCd | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PL_TYP_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benpltypf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
