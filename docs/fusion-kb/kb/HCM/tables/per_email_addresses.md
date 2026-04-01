---
id: DOC-HCM-656
doc_type: system-doc
title: "PER_EMAIL_ADDRESSES — Endereços de E-mail"
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
  - emails
  - email-addresses
aliases:
  - PER_EMAIL_ADDRESSES
  - per_email_addresses
  - per-email-addresses
  - endereços-de-e-mail
  - per-email-addresses
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_EMAIL_ADDRESSES

## 📌 Visão Geral

Armazena os **endereços de e-mail** dos colaboradores. Suporta múltiplos endereços por pessoa (corporativo, pessoal, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comunicação** — endereços de e-mail para contato com colaboradores.
- **Self-service** — e-mail para login e notificações do sistema.
- **Integração** — sincronização com diretórios corporativos (Active Directory, etc.).
- **Relatórios** — distribuição de comunicados por e-mail.
- **Onboarding** — provisionamento de e-mail corporativo.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EMAIL_ADDRESS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do e-mail | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa associada | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EMAIL_ADDRESS | VARCHAR2(240) | NOT NULL | Dados | Endereço de e-mail | — | 🟢 95% |
| 4 | EMAIL_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo (W1=corporativo, H1=pessoal) | — | 🟢 90% |
| 5 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | E-mail primário (Y/N) | — | 🟢 90% |
| 6 | DATE_FROM | DATE | NULL | Período | Data de início de validade | — | 🟢 85% |
| 7 | DATE_TO | DATE | NULL | Período | Data de fim de validade | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular do endereço de e-mail)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### E-mail corporativo de um colaborador
```sql
SELECT pea.EMAIL_ADDRESS, pea.EMAIL_TYPE
FROM   PER_EMAIL_ADDRESSES pea
WHERE  pea.PERSON_ID = :p_person_id
  AND  pea.EMAIL_TYPE = 'W1'
  AND  pea.PRIMARY_FLAG = 'Y';
```

### Filtros comuns
- `EMAIL_TYPE = 'W1'` — E-mail corporativo
- `PRIMARY_FLAG = 'Y'` — E-mail principal
---

## 🔒 Observações

- Tipos comuns: W1 (Work/Corporativo), H1 (Home/Pessoal).
- O e-mail corporativo (W1) é tipicamente usado para login e notificações do Oracle.
- Dados pessoais — sujeitos a regras de privacidade (LGPD).
---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressBusinessGroupId | — |
| CREATED_BY | EmailAddressCreatedBy | — |
| CREATION_DATE | EmailAddressCreationDate | — |
| DATE_FROM | EmailAddressDateFrom | — |
| DATE_TO | EmailAddressDateTo | — |
| EMAIL_ADDRESS | EmailAddressEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressEmailAddressId | — |
| EMAIL_TYPE | EmailAddressEmailType | — |
| LAST_UPDATE_DATE | EmailAddressLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EmailAddressLastUpdateLogin | — |
| LAST_UPDATED_BY | EmailAddressLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EmailAddressObjectVersionNumber | — |
| PERSON_ID | EmailAddressPersonId | — |

### [[candidateemailaddressespvo|CandidateEmailAddressesPVO]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | ✅ |

### [[candidateinteractionpvo|CandidateInteractionPVO]] (HCM · BICC: 2/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute310 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute410 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId4 | — |

### [[candidatepoolinteractionpvo|CandidatePoolInteractionPVO]] (HCM · BICC: 2/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute310 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute410 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId4 | — |

### [[contactemailaddressespvo|ContactEmailAddressesPVO]] (HCM · BICC: 11/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressesPEOBusinessGroupId | — |
| CREATED_BY | EmailAddressesPEOCreatedBy | ✅ |
| CREATION_DATE | EmailAddressesPEOCreationDate | ✅ |
| DATE_FROM | EmailAddressesPEODateFrom | ✅ |
| DATE_TO | EmailAddressesPEODateTo | ✅ |
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | ✅ |
| EMAIL_TYPE | EmailAddressesPEOEmailType | ✅ |
| LAST_UPDATE_DATE | EmailAddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EmailAddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EmailAddressesPEOLastUpdatedBy | ✅ |
| MASTERED_IN_LDAP_FLAG | EmailAddressesPEOMasteredInLdapFlag | ✅ |
| OBJECT_VERSION_NUMBER | EmailAddressesPEOObjectVersionNumber | — |
| PERSON_ID | EmailAddressesPEOPersonId | ✅ |

