---
id: DOC-PO-094
doc_type: system-doc
title: "POZ_SUPPLIER_REGISTRATIONS — Registros de Fornecedores (Onboarding)"
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
  - supplier-registration
  - onboarding
  - cadastro
aliases:
  - POZ_SUPPLIER_REGISTRATIONS
  - poz_supplier_registrations
  - registro-fornecedores
  - supplier-registration
  - onboarding-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIER_REGISTRATIONS

## Visão Geral

Armazena os **registros de onboarding de fornecedores** no Oracle Fusion Procurement. Cada registro representa uma solicitação de cadastro de novo fornecedor, capturando dados básicos (nome, país, tipo) e o status do processo de aprovação. Quando aprovado, o registro gera um fornecedor efetivo na tabela `POZ_SUPPLIERS`.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Onboarding de fornecedores:** Captura inicial de dados durante o processo de registro.
- **Supplier Portal:** Suporte ao auto-registro de fornecedores prospectivos via portal.
- **Workflow de aprovação:** Controle do fluxo de aprovação do registro (interno ou por convite).
- **Qualificação:** Primeira etapa do processo de qualificação antes da efetivação.
- **Auditoria:** Histórico completo de todos os registros de fornecedores, incluindo rejeitados.
- **Due diligence:** Base para verificações prévias antes da aprovação do fornecedor.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUPPLIER_REG_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de fornecedor | — | 🟢 85% |
| 2 | SUPPLIER_NAME | VARCHAR2(360) | NOT NULL | Identificação | Razão social do fornecedor prospectivo | — | 🟢 85% |
| 3 | REGISTRATION_NUMBER | VARCHAR2(30) | NULL | Identificação | Número do registro (visível ao usuário) | — | 🟡 75% |
| 4 | VENDOR_ID | NUMBER(18) | NULL | FK | ID do fornecedor efetivado (preenchido após aprovação) | [[poz_suppliers]] | 🟢 85% |
| 5 | REGISTRATION_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: DRAFT, SUBMITTED, APPROVED, REJECTED, WITHDRAWN | — | 🟢 85% |
| 6 | REGISTRATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo: PROSPECTIVE, INVITED, INTERNAL | — | 🟡 75% |
| 7 | COUNTRY_CODE | VARCHAR2(2) | NULL | Localização | País do fornecedor (ISO 3166-1 alpha-2) | — | 🟡 75% |
| 8 | SUPPLIER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do fornecedor: VENDOR, CONTRACTOR, etc. | — | 🟡 70% |
| 9 | TAX_PAYER_ID | VARCHAR2(80) | NULL | Fiscal | CNPJ/CPF do fornecedor prospectivo | — | 🟡 75% |
| 10 | DUNS_NUMBER | VARCHAR2(30) | NULL | Identificação | Número DUNS (Dun & Bradstreet) | — | 🟡 65% |
| 11 | EMAIL_ADDRESS | VARCHAR2(320) | NULL | Comunicação | E-mail de contato do registro | — | 🟡 75% |
| 12 | SUBMITTED_DATE | DATE | NULL | Data | Data de submissão do registro | — | 🟡 70% |
| 13 | APPROVED_DATE | DATE | NULL | Data | Data de aprovação | — | 🟡 70% |
| 14 | APPROVED_BY | NUMBER(18) | NULL | Aprovação | Usuário que aprovou | — | 🟡 70% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor efetivado, preenchido após aprovação)

### Tabelas-filha (FK de saída)

### Tabelas relacionadas

---

## Uso Típico

### Registros pendentes de aprovação
```sql
SELECT sr.SUPPLIER_REG_ID, sr.REGISTRATION_NUMBER,
       sr.SUPPLIER_NAME, sr.COUNTRY_CODE,
       sr.REGISTRATION_TYPE, sr.SUBMITTED_DATE
FROM   POZ_SUPPLIER_REGISTRATIONS sr
WHERE  sr.REGISTRATION_STATUS = 'SUBMITTED'
ORDER BY sr.SUBMITTED_DATE;
```

### Registros aprovados em um período
```sql
SELECT sr.SUPPLIER_REG_ID, sr.SUPPLIER_NAME,
       sr.VENDOR_ID, sr.APPROVED_DATE
FROM   POZ_SUPPLIER_REGISTRATIONS sr
WHERE  sr.REGISTRATION_STATUS = 'APPROVED'
  AND  sr.APPROVED_DATE BETWEEN :start_date AND :end_date;
```

