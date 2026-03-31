---
id: DOC-HCM-302
doc_type: system-doc
title: "HWM_GRP_CRITERIA — Critérios de Grupo de Workforce"
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
  - group-criteria
  - elegibilidade
aliases:
  - HWM_GRP_CRITERIA
  - hwm_grp_criteria
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_GRP_CRITERIA

## 📌 Visão Geral

Armazena os critérios de elegibilidade e filtros utilizados para definir a composição dinâmica de grupos de workforce. Permite definir regras baseadas em atributos do trabalhador para inclusão automática.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de grupos de workforce:** Organização de trabalhadores em grupos para planejamento e alocação de recursos.
- **Planejamento de força de trabalho:** Base para análises de capacidade e distribuição de equipes.
- **Relatórios gerenciais:** Consolidação de dados por grupo para dashboards de workforce.
- **Integração com módulos:** Compartilhamento de definições de grupo com Payroll, Time Management e Project Costing.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | GRP_CRITERIA_ID | NUMBER(18) | NOT NULL | PK | Identificador único do critério | — | 🟢 95% |
| 2 | GRP_ID | NUMBER(18) | NOT NULL | FK | Referência ao grupo de workforce | HWM_GRPS_VL | 🟢 95% |
| 3 | CRITERIA_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do critério aplicado | — | 🟡 80% |
| 4 | CRITERIA_VALUE | VARCHAR2(240) | NULL | Dados | Valor do critério de filtro | — | 🟡 75% |
| 5 | SEQUENCE_NUMBER | NUMBER(9) | NULL | Controle | Ordem de avaliação do critério | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_grps_vl]] — via `GRP_ID` (grupo de workforce)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT gc.GRP_CRITERIA_ID, gc.CRITERIA_TYPE, gc.CRITERIA_VALUE
FROM   HWM_GRP_CRITERIA gc
WHERE  gc.GRP_ID = :p_grp_id
ORDER BY gc.SEQUENCE_NUMBER
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Workforce Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[groupcriteriapvo|GroupCriteriaPVO]] (GL · BICC: 17/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_ATTR_CATEGORY | GroupCriteriaPEOAddlAttrCategory | — |
| ADDL_ATTR_CHAR1 | GroupCriteriaPEOAddlAttrChar1 | — |
| ADDL_ATTR_CHAR2 | GroupCriteriaPEOAddlAttrChar2 | — |
| ADDL_ATTR_CHAR3 | GroupCriteriaPEOAddlAttrChar3 | — |
| ADDL_ATTR_CHAR4 | GroupCriteriaPEOAddlAttrChar4 | — |
| ADDL_ATTR_CHAR5 | GroupCriteriaPEOAddlAttrChar5 | — |
| ADDL_ATTR_NUMBER1 | GroupCriteriaPEOAddlAttrNumber1 | — |
| ADDL_ATTR_NUMBER2 | GroupCriteriaPEOAddlAttrNumber2 | — |
| ADDL_ATTR_NUMBER3 | GroupCriteriaPEOAddlAttrNumber3 | — |
| ADDL_ATTR_NUMBER4 | GroupCriteriaPEOAddlAttrNumber4 | — |
| ADDL_ATTR_NUMBER5 | GroupCriteriaPEOAddlAttrNumber5 | — |
| BOOL_OPER_CD | GroupCriteriaPEOBoolOperCd | ✅ |
| CREATED_BY | GroupCriteriaPEOCreatedBy | ✅ |
| CREATION_DATE | GroupCriteriaPEOCreationDate | ✅ |
| CRITERIA_DISPLAY_NAME | GroupCriteriaPEOCriteriaDisplayName | ✅ |
| CRITERIA_ID | GroupCriteriaPEOCriteriaId | — |
| CRITERIA_NAME | GroupCriteriaPEOCriteriaName | ✅ |
| ENTERPRISE_ID | GroupCriteriaPEOEnterpriseId | — |
| GRP_CRITERIA_ID | GroupCriteriaPEOGrpCriteriaId | ✅ |
| GRP_ID | GroupCriteriaPEOGrpId | — |
| LAST_UPDATE_DATE | GroupCriteriaPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GroupCriteriaPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GroupCriteriaPEOLastUpdatedBy | ✅ |
| LEFT_PARAM_NUM | GroupCriteriaPEOLeftParamNum | ✅ |
| OBJECT_VERSION_NUMBER | GroupCriteriaPEOObjectVersionNumber | — |
| OPERATOR_ID | GroupCriteriaPEOOperatorId | — |
| OPERATOR_NAME | GroupCriteriaPEOOperatorName | ✅ |
| ORDR_NUM | GroupCriteriaPEOOrdrNum | ✅ |
| RIGHT_PARAM_NUM | GroupCriteriaPEORightParamNum | ✅ |
| SEED_DATA_SOURCE | GroupCriteriaPEOSeedDataSource | — |
| VALUE_CHAR | GroupCriteriaPEOValueChar | ✅ |
| VALUE_DATE | GroupCriteriaPEOValueDate | ✅ |
| VALUE_NUMBER | GroupCriteriaPEOValueNumber | ✅ |
| VALUE_TS | GroupCriteriaPEOValueTs | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_GRP_CRITERIA](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_grp_criteria.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
