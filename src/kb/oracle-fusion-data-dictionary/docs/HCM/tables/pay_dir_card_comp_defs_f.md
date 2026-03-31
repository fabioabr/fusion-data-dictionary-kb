---
id: DOC-HCM-565
doc_type: system-doc
title: "PAY_DIR_CARD_COMP_DEFS_F — Definicoes de Componentes de Cartao"
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
  - dir-card-comp-defs
  - definicoes
  - pay-comp-defs
aliases:
  - PAY_DIR_CARD_COMP_DEFS_F
  - pay_dir_card_comp_defs_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_DIR_CARD_COMP_DEFS_F

## 📌 Visão Geral

Armazena as **definicoes de componentes** de cartoes de informacao direta. Define quais secoes (componentes) um tipo de cartao pode conter e suas regras de configuracao.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Definicao estrutural dos componentes de calculation cards
- Configuracao de regras de validacao por componente
- Template de secoes para novos cartoes

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DIR_CARD_COMP_DEF_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da definicao | --- | 🟢 90% |
| 2 | DIR_CARD_DEFINITION_ID | NUMBER(18) | NOT NULL | FK | ID da definicao do cartao | --- | 🟢 85% |
| 3 | COMPONENT_NAME | VARCHAR2(80) | NULL | Identificacao | Nome do componente | --- | 🟢 80% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Tabela de definicao de cartao (via `DIR_CARD_DEFINITION_ID`)

### Tabelas-filha (FK de saída)
- [[pay_dir_card_components_f]] --- via `DIR_CARD_COMP_DEF_ID` (componentes baseados na definição do cartão)

---

## 📎 Uso Típico

### Definicoes de componentes vigentes por cartao
```sql
SELECT cdf.DIR_CARD_COMP_DEF_ID, cdf.COMPONENT_NAME
FROM   PAY_DIR_CARD_COMP_DEFS_F cdf
WHERE  cdf.DIR_CARD_DEFINITION_ID = :p_def_id
  AND  SYSDATE BETWEEN cdf.EFFECTIVE_START_DATE AND cdf.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[dircardcompdefdpvo|DIRCardCompDefDPVO]] (HCM · BICC: 14/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSOCIABLE_TERM | DIRCardCompDefBaseDPEOAssociableTerm | ✅ |
| ASSOCIABLE_TRU | DIRCardCompDefBaseDPEOAssociableTru | ✅ |
| BASE_COMPONENT_NAME | DIRCardCompDefBaseDPEOBaseComponentName | ✅ |
| BREAKDOWN_COMPONENT_FLAG | DIRCardCompDefBaseDPEOBreakdownComponentFlag | ✅ |
| CREATED_BY | DIRCardCompDefBaseDPEOCreatedBy | — |
| CREATION_DATE | DIRCardCompDefBaseDPEOCreationDate | — |
| DEDUCTION_GROUP_ID | DIRCardCompDefBaseDPEODeductionGroupId | — |
| DEDUCTION_TYPE_ID | DIRCardCompDefBaseDPEODeductionTypeId | ✅ |
| DEFAULTING_TRU_COMP_FLAG | DIRCardCompDefBaseDPEODefaultingTruCompFlag | ✅ |
| DIR_CARD_COMP_DEF_ID | DirCardCompDefId | ✅ |
| DIR_CARD_DEFINITION_ID | DIRCardCompDefBaseDPEODirCardDefinitionId | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELEMENT_TYPE_ID | DIRCardCompDefBaseDPEOElementTypeId | ✅ |
| LAST_UPDATE_DATE | DIRCardCompDefBaseDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DIRCardCompDefBaseDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DIRCardCompDefBaseDPEOLastUpdatedBy | — |
| LEGISLATION_CODE | DIRCardCompDefBaseDPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | DIRCardCompDefBaseDPEOLegislativeDataGroupId | ✅ |
| MULTIPLE_ALLOWED | DIRCardCompDefBaseDPEOMultipleAllowed | — |
| OBJECT_VERSION_NUMBER | DIRCardCompDefBaseDPEOObjectVersionNumber | — |
| REQUIRED | DIRCardCompDefBaseDPEORequired | — |

---

## 📚 Referências

- [Oracle Docs — PAY_DIR_CARD_COMP_DEFS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paydircardcompdefsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
