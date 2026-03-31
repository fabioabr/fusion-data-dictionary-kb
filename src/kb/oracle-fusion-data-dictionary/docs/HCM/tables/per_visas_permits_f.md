---
id: DOC-HCM-721
doc_type: system-doc
title: "PER_VISAS_PERMITS_F — Vistos e Permissões de Trabalho"
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
  - vistos
  - permissões-trabalho
  - imigração
aliases:
  - PER_VISAS_PERMITS_F
  - per_visas_permits_f
  - per-visas-permits-f
  - vistos-e-permissões
  - visas-permits
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_VISAS_PERMITS_F

## Visão Geral

Armazena informações sobre **vistos e permissões de trabalho** dos colaboradores, incluindo tipo, validade e país emissor. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de expatriados** — controle de vistos para colaboradores internacionais.
- **Compliance imigratório** — garante que permissões de trabalho estejam válidas.
- **Alertas de vencimento** — identificação de vistos próximos da expiração.
- **Relatórios regulatórios** — evidência de autorização legal para trabalho.
- **Planejamento de mobilidade** — suporta decisões de transferência internacional.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VISA_PERMIT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do visto/permissão | — | 🟢 90% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 95% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa titular do visto | PER_ALL_PEOPLE_F | 🟢 90% |
| 5 | VISA_PERMIT_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de visto/permissão | — | 🟢 85% |
| 6 | ISSUING_COUNTRY | VARCHAR2(30) | NULL | Classificação | País emissor do visto | — | 🟢 85% |
| 7 | ISSUE_DATE | DATE | NULL | Data | Data de emissão | — | 🟢 85% |
| 8 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração | — | 🟢 85% |
| 9 | VISA_PERMIT_NUMBER | VARCHAR2(60) | NULL | Identificação | Número do visto/permissão | — | 🟢 85% |
| 10 | VISA_PERMIT_STATUS | VARCHAR2(30) | NULL | Status | Status atual (ativo, expirado, cancelado) | — | 🟡 80% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (titular do visto)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Vistos próximos do vencimento
```sql
SELECT vp.VISA_PERMIT_NUMBER, vp.VISA_PERMIT_TYPE, vp.EXPIRATION_DATE,
       p.FULL_NAME
FROM   PER_VISAS_PERMITS_F vp
JOIN   PER_ALL_PEOPLE_F p ON vp.PERSON_ID = p.PERSON_ID
WHERE  vp.EXPIRATION_DATE BETWEEN SYSDATE AND SYSDATE + 90
  AND  SYSDATE BETWEEN vp.EFFECTIVE_START_DATE AND vp.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Vistos de um colaborador específico
- `EXPIRATION_DATE < SYSDATE` — Vistos expirados

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Dados sensíveis (PII) — aplicar controles de confidencialidade.
- O campo VISA_PERMIT_NUMBER pode conter dados regulados.
- Fundamental para compliance imigratório em operações internacionais.

---

## Referências

- [Oracle Docs — PER_VISAS_PERMITS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pervisaspermitsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[contactvisapermitpvo|ContactVisaPermitPVO]] (HCM · BICC: 22/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | VisaPermitPEOBusinessGroupId | — |
| CREATED_BY | VisaPermitPEOCreatedBy | ✅ |
| CREATION_DATE | VisaPermitPEOCreationDate | ✅ |
| CURRENT_VISA_PERMIT | VisaPermitPEOCurrentVisaPermit | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTRY_DATE | VisaPermitPEOEntryDate | ✅ |
| EXPIRATION_DATE | VisaPermitPEOExpirationDate | ✅ |
| ISSUE_DATE | VisaPermitPEOIssueDate | ✅ |
| ISSUING_AUTHORITY | VisaPermitPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | VisaPermitPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | IssuingLocation | ✅ |
| LAST_UPDATE_DATE | VisaPermitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | VisaPermitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | VisaPermitPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | VisaPermitPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | VisaPermitPEOObjectVersionNumber | — |
| PERSON_ID | VisaPermitPEOPersonId | ✅ |
| PROFESSION | VisaPermitPEOProfession | ✅ |
| VISA_PERMIT_CATEGORY | VisaPermitPEOVisaPermitCategory | ✅ |
| VISA_PERMIT_ID | VisaPermitId | ✅ |
| VISA_PERMIT_NUMBER | VisaPermitPEOVisaPermitNumber | ✅ |
| VISA_PERMIT_STATUS | VisaPermitPEOVisaPermitStatus | ✅ |
| VISA_PERMIT_STATUS_DATE | VisaPermitPEOVisaPermitStatusDate | ✅ |
| VISA_PERMIT_TYPE | VisaPermitPEOVisaPermitType | ✅ |

### [[visapermitpvo|VisaPermitPVO]] (HCM · BICC: 25/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | VisaPermitPEOBusinessGroupId | ✅ |
| CREATED_BY | VisaPermitPEOCreatedBy | ✅ |
| CREATION_DATE | VisaPermitPEOCreationDate | ✅ |
| CURRENT_VISA_PERMIT | VisaPermitPEOCurrentVisaPermit | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTRY_DATE | VisaPermitPEOEntryDate | ✅ |
| EXPIRATION_DATE | VisaPermitPEOExpirationDate | ✅ |
| ISSUE_DATE | VisaPermitPEOIssueDate | ✅ |
| ISSUING_AUTHORITY | VisaPermitPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | VisaPermitPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | IssuingLocation | ✅ |
| LAST_UPDATE_DATE | VisaPermitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | VisaPermitPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | VisaPermitPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | VisaPermitPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | VisaPermitPEOObjectVersionNumber | ✅ |
| PERSON_ID | VisaPermitPEOPersonId | ✅ |
| PROFESSION | VisaPermitPEOProfession | ✅ |
| VISA_PERMIT_CATEGORY | VisaPermitPEOVisaPermitCategory | ✅ |
| VISA_PERMIT_ID | VisaPermitId | ✅ |
| VISA_PERMIT_NUMBER | VisaPermitPEOVisaPermitNumber | ✅ |
| VISA_PERMIT_STATUS | VisaPermitPEOVisaPermitStatus | ✅ |
| VISA_PERMIT_STATUS_DATE | VisaPermitPEOVisaPermitStatusDate | ✅ |
| VISA_PERMIT_TYPE | VisaPermitPEOVisaPermitType | ✅ |

### [[visapermitpvoviewall|VisaPermitPVOViewAll]] (HCM · BICC: 22/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | VisaPermitPEOBusinessGroupId | — |
| CREATED_BY | VisaPermitPEOCreatedBy | ✅ |
| CREATION_DATE | VisaPermitPEOCreationDate | ✅ |
| CURRENT_VISA_PERMIT | VisaPermitPEOCurrentVisaPermit | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTRY_DATE | VisaPermitPEOEntryDate | ✅ |
| EXPIRATION_DATE | VisaPermitPEOExpirationDate | ✅ |
| ISSUE_DATE | VisaPermitPEOIssueDate | ✅ |
| ISSUING_AUTHORITY | VisaPermitPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | VisaPermitPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | IssuingLocation | ✅ |
| LAST_UPDATE_DATE | VisaPermitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | VisaPermitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | VisaPermitPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | VisaPermitPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | VisaPermitPEOObjectVersionNumber | — |
| PERSON_ID | VisaPermitPEOPersonId | ✅ |
| PROFESSION | VisaPermitPEOProfession | ✅ |
| VISA_PERMIT_CATEGORY | VisaPermitPEOVisaPermitCategory | ✅ |
| VISA_PERMIT_ID | VisaPermitId | ✅ |
| VISA_PERMIT_NUMBER | VisaPermitPEOVisaPermitNumber | ✅ |
| VISA_PERMIT_STATUS | VisaPermitPEOVisaPermitStatus | ✅ |
| VISA_PERMIT_STATUS_DATE | VisaPermitPEOVisaPermitStatusDate | ✅ |
| VISA_PERMIT_TYPE | VisaPermitPEOVisaPermitType | ✅ |
