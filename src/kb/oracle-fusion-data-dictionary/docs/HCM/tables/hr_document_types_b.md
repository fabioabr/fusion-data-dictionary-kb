---
id: DOC-HCM-277
doc_type: system-doc
title: "HR_DOCUMENT_TYPES_B — Tipos de Documento — Base"
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
  - document-types
  - configuracao
  - compliance
aliases:
  - HR_DOCUMENT_TYPES_B
  - hr_document_types_b
  - hr-document-types-b
  - document-types-base
  - tipos-documento-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOCUMENT_TYPES_B

## 📌 Visao Geral

Tabela base que define os **tipos de documento** disponiveis para registro de colaboradores (e.g., Passaporte, RG, CPF, Diploma, Certificacao).

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir tipos de documento por legislacao.
- **Compliance:** Controlar quais documentos sao obrigatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador do tipo | — | 🟢 100% |
| 2 | DOCUMENT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificacao | Codigo do tipo | — | 🟢 95% |
| 3 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificacao | Legislacao aplicavel | — | 🟢 90% |
| 4 | CATEGORY_CODE | VARCHAR2(30) | NULL | Classificacao | Categoria do documento | — | 🟡 80% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NOT NULL | Classificacao | Ativo (Y/N) | — | 🟢 90% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hr_document_types_tl]] — via `DOCUMENT_TYPE_ID` (traducoes multilingue do registro)
- [[hr_documents_of_record]] — via `DOCUMENT_TYPE_ID` (documentos registrados do tipo)

---

## 📎 Uso Tipico

### Tipos de documento ativos
```sql
SELECT dt.DOCUMENT_TYPE_ID, dt.DOCUMENT_TYPE_CODE, dt.LEGISLATION_CODE
FROM   HR_DOCUMENT_TYPES_B dt
WHERE  dt.ACTIVE_FLAG = 'Y';
```

---

## 🔒 Observacoes

- Sufixo `_B` — traducoes em [[hr_document_types_tl]].
- Tipos podem ser especificos por legislacao (LEGISLATION_CODE).

---

## 📚 Referencias

