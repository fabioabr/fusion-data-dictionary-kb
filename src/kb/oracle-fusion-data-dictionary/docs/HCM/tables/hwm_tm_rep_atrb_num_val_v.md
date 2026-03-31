---
id: DOC-HCM-387
doc_type: system-doc
title: "HWM_TM_REP_ATRB_NUM_VAL_V — View de Valores Numérico de Atributos Reportados"
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
  - reported-attributes
  - valores-num
  - view
aliases:
  - HWM_TM_REP_ATRB_NUM_VAL_V
  - hwm_tm_rep_atrb_num_val_v
  - hwm-tm-rep-atrb-num-val-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_ATRB_NUM_VAL_V

## 📌 Visao Geral

View que apresenta os **valores do tipo Numérico** (NUM) dos atributos de entradas reportadas de tempo. Facilita a consulta de atributos com valores numérico sem necessidade de conversão.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Consulta de atributos numérico:** acesso direto a valores numérico de entradas reportadas.
- **Relatórios:** facilita extração de atributos numérico sem conversão de tipo.
- **Integração:** fonte para sistemas que consomem atributos tipados.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador do atributo | — | 🟡 65% |
| 2 | REP_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada reportada associada | — | 🟡 65% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do atributo | — | 🟡 65% |
| 4 | NUM_VALUE | NUMBER | NULL | Dados | Valor numérico do atributo | — | 🟡 60% |
| 5 | PERSON_ID | NUMBER(18) | NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 60% |
| 6 | ENTRY_DATE | DATE | NULL | Período | Data da entrada | — | 🟡 55% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tm_rep_atrbs]] — via `REP_ATRB_ID` (atributo de reporte do valor numerico)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Consultar valores numérico de atributos reportados
```sql
SELECT v.ATTRIBUTE_NAME, v.NUM_VALUE, v.REP_ENTRY_ID
FROM   HWM_TM_REP_ATRB_NUM_VAL_V v
WHERE  v.REP_ENTRY_ID = :p_rep_entry_id;
```

### Filtros comuns
- `REP_ENTRY_ID = :p_entry_id — Filtrar por entrada`
- `ATTRIBUTE_NAME = :p_name — Por atributo`

---

## 🔒 Observacoes

- View somente leitura — não suporta DML.
- Retorna apenas atributos com valores do tipo numérico.
- Para outros tipos de valor, utilizar as views correspondentes (_DATE_VAL_V, _NUM_VAL_V, _TS_VAL_V, _VARCHAR_VAL_V).

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_REP_ATRB_NUM_VAL_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepatrbnumvalv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[attributenumericvaluepvo|AttributeNumericValuePVO]] (HCM · BICC: 6/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOWED_SCOPE | AllowedScope | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_GROUP | AttributeGroup | — |
| ATTRIBUTE_NAME | AttributeName | ✅ |
| ATTRIBUTE_NUMERIC_VALUE | AttributeNumericValue | ✅ |
| ATTRIBUTE_TYPE | AttributeType | — |
| CLASS | Class11 | — |
| COMP_DISP_CODE | ComponentDisplayCode | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | — |
| ENTERPRISE_ID | EnterpriseId | — |
| GLOBAL_TM_ATRB_FLD_ID | GlobalTimeAttributeFieldId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MANDATORY_FOR_TCSMRS | MandatoryForTimeConsumers | — |
| MODULE_ID | ModuleId | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PARENT_TM_ATRB_FLD_ID | ParentTimeAttributeFieldId | — |
| TCSMRS_ID | TimeConsumersId | — |
| TM_ATRB_FLD_ID | TimeAttributeFieldId | ✅ |
| TM_REC_ID | TimeRecordId | — |
| TM_REC_VERSION | TimeRecordVersion | — |
| TM_REP_ATRB_ID | TimeRepositoryAttributeId | ✅ |
| VALUE_LOCATION | ValueLocation | — |
| VALUE_SET_ID | ValueSetId | — |
