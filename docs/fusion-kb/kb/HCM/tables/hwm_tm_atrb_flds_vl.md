---
id: DOC-HCM-356
doc_type: system-doc
title: "HWM_TM_ATRB_FLDS_VL — Campos de Atributos de Time Management (View Consolidada)"
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
  - time-management
  - atributos
  - campos
  - view-consolidada
aliases:
  - HWM_TM_ATRB_FLDS_VL
  - hwm_tm_atrb_flds_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_ATRB_FLDS_VL

## 📌 Visão Geral

Visão consolidada que combina dados base e traduções dos campos de atributos de Time Management.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view consolidada** que combina automaticamente a tabela `_B` (dados base) com a `_TL` (traduções) para o idioma da sessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Personalização de campos:** Configuração de campos adicionais para captura de informações específicas do negócio.
- **Flexibilidade de interface:** Definição de quais campos são exibidos e obrigatórios por contexto.
- **Referência mestre:** Manutenção de valores válidos para campos de atributo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TM_ATRBLDS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do registro | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida | — | 🟡 80% |
| 4 | CODE | VARCHAR2(30) | NULL | Classificação | Código identificador | — | 🟡 75% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 75% |
| 6 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma da tradução | — | 🟢 90% |
| 7 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma de origem da tradução | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.NAME, t.DESCRIPTION, t.CODE
FROM   HWM_TM_ATRB_FLDS_VL t
WHERE  t.LANGUAGE = USERENV('LANG')
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Tradução no idioma da sessão
- `LANGUAGE = 'PTB'` — Tradução em português brasileiro

---

## 🔒 Observações

