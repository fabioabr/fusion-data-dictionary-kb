---
id: DOC-HCM-550
doc_type: system-doc
title: "PAY_ASSIGNED_PAYROLLS_F — Folhas Atribuidas a Colaboradores"
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
  - assigned-payrolls
  - atribuicao
  - pay-assigned
aliases:
  - PAY_ASSIGNED_PAYROLLS_F
  - pay_assigned_payrolls_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ASSIGNED_PAYROLLS_F

## 📌 Visão Geral

Armazena a **atribuicao de folhas de pagamento** a colaboradores. Cada registro vincula um relacionamento de pagamento (payroll relationship) a uma folha especifica, com vigencia temporal (`_F`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Associacao de colaboradores a folhas de pagamento
- Controle de vigencia da atribuicao de payroll
- Historico de transferencias entre folhas

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNED_PAYROLL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da atribuicao | --- | 🟢 95% |
| 2 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 95% |
| 3 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 95% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 6 | PAYROLL_TERM_ID | NUMBER(18) | NULL | FK | ID do termo de folha | --- | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha do colaborador)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (definição da folha de pagamento)

### Tabelas-filha (FK de saída)
- [[pay_assigned_payrolls_dn]] --- via `ASSIGNED_PAYROLL_ID` (visão desnormalizada da folha atribuída)

---

## 📎 Uso Típico

