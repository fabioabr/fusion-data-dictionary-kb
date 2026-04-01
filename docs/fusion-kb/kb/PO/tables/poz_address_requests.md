---
id: DOC-PO-069
doc_type: system-doc
title: "POZ_ADDRESS_REQUESTS — Solicitações de Endereço de Fornecedores"
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
  - endereco
  - cadastro
aliases:
  - POZ_ADDRESS_REQUESTS
  - poz_address_requests
  - solicitacoes-endereco-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_ADDRESS_REQUESTS

## 📌 Visão Geral

Armazena as **solicitações de criação ou alteração de endereços** de fornecedores no processo de registro e manutenção cadastral. Funciona como tabela de staging para endereços submetidos pelo fornecedor (via portal self-service) ou por compradores internos, que aguardam aprovação antes de serem efetivados no cadastro principal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro de fornecedores:** Registro de novos endereços durante o processo de supplier registration.
- **Atualização de endereço:** Solicitações de mudança de endereço pelo fornecedor via portal.
- **Workflow de aprovação:** Endereços submetidos que aguardam validação/aprovação interna.
- **Auditoria de mudanças:** Histórico de solicitações de alteração de endereço com status de aprovação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDRESS_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da solicitação de endereço | — | 🟡 80% |
| 2 | SUPPLIER_REG_ID | NUMBER(18) | NULL | FK | Registro de fornecedor associado (se novo cadastro) | — | 🟡 70% |
| 3 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor existente (se atualização) | [[poz_suppliers]] | 🟡 75% |
| 4 | ADDRESS_NAME | VARCHAR2(240) | NULL | Descrição | Nome/alias do endereço | — | 🟡 75% |
| 5 | ADDRESS_LINE1 | VARCHAR2(240) | NOT NULL | Endereço | Linha 1 do endereço | — | 🟢 90% |
| 6 | ADDRESS_LINE2 | VARCHAR2(240) | NULL | Endereço | Linha 2 do endereço | — | 🟢 90% |
| 7 | ADDRESS_LINE3 | VARCHAR2(240) | NULL | Endereço | Linha 3 do endereço | — | 🟢 85% |
| 8 | CITY | VARCHAR2(60) | NULL | Endereço | Cidade | — | 🟢 90% |
| 9 | STATE | VARCHAR2(60) | NULL | Endereço | Estado/província | — | 🟢 90% |
| 10 | POSTAL_CODE | VARCHAR2(30) | NULL | Endereço | CEP/código postal | — | 🟢 90% |
| 11 | COUNTRY | VARCHAR2(60) | NOT NULL | Endereço | País (código ISO) | — | 🟢 90% |
| 12 | REQUEST_STATUS | VARCHAR2(30) | NULL | Status | Status da solicitação: PENDING, APPROVED, REJECTED | — | 🟡 75% |
| 13 | REQUEST_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo: NEW, UPDATE, DELETE | — | 🟡 70% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor existente)

### Tabelas-filha (FK de saída)
- Após aprovação, os dados são transferidos para `HZ_LOCATIONS` / `HZ_PARTY_SITES`

---

## 📎 Uso Típico

### Solicitações pendentes de aprovação
```sql
SELECT ar.ADDRESS_REQUEST_ID, ar.VENDOR_ID,
       ar.ADDRESS_LINE1, ar.CITY, ar.STATE, ar.COUNTRY,
       ar.REQUEST_STATUS
FROM   POZ_ADDRESS_REQUESTS ar
WHERE  ar.REQUEST_STATUS = 'PENDING';
```

### Histórico de endereços solicitados por fornecedor
```sql
SELECT ar.ADDRESS_LINE1, ar.CITY, ar.STATE,
       ar.REQUEST_TYPE, ar.REQUEST_STATUS,
       ar.CREATION_DATE
FROM   POZ_ADDRESS_REQUESTS ar
WHERE  ar.VENDOR_ID = :p_vendor_id
ORDER BY ar.CREATION_DATE DESC;
```

---

## 🔒 Observações