### [[emailaddressespvo|EmailAddressesPVO]] (HCM · BICC: 11/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressesPEOBusinessGroupId | — |
| CREATED_BY | EmailAddressesPEOCreatedBy | ✅ |
| CREATION_DATE | EmailAddressesPEOCreationDate | ✅ |
| DATE_FROM | EmailAddressesPEODateFrom | ✅ |
| DATE_TO | EmailAddressesPEODateTo | ✅ |
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | ✅ |
| EMAIL_TYPE | EmailAddressesPEOEmailType | ✅ |
| LAST_UPDATE_DATE | EmailAddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EmailAddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EmailAddressesPEOLastUpdatedBy | ✅ |
| MASTERED_IN_LDAP_FLAG | EmailAddressesPEOMasteredInLdapFlag | ✅ |
| OBJECT_VERSION_NUMBER | EmailAddressesPEOObjectVersionNumber | — |
| PERSON_ID | EmailAddressesPEOPersonId | ✅ |

### [[emailaddressespvoviewall|EmailAddressesPVOViewAll]] (HCM · BICC: 11/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressesPEOBusinessGroupId | — |
| CREATED_BY | EmailAddressesPEOCreatedBy | ✅ |
| CREATION_DATE | EmailAddressesPEOCreationDate | ✅ |
| DATE_FROM | EmailAddressesPEODateFrom | ✅ |
| DATE_TO | EmailAddressesPEODateTo | ✅ |
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | ✅ |
| EMAIL_TYPE | EmailAddressesPEOEmailType | ✅ |
| LAST_UPDATE_DATE | EmailAddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EmailAddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EmailAddressesPEOLastUpdatedBy | ✅ |
| MASTERED_IN_LDAP_FLAG | EmailAddressesPEOMasteredInLdapFlag | ✅ |
| OBJECT_VERSION_NUMBER | EmailAddressesPEOObjectVersionNumber | — |
| PERSON_ID | EmailAddressesPEOPersonId | ✅ |

### [[endorsementspvo|EndorsementsPVO]] (PO · BICC: 3/160)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE1 | Attribute120 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE10 | Attribute106 | — |
| ATTRIBUTE11 | Attribute1110 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE12 | Attribute126 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE13 | Attribute136 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE14 | Attribute146 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE15 | Attribute156 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE16 | Attribute166 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE17 | Attribute176 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE18 | Attribute186 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE19 | Attribute196 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE2 | Attribute220 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE20 | Attribute206 | — |
| ATTRIBUTE21 | Attribute2110 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE22 | Attribute226 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE23 | Attribute236 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE24 | Attribute246 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE25 | Attribute256 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE26 | Attribute266 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE27 | Attribute276 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE28 | Attribute286 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE29 | Attribute296 | — |
| ATTRIBUTE3 | Attribute312 | — |
| ATTRIBUTE3 | Attribute316 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE30 | Attribute306 | — |
| ATTRIBUTE4 | Attribute412 | — |
| ATTRIBUTE4 | Attribute416 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE5 | Attribute56 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE6 | Attribute66 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE7 | Attribute76 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE8 | Attribute86 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE9 | Attribute96 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory6 | — |
| ATTRIBUTE_DATE1 | AttributeDate116 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE10 | AttributeDate106 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE11 | AttributeDate117 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE12 | AttributeDate126 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE13 | AttributeDate136 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE14 | AttributeDate146 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE15 | AttributeDate156 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE2 | AttributeDate26 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE3 | AttributeDate36 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE4 | AttributeDate46 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE5 | AttributeDate56 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE6 | AttributeDate66 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE7 | AttributeDate76 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE8 | AttributeDate86 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_DATE9 | AttributeDate96 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber120 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber106 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber1110 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber126 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber136 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber146 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber156 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber166 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber176 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber186 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber196 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber26 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber206 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber36 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber46 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber56 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber66 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber76 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber86 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber96 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| BUSINESS_GROUP_ID | BusinessGroupId6 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATED_BY | CreatedBy7 | — |
| CREATION_DATE | CreationDate4 | — |
| CREATION_DATE | CreationDate7 | — |
| DATE_FROM | DateFrom | — |
| DATE_FROM | DateFrom1 | — |
| DATE_TO | DateTo | — |
| DATE_TO | DateTo1 | — |
| EMAIL_ADDRESS | EmailAddress | — |
| EMAIL_ADDRESS | EmailAddress1 | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_ADDRESS_ID | EmailAddressId1 | — |
| EMAIL_TYPE | EmailType | — |
| EMAIL_TYPE | EmailType1 | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate7 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin7 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| LAST_UPDATED_BY | LastUpdatedBy7 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber7 | — |
| PERSON_ID | PersonId3 | — |
| PERSON_ID | PersonId6 | — |