- [Oracle Docs — HR_DOCUMENT_TYPES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdocumenttypesb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[documenttypespvo|DocumentTypesPVO]] (GL · BICC: 23/120)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_INACTIVE_FLAG | DocumentTypesPEOActiveInactiveFlag | ✅ |
| ARCHIVE_CRITERIA_BASIS | DocumentTypesPEOArchiveCriteriaBasis | — |
| ARCHIVE_CRITERIA_DAYS | DocumentTypesPEOArchiveCriteriaDays | — |
| AUTHORIZATION_REQUIRED | DocumentTypesPEOAuthorizationRequired | ✅ |
| BI_REPORT_PATH | BiReportPath | ✅ |
| CATEGORY_CODE | DocumentTypesPEOCategoryCode | ✅ |
| COMMENTS_REQUIRED | DocumentTypesPEOCommentsRequired | — |
| CREATED_BY | DocumentTypesPEOCreatedBy | ✅ |
| CREATION_DATE | DocumentTypesPEOCreationDate | ✅ |
| DATE_FROM_REQUIRED | DocumentTypesPEODateFromRequired | — |
| DATE_TO_REQUIRED | DocumentTypesPEODateToRequired | — |
| DFF_CTX_SEG_DEFAULT_VALUE | DocumentTypesPEODffCtxSegDefaultValue | — |
| DFF_CTX_SEG_DISPLAY_PREF | DocumentTypesPEODffCtxSegDisplayPref | — |
| DFF_GLB_SEG_DISPLAY_PREF | DocumentTypesPEODffGlbSegDisplayPref | — |
| DOCUMENT_NAME_REQUIRED | DocumentTypesPEODocumentNameRequired | — |
| DOCUMENT_NUMBER_REQUIRED | DocumentTypesPEODocumentNumberRequired | — |
| DOCUMENT_TYPE_ID | DocumentTypeId | ✅ |
| DOCUMENT_TYPE_LEVEL | DocumentTypeLevel | ✅ |
| DT_ATTRIBUTE1 | DtAttribute1 | — |
| DT_ATTRIBUTE10 | DtAttribute10 | — |
| DT_ATTRIBUTE2 | DtAttribute2 | — |
| DT_ATTRIBUTE3 | DtAttribute3 | — |
| DT_ATTRIBUTE4 | DtAttribute4 | — |
| DT_ATTRIBUTE5 | DtAttribute5 | — |
| DT_ATTRIBUTE6 | DtAttribute6 | — |
| DT_ATTRIBUTE7 | DtAttribute7 | — |
| DT_ATTRIBUTE8 | DtAttribute8 | — |
| DT_ATTRIBUTE9 | DtAttribute9 | — |
| DT_ATTRIBUTE_CATEGORY | DtAttributeCategory | — |
| DT_ATTRIBUTE_DATE1 | DtAttributeDate1 | — |
| DT_ATTRIBUTE_DATE10 | DtAttributeDate10 | — |
| DT_ATTRIBUTE_DATE2 | DtAttributeDate2 | — |
| DT_ATTRIBUTE_DATE3 | DtAttributeDate3 | — |
| DT_ATTRIBUTE_DATE4 | DtAttributeDate4 | — |
| DT_ATTRIBUTE_DATE5 | DtAttributeDate5 | — |
| DT_ATTRIBUTE_DATE6 | DtAttributeDate6 | — |
| DT_ATTRIBUTE_DATE7 | DtAttributeDate7 | — |
| DT_ATTRIBUTE_DATE8 | DtAttributeDate8 | — |
| DT_ATTRIBUTE_DATE9 | DtAttributeDate9 | — |
| DT_ATTRIBUTE_NUMBER1 | DtAttributeNumber1 | — |
| DT_ATTRIBUTE_NUMBER10 | DtAttributeNumber10 | — |
| DT_ATTRIBUTE_NUMBER2 | DtAttributeNumber2 | — |
| DT_ATTRIBUTE_NUMBER3 | DtAttributeNumber3 | — |
| DT_ATTRIBUTE_NUMBER4 | DtAttributeNumber4 | — |
| DT_ATTRIBUTE_NUMBER5 | DtAttributeNumber5 | — |
| DT_ATTRIBUTE_NUMBER6 | DtAttributeNumber6 | — |
| DT_ATTRIBUTE_NUMBER7 | DtAttributeNumber7 | — |
| DT_ATTRIBUTE_NUMBER8 | DtAttributeNumber8 | — |
| DT_ATTRIBUTE_NUMBER9 | DtAttributeNumber9 | — |
| DT_ATTRIBUTE_TIMESTAMP1 | DtAttributeTimestamp1 | — |
| DT_ATTRIBUTE_TIMESTAMP2 | DtAttributeTimestamp2 | — |
| DT_ATTRIBUTE_TIMESTAMP3 | DtAttributeTimestamp3 | — |
| DT_ATTRIBUTE_TIMESTAMP4 | DtAttributeTimestamp4 | — |
| DT_ATTRIBUTE_TIMESTAMP5 | DtAttributeTimestamp5 | — |
| DT_INFORMATION1 | DtInformation1 | — |
| DT_INFORMATION10 | DtInformation10 | — |
| DT_INFORMATION2 | DtInformation2 | — |
| DT_INFORMATION3 | DtInformation3 | — |
| DT_INFORMATION4 | DtInformation4 | — |
| DT_INFORMATION5 | DtInformation5 | — |
| DT_INFORMATION6 | DtInformation6 | — |
| DT_INFORMATION7 | DtInformation7 | — |
| DT_INFORMATION8 | DtInformation8 | — |
| DT_INFORMATION9 | DtInformation9 | — |
| DT_INFORMATION_CATEGORY | DtInformationCategory | — |
| DT_INFORMATION_DATE1 | DtInformationDate1 | — |
| DT_INFORMATION_DATE10 | DtInformationDate10 | — |
| DT_INFORMATION_DATE2 | DtInformationDate2 | — |
| DT_INFORMATION_DATE3 | DtInformationDate3 | — |
| DT_INFORMATION_DATE4 | DtInformationDate4 | — |
| DT_INFORMATION_DATE5 | DtInformationDate5 | — |
| DT_INFORMATION_DATE6 | DtInformationDate6 | — |
| DT_INFORMATION_DATE7 | DtInformationDate7 | — |
| DT_INFORMATION_DATE8 | DtInformationDate8 | — |
| DT_INFORMATION_DATE9 | DtInformationDate9 | — |
| DT_INFORMATION_NUMBER1 | DtInformationNumber1 | — |
| DT_INFORMATION_NUMBER10 | DtInformationNumber10 | — |
| DT_INFORMATION_NUMBER2 | DtInformationNumber2 | — |
| DT_INFORMATION_NUMBER3 | DtInformationNumber3 | — |
| DT_INFORMATION_NUMBER4 | DtInformationNumber4 | — |
| DT_INFORMATION_NUMBER5 | DtInformationNumber5 | — |
| DT_INFORMATION_NUMBER6 | DtInformationNumber6 | — |
| DT_INFORMATION_NUMBER7 | DtInformationNumber7 | — |
| DT_INFORMATION_NUMBER8 | DtInformationNumber8 | — |
| DT_INFORMATION_NUMBER9 | DtInformationNumber9 | — |
| DT_INFORMATION_TIMESTAMP1 | DtInformationTimestamp1 | — |
| DT_INFORMATION_TIMESTAMP2 | DtInformationTimestamp2 | — |
| DT_INFORMATION_TIMESTAMP3 | DtInformationTimestamp3 | — |
| DT_INFORMATION_TIMESTAMP4 | DtInformationTimestamp4 | — |
| DT_INFORMATION_TIMESTAMP5 | DtInformationTimestamp5 | — |
| ENTERPRISE_ID | DocumentTypesPEOEnterpriseId | — |
| HIERARCHY_CODE | DocumentTypesPEOHierarchyCode | ✅ |
| ISSUED_DATE_REQUIRED | DocumentTypesPEOIssuedDateRequired | — |
| ISSUING_AUTHORITY_REQUIRED | DocumentTypesPEOIssuingAuthorityRequired | — |
| ISSUING_COUNTRY_REQUIRED | DocumentTypesPEOIssuingCountryRequired | — |
| ISSUING_LOCATION_REQUIRED | DocumentTypesPEOIssuingLocationRequired | — |
| LAST_UPDATE_DATE | DocumentTypesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DocumentTypesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DocumentTypesPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | DocumentTypesPEOLegislationCode | ✅ |
| LOCK_CREATE | LockCreate | ✅ |
| LOCK_CREATE_ROLE_LIST | DocumentTypesPEOLockCreateRoleList | — |
| LOCK_DELETE | LockDelete | ✅ |
| LOCK_DELETE_ROLE_LIST | DocumentTypesPEOLockDeleteRoleList | — |
| LOCK_UPDATE | LockUpdate | ✅ |
| LOCK_UPDATE_ROLE_LIST | DocumentTypesPEOLockUpdateRoleList | — |
| MIN_ATTACHMENTS_COUNT | MinAttachmentsCount | ✅ |
| MODULE_ID | DocumentTypesPEOModuleId | — |
| MULTIPLE_OCCURENCES_FLAG | DocumentTypesPEOMultipleOccurencesFlag | ✅ |
| OBJECT_VERSION_NUMBER | DocumentTypesPEOObjectVersionNumber | — |
| PUBLISH_REQUIRED | DocumentTypesPEOPublishRequired | ✅ |
| PURGE_ARCHIVE_CRITERIA_DAYS | DocumentTypesPEOPurgeArchiveCriteriaDays | — |
| RESTRICT_CREATE_ATTACH | RestrictCreateAttach | ✅ |
| RESTRICT_DELETE_ATTACH | RestrictDeleteAttach | ✅ |
| RESTRICT_UPDATE_ATTACH | RestrictUpdateAttach | ✅ |
| SEED_DATA_SOURCE | SeedDataSource | — |
| SUB_CATEGORY_CODE | DocumentTypesPEOSubCategoryCode | — |
| SYSTEM_DOCUMENT_TYPE | DocumentTypesPEOSystemDocumentType | ✅ |
| TAG_LIST | DocumentTypesPEOTagList | — |
| WARNING_PERIOD | DocumentTypesPEOWarningPeriod | ✅ |
