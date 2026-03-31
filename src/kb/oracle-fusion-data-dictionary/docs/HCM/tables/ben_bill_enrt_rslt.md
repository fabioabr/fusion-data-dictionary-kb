---
id: DOC-HCM-032
doc_type: system-doc
title: "BEN_BILL_ENRT_RSLT — Resultados de Inscrição para Cobrança"
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
  - inscricao-cobranca
  - bill-enrollment
aliases:
  - BEN_BILL_ENRT_RSLT
  - ben_bill_enrt_rslt
  - inscricao-cobranca-beneficios
  - bill-enrollment-result
  - ben-bill-enrt-rslt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BILL_ENRT_RSLT

## 📌 Visão Geral

Armazena a **vinculação entre inscrições de benefícios e cobranças**. Conecta os resultados de inscrição (`BEN_PRTT_ENRT_RSLT`) ao sistema de billing.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão financeira de benefícios:** Resultados de Inscrição para Cobrança.
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
| 1 | BILL_ENRT_RSLT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 85% |
| 2 | PRTT_ENRT_RSLT_ID | NUMBER(18) | NOT NULL | FK | Resultado de inscrição | [[ben_prtt_enrt_rslt]] | 🟢 90% |
| 3 | BILL_CHARGE_ID | NUMBER(18) | NULL | FK | Cobrança associada | [[ben_bill_charges]] | 🟡 80% |
| 4 | BILLING_STATUS | VARCHAR2(30) | NULL | Classificação | Status de cobrança da inscrição | — | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_prtt_enrt_rslt]] — via `PRTT_ENRT_RSLT_ID` (inscricao em beneficio da cobranca)
- [[ben_bill_charges]] — via `BILL_CHARGE_ID` (cobranca vinculada a inscricao)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Inscrições com cobrança
```sql
SELECT be.PRTT_ENRT_RSLT_ID, be.BILLING_STATUS
FROM   BEN_BILL_ENRT_RSLT be;
```

### Filtros comuns
- `BILLING_STATUS = 'BILLED'` — Já cobrados

---

## 🔒 Observações

- Tabela de ligação entre inscrições e cobranças.
- Permite rastrear quais inscrições já foram cobradas.

---

## 🔗 PVOs Relacionados

### [[billchargedetailspvo|BillChargeDetailsPVO]] (HCM · BICC: 2/69)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_RELATION_ID | BenefitRelationId2 | — |
| BER_ATTRIBUTE1 | BerAttribute1 | — |
| BER_ATTRIBUTE10 | BerAttribute10 | — |
| BER_ATTRIBUTE2 | BerAttribute2 | — |
| BER_ATTRIBUTE3 | BerAttribute3 | — |
| BER_ATTRIBUTE4 | BerAttribute4 | — |
| BER_ATTRIBUTE5 | BerAttribute5 | — |
| BER_ATTRIBUTE6 | BerAttribute6 | — |
| BER_ATTRIBUTE7 | BerAttribute7 | — |
| BER_ATTRIBUTE8 | BerAttribute8 | — |
| BER_ATTRIBUTE9 | BerAttribute9 | — |
| BER_ATTRIBUTE_CATEGORY | BerAttributeCategory | — |
| BER_ATTRIBUTE_DATE1 | BerAttributeDate1 | — |
| BER_ATTRIBUTE_DATE2 | BerAttributeDate2 | — |
| BER_ATTRIBUTE_DATE3 | BerAttributeDate3 | — |
| BER_ATTRIBUTE_DATE4 | BerAttributeDate4 | — |
| BER_ATTRIBUTE_DATE5 | BerAttributeDate5 | — |
| BER_ATTRIBUTE_NUMBER1 | BerAttributeNumber1 | — |
| BER_ATTRIBUTE_NUMBER2 | BerAttributeNumber2 | — |
| BER_ATTRIBUTE_NUMBER3 | BerAttributeNumber3 | — |
| BER_ATTRIBUTE_NUMBER4 | BerAttributeNumber4 | — |
| BER_ATTRIBUTE_NUMBER5 | BerAttributeNumber5 | — |
| BILL_END_DATE | BillEndDate | — |
| BILL_ENRT_RSLT_ID | BillEnrtRsltId | ✅ |
| BILL_START_DATE | BillStartDate | — |
| BNFT_AMT | BnftAmt | — |
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| CONFIG_CHAR_1 | ConfigChar13 | — |
| CONFIG_CHAR_2 | ConfigChar23 | — |
| CONFIG_CHAR_3 | ConfigChar33 | — |
| CONFIG_CHAR_4 | ConfigChar43 | — |
| CONFIG_CHAR_5 | ConfigChar53 | — |
| CONFIG_DATE_1 | ConfigDate13 | — |
| CONFIG_DATE_2 | ConfigDate23 | — |
| CONFIG_DATE_3 | ConfigDate33 | — |
| CONFIG_DATE_4 | ConfigDate43 | — |
| CONFIG_DATE_5 | ConfigDate53 | — |
| CONFIG_NUM_1 | ConfigNum13 | — |
| CONFIG_NUM_2 | ConfigNum23 | — |
| CONFIG_NUM_3 | ConfigNum33 | — |
| CONFIG_NUM_4 | ConfigNum43 | — |
| CONFIG_NUM_5 | ConfigNum53 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| ELECTION_DATE | ElectionDate | — |
| ENRT_CVG_STRT_DT | EnrtCvgStrtDt | — |
| ENRT_CVG_THRU_DT | EnrtCvgThruDt | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| LEGAL_ENTITY_ID | LegalEntityId2 | — |
| LER_ID | LerId | — |
| LER_TYP_CD | LerTypCd | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| OIPL_ID | OiplId1 | — |
| OPT_ID | OptId1 | — |
| ORGNL_ENRT_DT | OrgnlEnrtDt | — |
| ORGNL_PRTT_ENRT_RSLT_ID | OrgnlPrttEnrtRsltId | — |
| PER_IN_LER_ID | PerInLerId | — |
| PERSON_ID | PersonId3 | — |
| PGM_ID | PgmId1 | — |
| PL_ID | PlId1 | — |
| PL_TYP_ID | PlTypId1 | — |
| PRORATE_DAYS | ProrateDays | — |
| PRORATE_PERCENT | ProratePercent | — |
| PRORATE_TYPE | ProrateType | — |
| PTIP_ID | PtipId1 | — |
| SRC_CD | SrcCd | — |
| STOP_BILL_FLAG | StopBillFlag1 | — |

---

## 📚 Referências

- [Oracle Docs — BEN_BILL_ENRT_RSLT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbillenrtrslt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
