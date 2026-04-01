---
id: DOC-HCM-591
doc_type: system-doc
title: "PAY_PAY_RELATIONSHIPS_F — Relacionamentos de Pagamento"
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
  - pay-relationships
  - relacionamento
  - pay-relationships
aliases:
  - PAY_PAY_RELATIONSHIPS_F
  - pay_pay_relationships_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_PAY_RELATIONSHIPS_F

## 📌 Visão Geral

Tabela central que armazena os **relacionamentos de pagamento** (payroll relationships) entre pessoas e a folha de pagamento. Eh a entidade principal que vincula um colaborador ao sistema de payroll, com vigencia temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Vinculacao de colaboradores ao sistema de folha de pagamento
- Controle de vigencia do relacionamento de pagamento
- Base para todas as transacoes de folha (entradas, cartoes, resultados)
- Entidade central do modelo de dados do Payroll

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
| 3 | PAYROLL_STAT_UNIT_ID | NUMBER(18) | NULL | FK | ID da unidade estatutaria | --- | 🟡 75% |
| 4 | RELATIONSHIP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de relacionamento | --- | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] --- via `PERSON_ID` (pessoa vinculada ao relacionamento de folha)

### Tabelas-filha (FK de saída)
- [[pay_assigned_payrolls_f]] --- via `PAYROLL_RELATIONSHIP_ID` (folhas atribuídas ao relacionamento)
- [[pay_element_entries_f]] --- via `PAYROLL_RELATIONSHIP_ID` (entradas de elemento do relacionamento de folha)
- [[pay_dir_cards_f]] --- via `PAYROLL_RELATIONSHIP_ID` (cartões de depósito direto do relacionamento)
- [[pay_payroll_rel_actions]] --- via `PAYROLL_RELATIONSHIP_ID` (ações de folha do relacionamento)
- [[pay_person_pay_methods_f]] --- via `PAYROLL_RELATIONSHIP_ID` (métodos de pagamento pessoais do relacionamento)

---

## 📎 Uso Típico