### [[expensereporthistorypvo|ExpenseReportHistoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | PerformerPersonEmailEmailAddress | — |
| EMAIL_ADDRESS_ID | PerformerPersonEmailEmailAddressId | — |

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 6/160)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute118 | — |
| ATTRIBUTE1 | Attribute127 | — |
| ATTRIBUTE10 | Attribute105 | — |
| ATTRIBUTE10 | Attribute107 | — |
| ATTRIBUTE11 | Attribute1111 | — |
| ATTRIBUTE11 | Attribute119 | — |
| ATTRIBUTE12 | Attribute125 | — |
| ATTRIBUTE12 | Attribute128 | — |
| ATTRIBUTE13 | Attribute135 | — |
| ATTRIBUTE13 | Attribute137 | — |
| ATTRIBUTE14 | Attribute145 | — |
| ATTRIBUTE14 | Attribute147 | — |
| ATTRIBUTE15 | Attribute155 | — |
| ATTRIBUTE15 | Attribute157 | — |
| ATTRIBUTE16 | Attribute165 | — |
| ATTRIBUTE16 | Attribute167 | — |
| ATTRIBUTE17 | Attribute175 | — |
| ATTRIBUTE17 | Attribute177 | — |
| ATTRIBUTE18 | Attribute185 | — |
| ATTRIBUTE18 | Attribute187 | — |
| ATTRIBUTE19 | Attribute195 | — |
| ATTRIBUTE19 | Attribute197 | — |
| ATTRIBUTE2 | Attribute218 | — |
| ATTRIBUTE2 | Attribute227 | — |
| ATTRIBUTE20 | Attribute205 | — |
| ATTRIBUTE20 | Attribute207 | — |
| ATTRIBUTE21 | Attribute2111 | — |
| ATTRIBUTE21 | Attribute219 | — |
| ATTRIBUTE22 | Attribute225 | — |
| ATTRIBUTE22 | Attribute228 | — |
| ATTRIBUTE23 | Attribute235 | — |
| ATTRIBUTE23 | Attribute237 | — |
| ATTRIBUTE24 | Attribute245 | — |
| ATTRIBUTE24 | Attribute247 | — |
| ATTRIBUTE25 | Attribute255 | — |
| ATTRIBUTE25 | Attribute257 | — |
| ATTRIBUTE26 | Attribute265 | — |
| ATTRIBUTE26 | Attribute267 | — |
| ATTRIBUTE27 | Attribute275 | — |
| ATTRIBUTE27 | Attribute277 | — |
| ATTRIBUTE28 | Attribute285 | — |
| ATTRIBUTE28 | Attribute287 | — |
| ATTRIBUTE29 | Attribute295 | — |
| ATTRIBUTE29 | Attribute297 | — |
| ATTRIBUTE3 | Attribute310 | — |
| ATTRIBUTE3 | Attribute314 | — |
| ATTRIBUTE30 | Attribute305 | — |
| ATTRIBUTE30 | Attribute307 | — |
| ATTRIBUTE4 | Attribute410 | — |
| ATTRIBUTE4 | Attribute414 | — |
| ATTRIBUTE5 | Attribute55 | — |
| ATTRIBUTE5 | Attribute57 | — |
| ATTRIBUTE6 | Attribute65 | — |
| ATTRIBUTE6 | Attribute67 | — |
| ATTRIBUTE7 | Attribute75 | — |
| ATTRIBUTE7 | Attribute77 | — |
| ATTRIBUTE8 | Attribute85 | — |
| ATTRIBUTE8 | Attribute87 | — |
| ATTRIBUTE9 | Attribute95 | — |
| ATTRIBUTE9 | Attribute97 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory5 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory7 | — |
| ATTRIBUTE_DATE1 | AttributeDate110 | — |
| ATTRIBUTE_DATE1 | AttributeDate118 | — |
| ATTRIBUTE_DATE10 | AttributeDate105 | — |
| ATTRIBUTE_DATE10 | AttributeDate107 | — |
| ATTRIBUTE_DATE11 | AttributeDate115 | — |
| ATTRIBUTE_DATE11 | AttributeDate119 | — |
| ATTRIBUTE_DATE12 | AttributeDate125 | — |
| ATTRIBUTE_DATE12 | AttributeDate127 | — |
| ATTRIBUTE_DATE13 | AttributeDate135 | — |
| ATTRIBUTE_DATE13 | AttributeDate137 | — |
| ATTRIBUTE_DATE14 | AttributeDate145 | — |
| ATTRIBUTE_DATE14 | AttributeDate147 | — |
| ATTRIBUTE_DATE15 | AttributeDate155 | — |
| ATTRIBUTE_DATE15 | AttributeDate157 | — |
| ATTRIBUTE_DATE2 | AttributeDate25 | — |
| ATTRIBUTE_DATE2 | AttributeDate27 | — |
| ATTRIBUTE_DATE3 | AttributeDate35 | — |
| ATTRIBUTE_DATE3 | AttributeDate37 | — |
| ATTRIBUTE_DATE4 | AttributeDate45 | — |
| ATTRIBUTE_DATE4 | AttributeDate47 | — |
| ATTRIBUTE_DATE5 | AttributeDate55 | — |
| ATTRIBUTE_DATE5 | AttributeDate57 | — |
| ATTRIBUTE_DATE6 | AttributeDate65 | — |
| ATTRIBUTE_DATE6 | AttributeDate67 | — |
| ATTRIBUTE_DATE7 | AttributeDate75 | — |
| ATTRIBUTE_DATE7 | AttributeDate77 | — |
| ATTRIBUTE_DATE8 | AttributeDate85 | — |
| ATTRIBUTE_DATE8 | AttributeDate87 | — |
| ATTRIBUTE_DATE9 | AttributeDate95 | — |
| ATTRIBUTE_DATE9 | AttributeDate97 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber118 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber127 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber105 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber107 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber1111 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber119 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber125 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber128 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber135 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber137 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber145 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber147 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber155 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber157 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber165 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber167 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber175 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber177 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber185 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber187 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber195 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber197 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber25 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber27 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber205 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber207 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber35 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber37 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber45 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber47 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber55 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber57 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber65 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber67 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber75 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber77 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber85 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber87 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber95 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber97 | — |
| BUSINESS_GROUP_ID | BusinessGroupId7 | — |
| BUSINESS_GROUP_ID | BusinessGroupId9 | — |
| CREATED_BY | CreatedBy11 | — |
| CREATED_BY | CreatedBy13 | — |
| CREATION_DATE | CreationDate11 | — |
| CREATION_DATE | CreationDate13 | — |
| DATE_FROM | DateFrom | ✅ |
| DATE_FROM | DateFrom1 | — |
| DATE_TO | DateTo | ✅ |
| DATE_TO | DateTo1 | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS | EmailAddress1 | — |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_ADDRESS_ID | EmailAddressId1 | — |
| EMAIL_TYPE | EmailType | ✅ |
| EMAIL_TYPE | EmailType1 | — |
| LAST_UPDATE_DATE | LastUpdateDate11 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate13 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin11 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin13 | — |
| LAST_UPDATED_BY | LastUpdatedBy11 | — |
| LAST_UPDATED_BY | LastUpdatedBy13 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber10 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber12 | — |
| PERSON_ID | PersonId6 | — |
| PERSON_ID | PersonId8 | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 17/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressesPEOBusinessGroupId | ✅ |
| CREATED_BY | EmailAddressesPEOCreatedBy | ✅ |
| CREATION_DATE | EmailAddressesPEOCreationDate | ✅ |
| DATE_FROM | EmailAddressesPEODateFrom | ✅ |
| DATE_TO | EmailAddressesPEODateTo | ✅ |
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS | SupervisorEmailAddressPEOEmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressesPEOEmailAddressId | ✅ |
| EMAIL_ADDRESS_ID | SupervisorEmailAddressPEOEmailAddressId | ✅ |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOEmailAddressId | — |
| EMAIL_TYPE | EmailAddressesPEOEmailType | ✅ |
| EMAIL_TYPE | WorkEmailAddressesPEOEmailType | — |
| LAST_UPDATE_DATE | EmailAddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | SupervisorEmailAddressPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WorkEmailAddressesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | EmailAddressesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | EmailAddressesPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | EmailAddressesPEOObjectVersionNumber | ✅ |
| PERSON_ID | EmailAddressesPEOPersonId | ✅ |
| PERSON_ID | WorkEmailAddressesPEOPersonId | — |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 6/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressesPEOBusinessGroupId | — |
| CREATED_BY | EmailAddressesPEOCreatedBy | — |
| CREATION_DATE | EmailAddressesPEOCreationDate | — |
| DATE_FROM | EmailAddressesPEODateFrom | — |
| DATE_TO | EmailAddressesPEODateTo | — |
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS | SupervisorEmailAddressPEOEmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressesPEOEmailAddressId | — |
| EMAIL_ADDRESS_ID | SupervisorEmailAddressPEOEmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOEmailAddressId | — |
| EMAIL_TYPE | EmailAddressesPEOEmailType | ✅ |
| EMAIL_TYPE | WorkEmailAddressesPEOEmailType | — |
| LAST_UPDATE_DATE | EmailAddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | SupervisorEmailAddressPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | WorkEmailAddressesPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | EmailAddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EmailAddressesPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EmailAddressesPEOObjectVersionNumber | — |
| PERSON_ID | EmailAddressesPEOPersonId | — |
| PERSON_ID | WorkEmailAddressesPEOPersonId | — |

