---
id: DOC-OTHER-PVO-ParticipantCertificationPVO
doc_type: system-doc
title: "ParticipantCertificationPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ParticipantCertificationPVO
  - participantcertificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ParticipantCertificationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Participant Certification. Acessa as tabelas: BEN_DOCS_PRVDD_DTLS, BEN_PRTT_ENRT_CTFN_PRVDD.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.ParticipantCertificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 116 | 2 | 1 | 27 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[ben_docs_prvdd_dtls|BEN_DOCS_PRVDD_DTLS]] — 60 atributos (17 BICC)
- [[ben_prtt_enrt_ctfn_prvdd|BEN_PRTT_ENRT_CTFN_PRVDD]] — 56 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ben_docs_prvdd_dtls|BEN_DOCS_PRVDD_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentProvidedDetailsPEOApprovalEndDt | APPROVAL_END_DT | — | — |
| 2 | DocumentProvidedDetailsPEOApprovalPerdCd | APPROVAL_PERD_CD | — | — |
| 3 | DocumentProvidedDetailsPEOApprovalPerdTmNum | APPROVAL_PERD_TM_NUM | — | — |
| 4 | DocumentProvidedDetailsPEOApprovalStrtDt | APPROVAL_STRT_DT | — | — |
| 5 | DocumentProvidedDetailsPEOApprovedBy | APPROVED_BY | — | ✅ |
| 6 | DocumentProvidedDetailsPEOApprovedDt | APPROVED_DT | — | ✅ |
| 7 | DocumentProvidedDetailsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | DocumentProvidedDetailsPEOComments | COMMENTS | — | ✅ |
| 9 | DocumentProvidedDetailsPEOConfigChar1 | CONFIG_CHAR_1 | — | — |
| 10 | DocumentProvidedDetailsPEOConfigChar2 | CONFIG_CHAR_2 | — | — |
| 11 | DocumentProvidedDetailsPEOConfigChar3 | CONFIG_CHAR_3 | — | — |
| 12 | DocumentProvidedDetailsPEOConfigChar4 | CONFIG_CHAR_4 | — | — |
| 13 | DocumentProvidedDetailsPEOConfigChar5 | CONFIG_CHAR_5 | — | — |
| 14 | DocumentProvidedDetailsPEOConfigDate1 | CONFIG_DATE_1 | — | — |
| 15 | DocumentProvidedDetailsPEOConfigDate2 | CONFIG_DATE_2 | — | — |
| 16 | DocumentProvidedDetailsPEOConfigDate3 | CONFIG_DATE_3 | — | — |
| 17 | DocumentProvidedDetailsPEOConfigDate4 | CONFIG_DATE_4 | — | — |
| 18 | DocumentProvidedDetailsPEOConfigDate5 | CONFIG_DATE_5 | — | — |
| 19 | DocumentProvidedDetailsPEOConfigId1 | CONFIG_ID_1 | — | — |
| 20 | DocumentProvidedDetailsPEOConfigId2 | CONFIG_ID_2 | — | — |
| 21 | DocumentProvidedDetailsPEOConfigId3 | CONFIG_ID_3 | — | — |
| 22 | DocumentProvidedDetailsPEOConfigId4 | CONFIG_ID_4 | — | — |
| 23 | DocumentProvidedDetailsPEOConfigId5 | CONFIG_ID_5 | — | — |
| 24 | DocumentProvidedDetailsPEOConfigNum1 | CONFIG_NUM_1 | — | — |
| 25 | DocumentProvidedDetailsPEOConfigNum2 | CONFIG_NUM_2 | — | — |
| 26 | DocumentProvidedDetailsPEOConfigNum3 | CONFIG_NUM_3 | — | — |
| 27 | DocumentProvidedDetailsPEOConfigNum4 | CONFIG_NUM_4 | — | — |
| 28 | DocumentProvidedDetailsPEOConfigNum5 | CONFIG_NUM_5 | — | — |
| 29 | DocumentProvidedDetailsPEOContactPersonId | CONTACT_PERSON_ID | — | ✅ |
| 30 | DocumentProvidedDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 31 | DocumentProvidedDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 32 | DocumentProvidedDetailsPEOCtfnTypeCd | CTFN_TYPE_CD | — | ✅ |
| 33 | DocumentProvidedDetailsPEODocUsgCd | DOC_USG_CD | — | — |
| 34 | DocumentProvidedDetailsPEODocsPrvddDtlsId | DOCS_PRVDD_DTLS_ID | — | — |
| 35 | DocumentProvidedDetailsPEODocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 36 | DocumentProvidedDetailsPEODorId | DOR_ID | — | ✅ |
| 37 | DocumentProvidedDetailsPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 38 | DocumentProvidedDetailsPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 39 | DocumentProvidedDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | DocumentProvidedDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | DocumentProvidedDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | DocumentProvidedDetailsPEOMappingColumnName | MAPPING_COLUMN_NAME | — | — |
| 43 | DocumentProvidedDetailsPEOMappingTableName | MAPPING_TABLE_NAME | — | — |
| 44 | DocumentProvidedDetailsPEOMappingTablePkId | MAPPING_TABLE_PK_ID | — | — |
| 45 | DocumentProvidedDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | DocumentProvidedDetailsPEOPersonId | PERSON_ID | — | ✅ |
| 47 | DocumentProvidedDetailsPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 48 | DocumentProvidedDetailsPEOProgramName1 | PROGRAM_NAME | — | — |
| 49 | DocumentProvidedDetailsPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 50 | DocumentProvidedDetailsPEORejectedDt | REJECTED_DT | — | — |
| 51 | DocumentProvidedDetailsPEORejectionReason | REJECTION_REASON | — | ✅ |
| 52 | DocumentProvidedDetailsPEORequestId | REQUEST_ID | — | — |
| 53 | DocumentProvidedDetailsPEOStatus | STATUS | — | ✅ |
| 54 | DocumentProvidedDetailsPEOUploadedBy | UPLOADED_BY | — | — |
| 55 | DocumentProvidedDetailsPEOUploadedDt | UPLOADED_DT | — | — |
| 56 | DocumentProvidedDetailsPEOValidityCd | VALIDITY_CD | — | ✅ |
| 57 | DocumentProvidedDetailsPEOValidityEndDt | VALIDITY_END_DT | — | ✅ |
| 58 | DocumentProvidedDetailsPEOValidityStrtDt | VALIDITY_STRT_DT | — | ✅ |
| 59 | DocumentProvidedDetailsPEOValidityTmNum | VALIDITY_TM_NUM | — | ✅ |
| 60 | DocumentProvidedDetailsPEOVerificationMode | VERIFICATION_MODE | — | — |

