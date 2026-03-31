---
id: DOC-HCM-689
doc_type: system-doc
title: "PER_PERSON_ADDR_USAGES_F — Usos de Endereço de Pessoa"
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
  - endereco-pessoa
  - address-usage
  - residencia
  - correspondencia
aliases:
  - PER_PERSON_ADDR_USAGES_F
  - per_person_addr_usages_f
  - uso-endereco-pessoa
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_ADDR_USAGES_F

## Visão Geral

Armazena os **usos de endereço** das pessoas no sistema, definindo a finalidade de cada endereço (residência, correspondência, fiscal). Tabela date-effective que controla a vigência temporal de cada endereço.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro de endereços de colaboradores** — residência, correspondência, fiscal
- **Folha de pagamento** — endereço fiscal para cálculos tributários (IRRF, INSS)
- **Envio de correspondência** — holerites, informes de rendimento
- **eSocial** — endereço residencial obrigatório para eventos trabalhistas
- **Logística de benefícios** — entrega de cartões, uniformes, etc.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ADDR_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso de endereço | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | ADDRESS_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de uso do endereço (HOME, MAIL, TAX) | — | 🟢 85% |
| 4 | ADDRESS_ID | NUMBER(18) | NULL | FK | Referência ao endereço detalhado | PER_ADDRESSES_F | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é o endereço principal (Y/N) | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa do uso de endereço)
- [[per_addresses_f]] — via `ADDRESS_ID` (endereço utilizado pela pessoa)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Endereço residencial atual de um colaborador
```sql
SELECT pau.PERSON_ADDR_USAGE_ID, pau.ADDRESS_ID, pau.ADDRESS_TYPE
FROM   PER_PERSON_ADDR_USAGES_F pau
WHERE  pau.PERSON_ID = :p_person_id
  AND  pau.ADDRESS_TYPE = 'HOME'
  AND  SYSDATE BETWEEN pau.EFFECTIVE_START_DATE AND pau.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- Uma pessoa pode ter múltiplos usos de endereço simultâneos (residência, correspondência, fiscal).
- O endereço detalhado (rua, cidade, CEP) está na tabela referenciada via `ADDRESS_ID`.
- `ADDRESS_TYPE` = 'HOME' é geralmente obrigatório para colaboradores ativos.

---

## Referências

- [Oracle Docs — PER_PERSON_ADDR_USAGES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersonaddrusagesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[contactpersonaddresspvo|ContactPersonAddressPVO]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | PersonAddressUsagesPEOAddressId | — |
| ADDRESS_TYPE | PersonAddressUsagesPEOAddressType | ✅ |
| BUSINESS_GROUP_ID | PersonAddressUsagesPEOBusinessGroupId | — |
| CREATED_BY | PersonAddressUsagesPEOCreatedBy | — |
| CREATION_DATE | PersonAddressUsagesPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonAddressUsagesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PersonAddressUsagesPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonAddressUsagesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonAddressUsagesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonAddressUsagesPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PersonAddressUsagesPEOObjectVersionNumber | — |
| PERSON_ADDR_USAGE_ID | PersonAddressUsagesPEOPersonAddrUsageId | — |
| PERSON_ID | PersonAddressUsagesPEOPersonId | — |

### [[personaddresspvo|PersonAddressPVO]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | PersonAddressUsagesPEOAddressId | — |
| ADDRESS_TYPE | PersonAddressUsagesPEOAddressType | ✅ |
| BUSINESS_GROUP_ID | PersonAddressUsagesPEOBusinessGroupId | — |
| CREATED_BY | PersonAddressUsagesPEOCreatedBy | — |
| CREATION_DATE | PersonAddressUsagesPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonAddressUsagesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PersonAddressUsagesPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonAddressUsagesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonAddressUsagesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonAddressUsagesPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PersonAddressUsagesPEOObjectVersionNumber | — |
| PERSON_ADDR_USAGE_ID | PersonAddressUsagesPEOPersonAddrUsageId | — |
| PERSON_ID | PersonAddressUsagesPEOPersonId | — |

### [[personaddresspvoviewall|PersonAddressPVOViewAll]] (HCM · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | PersonAddressUsagesPEOAddressId | — |
| ADDRESS_TYPE | PersonAddressUsagesPEOAddressType | ✅ |
| BUSINESS_GROUP_ID | PersonAddressUsagesPEOBusinessGroupId | — |
| CREATED_BY | PersonAddressUsagesPEOCreatedBy | — |
| CREATION_DATE | PersonAddressUsagesPEOCreationDate | — |
| EFFECTIVE_END_DATE | PersonAddressUsagesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PersonAddressUsagesPEOEffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PersonAddressUsagesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonAddressUsagesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonAddressUsagesPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PersonAddressUsagesPEOObjectVersionNumber | — |
| PERSON_ADDR_USAGE_ID | PersonAddressUsagesPEOPersonAddrUsageId | — |
| PERSON_ID | PersonAddressUsagesPEOPersonId | — |

### [[personaddressusageextractpvo|PersonAddressUsageExtractPVO]] (HCM · BICC: 13/79)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_ID | AddressId | ✅ |
| ADDRESS_TYPE | AddressType | ✅ |
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
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ADDR_USAGE_ID | PersonAddrUsageId | ✅ |
| PERSON_ID | PersonId | ✅ |
