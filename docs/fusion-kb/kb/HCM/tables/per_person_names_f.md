---
id: DOC-HCM-691
doc_type: system-doc
title: "PER_PERSON_NAMES_F — Nomes de Pessoas"
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
  - nomes-pessoas
  - person-names
  - nome-completo
  - core-hr
aliases:
  - PER_PERSON_NAMES_F
  - per_person_names_f
  - nomes-pessoas
  - person-names-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_NAMES_F

## Visão Geral

Armazena os **nomes** das pessoas no sistema com vigência temporal. Suporta múltiplos tipos de nome (legal, preferido, exibição) e legislações, permitindo rastrear mudanças de nome ao longo do tempo.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Identificação de colaboradores** — nome completo para exibição em sistemas
- **Documentos legais** — nome legal para contratos, holerites, eSocial
- **Alteração de nome** — casamento, divórcio, retificação
- **Relatórios regulatórios** — RAIS, DIRF, eSocial exigem nome legal vigente
- **Busca e pesquisa** — localizar pessoas por nome ou sobrenome

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_NAME_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de nome | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | NAME_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de nome (GLOBAL, LEGAL, PREFERRED) | — | 🟢 90% |
| 4 | LEGISLATION_CODE | VARCHAR2(4) | NULL | Classificação | Código do país/legislação | — | 🟢 85% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | FIRST_NAME | VARCHAR2(150) | NULL | Nome | Primeiro nome | — | 🟢 95% |
| 8 | MIDDLE_NAMES | VARCHAR2(80) | NULL | Nome | Nomes do meio | — | 🟢 90% |
| 9 | LAST_NAME | VARCHAR2(150) | NOT NULL | Nome | Sobrenome | — | 🟢 95% |
| 10 | FULL_NAME | VARCHAR2(360) | NULL | Nome | Nome completo concatenado | — | 🟢 90% |
| 11 | DISPLAY_NAME | VARCHAR2(360) | NULL | Nome | Nome para exibição | — | 🟢 85% |
| 12 | LIST_NAME | VARCHAR2(360) | NULL | Nome | Nome para listas (sobrenome, nome) | — | 🟡 80% |
| 13 | TITLE | VARCHAR2(30) | NULL | Nome | Título (Sr., Sra., Dr.) | — | 🟡 80% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 18 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa titular do registro de nome)

### Tabelas-filha (FK de saída)

---

## Uso Típico

