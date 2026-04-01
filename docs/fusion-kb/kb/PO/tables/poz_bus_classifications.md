---
id: DOC-PO-078
doc_type: system-doc
title: "POZ_BUS_CLASSIFICATIONS — Classificações de Negócio de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - fornecedores
  - classificacao
  - diversidade
aliases:
  - POZ_BUS_CLASSIFICATIONS
  - poz_bus_classifications
  - classificacoes-negocio
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_BUS_CLASSIFICATIONS

## 📌 Visão Geral

Armazena as **classificações de negócio** atribuídas a fornecedores — incluindo classificações de diversidade (Small Business, Minority-Owned, Woman-Owned, etc.), classificações setoriais e certificações. Cada registro representa uma classificação específica vinculada a um fornecedor, com dados de certificação, agência certificadora e validade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de diversidade:** Registro e controle de classificações de diversidade de fornecedores.
- **Compliance regulatório:** Evidência de aderência a políticas de gastos com fornecedores diversificados.
- **Qualificação de fornecedores:** Armazenamento de certificações obrigatórias para participação em processos de compra.
- **Sourcing:** Filtro de fornecedores elegíveis por classificação em processos de licitação.
- **Relatórios de diversidade:** Base de dados para métricas de diversidade de fornecedores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da classificação | — | 🟢 90% |
| 2 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 3 | LOOKUP_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da classificação (ex: BUSINESS_CLASSIFICATION) | — | 🟢 85% |
| 4 | LOOKUP_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da classificação (ex: SMALL_BUSINESS, MINORITY_OWNED) | — | 🟢 85% |
| 5 | CERTIFYING_AGENCY_ID | NUMBER(18) | NULL | FK | Agência que emitiu a certificação | [[poz_certifying_agencies]] | 🟢 85% |
| 6 | CERTIFICATION_NUM | VARCHAR2(30) | NULL | Identificação | Número do certificado emitido | — | 🟡 80% |
| 7 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da classificação/certificação | — | 🟢 85% |
| 8 | CLASS_STATUS | VARCHAR2(30) | NULL | Status | Status: APPROVED, PENDING, EXPIRED, REJECTED | — | 🟡 75% |
| 9 | PARTY_ID | NUMBER(18) | NULL | FK | Party ID no TCA | [[hz_parties]] | 🟡 80% |
| 10 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟢 90% |
| 11 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 16 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor classificado pela classificação empresarial)
- [[poz_certifying_agencies]] — via `CERTIFYING_AGENCY_ID` (agência certificadora)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA da classificação empresarial)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Classificações ativas por fornecedor
```sql
SELECT bc.CLASSIFICATION_ID, bc.LOOKUP_CODE,
       bc.CERTIFICATION_NUM, bc.EXPIRATION_DATE,
       bc.CLASS_STATUS
FROM   POZ_BUS_CLASSIFICATIONS bc
WHERE  bc.VENDOR_ID = :p_vendor_id
  AND  (bc.EXPIRATION_DATE IS NULL OR bc.EXPIRATION_DATE > SYSDATE)
  AND  bc.CLASS_STATUS = 'APPROVED';
```

### Classificações expiradas (renovação necessária)
```sql
SELECT bc.VENDOR_ID, bc.LOOKUP_CODE,
       bc.CERTIFICATION_NUM, bc.EXPIRATION_DATE
FROM   POZ_BUS_CLASSIFICATIONS bc
WHERE  bc.EXPIRATION_DATE < SYSDATE
  AND  bc.CLASS_STATUS = 'APPROVED';
```

---

## 🔒 Observações

- Um fornecedor pode ter múltiplas classificações simultâneas (ex: Small Business + Minority-Owned).
- A `EXPIRATION_DATE` deve ser monitorada; classificações expiradas devem ser renovadas ou desativadas.
- Os códigos de classificação padrão Oracle incluem: `SMALL_BUSINESS`, `MINORITY_OWNED`, `WOMAN_OWNED`, `VETERAN_OWNED`, `HUB_ZONE`, `DISABLED_VETERAN`.
- A agência certificadora valida a autenticidade da classificação; referencia [[poz_certifying_agencies]].
- Classificações podem ser auto-declaradas ou certificadas por terceiros, conforme política da organização.

