---
id: DOC-HCM-276
doc_type: system-doc
title: "HR_DOCUMENTS_OF_RECORD — Documentos de Registro"
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
  - compliance
  - pessoal
aliases:
  - HR_DOCUMENTS_OF_RECORD
  - hr_documents_of_record
  - hr-documents-of-record
  - documents-of-record
  - documentos-registro
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_DOCUMENTS_OF_RECORD

## 📌 Visao Geral

Armazena os **documentos de registro** (documents of record) dos colaboradores — carteira de identidade, passaporte, certidoes, diplomas e outros documentos legais/pessoais.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Compliance:** Manter documentos obrigatorios de colaboradores.
- **Vencimento:** Controlar validade de documentos.
- **Auditoria:** Rastrear documentos entregues por colaboradores.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DOCUMENTS_OF_RECORD_ID | NUMBER(18) | NOT NULL | PK | Identificador do documento | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador proprietario | [[per_all_people_f]] | 🟢 95% |
| 3 | DOCUMENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de documento | [[hr_document_types_b]] | 🟢 95% |
| 4 | DOCUMENT_NUMBER | VARCHAR2(150) | NULL | Dados | Numero do documento | — | 🟢 90% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de emissao | — | 🟢 90% |
| 6 | DATE_TO | DATE | NULL | Data | Data de vencimento | — | 🟢 90% |
| 7 | ISSUING_AUTHORITY | VARCHAR2(240) | NULL | Dados | Autoridade emissora | — | 🟡 80% |
| 8 | ISSUING_COUNTRY | VARCHAR2(30) | NULL | Dados | Pais de emissao | — | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do documento registrado)
- [[hr_document_types_b]] — via `DOCUMENT_TYPE_ID` (tipo do documento registrado)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Documentos de um colaborador
```sql
SELECT dor.DOCUMENT_NUMBER, dor.DATE_FROM, dor.DATE_TO
FROM   HR_DOCUMENTS_OF_RECORD dor
WHERE  dor.PERSON_ID = :p_person_id;
```

---

## 🔒 Observacoes

- Pode conter dados sensiveis (PII) — aplicar controle de acesso.
- DATE_TO indica vencimento — documentos vencidos devem gerar alertas.

---

## 📚 Referencias

