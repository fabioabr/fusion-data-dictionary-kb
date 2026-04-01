---
id: DOC-HCM-688
doc_type: system-doc
title: "PER_PERSONS — Cadastro de Pessoas"
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
  - pessoas
  - cadastro-pessoa
  - person
  - core-hr
aliases:
  - PER_PERSONS
  - per_persons
  - cadastro-pessoas
  - tabela-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSONS

## Visão Geral

Tabela **central** do módulo HCM que armazena o cadastro de todas as **pessoas** no sistema — colaboradores, candidatos, contatos, dependentes e trabalhadores contingentes. É a tabela raiz para a maioria das entidades de pessoas no Oracle Fusion HCM.

> [!important] Tabela Core
> Esta é uma das tabelas mais referenciadas do HCM. Praticamente todas as tabelas PER_* possuem FK para `PER_PERSONS.PERSON_ID`.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro único de pessoas** — registro central de todas as pessoas no sistema
- **Base para vínculos empregatícios** — origem de dados para `PER_PERIODS_OF_SERVICE`
- **Gestão de identidade** — vinculação com nomes, endereços, documentos
- **Relatórios de headcount** — contagem de pessoas por tipo e status
- **Integrações com folha de pagamento** — referência base para processamentos
- **Auditoria e compliance** — rastreabilidade do ciclo de vida da pessoa

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pessoa | — | 🟢 95% |
| 2 | PERSON_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número da pessoa (matrícula visível ao usuário) | — | 🟢 95% |
| 3 | DATE_OF_BIRTH | DATE | NULL | Pessoal | Data de nascimento | — | 🟢 90% |
| 4 | DATE_OF_DEATH | DATE | NULL | Pessoal | Data de falecimento (quando aplicável) | — | 🟢 85% |
| 5 | COUNTRY_OF_BIRTH | VARCHAR2(60) | NULL | Pessoal | País de nascimento | — | 🟡 80% |
| 6 | REGION_OF_BIRTH | VARCHAR2(120) | NULL | Pessoal | Estado/região de nascimento | — | 🟡 75% |
| 7 | TOWN_OF_BIRTH | VARCHAR2(90) | NULL | Pessoal | Cidade de nascimento | — | 🟡 75% |
| 8 | START_DATE | DATE | NOT NULL | Controle | Data de início do registro no sistema | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma — esta é a tabela raiz de pessoas.

### Tabelas-filha (FK de saída)
- [[per_person_names_f]] — via `PERSON_ID` (nomes da pessoa ao longo do tempo)
- [[per_periods_of_service]] — via `PERSON_ID` (períodos de serviço da pessoa)
- [[per_all_assignments_m]] — via `PERSON_ID` (vínculos empregatícios da pessoa)
- [[per_national_identifiers]] — via `PERSON_ID` (documentos de identidade nacional da pessoa)
- [[per_passports]] — via `PERSON_ID` (passaportes da pessoa)
- [[per_phones]] — via `PERSON_ID` (telefones de contato da pessoa)
- [[per_person_addr_usages_f]] — via `PERSON_ID` (usos de endereço da pessoa)
- [[per_people_legislative_f]] — via `PERSON_ID` (dados legislativos)
- [[per_person_dlvry_methods]] — via `PERSON_ID` (métodos de entrega)
- [[per_person_type_usages_m]] — via `PERSON_ID` (tipos de pessoa)
- [[per_religions]] — via `PERSON_ID` (registros de religião da pessoa)

---

## Uso Típico

### Buscar pessoa por número/matrícula
```sql
SELECT p.PERSON_ID, p.PERSON_NUMBER, p.DATE_OF_BIRTH
FROM   PER_PERSONS p
WHERE  p.PERSON_NUMBER = :p_person_number;
```

### Listar todas as pessoas ativas
```sql
SELECT p.PERSON_ID, p.PERSON_NUMBER
FROM   PER_PERSONS p
WHERE  EXISTS (
  SELECT 1 FROM PER_PERIODS_OF_SERVICE ps
  WHERE ps.PERSON_ID = p.PERSON_ID
    AND ps.ACTUAL_TERMINATION_DATE IS NULL
);
```

---

## Observações

