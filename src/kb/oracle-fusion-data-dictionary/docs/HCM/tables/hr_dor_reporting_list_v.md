---
id: DOC-HCM-279
doc_type: system-doc
title: "HR_DOR_REPORTING_LIST_V — Lista de Relatorios de Documentos de Registro (View)"
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
  - documents
  - reporting
  - compliance
aliases:
  - HR_DOR_REPORTING_LIST_V
  - hr_dor_reporting_list_v
  - hr-dor-reporting-list-v
  - dor-reporting-list
  - relatorio-documentos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOR_REPORTING_LIST_V

## 📌 Visao Geral

View que consolida dados de **documentos de registro** para fins de reporting. Combina informacoes de documentos, pessoas e tipos de documento.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Relatorios:** Extracao consolidada de documentos para relatorios gerenciais.
- **Compliance:** Monitorar documentos vencidos ou pendentes.
- **BI/Analytics:** Fonte para dashboards de compliance documental.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENTS_OF_RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador do documento | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de documento | [[hr_document_types_b]] | 🟢 95% |
| 4 | DOCUMENT_TYPE_NAME | VARCHAR2(240) | NULL | Dados | Nome do tipo de documento | — | 🟢 90% |
| 5 | DOCUMENT_NUMBER | VARCHAR2(150) | NULL | Dados | Numero do documento | — | 🟢 90% |
| 6 | DATE_FROM | DATE | NULL | Data | Data de emissao | — | 🟢 90% |
| 7 | DATE_TO | DATE | NULL | Data | Data de vencimento | — | 🟢 90% |
| 8 | PERSON_NAME | VARCHAR2(360) | NULL | Dados | Nome do colaborador | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador na lista de documentos obrigatorios)
- [[hr_document_types_b]] — via `DOCUMENT_TYPE_ID` (tipo de documento na lista obrigatoria)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Documentos vencidos
```sql
SELECT v.PERSON_NAME, v.DOCUMENT_TYPE_NAME,
       v.DOCUMENT_NUMBER, v.DATE_TO
FROM   HR_DOR_REPORTING_LIST_V v
WHERE  v.DATE_TO < SYSDATE;
```

---

## 🔒 Observacoes

- Sufixo `_V` indica view — somente leitura.
- Pode conter dados sensiveis (PII).

---

## 📚 Referencias