### [[hitspvo|HitsPVO]] (PO · BICC: 2/160)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE1 | Attribute120 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE10 | Attribute106 | — |
| ATTRIBUTE11 | Attribute1110 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE12 | Attribute126 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE13 | Attribute136 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE14 | Attribute146 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE15 | Attribute156 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE16 | Attribute166 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE17 | Attribute176 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE18 | Attribute186 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE19 | Attribute196 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE2 | Attribute220 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE20 | Attribute206 | — |
| ATTRIBUTE21 | Attribute2110 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE22 | Attribute226 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE23 | Attribute236 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE24 | Attribute246 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE25 | Attribute256 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE26 | Attribute266 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE27 | Attribute276 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE28 | Attribute286 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE29 | Attribute296 | — |
| ATTRIBUTE3 | Attribute312 | — |
| ATTRIBUTE3 | Attribute316 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE30 | Attribute306 | — |
| ATTRIBUTE4 | Attribute412 | — |
| ATTRIBUTE4 | Attribute416 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE5 | Attribute56 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE6 | Attribute66 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE7 | Attribute76 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE8 | Attribute86 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE9 | Attribute96 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory6 | — |
| ATTRIBUTE_DATE1 | AttributeDate116 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE10 | AttributeDate106 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE11 | AttributeDate117 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE12 | AttributeDate126 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE13 | AttributeDate136 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE14 | AttributeDate146 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE15 | AttributeDate156 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE2 | AttributeDate26 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE3 | AttributeDate36 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE4 | AttributeDate46 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE5 | AttributeDate56 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE6 | AttributeDate66 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE7 | AttributeDate76 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE8 | AttributeDate86 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_DATE9 | AttributeDate96 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber120 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber106 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber1110 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber126 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber136 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber146 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber156 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber166 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber176 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber186 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber196 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber26 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber206 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber36 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber46 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber56 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber66 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber76 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber86 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber96 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| BUSINESS_GROUP_ID | BusinessGroupId6 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATED_BY | CreatedBy7 | — |
| CREATION_DATE | CreationDate4 | — |
| CREATION_DATE | CreationDate7 | — |
| DATE_FROM | DateFrom | — |
| DATE_FROM | DateFrom1 | — |
| DATE_TO | DateTo | — |
| DATE_TO | DateTo1 | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS | EmailAddress1 | — |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_ADDRESS_ID | EmailAddressId1 | — |
| EMAIL_TYPE | EmailType | — |
| EMAIL_TYPE | EmailType1 | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate7 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin7 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| LAST_UPDATED_BY | LastUpdatedBy7 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber7 | — |
| PERSON_ID | PersonId3 | — |
| PERSON_ID | PersonId6 | — |