### Nome legal vigente de um colaborador
```sql
SELECT pn.FIRST_NAME, pn.LAST_NAME, pn.FULL_NAME
FROM   PER_PERSON_NAMES_F pn
WHERE  pn.PERSON_ID = :p_person_id
  AND  pn.NAME_TYPE = 'GLOBAL'
  AND  SYSDATE BETWEEN pn.EFFECTIVE_START_DATE AND pn.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência para obter o nome corrente.
- `NAME_TYPE = 'GLOBAL'` é o tipo padrão usado na maioria das consultas.
- `FULL_NAME` é calculado automaticamente a partir das partes do nome.
- Contém dados PII — sujeita a LGPD/GDPR.
- Alterações de nome (casamento, etc.) geram novos registros com novas datas de vigência.

---

## Referências

- [Oracle Docs — PER_PERSON_NAMES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersonnamesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[grantsbusinessunitpvo|GrantsBusinessUnitPVO]] (OTHER · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | PersonNameDPEODisplayName | ✅ |
| EFFECTIVE_END_DATE | PersonNameDPEOEffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | PersonNameDPEOEffectiveStartDate | ✅ |
| OBJECT_VERSION_NUMBER | PersonNameDPEOObjectVersionNumber | — |
| PERSON_NAME_ID | PersonNameDPEOPersonNameId | — |

### [[personnamebasicpvoglobalname|PersonNameBasicPVOGlobalName]] (HCM · BICC: 54/160)

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
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CHAR_SET_CONTEXT | CharSetContext | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_NAME | DisplayName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FIRST_NAME | FirstName | ✅ |
| FULL_NAME | FullName | ✅ |
| HONORS | Honors | ✅ |
| KNOWN_AS | KnownAs | ✅ |
| LAST_NAME | LastName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LIST_NAME | ListName | ✅ |
| MIDDLE_NAMES | MiddleNames | ✅ |
| MILITARY_RANK | MilitaryRank | ✅ |
| NAM_INFORMATION1 | NamInformation1 | ✅ |
| NAM_INFORMATION10 | NamInformation10 | ✅ |
| NAM_INFORMATION11 | NamInformation11 | ✅ |
| NAM_INFORMATION12 | NamInformation12 | ✅ |
| NAM_INFORMATION13 | NamInformation13 | ✅ |
| NAM_INFORMATION14 | NamInformation14 | ✅ |
| NAM_INFORMATION15 | NamInformation15 | ✅ |
| NAM_INFORMATION16 | NamInformation16 | ✅ |
| NAM_INFORMATION17 | NamInformation17 | ✅ |
| NAM_INFORMATION18 | NamInformation18 | ✅ |
| NAM_INFORMATION19 | NamInformation19 | ✅ |
| NAM_INFORMATION2 | NamInformation2 | ✅ |
| NAM_INFORMATION20 | NamInformation20 | ✅ |
| NAM_INFORMATION21 | NamInformation21 | ✅ |
| NAM_INFORMATION22 | NamInformation22 | ✅ |
| NAM_INFORMATION23 | NamInformation23 | ✅ |
| NAM_INFORMATION24 | NamInformation24 | ✅ |
| NAM_INFORMATION25 | NamInformation25 | ✅ |
| NAM_INFORMATION26 | NamInformation26 | ✅ |
| NAM_INFORMATION27 | NamInformation27 | ✅ |
| NAM_INFORMATION28 | NamInformation28 | ✅ |
| NAM_INFORMATION29 | NamInformation29 | ✅ |
| NAM_INFORMATION3 | NamInformation3 | ✅ |
| NAM_INFORMATION30 | NamInformation30 | ✅ |
| NAM_INFORMATION4 | NamInformation4 | ✅ |
| NAM_INFORMATION5 | NamInformation5 | ✅ |
| NAM_INFORMATION6 | NamInformation6 | ✅ |
| NAM_INFORMATION7 | NamInformation7 | ✅ |
| NAM_INFORMATION8 | NamInformation8 | ✅ |
| NAM_INFORMATION9 | NamInformation9 | ✅ |
| NAM_INFORMATION_CATEGORY | NamInformationCategory | — |
| NAM_INFORMATION_DATE1 | NamInformationDate1 | — |
| NAM_INFORMATION_DATE10 | NamInformationDate10 | — |
| NAM_INFORMATION_DATE11 | NamInformationDate11 | — |
| NAM_INFORMATION_DATE12 | NamInformationDate12 | — |
| NAM_INFORMATION_DATE13 | NamInformationDate13 | — |
| NAM_INFORMATION_DATE14 | NamInformationDate14 | — |
| NAM_INFORMATION_DATE15 | NamInformationDate15 | — |
| NAM_INFORMATION_DATE2 | NamInformationDate2 | — |
| NAM_INFORMATION_DATE3 | NamInformationDate3 | — |
| NAM_INFORMATION_DATE4 | NamInformationDate4 | — |
| NAM_INFORMATION_DATE5 | NamInformationDate5 | — |
| NAM_INFORMATION_DATE6 | NamInformationDate6 | — |
| NAM_INFORMATION_DATE7 | NamInformationDate7 | — |
| NAM_INFORMATION_DATE8 | NamInformationDate8 | — |
| NAM_INFORMATION_DATE9 | NamInformationDate9 | — |
| NAM_INFORMATION_NUMBER1 | NamInformationNumber1 | — |
| NAM_INFORMATION_NUMBER10 | NamInformationNumber10 | — |
| NAM_INFORMATION_NUMBER11 | NamInformationNumber11 | — |
| NAM_INFORMATION_NUMBER12 | NamInformationNumber12 | — |
| NAM_INFORMATION_NUMBER13 | NamInformationNumber13 | — |
| NAM_INFORMATION_NUMBER14 | NamInformationNumber14 | — |
| NAM_INFORMATION_NUMBER15 | NamInformationNumber15 | — |
| NAM_INFORMATION_NUMBER16 | NamInformationNumber16 | — |
| NAM_INFORMATION_NUMBER17 | NamInformationNumber17 | — |
| NAM_INFORMATION_NUMBER18 | NamInformationNumber18 | — |
| NAM_INFORMATION_NUMBER19 | NamInformationNumber19 | — |
| NAM_INFORMATION_NUMBER2 | NamInformationNumber2 | — |
| NAM_INFORMATION_NUMBER20 | NamInformationNumber20 | — |
| NAM_INFORMATION_NUMBER3 | NamInformationNumber3 | — |
| NAM_INFORMATION_NUMBER4 | NamInformationNumber4 | — |
| NAM_INFORMATION_NUMBER5 | NamInformationNumber5 | — |
| NAM_INFORMATION_NUMBER6 | NamInformationNumber6 | — |
| NAM_INFORMATION_NUMBER7 | NamInformationNumber7 | — |
| NAM_INFORMATION_NUMBER8 | NamInformationNumber8 | — |
| NAM_INFORMATION_NUMBER9 | NamInformationNumber9 | — |
| NAME_TYPE | NameType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORDER_NAME | OrderName | ✅ |
| PERSON_ID | PersonId | ✅ |
| PERSON_NAME_ID | PersonNameId | ✅ |
| PRE_NAME_ADJUNCT | PreNameAdjunct | ✅ |
| PREVIOUS_LAST_NAME | PreviousLastName | ✅ |
| SUFFIX | Suffix | ✅ |
| TITLE | Title | ✅ |

### [[personnamebasicpvoglobalnameviewall|PersonNameBasicPVOGlobalNameViewAll]] (HCM · BICC: 54/160)

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
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CHAR_SET_CONTEXT | CharSetContext | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_NAME | DisplayName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FIRST_NAME | FirstName | ✅ |
| FULL_NAME | FullName | ✅ |
| HONORS | Honors | ✅ |
| KNOWN_AS | KnownAs | ✅ |
| LAST_NAME | LastName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LIST_NAME | ListName | ✅ |
| MIDDLE_NAMES | MiddleNames | ✅ |
| MILITARY_RANK | MilitaryRank | ✅ |
| NAM_INFORMATION1 | NamInformation1 | ✅ |
| NAM_INFORMATION10 | NamInformation10 | ✅ |
| NAM_INFORMATION11 | NamInformation11 | ✅ |
| NAM_INFORMATION12 | NamInformation12 | ✅ |
| NAM_INFORMATION13 | NamInformation13 | ✅ |
| NAM_INFORMATION14 | NamInformation14 | ✅ |
| NAM_INFORMATION15 | NamInformation15 | ✅ |
| NAM_INFORMATION16 | NamInformation16 | ✅ |
| NAM_INFORMATION17 | NamInformation17 | ✅ |
| NAM_INFORMATION18 | NamInformation18 | ✅ |
| NAM_INFORMATION19 | NamInformation19 | ✅ |
| NAM_INFORMATION2 | NamInformation2 | ✅ |
| NAM_INFORMATION20 | NamInformation20 | ✅ |
| NAM_INFORMATION21 | NamInformation21 | ✅ |
| NAM_INFORMATION22 | NamInformation22 | ✅ |
| NAM_INFORMATION23 | NamInformation23 | ✅ |
| NAM_INFORMATION24 | NamInformation24 | ✅ |
| NAM_INFORMATION25 | NamInformation25 | ✅ |
| NAM_INFORMATION26 | NamInformation26 | ✅ |
| NAM_INFORMATION27 | NamInformation27 | ✅ |
| NAM_INFORMATION28 | NamInformation28 | ✅ |
| NAM_INFORMATION29 | NamInformation29 | ✅ |
| NAM_INFORMATION3 | NamInformation3 | ✅ |
| NAM_INFORMATION30 | NamInformation30 | ✅ |
| NAM_INFORMATION4 | NamInformation4 | ✅ |
| NAM_INFORMATION5 | NamInformation5 | ✅ |
| NAM_INFORMATION6 | NamInformation6 | ✅ |
| NAM_INFORMATION7 | NamInformation7 | ✅ |
| NAM_INFORMATION8 | NamInformation8 | ✅ |
| NAM_INFORMATION9 | NamInformation9 | ✅ |
| NAM_INFORMATION_CATEGORY | NamInformationCategory | — |
| NAM_INFORMATION_DATE1 | NamInformationDate1 | — |
| NAM_INFORMATION_DATE10 | NamInformationDate10 | — |
| NAM_INFORMATION_DATE11 | NamInformationDate11 | — |
| NAM_INFORMATION_DATE12 | NamInformationDate12 | — |
| NAM_INFORMATION_DATE13 | NamInformationDate13 | — |
| NAM_INFORMATION_DATE14 | NamInformationDate14 | — |
| NAM_INFORMATION_DATE15 | NamInformationDate15 | — |
| NAM_INFORMATION_DATE2 | NamInformationDate2 | — |
| NAM_INFORMATION_DATE3 | NamInformationDate3 | — |
| NAM_INFORMATION_DATE4 | NamInformationDate4 | — |
| NAM_INFORMATION_DATE5 | NamInformationDate5 | — |
| NAM_INFORMATION_DATE6 | NamInformationDate6 | — |
| NAM_INFORMATION_DATE7 | NamInformationDate7 | — |
| NAM_INFORMATION_DATE8 | NamInformationDate8 | — |
| NAM_INFORMATION_DATE9 | NamInformationDate9 | — |
| NAM_INFORMATION_NUMBER1 | NamInformationNumber1 | — |
| NAM_INFORMATION_NUMBER10 | NamInformationNumber10 | — |
| NAM_INFORMATION_NUMBER11 | NamInformationNumber11 | — |
| NAM_INFORMATION_NUMBER12 | NamInformationNumber12 | — |
| NAM_INFORMATION_NUMBER13 | NamInformationNumber13 | — |
| NAM_INFORMATION_NUMBER14 | NamInformationNumber14 | — |
| NAM_INFORMATION_NUMBER15 | NamInformationNumber15 | — |
| NAM_INFORMATION_NUMBER16 | NamInformationNumber16 | — |
| NAM_INFORMATION_NUMBER17 | NamInformationNumber17 | — |
| NAM_INFORMATION_NUMBER18 | NamInformationNumber18 | — |
| NAM_INFORMATION_NUMBER19 | NamInformationNumber19 | — |
| NAM_INFORMATION_NUMBER2 | NamInformationNumber2 | — |
| NAM_INFORMATION_NUMBER20 | NamInformationNumber20 | — |
| NAM_INFORMATION_NUMBER3 | NamInformationNumber3 | — |
| NAM_INFORMATION_NUMBER4 | NamInformationNumber4 | — |
| NAM_INFORMATION_NUMBER5 | NamInformationNumber5 | — |
| NAM_INFORMATION_NUMBER6 | NamInformationNumber6 | — |
| NAM_INFORMATION_NUMBER7 | NamInformationNumber7 | — |
| NAM_INFORMATION_NUMBER8 | NamInformationNumber8 | — |
| NAM_INFORMATION_NUMBER9 | NamInformationNumber9 | — |
| NAME_TYPE | NameType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORDER_NAME | OrderName | ✅ |
| PERSON_ID | PersonId | ✅ |
| PERSON_NAME_ID | PersonNameId | ✅ |
| PRE_NAME_ADJUNCT | PreNameAdjunct | ✅ |
| PREVIOUS_LAST_NAME | PreviousLastName | ✅ |
| SUFFIX | Suffix | ✅ |
| TITLE | Title | ✅ |

### [[personnamebasicpvolocalname|PersonNameBasicPVOLocalName]] (HCM · BICC: 54/160)

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
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CHAR_SET_CONTEXT | CharSetContext | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_NAME | DisplayName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FIRST_NAME | FirstName | ✅ |
| FULL_NAME | FullName | ✅ |
| HONORS | Honors | ✅ |
| KNOWN_AS | KnownAs | ✅ |
| LAST_NAME | LastName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LIST_NAME | ListName | ✅ |
| MIDDLE_NAMES | MiddleNames | ✅ |
| MILITARY_RANK | MilitaryRank | ✅ |
| NAM_INFORMATION1 | NamInformation1 | ✅ |
| NAM_INFORMATION10 | NamInformation10 | ✅ |
| NAM_INFORMATION11 | NamInformation11 | ✅ |
| NAM_INFORMATION12 | NamInformation12 | ✅ |
| NAM_INFORMATION13 | NamInformation13 | ✅ |
| NAM_INFORMATION14 | NamInformation14 | ✅ |
| NAM_INFORMATION15 | NamInformation15 | ✅ |
| NAM_INFORMATION16 | NamInformation16 | ✅ |
| NAM_INFORMATION17 | NamInformation17 | ✅ |
| NAM_INFORMATION18 | NamInformation18 | ✅ |
| NAM_INFORMATION19 | NamInformation19 | ✅ |
| NAM_INFORMATION2 | NamInformation2 | ✅ |
| NAM_INFORMATION20 | NamInformation20 | ✅ |
| NAM_INFORMATION21 | NamInformation21 | ✅ |
| NAM_INFORMATION22 | NamInformation22 | ✅ |
| NAM_INFORMATION23 | NamInformation23 | ✅ |
| NAM_INFORMATION24 | NamInformation24 | ✅ |
| NAM_INFORMATION25 | NamInformation25 | ✅ |
| NAM_INFORMATION26 | NamInformation26 | ✅ |
| NAM_INFORMATION27 | NamInformation27 | ✅ |
| NAM_INFORMATION28 | NamInformation28 | ✅ |
| NAM_INFORMATION29 | NamInformation29 | ✅ |
| NAM_INFORMATION3 | NamInformation3 | ✅ |
| NAM_INFORMATION30 | NamInformation30 | ✅ |
| NAM_INFORMATION4 | NamInformation4 | ✅ |
| NAM_INFORMATION5 | NamInformation5 | ✅ |
| NAM_INFORMATION6 | NamInformation6 | ✅ |
| NAM_INFORMATION7 | NamInformation7 | ✅ |
| NAM_INFORMATION8 | NamInformation8 | ✅ |
| NAM_INFORMATION9 | NamInformation9 | ✅ |
| NAM_INFORMATION_CATEGORY | NamInformationCategory | — |
| NAM_INFORMATION_DATE1 | NamInformationDate1 | — |
| NAM_INFORMATION_DATE10 | NamInformationDate10 | — |
| NAM_INFORMATION_DATE11 | NamInformationDate11 | — |
| NAM_INFORMATION_DATE12 | NamInformationDate12 | — |
| NAM_INFORMATION_DATE13 | NamInformationDate13 | — |
| NAM_INFORMATION_DATE14 | NamInformationDate14 | — |
| NAM_INFORMATION_DATE15 | NamInformationDate15 | — |
| NAM_INFORMATION_DATE2 | NamInformationDate2 | — |
| NAM_INFORMATION_DATE3 | NamInformationDate3 | — |
| NAM_INFORMATION_DATE4 | NamInformationDate4 | — |
| NAM_INFORMATION_DATE5 | NamInformationDate5 | — |
| NAM_INFORMATION_DATE6 | NamInformationDate6 | — |
| NAM_INFORMATION_DATE7 | NamInformationDate7 | — |
| NAM_INFORMATION_DATE8 | NamInformationDate8 | — |
| NAM_INFORMATION_DATE9 | NamInformationDate9 | — |
| NAM_INFORMATION_NUMBER1 | NamInformationNumber1 | — |
| NAM_INFORMATION_NUMBER10 | NamInformationNumber10 | — |
| NAM_INFORMATION_NUMBER11 | NamInformationNumber11 | — |
| NAM_INFORMATION_NUMBER12 | NamInformationNumber12 | — |
| NAM_INFORMATION_NUMBER13 | NamInformationNumber13 | — |
| NAM_INFORMATION_NUMBER14 | NamInformationNumber14 | — |
| NAM_INFORMATION_NUMBER15 | NamInformationNumber15 | — |
| NAM_INFORMATION_NUMBER16 | NamInformationNumber16 | — |
| NAM_INFORMATION_NUMBER17 | NamInformationNumber17 | — |
| NAM_INFORMATION_NUMBER18 | NamInformationNumber18 | — |
| NAM_INFORMATION_NUMBER19 | NamInformationNumber19 | — |
| NAM_INFORMATION_NUMBER2 | NamInformationNumber2 | — |
| NAM_INFORMATION_NUMBER20 | NamInformationNumber20 | — |
| NAM_INFORMATION_NUMBER3 | NamInformationNumber3 | — |
| NAM_INFORMATION_NUMBER4 | NamInformationNumber4 | — |
| NAM_INFORMATION_NUMBER5 | NamInformationNumber5 | — |
| NAM_INFORMATION_NUMBER6 | NamInformationNumber6 | — |
| NAM_INFORMATION_NUMBER7 | NamInformationNumber7 | — |
| NAM_INFORMATION_NUMBER8 | NamInformationNumber8 | — |
| NAM_INFORMATION_NUMBER9 | NamInformationNumber9 | — |
| NAME_TYPE | NameType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORDER_NAME | OrderName | ✅ |
| PERSON_ID | PersonId | ✅ |
| PERSON_NAME_ID | PersonNameId | ✅ |
| PRE_NAME_ADJUNCT | PreNameAdjunct | ✅ |
| PREVIOUS_LAST_NAME | PreviousLastName | ✅ |
| SUFFIX | Suffix | ✅ |
| TITLE | Title | ✅ |

### [[personnamebasicpvolocalnameviewall|PersonNameBasicPVOLocalNameViewAll]] (HCM · BICC: 54/160)

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
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CHAR_SET_CONTEXT | CharSetContext | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_NAME | DisplayName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FIRST_NAME | FirstName | ✅ |
| FULL_NAME | FullName | ✅ |
| HONORS | Honors | ✅ |
| KNOWN_AS | KnownAs | ✅ |
| LAST_NAME | LastName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LIST_NAME | ListName | ✅ |
| MIDDLE_NAMES | MiddleNames | ✅ |
| MILITARY_RANK | MilitaryRank | ✅ |
| NAM_INFORMATION1 | NamInformation1 | ✅ |
| NAM_INFORMATION10 | NamInformation10 | ✅ |
| NAM_INFORMATION11 | NamInformation11 | ✅ |
| NAM_INFORMATION12 | NamInformation12 | ✅ |
| NAM_INFORMATION13 | NamInformation13 | ✅ |
| NAM_INFORMATION14 | NamInformation14 | ✅ |
| NAM_INFORMATION15 | NamInformation15 | ✅ |
| NAM_INFORMATION16 | NamInformation16 | ✅ |
| NAM_INFORMATION17 | NamInformation17 | ✅ |
| NAM_INFORMATION18 | NamInformation18 | ✅ |
| NAM_INFORMATION19 | NamInformation19 | ✅ |
| NAM_INFORMATION2 | NamInformation2 | ✅ |
| NAM_INFORMATION20 | NamInformation20 | ✅ |
| NAM_INFORMATION21 | NamInformation21 | ✅ |
| NAM_INFORMATION22 | NamInformation22 | ✅ |
| NAM_INFORMATION23 | NamInformation23 | ✅ |
| NAM_INFORMATION24 | NamInformation24 | ✅ |
| NAM_INFORMATION25 | NamInformation25 | ✅ |
| NAM_INFORMATION26 | NamInformation26 | ✅ |
| NAM_INFORMATION27 | NamInformation27 | ✅ |
| NAM_INFORMATION28 | NamInformation28 | ✅ |
| NAM_INFORMATION29 | NamInformation29 | ✅ |
| NAM_INFORMATION3 | NamInformation3 | ✅ |
| NAM_INFORMATION30 | NamInformation30 | ✅ |
| NAM_INFORMATION4 | NamInformation4 | ✅ |
| NAM_INFORMATION5 | NamInformation5 | ✅ |
| NAM_INFORMATION6 | NamInformation6 | ✅ |
| NAM_INFORMATION7 | NamInformation7 | ✅ |
| NAM_INFORMATION8 | NamInformation8 | ✅ |
| NAM_INFORMATION9 | NamInformation9 | ✅ |
| NAM_INFORMATION_CATEGORY | NamInformationCategory | — |
| NAM_INFORMATION_DATE1 | NamInformationDate1 | — |
| NAM_INFORMATION_DATE10 | NamInformationDate10 | — |
| NAM_INFORMATION_DATE11 | NamInformationDate11 | — |
| NAM_INFORMATION_DATE12 | NamInformationDate12 | — |
| NAM_INFORMATION_DATE13 | NamInformationDate13 | — |
| NAM_INFORMATION_DATE14 | NamInformationDate14 | — |
| NAM_INFORMATION_DATE15 | NamInformationDate15 | — |
| NAM_INFORMATION_DATE2 | NamInformationDate2 | — |
| NAM_INFORMATION_DATE3 | NamInformationDate3 | — |
| NAM_INFORMATION_DATE4 | NamInformationDate4 | — |
| NAM_INFORMATION_DATE5 | NamInformationDate5 | — |
| NAM_INFORMATION_DATE6 | NamInformationDate6 | — |
| NAM_INFORMATION_DATE7 | NamInformationDate7 | — |
| NAM_INFORMATION_DATE8 | NamInformationDate8 | — |
| NAM_INFORMATION_DATE9 | NamInformationDate9 | — |
| NAM_INFORMATION_NUMBER1 | NamInformationNumber1 | — |
| NAM_INFORMATION_NUMBER10 | NamInformationNumber10 | — |
| NAM_INFORMATION_NUMBER11 | NamInformationNumber11 | — |
| NAM_INFORMATION_NUMBER12 | NamInformationNumber12 | — |
| NAM_INFORMATION_NUMBER13 | NamInformationNumber13 | — |
| NAM_INFORMATION_NUMBER14 | NamInformationNumber14 | — |
| NAM_INFORMATION_NUMBER15 | NamInformationNumber15 | — |
| NAM_INFORMATION_NUMBER16 | NamInformationNumber16 | — |
| NAM_INFORMATION_NUMBER17 | NamInformationNumber17 | — |
| NAM_INFORMATION_NUMBER18 | NamInformationNumber18 | — |
| NAM_INFORMATION_NUMBER19 | NamInformationNumber19 | — |
| NAM_INFORMATION_NUMBER2 | NamInformationNumber2 | — |
| NAM_INFORMATION_NUMBER20 | NamInformationNumber20 | — |
| NAM_INFORMATION_NUMBER3 | NamInformationNumber3 | — |
| NAM_INFORMATION_NUMBER4 | NamInformationNumber4 | — |
| NAM_INFORMATION_NUMBER5 | NamInformationNumber5 | — |
| NAM_INFORMATION_NUMBER6 | NamInformationNumber6 | — |
| NAM_INFORMATION_NUMBER7 | NamInformationNumber7 | — |
| NAM_INFORMATION_NUMBER8 | NamInformationNumber8 | — |
| NAM_INFORMATION_NUMBER9 | NamInformationNumber9 | — |
| NAME_TYPE | NameType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORDER_NAME | OrderName | ✅ |
| PERSON_ID | PersonId | ✅ |
| PERSON_NAME_ID | PersonNameId | ✅ |
| PRE_NAME_ADJUNCT | PreNameAdjunct | ✅ |
| PREVIOUS_LAST_NAME | PreviousLastName | ✅ |
| SUFFIX | Suffix | ✅ |
| TITLE | Title | ✅ |

### [[personnameextractpvo|PersonNameExtractPVO]] (HCM · BICC: 30/160)

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
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CHAR_SET_CONTEXT | CharSetContext | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISPLAY_NAME | DisplayName | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FIRST_NAME | FirstName | ✅ |
| FULL_NAME | FullName | ✅ |
| HONORS | Honors | ✅ |
| KNOWN_AS | KnownAs | ✅ |
| LAST_NAME | LastName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LIST_NAME | ListName | ✅ |
| MIDDLE_NAMES | MiddleNames | ✅ |
| MILITARY_RANK | MilitaryRank | ✅ |
| NAM_INFORMATION1 | NamInformation1 | — |
| NAM_INFORMATION10 | NamInformation10 | — |
| NAM_INFORMATION11 | NamInformation11 | — |
| NAM_INFORMATION12 | NamInformation12 | — |
| NAM_INFORMATION13 | NamInformation13 | — |
| NAM_INFORMATION14 | NamInformation14 | — |
| NAM_INFORMATION15 | NamInformation15 | — |
| NAM_INFORMATION16 | NamInformation16 | — |
| NAM_INFORMATION17 | NamInformation17 | — |
| NAM_INFORMATION18 | NamInformation18 | — |
| NAM_INFORMATION19 | NamInformation19 | — |
| NAM_INFORMATION2 | NamInformation2 | — |
| NAM_INFORMATION20 | NamInformation20 | — |
| NAM_INFORMATION21 | NamInformation21 | — |
| NAM_INFORMATION22 | NamInformation22 | — |
| NAM_INFORMATION23 | NamInformation23 | — |
| NAM_INFORMATION24 | NamInformation24 | — |
| NAM_INFORMATION25 | NamInformation25 | — |
| NAM_INFORMATION26 | NamInformation26 | — |
| NAM_INFORMATION27 | NamInformation27 | — |
| NAM_INFORMATION28 | NamInformation28 | — |
| NAM_INFORMATION29 | NamInformation29 | — |
| NAM_INFORMATION3 | NamInformation3 | — |
| NAM_INFORMATION30 | NamInformation30 | — |
| NAM_INFORMATION4 | NamInformation4 | — |
| NAM_INFORMATION5 | NamInformation5 | — |
| NAM_INFORMATION6 | NamInformation6 | — |
| NAM_INFORMATION7 | NamInformation7 | — |
| NAM_INFORMATION8 | NamInformation8 | — |
| NAM_INFORMATION9 | NamInformation9 | — |
| NAM_INFORMATION_CATEGORY | NamInformationCategory | ✅ |
| NAM_INFORMATION_DATE1 | NamInformationDate1 | — |
| NAM_INFORMATION_DATE10 | NamInformationDate10 | — |
| NAM_INFORMATION_DATE11 | NamInformationDate11 | — |
| NAM_INFORMATION_DATE12 | NamInformationDate12 | — |
| NAM_INFORMATION_DATE13 | NamInformationDate13 | — |
| NAM_INFORMATION_DATE14 | NamInformationDate14 | — |
| NAM_INFORMATION_DATE15 | NamInformationDate15 | — |
| NAM_INFORMATION_DATE2 | NamInformationDate2 | — |
| NAM_INFORMATION_DATE3 | NamInformationDate3 | — |
| NAM_INFORMATION_DATE4 | NamInformationDate4 | — |
| NAM_INFORMATION_DATE5 | NamInformationDate5 | — |
| NAM_INFORMATION_DATE6 | NamInformationDate6 | — |
| NAM_INFORMATION_DATE7 | NamInformationDate7 | — |
| NAM_INFORMATION_DATE8 | NamInformationDate8 | — |
| NAM_INFORMATION_DATE9 | NamInformationDate9 | — |
| NAM_INFORMATION_NUMBER1 | NamInformationNumber1 | — |
| NAM_INFORMATION_NUMBER10 | NamInformationNumber10 | — |
| NAM_INFORMATION_NUMBER11 | NamInformationNumber11 | — |
| NAM_INFORMATION_NUMBER12 | NamInformationNumber12 | — |
| NAM_INFORMATION_NUMBER13 | NamInformationNumber13 | — |
| NAM_INFORMATION_NUMBER14 | NamInformationNumber14 | — |
| NAM_INFORMATION_NUMBER15 | NamInformationNumber15 | — |
| NAM_INFORMATION_NUMBER16 | NamInformationNumber16 | — |
| NAM_INFORMATION_NUMBER17 | NamInformationNumber17 | — |
| NAM_INFORMATION_NUMBER18 | NamInformationNumber18 | — |
| NAM_INFORMATION_NUMBER19 | NamInformationNumber19 | — |
| NAM_INFORMATION_NUMBER2 | NamInformationNumber2 | — |
| NAM_INFORMATION_NUMBER20 | NamInformationNumber20 | — |
| NAM_INFORMATION_NUMBER3 | NamInformationNumber3 | — |
| NAM_INFORMATION_NUMBER4 | NamInformationNumber4 | — |
| NAM_INFORMATION_NUMBER5 | NamInformationNumber5 | — |
| NAM_INFORMATION_NUMBER6 | NamInformationNumber6 | — |
| NAM_INFORMATION_NUMBER7 | NamInformationNumber7 | — |
| NAM_INFORMATION_NUMBER8 | NamInformationNumber8 | — |
| NAM_INFORMATION_NUMBER9 | NamInformationNumber9 | — |
| NAME_TYPE | NameType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORDER_NAME | OrderName | ✅ |
| PERSON_ID | PersonId | ✅ |
| PERSON_NAME_ID | PersonNameId | ✅ |
| PRE_NAME_ADJUNCT | PreNameAdjunct | ✅ |
| PREVIOUS_LAST_NAME | PreviousLastName | ✅ |
| SUFFIX | Suffix | ✅ |
| TITLE | Title | ✅ |

### [[pscinspectionpvo|PSCInspectionPVO]] (OTHER · BICC: 1/160)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PersonProfileDPEOAttribute1 | — |
| ATTRIBUTE10 | PersonProfileDPEOAttribute10 | — |
| ATTRIBUTE11 | PersonProfileDPEOAttribute11 | — |
| ATTRIBUTE12 | PersonProfileDPEOAttribute12 | — |
| ATTRIBUTE13 | PersonProfileDPEOAttribute13 | — |
| ATTRIBUTE14 | PersonProfileDPEOAttribute14 | — |
| ATTRIBUTE15 | PersonProfileDPEOAttribute15 | — |
| ATTRIBUTE16 | PersonProfileDPEOAttribute16 | — |
| ATTRIBUTE17 | PersonProfileDPEOAttribute17 | — |
| ATTRIBUTE18 | PersonProfileDPEOAttribute18 | — |
| ATTRIBUTE19 | PersonProfileDPEOAttribute19 | — |
| ATTRIBUTE2 | PersonProfileDPEOAttribute2 | — |
| ATTRIBUTE20 | PersonProfileDPEOAttribute20 | — |
| ATTRIBUTE21 | PersonProfileDPEOAttribute21 | — |
| ATTRIBUTE22 | PersonProfileDPEOAttribute22 | — |
| ATTRIBUTE23 | PersonProfileDPEOAttribute23 | — |
| ATTRIBUTE24 | PersonProfileDPEOAttribute24 | — |
| ATTRIBUTE25 | PersonProfileDPEOAttribute25 | — |
| ATTRIBUTE26 | PersonProfileDPEOAttribute26 | — |
| ATTRIBUTE27 | PersonProfileDPEOAttribute27 | — |
| ATTRIBUTE28 | PersonProfileDPEOAttribute28 | — |
| ATTRIBUTE29 | PersonProfileDPEOAttribute29 | — |
| ATTRIBUTE3 | PersonProfileDPEOAttribute3 | — |
| ATTRIBUTE30 | PersonProfileDPEOAttribute30 | — |
| ATTRIBUTE4 | PersonProfileDPEOAttribute4 | — |
| ATTRIBUTE5 | PersonProfileDPEOAttribute5 | — |
| ATTRIBUTE6 | PersonProfileDPEOAttribute6 | — |
| ATTRIBUTE7 | PersonProfileDPEOAttribute7 | — |
| ATTRIBUTE8 | PersonProfileDPEOAttribute8 | — |
| ATTRIBUTE9 | PersonProfileDPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PersonProfileDPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PersonProfileDPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PersonProfileDPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PersonProfileDPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PersonProfileDPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PersonProfileDPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PersonProfileDPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PersonProfileDPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PersonProfileDPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PersonProfileDPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PersonProfileDPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PersonProfileDPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PersonProfileDPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PersonProfileDPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PersonProfileDPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PersonProfileDPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PersonProfileDPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PersonProfileDPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PersonProfileDPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PersonProfileDPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PersonProfileDPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PersonProfileDPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PersonProfileDPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PersonProfileDPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PersonProfileDPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PersonProfileDPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PersonProfileDPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PersonProfileDPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PersonProfileDPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PersonProfileDPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PersonProfileDPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PersonProfileDPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PersonProfileDPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PersonProfileDPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PersonProfileDPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PersonProfileDPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | PersonProfileDPEOBusinessGroupId | — |
| CHAR_SET_CONTEXT | PersonProfileDPEOCharSetContext | — |
| CREATED_BY | PersonProfileDPEOCreatedBy | — |
| CREATION_DATE | PersonProfileDPEOCreationDate | — |
| DISPLAY_NAME | PersonProfileDPEODisplayName | ✅ |
| EFFECTIVE_END_DATE | PersonProfileDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonProfileDPEOEffectiveStartDate | — |
| FIRST_NAME | PersonProfileDPEOFirstName | — |
| FULL_NAME | PersonProfileDPEOFullName | — |
| HONORS | PersonProfileDPEOHonors | — |
| KNOWN_AS | PersonProfileDPEOKnownAs | — |
| LAST_NAME | PersonProfileDPEOLastName | — |
| LAST_UPDATE_DATE | PersonProfileDPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PersonProfileDPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonProfileDPEOLastUpdatedBy | — |
| LEGISLATION_CODE | PersonProfileDPEOLegislationCode | — |
| LIST_NAME | PersonProfileDPEOListName | — |
| MIDDLE_NAMES | PersonProfileDPEOMiddleNames | — |
| MILITARY_RANK | PersonProfileDPEOMilitaryRank | — |
| NAM_INFORMATION1 | PersonProfileDPEONamInformation1 | — |
| NAM_INFORMATION10 | PersonProfileDPEONamInformation10 | — |
| NAM_INFORMATION11 | PersonProfileDPEONamInformation11 | — |
| NAM_INFORMATION12 | PersonProfileDPEONamInformation12 | — |
| NAM_INFORMATION13 | PersonProfileDPEONamInformation13 | — |
| NAM_INFORMATION14 | PersonProfileDPEONamInformation14 | — |
| NAM_INFORMATION15 | PersonProfileDPEONamInformation15 | — |
| NAM_INFORMATION16 | PersonProfileDPEONamInformation16 | — |
| NAM_INFORMATION17 | PersonProfileDPEONamInformation17 | — |
| NAM_INFORMATION18 | PersonProfileDPEONamInformation18 | — |
| NAM_INFORMATION19 | PersonProfileDPEONamInformation19 | — |
| NAM_INFORMATION2 | PersonProfileDPEONamInformation2 | — |
| NAM_INFORMATION20 | PersonProfileDPEONamInformation20 | — |
| NAM_INFORMATION21 | PersonProfileDPEONamInformation21 | — |
| NAM_INFORMATION22 | PersonProfileDPEONamInformation22 | — |
| NAM_INFORMATION23 | PersonProfileDPEONamInformation23 | — |
| NAM_INFORMATION24 | PersonProfileDPEONamInformation24 | — |
| NAM_INFORMATION25 | PersonProfileDPEONamInformation25 | — |
| NAM_INFORMATION26 | PersonProfileDPEONamInformation26 | — |
| NAM_INFORMATION27 | PersonProfileDPEONamInformation27 | — |
| NAM_INFORMATION28 | PersonProfileDPEONamInformation28 | — |
| NAM_INFORMATION29 | PersonProfileDPEONamInformation29 | — |
| NAM_INFORMATION3 | PersonProfileDPEONamInformation3 | — |
| NAM_INFORMATION30 | PersonProfileDPEONamInformation30 | — |
| NAM_INFORMATION4 | PersonProfileDPEONamInformation4 | — |
| NAM_INFORMATION5 | PersonProfileDPEONamInformation5 | — |
| NAM_INFORMATION6 | PersonProfileDPEONamInformation6 | — |
| NAM_INFORMATION7 | PersonProfileDPEONamInformation7 | — |
| NAM_INFORMATION8 | PersonProfileDPEONamInformation8 | — |
| NAM_INFORMATION9 | PersonProfileDPEONamInformation9 | — |
| NAM_INFORMATION_CATEGORY | PersonProfileDPEONamInformationCategory | — |
| NAM_INFORMATION_DATE1 | PersonProfileDPEONamInformationDate1 | — |
| NAM_INFORMATION_DATE10 | PersonProfileDPEONamInformationDate10 | — |
| NAM_INFORMATION_DATE11 | PersonProfileDPEONamInformationDate11 | — |
| NAM_INFORMATION_DATE12 | PersonProfileDPEONamInformationDate12 | — |
| NAM_INFORMATION_DATE13 | PersonProfileDPEONamInformationDate13 | — |
| NAM_INFORMATION_DATE14 | PersonProfileDPEONamInformationDate14 | — |
| NAM_INFORMATION_DATE15 | PersonProfileDPEONamInformationDate15 | — |
| NAM_INFORMATION_DATE2 | PersonProfileDPEONamInformationDate2 | — |
| NAM_INFORMATION_DATE3 | PersonProfileDPEONamInformationDate3 | — |
| NAM_INFORMATION_DATE4 | PersonProfileDPEONamInformationDate4 | — |
| NAM_INFORMATION_DATE5 | PersonProfileDPEONamInformationDate5 | — |
| NAM_INFORMATION_DATE6 | PersonProfileDPEONamInformationDate6 | — |
| NAM_INFORMATION_DATE7 | PersonProfileDPEONamInformationDate7 | — |
| NAM_INFORMATION_DATE8 | PersonProfileDPEONamInformationDate8 | — |
| NAM_INFORMATION_DATE9 | PersonProfileDPEONamInformationDate9 | — |
| NAM_INFORMATION_NUMBER1 | PersonProfileDPEONamInformationNumber1 | — |
| NAM_INFORMATION_NUMBER10 | PersonProfileDPEONamInformationNumber10 | — |
| NAM_INFORMATION_NUMBER11 | PersonProfileDPEONamInformationNumber11 | — |
| NAM_INFORMATION_NUMBER12 | PersonProfileDPEONamInformationNumber12 | — |
| NAM_INFORMATION_NUMBER13 | PersonProfileDPEONamInformationNumber13 | — |
| NAM_INFORMATION_NUMBER14 | PersonProfileDPEONamInformationNumber14 | — |
| NAM_INFORMATION_NUMBER15 | PersonProfileDPEONamInformationNumber15 | — |
| NAM_INFORMATION_NUMBER16 | PersonProfileDPEONamInformationNumber16 | — |
| NAM_INFORMATION_NUMBER17 | PersonProfileDPEONamInformationNumber17 | — |
| NAM_INFORMATION_NUMBER18 | PersonProfileDPEONamInformationNumber18 | — |
| NAM_INFORMATION_NUMBER19 | PersonProfileDPEONamInformationNumber19 | — |
| NAM_INFORMATION_NUMBER2 | PersonProfileDPEONamInformationNumber2 | — |
| NAM_INFORMATION_NUMBER20 | PersonProfileDPEONamInformationNumber20 | — |
| NAM_INFORMATION_NUMBER3 | PersonProfileDPEONamInformationNumber3 | — |
| NAM_INFORMATION_NUMBER4 | PersonProfileDPEONamInformationNumber4 | — |
| NAM_INFORMATION_NUMBER5 | PersonProfileDPEONamInformationNumber5 | — |
| NAM_INFORMATION_NUMBER6 | PersonProfileDPEONamInformationNumber6 | — |
| NAM_INFORMATION_NUMBER7 | PersonProfileDPEONamInformationNumber7 | — |
| NAM_INFORMATION_NUMBER8 | PersonProfileDPEONamInformationNumber8 | — |
| NAM_INFORMATION_NUMBER9 | PersonProfileDPEONamInformationNumber9 | — |
| NAME_TYPE | PersonProfileDPEONameType | — |
| OBJECT_VERSION_NUMBER | PersonProfileDPEOObjectVersionNumber | — |
| ORDER_NAME | PersonProfileDPEOOrderName | — |
| PERSON_ID | PersonProfileDPEOPersonId | — |
| PERSON_NAME_ID | PersonProfileDPEOPersonNameId | — |
| PRE_NAME_ADJUNCT | PersonProfileDPEOPreNameAdjunct | — |
| PREVIOUS_LAST_NAME | PersonProfileDPEOPreviousLastName | — |
| SUFFIX | PersonProfileDPEOSuffix | — |
| TITLE | PersonProfileDPEOTitle | — |

### [[pscplanreviewerspvo|PSCPlanReviewersPVO]] (OTHER · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DISPLAY_NAME | PersonProfileDPEODisplayName | ✅ |
| EFFECTIVE_END_DATE | PersonProfileDPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PersonProfileDPEOEffectiveStartDate | — |
| PERSON_NAME_ID | PersonProfileDPEOPersonNameId | — |
