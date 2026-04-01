---
id: DOC-HCM-594
doc_type: system-doc
title: "PAY_REL_GROUPS_DN — Grupos de Relacionamento (Desnormalizada)"
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
  - rel-groups-dn
  - desnormalizada
  - pay-rel-groups-dn
aliases:
  - PAY_REL_GROUPS_DN
  - pay_rel_groups_dn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_REL_GROUPS_DN

## 📌 Visão Geral

Visao **desnormalizada** dos grupos de relacionamento de folha. Consolida dados de `PAY_REL_GROUPS_F` para consultas otimizadas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas otimizadas de grupos de relacionamento
- Relatorios de agrupamento de colaboradores para folha

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
| 2 | REL_GROUP_NAME | VARCHAR2(80) | NULL | Identificacao | Nome do grupo | --- | 🟡 75% |
| 3 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NULL | FK | ID do relacionamento | PAY_PAY_RELATIONSHIPS_F | 🟢 85% |
| 4 | GROUP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do grupo | --- | 🟡 70% |
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

### Grupos de um relacionamento de pagamento
```sql
SELECT dn.REL_GROUP_ID, dn.REL_GROUP_NAME, dn.GROUP_TYPE
FROM   PAY_REL_GROUPS_DN dn
WHERE  dn.PAYROLL_RELATIONSHIP_ID = :p_rel_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[bipayrollrelationshipgrouppvo|BIPayrollRelationshipGroupPVO]] (HCM · BICC: 20/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AC_TRIGGER_FLAG | PayrollRelationshipGroupPEOAcTriggerFlag | ✅ |
| ASSIGNMENT_ID | PayrollRelationshipGroupPEOAssignmentId | ✅ |
| ASSIGNMENT_NUMBER | PayrollRelationshipGroupPEOAssignmentNumber | ✅ |
| CREATED_BY | PayrollRelationshipGroupPEOCreatedBy | ✅ |
| CREATION_DATE | PayrollRelationshipGroupPEOCreationDate | ✅ |
| END_DATE | PayrollRelationshipGroupPEOEndDate | ✅ |
| ENTERPRISE_ID | PayrollRelationshipGroupPEOEnterpriseId | ✅ |
| GROUP_TYPE | PayrollRelationshipGroupPEOGroupType | ✅ |
| LAST_UPDATE_DATE | PayrollRelationshipGroupPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollRelationshipGroupPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PayrollRelationshipGroupPEOLastUpdatedBy | ✅ |
| LEGAL_EMPLOYER_ID | PayrollRelationshipGroupPEOLegalEmployerId | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | PayrollRelationshipGroupPEOLegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | PayrollRelationshipGroupPEOObjectVersionNumber | ✅ |
| PARENT_REL_GROUP_ID | PayrollRelationshipGroupPEOParentRelGroupId | ✅ |
| PAYROLL_RELATIONSHIP_ID | PayrollRelationshipGroupPEOPayrollRelationshipId | ✅ |
| RELATIONSHIP_GROUP_ID | PayrollRelationshipGroupPEORelationshipGroupId | ✅ |
| START_DATE | PayrollRelationshipGroupPEOStartDate | ✅ |
| TAX_REPORTING_UNIT_ID | PayrollRelationshipGroupPEOTaxReportingUnitId | ✅ |
| TERM_ID | PayrollRelationshipGroupPEOTermId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_REL_GROUPS_DN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payrelgroupsdn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