### [[institutioncontactspvo|InstitutionContactsPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | EmailAddressPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressPEOEmailAddressId | — |
| OBJECT_VERSION_NUMBER | EmailAddressPEOObjectVersionNumber | — |

### [[jobapplicationinteractionpvo|JobApplicationInteractionPVO]] (HCM · BICC: 4/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute310 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute410 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId4 | — |

### [[managerhrchybottomuppvolinemanager|ManagerHrchyBottomUpPVOLineManager]] (HCM · BICC: 15/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | WorkEmailAddressesPEOL10EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL11EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL12EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL13EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL14EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL15EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL16EmailAddress | — |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL17EmailAddress | — |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL18EmailAddress | — |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL19EmailAddress | — |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL1EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL20EmailAddress | — |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL2EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL3EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL4EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL5EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL6EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL7EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL8EmailAddress | ✅ |
| EMAIL_ADDRESS | WorkEmailAddressesPEOL9EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL10EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL11EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL12EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL13EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL14EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL15EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL16EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL17EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL18EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL19EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL1EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL20EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL2EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL3EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL4EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL5EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL6EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL7EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL8EmailAddressId | — |
| EMAIL_ADDRESS_ID | WorkEmailAddressesPEOL9EmailAddressId | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL10EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL11EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL12EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL13EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL14EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL15EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL16EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL17EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL18EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL19EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL1EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL20EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL2EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL3EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL4EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL5EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL6EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL7EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL8EmailType | — |
| EMAIL_TYPE | WorkEmailAddressesPEOL9EmailType | — |
| PERSON_ID | WorkEmailAddressesPEOL10PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL11PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL12PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL13PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL14PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL15PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL16PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL17PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL18PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL19PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL1PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL20PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL2PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL3PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL4PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL5PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL6PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL7PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL8PersonId | — |
| PERSON_ID | WorkEmailAddressesPEOL9PersonId | — |

