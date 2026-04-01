---
id: DOC-HCM-049
doc_type: system-doc
title: "BEN_PER_BNF_ORG — Beneficiários por Organização"
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
  - beneficiarios
  - beneficiary-org
aliases:
  - BEN_PER_BNF_ORG
  - ben_per_bnf_org
  - beneficiarios-beneficios
  - beneficiary-org
  - ben-per-bnf-org
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PER_BNF_ORG

## 📌 Visão Geral

Armazena os **beneficiários designados** pelos participantes de planos de benefícios (ex.: beneficiários de seguro de vida).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Designação de beneficiários:** Registro de quem recebe em caso de sinistro.
- **Percentuais:** Divisão percentual entre múltiplos beneficiários.
- **Compliance:** Atende requisitos regulatórios de designação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de beneficiários por organização
```sql
SELECT * FROM BEN_PER_BNF_ORG
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Beneficiários por Organização).

---

## 🔗 PVOs Relacionados

### [[beneficiaryorganizationpvo|BeneficiaryOrganizationPVO]] (HCM · BICC: 11/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BNF_ORGANIZATION_ID | BeneficiaryOrganizationPEOBnfOrganizationId | ✅ |
| BNF_TYP_CD | BeneficiaryOrganizationPEOBnfTypCd | ✅ |
| BUSINESS_GROUP_ID | BeneficiaryOrganizationPEOBusinessGroupId | — |
| CREATED_BY | BeneficiaryOrganizationPEOCreatedBy | — |
| CREATION_DATE | BeneficiaryOrganizationPEOCreationDate | — |
| END_DATE | BeneficiaryOrganizationPEOEndDate | ✅ |
| LAST_UPDATE_DATE | BeneficiaryOrganizationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BeneficiaryOrganizationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BeneficiaryOrganizationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | BeneficiaryOrganizationPEOObjectVersionNumber | — |
| PER_BNF_ORG_ID | BeneficiaryOrganizationPEOPerBnfOrgId | ✅ |
| PERSON_ID | BeneficiaryOrganizationPEOPersonId | — |
| START_DATE | BeneficiaryOrganizationPEOStartDate | ✅ |
| TRUSTEE_ADDL_DETAILS | BeneficiaryOrganizationPEOTrusteeAddlDetails | ✅ |
| TRUSTEE_EXECUTOR_NAME | BeneficiaryOrganizationPEOTrusteeExecutorName | ✅ |
| TRUSTEE_ORG_DESCRIPTION | BeneficiaryOrganizationPEOTrusteeOrgDescription | ✅ |
| TRUSTEE_ORG_NAME | BeneficiaryOrganizationPEOTrusteeOrgName | ✅ |
| TRUSTEE_ORG_REG_CD | BeneficiaryOrganizationPEOTrusteeOrgRegCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PER_BNF_ORG](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benperbnforg.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