### Folha atribuida vigente por relacionamento
```sql
SELECT ap.ASSIGNED_PAYROLL_ID, ap.PAYROLL_ID, ap.EFFECTIVE_START_DATE
FROM   PAY_ASSIGNED_PAYROLLS_F ap
WHERE  ap.PAYROLL_RELATIONSHIP_ID = :p_rel_id
  AND  SYSDATE BETWEEN ap.EFFECTIVE_START_DATE AND ap.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Um colaborador pode ter historico de multiplas folhas ao longo do tempo.
- Relaciona-se com `PAY_PAY_RELATIONSHIPS_F` que eh a entidade principal de vinculo de pagamento.

---

## 🔗 PVOs Relacionados

### [[biassignedpayrolldpvo|BIAssignedPayrollDPVO]] (HCM · BICC: 77/77)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASG_INFORMATION1 | PayrollUsageDPEOAsgInformation1 | ✅ |
| ASG_INFORMATION10 | PayrollUsageDPEOAsgInformation10 | ✅ |
| ASG_INFORMATION11 | PayrollUsageDPEOAsgInformation11 | ✅ |
| ASG_INFORMATION12 | PayrollUsageDPEOAsgInformation12 | ✅ |
| ASG_INFORMATION13 | PayrollUsageDPEOAsgInformation13 | ✅ |
| ASG_INFORMATION14 | PayrollUsageDPEOAsgInformation14 | ✅ |
| ASG_INFORMATION15 | PayrollUsageDPEOAsgInformation15 | ✅ |
| ASG_INFORMATION16 | PayrollUsageDPEOAsgInformation16 | ✅ |
| ASG_INFORMATION17 | PayrollUsageDPEOAsgInformation17 | ✅ |
| ASG_INFORMATION18 | PayrollUsageDPEOAsgInformation18 | ✅ |
| ASG_INFORMATION19 | PayrollUsageDPEOAsgInformation19 | ✅ |
| ASG_INFORMATION2 | PayrollUsageDPEOAsgInformation2 | ✅ |
| ASG_INFORMATION20 | PayrollUsageDPEOAsgInformation20 | ✅ |
| ASG_INFORMATION21 | PayrollUsageDPEOAsgInformation21 | ✅ |
| ASG_INFORMATION22 | PayrollUsageDPEOAsgInformation22 | ✅ |
| ASG_INFORMATION23 | PayrollUsageDPEOAsgInformation23 | ✅ |
| ASG_INFORMATION24 | PayrollUsageDPEOAsgInformation24 | ✅ |
| ASG_INFORMATION25 | PayrollUsageDPEOAsgInformation25 | ✅ |
| ASG_INFORMATION26 | PayrollUsageDPEOAsgInformation26 | ✅ |
| ASG_INFORMATION27 | PayrollUsageDPEOAsgInformation27 | ✅ |
| ASG_INFORMATION28 | PayrollUsageDPEOAsgInformation28 | ✅ |
| ASG_INFORMATION29 | PayrollUsageDPEOAsgInformation29 | ✅ |
| ASG_INFORMATION3 | PayrollUsageDPEOAsgInformation3 | ✅ |
| ASG_INFORMATION30 | PayrollUsageDPEOAsgInformation30 | ✅ |
| ASG_INFORMATION4 | PayrollUsageDPEOAsgInformation4 | ✅ |
| ASG_INFORMATION5 | PayrollUsageDPEOAsgInformation5 | ✅ |
| ASG_INFORMATION6 | PayrollUsageDPEOAsgInformation6 | ✅ |
| ASG_INFORMATION7 | PayrollUsageDPEOAsgInformation7 | ✅ |
| ASG_INFORMATION8 | PayrollUsageDPEOAsgInformation8 | ✅ |
| ASG_INFORMATION9 | PayrollUsageDPEOAsgInformation9 | ✅ |
| ASG_INFORMATION_DATE1 | PayrollUsageDPEOAsgInformationDate1 | ✅ |
| ASG_INFORMATION_DATE10 | PayrollUsageDPEOAsgInformationDate10 | ✅ |
| ASG_INFORMATION_DATE11 | PayrollUsageDPEOAsgInformationDate11 | ✅ |
| ASG_INFORMATION_DATE12 | PayrollUsageDPEOAsgInformationDate12 | ✅ |
| ASG_INFORMATION_DATE13 | PayrollUsageDPEOAsgInformationDate13 | ✅ |
| ASG_INFORMATION_DATE14 | PayrollUsageDPEOAsgInformationDate14 | ✅ |
| ASG_INFORMATION_DATE15 | PayrollUsageDPEOAsgInformationDate15 | ✅ |
| ASG_INFORMATION_DATE2 | PayrollUsageDPEOAsgInformationDate2 | ✅ |
| ASG_INFORMATION_DATE3 | PayrollUsageDPEOAsgInformationDate3 | ✅ |
| ASG_INFORMATION_DATE4 | PayrollUsageDPEOAsgInformationDate4 | ✅ |
| ASG_INFORMATION_DATE5 | PayrollUsageDPEOAsgInformationDate5 | ✅ |
| ASG_INFORMATION_DATE6 | PayrollUsageDPEOAsgInformationDate6 | ✅ |
| ASG_INFORMATION_DATE7 | PayrollUsageDPEOAsgInformationDate7 | ✅ |
| ASG_INFORMATION_DATE8 | PayrollUsageDPEOAsgInformationDate8 | ✅ |
| ASG_INFORMATION_DATE9 | PayrollUsageDPEOAsgInformationDate9 | ✅ |
| ASG_INFORMATION_NUMBER1 | PayrollUsageDPEOAsgInformationNumber1 | ✅ |
| ASG_INFORMATION_NUMBER10 | PayrollUsageDPEOAsgInformationNumber10 | ✅ |
| ASG_INFORMATION_NUMBER11 | PayrollUsageDPEOAsgInformationNumber11 | ✅ |
| ASG_INFORMATION_NUMBER12 | PayrollUsageDPEOAsgInformationNumber12 | ✅ |
| ASG_INFORMATION_NUMBER13 | PayrollUsageDPEOAsgInformationNumber13 | ✅ |
| ASG_INFORMATION_NUMBER14 | PayrollUsageDPEOAsgInformationNumber14 | ✅ |
| ASG_INFORMATION_NUMBER15 | PayrollUsageDPEOAsgInformationNumber15 | ✅ |
| ASG_INFORMATION_NUMBER16 | PayrollUsageDPEOAsgInformationNumber16 | ✅ |
| ASG_INFORMATION_NUMBER17 | PayrollUsageDPEOAsgInformationNumber17 | ✅ |
| ASG_INFORMATION_NUMBER18 | PayrollUsageDPEOAsgInformationNumber18 | ✅ |
| ASG_INFORMATION_NUMBER19 | PayrollUsageDPEOAsgInformationNumber19 | ✅ |
| ASG_INFORMATION_NUMBER2 | PayrollUsageDPEOAsgInformationNumber2 | ✅ |
| ASG_INFORMATION_NUMBER20 | PayrollUsageDPEOAsgInformationNumber20 | ✅ |
| ASG_INFORMATION_NUMBER3 | PayrollUsageDPEOAsgInformationNumber3 | ✅ |
| ASG_INFORMATION_NUMBER4 | PayrollUsageDPEOAsgInformationNumber4 | ✅ |
| ASG_INFORMATION_NUMBER5 | PayrollUsageDPEOAsgInformationNumber5 | ✅ |
| ASG_INFORMATION_NUMBER6 | PayrollUsageDPEOAsgInformationNumber6 | ✅ |
| ASG_INFORMATION_NUMBER7 | PayrollUsageDPEOAsgInformationNumber7 | ✅ |
| ASG_INFORMATION_NUMBER8 | PayrollUsageDPEOAsgInformationNumber8 | ✅ |
| ASG_INFORMATION_NUMBER9 | PayrollUsageDPEOAsgInformationNumber9 | ✅ |
| ASG_INFORMATION_TYPE | PayrollUsageDPEOAsgInformationType | ✅ |
| ASSIGNED_PAYROLL_ID | PayrollUsageDPEOAssignedPayrollId | ✅ |
| CREATED_BY | PayrollUsageDPEOCreatedBy | ✅ |
| CREATION_DATE | PayrollUsageDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | PayrollUsageDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PayrollUsageDPEOEffectiveStartDate | ✅ |
| ELEMENT_CRITERIA_ID | PayrollUsageDPEOElementCriteriaId | ✅ |
| LAST_UPDATE_DATE | PayrollUsageDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollUsageDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PayrollUsageDPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PayrollUsageDPEOObjectVersionNumber | ✅ |
| PRIMARY_FLAG | PayrollUsageDPEOPrimaryFlag | ✅ |

### [[retroelemententry|RetroElementEntry]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASG_INFORMATION_TYPE | AssignedPayrollAsgInformationType | — |
| ASSIGNED_PAYROLL_ID | AssignedPayrollAssignedPayrollId | — |
| EFFECTIVE_END_DATE | AssignedPayrollEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AssignedPayrollEffectiveStartDate | ✅ |
| ELEMENT_CRITERIA_ID | AssignedPayrollElementCriteriaId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PRIMARY_FLAG | AssignedPayrollPrimaryFlag | — |

---

## 📚 Referências

- [Oracle Docs — PAY_ASSIGNED_PAYROLLS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payassignedpayrollsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