- Tabela central do HCM: alterações aqui impactam praticamente todas as funcionalidades.
- `PERSON_NUMBER` é o identificador visível ao usuário (matrícula).
- `PERSON_ID` é a chave técnica utilizada em todas as FKs.
- Contém dados PII (data de nascimento) — sujeita a LGPD/GDPR.
- Uma pessoa pode ter múltiplos períodos de serviço, atribuições e tipos.

---

## Referências

- [Oracle Docs — PER_PERSONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersons.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[candidateinteractionpvo|CandidateInteractionPVO]] (HCM · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId1 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |

### [[candidatepoolinteractionpvo|CandidatePoolInteractionPVO]] (HCM · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId1 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |

### [[contactrelshipspvo|ContactRelshipsPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| PERSON_ID | PersonPEOPersonId | — |

### [[contactrelshipspvoviewall|ContactRelshipsPVOViewAll]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| PERSON_ID | PersonPEOPersonId | ✅ |

### [[endorsementspvo|EndorsementsPVO]] (PO · BICC: 2/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE1 | Attribute116 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE10 | Attribute104 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE11 | Attribute117 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE12 | Attribute124 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE13 | Attribute134 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE14 | Attribute144 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE15 | Attribute154 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE16 | Attribute164 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE17 | Attribute174 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE18 | Attribute184 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE19 | Attribute194 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE2 | Attribute216 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE20 | Attribute204 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE21 | Attribute217 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE22 | Attribute224 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE23 | Attribute234 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE24 | Attribute244 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE25 | Attribute254 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE26 | Attribute264 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE27 | Attribute274 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE28 | Attribute284 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE29 | Attribute294 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE3 | Attribute313 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE30 | Attribute304 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE4 | Attribute413 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE5 | Attribute54 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE6 | Attribute64 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE7 | Attribute74 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE8 | Attribute84 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE9 | Attribute94 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CATEGORY | AttributeCategory4 | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE1 | AttributeDate19 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE10 | AttributeDate104 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE11 | AttributeDate114 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE12 | AttributeDate124 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE13 | AttributeDate134 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE14 | AttributeDate144 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE15 | AttributeDate154 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE2 | AttributeDate24 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE3 | AttributeDate34 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE4 | AttributeDate44 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE5 | AttributeDate54 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE6 | AttributeDate64 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE7 | AttributeDate74 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE8 | AttributeDate84 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_DATE9 | AttributeDate94 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber116 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber104 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber117 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber124 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber134 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber144 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber154 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber164 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber174 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber184 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber194 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber24 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber204 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber34 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber44 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber54 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber64 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber74 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber84 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber94 | — |
| BLOOD_TYPE | BloodType | — |
| BLOOD_TYPE | BloodType1 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage1 | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| COUNTRY_OF_BIRTH | CountryOfBirth1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATED_BY | CreatedBy5 | — |
| CREATION_DATE | CreationDate1 | — |
| CREATION_DATE | CreationDate5 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_BIRTH | DateOfBirth1 | — |
| DATE_OF_DEATH | DateOfDeath | — |
| DATE_OF_DEATH | DateOfDeath1 | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate5 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin5 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| LAST_UPDATED_BY | LastUpdatedBy5 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber5 | — |
| PARTY_ID | PartyId | — |
| PARTY_ID | PartyId1 | — |
| PERSON_ID | PersonId | — |
| PERSON_ID | PersonId4 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| REGION_OF_BIRTH | RegionOfBirth1 | — |
| START_DATE | StartDate | — |
| START_DATE | StartDate2 | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| TOWN_OF_BIRTH | TownOfBirth1 | — |
| USER_GUID | UserGuid | — |
| USER_GUID | UserGuid1 | — |

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 8/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE1 | Attribute112 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE10 | Attribute102 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE11 | Attribute113 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE12 | Attribute122 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE13 | Attribute132 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE14 | Attribute142 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE15 | Attribute152 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE16 | Attribute162 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE17 | Attribute172 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE18 | Attribute182 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE19 | Attribute192 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE2 | Attribute212 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE20 | Attribute202 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE21 | Attribute213 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE22 | Attribute222 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE23 | Attribute232 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE24 | Attribute242 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE25 | Attribute252 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE26 | Attribute262 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE27 | Attribute272 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE28 | Attribute282 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE29 | Attribute292 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE3 | Attribute32 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE30 | Attribute302 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE4 | Attribute42 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE5 | Attribute52 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE6 | Attribute62 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE7 | Attribute72 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE8 | Attribute82 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE9 | Attribute92 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_CATEGORY | AttributeCategory2 | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE1 | AttributeDate17 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE10 | AttributeDate102 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE11 | AttributeDate112 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE12 | AttributeDate122 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE13 | AttributeDate132 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE14 | AttributeDate142 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE15 | AttributeDate152 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE2 | AttributeDate22 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE3 | AttributeDate32 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE4 | AttributeDate42 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE5 | AttributeDate52 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE6 | AttributeDate62 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE7 | AttributeDate72 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE8 | AttributeDate82 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_DATE9 | AttributeDate92 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber112 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber102 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber113 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber122 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber132 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber142 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber152 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber162 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber172 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber182 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber192 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber22 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber202 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber32 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber42 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber52 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber62 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber72 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber82 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber92 | — |
| BLOOD_TYPE | BloodType | ✅ |
| BLOOD_TYPE | BloodType1 | — |
| BUSINESS_GROUP_ID | BusinessGroupId2 | — |
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | ✅ |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage1 | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | ✅ |
| COUNTRY_OF_BIRTH | CountryOfBirth1 | — |
| CREATED_BY | CreatedBy6 | — |
| CREATED_BY | CreatedBy8 | — |
| CREATION_DATE | CreationDate6 | — |
| CREATION_DATE | CreationDate8 | — |
| DATE_OF_BIRTH | DateOfBirth | ✅ |
| DATE_OF_BIRTH | DateOfBirth1 | — |
| DATE_OF_DEATH | DateOfDeath | — |
| DATE_OF_DEATH | DateOfDeath1 | — |
| LAST_UPDATE_DATE | LastUpdateDate6 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate8 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin6 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin8 | — |
| LAST_UPDATED_BY | LastUpdatedBy6 | — |
| LAST_UPDATED_BY | LastUpdatedBy8 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber5 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber7 | — |
| PARTY_ID | PartyId | — |
| PARTY_ID | PartyId1 | — |
| PERSON_ID | PersonId1 | — |
| PERSON_ID | PersonId3 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| REGION_OF_BIRTH | RegionOfBirth1 | — |
| START_DATE | StartDate | ✅ |
| START_DATE | StartDate1 | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| TOWN_OF_BIRTH | TownOfBirth1 | — |
| USER_GUID | UserGuid | — |
| USER_GUID | UserGuid1 | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 18/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BLOOD_TYPE | PersonPEOBloodType | ✅ |
| BUSINESS_GROUP_ID | PersonPEOBusinessGroupId | ✅ |
| CORRESPONDENCE_LANGUAGE | PersonPEOCorrespondenceLanguage | ✅ |
| COUNTRY_OF_BIRTH | PersonPEOCountryOfBirth | ✅ |
| CREATED_BY | PersonPEOCreatedBy | ✅ |
| CREATION_DATE | PersonPEOCreationDate | ✅ |
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| DATE_OF_DEATH | PersonPEODateOfDeath | ✅ |
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PersonPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PersonPEOObjectVersionNumber | ✅ |
| PARTY_ID | PersonPEOPartyId | ✅ |
| PERSON_ID | PersonId | ✅ |
| REGION_OF_BIRTH | PersonPEORegionOfBirth | ✅ |
| START_DATE | PersonPEOStartDate | ✅ |
| TOWN_OF_BIRTH | PersonPEOTownOfBirth | ✅ |
| USER_GUID | PersonPEOUserGuid | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 15/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BLOOD_TYPE | PersonPEOBloodType | ✅ |
| BUSINESS_GROUP_ID | PersonPEOBusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | PersonPEOCorrespondenceLanguage | ✅ |
| COUNTRY_OF_BIRTH | PersonPEOCountryOfBirth | ✅ |
| CREATED_BY | PersonPEOCreatedBy | ✅ |
| CREATION_DATE | PersonPEOCreationDate | ✅ |
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| DATE_OF_DEATH | PersonPEODateOfDeath | ✅ |
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PersonPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PersonPEOObjectVersionNumber | — |
| PARTY_ID | PersonPEOPartyId | — |
| PERSON_ID | PersonId | ✅ |
| REGION_OF_BIRTH | PersonPEORegionOfBirth | ✅ |
| START_DATE | PersonPEOStartDate | ✅ |
| TOWN_OF_BIRTH | PersonPEOTownOfBirth | ✅ |
| USER_GUID | PersonPEOUserGuid | ✅ |

### [[hitspvo|HitsPVO]] (PO · BICC: 1/168)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE1 | Attribute116 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE10 | Attribute104 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE11 | Attribute117 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE12 | Attribute124 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE13 | Attribute134 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE14 | Attribute144 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE15 | Attribute154 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE16 | Attribute164 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE17 | Attribute174 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE18 | Attribute184 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE19 | Attribute194 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE2 | Attribute216 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE20 | Attribute204 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE21 | Attribute217 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE22 | Attribute224 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE23 | Attribute234 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE24 | Attribute244 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE25 | Attribute254 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE26 | Attribute264 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE27 | Attribute274 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE28 | Attribute284 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE29 | Attribute294 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE3 | Attribute313 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE30 | Attribute304 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE4 | Attribute413 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE5 | Attribute54 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE6 | Attribute64 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE7 | Attribute74 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE8 | Attribute84 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE9 | Attribute94 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CATEGORY | AttributeCategory4 | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE1 | AttributeDate19 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE10 | AttributeDate104 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE11 | AttributeDate114 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE12 | AttributeDate124 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE13 | AttributeDate134 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE14 | AttributeDate144 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE15 | AttributeDate154 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE2 | AttributeDate24 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE3 | AttributeDate34 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE4 | AttributeDate44 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE5 | AttributeDate54 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE6 | AttributeDate64 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE7 | AttributeDate74 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE8 | AttributeDate84 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_DATE9 | AttributeDate94 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber116 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber104 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber117 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber124 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber134 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber144 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber154 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber164 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber174 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber184 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber194 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber24 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber204 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber34 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber44 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber54 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber64 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber74 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber84 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber94 | — |
| BLOOD_TYPE | BloodType | — |
| BLOOD_TYPE | BloodType1 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| BUSINESS_GROUP_ID | BusinessGroupId4 | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage1 | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| COUNTRY_OF_BIRTH | CountryOfBirth1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATED_BY | CreatedBy5 | — |
| CREATION_DATE | CreationDate1 | — |
| CREATION_DATE | CreationDate5 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_BIRTH | DateOfBirth1 | — |
| DATE_OF_DEATH | DateOfDeath | — |
| DATE_OF_DEATH | DateOfDeath1 | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate5 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin5 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| LAST_UPDATED_BY | LastUpdatedBy5 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber5 | — |
| PARTY_ID | PartyId | — |
| PARTY_ID | PartyId1 | — |
| PERSON_ID | PersonId | — |
| PERSON_ID | PersonId4 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| REGION_OF_BIRTH | RegionOfBirth1 | — |
| START_DATE | StartDate | — |
| START_DATE | StartDate2 | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| TOWN_OF_BIRTH | TownOfBirth1 | — |
| USER_GUID | UserGuid | — |
| USER_GUID | UserGuid1 | — |

### [[jobapplicationinteractionpvo|JobApplicationInteractionPVO]] (HCM · BICC: 2/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId1 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |

### [[offerpvo|OfferPVO]] (HCM · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId1 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |

### [[personnamepvo|PersonNamePVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| PERSON_ID | PersonPEOPersonId | ✅ |

### [[personnamepvoviewall|PersonNamePVOViewAll]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| PERSON_ID | PersonPEOPersonId | ✅ |

### [[personpvo|PersonPVO]] (HCM · BICC: 15/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BLOOD_TYPE | PersonPEOBloodType | ✅ |
| BUSINESS_GROUP_ID | PersonPEOBusinessGroupId | ✅ |
| CORRESPONDENCE_LANGUAGE | PersonPEOCorrespondenceLanguage | ✅ |
| COUNTRY_OF_BIRTH | PersonPEOCountryOfBirth | ✅ |
| CREATED_BY | PersonPEOCreatedBy | ✅ |
| CREATION_DATE | PersonPEOCreationDate | ✅ |
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| DATE_OF_DEATH | PersonPEODateOfDeath | ✅ |
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PersonPEOObjectVersionNumber | — |
| PARTY_ID | PersonPEOPartyId | ✅ |
| PERSON_ID | PersonId | ✅ |
| REGION_OF_BIRTH | PersonPEORegionOfBirth | ✅ |
| START_DATE | PersonPEOStartDate | ✅ |
| TOWN_OF_BIRTH | PersonPEOTownOfBirth | ✅ |
| USER_GUID | PersonPEOUserGuid | — |

### [[personpvoviewall|PersonPVOViewAll]] (HCM · BICC: 4/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BLOOD_TYPE | PersonPEOBloodType | — |
| BUSINESS_GROUP_ID | PersonPEOBusinessGroupId | ✅ |
| CORRESPONDENCE_LANGUAGE | PersonPEOCorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | PersonPEOCountryOfBirth | — |
| CREATED_BY | PersonPEOCreatedBy | — |
| CREATION_DATE | PersonPEOCreationDate | — |
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| DATE_OF_DEATH | PersonPEODateOfDeath | — |
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PersonPEOObjectVersionNumber | — |
| PARTY_ID | PersonPEOPartyId | — |
| PERSON_ID | PersonId | ✅ |
| REGION_OF_BIRTH | PersonPEORegionOfBirth | — |
| START_DATE | PersonPEOStartDate | — |
| TOWN_OF_BIRTH | PersonPEOTownOfBirth | — |
| USER_GUID | PersonPEOUserGuid | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BLOOD_TYPE | PersonPEOBloodType | — |
| CORRESPONDENCE_LANGUAGE | PersonPEOCorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | PersonPEOCountryOfBirth | — |
| DATE_OF_BIRTH | PersonPEODateOfBirth | ✅ |
| DATE_OF_DEATH | PersonPEODateOfDeath | — |
| PERSON_ID | PersonPEOPersonId | — |
| REGION_OF_BIRTH | PersonPEORegionOfBirth | — |
| TOWN_OF_BIRTH | PersonPEOTownOfBirth | — |
| USER_GUID | PersonPEOUserGuid | — |

### [[persontypeusagespvo|PersonTypeUsagesPVO]] (HCM · BICC: 2/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BLOOD_TYPE | PersonPEOBloodType | — |
| BUSINESS_GROUP_ID | PersonPEOBusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | PersonPEOCorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | PersonPEOCountryOfBirth | — |
| CREATED_BY | PersonPEOCreatedBy | — |
| CREATION_DATE | PersonPEOCreationDate | — |
| DATE_OF_BIRTH | PersonPEODateOfBirth | — |
| DATE_OF_DEATH | PersonPEODateOfDeath | — |
| LAST_UPDATE_DATE | PersonPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PersonPEOObjectVersionNumber | — |
| PARTY_ID | PersonPEOPartyId | — |
| PERSON_ID | PersonPEOPersonId | ✅ |
| REGION_OF_BIRTH | PersonPEORegionOfBirth | — |
| START_DATE | PersonPEOStartDate | — |
| TOWN_OF_BIRTH | PersonPEOTownOfBirth | — |

### [[projectplanlinebudgetpvo|ProjectPlanLineBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | BaselineIdForPlanVersionPersonId | — |
| PERSON_ID | LockedIdForPlanVersionPersonId | — |
| PERSON_ID | RejectedIdForPlanVersionPersonId | — |
| PERSON_ID | SubmittedIdForPlanVersionPersonId | — |
| USER_GUID | BaselineIdForPlanVersionUserGuid | — |
| USER_GUID | LockedIdForPlanVersionUserGuid | — |
| USER_GUID | RejectedIdForPlanVersionUserGuid | — |
| USER_GUID | SubmittedIdForPlanVersionUserGuid | — |

### [[projectplanlinedetailbudgetpvo|ProjectPlanLineDetailBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | BaselineIdForPlanVersionPersonId | — |
| PERSON_ID | LockedIdForPlanVersionPersonId | — |
| PERSON_ID | RejectedIdForPlanVersionPersonId | — |
| PERSON_ID | SubmittedIdForPlanVersionPersonId | — |
| USER_GUID | BaselineIdForPlanVersionUserGuid | — |
| USER_GUID | LockedIdForPlanVersionUserGuid | — |
| USER_GUID | RejectedIdForPlanVersionUserGuid | — |
| USER_GUID | SubmittedIdForPlanVersionUserGuid | — |

### [[projectplanlineforecastpvo|ProjectPlanLineForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | BaselineIdForPlanVersionPersonId | — |
| PERSON_ID | LockedIdForPlanVersionPersonId | — |
| PERSON_ID | RejectedIdForPlanVersionPersonId | — |
| PERSON_ID | SubmittedIdForPlanVersionPersonId | — |
| USER_GUID | BaselineIdForPlanVersionUserGuid | — |
| USER_GUID | LockedIdForPlanVersionUserGuid | — |
| USER_GUID | RejectedIdForPlanVersionUserGuid | — |
| USER_GUID | SubmittedIdForPlanVersionUserGuid | — |

### [[projectplanversionbudgetpvo|ProjectPlanVersionBudgetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | BaselineIdForPlanVersionPersonId | — |
| PERSON_ID | LockedIdForPlanVersionPersonId | — |
| PERSON_ID | RejectedIdForPlanVersionPersonId | — |
| PERSON_ID | SubmittedIdForPlanVersionPersonId | — |
| USER_GUID | BaselineIdForPlanVersionUserGuid | — |
| USER_GUID | LockedIdForPlanVersionUserGuid | — |
| USER_GUID | RejectedIdForPlanVersionUserGuid | — |
| USER_GUID | SubmittedIdForPlanVersionUserGuid | — |

### [[projectplanversionforecastpvo|ProjectPlanVersionForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | BaselineIdForPlanVersionPersonId | — |
| PERSON_ID | LockedIdForPlanVersionPersonId | — |
| PERSON_ID | RejectedIdForPlanVersionPersonId | — |
| PERSON_ID | SubmittedIdForPlanVersionPersonId | — |
| USER_GUID | BaselineIdForPlanVersionUserGuid | — |
| USER_GUID | LockedIdForPlanVersionUserGuid | — |
| USER_GUID | RejectedIdForPlanVersionUserGuid | — |
| USER_GUID | SubmittedIdForPlanVersionUserGuid | — |

### [[projplanlinedetailforecastpvo|ProjPlanLineDetailForecastPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PERSON_ID | BaselineIdForPlanVersionPersonId | — |
| PERSON_ID | LockedIdForPlanVersionPersonId | — |
| PERSON_ID | RejectedIdForPlanVersionPersonId | — |
| PERSON_ID | SubmittedIdForPlanVersionPersonId | — |
| USER_GUID | BaselineIdForPlanVersionUserGuid | — |
| USER_GUID | LockedIdForPlanVersionUserGuid | — |
| USER_GUID | RejectedIdForPlanVersionUserGuid | — |
| USER_GUID | SubmittedIdForPlanVersionUserGuid | — |

### [[prospectinteractionpvo|ProspectInteractionPVO]] (HCM · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId1 | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |

### [[referralspvo|ReferralsPVO]] (PO · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |

### [[sharespvo|SharesPVO]] (PO · BICC: 1/84)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BLOOD_TYPE | BloodType | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CORRESPONDENCE_LANGUAGE | CorrespondenceLanguage | — |
| COUNTRY_OF_BIRTH | CountryOfBirth | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATE_OF_BIRTH | DateOfBirth | — |
| DATE_OF_DEATH | DateOfDeath | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PARTY_ID | PartyId | — |
| PERSON_ID | PersonId | — |
| REGION_OF_BIRTH | RegionOfBirth | — |
| START_DATE | StartDate | — |
| TOWN_OF_BIRTH | TownOfBirth | — |
| USER_GUID | UserGuid | — |
