---
id: DOC-HCM-682
doc_type: system-doc
title: "PER_NATIONAL_IDENTIFIERS — Identificadores Nacionais de Pessoas"
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
  - identificadores-nacionais
  - cpf
  - documentos-pessoais
  - national-id
aliases:
  - PER_NATIONAL_IDENTIFIERS
  - per_national_identifiers
  - identificadores-nacionais
  - documentos-pessoais
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_NATIONAL_IDENTIFIERS

## Visão Geral

Armazena os **identificadores nacionais** (documentos de identidade) das pessoas no sistema. Inclui documentos como CPF, RG, passaporte, número de seguro social, entre outros, conforme a legislação de cada país.

> [!warning] Dados Sensíveis
> Esta tabela contém **dados pessoais sensíveis** (PII). Acesso deve ser restrito conforme LGPD/GDPR.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro de colaboradores** — registro de documentos obrigatórios (CPF, RG)
- **Compliance trabalhista** — validação de documentos para admissão e eSocial
- **Folha de pagamento** — identificação fiscal para cálculos tributários
- **Relatórios regulatórios** — RAIS, DIRF, eSocial, CAGED
- **Validação de unicidade** — impedir cadastros duplicados

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | NATIONAL_IDENTIFIER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | LEGISLATION_CODE | VARCHAR2(4) | NOT NULL | Classificação | Código do país/legislação (BR, US, etc.) | — | 🟢 90% |
| 4 | NATIONAL_IDENTIFIER_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do documento (CPF, SSN, NIN, etc.) | — | 🟢 90% |
| 5 | NATIONAL_IDENTIFIER_NUMBER | VARCHAR2(30) | NOT NULL | Documento | Número do documento | — | 🟢 95% |
| 6 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é o identificador principal (Y/N) | — | 🟡 75% |
| 7 | ISSUE_DATE | DATE | NULL | Documento | Data de emissão do documento | — | 🟡 70% |
| 8 | EXPIRATION_DATE | DATE | NULL | Documento | Data de validade do documento | — | 🟡 70% |
| 9 | PLACE_OF_ISSUE | VARCHAR2(150) | NULL | Documento | Local de emissão | — | 🟡 65% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa titular do documento de identidade nacional)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Obter CPF de um colaborador
```sql
SELECT ni.NATIONAL_IDENTIFIER_NUMBER
FROM   PER_NATIONAL_IDENTIFIERS ni
WHERE  ni.PERSON_ID = :p_person_id
  AND  ni.LEGISLATION_CODE = 'BR'
  AND  ni.NATIONAL_IDENTIFIER_TYPE = 'CPF';
```

---

## Observações

- Contém dados PII — acesso deve ser controlado e auditado.
- O tipo do documento varia por legislação: CPF (BR), SSN (US), NIN (UK), etc.
- `PRIMARY_FLAG = 'Y'` indica o identificador principal para a legislação.
- Para o Brasil, os tipos comuns incluem: CPF, RG, PIS/PASEP, CTPS.

---

## Referências

- [Oracle Docs — PER_NATIONAL_IDENTIFIERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pernationalidentifiers.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[contactpersonnationalidentifierpvo|ContactPersonNationalIdentifierPVO]] (HCM · BICC: 12/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | NationalIdentifierPEOBusinessGroupId | — |
| CREATED_BY | NationalIdentifierPEOCreatedBy | ✅ |
| CREATION_DATE | NationalIdentifierPEOCreationDate | ✅ |
| EXPIRATION_DATE | NationalIdentifierPEOExpirationDate | ✅ |
| ISSUE_DATE | NationalIdentifierPEOIssueDate | ✅ |
| LAST_UPDATE_DATE | NationalIdentifierPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NationalIdentifierPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | NationalIdentifierPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | NationalIdentifierPEOLegislationCode | ✅ |
| NATIONAL_IDENTIFIER_ID | NationalIdentifierId | ✅ |
| NATIONAL_IDENTIFIER_NUMBER | NationalIdentifierPEONationalIdentifierNumber | ✅ |
| NATIONAL_IDENTIFIER_TYPE | NationalIdentifierPEONationalIdentifierType | ✅ |
| OBJECT_VERSION_NUMBER | NationalIdentifierPEOObjectVersionNumber | — |
| PERSON_ID | NationalIdentifierPEOPersonId | ✅ |
| PLACE_OF_ISSUE | NationalIdentifierPEOPlaceOfIssue | ✅ |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | NationalIdentifierPEOLastUpdateDate | ✅ |
| NATIONAL_IDENTIFIER_ID | NationalIdentifierPEONationalIdentifierId | ✅ |
| NATIONAL_IDENTIFIER_NUMBER | NationalIdentifierPEONationalIdentifierNumber | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | NationalIdentifierPEOLastUpdateDate | ✅ |
| NATIONAL_IDENTIFIER_ID | NationalIdentifierPEONationalIdentifierId | — |
| NATIONAL_IDENTIFIER_NUMBER | NationalIdentifierPEONationalIdentifierNumber | ✅ |

### [[personnationalidentifierpvo|PersonNationalIdentifierPVO]] (HCM · BICC: 15/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | NationalIdentifierPEOBusinessGroupId | ✅ |
| CREATED_BY | NationalIdentifierPEOCreatedBy | ✅ |
| CREATION_DATE | NationalIdentifierPEOCreationDate | ✅ |
| EXPIRATION_DATE | NationalIdentifierPEOExpirationDate | ✅ |
| ISSUE_DATE | NationalIdentifierPEOIssueDate | ✅ |
| LAST_UPDATE_DATE | NationalIdentifierPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NationalIdentifierPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | NationalIdentifierPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | NationalIdentifierPEOLegislationCode | ✅ |
| NATIONAL_IDENTIFIER_ID | NationalIdentifierId | ✅ |
| NATIONAL_IDENTIFIER_NUMBER | NationalIdentifierPEONationalIdentifierNumber | ✅ |
| NATIONAL_IDENTIFIER_TYPE | NationalIdentifierPEONationalIdentifierType | ✅ |
| OBJECT_VERSION_NUMBER | NationalIdentifierPEOObjectVersionNumber | ✅ |
| PERSON_ID | NationalIdentifierPEOPersonId | ✅ |
| PLACE_OF_ISSUE | NationalIdentifierPEOPlaceOfIssue | ✅ |

### [[personnationalidentifierpvoviewall|PersonNationalIdentifierPVOViewAll]] (HCM · BICC: 12/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | NationalIdentifierPEOBusinessGroupId | — |
| CREATED_BY | NationalIdentifierPEOCreatedBy | ✅ |
| CREATION_DATE | NationalIdentifierPEOCreationDate | ✅ |
| EXPIRATION_DATE | NationalIdentifierPEOExpirationDate | ✅ |
| ISSUE_DATE | NationalIdentifierPEOIssueDate | ✅ |
| LAST_UPDATE_DATE | NationalIdentifierPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | NationalIdentifierPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | NationalIdentifierPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | NationalIdentifierPEOLegislationCode | ✅ |
| NATIONAL_IDENTIFIER_ID | NationalIdentifierId | ✅ |
| NATIONAL_IDENTIFIER_NUMBER | NationalIdentifierPEONationalIdentifierNumber | ✅ |
| NATIONAL_IDENTIFIER_TYPE | NationalIdentifierPEONationalIdentifierType | ✅ |
| OBJECT_VERSION_NUMBER | NationalIdentifierPEOObjectVersionNumber | — |
| PERSON_ID | NationalIdentifierPEOPersonId | ✅ |
| PLACE_OF_ISSUE | NationalIdentifierPEOPlaceOfIssue | ✅ |
