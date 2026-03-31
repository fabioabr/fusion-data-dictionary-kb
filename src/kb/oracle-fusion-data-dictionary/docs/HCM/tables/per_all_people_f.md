---
id: DOC-HCM-627
doc_type: system-doc
title: "PER_ALL_PEOPLE_F — Pessoas (Cadastro Principal)"
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
  - workforce-management
  - pessoas
  - cadastro
  - people
aliases:
  - PER_ALL_PEOPLE_F
  - per_all_people_f
  - per-all-people-f
  - pessoas-(cadastro-principal)
  - per-all-people-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALL_PEOPLE_F

## 📌 Visão Geral

Tabela **principal de cadastro de pessoas** no Oracle HCM. Armazena dados pessoais de todos os tipos de pessoas: colaboradores, contingentes, candidatos e contatos. É a tabela central de identidade no módulo HCM, com controle de vigência temporal.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro central** — dados pessoais de todos os colaboradores e pessoas relacionadas.
- **Identidade** — nome, data de nascimento, gênero e informações demográficas.
- **Integração** — chave de ligação com praticamente todas as tabelas de HCM.
- **Compliance LGPD** — contém dados pessoais sensíveis sujeitos a proteção.
- **Relatórios de workforce** — base para headcount e análises demográficas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pessoa | — | 🟢 95% |
| 2 | PERSON_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número/matrícula da pessoa | — | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | FIRST_NAME | VARCHAR2(150) | NULL | Dados Pessoais | Primeiro nome | — | 🟢 95% |
| 6 | LAST_NAME | VARCHAR2(150) | NOT NULL | Dados Pessoais | Sobrenome | — | 🟢 95% |
| 7 | FULL_NAME | VARCHAR2(360) | NULL | Dados Pessoais | Nome completo | — | 🟢 90% |
| 8 | DATE_OF_BIRTH | DATE | NULL | Dados Pessoais | Data de nascimento | — | 🟢 90% |
| 9 | SEX | VARCHAR2(30) | NULL | Dados Pessoais | Gênero | — | 🟢 85% |
| 10 | NATIONAL_IDENTIFIER | VARCHAR2(30) | NULL | Identificação | Identificador nacional (CPF) | — | 🟢 85% |
| 11 | PERSON_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de pessoa | — | 🟢 85% |
| 12 | START_DATE | DATE | NULL | Vigência | Data de início | — | 🟢 90% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 17 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de cadastro de pessoas.

### Tabelas-filha (FK de saída)
- [[per_all_assignments_m]] — via `PERSON_ID` (vínculos empregatícios da pessoa)
- [[per_addresses_f]] — via `PERSON_ID` (endereços do colaborador)
- [[per_email_addresses]] — via `PERSON_ID` (endereços de e-mail do colaborador)
- [[per_contact_relships_f]] — via `PERSON_ID` (contatos/dependentes)
- [[per_citizenships]] — via `PERSON_ID` (cidadanias e nacionalidades do colaborador)
- [[per_disabilities_f]] — via `PERSON_ID` (registros de deficiência do colaborador)
- [[per_ethnicities]] — via `PERSON_ID` (informações de etnia do colaborador)
- [[per_drivers_licenses]] — via `PERSON_ID` (carteiras de habilitação do colaborador)

---

## 📎 Uso Típico