### [[ben_prtt_enrt_ctfn_prvdd|BEN_PRTT_ENRT_CTFN_PRVDD]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParticipantCertificationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | ParticipantCertificationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ParticipantCertificationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ParticipantCertificationPEOCtfnDetermineLvlCd | CTFN_DETERMINE_LVL_CD | — | ✅ |
| 5 | ParticipantCertificationPEOCvrdEnrtCtfnDndDt | CVRD_ENRT_CTFN_DND_DT | — | ✅ |
| 6 | ParticipantCertificationPEOCvrdEnrtCtfnRecdDt | CVRD_ENRT_CTFN_RECD_DT | — | ✅ |
| 7 | ParticipantCertificationPEOEndedPerInLerId | ENDED_PER_IN_LER_ID | — | — |
| 8 | ParticipantCertificationPEOEnrtCtfnDndDt | ENRT_CTFN_DND_DT | — | ✅ |
| 9 | ParticipantCertificationPEOEnrtCtfnRecdDt | ENRT_CTFN_RECD_DT | — | ✅ |
| 10 | ParticipantCertificationPEOEnrtCtfnRqdFlag | ENRT_CTFN_RQD_FLAG | — | ✅ |
| 11 | ParticipantCertificationPEOEnrtCtfnTypCd | ENRT_CTFN_TYP_CD | — | ✅ |
| 12 | ParticipantCertificationPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 13 | ParticipantCertificationPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 14 | ParticipantCertificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ParticipantCertificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ParticipantCertificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ParticipantCertificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ParticipantCertificationPEOPcsAttribute1 | PCS_ATTRIBUTE1 | — | — |
| 19 | ParticipantCertificationPEOPcsAttribute10 | PCS_ATTRIBUTE10 | — | — |
| 20 | ParticipantCertificationPEOPcsAttribute11 | PCS_ATTRIBUTE11 | — | — |
| 21 | ParticipantCertificationPEOPcsAttribute12 | PCS_ATTRIBUTE12 | — | — |
| 22 | ParticipantCertificationPEOPcsAttribute13 | PCS_ATTRIBUTE13 | — | — |
| 23 | ParticipantCertificationPEOPcsAttribute14 | PCS_ATTRIBUTE14 | — | — |
| 24 | ParticipantCertificationPEOPcsAttribute15 | PCS_ATTRIBUTE15 | — | — |
| 25 | ParticipantCertificationPEOPcsAttribute16 | PCS_ATTRIBUTE16 | — | — |
| 26 | ParticipantCertificationPEOPcsAttribute17 | PCS_ATTRIBUTE17 | — | — |
| 27 | ParticipantCertificationPEOPcsAttribute18 | PCS_ATTRIBUTE18 | — | — |
| 28 | ParticipantCertificationPEOPcsAttribute19 | PCS_ATTRIBUTE19 | — | — |
| 29 | ParticipantCertificationPEOPcsAttribute2 | PCS_ATTRIBUTE2 | — | — |
| 30 | ParticipantCertificationPEOPcsAttribute20 | PCS_ATTRIBUTE20 | — | — |
| 31 | ParticipantCertificationPEOPcsAttribute21 | PCS_ATTRIBUTE21 | — | — |
| 32 | ParticipantCertificationPEOPcsAttribute22 | PCS_ATTRIBUTE22 | — | — |
| 33 | ParticipantCertificationPEOPcsAttribute23 | PCS_ATTRIBUTE23 | — | — |
| 34 | ParticipantCertificationPEOPcsAttribute24 | PCS_ATTRIBUTE24 | — | — |
| 35 | ParticipantCertificationPEOPcsAttribute25 | PCS_ATTRIBUTE25 | — | — |
| 36 | ParticipantCertificationPEOPcsAttribute26 | PCS_ATTRIBUTE26 | — | — |
| 37 | ParticipantCertificationPEOPcsAttribute27 | PCS_ATTRIBUTE27 | — | — |
| 38 | ParticipantCertificationPEOPcsAttribute28 | PCS_ATTRIBUTE28 | — | — |
| 39 | ParticipantCertificationPEOPcsAttribute29 | PCS_ATTRIBUTE29 | — | — |
| 40 | ParticipantCertificationPEOPcsAttribute3 | PCS_ATTRIBUTE3 | — | — |
| 41 | ParticipantCertificationPEOPcsAttribute30 | PCS_ATTRIBUTE30 | — | — |
| 42 | ParticipantCertificationPEOPcsAttribute4 | PCS_ATTRIBUTE4 | — | — |
| 43 | ParticipantCertificationPEOPcsAttribute5 | PCS_ATTRIBUTE5 | — | — |
| 44 | ParticipantCertificationPEOPcsAttribute6 | PCS_ATTRIBUTE6 | — | — |
| 45 | ParticipantCertificationPEOPcsAttribute7 | PCS_ATTRIBUTE7 | — | — |
| 46 | ParticipantCertificationPEOPcsAttribute8 | PCS_ATTRIBUTE8 | — | — |
| 47 | ParticipantCertificationPEOPcsAttribute9 | PCS_ATTRIBUTE9 | — | — |
| 48 | ParticipantCertificationPEOPcsAttributeCategory | PCS_ATTRIBUTE_CATEGORY | — | — |
| 49 | ParticipantCertificationPEOPerInLerId | PER_IN_LER_ID | — | — |
| 50 | ParticipantCertificationPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 51 | ParticipantCertificationPEOProgramName | PROGRAM_NAME | — | — |
| 52 | ParticipantCertificationPEOProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 53 | ParticipantCertificationPEOPrttEnrtActnId | PRTT_ENRT_ACTN_ID | — | ✅ |
| 54 | ParticipantCertificationPEOPrttEnrtCtfnPrvddId | PRTT_ENRT_CTFN_PRVDD_ID | 🔑 | ✅ |
| 55 | ParticipantCertificationPEOPrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | — |
| 56 | ParticipantCertificationPEORequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