- [Oracle Docs — HR_DOCUMENTS_OF_RECORD](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrdocumentsofrecord.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[documentsofrecordextractpvo|DocumentsOfRecordExtractPVO]] (HCM · BICC: 30/192)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CREATION_SOURCE | CreationSource | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DEI_ATTRIBUTE1 | DeiAttribute1 | — |
| DEI_ATTRIBUTE10 | DeiAttribute10 | — |
| DEI_ATTRIBUTE11 | DeiAttribute11 | — |
| DEI_ATTRIBUTE12 | DeiAttribute12 | — |
| DEI_ATTRIBUTE13 | DeiAttribute13 | — |
| DEI_ATTRIBUTE14 | DeiAttribute14 | — |
| DEI_ATTRIBUTE15 | DeiAttribute15 | — |
| DEI_ATTRIBUTE16 | DeiAttribute16 | — |
| DEI_ATTRIBUTE17 | DeiAttribute17 | — |
| DEI_ATTRIBUTE18 | DeiAttribute18 | — |
| DEI_ATTRIBUTE19 | DeiAttribute19 | — |
| DEI_ATTRIBUTE2 | DeiAttribute2 | — |
| DEI_ATTRIBUTE20 | DeiAttribute20 | — |
| DEI_ATTRIBUTE21 | DeiAttribute21 | — |
| DEI_ATTRIBUTE22 | DeiAttribute22 | — |
| DEI_ATTRIBUTE23 | DeiAttribute23 | — |
| DEI_ATTRIBUTE24 | DeiAttribute24 | — |
| DEI_ATTRIBUTE25 | DeiAttribute25 | — |
| DEI_ATTRIBUTE26 | DeiAttribute26 | — |
| DEI_ATTRIBUTE27 | DeiAttribute27 | — |
| DEI_ATTRIBUTE28 | DeiAttribute28 | — |
| DEI_ATTRIBUTE29 | DeiAttribute29 | — |
| DEI_ATTRIBUTE3 | DeiAttribute3 | — |
| DEI_ATTRIBUTE30 | DeiAttribute30 | — |
| DEI_ATTRIBUTE31 | DeiAttribute31 | — |
| DEI_ATTRIBUTE32 | DeiAttribute32 | — |
| DEI_ATTRIBUTE33 | DeiAttribute33 | — |
| DEI_ATTRIBUTE34 | DeiAttribute34 | — |
| DEI_ATTRIBUTE35 | DeiAttribute35 | — |
| DEI_ATTRIBUTE36 | DeiAttribute36 | — |
| DEI_ATTRIBUTE37 | DeiAttribute37 | — |
| DEI_ATTRIBUTE38 | DeiAttribute38 | — |
| DEI_ATTRIBUTE39 | DeiAttribute39 | — |
| DEI_ATTRIBUTE4 | DeiAttribute4 | — |
| DEI_ATTRIBUTE40 | DeiAttribute40 | — |
| DEI_ATTRIBUTE5 | DeiAttribute5 | — |
| DEI_ATTRIBUTE6 | DeiAttribute6 | — |
| DEI_ATTRIBUTE7 | DeiAttribute7 | — |
| DEI_ATTRIBUTE8 | DeiAttribute8 | — |
| DEI_ATTRIBUTE9 | DeiAttribute9 | — |
| DEI_ATTRIBUTE_CATEGORY | DeiAttributeCategory | — |
| DEI_ATTRIBUTE_DATE1 | DeiAttributeDate1 | — |
| DEI_ATTRIBUTE_DATE10 | DeiAttributeDate10 | — |
| DEI_ATTRIBUTE_DATE11 | DeiAttributeDate11 | — |
| DEI_ATTRIBUTE_DATE12 | DeiAttributeDate12 | — |
| DEI_ATTRIBUTE_DATE13 | DeiAttributeDate13 | — |
| DEI_ATTRIBUTE_DATE14 | DeiAttributeDate14 | — |
| DEI_ATTRIBUTE_DATE15 | DeiAttributeDate15 | — |
| DEI_ATTRIBUTE_DATE2 | DeiAttributeDate2 | — |
| DEI_ATTRIBUTE_DATE3 | DeiAttributeDate3 | — |
| DEI_ATTRIBUTE_DATE4 | DeiAttributeDate4 | — |
| DEI_ATTRIBUTE_DATE5 | DeiAttributeDate5 | — |
| DEI_ATTRIBUTE_DATE6 | DeiAttributeDate6 | — |
| DEI_ATTRIBUTE_DATE7 | DeiAttributeDate7 | — |
| DEI_ATTRIBUTE_DATE8 | DeiAttributeDate8 | — |
| DEI_ATTRIBUTE_DATE9 | DeiAttributeDate9 | — |
| DEI_ATTRIBUTE_NUMBER1 | DeiAttributeNumber1 | — |
| DEI_ATTRIBUTE_NUMBER10 | DeiAttributeNumber10 | — |
| DEI_ATTRIBUTE_NUMBER11 | DeiAttributeNumber11 | — |
| DEI_ATTRIBUTE_NUMBER12 | DeiAttributeNumber12 | — |
| DEI_ATTRIBUTE_NUMBER13 | DeiAttributeNumber13 | — |
| DEI_ATTRIBUTE_NUMBER14 | DeiAttributeNumber14 | — |
| DEI_ATTRIBUTE_NUMBER15 | DeiAttributeNumber15 | — |
| DEI_ATTRIBUTE_NUMBER16 | DeiAttributeNumber16 | — |
| DEI_ATTRIBUTE_NUMBER17 | DeiAttributeNumber17 | — |
| DEI_ATTRIBUTE_NUMBER18 | DeiAttributeNumber18 | — |
| DEI_ATTRIBUTE_NUMBER19 | DeiAttributeNumber19 | — |
| DEI_ATTRIBUTE_NUMBER2 | DeiAttributeNumber2 | — |
| DEI_ATTRIBUTE_NUMBER20 | DeiAttributeNumber20 | — |
| DEI_ATTRIBUTE_NUMBER3 | DeiAttributeNumber3 | — |
| DEI_ATTRIBUTE_NUMBER4 | DeiAttributeNumber4 | — |
| DEI_ATTRIBUTE_NUMBER5 | DeiAttributeNumber5 | — |
| DEI_ATTRIBUTE_NUMBER6 | DeiAttributeNumber6 | — |
| DEI_ATTRIBUTE_NUMBER7 | DeiAttributeNumber7 | — |
| DEI_ATTRIBUTE_NUMBER8 | DeiAttributeNumber8 | — |
| DEI_ATTRIBUTE_NUMBER9 | DeiAttributeNumber9 | — |
| DEI_ATTRIBUTE_TIMESTAMP1 | DeiAttributeTimestamp1 | — |
| DEI_ATTRIBUTE_TIMESTAMP2 | DeiAttributeTimestamp2 | — |
| DEI_ATTRIBUTE_TIMESTAMP3 | DeiAttributeTimestamp3 | — |
| DEI_ATTRIBUTE_TIMESTAMP4 | DeiAttributeTimestamp4 | — |
| DEI_ATTRIBUTE_TIMESTAMP5 | DeiAttributeTimestamp5 | — |
| DEI_INFORMATION1 | DeiInformation1 | — |
| DEI_INFORMATION10 | DeiInformation10 | — |
| DEI_INFORMATION11 | DeiInformation11 | — |
| DEI_INFORMATION12 | DeiInformation12 | — |
| DEI_INFORMATION13 | DeiInformation13 | — |
| DEI_INFORMATION14 | DeiInformation14 | — |
| DEI_INFORMATION15 | DeiInformation15 | — |
| DEI_INFORMATION16 | DeiInformation16 | — |
| DEI_INFORMATION17 | DeiInformation17 | — |
| DEI_INFORMATION18 | DeiInformation18 | — |
| DEI_INFORMATION19 | DeiInformation19 | — |
| DEI_INFORMATION2 | DeiInformation2 | — |
| DEI_INFORMATION20 | DeiInformation20 | — |
| DEI_INFORMATION21 | DeiInformation21 | — |
| DEI_INFORMATION22 | DeiInformation22 | — |
| DEI_INFORMATION23 | DeiInformation23 | — |
| DEI_INFORMATION24 | DeiInformation24 | — |
| DEI_INFORMATION25 | DeiInformation25 | — |
| DEI_INFORMATION26 | DeiInformation26 | — |
| DEI_INFORMATION27 | DeiInformation27 | — |
| DEI_INFORMATION28 | DeiInformation28 | — |
| DEI_INFORMATION29 | DeiInformation29 | — |
| DEI_INFORMATION3 | DeiInformation3 | — |
| DEI_INFORMATION30 | DeiInformation30 | — |
| DEI_INFORMATION31 | DeiInformation31 | — |
| DEI_INFORMATION32 | DeiInformation32 | — |
| DEI_INFORMATION33 | DeiInformation33 | — |
| DEI_INFORMATION34 | DeiInformation34 | — |
| DEI_INFORMATION35 | DeiInformation35 | — |
| DEI_INFORMATION36 | DeiInformation36 | — |
| DEI_INFORMATION37 | DeiInformation37 | — |
| DEI_INFORMATION38 | DeiInformation38 | — |
| DEI_INFORMATION39 | DeiInformation39 | — |
| DEI_INFORMATION4 | DeiInformation4 | — |
| DEI_INFORMATION40 | DeiInformation40 | — |
| DEI_INFORMATION5 | DeiInformation5 | — |
| DEI_INFORMATION6 | DeiInformation6 | — |
| DEI_INFORMATION7 | DeiInformation7 | — |
| DEI_INFORMATION8 | DeiInformation8 | — |
| DEI_INFORMATION9 | DeiInformation9 | — |
| DEI_INFORMATION_CATEGORY | DeiInformationCategory | — |
| DEI_INFORMATION_DATE1 | DeiInformationDate1 | — |
| DEI_INFORMATION_DATE10 | DeiInformationDate10 | — |
| DEI_INFORMATION_DATE11 | DeiInformationDate11 | — |
| DEI_INFORMATION_DATE12 | DeiInformationDate12 | — |
| DEI_INFORMATION_DATE13 | DeiInformationDate13 | — |
| DEI_INFORMATION_DATE14 | DeiInformationDate14 | — |
| DEI_INFORMATION_DATE15 | DeiInformationDate15 | — |
| DEI_INFORMATION_DATE2 | DeiInformationDate2 | — |
| DEI_INFORMATION_DATE3 | DeiInformationDate3 | — |
| DEI_INFORMATION_DATE4 | DeiInformationDate4 | — |
| DEI_INFORMATION_DATE5 | DeiInformationDate5 | — |
| DEI_INFORMATION_DATE6 | DeiInformationDate6 | — |
| DEI_INFORMATION_DATE7 | DeiInformationDate7 | — |
| DEI_INFORMATION_DATE8 | DeiInformationDate8 | — |
| DEI_INFORMATION_DATE9 | DeiInformationDate9 | — |
| DEI_INFORMATION_NUMBER1 | DeiInformationNumber1 | — |
| DEI_INFORMATION_NUMBER10 | DeiInformationNumber10 | — |
| DEI_INFORMATION_NUMBER11 | DeiInformationNumber11 | — |
| DEI_INFORMATION_NUMBER12 | DeiInformationNumber12 | — |
| DEI_INFORMATION_NUMBER13 | DeiInformationNumber13 | — |
| DEI_INFORMATION_NUMBER14 | DeiInformationNumber14 | — |
| DEI_INFORMATION_NUMBER15 | DeiInformationNumber15 | — |
| DEI_INFORMATION_NUMBER16 | DeiInformationNumber16 | — |
| DEI_INFORMATION_NUMBER17 | DeiInformationNumber17 | — |
| DEI_INFORMATION_NUMBER18 | DeiInformationNumber18 | — |
| DEI_INFORMATION_NUMBER19 | DeiInformationNumber19 | — |
| DEI_INFORMATION_NUMBER2 | DeiInformationNumber2 | — |
| DEI_INFORMATION_NUMBER20 | DeiInformationNumber20 | — |
| DEI_INFORMATION_NUMBER3 | DeiInformationNumber3 | — |
| DEI_INFORMATION_NUMBER4 | DeiInformationNumber4 | — |
| DEI_INFORMATION_NUMBER5 | DeiInformationNumber5 | — |
| DEI_INFORMATION_NUMBER6 | DeiInformationNumber6 | — |
| DEI_INFORMATION_NUMBER7 | DeiInformationNumber7 | — |
| DEI_INFORMATION_NUMBER8 | DeiInformationNumber8 | — |
| DEI_INFORMATION_NUMBER9 | DeiInformationNumber9 | — |
| DEI_INFORMATION_TIMESTAMP1 | DeiInformationTimestamp1 | — |
| DEI_INFORMATION_TIMESTAMP2 | DeiInformationTimestamp2 | — |
| DEI_INFORMATION_TIMESTAMP3 | DeiInformationTimestamp3 | — |
| DEI_INFORMATION_TIMESTAMP4 | DeiInformationTimestamp4 | — |
| DEI_INFORMATION_TIMESTAMP5 | DeiInformationTimestamp5 | — |
| DOCUMENT_CODE | DocumentCode | ✅ |
| DOCUMENT_NAME | DocumentName | ✅ |
| DOCUMENT_NUMBER | DocumentNumber | ✅ |
| DOCUMENT_TYPE_ID | DocumentTypeId | ✅ |
| DOCUMENTS_OF_RECORD_ID | DocumentsOfRecordId | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| ISSUED_DATE | IssuedDate | ✅ |
| ISSUING_AUTHORITY | IssuingAuthority | ✅ |
| ISSUING_COUNTRY | IssuingCountry | ✅ |
| ISSUING_LOCATION | IssuingLocation | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ID | PersonId | ✅ |
| PUBLISH | Publish | ✅ |
| PUBLISH_DATE | PublishDate | ✅ |
| RELATED_OBJECT_ID | RelatedObjectId | ✅ |
| RELATED_OBJECT_ID_COL | RelatedObjectIdCol | ✅ |
| RELATED_OBJECT_NAME | RelatedObjectName | ✅ |
| STATUS | Status | ✅ |
| VERIFIED_BY | VerifiedBy | ✅ |
| VERIFIED_DATE | VerifiedDate | ✅ |