### Taxa de aprovação
```sql
SELECT sr.REGISTRATION_STATUS, COUNT(*) AS qtd
FROM   POZ_SUPPLIER_REGISTRATIONS sr
WHERE  sr.CREATION_DATE >= ADD_MONTHS(SYSDATE, -12)
GROUP BY sr.REGISTRATION_STATUS;
```

---

## Observações

- O campo `VENDOR_ID` é **NULL** até a aprovação do registro; após aprovação, é preenchido com o ID do fornecedor criado em `POZ_SUPPLIERS`.
- O ciclo de vida do registro segue: DRAFT → SUBMITTED → APPROVED/REJECTED/WITHDRAWN.
- Registros do tipo `PROSPECTIVE` são originados pelo fornecedor no **Supplier Portal**; `INVITED` são gerados por convite interno; `INTERNAL` são criados pelo comprador.
- O campo `TAX_PAYER_ID` contém o CNPJ/CPF do prospectivo; após aprovação, este dado migra para `POZ_SUPPLIERS_PII`.
- Registros rejeitados (`REJECTED`) são mantidos para auditoria e não geram fornecedor efetivo.

---

## Referências

- [Oracle Docs — POZ_SUPPLIER_REGISTRATIONS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[negdocumentsourcingsupplierinviteepvo|NegDocumentSourcingSupplierInviteePVO]] (PO · BICC: 9/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | SupplierRegisAddressLine1 | — |
| ADDRESS_LINE2 | SupplierRegisAddressLine2 | — |
| ADDRESS_LINE3 | SupplierRegisAddressLine3 | — |
| ADDRESS_LINE4 | SupplierRegisAddressLine4 | — |
| ADDRESS_NICKNAME | SupplierRegisAddressNickname | — |
| CITY | SupplierRegisCity | — |
| CORPORATE_WEBSITE | SupplierRegisCorporateWebsite | — |
| COUNTRY | SupplierRegisCountry | — |
| COUNTY | SupplierRegisCounty | — |
| CREATED_BY | SupplierRegisCreatedBy | — |
| CREATION_DATE | SupplierRegisCreationDate | ✅ |
| DUNS_NUMBER | SupplierRegisDunsNumber | — |
| LAST_UPDATE_DATE | SupplierRegisLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierRegisLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierRegisLastUpdatedBy | ✅ |
| NOTE_FROM_SUPPLIER | SupplierRegisNoteFromSupplier | — |
| NOTE_TO_SUPPLIER | SupplierRegisNoteToSupplier | — |
| OBJECT_VERSION_NUMBER | SupplierRegisObjectVersionNumber | — |
| POSTAL_CODE | SupplierRegisPostalCode | — |
| PRC_BU_ID | SupplierRegisPrcBuId | — |
| PROVINCE | SupplierRegisProvince | — |
| REG_KEY | SupplierRegisRegKey | — |
| REGISTRATION_STATUS | SupplierRegisRegistrationStatus | — |
| REGISTRATION_TYPE | SupplierRegisRegistrationType | — |
| REJECTION_CODE | SupplierRegisRejectionCode | — |
| REQUEST_NUMBER | SupplierRegisRequestNumber | — |
| STATE | SupplierRegisState | — |
| SUPPLIER_NAME | SupplierRegisSupplierName | ✅ |
| SUPPLIER_NUMBER | SupplierRegisSupplierNumber | ✅ |
| SUPPLIER_REG_ID | SupplierRegisSupplierRegId | ✅ |
| TAX_REG_COUNTRY_CODE | SupplierRegisTaxRegCountryCode | — |
| TAX_REG_TYPE | SupplierRegisTaxRegType | — |
| TAX_REGISTRATION_NUMBER | SupplierRegisTaxRegistrationNumber | — |
| TAXPAYER_ID | SupplierRegisTaxpayerId | — |
| USER_REG_ID | SupplierRegisUserRegId | ✅ |
| VENDOR_ID | SupplierRegisVendorId | ✅ |
| VENDOR_PARTY_ID | SupplierRegisVendorPartyId | ✅ |

### [[negotiationsupplierinviteeextractpvo|NegotiationSupplierInviteeExtractPVO]] (PO · BICC: 53/53)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | AddressLine1 | ✅ |
| ADDRESS_LINE2 | AddressLine2 | ✅ |
| ADDRESS_LINE3 | AddressLine3 | ✅ |
| ADDRESS_LINE4 | AddressLine4 | ✅ |
| ADDRESS_NICKNAME | AddressNickname | ✅ |
| APPROVED_DATE | ApprovedDate | ✅ |
| BUSINESS_RELATIONSHIP_CODE | BusinessRelationshipCode | ✅ |
| CITY | City | ✅ |
| CORPORATE_WEBSITE | CorporateWebsite | ✅ |
| COUNTRY | Country | ✅ |
| COUNTY | County | ✅ |
| CREATED_BY | CreatedBy1 | ✅ |
| CREATION_DATE | CreationDate1 | ✅ |
| DUNS_NUMBER | DunsNumber | ✅ |
| INCOME_TAX_ID_FLAG | IncomeTaxIdFlag | ✅ |
| JUSTIFICATION | Justification | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy1 | ✅ |
| NOTE_FROM_SUPPLIER | NoteFromSupplier | ✅ |
| NOTE_TO_APPROVER | NoteToApprover | ✅ |
| NOTE_TO_SUPPLIER | NoteToSupplier | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | ✅ |
| ORGANIZATION_TYPE | OrganizationType | ✅ |
| POSTAL_CODE | PostalCode | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| PROVINCE | Province | ✅ |
| REG_KEY | RegKey | ✅ |
| REGISTRATION_STATUS | RegistrationStatus | ✅ |
| REGISTRATION_TYPE | RegistrationType | ✅ |
| REJECTION_CODE | RejectionCode | ✅ |
| REQUEST_NUMBER | RequestNumber | ✅ |
| REQUEST_REASON_CODE | RequestReasonCode | ✅ |
| REQUESTED_DATE | RequestedDate | ✅ |
| REQUESTER_EMAIL_ADDRESS | RequesterEmailAddress | ✅ |
| REQUESTER_FIRST_NAME | RequesterFirstName | ✅ |
| REQUESTER_LANGUAGE | RequesterLanguage | ✅ |
| REQUESTER_LAST_NAME | RequesterLastName | ✅ |
| REQUESTER_PERSON_ID | RequesterPersonId | ✅ |
| STATE | State | ✅ |
| SUPPLIER_CREATION_STATUS | SupplierCreationStatus | ✅ |
| SUPPLIER_NAME | SupplierName | ✅ |
| SUPPLIER_NUMBER | SupplierNumber | ✅ |
| SUPPLIER_REG_ID | SupplierRegId | ✅ |
| TAX_REG_COUNTRY_CODE | TaxRegCountryCode | ✅ |
| TAX_REG_NUMBER_FLAG | TaxRegNumberFlag | ✅ |
| TAX_REG_TYPE | TaxRegType | ✅ |
| TAX_REGISTRATION_NUMBER | TaxRegistrationNumber | ✅ |
| TAXPAYER_ID | TaxpayerId | ✅ |
| USER_REG_ID | UserRegId | ✅ |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_PARTY_ID | VendorPartyId | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | VendorTypeLookupCode | ✅ |

### [[supplierregistrationmappingpvo|SupplierRegistrationMappingPVO]] (PO · BICC: 22/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | SupplierRegistrationAddressLine1 | — |
| ADDRESS_LINE2 | SupplierRegistrationAddressLine2 | — |
| ADDRESS_LINE3 | SupplierRegistrationAddressLine3 | — |
| ADDRESS_LINE4 | SupplierRegistrationAddressLine4 | — |
| ADDRESS_NICKNAME | SupplierRegistrationAddressNickname | — |
| APPROVAL_INSTANCE_ID | SupplierRegistrationApprovalInstanceId | — |
| APPROVED_DATE | SupplierRegistrationApprovedDate | ✅ |
| BC_NOT_APPLICABLE_FLAG | SupplierRegistrationBcNotApplicableFlag | — |
| BUSINESS_RELATIONSHIP_CODE | SupplierRegistrationBusinessRelationshipCode | ✅ |
| CITY | SupplierRegistrationCity | — |
| CORPORATE_WEBSITE | SupplierRegistrationCorporateWebsite | ✅ |
| COUNTRY | SupplierRegistrationCountry | — |
| COUNTY | SupplierRegistrationCounty | — |
| CREATED_BY | SupplierRegistrationCreatedBy | — |
| CREATION_DATE | SupplierRegistrationCreationDate | — |
| DENIED_PARTY_FLAG | DeniedPartyFlag | — |
| DUNS_NUMBER | SupplierRegistrationDunsNumber | ✅ |
| INCOME_TAX_ID_FLAG | SupplierRegistrationIncomeTaxIdFlag | — |
| JUSTIFICATION | SupplierRegistrationJustification | ✅ |
| LAST_UPDATE_DATE | SupplierRegistrationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierRegistrationLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierRegistrationLastUpdatedBy | — |
| NOTE_FROM_SUPPLIER | SupplierRegistrationNoteFromSupplier | — |
| NOTE_TO_APPROVER | SupplierRegistrationNoteToApprover | ✅ |
| NOTE_TO_SUPPLIER | SupplierRegistrationNoteToSupplier | — |
| OBJECT_VERSION_NUMBER | SupplierRegistrationObjectVersionNumber | — |
| ORGANIZATION_TYPE | SupplierRegistrationOrganizationType | ✅ |
| POSTAL_CODE | SupplierRegistrationPostalCode | — |
| PRC_BU_ID | SupplierRegistrationPrcBuId | — |
| PROVINCE | SupplierRegistrationProvince | — |
| REG_KEY | SupplierRegistrationRegKey | — |
| REGISTRATION_STATUS | SupplierRegistrationRegistrationStatus | ✅ |
| REGISTRATION_TYPE | SupplierRegistrationRegistrationType | ✅ |
| REJECT_COMMENTS | RejectComments | ✅ |
| REJECT_REASON_CODE | RejectReasonCode | ✅ |
| REJECTION_CODE | SupplierRegistrationRejectionCode | — |
| REQ_TO_RESUBMIT_REASON | SupplierRegistrationReqToResubmitReason | — |
| REQUEST_NUMBER | SupplierRegistrationRequestNumber | ✅ |
| REQUEST_REASON_CODE | SupplierRegistrationRequestReasonCode | ✅ |
| REQUESTED_DATE | SupplierRegistrationRequestedDate | ✅ |
| REQUESTER_EMAIL_ADDRESS | SupplierRegistrationRequesterEmailAddress | ✅ |
| REQUESTER_FIRST_NAME | SupplierRegistrationRequesterFirstName | ✅ |
| REQUESTER_LANGUAGE | SupplierRegistrationRequesterLanguage | — |
| REQUESTER_LAST_NAME | SupplierRegistrationRequesterLastName | ✅ |
| REQUESTER_PERSON_ID | SupplierRegistrationRequesterPersonId | — |
| RESUBMISSION_NUM | SupplierRegistrationResubmissionNum | — |
| STATE | SupplierRegistrationState | — |
| SUPPLIER_CREATION_STATUS | SupplierRegistrationSupplierCreationStatus | ✅ |
| SUPPLIER_NAME | SupplierRegistrationSupplierName | ✅ |
| SUPPLIER_NUMBER | SupplierRegistrationSupplierNumber | — |
| SUPPLIER_REG_ID | SupplierRegId | ✅ |
| TAX_REG_COUNTRY_CODE | SupplierRegistrationTaxRegCountryCode | — |
| TAX_REG_NUMBER_FLAG | SupplierRegistrationTaxRegNumberFlag | — |
| TAX_REG_TYPE | SupplierRegistrationTaxRegType | — |
| TAX_REGISTRATION_NUMBER | SupplierRegistrationTaxRegistrationNumber | — |
| TAXPAYER_ID | SupplierRegistrationTaxpayerId | — |
| URL_VALIDATION_PARAM | SupplierRegistrationUrlValidationParam | — |
| USER_REG_ID | SupplierRegistrationUserRegId | — |
| VENDOR_ID | SupplierRegistrationVendorId | — |
| VENDOR_PARTY_ID | SupplierRegistrationVendorPartyId | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierRegistrationVendorTypeLookupCode | ✅ |