### [[offerpvo|OfferPVO]] (HCM · BICC: 2/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute312 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute412 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId4 | — |

### [[personemailpvo|PersonEmailPVO]] (HCM · BICC: 3/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EmailAddressesPEOBusinessGroupId | — |
| CREATED_BY | EmailAddressesPEOCreatedBy | — |
| CREATION_DATE | EmailAddressesPEOCreationDate | — |
| DATE_FROM | EmailAddressesPEODateFrom | — |
| DATE_TO | EmailAddressesPEODateTo | — |
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | ✅ |
| EMAIL_TYPE | EmailAddressesPEOEmailType | — |
| LAST_UPDATE_DATE | EmailAddressesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EmailAddressesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EmailAddressesPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EmailAddressesPEOObjectVersionNumber | — |
| PERSON_ID | EmailAddressesPEOPersonId | — |

### [[personrefpvo|PersonRefPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | EmailAddressesPEOEmailAddress | — |
| EMAIL_ADDRESS_ID | EmailAddressesPEOEmailAddressId | — |

### [[prospectinteractionpvo|ProspectInteractionPVO]] (HCM · BICC: 2/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute310 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute410 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId4 | — |

### [[prospectspvo|ProspectsPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | EmailAddrPEOAddedByEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddrPEOEmailAddressId | ✅ |

