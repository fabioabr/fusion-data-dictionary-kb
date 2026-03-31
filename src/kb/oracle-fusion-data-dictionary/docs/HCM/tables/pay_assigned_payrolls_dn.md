---
id: DOC-HCM-549
doc_type: system-doc
title: "PAY_ASSIGNED_PAYROLLS_DN — Folhas Atribuidas (Desnormalizada)"
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
  - assigned-payrolls-dn
  - desnormalizada
  - pay-assigned-dn
aliases:
  - PAY_ASSIGNED_PAYROLLS_DN
  - pay_assigned_payrolls_dn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_ASSIGNED_PAYROLLS_DN

## 📌 Visão Geral

Visao **desnormalizada** das folhas de pagamento atribuidas a colaboradores. Consolida dados de `PAY_ASSIGNED_PAYROLLS_F` com informacoes pre-calculadas para consultas otimizadas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Consultas otimizadas de associacao colaborador-folha
- Relatorios rapidos de colaboradores por folha
- Dashboards de distribuicao de headcount por payroll

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNED_PAYROLL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da atribuicao | --- | 🟢 90% |
| 2 | PAYROLL_ID | NUMBER(18) | NOT NULL | FK | ID da folha de pagamento | PAY_ALL_PAYROLLS_F | 🟢 90% |
| 3 | PAYROLL_RELATIONSHIP_ID | NUMBER(18) | NOT NULL | FK | ID do relacionamento de folha | PAY_PAY_RELATIONSHIPS_F | 🟢 85% |
| 4 | PAYROLL_NAME | VARCHAR2(100) | NULL | Identificacao | Nome da folha (desnormalizado) | --- | 🟡 75% |
| 5 | PERSON_ID | NUMBER(18) | NULL | FK | ID da pessoa | PER_ALL_PEOPLE_F | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_all_payrolls_f]] --- via `PAYROLL_ID` (folha de pagamento de origem)
- [[pay_pay_relationships_f]] --- via `PAYROLL_RELATIONSHIP_ID` (relacionamento de folha do colaborador)

### Tabelas-filha (FK de saída)
- --- Visao desnormalizada para relatorios

---

## 📎 Uso Típico

### Colaboradores por folha de pagamento
```sql
SELECT dn.PERSON_ID, dn.PAYROLL_NAME
FROM   PAY_ASSIGNED_PAYROLLS_DN dn
WHERE  dn.PAYROLL_ID = :p_payroll_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[biassignedpayrollpvo|BIAssignedPayrollPVO]] (HCM · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNED_PAYROLL_ID | PayrollUsagePEOAssignedPayrollId | ✅ |
| CREATED_BY | PayrollUsagePEOCreatedBy | ✅ |
| CREATION_DATE | PayrollUsagePEOCreationDate | ✅ |
| END_DATE | PayrollUsagePEOEndDate | ✅ |
| FINC | PayrollUsagePEOFinc | ✅ |
| FSED | PayrollUsagePEOFsed | ✅ |
| LAST_UPDATE_DATE | PayrollUsagePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayrollUsagePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PayrollUsagePEOLastUpdatedBy | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | PayrollUsagePEOLegislativeDataGroupId | ✅ |
| LSED | PayrollUsagePEOLsed | ✅ |
| LSPD | PayrollUsagePEOLspd | ✅ |
| OBJECT_VERSION_NUMBER | PayrollUsagePEOObjectVersionNumber | ✅ |
| PAYROLL_ID | PayrollUsagePEOPayrollId | ✅ |
| PAYROLL_TERM_ID | PayrollUsagePEOPayrollTermId | ✅ |
| START_DATE | PayrollUsagePEOStartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — PAY_ASSIGNED_PAYROLLS_DN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payassignedpayrollsdn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