### Relacionamento de pagamento vigente por pessoa
```sql
SELECT pr.PAYROLL_RELATIONSHIP_ID, pr.PERSON_ID, pr.RELATIONSHIP_TYPE
FROM   PAY_PAY_RELATIONSHIPS_F pr
WHERE  pr.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN pr.EFFECTIVE_START_DATE AND pr.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigencia.
- Entidade central do Payroll: todas as transacoes de folha se vinculam ao payroll relationship.
- Uma pessoa pode ter mais de um relacionamento de pagamento (ex.: empregado + diretor).

---

## 🔗 PVOs Relacionados

### [[payrollrelationshipdpvo|PayrollRelationshipDPVO]] (HCM · BICC: 4/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayrollRelationshipDPEOCreatedBy | — |
| CREATION_DATE | PayrollRelationshipDPEOCreationDate | — |
| EFFECTIVE_END_DATE | PayrollRelationshipDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PayrollRelationshipDPEOEffectiveStartDate | ✅ |
| ELEMENT_CRITERIA_ID | PayrollRelationshipDPEOElementCriteriaId | — |
| LAST_UPDATE_DATE | PayrollRelationshipDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollRelationshipDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PayrollRelationshipDPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PayrollRelationshipDPEOObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipDPEOPayrollRelationshipId | — |
| REL_INFORMATION1 | PayrollRelationshipDPEORelInformation1 | — |
| REL_INFORMATION10 | PayrollRelationshipDPEORelInformation10 | — |
| REL_INFORMATION11 | PayrollRelationshipDPEORelInformation11 | — |
| REL_INFORMATION12 | PayrollRelationshipDPEORelInformation12 | — |
| REL_INFORMATION13 | PayrollRelationshipDPEORelInformation13 | — |
| REL_INFORMATION14 | PayrollRelationshipDPEORelInformation14 | — |
| REL_INFORMATION15 | PayrollRelationshipDPEORelInformation15 | — |
| REL_INFORMATION16 | PayrollRelationshipDPEORelInformation16 | — |
| REL_INFORMATION17 | PayrollRelationshipDPEORelInformation17 | — |
| REL_INFORMATION18 | PayrollRelationshipDPEORelInformation18 | — |
| REL_INFORMATION19 | PayrollRelationshipDPEORelInformation19 | — |
| REL_INFORMATION2 | PayrollRelationshipDPEORelInformation2 | — |
| REL_INFORMATION20 | PayrollRelationshipDPEORelInformation20 | — |
| REL_INFORMATION21 | PayrollRelationshipDPEORelInformation21 | — |
| REL_INFORMATION22 | PayrollRelationshipDPEORelInformation22 | — |
| REL_INFORMATION23 | PayrollRelationshipDPEORelInformation23 | — |
| REL_INFORMATION24 | PayrollRelationshipDPEORelInformation24 | — |
| REL_INFORMATION25 | PayrollRelationshipDPEORelInformation25 | — |
| REL_INFORMATION26 | PayrollRelationshipDPEORelInformation26 | — |
| REL_INFORMATION27 | PayrollRelationshipDPEORelInformation27 | — |
| REL_INFORMATION28 | PayrollRelationshipDPEORelInformation28 | — |
| REL_INFORMATION29 | PayrollRelationshipDPEORelInformation29 | — |
| REL_INFORMATION3 | PayrollRelationshipDPEORelInformation3 | — |
| REL_INFORMATION30 | PayrollRelationshipDPEORelInformation30 | — |
| REL_INFORMATION4 | PayrollRelationshipDPEORelInformation4 | — |
| REL_INFORMATION5 | PayrollRelationshipDPEORelInformation5 | — |
| REL_INFORMATION6 | PayrollRelationshipDPEORelInformation6 | — |
| REL_INFORMATION7 | PayrollRelationshipDPEORelInformation7 | — |
| REL_INFORMATION8 | PayrollRelationshipDPEORelInformation8 | — |
| REL_INFORMATION9 | PayrollRelationshipDPEORelInformation9 | — |
| REL_INFORMATION_DATE1 | PayrollRelationshipDPEORelInformationDate1 | — |
| REL_INFORMATION_DATE10 | PayrollRelationshipDPEORelInformationDate10 | — |
| REL_INFORMATION_DATE11 | PayrollRelationshipDPEORelInformationDate11 | — |
| REL_INFORMATION_DATE12 | PayrollRelationshipDPEORelInformationDate12 | — |
| REL_INFORMATION_DATE13 | PayrollRelationshipDPEORelInformationDate13 | — |
| REL_INFORMATION_DATE14 | PayrollRelationshipDPEORelInformationDate14 | — |
| REL_INFORMATION_DATE15 | PayrollRelationshipDPEORelInformationDate15 | — |
| REL_INFORMATION_DATE2 | PayrollRelationshipDPEORelInformationDate2 | — |
| REL_INFORMATION_DATE3 | PayrollRelationshipDPEORelInformationDate3 | — |
| REL_INFORMATION_DATE4 | PayrollRelationshipDPEORelInformationDate4 | — |
| REL_INFORMATION_DATE5 | PayrollRelationshipDPEORelInformationDate5 | — |
| REL_INFORMATION_DATE6 | PayrollRelationshipDPEORelInformationDate6 | — |
| REL_INFORMATION_DATE7 | PayrollRelationshipDPEORelInformationDate7 | — |
| REL_INFORMATION_DATE8 | PayrollRelationshipDPEORelInformationDate8 | — |
| REL_INFORMATION_DATE9 | PayrollRelationshipDPEORelInformationDate9 | — |
| REL_INFORMATION_NUMBER1 | PayrollRelationshipDPEORelInformationNumber1 | — |
| REL_INFORMATION_NUMBER10 | PayrollRelationshipDPEORelInformationNumber10 | — |
| REL_INFORMATION_NUMBER11 | PayrollRelationshipDPEORelInformationNumber11 | — |
| REL_INFORMATION_NUMBER12 | PayrollRelationshipDPEORelInformationNumber12 | — |
| REL_INFORMATION_NUMBER13 | PayrollRelationshipDPEORelInformationNumber13 | — |
| REL_INFORMATION_NUMBER14 | PayrollRelationshipDPEORelInformationNumber14 | — |
| REL_INFORMATION_NUMBER15 | PayrollRelationshipDPEORelInformationNumber15 | — |
| REL_INFORMATION_NUMBER16 | PayrollRelationshipDPEORelInformationNumber16 | — |
| REL_INFORMATION_NUMBER17 | PayrollRelationshipDPEORelInformationNumber17 | — |
| REL_INFORMATION_NUMBER18 | PayrollRelationshipDPEORelInformationNumber18 | — |
| REL_INFORMATION_NUMBER19 | PayrollRelationshipDPEORelInformationNumber19 | — |
| REL_INFORMATION_NUMBER2 | PayrollRelationshipDPEORelInformationNumber2 | — |
| REL_INFORMATION_NUMBER20 | PayrollRelationshipDPEORelInformationNumber20 | — |
| REL_INFORMATION_NUMBER3 | PayrollRelationshipDPEORelInformationNumber3 | — |
| REL_INFORMATION_NUMBER4 | PayrollRelationshipDPEORelInformationNumber4 | — |
| REL_INFORMATION_NUMBER5 | PayrollRelationshipDPEORelInformationNumber5 | — |
| REL_INFORMATION_NUMBER6 | PayrollRelationshipDPEORelInformationNumber6 | — |
| REL_INFORMATION_NUMBER7 | PayrollRelationshipDPEORelInformationNumber7 | — |
| REL_INFORMATION_NUMBER8 | PayrollRelationshipDPEORelInformationNumber8 | — |
| REL_INFORMATION_NUMBER9 | PayrollRelationshipDPEORelInformationNumber9 | — |
| REL_INFORMATION_TYPE | PayrollRelationshipDPEORelInformationType | ✅ |

### [[payrollrelationshippvo|PayrollRelationshipPVO]] (HCM · BICC: 3/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayrollRelationshipDPEOCreatedBy | — |
| CREATION_DATE | PayrollRelationshipDPEOCreationDate | — |
| EFFECTIVE_END_DATE | PayrollRelationshipDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PayrollRelationshipDPEOEffectiveStartDate | ✅ |
| ELEMENT_CRITERIA_ID | PayrollRelationshipDPEOElementCriteriaId | — |
| LAST_UPDATE_DATE | PayrollRelationshipDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollRelationshipDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PayrollRelationshipDPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PayrollRelationshipDPEOObjectVersionNumber | — |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipDPEOPayrollRelationshipId1 | — |
| REL_INFORMATION1 | PayrollRelationshipDPEORelInformation1 | — |
| REL_INFORMATION10 | PayrollRelationshipDPEORelInformation10 | — |
| REL_INFORMATION11 | PayrollRelationshipDPEORelInformation11 | — |
| REL_INFORMATION12 | PayrollRelationshipDPEORelInformation12 | — |
| REL_INFORMATION13 | PayrollRelationshipDPEORelInformation13 | — |
| REL_INFORMATION14 | PayrollRelationshipDPEORelInformation14 | — |
| REL_INFORMATION15 | PayrollRelationshipDPEORelInformation15 | — |
| REL_INFORMATION16 | PayrollRelationshipDPEORelInformation16 | — |
| REL_INFORMATION17 | PayrollRelationshipDPEORelInformation17 | — |
| REL_INFORMATION18 | PayrollRelationshipDPEORelInformation18 | — |
| REL_INFORMATION19 | PayrollRelationshipDPEORelInformation19 | — |
| REL_INFORMATION2 | PayrollRelationshipDPEORelInformation2 | — |
| REL_INFORMATION20 | PayrollRelationshipDPEORelInformation20 | — |
| REL_INFORMATION21 | PayrollRelationshipDPEORelInformation21 | — |
| REL_INFORMATION22 | PayrollRelationshipDPEORelInformation22 | — |
| REL_INFORMATION23 | PayrollRelationshipDPEORelInformation23 | — |
| REL_INFORMATION24 | PayrollRelationshipDPEORelInformation24 | — |
| REL_INFORMATION25 | PayrollRelationshipDPEORelInformation25 | — |
| REL_INFORMATION26 | PayrollRelationshipDPEORelInformation26 | — |
| REL_INFORMATION27 | PayrollRelationshipDPEORelInformation27 | — |
| REL_INFORMATION28 | PayrollRelationshipDPEORelInformation28 | — |
| REL_INFORMATION29 | PayrollRelationshipDPEORelInformation29 | — |
| REL_INFORMATION3 | PayrollRelationshipDPEORelInformation3 | — |
| REL_INFORMATION30 | PayrollRelationshipDPEORelInformation30 | — |
| REL_INFORMATION4 | PayrollRelationshipDPEORelInformation4 | — |
| REL_INFORMATION5 | PayrollRelationshipDPEORelInformation5 | — |
| REL_INFORMATION6 | PayrollRelationshipDPEORelInformation6 | — |
| REL_INFORMATION7 | PayrollRelationshipDPEORelInformation7 | — |
| REL_INFORMATION8 | PayrollRelationshipDPEORelInformation8 | — |
| REL_INFORMATION9 | PayrollRelationshipDPEORelInformation9 | — |
| REL_INFORMATION_DATE1 | PayrollRelationshipDPEORelInformationDate1 | — |
| REL_INFORMATION_DATE10 | PayrollRelationshipDPEORelInformationDate10 | — |
| REL_INFORMATION_DATE11 | PayrollRelationshipDPEORelInformationDate11 | — |
| REL_INFORMATION_DATE12 | PayrollRelationshipDPEORelInformationDate12 | — |
| REL_INFORMATION_DATE13 | PayrollRelationshipDPEORelInformationDate13 | — |
| REL_INFORMATION_DATE14 | PayrollRelationshipDPEORelInformationDate14 | — |
| REL_INFORMATION_DATE15 | PayrollRelationshipDPEORelInformationDate15 | — |
| REL_INFORMATION_DATE2 | PayrollRelationshipDPEORelInformationDate2 | — |
| REL_INFORMATION_DATE3 | PayrollRelationshipDPEORelInformationDate3 | — |
| REL_INFORMATION_DATE4 | PayrollRelationshipDPEORelInformationDate4 | — |
| REL_INFORMATION_DATE5 | PayrollRelationshipDPEORelInformationDate5 | — |
| REL_INFORMATION_DATE6 | PayrollRelationshipDPEORelInformationDate6 | — |
| REL_INFORMATION_DATE7 | PayrollRelationshipDPEORelInformationDate7 | — |
| REL_INFORMATION_DATE8 | PayrollRelationshipDPEORelInformationDate8 | — |
| REL_INFORMATION_DATE9 | PayrollRelationshipDPEORelInformationDate9 | — |
| REL_INFORMATION_NUMBER1 | PayrollRelationshipDPEORelInformationNumber1 | — |
| REL_INFORMATION_NUMBER10 | PayrollRelationshipDPEORelInformationNumber10 | — |
| REL_INFORMATION_NUMBER11 | PayrollRelationshipDPEORelInformationNumber11 | — |
| REL_INFORMATION_NUMBER12 | PayrollRelationshipDPEORelInformationNumber12 | — |
| REL_INFORMATION_NUMBER13 | PayrollRelationshipDPEORelInformationNumber13 | — |
| REL_INFORMATION_NUMBER14 | PayrollRelationshipDPEORelInformationNumber14 | — |
| REL_INFORMATION_NUMBER15 | PayrollRelationshipDPEORelInformationNumber15 | — |
| REL_INFORMATION_NUMBER16 | PayrollRelationshipDPEORelInformationNumber16 | — |
| REL_INFORMATION_NUMBER17 | PayrollRelationshipDPEORelInformationNumber17 | — |
| REL_INFORMATION_NUMBER18 | PayrollRelationshipDPEORelInformationNumber18 | — |
| REL_INFORMATION_NUMBER19 | PayrollRelationshipDPEORelInformationNumber19 | — |
| REL_INFORMATION_NUMBER2 | PayrollRelationshipDPEORelInformationNumber2 | — |
| REL_INFORMATION_NUMBER20 | PayrollRelationshipDPEORelInformationNumber20 | — |
| REL_INFORMATION_NUMBER3 | PayrollRelationshipDPEORelInformationNumber3 | — |
| REL_INFORMATION_NUMBER4 | PayrollRelationshipDPEORelInformationNumber4 | — |
| REL_INFORMATION_NUMBER5 | PayrollRelationshipDPEORelInformationNumber5 | — |
| REL_INFORMATION_NUMBER6 | PayrollRelationshipDPEORelInformationNumber6 | — |
| REL_INFORMATION_NUMBER7 | PayrollRelationshipDPEORelInformationNumber7 | — |
| REL_INFORMATION_NUMBER8 | PayrollRelationshipDPEORelInformationNumber8 | — |
| REL_INFORMATION_NUMBER9 | PayrollRelationshipDPEORelInformationNumber9 | — |
| REL_INFORMATION_TYPE | PayrollRelationshipDPEORelInformationType | — |

---

## 📚 Referências

- [Oracle Docs — PAY_PAY_RELATIONSHIPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/paypayrelationshipsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
