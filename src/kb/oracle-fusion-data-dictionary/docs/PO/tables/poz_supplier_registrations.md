---
id: DOC-PO-094
doc_type: system-doc
title: "POZ_SUPPLIER_REGISTRATIONS — Registros de Fornecedores (Onboarding)"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - supplier-registration
  - onboarding
  - cadastro
aliases:
  - POZ_SUPPLIER_REGISTRATIONS
  - poz_supplier_registrations
  - registro-fornecedores
  - supplier-registration
  - onboarding-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_REGISTRATIONS

## Visão Geral

Armazena os **registros de onboarding de fornecedores** no Oracle Fusion Procurement. Cada registro representa uma solicitação de cadastro de novo fornecedor, capturando dados básicos (nome, país, tipo) e o status do processo de aprovação. Quando aprovado, o registro gera um fornecedor efetivo na tabela `POZ_SUPPLIERS`.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Onboarding de fornecedores:** Captura inicial de dados durante o processo de registro.
- **Supplier Portal:** Suporte ao auto-registro de fornecedores prospectivos via portal.
- **Workflow de aprovação:** Controle do fluxo de aprovação do registro (interno ou por convite).
- **Qualificação:** Primeira etapa do processo de qualificação antes da efetivação.
- **Auditoria:** Histórico completo de todos os registros de fornecedores, incluindo rejeitados.
- **Due diligence:** Base para verificações prévias antes da aprovação do fornecedor.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUPPLIER_REG_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de fornecedor | — | 🟢 85% |
| 2 | SUPPLIER_NAME | VARCHAR2(360) | NOT NULL | Identificação | Razão social do fornecedor prospectivo | — | 🟢 85% |
| 3 | REGISTRATION_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do registro (visível ao usuário) | — | 🟡 75% |
| 4 | VENDOR_ID | NUMBER(18) | NULL | FK | ID do fornecedor efetivado (preenchido após aprovação) | [[poz_suppliers]] | 🟢 85% |
| 5 | REGISTRATION_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: DRAFT, SUBMITTED, APPROVED, REJECTED, WITHDRAWN | — | 🟢 85% |
| 6 | REGISTRATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo: PROSPECTIVE, INVITED, INTERNAL | — | 🟡 75% |
| 7 | COUNTRY_CODE | VARCHAR2(2) | NULL | Localização | País do fornecedor (ISO 3166-1 alpha-2) | — | 🟡 75% |
| 8 | SUPPLIER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do fornecedor: VENDOR, CONTRACTOR, etc. | — | 🟡 70% |
| 9 | TAX_PAYER_ID | VARCHAR2(80) | NULL | Fiscal | CNPJ/CPF do fornecedor prospectivo | — | 🟡 75% |
| 10 | DUNS_NUMBER | VARCHAR2(30) | NULL | Identificação | Número DUNS (Dun & Bradstreet) | — | 🟡 65% |
| 11 | EMAIL_ADDRESS | VARCHAR2(320) | NULL | Comunicação | E-mail de contato do registro | — | 🟡 75% |
| 12 | SUBMITTED_DATE | DATE | NULL | Data | Data de submissão do registro | — | 🟡 70% |
| 13 | APPROVED_DATE | DATE | NULL | Data | Data de aprovação | — | 🟡 70% |
| 14 | APPROVED_BY | NUMBER(18) | NULL | Aprovação | Usuário que aprovou | — | 🟡 70% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor efetivado, preenchido após aprovação)

### Tabelas-filha (FK de saída)

### Tabelas relacionadas

---

## Uso Típico

### Registros pendentes de aprovação
```sql
SELECT sr.SUPPLIER_REG_ID, sr.REGISTRATION_NUMBER,
       sr.SUPPLIER_NAME, sr.COUNTRY_CODE,
       sr.REGISTRATION_TYPE, sr.SUBMITTED_DATE
FROM   POZ_SUPPLIER_REGISTRATIONS sr
WHERE  sr.REGISTRATION_STATUS = 'SUBMITTED'
ORDER BY sr.SUBMITTED_DATE;
```

### Registros aprovados em um período
```sql
SELECT sr.SUPPLIER_REG_ID, sr.SUPPLIER_NAME,
       sr.VENDOR_ID, sr.APPROVED_DATE
FROM   POZ_SUPPLIER_REGISTRATIONS sr
WHERE  sr.REGISTRATION_STATUS = 'APPROVED'
  AND  sr.APPROVED_DATE BETWEEN :start_date AND :end_date;
```

### Taxa de aprovação
```sql
SELECT sr.REGISTRATION_STATUS, COUNT(*) AS qtd
FROM   POZ_SUPPLIER_REGISTRATIONS sr
WHERE  sr.CREATION_DATE >= ADD_MONTHS(SYSDATE, -12)
GROUP BY sr.REGISTRATION_STATUS;
```

---

## Observações

- O campo `VENDOR_ID` é **NULL** até a aprovação do registro; após aprovação, é preenchido com o ID do fornecedor criado em `POZ_SUPPLIERS`.
- O ciclo de vida do registro segue: DRAFT → SUBMITTED → APPROVED/REJECTED/WITHDRAWN.
- Registros do tipo `PROSPECTIVE` são originados pelo fornecedor no **Supplier Portal**; `INVITED` são gerados por convite interno; `INTERNAL` são criados pelo comprador.
- O campo `TAX_PAYER_ID` contém o CNPJ/CPF do prospectivo; após aprovação, este dado migra para `POZ_SUPPLIERS_PII`.
- Registros rejeitados (`REJECTED`) são mantidos para auditoria e não geram fornecedor efetivo.

---

## Referências

- [Oracle Docs — POZ_SUPPLIER_REGISTRATIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
