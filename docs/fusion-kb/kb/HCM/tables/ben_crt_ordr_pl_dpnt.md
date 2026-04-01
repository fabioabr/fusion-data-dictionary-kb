---
id: DOC-HCM-036
doc_type: system-doc
title: "BEN_CRT_ORDR_PL_DPNT — Planos e Dependentes de Ordens Judiciais"
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
  - planos-dependentes-ordem
  - court-order-plans
aliases:
  - BEN_CRT_ORDR_PL_DPNT
  - ben_crt_ordr_pl_dpnt
  - planos-dependentes-ordem
  - court-order-plan-dpnt
  - ben-crt-ordr-pl-dpnt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_CRT_ORDR_PL_DPNT

## 📌 Visão Geral

Armazena os **planos e dependentes** especificados em ordens judiciais de benefícios. Detalha quais planos e quais dependentes devem ser cobertos conforme determinação judicial.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento da ordem:** Especifica planos e dependentes impactados.
- **Cobertura obrigatória:** Garante que dependentes judicialmente determinados sejam cobertos.
- **Auditoria:** Rastreabilidade de cobertura por ordem judicial.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CRT_ORDR_PL_DPNT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 85% |
| 2 | CRT_ORDR_ID | NUMBER(18) | NOT NULL | FK | Ordem judicial | [[ben_crt_ordr_f]] | 🟢 90% |
| 3 | PL_ID | NUMBER(18) | NULL | FK | Plano de benefício | [[ben_pl_f]] | 🟡 80% |
| 4 | DPNT_PERSON_ID | NUMBER(18) | NULL | FK | Dependente | [[per_all_people_f]] | 🟡 80% |
| 5 | COVERAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de cobertura | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_crt_ordr_f]] — via `CRT_ORDR_ID` (ordem judicial do dependente de beneficio)
- [[ben_pl_f]] — via `PL_ID` (plano de beneficio da ordem judicial)
- [[per_all_people_f]] — via `DPNT_PERSON_ID` (dependente na ordem judicial de beneficio)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Consulta de planos e dependentes de ordens judiciais
```sql
SELECT * FROM BEN_CRT_ORDR_PL_DPNT
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Planos e Dependentes de Ordens Judiciais).

---

## 🔗 PVOs Relacionados

### [[courtorderpvo|CourtOrderPVO]] (HCM · BICC: 15/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CONFIG_CHAR_1 | ConfigChar1 | — |
| CONFIG_CHAR_10 | ConfigChar10 | — |
| CONFIG_CHAR_2 | ConfigChar2 | — |
| CONFIG_CHAR_3 | ConfigChar3 | — |
| CONFIG_CHAR_4 | ConfigChar4 | — |
| CONFIG_CHAR_5 | ConfigChar5 | — |
| CONFIG_CHAR_6 | ConfigChar6 | — |
| CONFIG_CHAR_7 | ConfigChar7 | — |
| CONFIG_CHAR_8 | ConfigChar8 | — |
| CONFIG_CHAR_9 | ConfigChar9 | — |
| CONFIG_DATE_1 | ConfigDate1 | — |
| CONFIG_DATE_10 | ConfigDate10 | — |
| CONFIG_DATE_2 | ConfigDate2 | — |
| CONFIG_DATE_3 | ConfigDate3 | — |
| CONFIG_DATE_4 | ConfigDate4 | — |
| CONFIG_DATE_5 | ConfigDate5 | — |
| CONFIG_DATE_6 | ConfigDate6 | — |
| CONFIG_DATE_7 | ConfigDate7 | — |
| CONFIG_DATE_8 | ConfigDate8 | — |
| CONFIG_DATE_9 | ConfigDate9 | — |
| CONFIG_ID_1 | ConfigId1 | — |
| CONFIG_ID_10 | ConfigId10 | — |
| CONFIG_ID_2 | ConfigId2 | — |
| CONFIG_ID_3 | ConfigId3 | — |
| CONFIG_ID_4 | ConfigId4 | — |
| CONFIG_ID_5 | ConfigId5 | — |
| CONFIG_ID_6 | ConfigId6 | — |
| CONFIG_ID_7 | ConfigId7 | — |
| CONFIG_ID_8 | ConfigId8 | — |
| CONFIG_ID_9 | ConfigId9 | — |
| CONFIG_NUM_1 | ConfigNum1 | — |
| CONFIG_NUM_10 | ConfigNum10 | — |
| CONFIG_NUM_2 | ConfigNum2 | — |
| CONFIG_NUM_3 | ConfigNum3 | — |
| CONFIG_NUM_4 | ConfigNum4 | — |
| CONFIG_NUM_5 | ConfigNum5 | — |
| CONFIG_NUM_6 | ConfigNum6 | — |
| CONFIG_NUM_7 | ConfigNum7 | — |
| CONFIG_NUM_8 | ConfigNum8 | — |
| CONFIG_NUM_9 | ConfigNum9 | — |
| CONTACT_PERSON_ID | ContactPersonId | ✅ |
| CRD_ATTRIBUTE1 | CrdAttribute1 | — |
| CRD_ATTRIBUTE10 | CrdAttribute10 | — |
| CRD_ATTRIBUTE11 | CrdAttribute11 | — |
| CRD_ATTRIBUTE12 | CrdAttribute12 | — |
| CRD_ATTRIBUTE13 | CrdAttribute13 | — |
| CRD_ATTRIBUTE14 | CrdAttribute14 | — |
| CRD_ATTRIBUTE15 | CrdAttribute15 | — |
| CRD_ATTRIBUTE16 | CrdAttribute16 | — |
| CRD_ATTRIBUTE17 | CrdAttribute17 | — |
| CRD_ATTRIBUTE18 | CrdAttribute18 | — |
| CRD_ATTRIBUTE19 | CrdAttribute19 | — |
| CRD_ATTRIBUTE2 | CrdAttribute2 | — |
| CRD_ATTRIBUTE20 | CrdAttribute20 | — |
| CRD_ATTRIBUTE21 | CrdAttribute21 | — |
| CRD_ATTRIBUTE22 | CrdAttribute22 | — |
| CRD_ATTRIBUTE23 | CrdAttribute23 | — |
| CRD_ATTRIBUTE24 | CrdAttribute24 | — |
| CRD_ATTRIBUTE25 | CrdAttribute25 | — |
| CRD_ATTRIBUTE26 | CrdAttribute26 | — |
| CRD_ATTRIBUTE27 | CrdAttribute27 | — |
| CRD_ATTRIBUTE28 | CrdAttribute28 | — |
| CRD_ATTRIBUTE29 | CrdAttribute29 | — |
| CRD_ATTRIBUTE3 | CrdAttribute3 | — |
| CRD_ATTRIBUTE30 | CrdAttribute30 | — |
| CRD_ATTRIBUTE4 | CrdAttribute4 | — |
| CRD_ATTRIBUTE5 | CrdAttribute5 | — |
| CRD_ATTRIBUTE6 | CrdAttribute6 | — |
| CRD_ATTRIBUTE7 | CrdAttribute7 | — |
| CRD_ATTRIBUTE8 | CrdAttribute8 | — |
| CRD_ATTRIBUTE9 | CrdAttribute9 | — |
| CRD_ATTRIBUTE_CATEGORY | CrdAttributeCategory | — |
| CRD_ATTRIBUTE_DATE1 | CrdAttributeDate1 | — |
| CRD_ATTRIBUTE_DATE10 | CrdAttributeDate10 | — |
| CRD_ATTRIBUTE_DATE11 | CrdAttributeDate11 | — |
| CRD_ATTRIBUTE_DATE12 | CrdAttributeDate12 | — |
| CRD_ATTRIBUTE_DATE13 | CrdAttributeDate13 | — |
| CRD_ATTRIBUTE_DATE14 | CrdAttributeDate14 | — |
| CRD_ATTRIBUTE_DATE15 | CrdAttributeDate15 | — |
| CRD_ATTRIBUTE_DATE2 | CrdAttributeDate2 | — |
| CRD_ATTRIBUTE_DATE3 | CrdAttributeDate3 | — |
| CRD_ATTRIBUTE_DATE4 | CrdAttributeDate4 | — |
| CRD_ATTRIBUTE_DATE5 | CrdAttributeDate5 | — |
| CRD_ATTRIBUTE_DATE6 | CrdAttributeDate6 | — |
| CRD_ATTRIBUTE_DATE7 | CrdAttributeDate7 | — |
| CRD_ATTRIBUTE_DATE8 | CrdAttributeDate8 | — |
| CRD_ATTRIBUTE_DATE9 | CrdAttributeDate9 | — |
| CRD_ATTRIBUTE_NUMBER1 | CrdAttributeNumber1 | — |
| CRD_ATTRIBUTE_NUMBER10 | CrdAttributeNumber10 | — |
| CRD_ATTRIBUTE_NUMBER11 | CrdAttributeNumber11 | — |
| CRD_ATTRIBUTE_NUMBER12 | CrdAttributeNumber12 | — |
| CRD_ATTRIBUTE_NUMBER13 | CrdAttributeNumber13 | — |
| CRD_ATTRIBUTE_NUMBER14 | CrdAttributeNumber14 | — |
| CRD_ATTRIBUTE_NUMBER15 | CrdAttributeNumber15 | — |
| CRD_ATTRIBUTE_NUMBER16 | CrdAttributeNumber16 | — |
| CRD_ATTRIBUTE_NUMBER17 | CrdAttributeNumber17 | — |
| CRD_ATTRIBUTE_NUMBER18 | CrdAttributeNumber18 | — |
| CRD_ATTRIBUTE_NUMBER19 | CrdAttributeNumber19 | — |
| CRD_ATTRIBUTE_NUMBER2 | CrdAttributeNumber2 | — |
| CRD_ATTRIBUTE_NUMBER20 | CrdAttributeNumber20 | — |
| CRD_ATTRIBUTE_NUMBER3 | CrdAttributeNumber3 | — |
| CRD_ATTRIBUTE_NUMBER4 | CrdAttributeNumber4 | — |
| CRD_ATTRIBUTE_NUMBER5 | CrdAttributeNumber5 | — |
| CRD_ATTRIBUTE_NUMBER6 | CrdAttributeNumber6 | — |
| CRD_ATTRIBUTE_NUMBER7 | CrdAttributeNumber7 | — |
| CRD_ATTRIBUTE_NUMBER8 | CrdAttributeNumber8 | — |
| CRD_ATTRIBUTE_NUMBER9 | CrdAttributeNumber9 | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CRT_ORDR_ID | CrtOrdrId | ✅ |
| CRT_ORDR_PL_DPNT_ID | CrtOrdrPlDpntId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORDR_END_DATE | OrdrEndDate | ✅ |
| ORDR_START_DATE | OrdrStartDate | ✅ |
| PL_ID | PlId | ✅ |
| PL_TYP_ID | PlTypId | ✅ |
| PRVNT_DEENRT_FLAG | PrvntDeenrtFlag | ✅ |
| RLSHP_TYP_CD | RlshpTypCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_CRT_ORDR_PL_DPNT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/bencrtordrpldpnt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
