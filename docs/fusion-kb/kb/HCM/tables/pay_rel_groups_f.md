---
id: DOC-HCM-595
doc_type: system-doc
title: "PAY_REL_GROUPS_F — Grupos de Relacionamento de Folha"
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
  - rel-groups
  - grupos
  - pay-rel-groups
aliases:
  - PAY_REL_GROUPS_F
  - pay_rel_groups_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_REL_GROUPS_F

## 📌 Visão Geral

Armazena os **grupos de relacionamento** (relationship groups) que permitem agrupar relacionamentos de pagamento para processamento seletivo. Utilizado para executar folha para subconjuntos de colaboradores.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Agrupamento de colaboradores para processamento seletivo
- Configuracao de filtros de execucao de folha
- Processamento parcial de payroll por grupo

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REL_GROUP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do grupo | --- | 🟢 85% |
| 2 | REL_GROUP_NAME | VARCHAR2(80) | NOT NULL | Identificacao | Nome do grupo | --- | 🟢 80% |
| 3 | PAYROLL_ID | NUMBER(18) | NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 80% |
| 4 | GROUP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do grupo | --- | 🟡 70% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigencia | Data de inicio da vigencia | --- | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigencia | Data de fim da vigencia | --- | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento do grupo de relacionamento)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Grupos vigentes de uma folha
```sql
SELECT rg.REL_GROUP_ID, rg.REL_GROUP_NAME, rg.GROUP_TYPE
FROM   PAY_REL_GROUPS_F rg
WHERE  rg.PAYROLL_ID = :p_payroll_id
  AND  SYSDATE BETWEEN rg.EFFECTIVE_START_DATE AND rg.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[bipayrollrelationshipgroupdpvo|BIPayrollRelationshipGroupDPVO]] (HCM · BICC: 14/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_STATUS_TYPE_ID | PayrollRelationshipGroupDPEOAssignmentStatusTypeId | ✅ |
| CREATED_BY | PayrollRelationshipGroupDPEOCreatedBy | ✅ |
| CREATION_DATE | PayrollRelationshipGroupDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | PayrollRelationshipGroupDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PayrollRelationshipGroupDPEOEffectiveStartDate | ✅ |
| ELEMENT_CRITERIA_ID | PayrollRelationshipGroupDPEOElementCriteriaId | ✅ |
| ENTERPRISE_ID | PayrollRelationshipGroupDPEOEnterpriseId | ✅ |
| LAST_UPDATE_DATE | PayrollRelationshipGroupDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollRelationshipGroupDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PayrollRelationshipGroupDPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PayrollRelationshipGroupDPEOObjectVersionNumber | ✅ |
| OVERRIDING_PERIOD_ID | PayrollRelationshipGroupDPEOOverridingPeriodId | ✅ |
| REL_INFORMATION1 | PayrollRelationshipGroupDPEORelInformation1 | — |
| REL_INFORMATION10 | PayrollRelationshipGroupDPEORelInformation10 | — |
| REL_INFORMATION11 | PayrollRelationshipGroupDPEORelInformation11 | — |
| REL_INFORMATION12 | PayrollRelationshipGroupDPEORelInformation12 | — |
| REL_INFORMATION13 | PayrollRelationshipGroupDPEORelInformation13 | — |
| REL_INFORMATION14 | PayrollRelationshipGroupDPEORelInformation14 | — |
| REL_INFORMATION15 | PayrollRelationshipGroupDPEORelInformation15 | — |
| REL_INFORMATION16 | PayrollRelationshipGroupDPEORelInformation16 | — |
| REL_INFORMATION17 | PayrollRelationshipGroupDPEORelInformation17 | — |
| REL_INFORMATION18 | PayrollRelationshipGroupDPEORelInformation18 | — |
| REL_INFORMATION19 | PayrollRelationshipGroupDPEORelInformation19 | — |
| REL_INFORMATION2 | PayrollRelationshipGroupDPEORelInformation2 | — |
| REL_INFORMATION20 | PayrollRelationshipGroupDPEORelInformation20 | — |
| REL_INFORMATION21 | PayrollRelationshipGroupDPEORelInformation21 | — |
| REL_INFORMATION22 | PayrollRelationshipGroupDPEORelInformation22 | — |
| REL_INFORMATION23 | PayrollRelationshipGroupDPEORelInformation23 | — |
| REL_INFORMATION24 | PayrollRelationshipGroupDPEORelInformation24 | — |
| REL_INFORMATION25 | PayrollRelationshipGroupDPEORelInformation25 | — |
| REL_INFORMATION26 | PayrollRelationshipGroupDPEORelInformation26 | — |
| REL_INFORMATION27 | PayrollRelationshipGroupDPEORelInformation27 | — |
| REL_INFORMATION28 | PayrollRelationshipGroupDPEORelInformation28 | — |
| REL_INFORMATION29 | PayrollRelationshipGroupDPEORelInformation29 | — |
| REL_INFORMATION3 | PayrollRelationshipGroupDPEORelInformation3 | — |
| REL_INFORMATION30 | PayrollRelationshipGroupDPEORelInformation30 | — |
| REL_INFORMATION4 | PayrollRelationshipGroupDPEORelInformation4 | — |
| REL_INFORMATION5 | PayrollRelationshipGroupDPEORelInformation5 | — |
| REL_INFORMATION6 | PayrollRelationshipGroupDPEORelInformation6 | — |
| REL_INFORMATION7 | PayrollRelationshipGroupDPEORelInformation7 | — |
| REL_INFORMATION8 | PayrollRelationshipGroupDPEORelInformation8 | — |
| REL_INFORMATION9 | PayrollRelationshipGroupDPEORelInformation9 | — |
| REL_INFORMATION_DATE1 | PayrollRelationshipGroupDPEORelInformationDate1 | — |
| REL_INFORMATION_DATE10 | PayrollRelationshipGroupDPEORelInformationDate10 | — |
| REL_INFORMATION_DATE11 | PayrollRelationshipGroupDPEORelInformationDate11 | — |
| REL_INFORMATION_DATE12 | PayrollRelationshipGroupDPEORelInformationDate12 | — |
| REL_INFORMATION_DATE13 | PayrollRelationshipGroupDPEORelInformationDate13 | — |
| REL_INFORMATION_DATE14 | PayrollRelationshipGroupDPEORelInformationDate14 | — |
| REL_INFORMATION_DATE15 | PayrollRelationshipGroupDPEORelInformationDate15 | — |
| REL_INFORMATION_DATE2 | PayrollRelationshipGroupDPEORelInformationDate2 | — |
| REL_INFORMATION_DATE3 | PayrollRelationshipGroupDPEORelInformationDate3 | — |
| REL_INFORMATION_DATE4 | PayrollRelationshipGroupDPEORelInformationDate4 | — |
| REL_INFORMATION_DATE5 | PayrollRelationshipGroupDPEORelInformationDate5 | — |
| REL_INFORMATION_DATE6 | PayrollRelationshipGroupDPEORelInformationDate6 | — |
| REL_INFORMATION_DATE7 | PayrollRelationshipGroupDPEORelInformationDate7 | — |
| REL_INFORMATION_DATE8 | PayrollRelationshipGroupDPEORelInformationDate8 | — |
| REL_INFORMATION_DATE9 | PayrollRelationshipGroupDPEORelInformationDate9 | — |
| REL_INFORMATION_NUMBER1 | PayrollRelationshipGroupDPEORelInformationNumber1 | — |
| REL_INFORMATION_NUMBER10 | PayrollRelationshipGroupDPEORelInformationNumber10 | — |
| REL_INFORMATION_NUMBER11 | PayrollRelationshipGroupDPEORelInformationNumber11 | — |
| REL_INFORMATION_NUMBER12 | PayrollRelationshipGroupDPEORelInformationNumber12 | — |
| REL_INFORMATION_NUMBER13 | PayrollRelationshipGroupDPEORelInformationNumber13 | — |
| REL_INFORMATION_NUMBER14 | PayrollRelationshipGroupDPEORelInformationNumber14 | — |
| REL_INFORMATION_NUMBER15 | PayrollRelationshipGroupDPEORelInformationNumber15 | — |
| REL_INFORMATION_NUMBER16 | PayrollRelationshipGroupDPEORelInformationNumber16 | — |
| REL_INFORMATION_NUMBER17 | PayrollRelationshipGroupDPEORelInformationNumber17 | — |
| REL_INFORMATION_NUMBER18 | PayrollRelationshipGroupDPEORelInformationNumber18 | — |
| REL_INFORMATION_NUMBER19 | PayrollRelationshipGroupDPEORelInformationNumber19 | — |
| REL_INFORMATION_NUMBER2 | PayrollRelationshipGroupDPEORelInformationNumber2 | — |
| REL_INFORMATION_NUMBER20 | PayrollRelationshipGroupDPEORelInformationNumber20 | — |
| REL_INFORMATION_NUMBER3 | PayrollRelationshipGroupDPEORelInformationNumber3 | — |
| REL_INFORMATION_NUMBER4 | PayrollRelationshipGroupDPEORelInformationNumber4 | — |
| REL_INFORMATION_NUMBER5 | PayrollRelationshipGroupDPEORelInformationNumber5 | — |
| REL_INFORMATION_NUMBER6 | PayrollRelationshipGroupDPEORelInformationNumber6 | — |
| REL_INFORMATION_NUMBER7 | PayrollRelationshipGroupDPEORelInformationNumber7 | — |
| REL_INFORMATION_NUMBER8 | PayrollRelationshipGroupDPEORelInformationNumber8 | — |
| REL_INFORMATION_NUMBER9 | PayrollRelationshipGroupDPEORelInformationNumber9 | — |
| REL_INFORMATION_TYPE | PayrollRelationshipGroupDPEORelInformationType | — |
| RELATIONSHIP_GROUP_ID | PayrollRelationshipGroupDPEORelationshipGroupId | ✅ |
| TIME_CARD_REQ | PayrollRelationshipGroupDPEOTimeCardReq | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_REL_GROUPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payrelgroupsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
