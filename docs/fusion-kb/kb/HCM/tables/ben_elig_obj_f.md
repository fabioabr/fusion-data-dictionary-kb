---
id: DOC-HCM-041
doc_type: system-doc
title: "BEN_ELIG_OBJ_F — Objetos de Elegibilidade"
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
  - objetos-elegibilidade
  - eligibility-objects
aliases:
  - BEN_ELIG_OBJ_F
  - ben_elig_obj_f
  - objetos-elegibilidade-beneficios
  - eligibility-objects
  - ben-elig-obj
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_ELIG_OBJ_F

## 📌 Visão Geral

Armazena os **objetos de elegibilidade** individuais que representam critérios específicos (ex.: idade mínima, tempo de serviço, grupo de benefícios).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Critérios unitários:** Cada objeto representa um critério de elegibilidade.
- **Reutilização:** Objetos podem ser compartilhados entre perfis.
- **Flexibilidade:** Permite criar critérios customizados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_ELIG_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de objetos de elegibilidade
```sql
SELECT * FROM BEN_ELIG_OBJ_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Objetos de Elegibilidade).

---

## 🔗 PVOs Relacionados

### [[checkintemplateeligibilitypvo|CheckinTemplateEligibilityPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COLUMN_NAME | EligibilityObjectPEOColumnName | — |
| COLUMN_VALUE | EligibilityObjectPEOColumnValue | — |
| EFFECTIVE_END_DATE | EligibilityObjectPEOEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EligibilityObjectPEOEffectiveStartDate1 | ✅ |
| ELIG_OBJ_ID | EligibilityObjectPEOEligObjId1 | — |
| ELIG_OBJ_TYPE | EligibilityObjectPEOEligObjType | — |
| TABLE_NAME | EligibilityObjectPEOTableName | — |

### [[eligibilityobjectsextractpvo|EligibilityObjectsExtractPVO]] (HCM · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| COLUMN_NAME | ColumnName | ✅ |
| COLUMN_VALUE | ColumnValue | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELIG_OBJ_ID | EligObjId | ✅ |
| ELIG_OBJ_TYPE | EligObjType | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| TABLE_NAME | TableName | ✅ |

### [[eligibilityresultpvo|EligibilityResultPVO]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EligibilityObjectPEOBusinessGroupId | — |
| COLUMN_NAME | EligibilityObjectPEOColumnName | — |
| COLUMN_VALUE | EligibilityObjectPEOColumnValue | — |
| CREATED_BY | EligibilityObjectPEOCreatedBy | — |
| CREATION_DATE | EligibilityObjectPEOCreationDate | — |
| EFFECTIVE_END_DATE | EligibilityObjectPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EligibilityObjectPEOEffectiveStartDate | ✅ |
| ELIG_OBJ_ID | EligibilityObjectPEOEligObjId | ✅ |
| ELIG_OBJ_TYPE | EligibilityObjectPEOEligObjType | — |
| LAST_UPDATE_DATE | EligibilityObjectPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EligibilityObjectPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EligibilityObjectPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EligibilityObjectPEOObjectVersionNumber | — |
| TABLE_NAME | EligibilityObjectPEOTableName | — |

### [[eligibilityresultsdetailspvo|EligibilityResultsDetailsPVO]] (HCM · BICC: 5/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EligibilityObjectPEOBusinessGroupId | — |
| COLUMN_NAME | EligibilityObjectPEOColumnName | — |
| COLUMN_VALUE | EligibilityObjectPEOColumnValue | — |
| CREATED_BY | EligibilityObjectPEOCreatedBy | — |
| CREATION_DATE | EligibilityObjectPEOCreationDate | — |
| EFFECTIVE_END_DATE | EligibilityObjectPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EligibilityObjectPEOEffectiveStartDate | ✅ |
| ELIG_OBJ_ID | EligibilityObjectPEOEligObjId | ✅ |
| ELIG_OBJ_TYPE | EligibilityObjectPEOEligObjType | ✅ |
| LAST_UPDATE_DATE | EligibilityObjectPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EligibilityObjectPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EligibilityObjectPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EligibilityObjectPEOObjectVersionNumber | — |
| TABLE_NAME | EligibilityObjectPEOTableName | — |

### [[templateperiodpersoneligibilityresultpvo|TemplatePeriodPersonEligibilityResultPVO]] (HCM · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COLUMN_NAME | ColumnName | — |
| COLUMN_VALUE | ColumnValue | — |
| CREATED_BY | EligibilityObjectPEOCreatedBy | — |
| CREATION_DATE | EligibilityObjectPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| ELIG_OBJ_ID | EligObjId1 | — |
| ELIG_OBJ_ID | EligObjId2 | — |
| ELIG_OBJ_TYPE | EligObjType | — |
| LAST_UPDATE_DATE | EligibilityObjectPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | EligibilityObjectPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EligibilityObjectPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EligibilityObjectPEOObjectVersionNumber | — |
| TABLE_NAME | TableName | — |

---

## 📚 Referências

- [Oracle Docs — BEN_ELIG_OBJ_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/beneligobjf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
