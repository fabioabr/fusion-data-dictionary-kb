---
id: DOC-HCM-063
doc_type: system-doc
title: "BEN_PRTT_RT_VAL — Valores de Taxa do Participante"
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
  - valores-taxa
  - rate-values
  - premium
aliases:
  - BEN_PRTT_RT_VAL
  - ben_prtt_rt_val
  - valores-taxa-beneficios
  - rate-values
  - ben-prtt-rt-val
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PRTT_RT_VAL

## 📌 Visão Geral

Armazena os **valores de taxa/premium** calculados para cada participante por plano de benefício. Contém o valor efetivo que o participante paga ou contribui.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Precificação:** Valor individual de contribuição por participante.
- **Integração com folha:** Base para deduções salariais.
- **Histórico de valores:** Rastreamento de mudanças de taxa.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PRTT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de valores de taxa do participante
```sql
SELECT * FROM BEN_PRTT_RT_VAL
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Valores de Taxa do Participante).

---

## 🔗 PVOs Relacionados

### [[participantenrollmentpvo|ParticipantEnrollmentPVO]] (HCM · BICC: 28/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTL_PREM_ID | ActlPremId | — |
| ACTY_BASE_RT_ID | ActyBaseRtId | — |
| ACTY_REF_PERD_CD | ActyRefPerdCd | ✅ |
| ACTY_TYP_CD | ActyTypCd | ✅ |
| ANN_RT_VAL | AnnRtVal | ✅ |
| BNFT_RT_TYP_CD | BnftRtTypCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CMCD_REF_PERD_CD | CmcdRefPerdCd | ✅ |
| CMCD_RT_VAL | CmcdRtVal | ✅ |
| COMP_LVL_FCTR_ID | CompLvlFctrId | — |
| CONFIG_CHAR_1 | ParticipantEnrollmentRatePEOConfigChar1 | ✅ |
| CONFIG_CHAR_10 | PrvConfigChar10 | — |
| CONFIG_CHAR_6 | PrvConfigChar6 | — |
| CONFIG_CHAR_7 | PrvConfigChar7 | — |
| CONFIG_CHAR_8 | PrvConfigChar8 | — |
| CONFIG_CHAR_9 | PrvConfigChar9 | — |
| CONFIG_ID_1 | PrvConfigId1 | — |
| CONFIG_ID_2 | PrvConfigId2 | — |
| CONFIG_ID_3 | PrvConfigId3 | — |
| CONFIG_ID_4 | PrvConfigId4 | — |
| CONFIG_ID_5 | PrvConfigId5 | — |
| CONFIG_NUM_10 | PrvConfigNum10 | — |
| CONFIG_NUM_6 | PrvConfigNum6 | — |
| CONFIG_NUM_7 | PrvConfigNum7 | — |
| CONFIG_NUM_8 | PrvConfigNum8 | — |
| CONFIG_NUM_9 | PrvConfigNum9 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| CVG_AMT_CALC_MTHD_ID | CvgAmtCalcMthdId | — |
| DIR_CARD_COMP_DEF_ID | DirCardCompDefId | — |
| DIR_CARD_DEFINITION_ID | DirCardDefinitionId | — |
| DSPLY_ON_ENRT_FLAG | DsplyOnEnrtFlag | ✅ |
| ELCTNS_MADE_DT | ElctnsMadeDt | ✅ |
| ELEMENT_ENTRY_VALUE_ID | ElementEntryValueId | — |
| ENDED_PER_IN_LER_ID | EndedPerInLerId1 | — |
| ENDED_RATE_THRU_DT | EndedRateThruDt | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| MAPPING_ID | MappingId | — |
| MLT_CD | MltCd | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| ORDR_NUM | OrdrNum | ✅ |
| PER_IN_LER_ID | PerInLerId1 | — |
| PK_ID | PkId | — |
| PK_ID_TABLE_NAME | PkIdTableName | — |
| PP_IN_YR_USED_NUM | PpInYrUsedNum | ✅ |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId1 | — |
| PRTT_REIMBMT_RQST_ID | PrttReimbmtRqstId | — |
| PRTT_RMT_APRVD_FR_PYMT_ID | PrttRmtAprvdFrPymtId | — |
| PRTT_RT_VAL_ID | PrttRtValId | ✅ |
| PRTT_RT_VAL_STAT_CD | PrttRtValStatCd | ✅ |
| PRV_ATTRIBUTE1 | PrvAttribute1 | — |
| PRV_ATTRIBUTE10 | PrvAttribute10 | — |
| PRV_ATTRIBUTE11 | PrvAttribute11 | — |
| PRV_ATTRIBUTE12 | PrvAttribute12 | — |
| PRV_ATTRIBUTE13 | PrvAttribute13 | — |
| PRV_ATTRIBUTE14 | PrvAttribute14 | — |
| PRV_ATTRIBUTE15 | PrvAttribute15 | — |
| PRV_ATTRIBUTE16 | PrvAttribute16 | — |
| PRV_ATTRIBUTE17 | PrvAttribute17 | — |
| PRV_ATTRIBUTE18 | PrvAttribute18 | — |
| PRV_ATTRIBUTE19 | PrvAttribute19 | — |
| PRV_ATTRIBUTE2 | PrvAttribute2 | — |
| PRV_ATTRIBUTE20 | PrvAttribute20 | — |
| PRV_ATTRIBUTE21 | PrvAttribute21 | — |
| PRV_ATTRIBUTE22 | PrvAttribute22 | — |
| PRV_ATTRIBUTE23 | PrvAttribute23 | — |
| PRV_ATTRIBUTE24 | PrvAttribute24 | — |
| PRV_ATTRIBUTE25 | PrvAttribute25 | — |
| PRV_ATTRIBUTE26 | PrvAttribute26 | — |
| PRV_ATTRIBUTE27 | PrvAttribute27 | — |
| PRV_ATTRIBUTE28 | PrvAttribute28 | — |
| PRV_ATTRIBUTE29 | PrvAttribute29 | — |
| PRV_ATTRIBUTE3 | PrvAttribute3 | — |
| PRV_ATTRIBUTE30 | PrvAttribute30 | — |
| PRV_ATTRIBUTE4 | PrvAttribute4 | — |
| PRV_ATTRIBUTE5 | PrvAttribute5 | — |
| PRV_ATTRIBUTE6 | PrvAttribute6 | — |
| PRV_ATTRIBUTE7 | PrvAttribute7 | — |
| PRV_ATTRIBUTE8 | PrvAttribute8 | — |
| PRV_ATTRIBUTE9 | PrvAttribute9 | — |
| PRV_ATTRIBUTE_CATEGORY | PrvAttributeCategory | — |
| PRVS_RATE_STRT_DT | PrvsRateStrtDt | ✅ |
| PRVS_RATE_THRU_DT | PrvsRateThruDt | ✅ |
| RATE_DISPLAY_CD | RateDisplayCd | ✅ |
| RCRRG_FLAG | RcrrgFlag | ✅ |
| RT_END_DT | RtEndDt | ✅ |
| RT_OVRIDN_FLAG | RtOvridnFlag | ✅ |
| RT_OVRIDN_THRU_DT | RtOvridnThruDt | ✅ |
| RT_STRT_DT | RtStrtDt | ✅ |
| RT_TYP_CD | RtTypCd | ✅ |
| RT_VAL | RtVal | ✅ |
| TX_TYP_CD | TxTypCd | ✅ |
| TYPE_ID | ParticipantEnrollmentRatePEOTypeId | ✅ |
| VALUE_DEFINITION_BASE_NAME | ValueDefinitionBaseName | — |
| VDEFN_DIR_CARD_COMP_DEF_ID | VdefnDirCardCompDefId | — |
| VDEFN_ELEMENT_TYPE_ID | VdefnElementTypeId | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PRTT_RT_VAL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benprttrtval.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
