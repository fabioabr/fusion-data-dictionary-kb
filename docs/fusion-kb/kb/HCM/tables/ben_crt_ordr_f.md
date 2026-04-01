---
id: DOC-HCM-035
doc_type: system-doc
title: "BEN_CRT_ORDR_F — Ordens Judiciais de Benefícios"
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
  - ordens-judiciais
  - court-orders
  - compliance
aliases:
  - BEN_CRT_ORDR_F
  - ben_crt_ordr_f
  - ordens-judiciais-beneficios
  - court-orders
  - ben-crt-ordr
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_CRT_ORDR_F

## 📌 Visão Geral

Armazena as **ordens judiciais** (court orders) que impactam os benefícios dos colaboradores, como ordens de penhor, pensão alimentícia ou determinações judiciais de cobertura de dependentes.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance legal:** Registro de ordens judiciais que afetam benefícios.
- **Cobertura obrigatória:** Determinações judiciais de inclusão de dependentes.
- **Auditoria:** Rastreabilidade de ações judiciais por colaborador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CRT_ORDR_ID | NUMBER(18) | NOT NULL | PK | Identificador único da ordem | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | COURT_ORDER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de ordem judicial | — | 🟡 75% |
| 4 | ORDER_DATE | DATE | NULL | Data | Data da ordem | — | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da ordem judicial de beneficio)

### Tabelas-filha (FK de saída)
- [[ben_crt_ordr_pl_dpnt]] — via `CRT_ORDR_ID` (planos/dependentes da ordem)

---

## 📎 Uso Típico

