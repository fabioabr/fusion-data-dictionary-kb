---
id: DOC-PO-090
doc_type: system-doc
title: "POZ_SUPPLIERS_V — View Consolidada de Fornecedores"
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
  - suppliers
  - fornecedores
  - view-consolidada
aliases:
  - POZ_SUPPLIERS_V
  - poz_suppliers_v
  - view-fornecedores
  - suppliers-view
  - fornecedores-consolidado
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIERS_V

## Visão Geral

View consolidada que combina dados do **cadastro principal de fornecedores** (`POZ_SUPPLIERS`) com informações do Trading Community Architecture (`HZ_PARTIES`). Apresenta uma visão unificada do fornecedor incluindo nome, número, status, tipo, classificação e dados de party — simplificando consultas que normalmente exigiriam joins manuais.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** (visão), combinando dados de múltiplas tabelas base para simplificar consultas.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Consulta simplificada:** Acesso rápido a dados de fornecedores sem necessidade de joins com HZ_PARTIES.
- **Relatórios:** Base para reports e analytics que necessitam de dados consolidados de fornecedores.
- **LOVs (List of Values):** Utilizada em telas de seleção de fornecedor para exibir nome e número.
- **Integrações:** Fonte de dados para interfaces e APIs que consomem dados de fornecedores.
- **BI/Analytics:** Dimensão de fornecedor em modelos analíticos e OTBI.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do fornecedor | [[poz_suppliers]] | 🟢 90% |
| 2 | VENDOR_NAME | VARCHAR2(360) | NOT NULL | Identificação | Razão social / nome do fornecedor | — | 🟢 90% |
| 3 | SEGMENT1 | VARCHAR2(30) | NOT NULL | Identificação | Número do fornecedor (código visível) | — | 🟢 90% |
| 4 | VENDOR_TYPE_LOOKUP_CODE | VARCHAR2(30) | NULL | Classificação | Tipo: VENDOR, EMPLOYEE, TAX_AUTHORITY | — | 🟢 85% |
| 5 | PARTY_ID | NUMBER(18) | NOT NULL | FK | Identificador do party no TCA | [[hz_parties]] | 🟢 85% |
| 6 | PARTY_NAME | VARCHAR2(360) | NULL | Identificação | Nome do party no TCA (pode diferir de VENDOR_NAME) | — | 🟡 75% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Fornecedor ativo (Y/N) | — | 🟢 85% |
| 8 | BUSINESS_RELATIONSHIP | VARCHAR2(30) | NULL | Classificação | Tipo de relacionamento: SPEND_AUTHORIZED, NOT_AUTHORIZED | — | 🟡 75% |
| 9 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início de atividade | — | 🟢 85% |
| 10 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de encerramento de atividade | — | 🟢 85% |
| 11 | DUNS_NUMBER | VARCHAR2(30) | NULL | Identificação | Número DUNS (Dun & Bradstreet) | — | 🟡 70% |
| 12 | ONE_TIME_FLAG | VARCHAR2(1) | NULL | Classificação | Fornecedor de uso único (Y/N) | — | 🟡 75% |
| 13 | PARENT_VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor-pai (hierarquia) | [[poz_suppliers]] | 🟡 70% |
| 14 | TAX_ORGANIZATION_TYPE_CODE | VARCHAR2(30) | NULL | Fiscal | Tipo de organização fiscal | — | 🟡 65% |

---

## Relacionamentos

### Tabelas-base

### Tabelas relacionadas

---

## Uso Típico

### Pesquisa de fornecedores ativos
```sql
SELECT sv.VENDOR_ID, sv.SEGMENT1, sv.VENDOR_NAME,
       sv.VENDOR_TYPE_LOOKUP_CODE, sv.BUSINESS_RELATIONSHIP
FROM   POZ_SUPPLIERS_V sv
WHERE  sv.ENABLED_FLAG = 'Y'
  AND  (sv.END_DATE_ACTIVE IS NULL OR sv.END_DATE_ACTIVE > SYSDATE)
  AND  UPPER(sv.VENDOR_NAME) LIKE UPPER(:p_search || '%');
```

### LOV de fornecedores para seleção
```sql
SELECT sv.VENDOR_ID, sv.SEGMENT1 || ' - ' || sv.VENDOR_NAME AS display
FROM   POZ_SUPPLIERS_V sv
WHERE  sv.ENABLED_FLAG = 'Y'
  AND  sv.VENDOR_TYPE_LOOKUP_CODE = 'VENDOR'
ORDER BY sv.SEGMENT1;
```

---

## Observações

- Por ser uma **view**, não suporta operações DML; alterações devem ser feitas nas tabelas base (`POZ_SUPPLIERS`, `HZ_PARTIES`).
- A view combina dados de **POZ_SUPPLIERS** e **HZ_PARTIES**, eliminando a necessidade de join explícito.
- O campo `PARTY_NAME` pode diferir de `VENDOR_NAME` quando o registro TCA foi atualizado independentemente.
- Esta view é frequentemente utilizada como base para **OTBI (Oracle Transactional BI)** e relatórios customizados.
- Não contém dados PII — para informações fiscais, consultar `POZ_SUPPLIERS_PII` separadamente.

---

## Referências

