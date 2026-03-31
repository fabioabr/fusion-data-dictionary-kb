---
id: DOC-HCM-685
doc_type: system-doc
title: "PER_PASSPORTS — Passaportes de Pessoas"
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
  - passaportes
  - documentos-pessoais
  - viagem
  - expatriados
aliases:
  - PER_PASSPORTS
  - per_passports
  - passaportes
  - documentos-viagem
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PASSPORTS

## Visão Geral

Armazena os dados de **passaportes** dos colaboradores. Inclui informações como número do passaporte, país emissor, datas de emissão e validade, utilizados para gestão de viagens e expatriados.

> [!warning] Dados Sensíveis
> Esta tabela contém **dados pessoais sensíveis** (PII). Acesso deve ser restrito conforme LGPD/GDPR.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de expatriados** — controlar documentos de viagem para transferências internacionais
- **Viagens corporativas** — validar passaportes válidos para emissão de passagens
- **Compliance imigratório** — verificar validade de documentos para obtenção de vistos
- **Relatórios regulatórios** — informações para autoridades migratórias
- **Alertas de renovação** — notificar sobre passaportes próximos do vencimento

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PASSPORT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do passaporte | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | PASSPORT_NUMBER | VARCHAR2(30) | NOT NULL | Documento | Número do passaporte | — | 🟢 95% |
| 4 | COUNTRY | VARCHAR2(60) | NOT NULL | Documento | País emissor do passaporte | — | 🟢 90% |
| 5 | PASSPORT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do passaporte (ordinário, diplomático, etc.) | — | 🟡 70% |
| 6 | ISSUE_DATE | DATE | NULL | Documento | Data de emissão | — | 🟢 85% |
| 7 | EXPIRATION_DATE | DATE | NULL | Documento | Data de validade | — | 🟢 90% |
| 8 | ISSUING_AUTHORITY | VARCHAR2(150) | NULL | Documento | Autoridade emissora | — | 🟡 70% |
| 9 | PROFESSION | VARCHAR2(150) | NULL | Descritivo | Profissão registrada no passaporte | — | 🟡 60% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa titular do passaporte)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Passaportes válidos de um colaborador
```sql
SELECT p.PASSPORT_NUMBER, p.COUNTRY, p.EXPIRATION_DATE
FROM   PER_PASSPORTS p
WHERE  p.PERSON_ID = :p_person_id
  AND  p.EXPIRATION_DATE > SYSDATE;
```

---

## Observações

- Contém dados PII — acesso deve ser controlado e auditado.
- Uma pessoa pode ter múltiplos passaportes (dupla cidadania, renovações).
- Monitorar `EXPIRATION_DATE` para alertas de renovação.
- Verificar validade mínima exigida para vistos de destino (geralmente 6 meses).

---

## Referências

- [Oracle Docs — PER_PASSPORTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpassports.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[contactpassportspvo|ContactPassportsPVO]] (HCM · BICC: 15/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PassportsPEOBusinessGroupId | — |
| CREATED_BY | PassportsPEOCreatedBy | ✅ |
| CREATION_DATE | PassportsPEOCreationDate | ✅ |
| EXPIRATION_DATE | PassportsPEOExpirationDate | ✅ |
| ISSUE_DATE | PassportsPEOIssueDate | ✅ |
| ISSUING_AUTHORITY | PassportsPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | PassportsPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | PassportsPEOIssuingLocation | ✅ |
| LAST_UPDATE_DATE | PassportsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PassportsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PassportsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PassportsPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PassportsPEOObjectVersionNumber | — |
| PASSPORT_ID | PassportId | ✅ |
| PASSPORT_NUMBER | PassportsPEOPassportNumber | ✅ |
| PASSPORT_TYPE | PassportsPEOPassportType | ✅ |
| PERSON_ID | PassportsPEOPersonId | ✅ |
| PROFESSION | PassportsPEOProfession | ✅ |

### [[passportspvo|PassportsPVO]] (HCM · BICC: 15/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PassportsPEOBusinessGroupId | — |
| CREATED_BY | PassportsPEOCreatedBy | ✅ |
| CREATION_DATE | PassportsPEOCreationDate | ✅ |
| EXPIRATION_DATE | PassportsPEOExpirationDate | ✅ |
| ISSUE_DATE | PassportsPEOIssueDate | ✅ |
| ISSUING_AUTHORITY | PassportsPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | PassportsPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | PassportsPEOIssuingLocation | ✅ |
| LAST_UPDATE_DATE | PassportsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PassportsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PassportsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PassportsPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PassportsPEOObjectVersionNumber | — |
| PASSPORT_ID | PassportId | ✅ |
| PASSPORT_NUMBER | PassportsPEOPassportNumber | ✅ |
| PASSPORT_TYPE | PassportsPEOPassportType | ✅ |
| PERSON_ID | PassportsPEOPersonId | ✅ |
| PROFESSION | PassportsPEOProfession | ✅ |

### [[passportspvoviewall|PassportsPVOViewAll]] (HCM · BICC: 15/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | PassportsPEOBusinessGroupId | — |
| CREATED_BY | PassportsPEOCreatedBy | ✅ |
| CREATION_DATE | PassportsPEOCreationDate | ✅ |
| EXPIRATION_DATE | PassportsPEOExpirationDate | ✅ |
| ISSUE_DATE | PassportsPEOIssueDate | ✅ |
| ISSUING_AUTHORITY | PassportsPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | PassportsPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | PassportsPEOIssuingLocation | ✅ |
| LAST_UPDATE_DATE | PassportsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PassportsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PassportsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PassportsPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PassportsPEOObjectVersionNumber | — |
| PASSPORT_ID | PassportId | ✅ |
| PASSPORT_NUMBER | PassportsPEOPassportNumber | ✅ |
| PASSPORT_TYPE | PassportsPEOPassportType | ✅ |
| PERSON_ID | PassportsPEOPersonId | ✅ |
| PROFESSION | PassportsPEOProfession | ✅ |
