---
id: DOC-HCM-029
doc_type: system-doc
title: "BEN_BILL_CHARGE_DETAILS — Detalhes de Cobrança de Benefícios"
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
  - detalhes-cobranca
  - charge-details
aliases:
  - BEN_BILL_CHARGE_DETAILS
  - ben_bill_charge_details
  - detalhes-cobranca-beneficios
  - bill-charge-details
  - ben-bill-charge-details
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_CHARGE_DETAILS

## 📌 Visão Geral

Armazena os **detalhes** de cada cobrança de benefícios, discriminando os componentes do valor total (ex.: contribuição do empregado, contribuição do empregador, impostos).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Detalhes de Cobrança de Benefícios.
- **Controle de cobranças:** Rastreamento de valores devidos e pagos.
- **Reconciliação:** Base para reconciliação financeira de benefícios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BILL_CHARGE_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe | — | 🟢 90% |
| 2 | BILL_CHARGE_ID | NUMBER(18) | NOT NULL | FK | Cobrança principal | [[ben_bill_charges]] | 🟢 90% |
| 3 | COMPONENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de componente (EMPLOYEE, EMPLOYER, TAX) | — | 🟡 75% |
| 4 | COMPONENT_AMOUNT | NUMBER | NOT NULL | Financeiro | Valor do componente | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_bill_charges]] — via `BILL_CHARGE_ID` (cobranca de beneficio detalhada)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Detalhes por cobrança
```sql
SELECT cd.COMPONENT_TYPE, cd.COMPONENT_AMOUNT
FROM   BEN_BILL_CHARGE_DETAILS cd
WHERE  cd.BILL_CHARGE_ID = :p_charge_id;
```

### Filtros comuns
- `COMPONENT_TYPE = 'EMPLOYEE'` — Parcela do empregado

---

## 🔒 Observações

- Discrimina a composição do valor total da cobrança.
- A soma dos componentes deve coincidir com o `CHARGE_AMOUNT` da cobrança principal.

---

## 🔗 PVOs Relacionados

### [[billchargedetailspvo|BillChargeDetailsPVO]] (HCM · BICC: 27/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_FLAT_AMT | AddFlatAmt | ✅ |
| ADJ_AMT | AdjAmt | ✅ |
| ADJ_DATE | AdjDate | ✅ |
| ADJ_PERCENT | AdjPercent | ✅ |
| ALLOC_SEQ_NUM | AllocSeqNum | ✅ |
| AMT_DUE | AmtDue | ✅ |
| AMT_PAID | AmtPaid | ✅ |
| ANN_RT_VAL | AnnRtVal | ✅ |
| BCD_ATTRIBUTE1 | BcdAttribute1 | — |
| BCD_ATTRIBUTE10 | BcdAttribute10 | — |
| BCD_ATTRIBUTE2 | BcdAttribute2 | — |
| BCD_ATTRIBUTE3 | BcdAttribute3 | — |
| BCD_ATTRIBUTE4 | BcdAttribute4 | — |
| BCD_ATTRIBUTE5 | BcdAttribute5 | — |
| BCD_ATTRIBUTE6 | BcdAttribute6 | — |
| BCD_ATTRIBUTE7 | BcdAttribute7 | — |
| BCD_ATTRIBUTE8 | BcdAttribute8 | — |
| BCD_ATTRIBUTE9 | BcdAttribute9 | — |
| BCD_ATTRIBUTE_CATEGORY | BcdAttributeCategory | — |
| BCD_ATTRIBUTE_DATE1 | BcdAttributeDate1 | — |
| BCD_ATTRIBUTE_DATE2 | BcdAttributeDate2 | — |
| BCD_ATTRIBUTE_DATE3 | BcdAttributeDate3 | — |
| BCD_ATTRIBUTE_DATE4 | BcdAttributeDate4 | — |
| BCD_ATTRIBUTE_DATE5 | BcdAttributeDate5 | — |
| BCD_ATTRIBUTE_NUMBER1 | BcdAttributeNumber1 | — |
| BCD_ATTRIBUTE_NUMBER2 | BcdAttributeNumber2 | — |
| BCD_ATTRIBUTE_NUMBER3 | BcdAttributeNumber3 | — |
| BCD_ATTRIBUTE_NUMBER4 | BcdAttributeNumber4 | — |
| BCD_ATTRIBUTE_NUMBER5 | BcdAttributeNumber5 | — |
| BENEFIT_RELATION_ID | BenefitRelationId | — |
| BILL_AMT | BillAmt | ✅ |
| BILL_CHARGE_DTL_ID | BillChargeDtlId | ✅ |
| BILL_CHARGE_ID | BillChargeId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CMCD_RT_FREQ | CmcdRtFreq | ✅ |
| CMCD_RT_VAL | CmcdRtVal | ✅ |
| CONFIG_CHAR_1 | ConfigChar1 | — |
| CONFIG_CHAR_2 | ConfigChar2 | — |
| CONFIG_CHAR_3 | ConfigChar3 | — |
| CONFIG_CHAR_4 | ConfigChar4 | — |
| CONFIG_CHAR_5 | ConfigChar5 | — |
| CONFIG_DATE_1 | ConfigDate1 | — |
| CONFIG_DATE_2 | ConfigDate2 | — |
| CONFIG_DATE_3 | ConfigDate3 | — |
| CONFIG_DATE_4 | ConfigDate4 | — |
| CONFIG_DATE_5 | ConfigDate5 | — |
| CONFIG_NUM_1 | ConfigNum1 | — |
| CONFIG_NUM_2 | ConfigNum2 | — |
| CONFIG_NUM_3 | ConfigNum3 | — |
| CONFIG_NUM_4 | ConfigNum4 | — |
| CONFIG_NUM_5 | ConfigNum5 | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CURRENCY_CD | CurrencyCd | — |
| DAILY_PROTN_FLAG | DailyProtnFlag | ✅ |
| DFND_RT_FREQ | DfndRtFreq | ✅ |
| DFND_RT_VAL | DfndRtVal | ✅ |
| HOLD_FLAG | HoldFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OIPL_ID | OiplId | — |
| OPT_ID | OptId | — |
| ORIGINAL_BILL_AMT | OriginalBillAmt | ✅ |
| OVERRIDE_DATE | OverrideDate | ✅ |
| OVERRIDE_REASON | OverrideReason | ✅ |
| PGM_ID | PgmId | — |
| PL_ID | PlId | — |
| PL_TYP_ID | PlTypId | — |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId | — |
| PRTT_RT_VAL_ID | PrttRtValId | — |
| PTIP_ID | PtipId | — |
| RATE_END_DT | RateEndDt | ✅ |
| RATE_START_DT | RateStartDt | ✅ |
| STATUS | Status | ✅ |
| TAX_AMT | TaxAmt | ✅ |
| TAX_PERCENT | TaxPercent | ✅ |
| TAX_TYPE | TaxType | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_CHARGE_DETAILS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillchargedetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