- Esta tabela funciona como **staging** — os endereços finais aprovados são persistidos nas tabelas TCA (`HZ_LOCATIONS`, `HZ_PARTY_SITES`).
- Solicitações rejeitadas permanecem para auditoria com `REQUEST_STATUS = 'REJECTED'`.
- Durante o supplier registration (novo cadastro), o `VENDOR_ID` pode ser nulo; o `SUPPLIER_REG_ID` conecta ao registro em andamento.
- Endereços internacionais seguem o padrão ISO de país e podem ter formatos variados de estado/província.

---

## 🔗 PVOs Relacionados

### [[supplierregistrationaddressrequestpvo|SupplierRegistrationAddressRequestPVO]] (PO · BICC: 21/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_LINE1 | SupplierRegAddressRequestAddressLine1 | ✅ |
| ADDRESS_LINE2 | SupplierRegAddressRequestAddressLine2 | ✅ |
| ADDRESS_LINE3 | SupplierRegAddressRequestAddressLine3 | ✅ |
| ADDRESS_LINE4 | SupplierRegAddressRequestAddressLine4 | ✅ |
| ADDRESS_LINES_PHONETIC | SupplierRegAddressRequestAddressLinesPhonetic | — |
| ADDRESS_REQUEST_ID | AddressRequestId | ✅ |
| BUILDING | SupplierRegAddressRequestBuilding | — |
| CITY | SupplierRegAddressRequestCity | ✅ |
| COUNTRY | SupplierRegAddressRequestCountry | — |
| COUNTY | SupplierRegAddressRequestCounty | ✅ |
| CREATED_BY | SupplierRegAddressRequestCreatedBy | — |
| CREATION_DATE | SupplierRegAddressRequestCreationDate | — |
| EMAIL_ADDRESS | SupplierRegAddressRequestEmailAddress | ✅ |
| END_DATE_ACTIVE | SupplierRegAddressRequestEndDateActive | — |
| FAX_AREA_CODE | SupplierRegAddressRequestFaxAreaCode | ✅ |
| FAX_COUNTRY_CODE | SupplierRegAddressRequestFaxCountryCode | ✅ |
| FAX_NUMBER | SupplierRegAddressRequestFaxNumber | ✅ |
| FLOOR_NUMBER | SupplierRegAddressRequestFloorNumber | — |
| HAS_BACKING_DOC | SupplierRegAddressRequestHasBackingDoc | — |
| LAST_UPDATE_DATE | SupplierRegAddressRequestLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierRegAddressRequestLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierRegAddressRequestLastUpdatedBy | — |
| MAPPING_ID | SupplierRegAddressRequestMappingId | — |
| OBJECT_VERSION_NUMBER | SupplierRegAddressRequestObjectVersionNumber | — |
| PARTY_SITE_ID | SupplierRegAddressRequestPartySiteId | — |
| PARTY_SITE_NAME | SupplierRegAddressRequestPartySiteName | ✅ |
| PAY_FLAG | SupplierRegAddressRequestPayFlag | ✅ |
| PHONE_AREA_CODE | SupplierRegAddressRequestPhoneAreaCode | ✅ |
| PHONE_COUNTRY_CODE | SupplierRegAddressRequestPhoneCountryCode | ✅ |
| PHONE_EXTENSION | SupplierRegAddressRequestPhoneExtension | — |
| PHONE_NUMBER | SupplierRegAddressRequestPhoneNumber | ✅ |
| POSTAL_CODE | SupplierRegAddressRequestPostalCode | ✅ |
| POSTAL_PLUS4_CODE | SupplierRegAddressRequestPostalPlus4Code | — |
| PRIMARY_PAY_FLAG | SupplierRegAddressRequestPrimaryPayFlag | — |
| PROVINCE | SupplierRegAddressRequestProvince | — |
| PUR_FLAG | SupplierRegAddressRequestPurFlag | ✅ |
| REQUEST_STATUS | SupplierRegAddressRequestRequestStatus | — |
| REQUEST_TYPE | SupplierRegAddressRequestRequestType | — |
| REQUESTED_START_DATE | SupplierRegAddressRequestRequestedStartDate | — |
| RFQ_FLAG | SupplierRegAddressRequestRfqFlag | ✅ |
| STATE | SupplierRegAddressRequestState | ✅ |

---

## 📚 Referências

- [Oracle Docs — POZ Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poztables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