- View consolidada: combina automaticamente dados base (`_B`) e traduções (`_TL`). Preferir em consultas de leitura.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[changeauditattributepvo|ChangeAuditAttributePVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | TmAtrbFieldVLPEOName | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFieldVLPEOTmAtrbFldId1 | — |

### [[eventattributepvo|EventAttributePVO]] (GL · BICC: 4/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOWED_SCOPE | TimeAttributeFieldVLPEOAllowedScope | — |
| ATTRIBUTE_CATEGORY | TimeAttributeFieldVLPEOAttributeCategory | — |
| ATTRIBUTE_GROUP | TimeAttributeFieldVLPEOAttributeGroup | — |
| ATTRIBUTE_TYPE | TimeAttributeFieldVLPEOAttributeType | — |
| CLASS | TimeAttributeFieldVLPEOClass11 | — |
| COMP_DISP_CODE | TimeAttributeFieldVLPEOComponentDisplayCode | — |
| CREATED_BY | TimeAttributeFieldVLPEOCreatedBy | — |
| CREATION_DATE | TimeAttributeFieldVLPEOCreationDate | — |
| DESCRIPTION | TimeAttributeFieldVLPEODescription | — |
| DISPLAY_NAME | TimeAttributeFieldVLPEODisplayName | ✅ |
| ENTERPRISE_ID | TimeAttributeFieldVLPEOEnterpriseId | — |
| GLOBAL_TM_ATRB_FLD_ID | TimeAttributeFieldVLPEOGlobalTimeAttributeFieldId | — |
| LAST_UPDATE_DATE | TimeAttributeFieldVLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TimeAttributeFieldVLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TimeAttributeFieldVLPEOLastUpdatedBy | — |
| MANDATORY_FOR_TCSMRS | TimeAttributeFieldVLPEOMandatoryForTimeConsumers | — |
| MODULE_ID | TimeAttributeFieldVLPEOModuleId | — |
| NAME | TimeAttributeFieldVLPEOName | ✅ |
| OBJECT_VERSION_NUMBER | TimeAttributeFieldVLPEOObjectVersionNumber | — |
| PARENT_TM_ATRB_FLD_ID | TimeAttributeFieldVLPEOParentTimeAttributeFieldId | — |
| TCSMRS_ID | TimeAttributeFieldVLPEOTimeConsumersId | — |
| TM_ATRB_FLD_ID | TimeAttributeFieldVLPEOTimeAttributeFieldId | ✅ |
| VALUE_LOCATION | TimeAttributeFieldVLPEOValueLocation | — |
| VALUE_SET_ID | TimeAttributeFieldVLPEOValueSetId | — |

### [[tcdmappingdetailpvo|TcdMappingDetailPVO]] (GL · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | ParentTmAtrbFldVLPEODisplayName | ✅ |
| DISPLAY_NAME | TmAtrbFldVLPEODisplayName | ✅ |
| NAME | ParentTmAtrbFldVLPEOName | ✅ |
| NAME | TmAtrbFldVLPEOName | ✅ |
| TM_ATRB_FLD_ID | ParentTmAtrbFldVLPEOTimeAttributeFieldId | — |
| TM_ATRB_FLD_ID | TmAtrbFldVLPEOTimeAttributeFieldId | — |

### [[templatelayoutcompdisplayvaluepvo|TemplateLayoutCompDisplayValuePVO]] (GL · BICC: 24/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | DepTCFParentAtrbPEODisplayName | ✅ |
| DISPLAY_NAME | DflParamTimeAtrbPEODisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO10DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO1DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO2DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO3DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO4DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO5DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO6DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO7DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO8DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO9DisplayName | ✅ |
| NAME | DepTCFParentAtrbPEOName | ✅ |
| NAME | DflParamTimeAtrbPEOName | ✅ |
| NAME | FilterAtrbPEO10Name | ✅ |
| NAME | FilterAtrbPEO1Name | ✅ |
| NAME | FilterAtrbPEO2Name | ✅ |
| NAME | FilterAtrbPEO3Name | ✅ |
| NAME | FilterAtrbPEO4Name | ✅ |
| NAME | FilterAtrbPEO5Name | ✅ |
| NAME | FilterAtrbPEO6Name | ✅ |
| NAME | FilterAtrbPEO7Name | ✅ |
| NAME | FilterAtrbPEO8Name | ✅ |
| NAME | FilterAtrbPEO9Name | ✅ |
| TM_ATRB_FLD_ID | DepTCFParentAtrbPEOTmAtrbFldId | — |
| TM_ATRB_FLD_ID | DflParamTimeAtrbPEOTmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO10TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO1TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO2TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO3TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO4TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO5TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO6TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO7TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO8TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO9TmAtrbFldId | — |

### [[templatelayoutcomponentpvo|TemplateLayoutComponentPVO]] (GL · BICC: 24/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | DepTCFParentAtrbPEODisplayName | ✅ |
| DISPLAY_NAME | DflParamTimeAtrbPEODisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO10DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO1DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO2DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO3DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO4DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO5DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO6DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO7DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO8DisplayName | ✅ |
| DISPLAY_NAME | FilterAtrbPEO9DisplayName | ✅ |
| NAME | DepTCFParentAtrbPEOName | ✅ |
| NAME | DflParamTimeAtrbPEOName | ✅ |
| NAME | FilterAtrbPEO10Name | ✅ |
| NAME | FilterAtrbPEO1Name | ✅ |
| NAME | FilterAtrbPEO2Name | ✅ |
| NAME | FilterAtrbPEO3Name | ✅ |
| NAME | FilterAtrbPEO4Name | ✅ |
| NAME | FilterAtrbPEO5Name | ✅ |
| NAME | FilterAtrbPEO6Name | ✅ |
| NAME | FilterAtrbPEO7Name | ✅ |
| NAME | FilterAtrbPEO8Name | ✅ |
| NAME | FilterAtrbPEO9Name | ✅ |
| TM_ATRB_FLD_ID | DepTCFParentAtrbPEOTmAtrbFldId | — |
| TM_ATRB_FLD_ID | DflParamTimeAtrbPEOTmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO10TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO1TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO2TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO3TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO4TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO5TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO6TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO7TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO8TmAtrbFldId | — |
| TM_ATRB_FLD_ID | FilterAtrbPEO9TmAtrbFldId | — |

### [[timeattributefieldallocationpvo|TimeAttributeFieldAllocationPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | GlobalTmAtrbFldVLPEODisplayName | — |
| DISPLAY_NAME | ParentTmAtrbFldVLPEODisplayName | — |
| NAME | GlobalTmAtrbFldVLPEOName | — |
| NAME | ParentTmAtrbFldVLPEOName | — |
| TM_ATRB_FLD_ID | GlobalTmAtrbFldVLPEOTimeAttributeFieldId | — |
| TM_ATRB_FLD_ID | ParentTmAtrbFldVLPEOTimeAttributeFieldId | — |

### [[timeattributefieldcomponentpvo|TimeAttributeFieldComponentPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | GlobalTmAtrbFldVLPEODisplayName | — |
| DISPLAY_NAME | ParentTmAtrbFldVLPEODisplayName | — |
| NAME | GlobalTmAtrbFldVLPEOName | — |
| NAME | ParentTmAtrbFldVLPEOName | — |
| TM_ATRB_FLD_ID | GlobalTmAtrbFldVLPEOTimeAttributeFieldId | — |
| TM_ATRB_FLD_ID | ParentTmAtrbFldVLPEOTimeAttributeFieldId | — |

### [[timeattributefieldcustompvo|TimeAttributeFieldCustomPVO]] (GL · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | GlobalTmAtrbFldVLPEODisplayName | ✅ |
| DISPLAY_NAME | ParentTmAtrbFldVLPEODisplayName | ✅ |
| NAME | GlobalTmAtrbFldVLPEOName | ✅ |
| NAME | ParentTmAtrbFldVLPEOName | ✅ |
| TM_ATRB_FLD_ID | GlobalTmAtrbFldVLPEOTimeAttributeFieldId | — |
| TM_ATRB_FLD_ID | ParentTmAtrbFldVLPEOTimeAttributeFieldId | — |

### [[timeattributefieldpvo|TimeAttributeFieldPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | GlobalTmAtrbFldVLPEODisplayName | — |
| DISPLAY_NAME | ParentTmAtrbFldVLPEODisplayName | — |
| NAME | GlobalTmAtrbFldVLPEOName | — |
| NAME | ParentTmAtrbFldVLPEOName | — |
| TM_ATRB_FLD_ID | GlobalTmAtrbFldVLPEOTimeAttributeFieldId | — |
| TM_ATRB_FLD_ID | ParentTmAtrbFldVLPEOTimeAttributeFieldId | — |

### [[timecategoryexprresultp|TimeCategoryExprResultP]] (GL · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | TimeAttributeFieldVLPEODisplayName | ✅ |
| NAME | TimeAttributeFieldVLPEOName | ✅ |
| TM_ATRB_FLD_ID | TimeAttributeFieldVLPEOTimeAttributeFieldId | — |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_ATRB_FLDS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_atrb_flds_vl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
