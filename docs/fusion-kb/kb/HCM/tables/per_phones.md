---
id: DOC-HCM-696
doc_type: system-doc
title: "PER_PHONES — Telefones de Pessoas"
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
  - telefones
  - contato
  - comunicacao
  - phones
aliases:
  - PER_PHONES
  - per_phones
  - telefones-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PHONES

## Visão Geral

Armazena os **números de telefone** das pessoas no sistema. Suporta múltiplos tipos de telefone (celular, residencial, comercial, fax) e permite definir um número principal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro de contatos** — registrar telefones dos colaboradores
- **Comunicação de emergência** — contato rápido em situações urgentes
- **Notificações por SMS** — integração com sistemas de mensageria
- **Diretório corporativo** — listar ramais e telefones de contato
- **Compliance trabalhista** — dados de contato para eSocial

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PHONE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do telefone | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | PHONE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do telefone (MOBILE, HOME, WORK, FAX) | — | 🟢 90% |
| 4 | PHONE_NUMBER | VARCHAR2(60) | NOT NULL | Contato | Número do telefone | — | 🟢 95% |
| 5 | COUNTRY_CODE_NUMBER | VARCHAR2(10) | NULL | Contato | Código do país (+55, +1, etc.) | — | 🟡 80% |
| 6 | AREA_CODE | VARCHAR2(10) | NULL | Contato | Código de área (DDD) | — | 🟡 80% |
| 7 | EXTENSION | VARCHAR2(10) | NULL | Contato | Ramal | — | 🟡 75% |
| 8 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é o telefone principal (Y/N) | — | 🟡 80% |
| 9 | DATE_FROM | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 80% |
| 10 | DATE_TO | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 80% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa titular do telefone)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Telefone celular principal de um colaborador
```sql
SELECT ph.COUNTRY_CODE_NUMBER, ph.AREA_CODE, ph.PHONE_NUMBER
FROM   PER_PHONES ph
WHERE  ph.PERSON_ID = :p_person_id
  AND  ph.PHONE_TYPE = 'MOBILE'
  AND  ph.PRIMARY_FLAG = 'Y'
  AND  (ph.DATE_TO IS NULL OR ph.DATE_TO >= SYSDATE);
```

---

## Observações

- Uma pessoa pode ter múltiplos telefones de diferentes tipos.
- `PRIMARY_FLAG = 'Y'` indica o telefone principal.
- Contém dados PII — sujeita a LGPD/GDPR.
- Para o Brasil, `COUNTRY_CODE_NUMBER` = '+55' e `AREA_CODE` = DDD.

---

## Referências