---

## 🔗 PVOs Relacionados

### [[supplierbusinessclassificationextractpvo|SupplierBusinessClassificationExtractPVO]] (PO · BICC: 21/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CERTIFICATE_NUMBER | CertificateNumber | ✅ |
| CERTIFYING_AGENCY_ID | CertifyingAgencyId | ✅ |
| CLASS_STATUS | ClassStatus | ✅ |
| CLASSIFICATION_ID | ClassificationId | ✅ |
| CONFIRMED_ON | ConfirmedOn | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DELETED | Deleted | ✅ |
| EXPIRATION_DATE | ExpirationDate | ✅ |
| EXT_ATTR_1 | ExtAttr1 | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOOKUP_CODE | LookupCode | ✅ |
| NOTES | Notes | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OTHER_CERTIFYING_AGENCY | OtherCertifyingAgency | ✅ |
| PARTY_ID | PartyId | ✅ |
| PROVIDED_BY_CONTACT_ID | ProvidedByContactId | ✅ |
| START_DATE | StartDate | ✅ |
| VENDOR_ID | VendorId | ✅ |

### [[supplierpvo|SupplierPVO]] (PO · BICC: 26/108)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CERTIFICATE_NUMBER | BusClass1CertificateNumber | — |
| CERTIFICATE_NUMBER | BusClass2CertificateNumber | — |
| CERTIFICATE_NUMBER | BusClass3CertificateNumber | — |
| CERTIFICATE_NUMBER | BusClass4CertificateNumber | — |
| CERTIFICATE_NUMBER | BusClass5CertificateNumber | — |
| CERTIFICATE_NUMBER | BusClass6CertificateNumber | — |
| CERTIFYING_AGENCY | BusClass1CertifyingAgency | — |
| CERTIFYING_AGENCY | BusClass2CertifyingAgency | — |
| CERTIFYING_AGENCY | BusClass3CertifyingAgency | — |
| CERTIFYING_AGENCY | BusClass4CertifyingAgency | — |
| CERTIFYING_AGENCY | BusClass5CertifyingAgency | — |
| CERTIFYING_AGENCY | BusClass6CertifyingAgency | — |
| CLASS_STATUS | BusClass1ClassStatus | — |
| CLASS_STATUS | BusClass2ClassStatus | — |
| CLASS_STATUS | BusClass3ClassStatus | — |
| CLASS_STATUS | BusClass4ClassStatus | — |
| CLASS_STATUS | BusClass5ClassStatus | — |
| CLASS_STATUS | BusClass6ClassStatus | — |
| CLASSIFICATION_ID | BusClass1ClassificationId | ✅ |
| CLASSIFICATION_ID | BusClass2ClassificationId | ✅ |
| CLASSIFICATION_ID | BusClass3ClassificationId | ✅ |
| CLASSIFICATION_ID | BusClass4ClassificationId | ✅ |
| CLASSIFICATION_ID | BusClass5ClassificationId | ✅ |
| CLASSIFICATION_ID | BusClass6ClassificationId | ✅ |
| CREATED_BY | BusClass1CreatedBy | — |
| CREATED_BY | BusClass2CreatedBy | — |
| CREATED_BY | BusClass3CreatedBy | — |
| CREATED_BY | BusClass4CreatedBy | — |
| CREATED_BY | BusClass5CreatedBy | — |
| CREATED_BY | BusClass6CreatedBy | — |
| CREATION_DATE | BusClass1CreationDate | — |
| CREATION_DATE | BusClass2CreationDate | — |
| CREATION_DATE | BusClass3CreationDate | — |
| CREATION_DATE | BusClass4CreationDate | — |
| CREATION_DATE | BusClass5CreationDate | — |
| CREATION_DATE | BusClass6CreationDate | — |
| END_DATE_ACTIVE | BusClass1EndDateActive | — |
| END_DATE_ACTIVE | BusClass2EndDateActive | — |
| END_DATE_ACTIVE | BusClass3EndDateActive | — |
| END_DATE_ACTIVE | BusClass4EndDateActive | — |
| END_DATE_ACTIVE | BusClass5EndDateActive | — |
| END_DATE_ACTIVE | BusClass6EndDateActive | — |
| EXPIRATION_DATE | BusClass1ExpirationDate | — |
| EXPIRATION_DATE | BusClass2ExpirationDate | — |
| EXPIRATION_DATE | BusClass3ExpirationDate | — |
| EXPIRATION_DATE | BusClass4ExpirationDate | — |
| EXPIRATION_DATE | BusClass5ExpirationDate | — |
| EXPIRATION_DATE | BusClass6ExpirationDate | — |
| EXT_ATTR_1 | BusClass1ExtAttr1 | ✅ |
| EXT_ATTR_1 | BusClass2ExtAttr1 | ✅ |
| EXT_ATTR_1 | BusClass3ExtAttr1 | — |
| EXT_ATTR_1 | BusClass4ExtAttr1 | — |
| EXT_ATTR_1 | BusClass5ExtAttr1 | — |
| EXT_ATTR_1 | BusClass6ExtAttr1 | — |
| LAST_UPDATE_DATE | BusClass1LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | BusClass2LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | BusClass3LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | BusClass4LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | BusClass5LastUpdateDate | ✅ |
| LAST_UPDATE_DATE | BusClass6LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusClass1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BusClass2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BusClass3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BusClass4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BusClass5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | BusClass6LastUpdateLogin | — |
| LAST_UPDATED_BY | BusClass1LastUpdatedBy | — |
| LAST_UPDATED_BY | BusClass2LastUpdatedBy | — |
| LAST_UPDATED_BY | BusClass3LastUpdatedBy | — |
| LAST_UPDATED_BY | BusClass4LastUpdatedBy | — |
| LAST_UPDATED_BY | BusClass5LastUpdatedBy | — |
| LAST_UPDATED_BY | BusClass6LastUpdatedBy | — |
| LOOKUP_CODE | BusClass1LookupCode | ✅ |
| LOOKUP_CODE | BusClass2LookupCode | ✅ |
| LOOKUP_CODE | BusClass3LookupCode | ✅ |
| LOOKUP_CODE | BusClass4LookupCode | ✅ |
| LOOKUP_CODE | BusClass5LookupCode | ✅ |
| LOOKUP_CODE | BusClass6LookupCode | ✅ |
| OBJECT_VERSION_NUMBER | BusClass1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BusClass2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BusClass3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BusClass4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BusClass5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | BusClass6ObjectVersionNumber | — |
| PARTY_ID | BusClass1PartyId | — |
| PARTY_ID | BusClass2PartyId | — |
| PARTY_ID | BusClass3PartyId | — |
| PARTY_ID | BusClass4PartyId | — |
| PARTY_ID | BusClass5PartyId | — |
| PARTY_ID | BusClass6PartyId | — |
| START_DATE_ACTIVE | BusClass1StartDateActive | — |
| START_DATE_ACTIVE | BusClass2StartDateActive | — |
| START_DATE_ACTIVE | BusClass3StartDateActive | — |
| START_DATE_ACTIVE | BusClass4StartDateActive | — |
| START_DATE_ACTIVE | BusClass5StartDateActive | — |
| START_DATE_ACTIVE | BusClass6StartDateActive | — |
| STATUS | BusClass1Status | ✅ |
| STATUS | BusClass2Status | ✅ |
| STATUS | BusClass3Status | ✅ |
| STATUS | BusClass4Status | ✅ |
| STATUS | BusClass5Status | ✅ |
| STATUS | BusClass6Status | ✅ |
| VENDOR_ID | BusClass1VendorId | — |
| VENDOR_ID | BusClass2VendorId | — |
| VENDOR_ID | BusClass3VendorId | — |
| VENDOR_ID | BusClass4VendorId | — |
| VENDOR_ID | BusClass5VendorId | — |
| VENDOR_ID | BusClass6VendorId | — |

---

## 📚 Referências

- [Oracle Docs — POZ_BUS_CLASSIFICATIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pozbusclassifications.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
