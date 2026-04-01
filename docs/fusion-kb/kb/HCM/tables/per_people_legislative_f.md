---
id: DOC-HCM-686
doc_type: system-doc
title: "PER_PEOPLE_LEGISLATIVE_F — Dados Legislativos de Pessoas"
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
  - dados-legislativos
  - legislacao
  - people-legislative
  - compliance
aliases:
  - PER_PEOPLE_LEGISLATIVE_F
  - per_people_legislative_f
  - dados-legislativos-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PEOPLE_LEGISLATIVE_F

## Visão Geral

Armazena os **dados legislativos** associados a cada pessoa, específicos por país/legislação. Contém informações regulatórias como etnia, deficiência, veterano, entre outros atributos exigidos pela legislação trabalhista de cada país. Tabela date-effective.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance regulatório** — armazenar dados exigidos pela legislação local
- **Relatórios EEO (Equal Employment Opportunity)** — classificação para relatórios de diversidade
- **eSocial (Brasil)** — informações trabalhistas para o governo
- **Relatórios de diversidade e inclusão** — análise demográfica da força de trabalho
- **Obrigações fiscais** — dados legislativos para cálculos tributários

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PEOPLE_LEGISLATIVE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro legislativo | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | LEGISLATION_CODE | VARCHAR2(4) | NOT NULL | Classificação | Código do país/legislação (BR, US, etc.) | — | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | SEX | VARCHAR2(30) | NULL | Legislativo | Sexo legal do colaborador | — | 🟡 80% |
| 7 | MARITAL_STATUS | VARCHAR2(30) | NULL | Legislativo | Estado civil | — | 🟡 75% |
| 8 | HIGHEST_EDUCATION_LEVEL | VARCHAR2(30) | NULL | Legislativo | Nível de escolaridade mais alto | — | 🟡 70% |
| 9 | ETHNICITY | VARCHAR2(30) | NULL | Legislativo | Etnia/raça (conforme legislação local) | — | 🟡 70% |
| 10 | DISABILITY_FLAG | VARCHAR2(1) | NULL | Legislativo | Indicador de pessoa com deficiência (Y/N) | — | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa com dados legislativos)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Dados legislativos brasileiros de um colaborador
```sql
SELECT pl.SEX, pl.MARITAL_STATUS, pl.HIGHEST_EDUCATION_LEVEL, pl.ETHNICITY
FROM   PER_PEOPLE_LEGISLATIVE_F pl
WHERE  pl.PERSON_ID = :p_person_id
  AND  pl.LEGISLATION_CODE = 'BR'
  AND  SYSDATE BETWEEN pl.EFFECTIVE_START_DATE AND pl.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência.
- Os campos disponíveis e seus valores válidos variam por `LEGISLATION_CODE`.
- Contém dados sensíveis (etnia, deficiência) — sujeitos a LGPD/GDPR.
- Para o Brasil, inclui dados exigidos pelo eSocial.

---

## Referências

- [Oracle Docs — PER_PEOPLE_LEGISLATIVE_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpeoplelegislativef.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[personlegislativeinfopvo|PersonLegislativeInfoPVO]] (HCM · BICC: 27/148)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PersonLegislativeInfoDPEOAttribute1 | — |
| ATTRIBUTE10 | PersonLegislativeInfoDPEOAttribute10 | — |
| ATTRIBUTE11 | PersonLegislativeInfoDPEOAttribute11 | — |
| ATTRIBUTE12 | PersonLegislativeInfoDPEOAttribute12 | — |
| ATTRIBUTE13 | PersonLegislativeInfoDPEOAttribute13 | — |
| ATTRIBUTE14 | PersonLegislativeInfoDPEOAttribute14 | — |
| ATTRIBUTE15 | PersonLegislativeInfoDPEOAttribute15 | — |
| ATTRIBUTE16 | PersonLegislativeInfoDPEOAttribute16 | — |
| ATTRIBUTE17 | PersonLegislativeInfoDPEOAttribute17 | — |
| ATTRIBUTE18 | PersonLegislativeInfoDPEOAttribute18 | — |
| ATTRIBUTE19 | PersonLegislativeInfoDPEOAttribute19 | — |
| ATTRIBUTE2 | PersonLegislativeInfoDPEOAttribute2 | — |
| ATTRIBUTE20 | PersonLegislativeInfoDPEOAttribute20 | — |
| ATTRIBUTE21 | PersonLegislativeInfoDPEOAttribute21 | — |
| ATTRIBUTE22 | PersonLegislativeInfoDPEOAttribute22 | — |
| ATTRIBUTE23 | PersonLegislativeInfoDPEOAttribute23 | — |
| ATTRIBUTE24 | PersonLegislativeInfoDPEOAttribute24 | — |
| ATTRIBUTE25 | PersonLegislativeInfoDPEOAttribute25 | — |
| ATTRIBUTE26 | PersonLegislativeInfoDPEOAttribute26 | — |
| ATTRIBUTE27 | PersonLegislativeInfoDPEOAttribute27 | — |
| ATTRIBUTE28 | PersonLegislativeInfoDPEOAttribute28 | — |
| ATTRIBUTE29 | PersonLegislativeInfoDPEOAttribute29 | — |
| ATTRIBUTE3 | PersonLegislativeInfoDPEOAttribute3 | — |
| ATTRIBUTE30 | PersonLegislativeInfoDPEOAttribute30 | — |
| ATTRIBUTE4 | PersonLegislativeInfoDPEOAttribute4 | — |
| ATTRIBUTE5 | PersonLegislativeInfoDPEOAttribute5 | — |
| ATTRIBUTE6 | PersonLegislativeInfoDPEOAttribute6 | — |
| ATTRIBUTE7 | PersonLegislativeInfoDPEOAttribute7 | — |
| ATTRIBUTE8 | PersonLegislativeInfoDPEOAttribute8 | — |
| ATTRIBUTE9 | PersonLegislativeInfoDPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PersonLegislativeInfoDPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PersonLegislativeInfoDPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PersonLegislativeInfoDPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PersonLegislativeInfoDPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PersonLegislativeInfoDPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PersonLegislativeInfoDPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PersonLegislativeInfoDPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PersonLegislativeInfoDPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PersonLegislativeInfoDPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PersonLegislativeInfoDPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PersonLegislativeInfoDPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PersonLegislativeInfoDPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PersonLegislativeInfoDPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PersonLegislativeInfoDPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PersonLegislativeInfoDPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PersonLegislativeInfoDPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PersonLegislativeInfoDPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PersonLegislativeInfoDPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PersonLegislativeInfoDPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PersonLegislativeInfoDPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PersonLegislativeInfoDPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PersonLegislativeInfoDPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PersonLegislativeInfoDPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PersonLegislativeInfoDPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PersonLegislativeInfoDPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PersonLegislativeInfoDPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PersonLegislativeInfoDPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PersonLegislativeInfoDPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PersonLegislativeInfoDPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PersonLegislativeInfoDPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PersonLegislativeInfoDPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PersonLegislativeInfoDPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PersonLegislativeInfoDPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PersonLegislativeInfoDPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PersonLegislativeInfoDPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PersonLegislativeInfoDPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | PersonLegislativeInfoDPEOBusinessGroupId | ✅ |
| CREATED_BY | PersonLegislativeInfoDPEOCreatedBy | ✅ |
| CREATION_DATE | PersonLegislativeInfoDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| HIGHEST_EDUCATION_LEVEL | PersonLegislativeInfoDPEOHighestEducationLevel | ✅ |
| LAST_UPDATE_DATE | PersonLegislativeInfoDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonLegislativeInfoDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PersonLegislativeInfoDPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PersonLegislativeInfoDPEOLegislationCode | ✅ |
| MARITAL_STATUS | PersonLegislativeInfoDPEOMaritalStatus | ✅ |
| MARITAL_STATUS_DATE | PersonLegislativeInfoDPEOMaritalStatusDate | ✅ |
| OBJECT_VERSION_NUMBER | PersonLegislativeInfoDPEOObjectVersionNumber | ✅ |
| PER_INFORMATION1 | PersonLegislativeInfoDPEOInformation1 | — |
| PER_INFORMATION10 | PersonLegislativeInfoDPEOInformation10 | ✅ |
| PER_INFORMATION11 | PersonLegislativeInfoDPEOInformation11 | ✅ |
| PER_INFORMATION12 | PersonLegislativeInfoDPEOInformation12 | ✅ |
| PER_INFORMATION13 | PersonLegislativeInfoDPEOInformation13 | ✅ |
| PER_INFORMATION14 | PersonLegislativeInfoDPEOInformation14 | ✅ |
| PER_INFORMATION15 | PersonLegislativeInfoDPEOInformation15 | ✅ |
| PER_INFORMATION16 | PersonLegislativeInfoDPEOInformation16 | ✅ |
| PER_INFORMATION17 | PersonLegislativeInfoDPEOInformation17 | ✅ |
| PER_INFORMATION18 | PersonLegislativeInfoDPEOInformation18 | ✅ |
| PER_INFORMATION19 | PersonLegislativeInfoDPEOInformation19 | ✅ |
| PER_INFORMATION2 | PersonLegislativeInfoDPEOInformation2 | — |
| PER_INFORMATION20 | PersonLegislativeInfoDPEOInformation20 | — |
| PER_INFORMATION21 | PersonLegislativeInfoDPEOInformation21 | — |
| PER_INFORMATION22 | PersonLegislativeInfoDPEOInformation22 | — |
| PER_INFORMATION23 | PersonLegislativeInfoDPEOInformation23 | — |
| PER_INFORMATION24 | PersonLegislativeInfoDPEOInformation24 | — |
| PER_INFORMATION25 | PersonLegislativeInfoDPEOInformation25 | — |
| PER_INFORMATION26 | PersonLegislativeInfoDPEOInformation26 | — |
| PER_INFORMATION27 | PersonLegislativeInfoDPEOInformation27 | — |
| PER_INFORMATION28 | PersonLegislativeInfoDPEOInformation28 | — |
| PER_INFORMATION29 | PersonLegislativeInfoDPEOInformation29 | — |
| PER_INFORMATION3 | PersonLegislativeInfoDPEOInformation3 | — |
| PER_INFORMATION30 | PersonLegislativeInfoDPEOInformation30 | — |
| PER_INFORMATION4 | PersonLegislativeInfoDPEOInformation4 | — |
| PER_INFORMATION5 | PersonLegislativeInfoDPEOInformation5 | — |
| PER_INFORMATION6 | PersonLegislativeInfoDPEOInformation6 | — |
| PER_INFORMATION7 | PersonLegislativeInfoDPEOInformation7 | — |
| PER_INFORMATION8 | PersonLegislativeInfoDPEOInformation8 | — |
| PER_INFORMATION9 | PersonLegislativeInfoDPEOInformation9 | — |
| PER_INFORMATION_CATEGORY | PersonLegislativeInfoDPEOInformationCategory | ✅ |
| PER_INFORMATION_DATE1 | PersonLegislativeInfoDPEOInformationDate1 | — |
| PER_INFORMATION_DATE10 | PersonLegislativeInfoDPEOInformationDate10 | — |
| PER_INFORMATION_DATE11 | PersonLegislativeInfoDPEOInformationDate11 | — |
| PER_INFORMATION_DATE12 | PersonLegislativeInfoDPEOInformationDate12 | — |
| PER_INFORMATION_DATE13 | PersonLegislativeInfoDPEOInformationDate13 | — |
| PER_INFORMATION_DATE14 | PersonLegislativeInfoDPEOInformationDate14 | — |
| PER_INFORMATION_DATE15 | PersonLegislativeInfoDPEOInformationDate15 | — |
| PER_INFORMATION_DATE2 | PersonLegislativeInfoDPEOInformationDate2 | — |
| PER_INFORMATION_DATE3 | PersonLegislativeInfoDPEOInformationDate3 | — |
| PER_INFORMATION_DATE4 | PersonLegislativeInfoDPEOInformationDate4 | — |
| PER_INFORMATION_DATE5 | PersonLegislativeInfoDPEOInformationDate5 | — |
| PER_INFORMATION_DATE6 | PersonLegislativeInfoDPEOInformationDate6 | — |
| PER_INFORMATION_DATE7 | PersonLegislativeInfoDPEOInformationDate7 | — |
| PER_INFORMATION_DATE8 | PersonLegislativeInfoDPEOInformationDate8 | — |
| PER_INFORMATION_DATE9 | PersonLegislativeInfoDPEOInformationDate9 | — |
| PER_INFORMATION_NUMBER1 | PersonLegislativeInfoDPEOInformationNumber1 | — |
| PER_INFORMATION_NUMBER10 | PersonLegislativeInfoDPEOInformationNumber10 | — |
| PER_INFORMATION_NUMBER11 | PersonLegislativeInfoDPEOInformationNumber11 | — |
| PER_INFORMATION_NUMBER12 | PersonLegislativeInfoDPEOInformationNumber12 | — |
| PER_INFORMATION_NUMBER13 | PersonLegislativeInfoDPEOInformationNumber13 | — |
| PER_INFORMATION_NUMBER14 | PersonLegislativeInfoDPEOInformationNumber14 | — |
| PER_INFORMATION_NUMBER15 | PersonLegislativeInfoDPEOInformationNumber15 | — |
| PER_INFORMATION_NUMBER16 | PersonLegislativeInfoDPEOInformationNumber16 | — |
| PER_INFORMATION_NUMBER17 | PersonLegislativeInfoDPEOInformationNumber17 | — |
| PER_INFORMATION_NUMBER18 | PersonLegislativeInfoDPEOInformationNumber18 | — |
| PER_INFORMATION_NUMBER19 | PersonLegislativeInfoDPEOInformationNumber19 | — |
| PER_INFORMATION_NUMBER2 | PersonLegislativeInfoDPEOInformationNumber2 | — |
| PER_INFORMATION_NUMBER20 | PersonLegislativeInfoDPEOInformationNumber20 | — |
| PER_INFORMATION_NUMBER3 | PersonLegislativeInfoDPEOInformationNumber3 | — |
| PER_INFORMATION_NUMBER4 | PersonLegislativeInfoDPEOInformationNumber4 | — |
| PER_INFORMATION_NUMBER5 | PersonLegislativeInfoDPEOInformationNumber5 | — |
| PER_INFORMATION_NUMBER6 | PersonLegislativeInfoDPEOInformationNumber6 | — |
| PER_INFORMATION_NUMBER7 | PersonLegislativeInfoDPEOInformationNumber7 | — |
| PER_INFORMATION_NUMBER8 | PersonLegislativeInfoDPEOInformationNumber8 | — |
| PER_INFORMATION_NUMBER9 | PersonLegislativeInfoDPEOInformationNumber9 | — |
| PERSON_ID | PersonLegislativeInfoDPEOPersonId | ✅ |
| PERSON_LEGISLATIVE_ID | PersonLegislativeId | ✅ |
| SEX | PersonLegislativeInfoDPEOSex | ✅ |

### [[personlegislativeinfopvoviewall|PersonLegislativeInfoPVOViewAll]] (HCM · BICC: 13/148)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PersonLegislativeInfoDPEOAttribute1 | — |
| ATTRIBUTE10 | PersonLegislativeInfoDPEOAttribute10 | — |
| ATTRIBUTE11 | PersonLegislativeInfoDPEOAttribute11 | — |
| ATTRIBUTE12 | PersonLegislativeInfoDPEOAttribute12 | — |
| ATTRIBUTE13 | PersonLegislativeInfoDPEOAttribute13 | — |
| ATTRIBUTE14 | PersonLegislativeInfoDPEOAttribute14 | — |
| ATTRIBUTE15 | PersonLegislativeInfoDPEOAttribute15 | — |
| ATTRIBUTE16 | PersonLegislativeInfoDPEOAttribute16 | — |
| ATTRIBUTE17 | PersonLegislativeInfoDPEOAttribute17 | — |
| ATTRIBUTE18 | PersonLegislativeInfoDPEOAttribute18 | — |
| ATTRIBUTE19 | PersonLegislativeInfoDPEOAttribute19 | — |
| ATTRIBUTE2 | PersonLegislativeInfoDPEOAttribute2 | — |
| ATTRIBUTE20 | PersonLegislativeInfoDPEOAttribute20 | — |
| ATTRIBUTE21 | PersonLegislativeInfoDPEOAttribute21 | — |
| ATTRIBUTE22 | PersonLegislativeInfoDPEOAttribute22 | — |
| ATTRIBUTE23 | PersonLegislativeInfoDPEOAttribute23 | — |
| ATTRIBUTE24 | PersonLegislativeInfoDPEOAttribute24 | — |
| ATTRIBUTE25 | PersonLegislativeInfoDPEOAttribute25 | — |
| ATTRIBUTE26 | PersonLegislativeInfoDPEOAttribute26 | — |
| ATTRIBUTE27 | PersonLegislativeInfoDPEOAttribute27 | — |
| ATTRIBUTE28 | PersonLegislativeInfoDPEOAttribute28 | — |
| ATTRIBUTE29 | PersonLegislativeInfoDPEOAttribute29 | — |
| ATTRIBUTE3 | PersonLegislativeInfoDPEOAttribute3 | — |
| ATTRIBUTE30 | PersonLegislativeInfoDPEOAttribute30 | — |
| ATTRIBUTE4 | PersonLegislativeInfoDPEOAttribute4 | — |
| ATTRIBUTE5 | PersonLegislativeInfoDPEOAttribute5 | — |
| ATTRIBUTE6 | PersonLegislativeInfoDPEOAttribute6 | — |
| ATTRIBUTE7 | PersonLegislativeInfoDPEOAttribute7 | — |
| ATTRIBUTE8 | PersonLegislativeInfoDPEOAttribute8 | — |
| ATTRIBUTE9 | PersonLegislativeInfoDPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PersonLegislativeInfoDPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PersonLegislativeInfoDPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PersonLegislativeInfoDPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PersonLegislativeInfoDPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PersonLegislativeInfoDPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PersonLegislativeInfoDPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PersonLegislativeInfoDPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PersonLegislativeInfoDPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PersonLegislativeInfoDPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PersonLegislativeInfoDPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PersonLegislativeInfoDPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PersonLegislativeInfoDPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PersonLegislativeInfoDPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PersonLegislativeInfoDPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PersonLegislativeInfoDPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PersonLegislativeInfoDPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PersonLegislativeInfoDPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PersonLegislativeInfoDPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PersonLegislativeInfoDPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PersonLegislativeInfoDPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PersonLegislativeInfoDPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PersonLegislativeInfoDPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PersonLegislativeInfoDPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PersonLegislativeInfoDPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PersonLegislativeInfoDPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PersonLegislativeInfoDPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PersonLegislativeInfoDPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PersonLegislativeInfoDPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PersonLegislativeInfoDPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PersonLegislativeInfoDPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PersonLegislativeInfoDPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PersonLegislativeInfoDPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PersonLegislativeInfoDPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PersonLegislativeInfoDPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PersonLegislativeInfoDPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PersonLegislativeInfoDPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | PersonLegislativeInfoDPEOBusinessGroupId | — |
| CREATED_BY | PersonLegislativeInfoDPEOCreatedBy | ✅ |
| CREATION_DATE | PersonLegislativeInfoDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| HIGHEST_EDUCATION_LEVEL | PersonLegislativeInfoDPEOHighestEducationLevel | ✅ |
| LAST_UPDATE_DATE | PersonLegislativeInfoDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonLegislativeInfoDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonLegislativeInfoDPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PersonLegislativeInfoDPEOLegislationCode | ✅ |
| MARITAL_STATUS | PersonLegislativeInfoDPEOMaritalStatus | ✅ |
| MARITAL_STATUS_DATE | PersonLegislativeInfoDPEOMaritalStatusDate | ✅ |
| OBJECT_VERSION_NUMBER | PersonLegislativeInfoDPEOObjectVersionNumber | — |
| PER_INFORMATION1 | PersonLegislativeInfoDPEOInformation1 | — |
| PER_INFORMATION10 | PersonLegislativeInfoDPEOInformation10 | — |
| PER_INFORMATION11 | PersonLegislativeInfoDPEOInformation11 | — |
| PER_INFORMATION12 | PersonLegislativeInfoDPEOInformation12 | — |
| PER_INFORMATION13 | PersonLegislativeInfoDPEOInformation13 | — |
| PER_INFORMATION14 | PersonLegislativeInfoDPEOInformation14 | — |
| PER_INFORMATION15 | PersonLegislativeInfoDPEOInformation15 | — |
| PER_INFORMATION16 | PersonLegislativeInfoDPEOInformation16 | — |
| PER_INFORMATION17 | PersonLegislativeInfoDPEOInformation17 | — |
| PER_INFORMATION18 | PersonLegislativeInfoDPEOInformation18 | — |
| PER_INFORMATION19 | PersonLegislativeInfoDPEOInformation19 | — |
| PER_INFORMATION2 | PersonLegislativeInfoDPEOInformation2 | — |
| PER_INFORMATION20 | PersonLegislativeInfoDPEOInformation20 | — |
| PER_INFORMATION21 | PersonLegislativeInfoDPEOInformation21 | — |
| PER_INFORMATION22 | PersonLegislativeInfoDPEOInformation22 | — |
| PER_INFORMATION23 | PersonLegislativeInfoDPEOInformation23 | — |
| PER_INFORMATION24 | PersonLegislativeInfoDPEOInformation24 | — |
| PER_INFORMATION25 | PersonLegislativeInfoDPEOInformation25 | — |
| PER_INFORMATION26 | PersonLegislativeInfoDPEOInformation26 | — |
| PER_INFORMATION27 | PersonLegislativeInfoDPEOInformation27 | — |
| PER_INFORMATION28 | PersonLegislativeInfoDPEOInformation28 | — |
| PER_INFORMATION29 | PersonLegislativeInfoDPEOInformation29 | — |
| PER_INFORMATION3 | PersonLegislativeInfoDPEOInformation3 | — |
| PER_INFORMATION30 | PersonLegislativeInfoDPEOInformation30 | — |
| PER_INFORMATION4 | PersonLegislativeInfoDPEOInformation4 | — |
| PER_INFORMATION5 | PersonLegislativeInfoDPEOInformation5 | — |
| PER_INFORMATION6 | PersonLegislativeInfoDPEOInformation6 | — |
| PER_INFORMATION7 | PersonLegislativeInfoDPEOInformation7 | — |
| PER_INFORMATION8 | PersonLegislativeInfoDPEOInformation8 | — |
| PER_INFORMATION9 | PersonLegislativeInfoDPEOInformation9 | — |
| PER_INFORMATION_CATEGORY | PersonLegislativeInfoDPEOInformationCategory | — |
| PER_INFORMATION_DATE1 | PersonLegislativeInfoDPEOInformationDate1 | — |
| PER_INFORMATION_DATE10 | PersonLegislativeInfoDPEOInformationDate10 | — |
| PER_INFORMATION_DATE11 | PersonLegislativeInfoDPEOInformationDate11 | — |
| PER_INFORMATION_DATE12 | PersonLegislativeInfoDPEOInformationDate12 | — |
| PER_INFORMATION_DATE13 | PersonLegislativeInfoDPEOInformationDate13 | — |
| PER_INFORMATION_DATE14 | PersonLegislativeInfoDPEOInformationDate14 | — |
| PER_INFORMATION_DATE15 | PersonLegislativeInfoDPEOInformationDate15 | — |
| PER_INFORMATION_DATE2 | PersonLegislativeInfoDPEOInformationDate2 | — |
| PER_INFORMATION_DATE3 | PersonLegislativeInfoDPEOInformationDate3 | — |
| PER_INFORMATION_DATE4 | PersonLegislativeInfoDPEOInformationDate4 | — |
| PER_INFORMATION_DATE5 | PersonLegislativeInfoDPEOInformationDate5 | — |
| PER_INFORMATION_DATE6 | PersonLegislativeInfoDPEOInformationDate6 | — |
| PER_INFORMATION_DATE7 | PersonLegislativeInfoDPEOInformationDate7 | — |
| PER_INFORMATION_DATE8 | PersonLegislativeInfoDPEOInformationDate8 | — |
| PER_INFORMATION_DATE9 | PersonLegislativeInfoDPEOInformationDate9 | — |
| PER_INFORMATION_NUMBER1 | PersonLegislativeInfoDPEOInformationNumber1 | — |
| PER_INFORMATION_NUMBER10 | PersonLegislativeInfoDPEOInformationNumber10 | — |
| PER_INFORMATION_NUMBER11 | PersonLegislativeInfoDPEOInformationNumber11 | — |
| PER_INFORMATION_NUMBER12 | PersonLegislativeInfoDPEOInformationNumber12 | — |
| PER_INFORMATION_NUMBER13 | PersonLegislativeInfoDPEOInformationNumber13 | — |
| PER_INFORMATION_NUMBER14 | PersonLegislativeInfoDPEOInformationNumber14 | — |
| PER_INFORMATION_NUMBER15 | PersonLegislativeInfoDPEOInformationNumber15 | — |
| PER_INFORMATION_NUMBER16 | PersonLegislativeInfoDPEOInformationNumber16 | — |
| PER_INFORMATION_NUMBER17 | PersonLegislativeInfoDPEOInformationNumber17 | — |
| PER_INFORMATION_NUMBER18 | PersonLegislativeInfoDPEOInformationNumber18 | — |
| PER_INFORMATION_NUMBER19 | PersonLegislativeInfoDPEOInformationNumber19 | — |
| PER_INFORMATION_NUMBER2 | PersonLegislativeInfoDPEOInformationNumber2 | — |
| PER_INFORMATION_NUMBER20 | PersonLegislativeInfoDPEOInformationNumber20 | — |
| PER_INFORMATION_NUMBER3 | PersonLegislativeInfoDPEOInformationNumber3 | — |
| PER_INFORMATION_NUMBER4 | PersonLegislativeInfoDPEOInformationNumber4 | — |
| PER_INFORMATION_NUMBER5 | PersonLegislativeInfoDPEOInformationNumber5 | — |
| PER_INFORMATION_NUMBER6 | PersonLegislativeInfoDPEOInformationNumber6 | — |
| PER_INFORMATION_NUMBER7 | PersonLegislativeInfoDPEOInformationNumber7 | — |
| PER_INFORMATION_NUMBER8 | PersonLegislativeInfoDPEOInformationNumber8 | — |
| PER_INFORMATION_NUMBER9 | PersonLegislativeInfoDPEOInformationNumber9 | — |
| PERSON_ID | PersonLegislativeInfoDPEOPersonId | ✅ |
| PERSON_LEGISLATIVE_ID | PersonLegislativeId | ✅ |
| SEX | PersonLegislativeInfoDPEOSex | ✅ |
