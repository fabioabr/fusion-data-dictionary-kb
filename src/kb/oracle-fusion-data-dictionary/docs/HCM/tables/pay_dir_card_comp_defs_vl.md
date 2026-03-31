---
id: DOC-HCM-566
doc_type: system-doc
title: "PAY_DIR_CARD_COMP_DEFS_VL — Definicoes de Componentes (View Localizada)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - payroll
  - comp-defs-vl
  - view-localizada
  - pay-comp-defs-vl
aliases:
  - PAY_DIR_CARD_COMP_DEFS_VL
  - pay_dir_card_comp_defs_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DIR_CARD_COMP_DEFS_VL

## 📌 Visão Geral

**View localizada** que combina as definicoes de componentes de cartao com suas traducoes no idioma da sessao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas simplificadas de definicoes de componentes
- Uso em interfaces de configuracao de cartoes

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DIR_CARD_COMP_DEF_ID | NUMBER(18) | NOT NULL | PK | Identificador da definicao | --- | 🟢 95% |
| 2 | DIR_CARD_DEFINITION_ID | NUMBER(18) | NOT NULL | FK | ID da definicao do cartao | --- | 🟢 85% |
| 3 | COMPONENT_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome traduzido do componente | --- | 🟢 85% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- --- View, sem filhas diretas

---

## 📎 Uso Típico

### Definicoes de componentes com nome traduzido
```sql
SELECT vl.DIR_CARD_COMP_DEF_ID, vl.COMPONENT_NAME
FROM   PAY_DIR_CARD_COMP_DEFS_VL vl
WHERE  vl.DIR_CARD_DEFINITION_ID = :p_def_id
  AND  SYSDATE BETWEEN vl.EFFECTIVE_START_DATE AND vl.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Esta eh uma view (VL = View Localizada), nao uma tabela fisica.

---

## 🔗 PVOs Relacionados

### [[calculationcomponentpvo|CalculationComponentPVO]] (HCM · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSOCIABLE_TERM | DIRCardCompDefPEOAssociableTerm | — |
| ASSOCIABLE_TRU | DIRCardCompDefPEOAssociableTru | — |
| BASE_COMPONENT_NAME | DIRCardCompDefPEOBaseComponentName | ✅ |
| BREAKDOWN_COMPONENT_FLAG | DIRCardCompDefPEOBreakdownComponentFlag | — |
| COMPONENT_NAME | DIRCardCompDefPEOComponentName | ✅ |
| DEDUCTION_GROUP_ID | DIRCardCompDefPEODeductionGroupId | — |
| DEDUCTION_TYPE_ID | DIRCardCompDefPEODeductionTypeId | — |
| DEFAULTING_TRU_COMP_FLAG | DIRCardCompDefPEODefaultingTruCompFlag | — |
| DIR_CARD_COMP_DEF_ID | DirCardCompDefId | ✅ |
| DIR_CARD_DEFINITION_ID | DIRCardCompDefPEODirCardDefinitionId | — |
| EFFECTIVE_END_DATE | DIRCardCompDefPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | DIRCardCompDefPEOEffectiveStartDate | ✅ |
| ELEMENT_TYPE_ID | DIRCardCompDefPEOElementTypeId | — |
| LEGISLATION_CODE | DIRCardCompDefPEOLegislationCode | — |
| LEGISLATIVE_DATA_GROUP_ID | DIRCardCompDefPEOLegislativeDataGroupId | — |
| MULTIPLE_ALLOWED | DIRCardCompDefPEOMultipleAllowed | — |
| OBJECT_VERSION_NUMBER | DIRCardCompDefPEOObjectVersionNumber | — |
| REQUIRED | DIRCardCompDefPEORequired | — |

---

## 📚 Referências

- [Oracle Docs — PAY_DIR_CARD_COMP_DEFS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydircardcompdefsvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