- [Oracle Docs — HR_DOR_REPORTING_LIST_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdorreportinglistv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[documentsofrecordpvo|DocumentsOfRecordPVO]] (GL · BICC: 22/192)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | DocumentsOfRecordPEOAssignmentId | — |
| COMMENTS | DocumentsOfRecordPEOComments | ✅ |
| CREATED_BY | DocumentsOfRecordPEOCreatedBy | ✅ |
| CREATION_DATE | DocumentsOfRecordPEOCreationDate | ✅ |
| CREATION_SOURCE | DocumentsOfRecordPEOCreationSource | — |
| DATE_FROM | DocumentsOfRecordPEODateFrom | ✅ |
| DATE_TO | DocumentsOfRecordPEODateTo | ✅ |
| DEI_ATTRIBUTE1 | DocumentsOfRecordPEODeiAttribute1 | — |
| DEI_ATTRIBUTE10 | DocumentsOfRecordPEODeiAttribute10 | — |
| DEI_ATTRIBUTE11 | DocumentsOfRecordPEODeiAttribute11 | — |
| DEI_ATTRIBUTE12 | DocumentsOfRecordPEODeiAttribute12 | — |
| DEI_ATTRIBUTE13 | DocumentsOfRecordPEODeiAttribute13 | — |
| DEI_ATTRIBUTE14 | DocumentsOfRecordPEODeiAttribute14 | — |
| DEI_ATTRIBUTE15 | DocumentsOfRecordPEODeiAttribute15 | — |
| DEI_ATTRIBUTE16 | DocumentsOfRecordPEODeiAttribute16 | — |
| DEI_ATTRIBUTE17 | DocumentsOfRecordPEODeiAttribute17 | — |
| DEI_ATTRIBUTE18 | DocumentsOfRecordPEODeiAttribute18 | — |
| DEI_ATTRIBUTE19 | DocumentsOfRecordPEODeiAttribute19 | — |
| DEI_ATTRIBUTE2 | DocumentsOfRecordPEODeiAttribute2 | — |
| DEI_ATTRIBUTE20 | DocumentsOfRecordPEODeiAttribute20 | — |
| DEI_ATTRIBUTE21 | DocumentsOfRecordPEODeiAttribute21 | — |
| DEI_ATTRIBUTE22 | DocumentsOfRecordPEODeiAttribute22 | — |
| DEI_ATTRIBUTE23 | DocumentsOfRecordPEODeiAttribute23 | — |
| DEI_ATTRIBUTE24 | DocumentsOfRecordPEODeiAttribute24 | — |
| DEI_ATTRIBUTE25 | DocumentsOfRecordPEODeiAttribute25 | — |
| DEI_ATTRIBUTE26 | DocumentsOfRecordPEODeiAttribute26 | — |
| DEI_ATTRIBUTE27 | DocumentsOfRecordPEODeiAttribute27 | — |
| DEI_ATTRIBUTE28 | DocumentsOfRecordPEODeiAttribute28 | — |
| DEI_ATTRIBUTE29 | DocumentsOfRecordPEODeiAttribute29 | — |
| DEI_ATTRIBUTE3 | DocumentsOfRecordPEODeiAttribute3 | — |
| DEI_ATTRIBUTE30 | DocumentsOfRecordPEODeiAttribute30 | — |
| DEI_ATTRIBUTE31 | DocumentsOfRecordPEODeiAttribute31 | — |
| DEI_ATTRIBUTE32 | DocumentsOfRecordPEODeiAttribute32 | — |
| DEI_ATTRIBUTE33 | DocumentsOfRecordPEODeiAttribute33 | — |
| DEI_ATTRIBUTE34 | DocumentsOfRecordPEODeiAttribute34 | — |
| DEI_ATTRIBUTE35 | DocumentsOfRecordPEODeiAttribute35 | — |
| DEI_ATTRIBUTE36 | DocumentsOfRecordPEODeiAttribute36 | — |
| DEI_ATTRIBUTE37 | DocumentsOfRecordPEODeiAttribute37 | — |
| DEI_ATTRIBUTE38 | DocumentsOfRecordPEODeiAttribute38 | — |
| DEI_ATTRIBUTE39 | DocumentsOfRecordPEODeiAttribute39 | — |
| DEI_ATTRIBUTE4 | DocumentsOfRecordPEODeiAttribute4 | — |
| DEI_ATTRIBUTE40 | DocumentsOfRecordPEODeiAttribute40 | — |
| DEI_ATTRIBUTE5 | DocumentsOfRecordPEODeiAttribute5 | — |
| DEI_ATTRIBUTE6 | DocumentsOfRecordPEODeiAttribute6 | — |
| DEI_ATTRIBUTE7 | DocumentsOfRecordPEODeiAttribute7 | — |
| DEI_ATTRIBUTE8 | DocumentsOfRecordPEODeiAttribute8 | — |
| DEI_ATTRIBUTE9 | DocumentsOfRecordPEODeiAttribute9 | — |
| DEI_ATTRIBUTE_CATEGORY | DocumentsOfRecordPEODeiAttributeCategory | — |
| DEI_ATTRIBUTE_DATE1 | DocumentsOfRecordPEODeiAttributeDate1 | — |
| DEI_ATTRIBUTE_DATE10 | DocumentsOfRecordPEODeiAttributeDate10 | — |
| DEI_ATTRIBUTE_DATE11 | DocumentsOfRecordPEODeiAttributeDate11 | — |
| DEI_ATTRIBUTE_DATE12 | DocumentsOfRecordPEODeiAttributeDate12 | — |
| DEI_ATTRIBUTE_DATE13 | DocumentsOfRecordPEODeiAttributeDate13 | — |
| DEI_ATTRIBUTE_DATE14 | DocumentsOfRecordPEODeiAttributeDate14 | — |
| DEI_ATTRIBUTE_DATE15 | DocumentsOfRecordPEODeiAttributeDate15 | — |
| DEI_ATTRIBUTE_DATE2 | DocumentsOfRecordPEODeiAttributeDate2 | — |
| DEI_ATTRIBUTE_DATE3 | DocumentsOfRecordPEODeiAttributeDate3 | — |
| DEI_ATTRIBUTE_DATE4 | DocumentsOfRecordPEODeiAttributeDate4 | — |
| DEI_ATTRIBUTE_DATE5 | DocumentsOfRecordPEODeiAttributeDate5 | — |
| DEI_ATTRIBUTE_DATE6 | DocumentsOfRecordPEODeiAttributeDate6 | — |
| DEI_ATTRIBUTE_DATE7 | DocumentsOfRecordPEODeiAttributeDate7 | — |
| DEI_ATTRIBUTE_DATE8 | DocumentsOfRecordPEODeiAttributeDate8 | — |
| DEI_ATTRIBUTE_DATE9 | DocumentsOfRecordPEODeiAttributeDate9 | — |
| DEI_ATTRIBUTE_NUMBER1 | DocumentsOfRecordPEODeiAttributeNumber1 | — |
| DEI_ATTRIBUTE_NUMBER10 | DocumentsOfRecordPEODeiAttributeNumber10 | — |
| DEI_ATTRIBUTE_NUMBER11 | DocumentsOfRecordPEODeiAttributeNumber11 | — |
| DEI_ATTRIBUTE_NUMBER12 | DocumentsOfRecordPEODeiAttributeNumber12 | — |
| DEI_ATTRIBUTE_NUMBER13 | DocumentsOfRecordPEODeiAttributeNumber13 | — |
| DEI_ATTRIBUTE_NUMBER14 | DocumentsOfRecordPEODeiAttributeNumber14 | — |
| DEI_ATTRIBUTE_NUMBER15 | DocumentsOfRecordPEODeiAttributeNumber15 | — |
| DEI_ATTRIBUTE_NUMBER16 | DocumentsOfRecordPEODeiAttributeNumber16 | — |
| DEI_ATTRIBUTE_NUMBER17 | DocumentsOfRecordPEODeiAttributeNumber17 | — |
| DEI_ATTRIBUTE_NUMBER18 | DocumentsOfRecordPEODeiAttributeNumber18 | — |
| DEI_ATTRIBUTE_NUMBER19 | DocumentsOfRecordPEODeiAttributeNumber19 | — |
| DEI_ATTRIBUTE_NUMBER2 | DocumentsOfRecordPEODeiAttributeNumber2 | — |
| DEI_ATTRIBUTE_NUMBER20 | DocumentsOfRecordPEODeiAttributeNumber20 | — |
| DEI_ATTRIBUTE_NUMBER3 | DocumentsOfRecordPEODeiAttributeNumber3 | — |
| DEI_ATTRIBUTE_NUMBER4 | DocumentsOfRecordPEODeiAttributeNumber4 | — |
| DEI_ATTRIBUTE_NUMBER5 | DocumentsOfRecordPEODeiAttributeNumber5 | — |
| DEI_ATTRIBUTE_NUMBER6 | DocumentsOfRecordPEODeiAttributeNumber6 | — |
| DEI_ATTRIBUTE_NUMBER7 | DocumentsOfRecordPEODeiAttributeNumber7 | — |
| DEI_ATTRIBUTE_NUMBER8 | DocumentsOfRecordPEODeiAttributeNumber8 | — |
| DEI_ATTRIBUTE_NUMBER9 | DocumentsOfRecordPEODeiAttributeNumber9 | — |
| DEI_ATTRIBUTE_TIMESTAMP1 | DocumentsOfRecordPEODeiAttributeTimestamp1 | — |
| DEI_ATTRIBUTE_TIMESTAMP2 | DocumentsOfRecordPEODeiAttributeTimestamp2 | — |
| DEI_ATTRIBUTE_TIMESTAMP3 | DocumentsOfRecordPEODeiAttributeTimestamp3 | — |
| DEI_ATTRIBUTE_TIMESTAMP4 | DocumentsOfRecordPEODeiAttributeTimestamp4 | — |
| DEI_ATTRIBUTE_TIMESTAMP5 | DocumentsOfRecordPEODeiAttributeTimestamp5 | — |
| DEI_INFORMATION1 | DocumentsOfRecordPEODeiInformation1 | — |
| DEI_INFORMATION10 | DocumentsOfRecordPEODeiInformation10 | — |
| DEI_INFORMATION11 | DocumentsOfRecordPEODeiInformation11 | — |
| DEI_INFORMATION12 | DocumentsOfRecordPEODeiInformation12 | — |
| DEI_INFORMATION13 | DocumentsOfRecordPEODeiInformation13 | — |
| DEI_INFORMATION14 | DocumentsOfRecordPEODeiInformation14 | — |
| DEI_INFORMATION15 | DocumentsOfRecordPEODeiInformation15 | — |
| DEI_INFORMATION16 | DocumentsOfRecordPEODeiInformation16 | — |
| DEI_INFORMATION17 | DocumentsOfRecordPEODeiInformation17 | — |
| DEI_INFORMATION18 | DocumentsOfRecordPEODeiInformation18 | — |
| DEI_INFORMATION19 | DocumentsOfRecordPEODeiInformation19 | — |
| DEI_INFORMATION2 | DocumentsOfRecordPEODeiInformation2 | — |
| DEI_INFORMATION20 | DocumentsOfRecordPEODeiInformation20 | — |
| DEI_INFORMATION21 | DocumentsOfRecordPEODeiInformation21 | — |
| DEI_INFORMATION22 | DocumentsOfRecordPEODeiInformation22 | — |
| DEI_INFORMATION23 | DocumentsOfRecordPEODeiInformation23 | — |
| DEI_INFORMATION24 | DocumentsOfRecordPEODeiInformation24 | — |
| DEI_INFORMATION25 | DocumentsOfRecordPEODeiInformation25 | — |
| DEI_INFORMATION26 | DocumentsOfRecordPEODeiInformation26 | — |
| DEI_INFORMATION27 | DocumentsOfRecordPEODeiInformation27 | — |
| DEI_INFORMATION28 | DocumentsOfRecordPEODeiInformation28 | — |
| DEI_INFORMATION29 | DocumentsOfRecordPEODeiInformation29 | — |
| DEI_INFORMATION3 | DocumentsOfRecordPEODeiInformation3 | — |
| DEI_INFORMATION30 | DocumentsOfRecordPEODeiInformation30 | — |
| DEI_INFORMATION31 | DocumentsOfRecordPEODeiInformation31 | — |
| DEI_INFORMATION32 | DocumentsOfRecordPEODeiInformation32 | — |
| DEI_INFORMATION33 | DocumentsOfRecordPEODeiInformation33 | — |
| DEI_INFORMATION34 | DocumentsOfRecordPEODeiInformation34 | — |
| DEI_INFORMATION35 | DocumentsOfRecordPEODeiInformation35 | — |
| DEI_INFORMATION36 | DocumentsOfRecordPEODeiInformation36 | — |
| DEI_INFORMATION37 | DocumentsOfRecordPEODeiInformation37 | — |
| DEI_INFORMATION38 | DocumentsOfRecordPEODeiInformation38 | — |
| DEI_INFORMATION39 | DocumentsOfRecordPEODeiInformation39 | — |
| DEI_INFORMATION4 | DocumentsOfRecordPEODeiInformation4 | — |
| DEI_INFORMATION40 | DocumentsOfRecordPEODeiInformation40 | — |
| DEI_INFORMATION5 | DocumentsOfRecordPEODeiInformation5 | — |
| DEI_INFORMATION6 | DocumentsOfRecordPEODeiInformation6 | — |
| DEI_INFORMATION7 | DocumentsOfRecordPEODeiInformation7 | — |
| DEI_INFORMATION8 | DocumentsOfRecordPEODeiInformation8 | — |
| DEI_INFORMATION9 | DocumentsOfRecordPEODeiInformation9 | — |
| DEI_INFORMATION_CATEGORY | DocumentsOfRecordPEODeiInformationCategory | — |
| DEI_INFORMATION_DATE1 | DocumentsOfRecordPEODeiInformationDate1 | — |
| DEI_INFORMATION_DATE10 | DocumentsOfRecordPEODeiInformationDate10 | — |
| DEI_INFORMATION_DATE11 | DocumentsOfRecordPEODeiInformationDate11 | — |
| DEI_INFORMATION_DATE12 | DocumentsOfRecordPEODeiInformationDate12 | — |
| DEI_INFORMATION_DATE13 | DocumentsOfRecordPEODeiInformationDate13 | — |
| DEI_INFORMATION_DATE14 | DocumentsOfRecordPEODeiInformationDate14 | — |
| DEI_INFORMATION_DATE15 | DocumentsOfRecordPEODeiInformationDate15 | — |
| DEI_INFORMATION_DATE2 | DocumentsOfRecordPEODeiInformationDate2 | — |
| DEI_INFORMATION_DATE3 | DocumentsOfRecordPEODeiInformationDate3 | — |
| DEI_INFORMATION_DATE4 | DocumentsOfRecordPEODeiInformationDate4 | — |
| DEI_INFORMATION_DATE5 | DocumentsOfRecordPEODeiInformationDate5 | — |
| DEI_INFORMATION_DATE6 | DocumentsOfRecordPEODeiInformationDate6 | — |
| DEI_INFORMATION_DATE7 | DocumentsOfRecordPEODeiInformationDate7 | — |
| DEI_INFORMATION_DATE8 | DocumentsOfRecordPEODeiInformationDate8 | — |
| DEI_INFORMATION_DATE9 | DocumentsOfRecordPEODeiInformationDate9 | — |
| DEI_INFORMATION_NUMBER1 | DocumentsOfRecordPEODeiInformationNumber1 | — |
| DEI_INFORMATION_NUMBER10 | DocumentsOfRecordPEODeiInformationNumber10 | — |
| DEI_INFORMATION_NUMBER11 | DocumentsOfRecordPEODeiInformationNumber11 | — |
| DEI_INFORMATION_NUMBER12 | DocumentsOfRecordPEODeiInformationNumber12 | — |
| DEI_INFORMATION_NUMBER13 | DocumentsOfRecordPEODeiInformationNumber13 | — |
| DEI_INFORMATION_NUMBER14 | DocumentsOfRecordPEODeiInformationNumber14 | — |
| DEI_INFORMATION_NUMBER15 | DocumentsOfRecordPEODeiInformationNumber15 | — |
| DEI_INFORMATION_NUMBER16 | DocumentsOfRecordPEODeiInformationNumber16 | — |
| DEI_INFORMATION_NUMBER17 | DocumentsOfRecordPEODeiInformationNumber17 | — |
| DEI_INFORMATION_NUMBER18 | DocumentsOfRecordPEODeiInformationNumber18 | — |
| DEI_INFORMATION_NUMBER19 | DocumentsOfRecordPEODeiInformationNumber19 | — |
| DEI_INFORMATION_NUMBER2 | DocumentsOfRecordPEODeiInformationNumber2 | — |
| DEI_INFORMATION_NUMBER20 | DocumentsOfRecordPEODeiInformationNumber20 | — |
| DEI_INFORMATION_NUMBER3 | DocumentsOfRecordPEODeiInformationNumber3 | — |
| DEI_INFORMATION_NUMBER4 | DocumentsOfRecordPEODeiInformationNumber4 | — |
| DEI_INFORMATION_NUMBER5 | DocumentsOfRecordPEODeiInformationNumber5 | — |
| DEI_INFORMATION_NUMBER6 | DocumentsOfRecordPEODeiInformationNumber6 | — |
| DEI_INFORMATION_NUMBER7 | DocumentsOfRecordPEODeiInformationNumber7 | — |
| DEI_INFORMATION_NUMBER8 | DocumentsOfRecordPEODeiInformationNumber8 | — |
| DEI_INFORMATION_NUMBER9 | DocumentsOfRecordPEODeiInformationNumber9 | — |
| DEI_INFORMATION_TIMESTAMP1 | DocumentsOfRecordPEODeiInformationTimestamp1 | — |
| DEI_INFORMATION_TIMESTAMP2 | DocumentsOfRecordPEODeiInformationTimestamp2 | — |
| DEI_INFORMATION_TIMESTAMP3 | DocumentsOfRecordPEODeiInformationTimestamp3 | — |
| DEI_INFORMATION_TIMESTAMP4 | DocumentsOfRecordPEODeiInformationTimestamp4 | — |
| DEI_INFORMATION_TIMESTAMP5 | DocumentsOfRecordPEODeiInformationTimestamp5 | — |
| DOCUMENT_CODE | DocumentsOfRecordPEODocumentCode | ✅ |
| DOCUMENT_NAME | DocumentsOfRecordPEODocumentName | ✅ |
| DOCUMENT_NUMBER | DocumentsOfRecordPEODocumentNumber | ✅ |
| DOCUMENT_TYPE_ID | DocumentsOfRecordPEODocumentTypeId | — |
| DOCUMENTS_OF_RECORD_ID | DocumentsOfRecordId | ✅ |
| ENTERPRISE_ID | DocumentsOfRecordPEOEnterpriseId | — |
| ISSUED_DATE | DocumentsOfRecordPEOIssuedDate | ✅ |
| ISSUING_AUTHORITY | DocumentsOfRecordPEOIssuingAuthority | ✅ |
| ISSUING_COUNTRY | DocumentsOfRecordPEOIssuingCountry | ✅ |
| ISSUING_LOCATION | DocumentsOfRecordPEOIssuingLocation | ✅ |
| LAST_UPDATE_DATE | DocumentsOfRecordPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DocumentsOfRecordPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DocumentsOfRecordPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | DocumentsOfRecordPEOObjectVersionNumber | — |
| PERSON_ID | DocumentsOfRecordPEOPersonId | — |
| PUBLISH | DocumentsOfRecordPEOPublish | — |
| PUBLISH_DATE | DocumentsOfRecordPEOPublishDate | ✅ |
| RELATED_OBJECT_ID | DocumentsOfRecordPEORelatedObjectId | ✅ |
| RELATED_OBJECT_ID_COL | DocumentsOfRecordPEORelatedObjectIdCol | ✅ |
| RELATED_OBJECT_NAME | DocumentsOfRecordPEORelatedObjectName | ✅ |
| STATUS | DocumentsOfRecordPEOStatus | ✅ |
| VERIFIED_BY | DocumentsOfRecordPEOVerifiedBy | ✅ |
| VERIFIED_DATE | DocumentsOfRecordPEOVerifiedDate | ✅ |