- [Oracle Docs — POZ_SUPPLIERS_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[assetinvoicepvo|AssetInvoicePVO]] (OTHER · BICC: 1/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierNameAllowAwtFlag | — |
| AWT_GROUP_ID | SupplierNameAwtGroupId | — |
| CORPORATE_WEBSITE | SupplierNameCorporateWebsite | — |
| CUSTOMER_NUM | SupplierNameCustomerNum | — |
| END_DATE_ACTIVE | SupplierNameEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierNameFederalReportableFlag | — |
| MIN_ORDER_AMOUNT | SupplierNameMinOrderAmount | — |
| NAME_CONTROL | SupplierNameNameControl | — |
| NI_NUMBER | SupplierNameNiNumber | — |
| ONE_TIME_FLAG | SupplierNameOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierNameOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierNameParentPartyId | — |
| PARENT_VENDOR_ID | SupplierNameParentVendorId | — |
| PARTY_ID | SupplierNamePartyId | — |
| PROGRAM_APPLICATION_ID | SupplierNameProgramApplicationId | — |
| PROGRAM_ID | SupplierNameProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierNameProgramUpdateDate | — |
| REQUEST_ID | SupplierNameRequestId | — |
| SEGMENT1 | SupplierNameSegment1 | — |
| STANDARD_INDUSTRY_CLASS | SupplierNameStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierNameStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierNameStateReportableFlag | — |
| TAX_REPORTING_NAME | SupplierNameTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierNameTaxVerificationDate | — |
| TYPE_1099 | SupplierNameType1099 | — |
| VENDOR_ID | SupplierNameVendorId | — |
| VENDOR_NAME | SupplierNameVendorName | ✅ |
| VENDOR_NAME_ALT | SupplierNameVendorNameAlt | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierNameVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierNameWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierNameWithholdingStatusLookupCode | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| VENDOR_ID | AwtSupplierVendorId | — |
| VENDOR_NAME | AwtSupplierVendorName | ✅ |

### [[maintenancewooperationspvo|MaintenanceWOOperationsPVO]] (OTHER · BICC: 3/292)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | POSupplierNamePEOAllowAwtFlag1 | — |
| ALLOW_AWT_FLAG | SupplierNamePEOAllowAwtFlag | — |
| ATTRIBUTE1 | POSupplierNamePEOAttribute150 | — |
| ATTRIBUTE1 | SupplierNamePEOAttribute130 | — |
| ATTRIBUTE10 | POSupplierNamePEOAttribute1011 | — |
| ATTRIBUTE10 | SupplierNamePEOAttribute109 | — |
| ATTRIBUTE11 | POSupplierNamePEOAttribute1115 | — |
| ATTRIBUTE11 | SupplierNamePEOAttribute1113 | — |
| ATTRIBUTE12 | POSupplierNamePEOAttribute1213 | — |
| ATTRIBUTE12 | SupplierNamePEOAttribute1211 | — |
| ATTRIBUTE13 | POSupplierNamePEOAttribute1311 | — |
| ATTRIBUTE13 | SupplierNamePEOAttribute139 | — |
| ATTRIBUTE14 | POSupplierNamePEOAttribute1411 | — |
| ATTRIBUTE14 | SupplierNamePEOAttribute149 | — |
| ATTRIBUTE15 | POSupplierNamePEOAttribute1511 | — |
| ATTRIBUTE15 | SupplierNamePEOAttribute159 | — |
| ATTRIBUTE16 | POSupplierNamePEOAttribute1611 | — |
| ATTRIBUTE16 | SupplierNamePEOAttribute169 | — |
| ATTRIBUTE17 | POSupplierNamePEOAttribute1711 | — |
| ATTRIBUTE17 | SupplierNamePEOAttribute179 | — |
| ATTRIBUTE18 | POSupplierNamePEOAttribute1811 | — |
| ATTRIBUTE18 | SupplierNamePEOAttribute189 | — |
| ATTRIBUTE19 | POSupplierNamePEOAttribute1911 | — |
| ATTRIBUTE19 | SupplierNamePEOAttribute199 | — |
| ATTRIBUTE2 | POSupplierNamePEOAttribute211 | — |
| ATTRIBUTE2 | SupplierNamePEOAttribute29 | — |
| ATTRIBUTE20 | POSupplierNamePEOAttribute2011 | — |
| ATTRIBUTE20 | SupplierNamePEOAttribute209 | — |
| ATTRIBUTE3 | POSupplierNamePEOAttribute311 | — |
| ATTRIBUTE3 | SupplierNamePEOAttribute39 | — |
| ATTRIBUTE4 | POSupplierNamePEOAttribute411 | — |
| ATTRIBUTE4 | SupplierNamePEOAttribute49 | — |
| ATTRIBUTE5 | POSupplierNamePEOAttribute511 | — |
| ATTRIBUTE5 | SupplierNamePEOAttribute59 | — |
| ATTRIBUTE6 | POSupplierNamePEOAttribute611 | — |
| ATTRIBUTE6 | SupplierNamePEOAttribute69 | — |
| ATTRIBUTE7 | POSupplierNamePEOAttribute711 | — |
| ATTRIBUTE7 | SupplierNamePEOAttribute79 | — |
| ATTRIBUTE8 | POSupplierNamePEOAttribute811 | — |
| ATTRIBUTE8 | SupplierNamePEOAttribute89 | — |
| ATTRIBUTE9 | POSupplierNamePEOAttribute911 | — |
| ATTRIBUTE9 | SupplierNamePEOAttribute99 | — |
| ATTRIBUTE_CATEGORY | POSupplierNamePEOAttributeCategory11 | — |
| ATTRIBUTE_CATEGORY | SupplierNamePEOAttributeCategory9 | — |
| ATTRIBUTE_DATE1 | POSupplierNamePEOAttributeDate111 | — |
| ATTRIBUTE_DATE1 | SupplierNamePEOAttributeDate19 | — |
| ATTRIBUTE_DATE10 | POSupplierNamePEOAttributeDate105 | — |
| ATTRIBUTE_DATE10 | SupplierNamePEOAttributeDate103 | — |
| ATTRIBUTE_DATE2 | POSupplierNamePEOAttributeDate211 | — |
| ATTRIBUTE_DATE2 | SupplierNamePEOAttributeDate29 | — |
| ATTRIBUTE_DATE3 | POSupplierNamePEOAttributeDate311 | — |
| ATTRIBUTE_DATE3 | SupplierNamePEOAttributeDate39 | — |
| ATTRIBUTE_DATE4 | POSupplierNamePEOAttributeDate411 | — |
| ATTRIBUTE_DATE4 | SupplierNamePEOAttributeDate49 | — |
| ATTRIBUTE_DATE5 | POSupplierNamePEOAttributeDate511 | — |
| ATTRIBUTE_DATE5 | SupplierNamePEOAttributeDate59 | — |
| ATTRIBUTE_DATE6 | POSupplierNamePEOAttributeDate65 | — |
| ATTRIBUTE_DATE6 | SupplierNamePEOAttributeDate63 | — |
| ATTRIBUTE_DATE7 | POSupplierNamePEOAttributeDate75 | — |
| ATTRIBUTE_DATE7 | SupplierNamePEOAttributeDate73 | — |
| ATTRIBUTE_DATE8 | POSupplierNamePEOAttributeDate85 | — |
| ATTRIBUTE_DATE8 | SupplierNamePEOAttributeDate83 | — |
| ATTRIBUTE_DATE9 | POSupplierNamePEOAttributeDate95 | — |
| ATTRIBUTE_DATE9 | SupplierNamePEOAttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | POSupplierNamePEOAttributeNumber111 | — |
| ATTRIBUTE_NUMBER1 | SupplierNamePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER10 | POSupplierNamePEOAttributeNumber1011 | — |
| ATTRIBUTE_NUMBER10 | SupplierNamePEOAttributeNumber109 | — |
| ATTRIBUTE_NUMBER2 | POSupplierNamePEOAttributeNumber211 | — |
| ATTRIBUTE_NUMBER2 | SupplierNamePEOAttributeNumber29 | — |
| ATTRIBUTE_NUMBER3 | POSupplierNamePEOAttributeNumber311 | — |
| ATTRIBUTE_NUMBER3 | SupplierNamePEOAttributeNumber39 | — |
| ATTRIBUTE_NUMBER4 | POSupplierNamePEOAttributeNumber411 | — |
| ATTRIBUTE_NUMBER4 | SupplierNamePEOAttributeNumber49 | — |
| ATTRIBUTE_NUMBER5 | POSupplierNamePEOAttributeNumber511 | — |
| ATTRIBUTE_NUMBER5 | SupplierNamePEOAttributeNumber59 | — |
| ATTRIBUTE_NUMBER6 | POSupplierNamePEOAttributeNumber611 | — |
| ATTRIBUTE_NUMBER6 | SupplierNamePEOAttributeNumber69 | — |
| ATTRIBUTE_NUMBER7 | POSupplierNamePEOAttributeNumber711 | — |
| ATTRIBUTE_NUMBER7 | SupplierNamePEOAttributeNumber79 | — |
| ATTRIBUTE_NUMBER8 | POSupplierNamePEOAttributeNumber811 | — |
| ATTRIBUTE_NUMBER8 | SupplierNamePEOAttributeNumber89 | — |
| ATTRIBUTE_NUMBER9 | POSupplierNamePEOAttributeNumber911 | — |
| ATTRIBUTE_NUMBER9 | SupplierNamePEOAttributeNumber99 | — |
| ATTRIBUTE_TIMESTAMP1 | POSupplierNamePEOAttributeTimestamp111 | — |
| ATTRIBUTE_TIMESTAMP1 | SupplierNamePEOAttributeTimestamp19 | — |
| ATTRIBUTE_TIMESTAMP10 | POSupplierNamePEOAttributeTimestamp105 | — |
| ATTRIBUTE_TIMESTAMP10 | SupplierNamePEOAttributeTimestamp103 | — |
| ATTRIBUTE_TIMESTAMP2 | POSupplierNamePEOAttributeTimestamp211 | — |
| ATTRIBUTE_TIMESTAMP2 | SupplierNamePEOAttributeTimestamp29 | — |
| ATTRIBUTE_TIMESTAMP3 | POSupplierNamePEOAttributeTimestamp311 | — |
| ATTRIBUTE_TIMESTAMP3 | SupplierNamePEOAttributeTimestamp39 | — |
| ATTRIBUTE_TIMESTAMP4 | POSupplierNamePEOAttributeTimestamp411 | — |
| ATTRIBUTE_TIMESTAMP4 | SupplierNamePEOAttributeTimestamp49 | — |
| ATTRIBUTE_TIMESTAMP5 | POSupplierNamePEOAttributeTimestamp511 | — |
| ATTRIBUTE_TIMESTAMP5 | SupplierNamePEOAttributeTimestamp59 | — |
| ATTRIBUTE_TIMESTAMP6 | POSupplierNamePEOAttributeTimestamp65 | — |
| ATTRIBUTE_TIMESTAMP6 | SupplierNamePEOAttributeTimestamp63 | — |
| ATTRIBUTE_TIMESTAMP7 | POSupplierNamePEOAttributeTimestamp75 | — |
| ATTRIBUTE_TIMESTAMP7 | SupplierNamePEOAttributeTimestamp73 | — |
| ATTRIBUTE_TIMESTAMP8 | POSupplierNamePEOAttributeTimestamp85 | — |
| ATTRIBUTE_TIMESTAMP8 | SupplierNamePEOAttributeTimestamp83 | — |
| ATTRIBUTE_TIMESTAMP9 | POSupplierNamePEOAttributeTimestamp95 | — |
| ATTRIBUTE_TIMESTAMP9 | SupplierNamePEOAttributeTimestamp93 | — |
| AWT_GROUP_ID | POSupplierNamePEOAwtGroupId1 | — |
| AWT_GROUP_ID | SupplierNamePEOAwtGroupId | — |
| BUSINESS_RELATIONSHIP | POSupplierNamePEOBusinessRelationship1 | — |
| BUSINESS_RELATIONSHIP | SupplierNamePEOBusinessRelationship | — |
| CORPORATE_WEBSITE | POSupplierNamePEOCorporateWebsite1 | — |
| CORPORATE_WEBSITE | SupplierNamePEOCorporateWebsite | — |
| CREATED_BY | POSupplierNamePEOCreatedBy12 | — |
| CREATED_BY | SupplierNamePEOCreatedBy10 | — |
| CREATION_DATE | POSupplierNamePEOCreationDate12 | — |
| CREATION_DATE | SupplierNamePEOCreationDate10 | — |
| CUSTOMER_NUM | POSupplierNamePEOCustomerNum2 | — |
| CUSTOMER_NUM | SupplierNamePEOCustomerNum | — |
| DUNS_NUMBER_C | POSupplierNamePEODunsNumberC1 | — |
| DUNS_NUMBER_C | SupplierNamePEODunsNumberC | — |
| END_DATE_ACTIVE | POSupplierNamePEOEndDateActive1 | — |
| END_DATE_ACTIVE | SupplierNamePEOEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | POSupplierNamePEOFederalReportableFlag1 | — |
| FEDERAL_REPORTABLE_FLAG | SupplierNamePEOFederalReportableFlag | — |
| GLOBAL_ATTRIBUTE1 | POSupplierNamePEOGlobalAttribute127 | — |
| GLOBAL_ATTRIBUTE1 | SupplierNamePEOGlobalAttribute118 | — |
| GLOBAL_ATTRIBUTE10 | POSupplierNamePEOGlobalAttribute107 | — |
| GLOBAL_ATTRIBUTE10 | SupplierNamePEOGlobalAttribute105 | — |
| GLOBAL_ATTRIBUTE11 | POSupplierNamePEOGlobalAttribute1111 | — |
| GLOBAL_ATTRIBUTE11 | SupplierNamePEOGlobalAttribute119 | — |
| GLOBAL_ATTRIBUTE12 | POSupplierNamePEOGlobalAttribute128 | — |
| GLOBAL_ATTRIBUTE12 | SupplierNamePEOGlobalAttribute125 | — |
| GLOBAL_ATTRIBUTE13 | POSupplierNamePEOGlobalAttribute137 | — |
| GLOBAL_ATTRIBUTE13 | SupplierNamePEOGlobalAttribute135 | — |
| GLOBAL_ATTRIBUTE14 | POSupplierNamePEOGlobalAttribute147 | — |
| GLOBAL_ATTRIBUTE14 | SupplierNamePEOGlobalAttribute145 | — |
| GLOBAL_ATTRIBUTE15 | POSupplierNamePEOGlobalAttribute157 | — |
| GLOBAL_ATTRIBUTE15 | SupplierNamePEOGlobalAttribute155 | — |
| GLOBAL_ATTRIBUTE16 | POSupplierNamePEOGlobalAttribute167 | — |
| GLOBAL_ATTRIBUTE16 | SupplierNamePEOGlobalAttribute165 | — |
| GLOBAL_ATTRIBUTE17 | POSupplierNamePEOGlobalAttribute177 | — |
| GLOBAL_ATTRIBUTE17 | SupplierNamePEOGlobalAttribute175 | — |
| GLOBAL_ATTRIBUTE18 | POSupplierNamePEOGlobalAttribute187 | — |
| GLOBAL_ATTRIBUTE18 | SupplierNamePEOGlobalAttribute185 | — |
| GLOBAL_ATTRIBUTE19 | POSupplierNamePEOGlobalAttribute197 | — |
| GLOBAL_ATTRIBUTE19 | SupplierNamePEOGlobalAttribute195 | — |
| GLOBAL_ATTRIBUTE2 | POSupplierNamePEOGlobalAttribute27 | — |
| GLOBAL_ATTRIBUTE2 | SupplierNamePEOGlobalAttribute25 | — |
| GLOBAL_ATTRIBUTE20 | POSupplierNamePEOGlobalAttribute207 | — |
| GLOBAL_ATTRIBUTE20 | SupplierNamePEOGlobalAttribute205 | — |
| GLOBAL_ATTRIBUTE3 | POSupplierNamePEOGlobalAttribute37 | — |
| GLOBAL_ATTRIBUTE3 | SupplierNamePEOGlobalAttribute35 | — |
| GLOBAL_ATTRIBUTE4 | POSupplierNamePEOGlobalAttribute47 | — |
| GLOBAL_ATTRIBUTE4 | SupplierNamePEOGlobalAttribute45 | — |
| GLOBAL_ATTRIBUTE5 | POSupplierNamePEOGlobalAttribute57 | — |
| GLOBAL_ATTRIBUTE5 | SupplierNamePEOGlobalAttribute55 | — |
| GLOBAL_ATTRIBUTE6 | POSupplierNamePEOGlobalAttribute67 | — |
| GLOBAL_ATTRIBUTE6 | SupplierNamePEOGlobalAttribute65 | — |
| GLOBAL_ATTRIBUTE7 | POSupplierNamePEOGlobalAttribute77 | — |
| GLOBAL_ATTRIBUTE7 | SupplierNamePEOGlobalAttribute75 | — |
| GLOBAL_ATTRIBUTE8 | POSupplierNamePEOGlobalAttribute87 | — |
| GLOBAL_ATTRIBUTE8 | SupplierNamePEOGlobalAttribute85 | — |
| GLOBAL_ATTRIBUTE9 | POSupplierNamePEOGlobalAttribute97 | — |
| GLOBAL_ATTRIBUTE9 | SupplierNamePEOGlobalAttribute95 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | POSupplierNamePEOGlobalAttributeCategory7 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierNamePEOGlobalAttributeCategory5 | — |
| GLOBAL_ATTRIBUTE_DATE1 | POSupplierNamePEOGlobalAttributeDate14 | — |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierNamePEOGlobalAttributeDate12 | — |
| GLOBAL_ATTRIBUTE_DATE10 | POSupplierNamePEOGlobalAttributeDate102 | — |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierNamePEOGlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | POSupplierNamePEOGlobalAttributeDate24 | — |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierNamePEOGlobalAttributeDate22 | — |
| GLOBAL_ATTRIBUTE_DATE3 | POSupplierNamePEOGlobalAttributeDate34 | — |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierNamePEOGlobalAttributeDate32 | — |
| GLOBAL_ATTRIBUTE_DATE4 | POSupplierNamePEOGlobalAttributeDate44 | — |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierNamePEOGlobalAttributeDate42 | — |
| GLOBAL_ATTRIBUTE_DATE5 | POSupplierNamePEOGlobalAttributeDate54 | — |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierNamePEOGlobalAttributeDate52 | — |
| GLOBAL_ATTRIBUTE_DATE6 | POSupplierNamePEOGlobalAttributeDate62 | — |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierNamePEOGlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | POSupplierNamePEOGlobalAttributeDate72 | — |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierNamePEOGlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | POSupplierNamePEOGlobalAttributeDate82 | — |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierNamePEOGlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | POSupplierNamePEOGlobalAttributeDate92 | — |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierNamePEOGlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | POSupplierNamePEOGlobalAttributeNumber14 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierNamePEOGlobalAttributeNumber12 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | POSupplierNamePEOGlobalAttributeNumber102 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierNamePEOGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | POSupplierNamePEOGlobalAttributeNumber24 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierNamePEOGlobalAttributeNumber22 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | POSupplierNamePEOGlobalAttributeNumber34 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierNamePEOGlobalAttributeNumber32 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | POSupplierNamePEOGlobalAttributeNumber44 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierNamePEOGlobalAttributeNumber42 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | POSupplierNamePEOGlobalAttributeNumber54 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierNamePEOGlobalAttributeNumber52 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | POSupplierNamePEOGlobalAttributeNumber62 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierNamePEOGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | POSupplierNamePEOGlobalAttributeNumber72 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierNamePEOGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | POSupplierNamePEOGlobalAttributeNumber82 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierNamePEOGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | POSupplierNamePEOGlobalAttributeNumber92 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierNamePEOGlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | POSupplierNamePEOGlobalAttributeTimestamp12 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierNamePEOGlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | POSupplierNamePEOGlobalAttributeTimestamp102 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierNamePEOGlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | POSupplierNamePEOGlobalAttributeTimestamp22 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierNamePEOGlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | POSupplierNamePEOGlobalAttributeTimestamp32 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierNamePEOGlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | POSupplierNamePEOGlobalAttributeTimestamp42 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierNamePEOGlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | POSupplierNamePEOGlobalAttributeTimestamp52 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierNamePEOGlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | POSupplierNamePEOGlobalAttributeTimestamp62 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierNamePEOGlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | POSupplierNamePEOGlobalAttributeTimestamp72 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierNamePEOGlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | POSupplierNamePEOGlobalAttributeTimestamp82 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierNamePEOGlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | POSupplierNamePEOGlobalAttributeTimestamp92 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierNamePEOGlobalAttributeTimestamp9 | — |
| LAST_UPDATE_DATE | POSupplierNamePEOLastUpdateDate12 | — |
| LAST_UPDATE_DATE | SupplierNamePEOLastUpdateDate10 | — |
| LAST_UPDATE_LOGIN | POSupplierNamePEOLastUpdateLogin12 | — |
| LAST_UPDATE_LOGIN | SupplierNamePEOLastUpdateLogin10 | — |
| LAST_UPDATED_BY | POSupplierNamePEOLastUpdatedBy12 | — |
| LAST_UPDATED_BY | SupplierNamePEOLastUpdatedBy10 | — |
| MINORITY_GROUP_LOOKUP_CODE | POSupplierNamePEOMinorityGroupLookupCode1 | — |
| MINORITY_GROUP_LOOKUP_CODE | SupplierNamePEOMinorityGroupLookupCode | — |
| NAME_CONTROL | POSupplierNamePEONameControl1 | — |
| NAME_CONTROL | SupplierNamePEONameControl | — |
| NI_NUMBER | POSupplierNamePEONiNumber1 | — |
| NI_NUMBER | SupplierNamePEONiNumber | — |
| OBJECT_VERSION_NUMBER | POSupplierNamePEOObjectVersionNumber12 | — |
| OBJECT_VERSION_NUMBER | SupplierNamePEOObjectVersionNumber10 | — |
| ONE_TIME_FLAG | POSupplierNamePEOOneTimeFlag1 | — |
| ONE_TIME_FLAG | SupplierNamePEOOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | POSupplierNamePEOOrganizationTypeLookupCode1 | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierNamePEOOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | POSupplierNamePEOParentPartyId1 | — |
| PARENT_PARTY_ID | SupplierNamePEOParentPartyId | — |
| PARENT_VENDOR_ID | POSupplierNamePEOParentVendorId1 | — |
| PARENT_VENDOR_ID | SupplierNamePEOParentVendorId | — |
| PARTY_ID | POSupplierNamePEOPartyId1 | — |
| PARTY_ID | SupplierNamePEOPartyId | — |
| PROGRAM_APPLICATION_ID | POSupplierNamePEOProgramApplicationId2 | — |
| PROGRAM_APPLICATION_ID | SupplierNamePEOProgramApplicationId | — |
| PROGRAM_ID | POSupplierNamePEOProgramId2 | — |
| PROGRAM_ID | SupplierNamePEOProgramId | — |
| PROGRAM_UPDATE_DATE | POSupplierNamePEOProgramUpdateDate2 | — |
| PROGRAM_UPDATE_DATE | SupplierNamePEOProgramUpdateDate | — |
| REBUILD_INDEX | POSupplierNamePEORebuildIndex2 | — |
| REBUILD_INDEX | SupplierNamePEORebuildIndex1 | — |
| REQUEST_ID | POSupplierNamePEORequestId12 | — |
| REQUEST_ID | SupplierNamePEORequestId10 | — |
| SEGMENT1 | POSupplierNamePEOSegment12 | ✅ |
| SEGMENT1 | SupplierNamePEOSegment11 | — |
| SMALL_BUSINESS_FLAG | POSupplierNamePEOSmallBusinessFlag1 | — |
| SMALL_BUSINESS_FLAG | SupplierNamePEOSmallBusinessFlag | — |
| SPEND_AUTH_JUSTIFICATION | POSupplierNamePEOSpendAuthJustification1 | — |
| SPEND_AUTH_JUSTIFICATION | SupplierNamePEOSpendAuthJustification | — |
| SPEND_AUTH_REVIEW_STATUS | POSupplierNamePEOSpendAuthReviewStatus1 | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierNamePEOSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | POSupplierNamePEOStandardIndustryClass1 | — |
| STANDARD_INDUSTRY_CLASS | SupplierNamePEOStandardIndustryClass | — |
| START_DATE_ACTIVE | POSupplierNamePEOStartDateActive1 | — |
| START_DATE_ACTIVE | SupplierNamePEOStartDateActive | — |
| STATE_REPORTABLE_FLAG | POSupplierNamePEOStateReportableFlag1 | — |
| STATE_REPORTABLE_FLAG | SupplierNamePEOStateReportableFlag | — |
| TAX_REPORTING_NAME | POSupplierNamePEOTaxReportingName1 | — |
| TAX_REPORTING_NAME | SupplierNamePEOTaxReportingName | — |
| TAX_VERIFICATION_DATE | POSupplierNamePEOTaxVerificationDate1 | — |
| TAX_VERIFICATION_DATE | SupplierNamePEOTaxVerificationDate | — |
| TYPE_1099 | POSupplierNamePEOType10992 | — |
| TYPE_1099 | SupplierNamePEOType10991 | — |
| VENDOR_ID | POSupplierNamePEOVendorId5 | — |
| VENDOR_ID | SupplierNamePEOVendorId3 | — |
| VENDOR_NAME | POSupplierNamePEOVendorName1 | ✅ |
| VENDOR_NAME | SupplierNamePEOVendorName | ✅ |
| VENDOR_NAME_ALT | POSupplierNamePEOVendorNameAlt1 | — |
| VENDOR_NAME_ALT | SupplierNamePEOVendorNameAlt | — |
| VENDOR_TYPE_LOOKUP_CODE | POSupplierNamePEOVendorTypeLookupCode1 | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierNamePEOVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | POSupplierNamePEOWithholdingStartDate1 | — |
| WITHHOLDING_START_DATE | SupplierNamePEOWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | POSupplierNamePEOWithholdingStatusLookupCode1 | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierNamePEOWithholdingStatusLookupCode | — |
| WOMEN_OWNED_FLAG | POSupplierNamePEOWomenOwnedFlag1 | — |
| WOMEN_OWNED_FLAG | SupplierNamePEOWomenOwnedFlag | — |

### [[maintenanceworkorderpvo|MaintenanceWorkOrderPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| VENDOR_ID | WarrantySupplierViewPEOVendorId | — |
| VENDOR_NAME | WarrantySupplierViewPEOVendorName | — |

### [[negotiationsupplieractivityp1|NegotiationSupplierActivityP1]] (PO · BICC: 148/149)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SVEOAllowAwtFlag | ✅ |
| ATTRIBUTE1 | SVEOAttribute110 | ✅ |
| ATTRIBUTE10 | SVEOAttribute101 | ✅ |
| ATTRIBUTE11 | SVEOAttribute111 | ✅ |
| ATTRIBUTE12 | SVEOAttribute121 | ✅ |
| ATTRIBUTE13 | SVEOAttribute131 | ✅ |
| ATTRIBUTE14 | SVEOAttribute141 | ✅ |
| ATTRIBUTE15 | SVEOAttribute151 | ✅ |
| ATTRIBUTE16 | SVEOAttribute161 | ✅ |
| ATTRIBUTE17 | SVEOAttribute171 | ✅ |
| ATTRIBUTE18 | SVEOAttribute181 | ✅ |
| ATTRIBUTE19 | SVEOAttribute191 | ✅ |
| ATTRIBUTE2 | SVEOAttribute210 | ✅ |
| ATTRIBUTE20 | SVEOAttribute201 | ✅ |
| ATTRIBUTE3 | SVEOAttribute31 | ✅ |
| ATTRIBUTE4 | SVEOAttribute41 | ✅ |
| ATTRIBUTE5 | SVEOAttribute51 | ✅ |
| ATTRIBUTE6 | SVEOAttribute61 | ✅ |
| ATTRIBUTE7 | SVEOAttribute71 | ✅ |
| ATTRIBUTE8 | SVEOAttribute81 | ✅ |
| ATTRIBUTE9 | SVEOAttribute91 | ✅ |
| ATTRIBUTE_CATEGORY | SVEOAttributeCategory1 | ✅ |
| ATTRIBUTE_DATE1 | SVEOAttributeDate13 | ✅ |
| ATTRIBUTE_DATE10 | SVEOAttributeDate101 | ✅ |
| ATTRIBUTE_DATE2 | SVEOAttributeDate21 | ✅ |
| ATTRIBUTE_DATE3 | SVEOAttributeDate31 | ✅ |
| ATTRIBUTE_DATE4 | SVEOAttributeDate41 | ✅ |
| ATTRIBUTE_DATE5 | SVEOAttributeDate51 | ✅ |
| ATTRIBUTE_DATE6 | SVEOAttributeDate61 | ✅ |
| ATTRIBUTE_DATE7 | SVEOAttributeDate71 | ✅ |
| ATTRIBUTE_DATE8 | SVEOAttributeDate81 | ✅ |
| ATTRIBUTE_DATE9 | SVEOAttributeDate91 | ✅ |
| ATTRIBUTE_NUMBER1 | SVEOAttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER10 | SVEOAttributeNumber101 | ✅ |
| ATTRIBUTE_NUMBER2 | SVEOAttributeNumber21 | ✅ |
| ATTRIBUTE_NUMBER3 | SVEOAttributeNumber31 | ✅ |
| ATTRIBUTE_NUMBER4 | SVEOAttributeNumber41 | ✅ |
| ATTRIBUTE_NUMBER5 | SVEOAttributeNumber51 | ✅ |
| ATTRIBUTE_NUMBER6 | SVEOAttributeNumber61 | ✅ |
| ATTRIBUTE_NUMBER7 | SVEOAttributeNumber71 | ✅ |
| ATTRIBUTE_NUMBER8 | SVEOAttributeNumber81 | ✅ |
| ATTRIBUTE_NUMBER9 | SVEOAttributeNumber91 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | SVEOAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | SVEOAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | SVEOAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | SVEOAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | SVEOAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | SVEOAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | SVEOAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | SVEOAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | SVEOAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | SVEOAttributeTimestamp9 | ✅ |
| AWT_GROUP_ID | SVEOAwtGroupId | ✅ |
| BANK_CHARGE_BEARER | SVEOBankChargeBearer | ✅ |
| BUSINESS_RELATIONSHIP | SVEOBusinessRelationship | ✅ |
| CORPORATE_WEBSITE | SVEOCorporateWebsite | ✅ |
| CREATED_BY | SVEOCreatedBy2 | ✅ |
| CREATION_DATE | SVEOCreationDate2 | ✅ |
| CUSTOMER_NUM | SVEOCustomerNum | ✅ |
| DUNS_NUMBER_C | SVEODunsNumberC1 | ✅ |
| ENABLED_FLAG | SVEOEnabledFlag | ✅ |
| END_DATE_ACTIVE | SVEOEndDateActive | ✅ |
| FEDERAL_REPORTABLE_FLAG | SVEOFederalReportableFlag | ✅ |
| GLOBAL_ATTRIBUTE1 | SVEOGlobalAttribute1 | ✅ |
| GLOBAL_ATTRIBUTE10 | SVEOGlobalAttribute10 | ✅ |
| GLOBAL_ATTRIBUTE11 | SVEOGlobalAttribute11 | ✅ |
| GLOBAL_ATTRIBUTE12 | SVEOGlobalAttribute12 | ✅ |
| GLOBAL_ATTRIBUTE13 | SVEOGlobalAttribute13 | ✅ |
| GLOBAL_ATTRIBUTE14 | SVEOGlobalAttribute14 | ✅ |
| GLOBAL_ATTRIBUTE15 | SVEOGlobalAttribute15 | ✅ |
| GLOBAL_ATTRIBUTE16 | SVEOGlobalAttribute16 | ✅ |
| GLOBAL_ATTRIBUTE17 | SVEOGlobalAttribute17 | ✅ |
| GLOBAL_ATTRIBUTE18 | SVEOGlobalAttribute18 | ✅ |
| GLOBAL_ATTRIBUTE19 | SVEOGlobalAttribute19 | ✅ |
| GLOBAL_ATTRIBUTE2 | SVEOGlobalAttribute2 | ✅ |
| GLOBAL_ATTRIBUTE20 | SVEOGlobalAttribute20 | ✅ |
| GLOBAL_ATTRIBUTE3 | SVEOGlobalAttribute3 | ✅ |
| GLOBAL_ATTRIBUTE4 | SVEOGlobalAttribute4 | ✅ |
| GLOBAL_ATTRIBUTE5 | SVEOGlobalAttribute5 | ✅ |
| GLOBAL_ATTRIBUTE6 | SVEOGlobalAttribute6 | ✅ |
| GLOBAL_ATTRIBUTE7 | SVEOGlobalAttribute7 | ✅ |
| GLOBAL_ATTRIBUTE8 | SVEOGlobalAttribute8 | ✅ |
| GLOBAL_ATTRIBUTE9 | SVEOGlobalAttribute9 | ✅ |
| GLOBAL_ATTRIBUTE_CATEGORY | SVEOGlobalAttributeCategory | ✅ |
| GLOBAL_ATTRIBUTE_DATE1 | SVEOGlobalAttributeDate1 | ✅ |
| GLOBAL_ATTRIBUTE_DATE10 | SVEOGlobalAttributeDate10 | ✅ |
| GLOBAL_ATTRIBUTE_DATE2 | SVEOGlobalAttributeDate2 | ✅ |
| GLOBAL_ATTRIBUTE_DATE3 | SVEOGlobalAttributeDate3 | ✅ |
| GLOBAL_ATTRIBUTE_DATE4 | SVEOGlobalAttributeDate4 | ✅ |
| GLOBAL_ATTRIBUTE_DATE5 | SVEOGlobalAttributeDate5 | ✅ |
| GLOBAL_ATTRIBUTE_DATE6 | SVEOGlobalAttributeDate6 | ✅ |
| GLOBAL_ATTRIBUTE_DATE7 | SVEOGlobalAttributeDate7 | ✅ |
| GLOBAL_ATTRIBUTE_DATE8 | SVEOGlobalAttributeDate8 | ✅ |
| GLOBAL_ATTRIBUTE_DATE9 | SVEOGlobalAttributeDate9 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER1 | SVEOGlobalAttributeNumber1 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER10 | SVEOGlobalAttributeNumber10 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER2 | SVEOGlobalAttributeNumber2 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER3 | SVEOGlobalAttributeNumber3 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER4 | SVEOGlobalAttributeNumber4 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER5 | SVEOGlobalAttributeNumber5 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER6 | SVEOGlobalAttributeNumber6 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER7 | SVEOGlobalAttributeNumber7 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER8 | SVEOGlobalAttributeNumber8 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER9 | SVEOGlobalAttributeNumber9 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SVEOGlobalAttributeTimestamp1 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SVEOGlobalAttributeTimestamp10 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SVEOGlobalAttributeTimestamp2 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SVEOGlobalAttributeTimestamp3 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SVEOGlobalAttributeTimestamp4 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SVEOGlobalAttributeTimestamp5 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SVEOGlobalAttributeTimestamp6 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SVEOGlobalAttributeTimestamp7 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SVEOGlobalAttributeTimestamp8 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SVEOGlobalAttributeTimestamp9 | ✅ |
| LAST_UPDATE_DATE | SVEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | SVEOLastUpdateLogin2 | ✅ |
| LAST_UPDATED_BY | SVEOLastUpdatedBy2 | ✅ |
| MIN_ORDER_AMOUNT | SVEOMinOrderAmount | ✅ |
| MINORITY_GROUP_LOOKUP_CODE | SVEOMinorityGroupLookupCode | ✅ |
| NAME_CONTROL | SVEONameControl | ✅ |
| NI_NUMBER | SVEONiNumber | ✅ |
| OBJECT_VERSION_NUMBER | SVEOObjectVersionNumber2 | ✅ |
| ONE_TIME_FLAG | SVEOOneTimeFlag | ✅ |
| ORGANIZATION_TYPE_LOOKUP_CODE | SVEOOrganizationTypeLookupCode | ✅ |
| PARENT_PARTY_ID | SVEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | SVEOParentVendorId | ✅ |
| PARTY_ID | SVEOPartyId1 | ✅ |
| PROGRAM_APPLICATION_ID | SVEOProgramApplicationId | ✅ |
| PROGRAM_ID | SVEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | SVEOProgramUpdateDate | ✅ |
| REQUEST_ID | SVEORequestId1 | ✅ |
| SEGMENT1 | SVEOSegment1 | ✅ |
| SET_OF_BOOKS_ID | SVEOSetOfBooksId | ✅ |
| SMALL_BUSINESS_FLAG | SVEOSmallBusinessFlag | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SVEOSpendAuthReviewStatus | ✅ |
| STANDARD_INDUSTRY_CLASS | SVEOStandardIndustryClass | ✅ |
| START_DATE_ACTIVE | SVEOStartDateActive | ✅ |
| STATE_REPORTABLE_FLAG | SVEOStateReportableFlag | ✅ |
| SUMMARY_FLAG | SVEOSummaryFlag | ✅ |
| TAX_REPORTING_NAME | SVEOTaxReportingName | ✅ |
| TAX_VERIFICATION_DATE | SVEOTaxVerificationDate | ✅ |
| TYPE_1099 | SVEOType1099 | ✅ |
| VENDOR_ID | SVEOVendorId | ✅ |
| VENDOR_NAME | SVEOVendorName | ✅ |
| VENDOR_NAME_ALT | SVEOVendorNameAlt | — |
| VENDOR_TYPE_LOOKUP_CODE | SVEOVendorTypeLookupCode | ✅ |
| WITHHOLDING_START_DATE | SVEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | SVEOWithholdingStatusLookupCode | ✅ |
| WOMEN_OWNED_FLAG | SVEOWomenOwnedFlag | ✅ |

### [[negotiationsupplieractivitypvo|NegotiationSupplierActivityPVO]] (PO · BICC: 148/148)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SVEOAllowAwtFlag | ✅ |
| ATTRIBUTE1 | SVEOAttribute110 | ✅ |
| ATTRIBUTE10 | SVEOAttribute101 | ✅ |
| ATTRIBUTE11 | SVEOAttribute111 | ✅ |
| ATTRIBUTE12 | SVEOAttribute121 | ✅ |
| ATTRIBUTE13 | SVEOAttribute131 | ✅ |
| ATTRIBUTE14 | SVEOAttribute141 | ✅ |
| ATTRIBUTE15 | SVEOAttribute151 | ✅ |
| ATTRIBUTE16 | SVEOAttribute161 | ✅ |
| ATTRIBUTE17 | SVEOAttribute171 | ✅ |
| ATTRIBUTE18 | SVEOAttribute181 | ✅ |
| ATTRIBUTE19 | SVEOAttribute191 | ✅ |
| ATTRIBUTE2 | SVEOAttribute210 | ✅ |
| ATTRIBUTE20 | SVEOAttribute201 | ✅ |
| ATTRIBUTE3 | SVEOAttribute31 | ✅ |
| ATTRIBUTE4 | SVEOAttribute41 | ✅ |
| ATTRIBUTE5 | SVEOAttribute51 | ✅ |
| ATTRIBUTE6 | SVEOAttribute61 | ✅ |
| ATTRIBUTE7 | SVEOAttribute71 | ✅ |
| ATTRIBUTE8 | SVEOAttribute81 | ✅ |
| ATTRIBUTE9 | SVEOAttribute91 | ✅ |
| ATTRIBUTE_CATEGORY | SVEOAttributeCategory1 | ✅ |
| ATTRIBUTE_DATE1 | SVEOAttributeDate13 | ✅ |
| ATTRIBUTE_DATE10 | SVEOAttributeDate101 | ✅ |
| ATTRIBUTE_DATE2 | SVEOAttributeDate21 | ✅ |
| ATTRIBUTE_DATE3 | SVEOAttributeDate31 | ✅ |
| ATTRIBUTE_DATE4 | SVEOAttributeDate41 | ✅ |
| ATTRIBUTE_DATE5 | SVEOAttributeDate51 | ✅ |
| ATTRIBUTE_DATE6 | SVEOAttributeDate61 | ✅ |
| ATTRIBUTE_DATE7 | SVEOAttributeDate71 | ✅ |
| ATTRIBUTE_DATE8 | SVEOAttributeDate81 | ✅ |
| ATTRIBUTE_DATE9 | SVEOAttributeDate91 | ✅ |
| ATTRIBUTE_NUMBER1 | SVEOAttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER10 | SVEOAttributeNumber101 | ✅ |
| ATTRIBUTE_NUMBER2 | SVEOAttributeNumber21 | ✅ |
| ATTRIBUTE_NUMBER3 | SVEOAttributeNumber31 | ✅ |
| ATTRIBUTE_NUMBER4 | SVEOAttributeNumber41 | ✅ |
| ATTRIBUTE_NUMBER5 | SVEOAttributeNumber51 | ✅ |
| ATTRIBUTE_NUMBER6 | SVEOAttributeNumber61 | ✅ |
| ATTRIBUTE_NUMBER7 | SVEOAttributeNumber71 | ✅ |
| ATTRIBUTE_NUMBER8 | SVEOAttributeNumber81 | ✅ |
| ATTRIBUTE_NUMBER9 | SVEOAttributeNumber91 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | SVEOAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | SVEOAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | SVEOAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | SVEOAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | SVEOAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | SVEOAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | SVEOAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | SVEOAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | SVEOAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | SVEOAttributeTimestamp9 | ✅ |
| AWT_GROUP_ID | SVEOAwtGroupId | ✅ |
| BANK_CHARGE_BEARER | SVEOBankChargeBearer | ✅ |
| BUSINESS_RELATIONSHIP | SVEOBusinessRelationship | ✅ |
| CORPORATE_WEBSITE | SVEOCorporateWebsite | ✅ |
| CREATED_BY | SVEOCreatedBy2 | ✅ |
| CREATION_DATE | SVEOCreationDate2 | ✅ |
| CUSTOMER_NUM | SVEOCustomerNum | ✅ |
| DUNS_NUMBER_C | SVEODunsNumberC1 | ✅ |
| END_DATE_ACTIVE | SVEOEndDateActive | ✅ |
| FEDERAL_REPORTABLE_FLAG | SVEOFederalReportableFlag | ✅ |
| GLOBAL_ATTRIBUTE1 | SVEOGlobalAttribute1 | ✅ |
| GLOBAL_ATTRIBUTE10 | SVEOGlobalAttribute10 | ✅ |
| GLOBAL_ATTRIBUTE11 | SVEOGlobalAttribute11 | ✅ |
| GLOBAL_ATTRIBUTE12 | SVEOGlobalAttribute12 | ✅ |
| GLOBAL_ATTRIBUTE13 | SVEOGlobalAttribute13 | ✅ |
| GLOBAL_ATTRIBUTE14 | SVEOGlobalAttribute14 | ✅ |
| GLOBAL_ATTRIBUTE15 | SVEOGlobalAttribute15 | ✅ |
| GLOBAL_ATTRIBUTE16 | SVEOGlobalAttribute16 | ✅ |
| GLOBAL_ATTRIBUTE17 | SVEOGlobalAttribute17 | ✅ |
| GLOBAL_ATTRIBUTE18 | SVEOGlobalAttribute18 | ✅ |
| GLOBAL_ATTRIBUTE19 | SVEOGlobalAttribute19 | ✅ |
| GLOBAL_ATTRIBUTE2 | SVEOGlobalAttribute2 | ✅ |
| GLOBAL_ATTRIBUTE20 | SVEOGlobalAttribute20 | ✅ |
| GLOBAL_ATTRIBUTE3 | SVEOGlobalAttribute3 | ✅ |
| GLOBAL_ATTRIBUTE4 | SVEOGlobalAttribute4 | ✅ |
| GLOBAL_ATTRIBUTE5 | SVEOGlobalAttribute5 | ✅ |
| GLOBAL_ATTRIBUTE6 | SVEOGlobalAttribute6 | ✅ |
| GLOBAL_ATTRIBUTE7 | SVEOGlobalAttribute7 | ✅ |
| GLOBAL_ATTRIBUTE8 | SVEOGlobalAttribute8 | ✅ |
| GLOBAL_ATTRIBUTE9 | SVEOGlobalAttribute9 | ✅ |
| GLOBAL_ATTRIBUTE_CATEGORY | SVEOGlobalAttributeCategory | ✅ |
| GLOBAL_ATTRIBUTE_DATE1 | SVEOGlobalAttributeDate1 | ✅ |
| GLOBAL_ATTRIBUTE_DATE10 | SVEOGlobalAttributeDate10 | ✅ |
| GLOBAL_ATTRIBUTE_DATE2 | SVEOGlobalAttributeDate2 | ✅ |
| GLOBAL_ATTRIBUTE_DATE3 | SVEOGlobalAttributeDate3 | ✅ |
| GLOBAL_ATTRIBUTE_DATE4 | SVEOGlobalAttributeDate4 | ✅ |
| GLOBAL_ATTRIBUTE_DATE5 | SVEOGlobalAttributeDate5 | ✅ |
| GLOBAL_ATTRIBUTE_DATE6 | SVEOGlobalAttributeDate6 | ✅ |
| GLOBAL_ATTRIBUTE_DATE7 | SVEOGlobalAttributeDate7 | ✅ |
| GLOBAL_ATTRIBUTE_DATE8 | SVEOGlobalAttributeDate8 | ✅ |
| GLOBAL_ATTRIBUTE_DATE9 | SVEOGlobalAttributeDate9 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER1 | SVEOGlobalAttributeNumber1 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER10 | SVEOGlobalAttributeNumber10 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER2 | SVEOGlobalAttributeNumber2 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER3 | SVEOGlobalAttributeNumber3 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER4 | SVEOGlobalAttributeNumber4 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER5 | SVEOGlobalAttributeNumber5 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER6 | SVEOGlobalAttributeNumber6 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER7 | SVEOGlobalAttributeNumber7 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER8 | SVEOGlobalAttributeNumber8 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER9 | SVEOGlobalAttributeNumber9 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SVEOGlobalAttributeTimestamp1 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SVEOGlobalAttributeTimestamp10 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SVEOGlobalAttributeTimestamp2 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SVEOGlobalAttributeTimestamp3 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SVEOGlobalAttributeTimestamp4 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SVEOGlobalAttributeTimestamp5 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SVEOGlobalAttributeTimestamp6 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SVEOGlobalAttributeTimestamp7 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SVEOGlobalAttributeTimestamp8 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SVEOGlobalAttributeTimestamp9 | ✅ |
| LAST_UPDATE_DATE | SVEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | SVEOLastUpdateLogin2 | ✅ |
| LAST_UPDATED_BY | SVEOLastUpdatedBy2 | ✅ |
| MIN_ORDER_AMOUNT | SVEOMinOrderAmount | ✅ |
| MINORITY_GROUP_LOOKUP_CODE | SVEOMinorityGroupLookupCode | ✅ |
| NAME_CONTROL | SVEONameControl | ✅ |
| NI_NUMBER | SVEONiNumber | ✅ |
| OBJECT_VERSION_NUMBER | SVEOObjectVersionNumber2 | ✅ |
| ONE_TIME_FLAG | SVEOOneTimeFlag | ✅ |
| ORGANIZATION_TYPE_LOOKUP_CODE | SVEOOrganizationTypeLookupCode | ✅ |
| PARENT_PARTY_ID | SVEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | SVEOParentVendorId | ✅ |
| PARTY_ID | SVEOPartyId1 | ✅ |
| PROGRAM_APPLICATION_ID | SVEOProgramApplicationId | ✅ |
| PROGRAM_ID | SVEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | SVEOProgramUpdateDate | ✅ |
| REQUEST_ID | SVEORequestId1 | ✅ |
| SEGMENT1 | SVEOSegment1 | ✅ |
| SET_OF_BOOKS_ID | SVEOSetOfBooksId | ✅ |
| SMALL_BUSINESS_FLAG | SVEOSmallBusinessFlag | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SVEOSpendAuthReviewStatus | ✅ |
| STANDARD_INDUSTRY_CLASS | SVEOStandardIndustryClass | ✅ |
| START_DATE_ACTIVE | SVEOStartDateActive | ✅ |
| STATE_REPORTABLE_FLAG | SVEOStateReportableFlag | ✅ |
| SUMMARY_FLAG | SVEOSummaryFlag | ✅ |
| TAX_REPORTING_NAME | SVEOTaxReportingName | ✅ |
| TAX_VERIFICATION_DATE | SVEOTaxVerificationDate | ✅ |
| TYPE_1099 | SVEOType1099 | ✅ |
| VENDOR_ID | SVEOVendorId | ✅ |
| VENDOR_NAME | SVEOVendorName | ✅ |
| VENDOR_NAME_ALT | SVEOVendorNameAlt | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SVEOVendorTypeLookupCode | ✅ |
| WITHHOLDING_START_DATE | SVEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | SVEOWithholdingStatusLookupCode | ✅ |
| WOMEN_OWNED_FLAG | SVEOWomenOwnedFlag | ✅ |

### [[supplierthirdpartypaymentpvo|SupplierThirdPartyPaymentPVO]] (PO · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| VENDOR_ID | VendorId | — |
| VENDOR_ID | VendorId2 | — |
| VENDOR_NAME | VendorName | ✅ |
| VENDOR_NAME | VendorName1 | ✅ |

### [[wooperationspvo|WOOperationsPVO]] (OTHER · BICC: 28/292)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | POSupplierNamePEOAllowAwtFlag1 | — |
| ALLOW_AWT_FLAG | SupplierNamePEOAllowAwtFlag | — |
| ATTRIBUTE1 | POSupplierNamePEOAttribute150 | — |
| ATTRIBUTE1 | SupplierNamePEOAttribute130 | — |
| ATTRIBUTE10 | POSupplierNamePEOAttribute1011 | — |
| ATTRIBUTE10 | SupplierNamePEOAttribute109 | — |
| ATTRIBUTE11 | POSupplierNamePEOAttribute1115 | — |
| ATTRIBUTE11 | SupplierNamePEOAttribute1113 | — |
| ATTRIBUTE12 | POSupplierNamePEOAttribute1213 | — |
| ATTRIBUTE12 | SupplierNamePEOAttribute1211 | — |
| ATTRIBUTE13 | POSupplierNamePEOAttribute1311 | — |
| ATTRIBUTE13 | SupplierNamePEOAttribute139 | — |
| ATTRIBUTE14 | POSupplierNamePEOAttribute1411 | — |
| ATTRIBUTE14 | SupplierNamePEOAttribute149 | — |
| ATTRIBUTE15 | POSupplierNamePEOAttribute1511 | — |
| ATTRIBUTE15 | SupplierNamePEOAttribute159 | — |
| ATTRIBUTE16 | POSupplierNamePEOAttribute1611 | — |
| ATTRIBUTE16 | SupplierNamePEOAttribute169 | — |
| ATTRIBUTE17 | POSupplierNamePEOAttribute1711 | — |
| ATTRIBUTE17 | SupplierNamePEOAttribute179 | — |
| ATTRIBUTE18 | POSupplierNamePEOAttribute1811 | — |
| ATTRIBUTE18 | SupplierNamePEOAttribute189 | — |
| ATTRIBUTE19 | POSupplierNamePEOAttribute1911 | — |
| ATTRIBUTE19 | SupplierNamePEOAttribute199 | — |
| ATTRIBUTE2 | POSupplierNamePEOAttribute211 | — |
| ATTRIBUTE2 | SupplierNamePEOAttribute29 | — |
| ATTRIBUTE20 | POSupplierNamePEOAttribute2011 | — |
| ATTRIBUTE20 | SupplierNamePEOAttribute209 | — |
| ATTRIBUTE3 | POSupplierNamePEOAttribute311 | — |
| ATTRIBUTE3 | SupplierNamePEOAttribute39 | — |
| ATTRIBUTE4 | POSupplierNamePEOAttribute411 | — |
| ATTRIBUTE4 | SupplierNamePEOAttribute49 | — |
| ATTRIBUTE5 | POSupplierNamePEOAttribute511 | — |
| ATTRIBUTE5 | SupplierNamePEOAttribute59 | — |
| ATTRIBUTE6 | POSupplierNamePEOAttribute611 | — |
| ATTRIBUTE6 | SupplierNamePEOAttribute69 | — |
| ATTRIBUTE7 | POSupplierNamePEOAttribute711 | — |
| ATTRIBUTE7 | SupplierNamePEOAttribute79 | — |
| ATTRIBUTE8 | POSupplierNamePEOAttribute811 | — |
| ATTRIBUTE8 | SupplierNamePEOAttribute89 | — |
| ATTRIBUTE9 | POSupplierNamePEOAttribute911 | — |
| ATTRIBUTE9 | SupplierNamePEOAttribute99 | — |
| ATTRIBUTE_CATEGORY | POSupplierNamePEOAttributeCategory11 | — |
| ATTRIBUTE_CATEGORY | SupplierNamePEOAttributeCategory9 | — |
| ATTRIBUTE_DATE1 | POSupplierNamePEOAttributeDate111 | — |
| ATTRIBUTE_DATE1 | SupplierNamePEOAttributeDate19 | — |
| ATTRIBUTE_DATE10 | POSupplierNamePEOAttributeDate105 | — |
| ATTRIBUTE_DATE10 | SupplierNamePEOAttributeDate103 | — |
| ATTRIBUTE_DATE2 | POSupplierNamePEOAttributeDate211 | — |
| ATTRIBUTE_DATE2 | SupplierNamePEOAttributeDate29 | — |
| ATTRIBUTE_DATE3 | POSupplierNamePEOAttributeDate311 | — |
| ATTRIBUTE_DATE3 | SupplierNamePEOAttributeDate39 | — |
| ATTRIBUTE_DATE4 | POSupplierNamePEOAttributeDate411 | — |
| ATTRIBUTE_DATE4 | SupplierNamePEOAttributeDate49 | — |
| ATTRIBUTE_DATE5 | POSupplierNamePEOAttributeDate511 | — |
| ATTRIBUTE_DATE5 | SupplierNamePEOAttributeDate59 | — |
| ATTRIBUTE_DATE6 | POSupplierNamePEOAttributeDate65 | — |
| ATTRIBUTE_DATE6 | SupplierNamePEOAttributeDate63 | — |
| ATTRIBUTE_DATE7 | POSupplierNamePEOAttributeDate75 | — |
| ATTRIBUTE_DATE7 | SupplierNamePEOAttributeDate73 | — |
| ATTRIBUTE_DATE8 | POSupplierNamePEOAttributeDate85 | — |
| ATTRIBUTE_DATE8 | SupplierNamePEOAttributeDate83 | — |
| ATTRIBUTE_DATE9 | POSupplierNamePEOAttributeDate95 | — |
| ATTRIBUTE_DATE9 | SupplierNamePEOAttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | POSupplierNamePEOAttributeNumber111 | — |
| ATTRIBUTE_NUMBER1 | SupplierNamePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER10 | POSupplierNamePEOAttributeNumber1011 | — |
| ATTRIBUTE_NUMBER10 | SupplierNamePEOAttributeNumber109 | — |
| ATTRIBUTE_NUMBER2 | POSupplierNamePEOAttributeNumber211 | — |
| ATTRIBUTE_NUMBER2 | SupplierNamePEOAttributeNumber29 | — |
| ATTRIBUTE_NUMBER3 | POSupplierNamePEOAttributeNumber311 | — |
| ATTRIBUTE_NUMBER3 | SupplierNamePEOAttributeNumber39 | — |
| ATTRIBUTE_NUMBER4 | POSupplierNamePEOAttributeNumber411 | — |
| ATTRIBUTE_NUMBER4 | SupplierNamePEOAttributeNumber49 | — |
| ATTRIBUTE_NUMBER5 | POSupplierNamePEOAttributeNumber511 | — |
| ATTRIBUTE_NUMBER5 | SupplierNamePEOAttributeNumber59 | — |
| ATTRIBUTE_NUMBER6 | POSupplierNamePEOAttributeNumber611 | — |
| ATTRIBUTE_NUMBER6 | SupplierNamePEOAttributeNumber69 | — |
| ATTRIBUTE_NUMBER7 | POSupplierNamePEOAttributeNumber711 | — |
| ATTRIBUTE_NUMBER7 | SupplierNamePEOAttributeNumber79 | — |
| ATTRIBUTE_NUMBER8 | POSupplierNamePEOAttributeNumber811 | — |
| ATTRIBUTE_NUMBER8 | SupplierNamePEOAttributeNumber89 | — |
| ATTRIBUTE_NUMBER9 | POSupplierNamePEOAttributeNumber911 | — |
| ATTRIBUTE_NUMBER9 | SupplierNamePEOAttributeNumber99 | — |
| ATTRIBUTE_TIMESTAMP1 | POSupplierNamePEOAttributeTimestamp111 | — |
| ATTRIBUTE_TIMESTAMP1 | SupplierNamePEOAttributeTimestamp19 | — |
| ATTRIBUTE_TIMESTAMP10 | POSupplierNamePEOAttributeTimestamp105 | — |
| ATTRIBUTE_TIMESTAMP10 | SupplierNamePEOAttributeTimestamp103 | — |
| ATTRIBUTE_TIMESTAMP2 | POSupplierNamePEOAttributeTimestamp211 | — |
| ATTRIBUTE_TIMESTAMP2 | SupplierNamePEOAttributeTimestamp29 | — |
| ATTRIBUTE_TIMESTAMP3 | POSupplierNamePEOAttributeTimestamp311 | — |
| ATTRIBUTE_TIMESTAMP3 | SupplierNamePEOAttributeTimestamp39 | — |
| ATTRIBUTE_TIMESTAMP4 | POSupplierNamePEOAttributeTimestamp411 | — |
| ATTRIBUTE_TIMESTAMP4 | SupplierNamePEOAttributeTimestamp49 | — |
| ATTRIBUTE_TIMESTAMP5 | POSupplierNamePEOAttributeTimestamp511 | — |
| ATTRIBUTE_TIMESTAMP5 | SupplierNamePEOAttributeTimestamp59 | — |
| ATTRIBUTE_TIMESTAMP6 | POSupplierNamePEOAttributeTimestamp65 | — |
| ATTRIBUTE_TIMESTAMP6 | SupplierNamePEOAttributeTimestamp63 | — |
| ATTRIBUTE_TIMESTAMP7 | POSupplierNamePEOAttributeTimestamp75 | — |
| ATTRIBUTE_TIMESTAMP7 | SupplierNamePEOAttributeTimestamp73 | — |
| ATTRIBUTE_TIMESTAMP8 | POSupplierNamePEOAttributeTimestamp85 | — |
| ATTRIBUTE_TIMESTAMP8 | SupplierNamePEOAttributeTimestamp83 | — |
| ATTRIBUTE_TIMESTAMP9 | POSupplierNamePEOAttributeTimestamp95 | — |
| ATTRIBUTE_TIMESTAMP9 | SupplierNamePEOAttributeTimestamp93 | — |
| AWT_GROUP_ID | POSupplierNamePEOAwtGroupId1 | ✅ |
| AWT_GROUP_ID | SupplierNamePEOAwtGroupId | ✅ |
| BUSINESS_RELATIONSHIP | POSupplierNamePEOBusinessRelationship1 | — |
| BUSINESS_RELATIONSHIP | SupplierNamePEOBusinessRelationship | — |
| CORPORATE_WEBSITE | POSupplierNamePEOCorporateWebsite1 | — |
| CORPORATE_WEBSITE | SupplierNamePEOCorporateWebsite | — |
| CREATED_BY | POSupplierNamePEOCreatedBy12 | — |
| CREATED_BY | SupplierNamePEOCreatedBy10 | — |
| CREATION_DATE | POSupplierNamePEOCreationDate12 | ✅ |
| CREATION_DATE | SupplierNamePEOCreationDate10 | ✅ |
| CUSTOMER_NUM | POSupplierNamePEOCustomerNum2 | — |
| CUSTOMER_NUM | SupplierNamePEOCustomerNum | — |
| DUNS_NUMBER_C | POSupplierNamePEODunsNumberC1 | — |
| DUNS_NUMBER_C | SupplierNamePEODunsNumberC | — |
| END_DATE_ACTIVE | POSupplierNamePEOEndDateActive1 | — |
| END_DATE_ACTIVE | SupplierNamePEOEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | POSupplierNamePEOFederalReportableFlag1 | — |
| FEDERAL_REPORTABLE_FLAG | SupplierNamePEOFederalReportableFlag | — |
| GLOBAL_ATTRIBUTE1 | POSupplierNamePEOGlobalAttribute127 | — |
| GLOBAL_ATTRIBUTE1 | SupplierNamePEOGlobalAttribute118 | — |
| GLOBAL_ATTRIBUTE10 | POSupplierNamePEOGlobalAttribute107 | — |
| GLOBAL_ATTRIBUTE10 | SupplierNamePEOGlobalAttribute105 | — |
| GLOBAL_ATTRIBUTE11 | POSupplierNamePEOGlobalAttribute1111 | — |
| GLOBAL_ATTRIBUTE11 | SupplierNamePEOGlobalAttribute119 | — |
| GLOBAL_ATTRIBUTE12 | POSupplierNamePEOGlobalAttribute128 | — |
| GLOBAL_ATTRIBUTE12 | SupplierNamePEOGlobalAttribute125 | — |
| GLOBAL_ATTRIBUTE13 | POSupplierNamePEOGlobalAttribute137 | — |
| GLOBAL_ATTRIBUTE13 | SupplierNamePEOGlobalAttribute135 | — |
| GLOBAL_ATTRIBUTE14 | POSupplierNamePEOGlobalAttribute147 | — |
| GLOBAL_ATTRIBUTE14 | SupplierNamePEOGlobalAttribute145 | — |
| GLOBAL_ATTRIBUTE15 | POSupplierNamePEOGlobalAttribute157 | — |
| GLOBAL_ATTRIBUTE15 | SupplierNamePEOGlobalAttribute155 | — |
| GLOBAL_ATTRIBUTE16 | POSupplierNamePEOGlobalAttribute167 | — |
| GLOBAL_ATTRIBUTE16 | SupplierNamePEOGlobalAttribute165 | — |
| GLOBAL_ATTRIBUTE17 | POSupplierNamePEOGlobalAttribute177 | — |
| GLOBAL_ATTRIBUTE17 | SupplierNamePEOGlobalAttribute175 | — |
| GLOBAL_ATTRIBUTE18 | POSupplierNamePEOGlobalAttribute187 | — |
| GLOBAL_ATTRIBUTE18 | SupplierNamePEOGlobalAttribute185 | — |
| GLOBAL_ATTRIBUTE19 | POSupplierNamePEOGlobalAttribute197 | — |
| GLOBAL_ATTRIBUTE19 | SupplierNamePEOGlobalAttribute195 | — |
| GLOBAL_ATTRIBUTE2 | POSupplierNamePEOGlobalAttribute27 | — |
| GLOBAL_ATTRIBUTE2 | SupplierNamePEOGlobalAttribute25 | — |
| GLOBAL_ATTRIBUTE20 | POSupplierNamePEOGlobalAttribute207 | — |
| GLOBAL_ATTRIBUTE20 | SupplierNamePEOGlobalAttribute205 | — |
| GLOBAL_ATTRIBUTE3 | POSupplierNamePEOGlobalAttribute37 | — |
| GLOBAL_ATTRIBUTE3 | SupplierNamePEOGlobalAttribute35 | — |
| GLOBAL_ATTRIBUTE4 | POSupplierNamePEOGlobalAttribute47 | — |
| GLOBAL_ATTRIBUTE4 | SupplierNamePEOGlobalAttribute45 | — |
| GLOBAL_ATTRIBUTE5 | POSupplierNamePEOGlobalAttribute57 | — |
| GLOBAL_ATTRIBUTE5 | SupplierNamePEOGlobalAttribute55 | — |
| GLOBAL_ATTRIBUTE6 | POSupplierNamePEOGlobalAttribute67 | — |
| GLOBAL_ATTRIBUTE6 | SupplierNamePEOGlobalAttribute65 | — |
| GLOBAL_ATTRIBUTE7 | POSupplierNamePEOGlobalAttribute77 | — |
| GLOBAL_ATTRIBUTE7 | SupplierNamePEOGlobalAttribute75 | — |
| GLOBAL_ATTRIBUTE8 | POSupplierNamePEOGlobalAttribute87 | — |
| GLOBAL_ATTRIBUTE8 | SupplierNamePEOGlobalAttribute85 | — |
| GLOBAL_ATTRIBUTE9 | POSupplierNamePEOGlobalAttribute97 | — |
| GLOBAL_ATTRIBUTE9 | SupplierNamePEOGlobalAttribute95 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | POSupplierNamePEOGlobalAttributeCategory7 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierNamePEOGlobalAttributeCategory5 | — |
| GLOBAL_ATTRIBUTE_DATE1 | POSupplierNamePEOGlobalAttributeDate14 | — |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierNamePEOGlobalAttributeDate12 | — |
| GLOBAL_ATTRIBUTE_DATE10 | POSupplierNamePEOGlobalAttributeDate102 | — |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierNamePEOGlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | POSupplierNamePEOGlobalAttributeDate24 | — |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierNamePEOGlobalAttributeDate22 | — |
| GLOBAL_ATTRIBUTE_DATE3 | POSupplierNamePEOGlobalAttributeDate34 | — |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierNamePEOGlobalAttributeDate32 | — |
| GLOBAL_ATTRIBUTE_DATE4 | POSupplierNamePEOGlobalAttributeDate44 | — |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierNamePEOGlobalAttributeDate42 | — |
| GLOBAL_ATTRIBUTE_DATE5 | POSupplierNamePEOGlobalAttributeDate54 | — |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierNamePEOGlobalAttributeDate52 | — |
| GLOBAL_ATTRIBUTE_DATE6 | POSupplierNamePEOGlobalAttributeDate62 | — |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierNamePEOGlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | POSupplierNamePEOGlobalAttributeDate72 | — |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierNamePEOGlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | POSupplierNamePEOGlobalAttributeDate82 | — |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierNamePEOGlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | POSupplierNamePEOGlobalAttributeDate92 | — |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierNamePEOGlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | POSupplierNamePEOGlobalAttributeNumber14 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierNamePEOGlobalAttributeNumber12 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | POSupplierNamePEOGlobalAttributeNumber102 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierNamePEOGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | POSupplierNamePEOGlobalAttributeNumber24 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierNamePEOGlobalAttributeNumber22 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | POSupplierNamePEOGlobalAttributeNumber34 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierNamePEOGlobalAttributeNumber32 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | POSupplierNamePEOGlobalAttributeNumber44 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierNamePEOGlobalAttributeNumber42 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | POSupplierNamePEOGlobalAttributeNumber54 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierNamePEOGlobalAttributeNumber52 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | POSupplierNamePEOGlobalAttributeNumber62 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierNamePEOGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | POSupplierNamePEOGlobalAttributeNumber72 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierNamePEOGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | POSupplierNamePEOGlobalAttributeNumber82 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierNamePEOGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | POSupplierNamePEOGlobalAttributeNumber92 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierNamePEOGlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | POSupplierNamePEOGlobalAttributeTimestamp12 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierNamePEOGlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | POSupplierNamePEOGlobalAttributeTimestamp102 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierNamePEOGlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | POSupplierNamePEOGlobalAttributeTimestamp22 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierNamePEOGlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | POSupplierNamePEOGlobalAttributeTimestamp32 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierNamePEOGlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | POSupplierNamePEOGlobalAttributeTimestamp42 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierNamePEOGlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | POSupplierNamePEOGlobalAttributeTimestamp52 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierNamePEOGlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | POSupplierNamePEOGlobalAttributeTimestamp62 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierNamePEOGlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | POSupplierNamePEOGlobalAttributeTimestamp72 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierNamePEOGlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | POSupplierNamePEOGlobalAttributeTimestamp82 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierNamePEOGlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | POSupplierNamePEOGlobalAttributeTimestamp92 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierNamePEOGlobalAttributeTimestamp9 | — |
| LAST_UPDATE_DATE | POSupplierNamePEOLastUpdateDate12 | ✅ |
| LAST_UPDATE_DATE | SupplierNamePEOLastUpdateDate10 | ✅ |
| LAST_UPDATE_LOGIN | POSupplierNamePEOLastUpdateLogin12 | — |
| LAST_UPDATE_LOGIN | SupplierNamePEOLastUpdateLogin10 | — |
| LAST_UPDATED_BY | POSupplierNamePEOLastUpdatedBy12 | — |
| LAST_UPDATED_BY | SupplierNamePEOLastUpdatedBy10 | — |
| MINORITY_GROUP_LOOKUP_CODE | POSupplierNamePEOMinorityGroupLookupCode1 | — |
| MINORITY_GROUP_LOOKUP_CODE | SupplierNamePEOMinorityGroupLookupCode | — |
| NAME_CONTROL | POSupplierNamePEONameControl1 | — |
| NAME_CONTROL | SupplierNamePEONameControl | — |
| NI_NUMBER | POSupplierNamePEONiNumber1 | — |
| NI_NUMBER | SupplierNamePEONiNumber | — |
| OBJECT_VERSION_NUMBER | POSupplierNamePEOObjectVersionNumber12 | — |
| OBJECT_VERSION_NUMBER | SupplierNamePEOObjectVersionNumber10 | — |
| ONE_TIME_FLAG | POSupplierNamePEOOneTimeFlag1 | — |
| ONE_TIME_FLAG | SupplierNamePEOOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | POSupplierNamePEOOrganizationTypeLookupCode1 | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierNamePEOOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | POSupplierNamePEOParentPartyId1 | ✅ |
| PARENT_PARTY_ID | SupplierNamePEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | POSupplierNamePEOParentVendorId1 | ✅ |
| PARENT_VENDOR_ID | SupplierNamePEOParentVendorId | ✅ |
| PARTY_ID | POSupplierNamePEOPartyId1 | ✅ |
| PARTY_ID | SupplierNamePEOPartyId | ✅ |
| PROGRAM_APPLICATION_ID | POSupplierNamePEOProgramApplicationId2 | ✅ |
| PROGRAM_APPLICATION_ID | SupplierNamePEOProgramApplicationId | ✅ |
| PROGRAM_ID | POSupplierNamePEOProgramId2 | ✅ |
| PROGRAM_ID | SupplierNamePEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | POSupplierNamePEOProgramUpdateDate2 | ✅ |
| PROGRAM_UPDATE_DATE | SupplierNamePEOProgramUpdateDate | ✅ |
| REBUILD_INDEX | POSupplierNamePEORebuildIndex2 | — |
| REBUILD_INDEX | SupplierNamePEORebuildIndex1 | — |
| REQUEST_ID | POSupplierNamePEORequestId12 | ✅ |
| REQUEST_ID | SupplierNamePEORequestId10 | ✅ |
| SEGMENT1 | POSupplierNamePEOSegment12 | — |
| SEGMENT1 | SupplierNamePEOSegment11 | — |
| SMALL_BUSINESS_FLAG | POSupplierNamePEOSmallBusinessFlag1 | — |
| SMALL_BUSINESS_FLAG | SupplierNamePEOSmallBusinessFlag | — |
| SPEND_AUTH_JUSTIFICATION | POSupplierNamePEOSpendAuthJustification1 | — |
| SPEND_AUTH_JUSTIFICATION | SupplierNamePEOSpendAuthJustification | — |
| SPEND_AUTH_REVIEW_STATUS | POSupplierNamePEOSpendAuthReviewStatus1 | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierNamePEOSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | POSupplierNamePEOStandardIndustryClass1 | — |
| STANDARD_INDUSTRY_CLASS | SupplierNamePEOStandardIndustryClass | — |
| START_DATE_ACTIVE | POSupplierNamePEOStartDateActive1 | — |
| START_DATE_ACTIVE | SupplierNamePEOStartDateActive | — |
| STATE_REPORTABLE_FLAG | POSupplierNamePEOStateReportableFlag1 | — |
| STATE_REPORTABLE_FLAG | SupplierNamePEOStateReportableFlag | — |
| TAX_REPORTING_NAME | POSupplierNamePEOTaxReportingName1 | — |
| TAX_REPORTING_NAME | SupplierNamePEOTaxReportingName | — |
| TAX_VERIFICATION_DATE | POSupplierNamePEOTaxVerificationDate1 | ✅ |
| TAX_VERIFICATION_DATE | SupplierNamePEOTaxVerificationDate | ✅ |
| TYPE_1099 | POSupplierNamePEOType10992 | — |
| TYPE_1099 | SupplierNamePEOType10991 | — |
| VENDOR_ID | POSupplierNamePEOVendorId5 | ✅ |
| VENDOR_ID | SupplierNamePEOVendorId3 | ✅ |
| VENDOR_NAME | POSupplierNamePEOVendorName1 | ✅ |
| VENDOR_NAME | SupplierNamePEOVendorName | ✅ |
| VENDOR_NAME_ALT | POSupplierNamePEOVendorNameAlt1 | — |
| VENDOR_NAME_ALT | SupplierNamePEOVendorNameAlt | — |
| VENDOR_TYPE_LOOKUP_CODE | POSupplierNamePEOVendorTypeLookupCode1 | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierNamePEOVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | POSupplierNamePEOWithholdingStartDate1 | ✅ |
| WITHHOLDING_START_DATE | SupplierNamePEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | POSupplierNamePEOWithholdingStatusLookupCode1 | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierNamePEOWithholdingStatusLookupCode | — |
| WOMEN_OWNED_FLAG | POSupplierNamePEOWomenOwnedFlag1 | — |
| WOMEN_OWNED_FLAG | SupplierNamePEOWomenOwnedFlag | — |

### [[wooperationsrefpvo|WOOperationsRefPVO]] (OTHER · BICC: 28/292)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | POSupplierNamePEOAllowAwtFlag1 | — |
| ALLOW_AWT_FLAG | SupplierNamePEOAllowAwtFlag | — |
| ATTRIBUTE1 | POSupplierNamePEOAttribute150 | — |
| ATTRIBUTE1 | SupplierNamePEOAttribute130 | — |
| ATTRIBUTE10 | POSupplierNamePEOAttribute1011 | — |
| ATTRIBUTE10 | SupplierNamePEOAttribute109 | — |
| ATTRIBUTE11 | POSupplierNamePEOAttribute1115 | — |
| ATTRIBUTE11 | SupplierNamePEOAttribute1113 | — |
| ATTRIBUTE12 | POSupplierNamePEOAttribute1213 | — |
| ATTRIBUTE12 | SupplierNamePEOAttribute1211 | — |
| ATTRIBUTE13 | POSupplierNamePEOAttribute1311 | — |
| ATTRIBUTE13 | SupplierNamePEOAttribute139 | — |
| ATTRIBUTE14 | POSupplierNamePEOAttribute1411 | — |
| ATTRIBUTE14 | SupplierNamePEOAttribute149 | — |
| ATTRIBUTE15 | POSupplierNamePEOAttribute1511 | — |
| ATTRIBUTE15 | SupplierNamePEOAttribute159 | — |
| ATTRIBUTE16 | POSupplierNamePEOAttribute1611 | — |
| ATTRIBUTE16 | SupplierNamePEOAttribute169 | — |
| ATTRIBUTE17 | POSupplierNamePEOAttribute1711 | — |
| ATTRIBUTE17 | SupplierNamePEOAttribute179 | — |
| ATTRIBUTE18 | POSupplierNamePEOAttribute1811 | — |
| ATTRIBUTE18 | SupplierNamePEOAttribute189 | — |
| ATTRIBUTE19 | POSupplierNamePEOAttribute1911 | — |
| ATTRIBUTE19 | SupplierNamePEOAttribute199 | — |
| ATTRIBUTE2 | POSupplierNamePEOAttribute211 | — |
| ATTRIBUTE2 | SupplierNamePEOAttribute29 | — |
| ATTRIBUTE20 | POSupplierNamePEOAttribute2011 | — |
| ATTRIBUTE20 | SupplierNamePEOAttribute209 | — |
| ATTRIBUTE3 | POSupplierNamePEOAttribute311 | — |
| ATTRIBUTE3 | SupplierNamePEOAttribute39 | — |
| ATTRIBUTE4 | POSupplierNamePEOAttribute411 | — |
| ATTRIBUTE4 | SupplierNamePEOAttribute49 | — |
| ATTRIBUTE5 | POSupplierNamePEOAttribute511 | — |
| ATTRIBUTE5 | SupplierNamePEOAttribute59 | — |
| ATTRIBUTE6 | POSupplierNamePEOAttribute611 | — |
| ATTRIBUTE6 | SupplierNamePEOAttribute69 | — |
| ATTRIBUTE7 | POSupplierNamePEOAttribute711 | — |
| ATTRIBUTE7 | SupplierNamePEOAttribute79 | — |
| ATTRIBUTE8 | POSupplierNamePEOAttribute811 | — |
| ATTRIBUTE8 | SupplierNamePEOAttribute89 | — |
| ATTRIBUTE9 | POSupplierNamePEOAttribute911 | — |
| ATTRIBUTE9 | SupplierNamePEOAttribute99 | — |
| ATTRIBUTE_CATEGORY | POSupplierNamePEOAttributeCategory11 | — |
| ATTRIBUTE_CATEGORY | SupplierNamePEOAttributeCategory9 | — |
| ATTRIBUTE_DATE1 | POSupplierNamePEOAttributeDate111 | — |
| ATTRIBUTE_DATE1 | SupplierNamePEOAttributeDate19 | — |
| ATTRIBUTE_DATE10 | POSupplierNamePEOAttributeDate105 | — |
| ATTRIBUTE_DATE10 | SupplierNamePEOAttributeDate103 | — |
| ATTRIBUTE_DATE2 | POSupplierNamePEOAttributeDate211 | — |
| ATTRIBUTE_DATE2 | SupplierNamePEOAttributeDate29 | — |
| ATTRIBUTE_DATE3 | POSupplierNamePEOAttributeDate311 | — |
| ATTRIBUTE_DATE3 | SupplierNamePEOAttributeDate39 | — |
| ATTRIBUTE_DATE4 | POSupplierNamePEOAttributeDate411 | — |
| ATTRIBUTE_DATE4 | SupplierNamePEOAttributeDate49 | — |
| ATTRIBUTE_DATE5 | POSupplierNamePEOAttributeDate511 | — |
| ATTRIBUTE_DATE5 | SupplierNamePEOAttributeDate59 | — |
| ATTRIBUTE_DATE6 | POSupplierNamePEOAttributeDate65 | — |
| ATTRIBUTE_DATE6 | SupplierNamePEOAttributeDate63 | — |
| ATTRIBUTE_DATE7 | POSupplierNamePEOAttributeDate75 | — |
| ATTRIBUTE_DATE7 | SupplierNamePEOAttributeDate73 | — |
| ATTRIBUTE_DATE8 | POSupplierNamePEOAttributeDate85 | — |
| ATTRIBUTE_DATE8 | SupplierNamePEOAttributeDate83 | — |
| ATTRIBUTE_DATE9 | POSupplierNamePEOAttributeDate95 | — |
| ATTRIBUTE_DATE9 | SupplierNamePEOAttributeDate93 | — |
| ATTRIBUTE_NUMBER1 | POSupplierNamePEOAttributeNumber111 | — |
| ATTRIBUTE_NUMBER1 | SupplierNamePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER10 | POSupplierNamePEOAttributeNumber1011 | — |
| ATTRIBUTE_NUMBER10 | SupplierNamePEOAttributeNumber109 | — |
| ATTRIBUTE_NUMBER2 | POSupplierNamePEOAttributeNumber211 | — |
| ATTRIBUTE_NUMBER2 | SupplierNamePEOAttributeNumber29 | — |
| ATTRIBUTE_NUMBER3 | POSupplierNamePEOAttributeNumber311 | — |
| ATTRIBUTE_NUMBER3 | SupplierNamePEOAttributeNumber39 | — |
| ATTRIBUTE_NUMBER4 | POSupplierNamePEOAttributeNumber411 | — |
| ATTRIBUTE_NUMBER4 | SupplierNamePEOAttributeNumber49 | — |
| ATTRIBUTE_NUMBER5 | POSupplierNamePEOAttributeNumber511 | — |
| ATTRIBUTE_NUMBER5 | SupplierNamePEOAttributeNumber59 | — |
| ATTRIBUTE_NUMBER6 | POSupplierNamePEOAttributeNumber611 | — |
| ATTRIBUTE_NUMBER6 | SupplierNamePEOAttributeNumber69 | — |
| ATTRIBUTE_NUMBER7 | POSupplierNamePEOAttributeNumber711 | — |
| ATTRIBUTE_NUMBER7 | SupplierNamePEOAttributeNumber79 | — |
| ATTRIBUTE_NUMBER8 | POSupplierNamePEOAttributeNumber811 | — |
| ATTRIBUTE_NUMBER8 | SupplierNamePEOAttributeNumber89 | — |
| ATTRIBUTE_NUMBER9 | POSupplierNamePEOAttributeNumber911 | — |
| ATTRIBUTE_NUMBER9 | SupplierNamePEOAttributeNumber99 | — |
| ATTRIBUTE_TIMESTAMP1 | POSupplierNamePEOAttributeTimestamp111 | — |
| ATTRIBUTE_TIMESTAMP1 | SupplierNamePEOAttributeTimestamp19 | — |
| ATTRIBUTE_TIMESTAMP10 | POSupplierNamePEOAttributeTimestamp105 | — |
| ATTRIBUTE_TIMESTAMP10 | SupplierNamePEOAttributeTimestamp103 | — |
| ATTRIBUTE_TIMESTAMP2 | POSupplierNamePEOAttributeTimestamp211 | — |
| ATTRIBUTE_TIMESTAMP2 | SupplierNamePEOAttributeTimestamp29 | — |
| ATTRIBUTE_TIMESTAMP3 | POSupplierNamePEOAttributeTimestamp311 | — |
| ATTRIBUTE_TIMESTAMP3 | SupplierNamePEOAttributeTimestamp39 | — |
| ATTRIBUTE_TIMESTAMP4 | POSupplierNamePEOAttributeTimestamp411 | — |
| ATTRIBUTE_TIMESTAMP4 | SupplierNamePEOAttributeTimestamp49 | — |
| ATTRIBUTE_TIMESTAMP5 | POSupplierNamePEOAttributeTimestamp511 | — |
| ATTRIBUTE_TIMESTAMP5 | SupplierNamePEOAttributeTimestamp59 | — |
| ATTRIBUTE_TIMESTAMP6 | POSupplierNamePEOAttributeTimestamp65 | — |
| ATTRIBUTE_TIMESTAMP6 | SupplierNamePEOAttributeTimestamp63 | — |
| ATTRIBUTE_TIMESTAMP7 | POSupplierNamePEOAttributeTimestamp75 | — |
| ATTRIBUTE_TIMESTAMP7 | SupplierNamePEOAttributeTimestamp73 | — |
| ATTRIBUTE_TIMESTAMP8 | POSupplierNamePEOAttributeTimestamp85 | — |
| ATTRIBUTE_TIMESTAMP8 | SupplierNamePEOAttributeTimestamp83 | — |
| ATTRIBUTE_TIMESTAMP9 | POSupplierNamePEOAttributeTimestamp95 | — |
| ATTRIBUTE_TIMESTAMP9 | SupplierNamePEOAttributeTimestamp93 | — |
| AWT_GROUP_ID | POSupplierNamePEOAwtGroupId1 | ✅ |
| AWT_GROUP_ID | SupplierNamePEOAwtGroupId | ✅ |
| BUSINESS_RELATIONSHIP | POSupplierNamePEOBusinessRelationship1 | — |
| BUSINESS_RELATIONSHIP | SupplierNamePEOBusinessRelationship | — |
| CORPORATE_WEBSITE | POSupplierNamePEOCorporateWebsite1 | — |
| CORPORATE_WEBSITE | SupplierNamePEOCorporateWebsite | — |
| CREATED_BY | POSupplierNamePEOCreatedBy12 | — |
| CREATED_BY | SupplierNamePEOCreatedBy10 | — |
| CREATION_DATE | POSupplierNamePEOCreationDate12 | ✅ |
| CREATION_DATE | SupplierNamePEOCreationDate10 | ✅ |
| CUSTOMER_NUM | POSupplierNamePEOCustomerNum2 | — |
| CUSTOMER_NUM | SupplierNamePEOCustomerNum | — |
| DUNS_NUMBER_C | POSupplierNamePEODunsNumberC1 | — |
| DUNS_NUMBER_C | SupplierNamePEODunsNumberC | — |
| END_DATE_ACTIVE | POSupplierNamePEOEndDateActive1 | — |
| END_DATE_ACTIVE | SupplierNamePEOEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | POSupplierNamePEOFederalReportableFlag1 | — |
| FEDERAL_REPORTABLE_FLAG | SupplierNamePEOFederalReportableFlag | — |
| GLOBAL_ATTRIBUTE1 | POSupplierNamePEOGlobalAttribute120 | — |
| GLOBAL_ATTRIBUTE1 | SupplierNamePEOGlobalAttribute116 | — |
| GLOBAL_ATTRIBUTE10 | POSupplierNamePEOGlobalAttribute106 | — |
| GLOBAL_ATTRIBUTE10 | SupplierNamePEOGlobalAttribute104 | — |
| GLOBAL_ATTRIBUTE11 | POSupplierNamePEOGlobalAttribute1110 | — |
| GLOBAL_ATTRIBUTE11 | SupplierNamePEOGlobalAttribute117 | — |
| GLOBAL_ATTRIBUTE12 | POSupplierNamePEOGlobalAttribute126 | — |
| GLOBAL_ATTRIBUTE12 | SupplierNamePEOGlobalAttribute124 | — |
| GLOBAL_ATTRIBUTE13 | POSupplierNamePEOGlobalAttribute136 | — |
| GLOBAL_ATTRIBUTE13 | SupplierNamePEOGlobalAttribute134 | — |
| GLOBAL_ATTRIBUTE14 | POSupplierNamePEOGlobalAttribute146 | — |
| GLOBAL_ATTRIBUTE14 | SupplierNamePEOGlobalAttribute144 | — |
| GLOBAL_ATTRIBUTE15 | POSupplierNamePEOGlobalAttribute156 | — |
| GLOBAL_ATTRIBUTE15 | SupplierNamePEOGlobalAttribute154 | — |
| GLOBAL_ATTRIBUTE16 | POSupplierNamePEOGlobalAttribute166 | — |
| GLOBAL_ATTRIBUTE16 | SupplierNamePEOGlobalAttribute164 | — |
| GLOBAL_ATTRIBUTE17 | POSupplierNamePEOGlobalAttribute176 | — |
| GLOBAL_ATTRIBUTE17 | SupplierNamePEOGlobalAttribute174 | — |
| GLOBAL_ATTRIBUTE18 | POSupplierNamePEOGlobalAttribute186 | — |
| GLOBAL_ATTRIBUTE18 | SupplierNamePEOGlobalAttribute184 | — |
| GLOBAL_ATTRIBUTE19 | POSupplierNamePEOGlobalAttribute196 | — |
| GLOBAL_ATTRIBUTE19 | SupplierNamePEOGlobalAttribute194 | — |
| GLOBAL_ATTRIBUTE2 | POSupplierNamePEOGlobalAttribute26 | — |
| GLOBAL_ATTRIBUTE2 | SupplierNamePEOGlobalAttribute24 | — |
| GLOBAL_ATTRIBUTE20 | POSupplierNamePEOGlobalAttribute206 | — |
| GLOBAL_ATTRIBUTE20 | SupplierNamePEOGlobalAttribute204 | — |
| GLOBAL_ATTRIBUTE3 | POSupplierNamePEOGlobalAttribute36 | — |
| GLOBAL_ATTRIBUTE3 | SupplierNamePEOGlobalAttribute34 | — |
| GLOBAL_ATTRIBUTE4 | POSupplierNamePEOGlobalAttribute46 | — |
| GLOBAL_ATTRIBUTE4 | SupplierNamePEOGlobalAttribute44 | — |
| GLOBAL_ATTRIBUTE5 | POSupplierNamePEOGlobalAttribute56 | — |
| GLOBAL_ATTRIBUTE5 | SupplierNamePEOGlobalAttribute54 | — |
| GLOBAL_ATTRIBUTE6 | POSupplierNamePEOGlobalAttribute66 | — |
| GLOBAL_ATTRIBUTE6 | SupplierNamePEOGlobalAttribute64 | — |
| GLOBAL_ATTRIBUTE7 | POSupplierNamePEOGlobalAttribute76 | — |
| GLOBAL_ATTRIBUTE7 | SupplierNamePEOGlobalAttribute74 | — |
| GLOBAL_ATTRIBUTE8 | POSupplierNamePEOGlobalAttribute86 | — |
| GLOBAL_ATTRIBUTE8 | SupplierNamePEOGlobalAttribute84 | — |
| GLOBAL_ATTRIBUTE9 | POSupplierNamePEOGlobalAttribute96 | — |
| GLOBAL_ATTRIBUTE9 | SupplierNamePEOGlobalAttribute94 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | POSupplierNamePEOGlobalAttributeCategory6 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierNamePEOGlobalAttributeCategory4 | — |
| GLOBAL_ATTRIBUTE_DATE1 | POSupplierNamePEOGlobalAttributeDate13 | — |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierNamePEOGlobalAttributeDate11 | — |
| GLOBAL_ATTRIBUTE_DATE10 | POSupplierNamePEOGlobalAttributeDate102 | — |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierNamePEOGlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | POSupplierNamePEOGlobalAttributeDate23 | — |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierNamePEOGlobalAttributeDate21 | — |
| GLOBAL_ATTRIBUTE_DATE3 | POSupplierNamePEOGlobalAttributeDate33 | — |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierNamePEOGlobalAttributeDate31 | — |
| GLOBAL_ATTRIBUTE_DATE4 | POSupplierNamePEOGlobalAttributeDate43 | — |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierNamePEOGlobalAttributeDate41 | — |
| GLOBAL_ATTRIBUTE_DATE5 | POSupplierNamePEOGlobalAttributeDate53 | — |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierNamePEOGlobalAttributeDate51 | — |
| GLOBAL_ATTRIBUTE_DATE6 | POSupplierNamePEOGlobalAttributeDate62 | — |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierNamePEOGlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | POSupplierNamePEOGlobalAttributeDate72 | — |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierNamePEOGlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | POSupplierNamePEOGlobalAttributeDate82 | — |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierNamePEOGlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | POSupplierNamePEOGlobalAttributeDate92 | — |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierNamePEOGlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | POSupplierNamePEOGlobalAttributeNumber13 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierNamePEOGlobalAttributeNumber11 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | POSupplierNamePEOGlobalAttributeNumber102 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierNamePEOGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | POSupplierNamePEOGlobalAttributeNumber23 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierNamePEOGlobalAttributeNumber21 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | POSupplierNamePEOGlobalAttributeNumber33 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierNamePEOGlobalAttributeNumber31 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | POSupplierNamePEOGlobalAttributeNumber43 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierNamePEOGlobalAttributeNumber41 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | POSupplierNamePEOGlobalAttributeNumber53 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierNamePEOGlobalAttributeNumber51 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | POSupplierNamePEOGlobalAttributeNumber62 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierNamePEOGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | POSupplierNamePEOGlobalAttributeNumber72 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierNamePEOGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | POSupplierNamePEOGlobalAttributeNumber82 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierNamePEOGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | POSupplierNamePEOGlobalAttributeNumber92 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierNamePEOGlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | POSupplierNamePEOGlobalAttributeTimestamp12 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierNamePEOGlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | POSupplierNamePEOGlobalAttributeTimestamp102 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierNamePEOGlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | POSupplierNamePEOGlobalAttributeTimestamp22 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierNamePEOGlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | POSupplierNamePEOGlobalAttributeTimestamp32 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierNamePEOGlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | POSupplierNamePEOGlobalAttributeTimestamp42 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierNamePEOGlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | POSupplierNamePEOGlobalAttributeTimestamp52 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierNamePEOGlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | POSupplierNamePEOGlobalAttributeTimestamp62 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierNamePEOGlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | POSupplierNamePEOGlobalAttributeTimestamp72 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierNamePEOGlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | POSupplierNamePEOGlobalAttributeTimestamp82 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierNamePEOGlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | POSupplierNamePEOGlobalAttributeTimestamp92 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierNamePEOGlobalAttributeTimestamp9 | — |
| LAST_UPDATE_DATE | POSupplierNamePEOLastUpdateDate12 | ✅ |
| LAST_UPDATE_DATE | SupplierNamePEOLastUpdateDate10 | ✅ |
| LAST_UPDATE_LOGIN | POSupplierNamePEOLastUpdateLogin12 | — |
| LAST_UPDATE_LOGIN | SupplierNamePEOLastUpdateLogin10 | — |
| LAST_UPDATED_BY | POSupplierNamePEOLastUpdatedBy12 | — |
| LAST_UPDATED_BY | SupplierNamePEOLastUpdatedBy10 | — |
| MINORITY_GROUP_LOOKUP_CODE | POSupplierNamePEOMinorityGroupLookupCode1 | — |
| MINORITY_GROUP_LOOKUP_CODE | SupplierNamePEOMinorityGroupLookupCode | — |
| NAME_CONTROL | POSupplierNamePEONameControl1 | — |
| NAME_CONTROL | SupplierNamePEONameControl | — |
| NI_NUMBER | POSupplierNamePEONiNumber1 | — |
| NI_NUMBER | SupplierNamePEONiNumber | — |
| OBJECT_VERSION_NUMBER | POSupplierNamePEOObjectVersionNumber12 | — |
| OBJECT_VERSION_NUMBER | SupplierNamePEOObjectVersionNumber10 | — |
| ONE_TIME_FLAG | POSupplierNamePEOOneTimeFlag1 | — |
| ONE_TIME_FLAG | SupplierNamePEOOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | POSupplierNamePEOOrganizationTypeLookupCode1 | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierNamePEOOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | POSupplierNamePEOParentPartyId1 | ✅ |
| PARENT_PARTY_ID | SupplierNamePEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | POSupplierNamePEOParentVendorId1 | ✅ |
| PARENT_VENDOR_ID | SupplierNamePEOParentVendorId | ✅ |
| PARTY_ID | POSupplierNamePEOPartyId1 | ✅ |
| PARTY_ID | SupplierNamePEOPartyId | ✅ |
| PROGRAM_APPLICATION_ID | POSupplierNamePEOProgramApplicationId2 | ✅ |
| PROGRAM_APPLICATION_ID | SupplierNamePEOProgramApplicationId | ✅ |
| PROGRAM_ID | POSupplierNamePEOProgramId2 | ✅ |
| PROGRAM_ID | SupplierNamePEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | POSupplierNamePEOProgramUpdateDate2 | ✅ |
| PROGRAM_UPDATE_DATE | SupplierNamePEOProgramUpdateDate | ✅ |
| REBUILD_INDEX | POSupplierNamePEORebuildIndex2 | — |
| REBUILD_INDEX | SupplierNamePEORebuildIndex1 | — |
| REQUEST_ID | POSupplierNamePEORequestId12 | ✅ |
| REQUEST_ID | SupplierNamePEORequestId10 | — |
| SEGMENT1 | POSupplierNamePEOSegment12 | ✅ |
| SEGMENT1 | SupplierNamePEOSegment11 | — |
| SMALL_BUSINESS_FLAG | POSupplierNamePEOSmallBusinessFlag1 | — |
| SMALL_BUSINESS_FLAG | SupplierNamePEOSmallBusinessFlag | — |
| SPEND_AUTH_JUSTIFICATION | POSupplierNamePEOSpendAuthJustification1 | — |
| SPEND_AUTH_JUSTIFICATION | SupplierNamePEOSpendAuthJustification | — |
| SPEND_AUTH_REVIEW_STATUS | POSupplierNamePEOSpendAuthReviewStatus1 | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierNamePEOSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | POSupplierNamePEOStandardIndustryClass1 | — |
| STANDARD_INDUSTRY_CLASS | SupplierNamePEOStandardIndustryClass | — |
| START_DATE_ACTIVE | POSupplierNamePEOStartDateActive1 | — |
| START_DATE_ACTIVE | SupplierNamePEOStartDateActive | — |
| STATE_REPORTABLE_FLAG | POSupplierNamePEOStateReportableFlag1 | — |
| STATE_REPORTABLE_FLAG | SupplierNamePEOStateReportableFlag | — |
| TAX_REPORTING_NAME | POSupplierNamePEOTaxReportingName1 | — |
| TAX_REPORTING_NAME | SupplierNamePEOTaxReportingName | — |
| TAX_VERIFICATION_DATE | POSupplierNamePEOTaxVerificationDate1 | ✅ |
| TAX_VERIFICATION_DATE | SupplierNamePEOTaxVerificationDate | ✅ |
| TYPE_1099 | POSupplierNamePEOType10992 | — |
| TYPE_1099 | SupplierNamePEOType10991 | — |
| VENDOR_ID | POSupplierNamePEOVendorId5 | ✅ |
| VENDOR_ID | SupplierNamePEOVendorId3 | ✅ |
| VENDOR_NAME | POSupplierNamePEOVendorName1 | ✅ |
| VENDOR_NAME | SupplierNamePEOVendorName | ✅ |
| VENDOR_NAME_ALT | POSupplierNamePEOVendorNameAlt1 | — |
| VENDOR_NAME_ALT | SupplierNamePEOVendorNameAlt | — |
| VENDOR_TYPE_LOOKUP_CODE | POSupplierNamePEOVendorTypeLookupCode1 | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierNamePEOVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | POSupplierNamePEOWithholdingStartDate1 | ✅ |
| WITHHOLDING_START_DATE | SupplierNamePEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | POSupplierNamePEOWithholdingStatusLookupCode1 | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierNamePEOWithholdingStatusLookupCode | — |
| WOMEN_OWNED_FLAG | POSupplierNamePEOWomenOwnedFlag1 | — |
| WOMEN_OWNED_FLAG | SupplierNamePEOWomenOwnedFlag | — |

### [[workorderpvo|WorkOrderPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| VENDOR_ID | WarrantySupplierViewPEOVendorId | — |
| VENDOR_NAME | WarrantySupplierViewPEOVendorName | — |

### [[workorderrefpvo|WorkOrderRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| VENDOR_ID | WarrantySupplierViewPEOVendorId | — |
| VENDOR_NAME | WarrantySupplierViewPEOVendorName | — |