### Consulta de ordens judiciais de benefícios
```sql
SELECT * FROM BEN_CRT_ORDR_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Ordens Judiciais de Benefícios).

---

## 🔗 PVOs Relacionados

### [[courtorderpvo|CourtOrderPVO]] (HCM · BICC: 31/138)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE_1 | AddressLine1 | ✅ |
| ADDRESS_LINE_2 | AddressLine2 | ✅ |
| ADDRESS_LINE_3 | AddressLine3 | ✅ |
| ADDRESS_LINE_4 | AddressLine4 | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId1 | ✅ |
| CITY | City | ✅ |
| CONFIG_CHAR_1 | ConfigChar11 | — |
| CONFIG_CHAR_10 | ConfigChar101 | — |
| CONFIG_CHAR_2 | ConfigChar21 | — |
| CONFIG_CHAR_3 | ConfigChar31 | — |
| CONFIG_CHAR_4 | ConfigChar41 | — |
| CONFIG_CHAR_5 | ConfigChar51 | — |
| CONFIG_CHAR_6 | ConfigChar61 | — |
| CONFIG_CHAR_7 | ConfigChar71 | — |
| CONFIG_CHAR_8 | ConfigChar81 | — |
| CONFIG_CHAR_9 | ConfigChar91 | — |
| CONFIG_DATE_1 | ConfigDate11 | — |
| CONFIG_DATE_10 | ConfigDate101 | — |
| CONFIG_DATE_2 | ConfigDate21 | — |
| CONFIG_DATE_3 | ConfigDate31 | — |
| CONFIG_DATE_4 | ConfigDate41 | — |
| CONFIG_DATE_5 | ConfigDate51 | — |
| CONFIG_DATE_6 | ConfigDate61 | — |
| CONFIG_DATE_7 | ConfigDate71 | — |
| CONFIG_DATE_8 | ConfigDate81 | — |
| CONFIG_DATE_9 | ConfigDate91 | — |
| CONFIG_ID_1 | ConfigId11 | — |
| CONFIG_ID_10 | ConfigId101 | — |
| CONFIG_ID_2 | ConfigId21 | — |
| CONFIG_ID_3 | ConfigId31 | — |
| CONFIG_ID_4 | ConfigId41 | — |
| CONFIG_ID_5 | ConfigId51 | — |
| CONFIG_ID_6 | ConfigId61 | — |
| CONFIG_ID_7 | ConfigId71 | — |
| CONFIG_ID_8 | ConfigId81 | — |
| CONFIG_ID_9 | ConfigId91 | — |
| CONFIG_NUM_1 | ConfigNum11 | — |
| CONFIG_NUM_10 | ConfigNum101 | — |
| CONFIG_NUM_2 | ConfigNum21 | — |
| CONFIG_NUM_3 | ConfigNum31 | — |
| CONFIG_NUM_4 | ConfigNum41 | — |
| CONFIG_NUM_5 | ConfigNum51 | — |
| CONFIG_NUM_6 | ConfigNum61 | — |
| CONFIG_NUM_7 | ConfigNum71 | — |
| CONFIG_NUM_8 | ConfigNum81 | — |
| CONFIG_NUM_9 | ConfigNum91 | — |
| COUNTRY | Country | ✅ |
| CREATED_BY | CreatedBy1 | ✅ |
| CREATION_DATE | CreationDate1 | ✅ |
| CRT_ATTRIBUTE1 | CrtAttribute1 | — |
| CRT_ATTRIBUTE10 | CrtAttribute10 | — |
| CRT_ATTRIBUTE11 | CrtAttribute11 | — |
| CRT_ATTRIBUTE12 | CrtAttribute12 | — |
| CRT_ATTRIBUTE13 | CrtAttribute13 | — |
| CRT_ATTRIBUTE14 | CrtAttribute14 | — |
| CRT_ATTRIBUTE15 | CrtAttribute15 | — |
| CRT_ATTRIBUTE16 | CrtAttribute16 | — |
| CRT_ATTRIBUTE17 | CrtAttribute17 | — |
| CRT_ATTRIBUTE18 | CrtAttribute18 | — |
| CRT_ATTRIBUTE19 | CrtAttribute19 | — |
| CRT_ATTRIBUTE2 | CrtAttribute2 | — |
| CRT_ATTRIBUTE20 | CrtAttribute20 | — |
| CRT_ATTRIBUTE21 | CrtAttribute21 | — |
| CRT_ATTRIBUTE22 | CrtAttribute22 | — |
| CRT_ATTRIBUTE23 | CrtAttribute23 | — |
| CRT_ATTRIBUTE24 | CrtAttribute24 | — |
| CRT_ATTRIBUTE25 | CrtAttribute25 | — |
| CRT_ATTRIBUTE26 | CrtAttribute26 | — |
| CRT_ATTRIBUTE27 | CrtAttribute27 | — |
| CRT_ATTRIBUTE28 | CrtAttribute28 | — |
| CRT_ATTRIBUTE29 | CrtAttribute29 | — |
| CRT_ATTRIBUTE3 | CrtAttribute3 | — |
| CRT_ATTRIBUTE30 | CrtAttribute30 | — |
| CRT_ATTRIBUTE4 | CrtAttribute4 | — |
| CRT_ATTRIBUTE5 | CrtAttribute5 | — |
| CRT_ATTRIBUTE6 | CrtAttribute6 | — |
| CRT_ATTRIBUTE7 | CrtAttribute7 | — |
| CRT_ATTRIBUTE8 | CrtAttribute8 | — |
| CRT_ATTRIBUTE9 | CrtAttribute9 | — |
| CRT_ATTRIBUTE_CATEGORY | CrtAttributeCategory | — |
| CRT_ATTRIBUTE_DATE1 | CrtAttributeDate1 | — |
| CRT_ATTRIBUTE_DATE10 | CrtAttributeDate10 | — |
| CRT_ATTRIBUTE_DATE11 | CrtAttributeDate11 | — |
| CRT_ATTRIBUTE_DATE12 | CrtAttributeDate12 | — |
| CRT_ATTRIBUTE_DATE13 | CrtAttributeDate13 | — |
| CRT_ATTRIBUTE_DATE14 | CrtAttributeDate14 | — |
| CRT_ATTRIBUTE_DATE15 | CrtAttributeDate15 | — |
| CRT_ATTRIBUTE_DATE2 | CrtAttributeDate2 | — |
| CRT_ATTRIBUTE_DATE3 | CrtAttributeDate3 | — |
| CRT_ATTRIBUTE_DATE4 | CrtAttributeDate4 | — |
| CRT_ATTRIBUTE_DATE5 | CrtAttributeDate5 | — |
| CRT_ATTRIBUTE_DATE6 | CrtAttributeDate6 | — |
| CRT_ATTRIBUTE_DATE7 | CrtAttributeDate7 | — |
| CRT_ATTRIBUTE_DATE8 | CrtAttributeDate8 | — |
| CRT_ATTRIBUTE_DATE9 | CrtAttributeDate9 | — |
| CRT_ATTRIBUTE_NUMBER1 | CrtAttributeNumber1 | — |
| CRT_ATTRIBUTE_NUMBER10 | CrtAttributeNumber10 | — |
| CRT_ATTRIBUTE_NUMBER11 | CrtAttributeNumber11 | — |
| CRT_ATTRIBUTE_NUMBER12 | CrtAttributeNumber12 | — |
| CRT_ATTRIBUTE_NUMBER13 | CrtAttributeNumber13 | — |
| CRT_ATTRIBUTE_NUMBER14 | CrtAttributeNumber14 | — |
| CRT_ATTRIBUTE_NUMBER15 | CrtAttributeNumber15 | — |
| CRT_ATTRIBUTE_NUMBER16 | CrtAttributeNumber16 | — |
| CRT_ATTRIBUTE_NUMBER17 | CrtAttributeNumber17 | — |
| CRT_ATTRIBUTE_NUMBER18 | CrtAttributeNumber18 | — |
| CRT_ATTRIBUTE_NUMBER19 | CrtAttributeNumber19 | — |
| CRT_ATTRIBUTE_NUMBER2 | CrtAttributeNumber2 | — |
| CRT_ATTRIBUTE_NUMBER20 | CrtAttributeNumber20 | — |
| CRT_ATTRIBUTE_NUMBER3 | CrtAttributeNumber3 | — |
| CRT_ATTRIBUTE_NUMBER4 | CrtAttributeNumber4 | — |
| CRT_ATTRIBUTE_NUMBER5 | CrtAttributeNumber5 | — |
| CRT_ATTRIBUTE_NUMBER6 | CrtAttributeNumber6 | — |
| CRT_ATTRIBUTE_NUMBER7 | CrtAttributeNumber7 | — |
| CRT_ATTRIBUTE_NUMBER8 | CrtAttributeNumber8 | — |
| CRT_ATTRIBUTE_NUMBER9 | CrtAttributeNumber9 | — |
| CRT_IDENT | CrtIdent | ✅ |
| CRT_ISSNG | CrtIssng | ✅ |
| CRT_ORDR_ID | CrtOrdrId1 | ✅ |
| CRT_ORDR_STAT_CD | CrtOrdrStatCd | ✅ |
| CRT_ORDR_TYP_CD | CrtOrdrTypCd | ✅ |
| DESCRIPTION | Description | ✅ |
| DETD_QLFD_ORDR_DT | DetdQlfdOrdrDt | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELIGIBLE_DT | EligibleDt | ✅ |
| ISSUE_DT | IssueDt | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| NOTES | Notes | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| ORDR_END_DATE | OrdrEndDate1 | ✅ |
| ORDR_START_DATE | OrdrStartDate1 | ✅ |
| PASSD_FIN_ASSMNT | PassdFinAssmnt | ✅ |
| PERSON_ID | PersonId | ✅ |
| POSTAL_CODE | PostalCode | ✅ |
| RCVD_DT | RcvdDt | ✅ |
| STATE | State | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_CRT_ORDR_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/bencrtordrf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
