---
id: DOC-HCM-590
doc_type: system-doc
title: "PAY_PAY_RELATIONSHIPS_DN — Relacionamentos de Pagamento (Desnormalizada)"
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
  - pay-relationships-dn
  - desnormalizada
  - pay-rel-dn
aliases:
  - PAY_PAY_RELATIONSHIPS_DN
  - pay_pay_relationships_dn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAY_RELATIONSHIPS_DN

## 📌 Visão Geral

Visao **desnormalizada** dos relacionamentos de pagamento. Consolida dados de `PAY_PAY_RELATIONSHIPS_F` com informacoes de pessoa e folha pre-calculadas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas otimizadas de relacionamentos de pagamento
- Relatorios rapidos de vinculo colaborador-folha
- Dashboards de headcount de folha de pagamento

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do relacionamento | --- | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | ID da pessoa | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | PAYROLL_NAME | VARCHAR2(100) | NULL | Identificacao | Nome da folha (desnormalizado) | --- | 🟡 75% |
| 4 | RELATIONSHIP_STATUS | VARCHAR2(30) | NULL | Classificacao | Status do relacionamento | --- | 🟡 75% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- --- Visao desnormalizada para relatorios

---

## 📎 Uso Típico

### Relacionamentos de pagamento por pessoa
```sql
SELECT dn.PAYROLL_RELATIONSHIP_ID, dn.PERSON_ID, dn.PAYROLL_NAME
FROM   PAY_PAY_RELATIONSHIPS_DN dn
WHERE  dn.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[calculationcomponentpvo|CalculationComponentPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayrollRelationshipPEOCreatedBy | — |
| CREATION_DATE | PayrollRelationshipPEOCreationDate | — |
| END_DATE | PayrollRelationshipPEOEndDate | — |
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipPEOLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | PayrollRelationshipPEOObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipPEOPayrollRelationshipId | — |
| PAYROLL_RELATIONSHIP_NUMBER | PayrollRelationshipPEOPayrollRelationshipNumber | — |
| PAYROLL_STAT_UNIT_ID | PayrollRelationshipPEOPayrollStatUnitId | — |
| PERSON_ID | PayrollRelationshipPEOPersonId | — |
| RELATIONSHIP_TYPE_ID | PayrollRelationshipPEORelationshipTypeId | — |
| START_DATE | PayrollRelationshipPEOStartDate | — |

### [[inboundrecordpvo|InboundRecordPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipPEOLegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | PayrollRelationshipPEOObjectVersionNumber | ✅ |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipPEOPayrollRelationshipId | ✅ |
| PAYROLL_STAT_UNIT_ID | PayrollRelationshipPEOPayrollStatUnitId | ✅ |

### [[paymentactionpvo|PaymentActionPVO]] (HCM · BICC: 2/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| END_DATE | PayrollRelationshipPEOEndDate | — |
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipPEOLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipId | ✅ |
| PAYROLL_RELATIONSHIP_NUMBER | PayrollRelationshipPEOPayrollRelationshipNumber | ✅ |
| PAYROLL_STAT_UNIT_ID | PayrollRelationshipPEOPayrollStatUnitId | — |
| PERSON_ID | PayrollRelationshipPEOPersonId | — |
| RELATIONSHIP_TYPE_ID | PayrollRelationshipPEORelationshipTypeId | — |
| START_DATE | PayrollRelationshipPEOStartDate | — |

### [[payrollrelationshipdpvo|PayrollRelationshipDPVO]] (HCM · BICC: 12/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayrollRelationshipPEOCreatedBy | ✅ |
| CREATION_DATE | PayrollRelationshipPEOCreationDate | ✅ |
| END_DATE | PayrollRelationshipPEOEndDate | ✅ |
| LAST_UPDATE_DATE | PayrollRelationshipPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollRelationshipPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PayrollRelationshipPEOLastUpdatedBy | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipPEOLegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | PayrollRelationshipPEOObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipPEOPayrollRelationshipId | ✅ |
| PAYROLL_RELATIONSHIP_NUMBER | PayrollRelationshipPEOPayrollRelationshipNumber | ✅ |
| PAYROLL_STAT_UNIT_ID | PayrollRelationshipPEOPayrollStatUnitId | ✅ |
| PERSON_ID | PayrollRelationshipPEOPersonId | ✅ |
| RELATIONSHIP_TYPE_ID | PayrollRelationshipPEORelationshipTypeId | ✅ |
| START_DATE | PayrollRelationshipPEOStartDate | ✅ |

### [[payrollrelationshippvo|PayrollRelationshipPVO]] (HCM · BICC: 12/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayrollRelationshipPEOCreatedBy | ✅ |
| CREATION_DATE | PayrollRelationshipPEOCreationDate | ✅ |
| END_DATE | PayrollRelationshipPEOEndDate | ✅ |
| LAST_UPDATE_DATE | PayrollRelationshipPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollRelationshipPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PayrollRelationshipPEOLastUpdatedBy | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipPEOLegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | PayrollRelationshipPEOObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipId | ✅ |
| PAYROLL_RELATIONSHIP_NUMBER | PayrollRelationshipPEOPayrollRelationshipNumber | ✅ |
| PAYROLL_STAT_UNIT_ID | PayrollRelationshipPEOPayrollStatUnitId | ✅ |
| PERSON_ID | PayrollRelationshipPEOPersonId | ✅ |
| RELATIONSHIP_TYPE_ID | PayrollRelationshipPEORelationshipTypeId | ✅ |
| START_DATE | PayrollRelationshipPEOStartDate | ✅ |

### [[payrollruncosting|PayrollRunCosting]] (GL · BICC: 2/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayRelDnCreatedBy | — |
| CREATION_DATE | PayRelDnCreationDate | — |
| END_DATE | PayRelDnEndDate | — |
| LAST_UPDATE_DATE | PayRelDnLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayRelDnLastUpdateLogin | — |
| LAST_UPDATED_BY | PayRelDnLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | PayRelDnLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | PayRelDnObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayRelDnPayrollRelationshipId | — |
| PAYROLL_RELATIONSHIP_NUMBER | PayRelDnPayrollRelationshipNumber | ✅ |
| PAYROLL_STAT_UNIT_ID | PayRelDnPayrollStatUnitId | — |
| PERSON_ID | PayRelDnPersonId | — |
| RELATIONSHIP_TYPE_ID | PayRelDnRelationshipTypeId | — |
| START_DATE | PayRelDnStartDate | — |

### [[personalpaymentmethoddetailsdpvo|PersonalPaymentMethodDetailsDPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OBJECT_VERSION_NUMBER | PayrollRelationshipPEOObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipPEOPayrollRelationshipId | — |
| PAYROLL_STAT_UNIT_ID | PayrollRelationshipPEOPayrollStatUnitId | — |
| PERSON_ID | PayrollRelationshipPEOPersonId | — |

### [[prepaymentcosting|PrePaymentCosting]] (GL · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayRelDnCreatedBy | — |
| CREATION_DATE | PayRelDnCreationDate | — |
| END_DATE | PayRelDnEndDate | ✅ |
| LAST_UPDATE_DATE | PayRelDnLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayRelDnLastUpdateLogin | — |
| LAST_UPDATED_BY | PayRelDnLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | PayRelDnLegislativeDataGroupId1 | — |
| OBJECT_VERSION_NUMBER | PayRelDnObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayRelDnPayrollRelationshipId | — |
| PAYROLL_RELATIONSHIP_NUMBER | PayRelDnPayrollRelationshipNumber | ✅ |
| PAYROLL_STAT_UNIT_ID | PayRelDnPayrollStatUnitId | — |
| PERSON_ID | PayRelDnPersonId | — |
| RELATIONSHIP_TYPE_ID | PayRelDnRelationshipTypeId | — |
| START_DATE | PayRelDnStartDate | ✅ |

### [[prepayments|PrePayments]] (AP · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayRelDNCreatedBy | — |
| CREATION_DATE | PayRelDNCreationDate | — |
| END_DATE | PayRelDNEndDate | ✅ |
| LAST_UPDATE_DATE | PayRelDNLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayRelDNLastUpdateLogin | — |
| LAST_UPDATED_BY | PayRelDNLastUpdatedBy | — |
| LEGISLATIVE_DATA_GROUP_ID | PayRelDNLegislativeDataGroupId | — |
| OBJECT_VERSION_NUMBER | PayRelDNObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayRelDNPayrollRelationshipId | — |
| PAYROLL_RELATIONSHIP_NUMBER | PayRelDNPayrollRelationshipNumber | ✅ |
| PAYROLL_STAT_UNIT_ID | PayRelDNPayrollStatUnitId | — |
| PERSON_ID | PayRelDNPersonId | — |
| RELATIONSHIP_TYPE_ID | PayRelDNRelationshipTypeId | — |
| START_DATE | PayRelDNStartDate | ✅ |

### [[retroelemententry|RetroElementEntry]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipPEOLegislativeDataGroupId | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipPEOPayrollRelationshipId | — |
| PERSON_ID | PayrollRelationshipPEOPersonId | — |

---

## 📚 Referências

- [Oracle Docs — PAY_PAY_RELATIONSHIPS_DN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypayrelationshipsdn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