### Dados de um colaborador
```sql
SELECT ppf.PERSON_NUMBER, ppf.FULL_NAME, ppf.DATE_OF_BIRTH, ppf.SEX
FROM   PER_ALL_PEOPLE_F ppf
WHERE  ppf.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN ppf.EFFECTIVE_START_DATE AND ppf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registro vigente
- `PERSON_NUMBER = :p_matricula` — Busca por matrícula
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência para dados correntes.
- Contém dados sensíveis (LGPD/GDPR) — acesso deve ser controlado.
- O `NATIONAL_IDENTIFIER` armazena o CPF no contexto brasileiro.
- É a tabela mais referenciada do HCM — praticamente todas as tabelas possuem FK para ela.
- O `PERSON_NUMBER` é a matrícula visível para o usuário.
---

## 🔗 PVOs Relacionados

### [[absencetimeentrypvo|AbsenceTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonApplicantNumber | — |
| BUSINESS_GROUP_ID | PersonBusinessGroupId | — |
| CREATED_BY | PersonCreatedBy | — |
| CREATION_DATE | PersonCreationDate | — |
| EFFECTIVE_END_DATE | PersonEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonLastUpdatedBy | — |
| MAILING_ADDRESS_ID | PersonMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonObjectVersionNumber | — |
| PERSON_ID | PersonPersonId | — |
| PERSON_NUMBER | PersonPersonNumber | — |
| PRIMARY_EMAIL_ID | PersonPrimaryEmailId | — |
| PRIMARY_NID_ID | PersonPrimaryNidId | — |
| PRIMARY_NID_NUMBER | PersonPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonPrimaryPhoneId | — |
| START_DATE | PersonStartDate | — |
| WAIVE_DATA_PROTECT | PersonWaiveDataProtect | — |

### [[allocatedchecklistspvo|AllocatedChecklistsPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[awardpersonnelpipvo|AwardPersonnelPIPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | — |
| PERSON_ID | PersonDPEOPersonId | — |
| PERSON_NUMBER | PersonDPEOPersonNumber | — |

### [[billchargedetailspvo|BillChargeDetailsPVO]] (HCM · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate1 | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| PERSON_ID | PersonId2 | — |

### [[billchargepaymentspvo|BillChargePaymentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId3 | — |

### [[billchargespvo|BillChargesPVO]] (HCM · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate1 | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| PERSON_ID | PersonId2 | — |

### [[billpaymentspvo|BillPaymentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId2 | — |

### [[candidateinteractionpvo|CandidateInteractionPVO]] (HCM · BICC: 3/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| ATTRIBUTE1 | Attribute112 | — |
| ATTRIBUTE10 | Attribute102 | — |
| ATTRIBUTE11 | Attribute113 | — |
| ATTRIBUTE12 | Attribute122 | — |
| ATTRIBUTE13 | Attribute132 | — |
| ATTRIBUTE14 | Attribute142 | — |
| ATTRIBUTE15 | Attribute152 | — |
| ATTRIBUTE16 | Attribute162 | — |
| ATTRIBUTE17 | Attribute172 | — |
| ATTRIBUTE18 | Attribute182 | — |
| ATTRIBUTE19 | Attribute192 | — |
| ATTRIBUTE2 | Attribute212 | — |
| ATTRIBUTE20 | Attribute202 | — |
| ATTRIBUTE21 | Attribute213 | — |
| ATTRIBUTE22 | Attribute222 | — |
| ATTRIBUTE23 | Attribute232 | — |
| ATTRIBUTE24 | Attribute242 | — |
| ATTRIBUTE25 | Attribute252 | — |
| ATTRIBUTE26 | Attribute262 | — |
| ATTRIBUTE27 | Attribute272 | — |
| ATTRIBUTE28 | Attribute282 | — |
| ATTRIBUTE29 | Attribute292 | — |
| ATTRIBUTE3 | Attribute32 | — |
| ATTRIBUTE30 | Attribute302 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute42 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute52 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute62 | — |
| ATTRIBUTE7 | Attribute72 | — |
| ATTRIBUTE8 | Attribute82 | — |
| ATTRIBUTE9 | Attribute92 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory2 | — |
| ATTRIBUTE_DATE1 | AttributeDate17 | — |
| ATTRIBUTE_DATE10 | AttributeDate102 | — |
| ATTRIBUTE_DATE11 | AttributeDate112 | — |
| ATTRIBUTE_DATE12 | AttributeDate122 | — |
| ATTRIBUTE_DATE13 | AttributeDate132 | — |
| ATTRIBUTE_DATE14 | AttributeDate142 | — |
| ATTRIBUTE_DATE15 | AttributeDate152 | — |
| ATTRIBUTE_DATE2 | AttributeDate22 | — |
| ATTRIBUTE_DATE3 | AttributeDate32 | — |
| ATTRIBUTE_DATE4 | AttributeDate42 | — |
| ATTRIBUTE_DATE5 | AttributeDate52 | — |
| ATTRIBUTE_DATE6 | AttributeDate62 | — |
| ATTRIBUTE_DATE7 | AttributeDate72 | — |
| ATTRIBUTE_DATE8 | AttributeDate82 | — |
| ATTRIBUTE_DATE9 | AttributeDate92 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber102 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber22 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber202 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber32 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber42 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber52 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber62 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber72 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber82 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber92 | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PERSON_ID | PersonId3 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[candidatepoolinteractionpvo|CandidatePoolInteractionPVO]] (HCM · BICC: 3/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| ATTRIBUTE1 | Attribute112 | — |
| ATTRIBUTE10 | Attribute102 | — |
| ATTRIBUTE11 | Attribute113 | — |
| ATTRIBUTE12 | Attribute122 | — |
| ATTRIBUTE13 | Attribute132 | — |
| ATTRIBUTE14 | Attribute142 | — |
| ATTRIBUTE15 | Attribute152 | — |
| ATTRIBUTE16 | Attribute162 | — |
| ATTRIBUTE17 | Attribute172 | — |
| ATTRIBUTE18 | Attribute182 | — |
| ATTRIBUTE19 | Attribute192 | — |
| ATTRIBUTE2 | Attribute212 | — |
| ATTRIBUTE20 | Attribute202 | — |
| ATTRIBUTE21 | Attribute213 | — |
| ATTRIBUTE22 | Attribute222 | — |
| ATTRIBUTE23 | Attribute232 | — |
| ATTRIBUTE24 | Attribute242 | — |
| ATTRIBUTE25 | Attribute252 | — |
| ATTRIBUTE26 | Attribute262 | — |
| ATTRIBUTE27 | Attribute272 | — |
| ATTRIBUTE28 | Attribute282 | — |
| ATTRIBUTE29 | Attribute292 | — |
| ATTRIBUTE3 | Attribute32 | — |
| ATTRIBUTE30 | Attribute302 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute42 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute52 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute62 | — |
| ATTRIBUTE7 | Attribute72 | — |
| ATTRIBUTE8 | Attribute82 | — |
| ATTRIBUTE9 | Attribute92 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory2 | — |
| ATTRIBUTE_DATE1 | AttributeDate17 | — |
| ATTRIBUTE_DATE10 | AttributeDate102 | — |
| ATTRIBUTE_DATE11 | AttributeDate112 | — |
| ATTRIBUTE_DATE12 | AttributeDate122 | — |
| ATTRIBUTE_DATE13 | AttributeDate132 | — |
| ATTRIBUTE_DATE14 | AttributeDate142 | — |
| ATTRIBUTE_DATE15 | AttributeDate152 | — |
| ATTRIBUTE_DATE2 | AttributeDate22 | — |
| ATTRIBUTE_DATE3 | AttributeDate32 | — |
| ATTRIBUTE_DATE4 | AttributeDate42 | — |
| ATTRIBUTE_DATE5 | AttributeDate52 | — |
| ATTRIBUTE_DATE6 | AttributeDate62 | — |
| ATTRIBUTE_DATE7 | AttributeDate72 | — |
| ATTRIBUTE_DATE8 | AttributeDate82 | — |
| ATTRIBUTE_DATE9 | AttributeDate92 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber102 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber22 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber202 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber32 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber42 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber52 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber62 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber72 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber82 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber92 | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PERSON_ID | PersonId3 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[candidatepvo|CandidatePVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | DeletedByPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DeletedByPersonDetailsPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | — |
| PERSON_ID | DeletedByPersonDetailsPEOPersonId | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | DeletedByPersonDetailsPEOPersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[checkintemplateeligibilitypvo|CheckinTemplateEligibilityPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId | — |
| PERSON_NUMBER | PersonNumber | — |

### [[contactemailaddressespvo|ContactEmailAddressesPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |
| PRIMARY_EMAIL_ID | ContactPersonDetailsPEOPrimaryEmailId | — |

### [[contactpassportspvo|ContactPassportsPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |

### [[contactpersonaddresspvo|ContactPersonAddressPVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| MAILING_ADDRESS_ID | ContactPersonDetailsPEOMailingAddressId | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |

### [[contactpersondisabilitypvo|ContactPersonDisabilityPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |

### [[contactpersonnationalidentifierpvo|ContactPersonNationalIdentifierPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |
| PRIMARY_NID_ID | ContactPersonDetailsPEOPrimaryNidId | — |

### [[contactphonespvo|ContactPhonesPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |
| PRIMARY_PHONE_ID | ContactPersonDetailsPEOPrimaryPhoneId | — |

### [[contactrelshipspvo|ContactRelshipsPVO]] (HCM · BICC: 3/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| ATTRIBUTE1 | PersonDetailsPEOAttribute1 | — |
| ATTRIBUTE10 | PersonDetailsPEOAttribute10 | — |
| ATTRIBUTE11 | PersonDetailsPEOAttribute11 | — |
| ATTRIBUTE12 | PersonDetailsPEOAttribute12 | — |
| ATTRIBUTE13 | PersonDetailsPEOAttribute13 | — |
| ATTRIBUTE14 | PersonDetailsPEOAttribute14 | — |
| ATTRIBUTE15 | PersonDetailsPEOAttribute15 | — |
| ATTRIBUTE16 | PersonDetailsPEOAttribute16 | — |
| ATTRIBUTE17 | PersonDetailsPEOAttribute17 | — |
| ATTRIBUTE18 | PersonDetailsPEOAttribute18 | — |
| ATTRIBUTE19 | PersonDetailsPEOAttribute19 | — |
| ATTRIBUTE2 | PersonDetailsPEOAttribute2 | — |
| ATTRIBUTE20 | PersonDetailsPEOAttribute20 | — |
| ATTRIBUTE21 | PersonDetailsPEOAttribute21 | — |
| ATTRIBUTE22 | PersonDetailsPEOAttribute22 | — |
| ATTRIBUTE23 | PersonDetailsPEOAttribute23 | — |
| ATTRIBUTE24 | PersonDetailsPEOAttribute24 | — |
| ATTRIBUTE25 | PersonDetailsPEOAttribute25 | — |
| ATTRIBUTE26 | PersonDetailsPEOAttribute26 | — |
| ATTRIBUTE27 | PersonDetailsPEOAttribute27 | — |
| ATTRIBUTE28 | PersonDetailsPEOAttribute28 | — |
| ATTRIBUTE29 | PersonDetailsPEOAttribute29 | — |
| ATTRIBUTE3 | PersonDetailsPEOAttribute3 | — |
| ATTRIBUTE30 | PersonDetailsPEOAttribute30 | — |
| ATTRIBUTE31 | PersonDetailsPEOAttribute31 | — |
| ATTRIBUTE32 | PersonDetailsPEOAttribute32 | — |
| ATTRIBUTE33 | PersonDetailsPEOAttribute33 | — |
| ATTRIBUTE34 | PersonDetailsPEOAttribute34 | — |
| ATTRIBUTE35 | PersonDetailsPEOAttribute35 | — |
| ATTRIBUTE36 | PersonDetailsPEOAttribute36 | — |
| ATTRIBUTE37 | PersonDetailsPEOAttribute37 | — |
| ATTRIBUTE38 | PersonDetailsPEOAttribute38 | — |
| ATTRIBUTE39 | PersonDetailsPEOAttribute39 | — |
| ATTRIBUTE4 | PersonDetailsPEOAttribute4 | — |
| ATTRIBUTE40 | PersonDetailsPEOAttribute40 | — |
| ATTRIBUTE41 | PersonDetailsPEOAttribute41 | — |
| ATTRIBUTE42 | PersonDetailsPEOAttribute42 | — |
| ATTRIBUTE43 | PersonDetailsPEOAttribute43 | — |
| ATTRIBUTE44 | PersonDetailsPEOAttribute44 | — |
| ATTRIBUTE45 | PersonDetailsPEOAttribute45 | — |
| ATTRIBUTE46 | PersonDetailsPEOAttribute46 | — |
| ATTRIBUTE47 | PersonDetailsPEOAttribute47 | — |
| ATTRIBUTE48 | PersonDetailsPEOAttribute48 | — |
| ATTRIBUTE49 | PersonDetailsPEOAttribute49 | — |
| ATTRIBUTE5 | PersonDetailsPEOAttribute5 | — |
| ATTRIBUTE50 | PersonDetailsPEOAttribute50 | — |
| ATTRIBUTE6 | PersonDetailsPEOAttribute6 | — |
| ATTRIBUTE7 | PersonDetailsPEOAttribute7 | — |
| ATTRIBUTE8 | PersonDetailsPEOAttribute8 | — |
| ATTRIBUTE9 | PersonDetailsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PersonDetailsPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PersonDetailsPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PersonDetailsPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PersonDetailsPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PersonDetailsPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PersonDetailsPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PersonDetailsPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PersonDetailsPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PersonDetailsPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PersonDetailsPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PersonDetailsPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PersonDetailsPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PersonDetailsPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PersonDetailsPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PersonDetailsPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PersonDetailsPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PersonDetailsPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PersonDetailsPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PersonDetailsPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PersonDetailsPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PersonDetailsPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PersonDetailsPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PersonDetailsPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PersonDetailsPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PersonDetailsPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PersonDetailsPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PersonDetailsPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PersonDetailsPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PersonDetailsPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PersonDetailsPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PersonDetailsPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PersonDetailsPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PersonDetailsPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PersonDetailsPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PersonDetailsPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PersonDetailsPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | — |
| CREATED_BY | PersonDetailsPEOCreatedBy | — |
| CREATION_DATE | PersonDetailsPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate1 | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |
| START_DATE | PersonDetailsPEOStartDate | — |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | — |

### [[contactrelshipspvoviewall|ContactRelshipsPVOViewAll]] (HCM · BICC: 11/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| ATTRIBUTE1 | PersonDetailsPEOAttribute1 | — |
| ATTRIBUTE10 | PersonDetailsPEOAttribute10 | — |
| ATTRIBUTE11 | PersonDetailsPEOAttribute11 | — |
| ATTRIBUTE12 | PersonDetailsPEOAttribute12 | — |
| ATTRIBUTE13 | PersonDetailsPEOAttribute13 | — |
| ATTRIBUTE14 | PersonDetailsPEOAttribute14 | — |
| ATTRIBUTE15 | PersonDetailsPEOAttribute15 | — |
| ATTRIBUTE16 | PersonDetailsPEOAttribute16 | — |
| ATTRIBUTE17 | PersonDetailsPEOAttribute17 | — |
| ATTRIBUTE18 | PersonDetailsPEOAttribute18 | — |
| ATTRIBUTE19 | PersonDetailsPEOAttribute19 | — |
| ATTRIBUTE2 | PersonDetailsPEOAttribute2 | — |
| ATTRIBUTE20 | PersonDetailsPEOAttribute20 | — |
| ATTRIBUTE21 | PersonDetailsPEOAttribute21 | — |
| ATTRIBUTE22 | PersonDetailsPEOAttribute22 | — |
| ATTRIBUTE23 | PersonDetailsPEOAttribute23 | — |
| ATTRIBUTE24 | PersonDetailsPEOAttribute24 | — |
| ATTRIBUTE25 | PersonDetailsPEOAttribute25 | — |
| ATTRIBUTE26 | PersonDetailsPEOAttribute26 | — |
| ATTRIBUTE27 | PersonDetailsPEOAttribute27 | — |
| ATTRIBUTE28 | PersonDetailsPEOAttribute28 | — |
| ATTRIBUTE29 | PersonDetailsPEOAttribute29 | — |
| ATTRIBUTE3 | PersonDetailsPEOAttribute3 | — |
| ATTRIBUTE30 | PersonDetailsPEOAttribute30 | — |
| ATTRIBUTE31 | PersonDetailsPEOAttribute31 | — |
| ATTRIBUTE32 | PersonDetailsPEOAttribute32 | — |
| ATTRIBUTE33 | PersonDetailsPEOAttribute33 | — |
| ATTRIBUTE34 | PersonDetailsPEOAttribute34 | — |
| ATTRIBUTE35 | PersonDetailsPEOAttribute35 | — |
| ATTRIBUTE36 | PersonDetailsPEOAttribute36 | — |
| ATTRIBUTE37 | PersonDetailsPEOAttribute37 | — |
| ATTRIBUTE38 | PersonDetailsPEOAttribute38 | — |
| ATTRIBUTE39 | PersonDetailsPEOAttribute39 | — |
| ATTRIBUTE4 | PersonDetailsPEOAttribute4 | — |
| ATTRIBUTE40 | PersonDetailsPEOAttribute40 | — |
| ATTRIBUTE41 | PersonDetailsPEOAttribute41 | — |
| ATTRIBUTE42 | PersonDetailsPEOAttribute42 | — |
| ATTRIBUTE43 | PersonDetailsPEOAttribute43 | — |
| ATTRIBUTE44 | PersonDetailsPEOAttribute44 | — |
| ATTRIBUTE45 | PersonDetailsPEOAttribute45 | — |
| ATTRIBUTE46 | PersonDetailsPEOAttribute46 | — |
| ATTRIBUTE47 | PersonDetailsPEOAttribute47 | — |
| ATTRIBUTE48 | PersonDetailsPEOAttribute48 | — |
| ATTRIBUTE49 | PersonDetailsPEOAttribute49 | — |
| ATTRIBUTE5 | PersonDetailsPEOAttribute5 | — |
| ATTRIBUTE50 | PersonDetailsPEOAttribute50 | — |
| ATTRIBUTE6 | PersonDetailsPEOAttribute6 | — |
| ATTRIBUTE7 | PersonDetailsPEOAttribute7 | — |
| ATTRIBUTE8 | PersonDetailsPEOAttribute8 | — |
| ATTRIBUTE9 | PersonDetailsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PersonDetailsPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PersonDetailsPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PersonDetailsPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PersonDetailsPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PersonDetailsPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PersonDetailsPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PersonDetailsPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PersonDetailsPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PersonDetailsPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PersonDetailsPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PersonDetailsPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PersonDetailsPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PersonDetailsPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PersonDetailsPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PersonDetailsPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PersonDetailsPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PersonDetailsPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PersonDetailsPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PersonDetailsPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PersonDetailsPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PersonDetailsPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PersonDetailsPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PersonDetailsPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PersonDetailsPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PersonDetailsPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PersonDetailsPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PersonDetailsPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PersonDetailsPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PersonDetailsPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PersonDetailsPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PersonDetailsPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PersonDetailsPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PersonDetailsPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PersonDetailsPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PersonDetailsPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PersonDetailsPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | ✅ |
| CREATED_BY | PersonDetailsPEOCreatedBy | — |
| CREATION_DATE | PersonDetailsPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate1 | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | ✅ |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonDetailsPEOPersonId | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | ✅ |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | ✅ |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | ✅ |
| START_DATE | PersonDetailsPEOStartDate | ✅ |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | ✅ |

### [[contactvisapermitpvo|ContactVisaPermitPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | ContactPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | ContactPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | ContactPersonDetailsPEOPersonId | — |

### [[courtorderpvo|CourtOrderPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | — |
| PERSON_ID | PersonId1 | — |

### [[deviceactivityinpvo|DeviceActivityInPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[deviceactivityoutpvo|DeviceActivityOutPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[deviceactivitypvo|DeviceActivityPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[deviceeventpvo|DeviceEventPVO]] (GL · BICC: 4/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | CorrPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | EventPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | CorrPersonDetailsPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EventPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | CorrPersonDetailsPEOPersonId | — |
| PERSON_ID | EventPersonDetailsPEOPersonId | — |
| PERSON_NUMBER | CorrPersonDetailsPEOPersonNumber | ✅ |
| PERSON_NUMBER | EventPersonDetailsPEOPersonNumber | ✅ |

### [[eligibilityresultpvo|EligibilityResultPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId | — |
| PERSON_NUMBER | PersonNumber | — |

### [[eligiblepersondetailpvo|EligiblePersonDetailPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId1 | — |

### [[emailaddressespvo|EmailAddressesPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |

### [[emailaddressespvoviewall|EmailAddressesPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |

### [[endorsementspvo|EndorsementsPVO]] (PO · BICC: 5/210)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| APPLICANT_NUMBER | ApplicantNumber1 | — |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE1 | Attribute118 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE10 | Attribute105 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE11 | Attribute119 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE12 | Attribute125 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE13 | Attribute135 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE14 | Attribute145 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE15 | Attribute155 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE16 | Attribute165 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE17 | Attribute175 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE18 | Attribute185 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE19 | Attribute195 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE2 | Attribute218 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE20 | Attribute205 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE21 | Attribute219 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE22 | Attribute225 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE23 | Attribute235 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE24 | Attribute245 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE25 | Attribute255 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE26 | Attribute265 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE27 | Attribute275 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE28 | Attribute285 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE29 | Attribute295 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE3 | Attribute314 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE30 | Attribute305 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE31 | Attribute315 | — |
| ATTRIBUTE32 | Attribute32 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE33 | Attribute331 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE34 | Attribute341 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE35 | Attribute351 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE36 | Attribute361 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE37 | Attribute371 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE38 | Attribute381 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE39 | Attribute391 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE4 | Attribute414 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE40 | Attribute401 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE41 | Attribute415 | — |
| ATTRIBUTE42 | Attribute42 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE43 | Attribute431 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE44 | Attribute441 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE45 | Attribute451 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE46 | Attribute461 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE47 | Attribute471 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE48 | Attribute481 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE49 | Attribute491 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE5 | Attribute55 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE50 | Attribute501 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE6 | Attribute65 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE7 | Attribute75 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE8 | Attribute85 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE9 | Attribute95 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory5 | — |
| ATTRIBUTE_DATE1 | AttributeDate110 | — |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE10 | AttributeDate105 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE11 | AttributeDate115 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE12 | AttributeDate125 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE13 | AttributeDate135 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE14 | AttributeDate145 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE15 | AttributeDate155 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE2 | AttributeDate25 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE3 | AttributeDate35 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE4 | AttributeDate45 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE5 | AttributeDate55 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE6 | AttributeDate65 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE7 | AttributeDate75 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE8 | AttributeDate85 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_DATE9 | AttributeDate95 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber118 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber105 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber119 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber125 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber135 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber145 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber155 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber165 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber175 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber185 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber195 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber25 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber205 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber35 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber45 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber55 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber65 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber75 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber85 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber95 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | BusinessGroupId5 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATED_BY | CreatedBy6 | — |
| CREATION_DATE | CreationDate2 | — |
| CREATION_DATE | CreationDate6 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate6 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin6 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| LAST_UPDATED_BY | LastUpdatedBy6 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| MAILING_ADDRESS_ID | MailingAddressId1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber6 | — |
| PERSON_ID | PersonId1 | — |
| PERSON_ID | PersonId5 | — |
| PERSON_NUMBER | PersonNumber | — |
| PERSON_NUMBER | PersonNumber1 | ✅ |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId1 | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_ID | PrimaryNidId1 | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber1 | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId1 | — |
| START_DATE | StartDate1 | — |
| START_DATE | StartDate3 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect1 | — |

### [[expensereporthistorypvo|ExpenseReportHistoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PerformerPersonDetailsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PerformerPersonDetailsEffectiveStartDate | — |
| PERSON_ID | PerformerPersonDetailsPersonId | — |
| PERSON_NUMBER | PerformerPersonDetailsPersonNumber | — |
| PRIMARY_EMAIL_ID | PerformerPersonDetailsPrimaryEmailId | — |

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 7/210)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | ✅ |
| APPLICANT_NUMBER | ApplicantNumber1 | — |
| ATTRIBUTE1 | Attribute116 | — |
| ATTRIBUTE1 | Attribute120 | — |
| ATTRIBUTE10 | Attribute104 | — |
| ATTRIBUTE10 | Attribute106 | — |
| ATTRIBUTE11 | Attribute1110 | — |
| ATTRIBUTE11 | Attribute117 | — |
| ATTRIBUTE12 | Attribute124 | — |
| ATTRIBUTE12 | Attribute126 | — |
| ATTRIBUTE13 | Attribute134 | — |
| ATTRIBUTE13 | Attribute136 | — |
| ATTRIBUTE14 | Attribute144 | — |
| ATTRIBUTE14 | Attribute146 | — |
| ATTRIBUTE15 | Attribute154 | — |
| ATTRIBUTE15 | Attribute156 | — |
| ATTRIBUTE16 | Attribute164 | — |
| ATTRIBUTE16 | Attribute166 | — |
| ATTRIBUTE17 | Attribute174 | — |
| ATTRIBUTE17 | Attribute176 | — |
| ATTRIBUTE18 | Attribute184 | — |
| ATTRIBUTE18 | Attribute186 | — |
| ATTRIBUTE19 | Attribute194 | — |
| ATTRIBUTE19 | Attribute196 | — |
| ATTRIBUTE2 | Attribute216 | — |
| ATTRIBUTE2 | Attribute220 | — |
| ATTRIBUTE20 | Attribute204 | — |
| ATTRIBUTE20 | Attribute206 | — |
| ATTRIBUTE21 | Attribute2110 | — |
| ATTRIBUTE21 | Attribute217 | — |
| ATTRIBUTE22 | Attribute224 | — |
| ATTRIBUTE22 | Attribute226 | — |
| ATTRIBUTE23 | Attribute234 | — |
| ATTRIBUTE23 | Attribute236 | — |
| ATTRIBUTE24 | Attribute244 | — |
| ATTRIBUTE24 | Attribute246 | — |
| ATTRIBUTE25 | Attribute254 | — |
| ATTRIBUTE25 | Attribute256 | — |
| ATTRIBUTE26 | Attribute264 | — |
| ATTRIBUTE26 | Attribute266 | — |
| ATTRIBUTE27 | Attribute274 | — |
| ATTRIBUTE27 | Attribute276 | — |
| ATTRIBUTE28 | Attribute284 | — |
| ATTRIBUTE28 | Attribute286 | — |
| ATTRIBUTE29 | Attribute294 | — |
| ATTRIBUTE29 | Attribute296 | — |
| ATTRIBUTE3 | Attribute312 | — |
| ATTRIBUTE3 | Attribute34 | — |
| ATTRIBUTE30 | Attribute304 | — |
| ATTRIBUTE30 | Attribute306 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE31 | Attribute313 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE32 | Attribute322 | — |
| ATTRIBUTE33 | Attribute331 | — |
| ATTRIBUTE33 | Attribute332 | — |
| ATTRIBUTE34 | Attribute341 | — |
| ATTRIBUTE34 | Attribute342 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE35 | Attribute351 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE36 | Attribute361 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE37 | Attribute371 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE38 | Attribute381 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE39 | Attribute391 | — |
| ATTRIBUTE4 | Attribute412 | — |
| ATTRIBUTE4 | Attribute44 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE40 | Attribute401 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE41 | Attribute413 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE42 | Attribute422 | — |
| ATTRIBUTE43 | Attribute431 | — |
| ATTRIBUTE43 | Attribute432 | — |
| ATTRIBUTE44 | Attribute441 | — |
| ATTRIBUTE44 | Attribute442 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE45 | Attribute451 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE46 | Attribute461 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE47 | Attribute471 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE48 | Attribute481 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE49 | Attribute491 | — |
| ATTRIBUTE5 | Attribute54 | — |
| ATTRIBUTE5 | Attribute56 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE50 | Attribute501 | — |
| ATTRIBUTE6 | Attribute64 | — |
| ATTRIBUTE6 | Attribute66 | — |
| ATTRIBUTE7 | Attribute74 | — |
| ATTRIBUTE7 | Attribute76 | — |
| ATTRIBUTE8 | Attribute84 | — |
| ATTRIBUTE8 | Attribute86 | — |
| ATTRIBUTE9 | Attribute94 | — |
| ATTRIBUTE9 | Attribute96 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory4 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory6 | — |
| ATTRIBUTE_DATE1 | AttributeDate116 | — |
| ATTRIBUTE_DATE1 | AttributeDate19 | — |
| ATTRIBUTE_DATE10 | AttributeDate104 | — |
| ATTRIBUTE_DATE10 | AttributeDate106 | — |
| ATTRIBUTE_DATE11 | AttributeDate114 | — |
| ATTRIBUTE_DATE11 | AttributeDate117 | — |
| ATTRIBUTE_DATE12 | AttributeDate124 | — |
| ATTRIBUTE_DATE12 | AttributeDate126 | — |
| ATTRIBUTE_DATE13 | AttributeDate134 | — |
| ATTRIBUTE_DATE13 | AttributeDate136 | — |
| ATTRIBUTE_DATE14 | AttributeDate144 | — |
| ATTRIBUTE_DATE14 | AttributeDate146 | — |
| ATTRIBUTE_DATE15 | AttributeDate154 | — |
| ATTRIBUTE_DATE15 | AttributeDate156 | — |
| ATTRIBUTE_DATE2 | AttributeDate24 | — |
| ATTRIBUTE_DATE2 | AttributeDate26 | — |
| ATTRIBUTE_DATE3 | AttributeDate34 | — |
| ATTRIBUTE_DATE3 | AttributeDate36 | — |
| ATTRIBUTE_DATE4 | AttributeDate44 | — |
| ATTRIBUTE_DATE4 | AttributeDate46 | — |
| ATTRIBUTE_DATE5 | AttributeDate54 | — |
| ATTRIBUTE_DATE5 | AttributeDate56 | — |
| ATTRIBUTE_DATE6 | AttributeDate64 | — |
| ATTRIBUTE_DATE6 | AttributeDate66 | — |
| ATTRIBUTE_DATE7 | AttributeDate74 | — |
| ATTRIBUTE_DATE7 | AttributeDate76 | — |
| ATTRIBUTE_DATE8 | AttributeDate84 | — |
| ATTRIBUTE_DATE8 | AttributeDate86 | — |
| ATTRIBUTE_DATE9 | AttributeDate94 | — |
| ATTRIBUTE_DATE9 | AttributeDate96 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber116 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber120 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber104 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber106 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber1110 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber117 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber124 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber126 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber134 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber136 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber144 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber146 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber154 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber156 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber164 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber166 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber174 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber176 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber184 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber186 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber194 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber196 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber24 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber26 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber204 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber206 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber34 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber36 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber44 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber46 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber54 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber56 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber64 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber66 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber74 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber76 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber84 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber86 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber94 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber96 | — |
| BUSINESS_GROUP_ID | BusinessGroupId6 | — |
| BUSINESS_GROUP_ID | BusinessGroupId8 | — |
| CREATED_BY | CreatedBy10 | — |
| CREATED_BY | CreatedBy12 | — |
| CREATION_DATE | CreationDate10 | — |
| CREATION_DATE | CreationDate12 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate3 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate3 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate10 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate12 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin10 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin12 | — |
| LAST_UPDATED_BY | LastUpdatedBy10 | — |
| LAST_UPDATED_BY | LastUpdatedBy12 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| MAILING_ADDRESS_ID | MailingAddressId1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber11 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber9 | — |
| PERSON_ID | PersonId5 | — |
| PERSON_ID | PersonId7 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PERSON_NUMBER | PersonNumber1 | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId1 | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_ID | PrimaryNidId1 | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber1 | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId1 | — |
| START_DATE | StartDate2 | — |
| START_DATE | StartDate3 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | ✅ |
| WAIVE_DATA_PROTECT | WaiveDataProtect1 | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 24/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | ✅ |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | ✅ |
| CREATED_BY | PersonDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | PersonDetailsPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | PersonDetailsPEO1EffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEO1EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEO1LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | ✅ |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | ✅ |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | ✅ |
| PERSON_ID | PersonDetailsPEO1PersonId1 | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | ✅ |
| PERSON_NUMBER | PersonDetailsPEO1PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEO1PrimaryEmailId | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | ✅ |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | ✅ |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | ✅ |
| START_DATE | PersonDetailsPEOStartDate | ✅ |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 9/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | ✅ |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | — |
| CREATED_BY | PersonDetailsPEOCreatedBy | — |
| CREATION_DATE | PersonDetailsPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEO1EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEO1EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEO1LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonDetailsPEO1PersonId1 | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEO1PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEO1PrimaryEmailId | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |
| START_DATE | PersonDetailsPEOStartDate | — |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | ✅ |

### [[groupinclmemberspvo|GroupInclMembersPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| PERSON_ID | PersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[groupmemberspvo|GroupMembersPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[historicabsencetimeentrypvo|HistoricAbsenceTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[hitspvo|HitsPVO]] (PO · BICC: 3/210)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| APPLICANT_NUMBER | ApplicantNumber1 | — |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE1 | Attribute118 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE10 | Attribute105 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE11 | Attribute119 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE12 | Attribute125 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE13 | Attribute135 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE14 | Attribute145 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE15 | Attribute155 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE16 | Attribute165 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE17 | Attribute175 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE18 | Attribute185 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE19 | Attribute195 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE2 | Attribute218 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE20 | Attribute205 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE21 | Attribute219 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE22 | Attribute225 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE23 | Attribute235 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE24 | Attribute245 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE25 | Attribute255 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE26 | Attribute265 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE27 | Attribute275 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE28 | Attribute285 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE29 | Attribute295 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE3 | Attribute314 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE30 | Attribute305 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE31 | Attribute315 | — |
| ATTRIBUTE32 | Attribute32 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE33 | Attribute331 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE34 | Attribute341 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE35 | Attribute351 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE36 | Attribute361 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE37 | Attribute371 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE38 | Attribute381 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE39 | Attribute391 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE4 | Attribute414 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE40 | Attribute401 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE41 | Attribute415 | — |
| ATTRIBUTE42 | Attribute42 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE43 | Attribute431 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE44 | Attribute441 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE45 | Attribute451 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE46 | Attribute461 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE47 | Attribute471 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE48 | Attribute481 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE49 | Attribute491 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE5 | Attribute55 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE50 | Attribute501 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE6 | Attribute65 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE7 | Attribute75 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE8 | Attribute85 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE9 | Attribute95 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory5 | — |
| ATTRIBUTE_DATE1 | AttributeDate110 | — |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE10 | AttributeDate105 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE11 | AttributeDate115 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE12 | AttributeDate125 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE13 | AttributeDate135 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE14 | AttributeDate145 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE15 | AttributeDate155 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE2 | AttributeDate25 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE3 | AttributeDate35 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE4 | AttributeDate45 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE5 | AttributeDate55 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE6 | AttributeDate65 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE7 | AttributeDate75 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE8 | AttributeDate85 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_DATE9 | AttributeDate95 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber118 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber105 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber119 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber125 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber135 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber145 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber155 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber165 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber175 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber185 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber195 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber25 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber205 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber35 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber45 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber55 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber65 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber75 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber85 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber95 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| BUSINESS_GROUP_ID | BusinessGroupId5 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATED_BY | CreatedBy6 | — |
| CREATION_DATE | CreationDate2 | — |
| CREATION_DATE | CreationDate6 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | — |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate6 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin6 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| LAST_UPDATED_BY | LastUpdatedBy6 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| MAILING_ADDRESS_ID | MailingAddressId1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber6 | — |
| PERSON_ID | PersonId1 | — |
| PERSON_ID | PersonId5 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PERSON_NUMBER | PersonNumber1 | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId1 | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_ID | PrimaryNidId1 | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber1 | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId1 | — |
| START_DATE | StartDate1 | — |
| START_DATE | StartDate3 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect1 | — |

### [[institutionauditalertspvo|InstitutionAuditAlertsPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDPEOPersonId | — |

### [[institutioncontactspvo|InstitutionContactsPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDPEOPersonId | — |

### [[jobapplicationinteractionpvo|JobApplicationInteractionPVO]] (HCM · BICC: 4/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | ✅ |
| ATTRIBUTE1 | Attribute112 | — |
| ATTRIBUTE10 | Attribute102 | — |
| ATTRIBUTE11 | Attribute113 | — |
| ATTRIBUTE12 | Attribute122 | — |
| ATTRIBUTE13 | Attribute132 | — |
| ATTRIBUTE14 | Attribute142 | — |
| ATTRIBUTE15 | Attribute152 | — |
| ATTRIBUTE16 | Attribute162 | — |
| ATTRIBUTE17 | Attribute172 | — |
| ATTRIBUTE18 | Attribute182 | — |
| ATTRIBUTE19 | Attribute192 | — |
| ATTRIBUTE2 | Attribute212 | — |
| ATTRIBUTE20 | Attribute202 | — |
| ATTRIBUTE21 | Attribute213 | — |
| ATTRIBUTE22 | Attribute222 | — |
| ATTRIBUTE23 | Attribute232 | — |
| ATTRIBUTE24 | Attribute242 | — |
| ATTRIBUTE25 | Attribute252 | — |
| ATTRIBUTE26 | Attribute262 | — |
| ATTRIBUTE27 | Attribute272 | — |
| ATTRIBUTE28 | Attribute282 | — |
| ATTRIBUTE29 | Attribute292 | — |
| ATTRIBUTE3 | Attribute32 | — |
| ATTRIBUTE30 | Attribute302 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute42 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute52 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute62 | — |
| ATTRIBUTE7 | Attribute72 | — |
| ATTRIBUTE8 | Attribute82 | — |
| ATTRIBUTE9 | Attribute92 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory2 | — |
| ATTRIBUTE_DATE1 | AttributeDate17 | — |
| ATTRIBUTE_DATE10 | AttributeDate102 | — |
| ATTRIBUTE_DATE11 | AttributeDate112 | — |
| ATTRIBUTE_DATE12 | AttributeDate122 | — |
| ATTRIBUTE_DATE13 | AttributeDate132 | — |
| ATTRIBUTE_DATE14 | AttributeDate142 | — |
| ATTRIBUTE_DATE15 | AttributeDate152 | — |
| ATTRIBUTE_DATE2 | AttributeDate22 | — |
| ATTRIBUTE_DATE3 | AttributeDate32 | — |
| ATTRIBUTE_DATE4 | AttributeDate42 | — |
| ATTRIBUTE_DATE5 | AttributeDate52 | — |
| ATTRIBUTE_DATE6 | AttributeDate62 | — |
| ATTRIBUTE_DATE7 | AttributeDate72 | — |
| ATTRIBUTE_DATE8 | AttributeDate82 | — |
| ATTRIBUTE_DATE9 | AttributeDate92 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber102 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber22 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber202 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber32 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber42 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber52 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber62 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber72 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber82 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber92 | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PERSON_ID | PersonId3 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[managerhrchybottomuppvolinemanager|ManagerHrchyBottomUpPVOLineManager]] (HCM · BICC: 35/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOL10EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL11EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL12EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL13EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL14EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL15EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL16EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL17EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL18EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL19EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL1EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL20EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL2EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL3EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL4EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL5EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL6EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL7EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL8EffectiveEndDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOL9EffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOL10EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL11EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL12EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL13EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL14EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL15EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL16EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL17EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL18EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL19EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL1EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL20EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL2EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL3EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL4EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL5EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL6EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL7EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL8EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOL9EffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOL10PersonId | — |
| PERSON_ID | PersonDetailsPEOL11PersonId | — |
| PERSON_ID | PersonDetailsPEOL12PersonId | — |
| PERSON_ID | PersonDetailsPEOL13PersonId | — |
| PERSON_ID | PersonDetailsPEOL14PersonId | — |
| PERSON_ID | PersonDetailsPEOL15PersonId | — |
| PERSON_ID | PersonDetailsPEOL16PersonId | — |
| PERSON_ID | PersonDetailsPEOL17PersonId | — |
| PERSON_ID | PersonDetailsPEOL18PersonId | — |
| PERSON_ID | PersonDetailsPEOL19PersonId | — |
| PERSON_ID | PersonDetailsPEOL1PersonId | — |
| PERSON_ID | PersonDetailsPEOL20PersonId | — |
| PERSON_ID | PersonDetailsPEOL2PersonId | — |
| PERSON_ID | PersonDetailsPEOL3PersonId | — |
| PERSON_ID | PersonDetailsPEOL4PersonId | — |
| PERSON_ID | PersonDetailsPEOL5PersonId | — |
| PERSON_ID | PersonDetailsPEOL6PersonId | — |
| PERSON_ID | PersonDetailsPEOL7PersonId | — |
| PERSON_ID | PersonDetailsPEOL8PersonId | — |
| PERSON_ID | PersonDetailsPEOL9PersonId | — |
| PERSON_NUMBER | PersonDetailsPEOL10PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL11PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL12PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL13PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL14PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL15PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL16PersonNumber | — |
| PERSON_NUMBER | PersonDetailsPEOL17PersonNumber | — |
| PERSON_NUMBER | PersonDetailsPEOL18PersonNumber | — |
| PERSON_NUMBER | PersonDetailsPEOL19PersonNumber | — |
| PERSON_NUMBER | PersonDetailsPEOL1PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL20PersonNumber | — |
| PERSON_NUMBER | PersonDetailsPEOL2PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL3PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL4PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL5PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL6PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL7PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL8PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOL9PersonNumber | ✅ |

### [[offerpvo|OfferPVO]] (HCM · BICC: 2/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute32 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute42 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PERSON_ID | PersonId2 | — |
| PERSON_NUMBER | PersonNumber | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[participantenrollmentpvo|ParticipantEnrollmentPVO]] (HCM · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate4 | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate3 | ✅ |
| PERSON_ID | PersonId1 | ✅ |

### [[personabsdailydetailpvo|PersonAbsDailyDetailPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId1 | — |

### [[personabsentrypvo|PersonAbsEntryPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId1 | — |

### [[personabsplanentrypvo|PersonAbsPlanEntryPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| PERSON_ID | PersonId1 | — |

### [[personabsplnsummaryentpvo|PersonAbsPlnSummaryEntPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| PERSON_ID | PersonId1 | — |

### [[personabstypeentrypvo|PersonAbsTypeEntryPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId1 | — |

### [[personaccrualentrydtlpvo|PersonAccrualEntryDtlPVO]] (GL · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| PERSON_ID | PersonId1 | — |

### [[personaccrualentrypvo|PersonAccrualEntryPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PERSON_ID | PersonId1 | — |

### [[personaddresspvo|PersonAddressPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |

### [[personaddresspvoviewall|PersonAddressPVOViewAll]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |

### [[persondetailspvo|PersonDetailsPVO]] (HCM · BICC: 15/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | ✅ |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | ✅ |
| CREATED_BY | PersonDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | PersonDetailsPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | ✅ |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonId | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | ✅ |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | ✅ |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | ✅ |
| START_DATE | PersonDetailsPEOStartDate | ✅ |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | ✅ |

### [[persondetailspvoviewall|PersonDetailsPVOViewAll]] (HCM · BICC: 14/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | ✅ |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | — |
| CREATED_BY | PersonDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | PersonDetailsPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | ✅ |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonId | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | ✅ |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | ✅ |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | ✅ |
| START_DATE | PersonDetailsPEOStartDate | ✅ |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | ✅ |

### [[persondonationentrydtlpvo|PersonDonationEntryDtlPVO]] (GL · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |

### [[personemailpvo|PersonEmailPVO]] (HCM · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | — |
| CREATED_BY | PersonDetailsPEOCreatedBy | — |
| CREATION_DATE | PersonDetailsPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |
| START_DATE | PersonDetailsPEOStartDate | — |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | — |

### [[personlifeeventpvo|PersonLifeEventPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate3 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | — |
| PERSON_ID | PersonId1 | — |

### [[personnamedpvo|PersonNameDPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDPEOPersonId | — |
| PERSON_NUMBER | PersonDPEOPersonNumber | ✅ |

### [[personnamepvo|PersonNamePVO]] (HCM · BICC: 3/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[personnamepvoviewall|PersonNamePVOViewAll]] (HCM · BICC: 4/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[personnationalidentifierpvo|PersonNationalIdentifierPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |

### [[personnationalidentifierpvoviewall|PersonNationalIdentifierPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |

### [[personphonepvo|PersonPhonePVO]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId | ✅ |
| CREATED_BY | PersonDetailsPEOCreatedBy | — |
| CREATION_DATE | PersonDetailsPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | ✅ |
| START_DATE | PersonDetailsPEOStartDate | — |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | — |

### [[personpotentiallifeeventpvo|PersonPotentialLifeEventPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate3 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | — |
| PERSON_ID | PersonId1 | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 4/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| EFFECTIVE_END_DATE | PersonDetailsPEO1EffectiveEndDate1 | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEO1EffectiveStartDate1 | ✅ |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEO1PersonId | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEO1PersonNumber | ✅ |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | — |

### [[phonespvo|PhonesPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |

### [[phonespvoviewall|PhonesPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[project|Project]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | — |
| PERSON_ID | PersonDPEOPersonId | — |
| PERSON_NUMBER | PersonDPEOPersonNumber | — |

### [[projectexec|ProjectExec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | — |
| PERSON_ID | PersonDPEOPersonId | — |
| PERSON_NUMBER | PersonDPEOPersonNumber | — |

### [[projectrefpvo|ProjectRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | — |
| PERSON_ID | PersonDPEOPersonId | — |
| PERSON_NUMBER | PersonDPEOPersonNumber | — |

### [[projectview|ProjectView]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDPEOEffectiveStartDate | — |
| PERSON_ID | PersonDPEOPersonId | — |
| PERSON_NUMBER | PersonDPEOPersonNumber | — |

### [[prospectinteractionpvo|ProspectInteractionPVO]] (HCM · BICC: 2/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| ATTRIBUTE1 | Attribute112 | — |
| ATTRIBUTE10 | Attribute102 | — |
| ATTRIBUTE11 | Attribute113 | — |
| ATTRIBUTE12 | Attribute122 | — |
| ATTRIBUTE13 | Attribute132 | — |
| ATTRIBUTE14 | Attribute142 | — |
| ATTRIBUTE15 | Attribute152 | — |
| ATTRIBUTE16 | Attribute162 | — |
| ATTRIBUTE17 | Attribute172 | — |
| ATTRIBUTE18 | Attribute182 | — |
| ATTRIBUTE19 | Attribute192 | — |
| ATTRIBUTE2 | Attribute212 | — |
| ATTRIBUTE20 | Attribute202 | — |
| ATTRIBUTE21 | Attribute213 | — |
| ATTRIBUTE22 | Attribute222 | — |
| ATTRIBUTE23 | Attribute232 | — |
| ATTRIBUTE24 | Attribute242 | — |
| ATTRIBUTE25 | Attribute252 | — |
| ATTRIBUTE26 | Attribute262 | — |
| ATTRIBUTE27 | Attribute272 | — |
| ATTRIBUTE28 | Attribute282 | — |
| ATTRIBUTE29 | Attribute292 | — |
| ATTRIBUTE3 | Attribute32 | — |
| ATTRIBUTE30 | Attribute302 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute321 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute42 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute421 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute52 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute62 | — |
| ATTRIBUTE7 | Attribute72 | — |
| ATTRIBUTE8 | Attribute82 | — |
| ATTRIBUTE9 | Attribute92 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory2 | — |
| ATTRIBUTE_DATE1 | AttributeDate17 | — |
| ATTRIBUTE_DATE10 | AttributeDate102 | — |
| ATTRIBUTE_DATE11 | AttributeDate112 | — |
| ATTRIBUTE_DATE12 | AttributeDate122 | — |
| ATTRIBUTE_DATE13 | AttributeDate132 | — |
| ATTRIBUTE_DATE14 | AttributeDate142 | — |
| ATTRIBUTE_DATE15 | AttributeDate152 | — |
| ATTRIBUTE_DATE2 | AttributeDate22 | — |
| ATTRIBUTE_DATE3 | AttributeDate32 | — |
| ATTRIBUTE_DATE4 | AttributeDate42 | — |
| ATTRIBUTE_DATE5 | AttributeDate52 | — |
| ATTRIBUTE_DATE6 | AttributeDate62 | — |
| ATTRIBUTE_DATE7 | AttributeDate72 | — |
| ATTRIBUTE_DATE8 | AttributeDate82 | — |
| ATTRIBUTE_DATE9 | AttributeDate92 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber102 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber22 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber202 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber32 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber42 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber52 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber62 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber72 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber82 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber92 | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| CREATED_BY | CreatedBy3 | — |
| CREATION_DATE | CreationDate3 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate3 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin3 | — |
| LAST_UPDATED_BY | LastUpdatedBy3 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| PERSON_ID | PersonId3 | — |
| PERSON_NUMBER | PersonNumber | — |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[prospectspvo|ProspectsPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PerDetailsPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PerDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PerDetailsPEOPersonId | ✅ |
| PERSON_NUMBER | PerDetailsPEOAddedByPersonNumber | ✅ |

### [[prospectsviewallpvo|ProspectsViewAllPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PerDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PerDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PerDetailsPEOPersonId | — |
| PERSON_NUMBER | PerDetailsPEOAddedByPersonNumber | ✅ |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| ATTRIBUTE1 | PersonDetailsPEOAttribute150 | — |
| ATTRIBUTE10 | PersonDetailsPEOAttribute1011 | — |
| ATTRIBUTE11 | PersonDetailsPEOAttribute1115 | — |
| ATTRIBUTE12 | PersonDetailsPEOAttribute1213 | — |
| ATTRIBUTE13 | PersonDetailsPEOAttribute1311 | — |
| ATTRIBUTE14 | PersonDetailsPEOAttribute1411 | — |
| ATTRIBUTE15 | PersonDetailsPEOAttribute1511 | — |
| ATTRIBUTE16 | PersonDetailsPEOAttribute168 | — |
| ATTRIBUTE17 | PersonDetailsPEOAttribute178 | — |
| ATTRIBUTE18 | PersonDetailsPEOAttribute188 | — |
| ATTRIBUTE19 | PersonDetailsPEOAttribute198 | — |
| ATTRIBUTE2 | PersonDetailsPEOAttribute212 | — |
| ATTRIBUTE20 | PersonDetailsPEOAttribute208 | — |
| ATTRIBUTE21 | PersonDetailsPEOAttribute213 | — |
| ATTRIBUTE22 | PersonDetailsPEOAttribute222 | — |
| ATTRIBUTE23 | PersonDetailsPEOAttribute232 | — |
| ATTRIBUTE24 | PersonDetailsPEOAttribute242 | — |
| ATTRIBUTE25 | PersonDetailsPEOAttribute252 | — |
| ATTRIBUTE26 | PersonDetailsPEOAttribute262 | — |
| ATTRIBUTE27 | PersonDetailsPEOAttribute272 | — |
| ATTRIBUTE28 | PersonDetailsPEOAttribute282 | — |
| ATTRIBUTE29 | PersonDetailsPEOAttribute292 | — |
| ATTRIBUTE3 | PersonDetailsPEOAttribute311 | — |
| ATTRIBUTE30 | PersonDetailsPEOAttribute301 | — |
| ATTRIBUTE31 | PersonDetailsPEOAttribute312 | — |
| ATTRIBUTE32 | PersonDetailsPEOAttribute321 | — |
| ATTRIBUTE33 | PersonDetailsPEOAttribute331 | — |
| ATTRIBUTE34 | PersonDetailsPEOAttribute341 | — |
| ATTRIBUTE35 | PersonDetailsPEOAttribute351 | — |
| ATTRIBUTE36 | PersonDetailsPEOAttribute361 | — |
| ATTRIBUTE37 | PersonDetailsPEOAttribute371 | — |
| ATTRIBUTE38 | PersonDetailsPEOAttribute381 | — |
| ATTRIBUTE39 | PersonDetailsPEOAttribute391 | — |
| ATTRIBUTE4 | PersonDetailsPEOAttribute411 | — |
| ATTRIBUTE40 | PersonDetailsPEOAttribute40 | — |
| ATTRIBUTE41 | PersonDetailsPEOAttribute412 | — |
| ATTRIBUTE42 | PersonDetailsPEOAttribute421 | — |
| ATTRIBUTE43 | PersonDetailsPEOAttribute431 | — |
| ATTRIBUTE44 | PersonDetailsPEOAttribute441 | — |
| ATTRIBUTE45 | PersonDetailsPEOAttribute451 | — |
| ATTRIBUTE46 | PersonDetailsPEOAttribute461 | — |
| ATTRIBUTE47 | PersonDetailsPEOAttribute471 | — |
| ATTRIBUTE48 | PersonDetailsPEOAttribute481 | — |
| ATTRIBUTE49 | PersonDetailsPEOAttribute491 | — |
| ATTRIBUTE5 | PersonDetailsPEOAttribute511 | — |
| ATTRIBUTE50 | PersonDetailsPEOAttribute50 | — |
| ATTRIBUTE6 | PersonDetailsPEOAttribute611 | — |
| ATTRIBUTE7 | PersonDetailsPEOAttribute711 | — |
| ATTRIBUTE8 | PersonDetailsPEOAttribute811 | — |
| ATTRIBUTE9 | PersonDetailsPEOAttribute911 | — |
| ATTRIBUTE_CATEGORY | PersonDetailsPEOAttributeCategory11 | — |
| ATTRIBUTE_DATE1 | PersonDetailsPEOAttributeDate112 | — |
| ATTRIBUTE_DATE10 | PersonDetailsPEOAttributeDate105 | — |
| ATTRIBUTE_DATE11 | PersonDetailsPEOAttributeDate113 | — |
| ATTRIBUTE_DATE12 | PersonDetailsPEOAttributeDate122 | — |
| ATTRIBUTE_DATE13 | PersonDetailsPEOAttributeDate132 | — |
| ATTRIBUTE_DATE14 | PersonDetailsPEOAttributeDate142 | — |
| ATTRIBUTE_DATE15 | PersonDetailsPEOAttributeDate152 | — |
| ATTRIBUTE_DATE2 | PersonDetailsPEOAttributeDate211 | — |
| ATTRIBUTE_DATE3 | PersonDetailsPEOAttributeDate311 | — |
| ATTRIBUTE_DATE4 | PersonDetailsPEOAttributeDate411 | — |
| ATTRIBUTE_DATE5 | PersonDetailsPEOAttributeDate511 | — |
| ATTRIBUTE_DATE6 | PersonDetailsPEOAttributeDate65 | — |
| ATTRIBUTE_DATE7 | PersonDetailsPEOAttributeDate75 | — |
| ATTRIBUTE_DATE8 | PersonDetailsPEOAttributeDate85 | — |
| ATTRIBUTE_DATE9 | PersonDetailsPEOAttributeDate95 | — |
| ATTRIBUTE_NUMBER1 | PersonDetailsPEOAttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | PersonDetailsPEOAttributeNumber108 | — |
| ATTRIBUTE_NUMBER11 | PersonDetailsPEOAttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | PersonDetailsPEOAttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | PersonDetailsPEOAttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | PersonDetailsPEOAttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | PersonDetailsPEOAttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | PersonDetailsPEOAttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | PersonDetailsPEOAttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | PersonDetailsPEOAttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | PersonDetailsPEOAttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | PersonDetailsPEOAttributeNumber211 | — |
| ATTRIBUTE_NUMBER20 | PersonDetailsPEOAttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | PersonDetailsPEOAttributeNumber311 | — |
| ATTRIBUTE_NUMBER4 | PersonDetailsPEOAttributeNumber411 | — |
| ATTRIBUTE_NUMBER5 | PersonDetailsPEOAttributeNumber511 | — |
| ATTRIBUTE_NUMBER6 | PersonDetailsPEOAttributeNumber68 | — |
| ATTRIBUTE_NUMBER7 | PersonDetailsPEOAttributeNumber78 | — |
| ATTRIBUTE_NUMBER8 | PersonDetailsPEOAttributeNumber88 | — |
| ATTRIBUTE_NUMBER9 | PersonDetailsPEOAttributeNumber98 | — |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId1 | — |
| CREATED_BY | PersonDetailsPEOCreatedBy14 | — |
| CREATION_DATE | PersonDetailsPEOCreationDate14 | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate1 | — |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate14 | — |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin14 | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy14 | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber11 | — |
| PERSON_ID | PersonDetailsPEOPersonId1 | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |
| START_DATE | PersonDetailsPEOStartDate3 | — |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | PersonDetailsPEOApplicantNumber | — |
| ATTRIBUTE1 | PersonDetailsPEOAttribute150 | — |
| ATTRIBUTE10 | PersonDetailsPEOAttribute1011 | — |
| ATTRIBUTE11 | PersonDetailsPEOAttribute1115 | — |
| ATTRIBUTE12 | PersonDetailsPEOAttribute1213 | — |
| ATTRIBUTE13 | PersonDetailsPEOAttribute1311 | — |
| ATTRIBUTE14 | PersonDetailsPEOAttribute1411 | — |
| ATTRIBUTE15 | PersonDetailsPEOAttribute1511 | — |
| ATTRIBUTE16 | PersonDetailsPEOAttribute168 | — |
| ATTRIBUTE17 | PersonDetailsPEOAttribute178 | — |
| ATTRIBUTE18 | PersonDetailsPEOAttribute188 | — |
| ATTRIBUTE19 | PersonDetailsPEOAttribute198 | — |
| ATTRIBUTE2 | PersonDetailsPEOAttribute212 | — |
| ATTRIBUTE20 | PersonDetailsPEOAttribute208 | — |
| ATTRIBUTE21 | PersonDetailsPEOAttribute213 | — |
| ATTRIBUTE22 | PersonDetailsPEOAttribute222 | — |
| ATTRIBUTE23 | PersonDetailsPEOAttribute232 | — |
| ATTRIBUTE24 | PersonDetailsPEOAttribute242 | — |
| ATTRIBUTE25 | PersonDetailsPEOAttribute252 | — |
| ATTRIBUTE26 | PersonDetailsPEOAttribute262 | — |
| ATTRIBUTE27 | PersonDetailsPEOAttribute272 | — |
| ATTRIBUTE28 | PersonDetailsPEOAttribute282 | — |
| ATTRIBUTE29 | PersonDetailsPEOAttribute292 | — |
| ATTRIBUTE3 | PersonDetailsPEOAttribute311 | — |
| ATTRIBUTE30 | PersonDetailsPEOAttribute301 | — |
| ATTRIBUTE31 | PersonDetailsPEOAttribute312 | — |
| ATTRIBUTE32 | PersonDetailsPEOAttribute321 | — |
| ATTRIBUTE33 | PersonDetailsPEOAttribute331 | — |
| ATTRIBUTE34 | PersonDetailsPEOAttribute341 | — |
| ATTRIBUTE35 | PersonDetailsPEOAttribute351 | — |
| ATTRIBUTE36 | PersonDetailsPEOAttribute361 | — |
| ATTRIBUTE37 | PersonDetailsPEOAttribute371 | — |
| ATTRIBUTE38 | PersonDetailsPEOAttribute381 | — |
| ATTRIBUTE39 | PersonDetailsPEOAttribute391 | — |
| ATTRIBUTE4 | PersonDetailsPEOAttribute411 | — |
| ATTRIBUTE40 | PersonDetailsPEOAttribute40 | — |
| ATTRIBUTE41 | PersonDetailsPEOAttribute412 | — |
| ATTRIBUTE42 | PersonDetailsPEOAttribute421 | — |
| ATTRIBUTE43 | PersonDetailsPEOAttribute431 | — |
| ATTRIBUTE44 | PersonDetailsPEOAttribute441 | — |
| ATTRIBUTE45 | PersonDetailsPEOAttribute451 | — |
| ATTRIBUTE46 | PersonDetailsPEOAttribute461 | — |
| ATTRIBUTE47 | PersonDetailsPEOAttribute471 | — |
| ATTRIBUTE48 | PersonDetailsPEOAttribute481 | — |
| ATTRIBUTE49 | PersonDetailsPEOAttribute491 | — |
| ATTRIBUTE5 | PersonDetailsPEOAttribute511 | — |
| ATTRIBUTE50 | PersonDetailsPEOAttribute50 | — |
| ATTRIBUTE6 | PersonDetailsPEOAttribute611 | — |
| ATTRIBUTE7 | PersonDetailsPEOAttribute711 | — |
| ATTRIBUTE8 | PersonDetailsPEOAttribute811 | — |
| ATTRIBUTE9 | PersonDetailsPEOAttribute911 | — |
| ATTRIBUTE_CATEGORY | PersonDetailsPEOAttributeCategory11 | — |
| ATTRIBUTE_DATE1 | PersonDetailsPEOAttributeDate112 | — |
| ATTRIBUTE_DATE10 | PersonDetailsPEOAttributeDate105 | — |
| ATTRIBUTE_DATE11 | PersonDetailsPEOAttributeDate113 | — |
| ATTRIBUTE_DATE12 | PersonDetailsPEOAttributeDate122 | — |
| ATTRIBUTE_DATE13 | PersonDetailsPEOAttributeDate132 | — |
| ATTRIBUTE_DATE14 | PersonDetailsPEOAttributeDate142 | — |
| ATTRIBUTE_DATE15 | PersonDetailsPEOAttributeDate152 | — |
| ATTRIBUTE_DATE2 | PersonDetailsPEOAttributeDate211 | — |
| ATTRIBUTE_DATE3 | PersonDetailsPEOAttributeDate311 | — |
| ATTRIBUTE_DATE4 | PersonDetailsPEOAttributeDate411 | — |
| ATTRIBUTE_DATE5 | PersonDetailsPEOAttributeDate511 | — |
| ATTRIBUTE_DATE6 | PersonDetailsPEOAttributeDate65 | — |
| ATTRIBUTE_DATE7 | PersonDetailsPEOAttributeDate75 | — |
| ATTRIBUTE_DATE8 | PersonDetailsPEOAttributeDate85 | — |
| ATTRIBUTE_DATE9 | PersonDetailsPEOAttributeDate95 | — |
| ATTRIBUTE_NUMBER1 | PersonDetailsPEOAttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | PersonDetailsPEOAttributeNumber108 | — |
| ATTRIBUTE_NUMBER11 | PersonDetailsPEOAttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | PersonDetailsPEOAttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | PersonDetailsPEOAttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | PersonDetailsPEOAttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | PersonDetailsPEOAttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | PersonDetailsPEOAttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | PersonDetailsPEOAttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | PersonDetailsPEOAttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | PersonDetailsPEOAttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | PersonDetailsPEOAttributeNumber211 | — |
| ATTRIBUTE_NUMBER20 | PersonDetailsPEOAttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | PersonDetailsPEOAttributeNumber311 | — |
| ATTRIBUTE_NUMBER4 | PersonDetailsPEOAttributeNumber411 | — |
| ATTRIBUTE_NUMBER5 | PersonDetailsPEOAttributeNumber511 | — |
| ATTRIBUTE_NUMBER6 | PersonDetailsPEOAttributeNumber68 | — |
| ATTRIBUTE_NUMBER7 | PersonDetailsPEOAttributeNumber78 | — |
| ATTRIBUTE_NUMBER8 | PersonDetailsPEOAttributeNumber88 | — |
| ATTRIBUTE_NUMBER9 | PersonDetailsPEOAttributeNumber98 | — |
| BUSINESS_GROUP_ID | PersonDetailsPEOBusinessGroupId1 | — |
| CREATED_BY | PersonDetailsPEOCreatedBy14 | — |
| CREATION_DATE | PersonDetailsPEOCreationDate14 | — |
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate1 | — |
| LAST_UPDATE_DATE | PersonDetailsPEOLastUpdateDate14 | — |
| LAST_UPDATE_LOGIN | PersonDetailsPEOLastUpdateLogin14 | — |
| LAST_UPDATED_BY | PersonDetailsPEOLastUpdatedBy14 | — |
| MAILING_ADDRESS_ID | PersonDetailsPEOMailingAddressId | — |
| OBJECT_VERSION_NUMBER | PersonDetailsPEOObjectVersionNumber11 | — |
| PERSON_ID | PersonDetailsPEOPersonId1 | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | — |
| PRIMARY_EMAIL_ID | PersonDetailsPEOPrimaryEmailId | — |
| PRIMARY_NID_ID | PersonDetailsPEOPrimaryNidId | — |
| PRIMARY_NID_NUMBER | PersonDetailsPEOPrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PersonDetailsPEOPrimaryPhoneId | — |
| START_DATE | PersonDetailsPEOStartDate3 | — |
| WAIVE_DATA_PROTECT | PersonDetailsPEOWaiveDataProtect | — |

### [[referralspvo|ReferralsPVO]] (PO · BICC: 3/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute32 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute42 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PERSON_ID | PersonId1 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonNumber | ✅ |

### [[requisitionpvo|RequisitionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[schedulerprofileoptionpvo|SchedulerProfileOptionPVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| PERSON_ID | PersonId | — |
| PERSON_NUMBER | GroupManagerPersonNumber | ✅ |

### [[searchpvo|SearchPVO]] (PO · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[searchresultpvo|SearchResultPVO]] (PO · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | PersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonDetailsPEOEffectiveStartDate | — |
| PERSON_ID | PersonDetailsPEOPersonId | — |
| PERSON_NUMBER | PersonDetailsPEOPersonNumber | ✅ |

### [[setupprofileasgpvo|SetupProfileAsgPVO]] (GL · BICC: 4/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | AsgToDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | MgrDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AsgToDetailsPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | MgrDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | AsgToDetailsPEOPersonId | — |
| PERSON_ID | MgrDetailsPEOPersonId | — |
| PERSON_NUMBER | AsgToDetailsPEOPersonNumber | ✅ |
| PERSON_NUMBER | MgrDetailsPEOPersonNumber | ✅ |

### [[setupprofilepvo|SetupProfilePVO]] (GL · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | MgrDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | MgrDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | MgrDetailsPEOPersonId | — |
| PERSON_NUMBER | MgrDetailsPEOPersonNumber | ✅ |

### [[sharespvo|SharesPVO]] (PO · BICC: 3/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICANT_NUMBER | ApplicantNumber | — |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE31 | Attribute311 | — |
| ATTRIBUTE32 | Attribute32 | — |
| ATTRIBUTE33 | Attribute33 | — |
| ATTRIBUTE34 | Attribute34 | — |
| ATTRIBUTE35 | Attribute35 | — |
| ATTRIBUTE36 | Attribute36 | — |
| ATTRIBUTE37 | Attribute37 | — |
| ATTRIBUTE38 | Attribute38 | — |
| ATTRIBUTE39 | Attribute39 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE40 | Attribute40 | — |
| ATTRIBUTE41 | Attribute411 | — |
| ATTRIBUTE42 | Attribute42 | — |
| ATTRIBUTE43 | Attribute43 | — |
| ATTRIBUTE44 | Attribute44 | — |
| ATTRIBUTE45 | Attribute45 | — |
| ATTRIBUTE46 | Attribute46 | — |
| ATTRIBUTE47 | Attribute47 | — |
| ATTRIBUTE48 | Attribute48 | — |
| ATTRIBUTE49 | Attribute49 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE50 | Attribute50 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| MAILING_ADDRESS_ID | MailingAddressId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |
| PERSON_ID | PersonId1 | — |
| PERSON_NUMBER | PersonNumber | ✅ |
| PRIMARY_EMAIL_ID | PrimaryEmailId | — |
| PRIMARY_NID_ID | PrimaryNidId | — |
| PRIMARY_NID_NUMBER | PrimaryNidNumber | — |
| PRIMARY_PHONE_ID | PrimaryPhoneId | — |
| START_DATE | StartDate1 | — |
| WAIVE_DATA_PROTECT | WaiveDataProtect | — |

### [[submissionrestrictedpvo|SubmissionRestrictedPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | AddedByPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddedByPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | AddedByPersonDetailsPEOPersonId | — |
| PERSON_NUMBER | AddedByPersonDetailsPEOPersonNumber | ✅ |

### [[submissionviewallpvo|SubmissionViewAllPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | AddedByPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AddedByPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | AddedByPersonDetailsPEOPersonId | — |
| PERSON_NUMBER | AddedByPersonDetailsPEOPersonNumber | ✅ |

### [[wfmodelrequisitionpvo|WfModelRequisitionPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | HMPersonDetailsPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | HMPersonDetailsPEOEffectiveStartDate | ✅ |
| PERSON_ID | HMPersonDetailsPEOPersonId | — |
| PERSON_NUMBER | HMPersonDetailsPEOPersonNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ALL_PEOPLE_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallpeoplef.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