### [[prospectsviewallpvo|ProspectsViewAllPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | EmailAddrPEOAddedByEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddrPEOEmailAddressId | — |

### [[referralspvo|ReferralsPVO]] (PO · BICC: 2/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute312 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute412 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId3 | — |

### [[sharespvo|SharesPVO]] (PO · BICC: 2/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute114 | — |
| ATTRIBUTE10 | Attribute103 | — |
| ATTRIBUTE11 | Attribute115 | — |
| ATTRIBUTE12 | Attribute123 | — |
| ATTRIBUTE13 | Attribute133 | — |
| ATTRIBUTE14 | Attribute143 | — |
| ATTRIBUTE15 | Attribute153 | — |
| ATTRIBUTE16 | Attribute163 | — |
| ATTRIBUTE17 | Attribute173 | — |
| ATTRIBUTE18 | Attribute183 | — |
| ATTRIBUTE19 | Attribute193 | — |
| ATTRIBUTE2 | Attribute214 | — |
| ATTRIBUTE20 | Attribute203 | — |
| ATTRIBUTE21 | Attribute215 | — |
| ATTRIBUTE22 | Attribute223 | — |
| ATTRIBUTE23 | Attribute233 | — |
| ATTRIBUTE24 | Attribute243 | — |
| ATTRIBUTE25 | Attribute253 | — |
| ATTRIBUTE26 | Attribute263 | — |
| ATTRIBUTE27 | Attribute273 | — |
| ATTRIBUTE28 | Attribute283 | — |
| ATTRIBUTE29 | Attribute293 | — |
| ATTRIBUTE3 | Attribute312 | — |
| ATTRIBUTE30 | Attribute303 | — |
| ATTRIBUTE4 | Attribute412 | — |
| ATTRIBUTE5 | Attribute53 | — |
| ATTRIBUTE6 | Attribute63 | — |
| ATTRIBUTE7 | Attribute73 | — |
| ATTRIBUTE8 | Attribute83 | — |
| ATTRIBUTE9 | Attribute93 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory3 | — |
| ATTRIBUTE_DATE1 | AttributeDate18 | — |
| ATTRIBUTE_DATE10 | AttributeDate103 | — |
| ATTRIBUTE_DATE11 | AttributeDate113 | — |
| ATTRIBUTE_DATE12 | AttributeDate123 | — |
| ATTRIBUTE_DATE13 | AttributeDate133 | — |
| ATTRIBUTE_DATE14 | AttributeDate143 | — |
| ATTRIBUTE_DATE15 | AttributeDate153 | — |
| ATTRIBUTE_DATE2 | AttributeDate23 | — |
| ATTRIBUTE_DATE3 | AttributeDate33 | — |
| ATTRIBUTE_DATE4 | AttributeDate43 | — |
| ATTRIBUTE_DATE5 | AttributeDate53 | — |
| ATTRIBUTE_DATE6 | AttributeDate63 | — |
| ATTRIBUTE_DATE7 | AttributeDate73 | — |
| ATTRIBUTE_DATE8 | AttributeDate83 | — |
| ATTRIBUTE_DATE9 | AttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber103 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber115 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber123 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber133 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber143 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber153 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber163 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber173 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber183 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber193 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber23 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber203 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber33 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber43 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber53 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber63 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber73 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber83 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber93 | — |
| BUSINESS_GROUP_ID | BusinessGroupId3 | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| EMAIL_ADDRESS | EmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressId | — |
| EMAIL_TYPE | EmailType | — |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| MASTERED_IN_LDAP_FLAG | MasteredInLdapFlag | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| PERSON_ID | PersonId3 | — |

### [[surveyresultspvo|SurveyResultsPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EMAIL_ADDRESS | EmailAddressPEOEmailAddress | ✅ |
| EMAIL_ADDRESS_ID | EmailAddressPEOEmailAddressId | — |
| EMAIL_TYPE | EmailAddressPEOEmailType | — |

---

## 📚 Referências

- [Oracle Docs — PER_EMAIL_ADDRESSES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peremailaddresses.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