- [Oracle Docs — PER_PHONES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perphones.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhoneAreaCode | — |
| BUSINESS_GROUP_ID | PhoneBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhoneCountryCodeNumber | — |
| CREATED_BY | PhoneCreatedBy | — |
| CREATION_DATE | PhoneCreationDate | — |
| DATE_FROM | PhoneDateFrom | — |
| DATE_TO | PhoneDateTo | — |
| EXTENSION | PhoneExtension | — |
| LAST_UPDATE_DATE | PhoneLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhoneLastUpdateLogin | — |
| LAST_UPDATED_BY | PhoneLastUpdatedBy | — |
| LEGISLATION_CODE | PhoneLegislationCode | — |
| OBJECT_VERSION_NUMBER | PhoneObjectVersionNumber | — |
| PERSON_ID | PhonePersonId | — |
| PHONE_ID | PhonePhoneId | — |
| PHONE_NUMBER | PhonePhoneNumber | ✅ |
| PHONE_TYPE | PhonePhoneType | — |
| SEARCH_PHONE_NUMBER | PhoneSearchPhoneNumber | — |
| SPEED_DIAL_NUMBER | PhoneSpeedDialNumber | — |
| VALIDITY | PhoneValidity | — |

### [[candidatephonespvo|CandidatePhonesPVO]] (HCM · BICC: 6/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| CREATED_BY | PhonesEOCreatedBy | — |
| CREATION_DATE | PhonesEOCreationDate | — |
| DATE_FROM | PhonesEODateFrom | — |
| DATE_TO | PhonesEODateTo | — |
| EXTENSION | PhonesEOExtension | — |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | — |
| LEGISLATION_CODE | PhonesEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | ✅ |
| PHONE_ID | PhoneId | — |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SEARCH_PHONE_NUMBER | PhonesEOSearchPhoneNumber | — |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | — |
| VALIDITY | Validity | — |

### [[contactphonespvo|ContactPhonesPVO]] (HCM · BICC: 16/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| CREATED_BY | PhonesEOCreatedBy | ✅ |
| CREATION_DATE | PhonesEOCreationDate | ✅ |
| DATE_FROM | PhonesEODateFrom | ✅ |
| DATE_TO | PhonesEODateTo | ✅ |
| EXTENSION | PhonesEOExtension | ✅ |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PhonesEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | ✅ |
| PHONE_ID | PhoneId | ✅ |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SEARCH_PHONE_NUMBER | PhonesEOSearchPhoneNumber | — |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | ✅ |
| VALIDITY | PhonesEOValidity | ✅ |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 19/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | ✅ |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| COUNTRY_CODE_NUMBER | WorkPhonePEOCountryCodeNumber | — |
| CREATED_BY | PhonesEOCreatedBy | ✅ |
| CREATION_DATE | PhonesEOCreationDate | ✅ |
| DATE_FROM | PhonesEODateFrom | ✅ |
| DATE_TO | PhonesEODateTo | ✅ |
| EXTENSION | PhonesEOExtension | ✅ |
| EXTENSION | WorkPhonePEOExtension | — |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PhonesEOLegislationCode | ✅ |
| LEGISLATION_CODE | WorkPhonePEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | ✅ |
| OBJECT_VERSION_NUMBER | WorkPhonePEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | ✅ |
| PERSON_ID | WorkPhonePEOPersonId | — |
| PHONE_ID | PhonesEOPhoneId | ✅ |
| PHONE_ID | WorkPhonePEOPhoneId | — |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_NUMBER | WorkPhonePEOPhoneNumber | — |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | ✅ |
| VALIDITY | PhonesEOValidity | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 8/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| COUNTRY_CODE_NUMBER | WorkPhonePEOCountryCodeNumber | — |
| CREATED_BY | PhonesEOCreatedBy | — |
| CREATION_DATE | PhonesEOCreationDate | — |
| DATE_FROM | PhonesEODateFrom | — |
| DATE_TO | PhonesEODateTo | — |
| EXTENSION | PhonesEOExtension | ✅ |
| EXTENSION | WorkPhonePEOExtension | — |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | — |
| LEGISLATION_CODE | PhonesEOLegislationCode | — |
| LEGISLATION_CODE | WorkPhonePEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | WorkPhonePEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | — |
| PERSON_ID | WorkPhonePEOPersonId | — |
| PHONE_ID | PhonesEOPhoneId | — |
| PHONE_ID | WorkPhonePEOPhoneId | — |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_NUMBER | WorkPhonePEOPhoneNumber | — |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | ✅ |
| VALIDITY | PhonesEOValidity | ✅ |

### [[personphonepvo|PersonPhonePVO]] (HCM · BICC: 10/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| CREATED_BY | PhonesEOCreatedBy | — |
| CREATION_DATE | PhonesEOCreationDate | ✅ |
| DATE_FROM | PhonesEODateFrom | ✅ |
| DATE_TO | PhonesEODateTo | ✅ |
| EXTENSION | PhonesEOExtension | — |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | — |
| LEGISLATION_CODE | PhonesEOLegislationCode | — |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | ✅ |
| PHONE_ID | PhoneId | ✅ |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SEARCH_PHONE_NUMBER | PhonesEOSearchPhoneNumber | — |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | — |
| VALIDITY | PhonesEOValidity | — |

### [[personrefpvo|PersonRefPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | — |
| EXTENSION | PhonesEOExtension | — |
| PHONE_ID | PhonesEOPhoneId | — |
| PHONE_NUMBER | PhonesEOPhoneNumber | — |
| PHONE_TYPE | PhonesEOPhoneType | — |
| SEARCH_PHONE_NUMBER | PhonesEOSearchPhoneNumber | — |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | — |
| VALIDITY | PhonesEOValidity | — |

### [[phonespvo|PhonesPVO]] (HCM · BICC: 17/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| CREATED_BY | PhonesEOCreatedBy | ✅ |
| CREATION_DATE | PhonesEOCreationDate | ✅ |
| DATE_FROM | PhonesEODateFrom | ✅ |
| DATE_TO | PhonesEODateTo | ✅ |
| EXTENSION | PhonesEOExtension | ✅ |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PhonesEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | ✅ |
| PHONE_ID | PhoneId | ✅ |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SEARCH_PHONE_NUMBER | PhonesEOSearchPhoneNumber | ✅ |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | ✅ |
| VALIDITY | PhonesEOValidity | ✅ |

### [[phonespvoviewall|PhonesPVOViewAll]] (HCM · BICC: 16/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AREA_CODE | PhonesEOAreaCode | ✅ |
| BUSINESS_GROUP_ID | PhonesEOBusinessGroupId | — |
| COUNTRY_CODE_NUMBER | PhonesEOCountryCodeNumber | ✅ |
| CREATED_BY | PhonesEOCreatedBy | ✅ |
| CREATION_DATE | PhonesEOCreationDate | ✅ |
| DATE_FROM | PhonesEODateFrom | ✅ |
| DATE_TO | PhonesEODateTo | ✅ |
| EXTENSION | PhonesEOExtension | ✅ |
| LAST_UPDATE_DATE | PhonesEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PhonesEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PhonesEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | PhonesEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | PhonesEOObjectVersionNumber | — |
| PERSON_ID | PhonesEOPersonId | ✅ |
| PHONE_ID | PhoneId | ✅ |
| PHONE_NUMBER | PhonesEOPhoneNumber | ✅ |
| PHONE_TYPE | PhonesEOPhoneType | ✅ |
| SEARCH_PHONE_NUMBER | PhonesEOSearchPhoneNumber | — |
| SPEED_DIAL_NUMBER | PhonesEOSpeedDialNumber | ✅ |
| VALIDITY | PhonesEOValidity | ✅ |
