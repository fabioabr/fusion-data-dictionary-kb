---
id: DOC-HCM-PVO-FeedbackDetailsPVO
doc_type: system-doc
title: "FeedbackDetailsPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
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
  - pvo
  - bicc
aliases:
  - FeedbackDetailsPVO
  - feedbackdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FeedbackDetailsPVO

## 📌 Visão Geral

Consolida detalhes de feedback de entrevistas de recrutamento, incluindo questionários e participantes. Suporta análise qualitativa do processo seletivo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringIntrMgmtAM.FeedbackDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 882 | 11 | 1 | 79 | 9% |

---

## 🔗 Tabelas Relacionadas

- [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]] — 26 atributos (10 BICC)
- [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]] — 15 atributos (7 BICC)
- [[irc_im_feedbacks|IRC_IM_FEEDBACKS]] — 10 atributos (1 PKs, 9 BICC)
- [[irc_im_feedbk_partcpts|IRC_IM_FEEDBK_PARTCPTS]] — 12 atributos (4 BICC)
- [[irc_im_feedbk_requests|IRC_IM_FEEDBK_REQUESTS]] — 21 atributos (9 BICC)
- [[irc_im_feedbk_reviews|IRC_IM_FEEDBK_REVIEWS]] — 8 atributos (3 BICC)
- [[irc_im_req_qstnrs|IRC_IM_REQ_QSTNRS]] — 4 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 210 atributos (7 BICC)
- [[per_email_addresses|PER_EMAIL_ADDRESSES]] — 160 atributos (6 BICC)
- [[per_persons|PER_PERSONS]] — 168 atributos (8 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 248 atributos (16 BICC)

---

## ⚙️ Atributos

### [[hrq_questionnaires_b|HRQ_QUESTIONNAIRES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CategoryId | CATEGORY_ID | — | — |
| 3 | CreatedBy4 | CREATED_BY | — | — |
| 4 | CreationDate4 | CREATION_DATE | — | — |
| 5 | InUse | IN_USE | — | ✅ |
| 6 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 9 | LatestVersion | LATEST_VERSION | — | — |
| 10 | ModuleId | MODULE_ID | — | — |
| 11 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 12 | Owner | OWNER | — | ✅ |
| 13 | PageLayout | PAGE_LAYOUT | — | — |
| 14 | PrivacyFlag | PRIVACY_FLAG | — | ✅ |
| 15 | QstnrTemplateId | QSTNR_TEMPLATE_ID | — | — |
| 16 | QstnrVersionNum2 | QSTNR_VERSION_NUM | — | — |
| 17 | QstnsPerPage | QSTNS_PER_PAGE | — | ✅ |
| 18 | QuestionnaireCode | QUESTIONNAIRE_CODE | — | ✅ |
| 19 | QuestionnaireId2 | QUESTIONNAIRE_ID | — | — |
| 20 | SectionOrder | SECTION_ORDER | — | ✅ |
| 21 | SectionPresentation | SECTION_PRESENTATION | — | ✅ |
| 22 | Status | STATUS | — | ✅ |
| 23 | SubscriberId | SUBSCRIBER_ID | — | — |
| 24 | TemplateFlag | TEMPLATE_FLAG | — | — |
| 25 | UpdateAllowed | UPDATE_ALLOWED | — | — |
| 26 | VersionDescription | VERSION_DESCRIPTION | — | ✅ |

### [[hrq_questionnaires_tl|HRQ_QUESTIONNAIRES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | CreatedBy5 | CREATED_BY | — | — |
| 3 | CreationDate5 | CREATION_DATE | — | — |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | IntroText | INTRO_TEXT | — | ✅ |
| 6 | Keywords | KEYWORDS | — | ✅ |
| 7 | Language | LANGUAGE | — | ✅ |
| 8 | LastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin5 | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy5 | LAST_UPDATED_BY | — | — |
| 11 | Name | NAME | — | ✅ |
| 12 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 13 | QstnrVersionNum3 | QSTNR_VERSION_NUM | — | — |
| 14 | QuestionnaireId3 | QUESTIONNAIRE_ID | — | — |
| 15 | SourceLang | SOURCE_LANG | — | ✅ |

### [[irc_im_feedbacks|IRC_IM_FEEDBACKS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | FeedbackId | FEEDBACK_ID | 🔑 | ✅ |
| 4 | FeedbackTypeCode | FEEDBACK_TYPE_CODE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RequisitionId | REQUISITION_ID | — | — |
| 10 | SubmissionId | SUBMISSION_ID | — | ✅ |

### [[irc_im_feedbk_partcpts|IRC_IM_FEEDBK_PARTCPTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy1 | CREATED_BY | — | — |
| 2 | CreationDate1 | CREATION_DATE | — | — |
| 3 | FeedbackId1 | FEEDBACK_ID | — | — |
| 4 | FeedbackParticipantId | FEEDBACK_PARTICIPANT_ID | — | ✅ |
| 5 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 8 | Notes | NOTES | — | ✅ |
| 9 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 10 | ParticipantId | PARTICIPANT_ID | — | — |
| 11 | QstnrVersionNum | QSTNR_VERSION_NUM | — | — |
| 12 | QuestionnaireId | QUESTIONNAIRE_ID | — | ✅ |

### [[irc_im_feedbk_requests|IRC_IM_FEEDBK_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CancelDate | CANCEL_DATE | — | ✅ |
| 2 | CompletionDate | COMPLETION_DATE | — | ✅ |
| 3 | CreatedBy3 | CREATED_BY | — | — |
| 4 | CreationDate3 | CREATION_DATE | — | — |
| 5 | DueDate | DUE_DATE | — | ✅ |
| 6 | ExpiryDate | EXPIRY_DATE | — | ✅ |
| 7 | FeedbackId2 | FEEDBACK_ID | — | — |
| 8 | FeedbackRequestId1 | FEEDBACK_REQUEST_ID | — | — |
| 9 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 12 | ObjectStatus | OBJECT_STATUS | — | ✅ |
| 13 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 14 | ParticipantId1 | PARTICIPANT_ID | — | — |
| 15 | QstnrVersionNum1 | QSTNR_VERSION_NUM | — | — |
| 16 | QuestionnaireId1 | QUESTIONNAIRE_ID | — | — |
| 17 | RenewCount | RENEW_COUNT | — | ✅ |
| 18 | RenewDate | RENEW_DATE | — | ✅ |
| 19 | RequisitionId1 | REQUISITION_ID | — | — |
| 20 | ResendCount | RESEND_COUNT | — | — |
| 21 | StatusTypeCode | STATUS_TYPE_CODE | — | ✅ |

### [[irc_im_feedbk_reviews|IRC_IM_FEEDBK_REVIEWS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy2 | CREATED_BY | — | — |
| 2 | CreationDate2 | CREATION_DATE | — | — |
| 3 | FeedbackRequestId | FEEDBACK_REQUEST_ID | — | ✅ |
| 4 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 7 | PersonId | PERSON_ID | — | — |
| 8 | ReviewDate | REVIEW_DATE | — | ✅ |

### [[irc_im_req_qstnrs|IRC_IM_REQ_QSTNRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QstnrTypeCode | QSTNR_TYPE_CODE | — | — |
| 2 | QstnrVersionNum4 | QSTNR_VERSION_NUM | — | — |
| 3 | QuestionnaireId4 | QUESTIONNAIRE_ID | — | — |
| 4 | RequisitionId2 | REQUISITION_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicantNumber | APPLICANT_NUMBER | — | ✅ |
| 2 | ApplicantNumber1 | APPLICANT_NUMBER | — | — |
| 3 | Attribute104 | ATTRIBUTE10 | — | — |
| 4 | Attribute106 | ATTRIBUTE10 | — | — |
| 5 | Attribute1110 | ATTRIBUTE11 | — | — |
| 6 | Attribute116 | ATTRIBUTE1 | — | — |
| 7 | Attribute117 | ATTRIBUTE11 | — | — |
| 8 | Attribute120 | ATTRIBUTE1 | — | — |
| 9 | Attribute124 | ATTRIBUTE12 | — | — |
| 10 | Attribute126 | ATTRIBUTE12 | — | — |
| 11 | Attribute134 | ATTRIBUTE13 | — | — |
| 12 | Attribute136 | ATTRIBUTE13 | — | — |
| 13 | Attribute144 | ATTRIBUTE14 | — | — |
| 14 | Attribute146 | ATTRIBUTE14 | — | — |
| 15 | Attribute154 | ATTRIBUTE15 | — | — |
| 16 | Attribute156 | ATTRIBUTE15 | — | — |
| 17 | Attribute164 | ATTRIBUTE16 | — | — |
| 18 | Attribute166 | ATTRIBUTE16 | — | — |
| 19 | Attribute174 | ATTRIBUTE17 | — | — |
| 20 | Attribute176 | ATTRIBUTE17 | — | — |
| 21 | Attribute184 | ATTRIBUTE18 | — | — |
| 22 | Attribute186 | ATTRIBUTE18 | — | — |
| 23 | Attribute194 | ATTRIBUTE19 | — | — |
| 24 | Attribute196 | ATTRIBUTE19 | — | — |
| 25 | Attribute204 | ATTRIBUTE20 | — | — |
| 26 | Attribute206 | ATTRIBUTE20 | — | — |
| 27 | Attribute2110 | ATTRIBUTE21 | — | — |
| 28 | Attribute216 | ATTRIBUTE2 | — | — |
| 29 | Attribute217 | ATTRIBUTE21 | — | — |
| 30 | Attribute220 | ATTRIBUTE2 | — | — |
| 31 | Attribute224 | ATTRIBUTE22 | — | — |
| 32 | Attribute226 | ATTRIBUTE22 | — | — |
| 33 | Attribute234 | ATTRIBUTE23 | — | — |
| 34 | Attribute236 | ATTRIBUTE23 | — | — |
| 35 | Attribute244 | ATTRIBUTE24 | — | — |
| 36 | Attribute246 | ATTRIBUTE24 | — | — |
| 37 | Attribute254 | ATTRIBUTE25 | — | — |
| 38 | Attribute256 | ATTRIBUTE25 | — | — |
| 39 | Attribute264 | ATTRIBUTE26 | — | — |
| 40 | Attribute266 | ATTRIBUTE26 | — | — |
| 41 | Attribute274 | ATTRIBUTE27 | — | — |
| 42 | Attribute276 | ATTRIBUTE27 | — | — |
| 43 | Attribute284 | ATTRIBUTE28 | — | — |
| 44 | Attribute286 | ATTRIBUTE28 | — | — |
| 45 | Attribute294 | ATTRIBUTE29 | — | — |
| 46 | Attribute296 | ATTRIBUTE29 | — | — |
| 47 | Attribute304 | ATTRIBUTE30 | — | — |
| 48 | Attribute306 | ATTRIBUTE30 | — | — |
| 49 | Attribute311 | ATTRIBUTE31 | — | — |
| 50 | Attribute312 | ATTRIBUTE3 | — | — |
| 51 | Attribute313 | ATTRIBUTE31 | — | — |
| 52 | Attribute321 | ATTRIBUTE32 | — | — |
| 53 | Attribute322 | ATTRIBUTE32 | — | — |
| 54 | Attribute331 | ATTRIBUTE33 | — | — |
| 55 | Attribute332 | ATTRIBUTE33 | — | — |
| 56 | Attribute34 | ATTRIBUTE3 | — | — |
| 57 | Attribute341 | ATTRIBUTE34 | — | — |
| 58 | Attribute342 | ATTRIBUTE34 | — | — |
| 59 | Attribute35 | ATTRIBUTE35 | — | — |
| 60 | Attribute351 | ATTRIBUTE35 | — | — |
| 61 | Attribute36 | ATTRIBUTE36 | — | — |
| 62 | Attribute361 | ATTRIBUTE36 | — | — |
| 63 | Attribute37 | ATTRIBUTE37 | — | — |
| 64 | Attribute371 | ATTRIBUTE37 | — | — |
| 65 | Attribute38 | ATTRIBUTE38 | — | — |
| 66 | Attribute381 | ATTRIBUTE38 | — | — |
| 67 | Attribute39 | ATTRIBUTE39 | — | — |
| 68 | Attribute391 | ATTRIBUTE39 | — | — |
| 69 | Attribute40 | ATTRIBUTE40 | — | — |
| 70 | Attribute401 | ATTRIBUTE40 | — | — |
| 71 | Attribute411 | ATTRIBUTE41 | — | — |
| 72 | Attribute412 | ATTRIBUTE4 | — | — |
| 73 | Attribute413 | ATTRIBUTE41 | — | — |
| 74 | Attribute421 | ATTRIBUTE42 | — | — |
| 75 | Attribute422 | ATTRIBUTE42 | — | — |
| 76 | Attribute431 | ATTRIBUTE43 | — | — |
| 77 | Attribute432 | ATTRIBUTE43 | — | — |
| 78 | Attribute44 | ATTRIBUTE4 | — | — |
| 79 | Attribute441 | ATTRIBUTE44 | — | — |
| 80 | Attribute442 | ATTRIBUTE44 | — | — |
| 81 | Attribute45 | ATTRIBUTE45 | — | — |
| 82 | Attribute451 | ATTRIBUTE45 | — | — |
| 83 | Attribute46 | ATTRIBUTE46 | — | — |
| 84 | Attribute461 | ATTRIBUTE46 | — | — |
| 85 | Attribute47 | ATTRIBUTE47 | — | — |
| 86 | Attribute471 | ATTRIBUTE47 | — | — |
| 87 | Attribute48 | ATTRIBUTE48 | — | — |
| 88 | Attribute481 | ATTRIBUTE48 | — | — |
| 89 | Attribute49 | ATTRIBUTE49 | — | — |
| 90 | Attribute491 | ATTRIBUTE49 | — | — |
| 91 | Attribute50 | ATTRIBUTE50 | — | — |
| 92 | Attribute501 | ATTRIBUTE50 | — | — |
| 93 | Attribute54 | ATTRIBUTE5 | — | — |
| 94 | Attribute56 | ATTRIBUTE5 | — | — |
| 95 | Attribute64 | ATTRIBUTE6 | — | — |
| 96 | Attribute66 | ATTRIBUTE6 | — | — |
| 97 | Attribute74 | ATTRIBUTE7 | — | — |
| 98 | Attribute76 | ATTRIBUTE7 | — | — |
| 99 | Attribute84 | ATTRIBUTE8 | — | — |
| 100 | Attribute86 | ATTRIBUTE8 | — | — |
| 101 | Attribute94 | ATTRIBUTE9 | — | — |
| 102 | Attribute96 | ATTRIBUTE9 | — | — |
| 103 | AttributeCategory4 | ATTRIBUTE_CATEGORY | — | — |
| 104 | AttributeCategory6 | ATTRIBUTE_CATEGORY | — | — |
| 105 | AttributeDate104 | ATTRIBUTE_DATE10 | — | — |
| 106 | AttributeDate106 | ATTRIBUTE_DATE10 | — | — |
| 107 | AttributeDate114 | ATTRIBUTE_DATE11 | — | — |
| 108 | AttributeDate116 | ATTRIBUTE_DATE1 | — | — |
| 109 | AttributeDate117 | ATTRIBUTE_DATE11 | — | — |
| 110 | AttributeDate124 | ATTRIBUTE_DATE12 | — | — |
| 111 | AttributeDate126 | ATTRIBUTE_DATE12 | — | — |
| 112 | AttributeDate134 | ATTRIBUTE_DATE13 | — | — |
| 113 | AttributeDate136 | ATTRIBUTE_DATE13 | — | — |
| 114 | AttributeDate144 | ATTRIBUTE_DATE14 | — | — |
| 115 | AttributeDate146 | ATTRIBUTE_DATE14 | — | — |
| 116 | AttributeDate154 | ATTRIBUTE_DATE15 | — | — |
| 117 | AttributeDate156 | ATTRIBUTE_DATE15 | — | — |
| 118 | AttributeDate19 | ATTRIBUTE_DATE1 | — | — |
| 119 | AttributeDate24 | ATTRIBUTE_DATE2 | — | — |
| 120 | AttributeDate26 | ATTRIBUTE_DATE2 | — | — |
| 121 | AttributeDate34 | ATTRIBUTE_DATE3 | — | — |
| 122 | AttributeDate36 | ATTRIBUTE_DATE3 | — | — |
| 123 | AttributeDate44 | ATTRIBUTE_DATE4 | — | — |
| 124 | AttributeDate46 | ATTRIBUTE_DATE4 | — | — |
| 125 | AttributeDate54 | ATTRIBUTE_DATE5 | — | — |
| 126 | AttributeDate56 | ATTRIBUTE_DATE5 | — | — |
| 127 | AttributeDate64 | ATTRIBUTE_DATE6 | — | — |
| 128 | AttributeDate66 | ATTRIBUTE_DATE6 | — | — |
| 129 | AttributeDate74 | ATTRIBUTE_DATE7 | — | — |
| 130 | AttributeDate76 | ATTRIBUTE_DATE7 | — | — |
| 131 | AttributeDate84 | ATTRIBUTE_DATE8 | — | — |
| 132 | AttributeDate86 | ATTRIBUTE_DATE8 | — | — |
| 133 | AttributeDate94 | ATTRIBUTE_DATE9 | — | — |
| 134 | AttributeDate96 | ATTRIBUTE_DATE9 | — | — |
| 135 | AttributeNumber104 | ATTRIBUTE_NUMBER10 | — | — |
| 136 | AttributeNumber106 | ATTRIBUTE_NUMBER10 | — | — |
| 137 | AttributeNumber1110 | ATTRIBUTE_NUMBER11 | — | — |
| 138 | AttributeNumber116 | ATTRIBUTE_NUMBER1 | — | — |
| 139 | AttributeNumber117 | ATTRIBUTE_NUMBER11 | — | — |
| 140 | AttributeNumber120 | ATTRIBUTE_NUMBER1 | — | — |
| 141 | AttributeNumber124 | ATTRIBUTE_NUMBER12 | — | — |
| 142 | AttributeNumber126 | ATTRIBUTE_NUMBER12 | — | — |
| 143 | AttributeNumber134 | ATTRIBUTE_NUMBER13 | — | — |
| 144 | AttributeNumber136 | ATTRIBUTE_NUMBER13 | — | — |
| 145 | AttributeNumber144 | ATTRIBUTE_NUMBER14 | — | — |
| 146 | AttributeNumber146 | ATTRIBUTE_NUMBER14 | — | — |
| 147 | AttributeNumber154 | ATTRIBUTE_NUMBER15 | — | — |
| 148 | AttributeNumber156 | ATTRIBUTE_NUMBER15 | — | — |
| 149 | AttributeNumber164 | ATTRIBUTE_NUMBER16 | — | — |
| 150 | AttributeNumber166 | ATTRIBUTE_NUMBER16 | — | — |
| 151 | AttributeNumber174 | ATTRIBUTE_NUMBER17 | — | — |
| 152 | AttributeNumber176 | ATTRIBUTE_NUMBER17 | — | — |
| 153 | AttributeNumber184 | ATTRIBUTE_NUMBER18 | — | — |
| 154 | AttributeNumber186 | ATTRIBUTE_NUMBER18 | — | — |
| 155 | AttributeNumber194 | ATTRIBUTE_NUMBER19 | — | — |
| 156 | AttributeNumber196 | ATTRIBUTE_NUMBER19 | — | — |
| 157 | AttributeNumber204 | ATTRIBUTE_NUMBER20 | — | — |
| 158 | AttributeNumber206 | ATTRIBUTE_NUMBER20 | — | — |
| 159 | AttributeNumber24 | ATTRIBUTE_NUMBER2 | — | — |
| 160 | AttributeNumber26 | ATTRIBUTE_NUMBER2 | — | — |
| 161 | AttributeNumber34 | ATTRIBUTE_NUMBER3 | — | — |
| 162 | AttributeNumber36 | ATTRIBUTE_NUMBER3 | — | — |
| 163 | AttributeNumber44 | ATTRIBUTE_NUMBER4 | — | — |
| 164 | AttributeNumber46 | ATTRIBUTE_NUMBER4 | — | — |
| 165 | AttributeNumber54 | ATTRIBUTE_NUMBER5 | — | — |
| 166 | AttributeNumber56 | ATTRIBUTE_NUMBER5 | — | — |
| 167 | AttributeNumber64 | ATTRIBUTE_NUMBER6 | — | — |
| 168 | AttributeNumber66 | ATTRIBUTE_NUMBER6 | — | — |
| 169 | AttributeNumber74 | ATTRIBUTE_NUMBER7 | — | — |
| 170 | AttributeNumber76 | ATTRIBUTE_NUMBER7 | — | — |
| 171 | AttributeNumber84 | ATTRIBUTE_NUMBER8 | — | — |
| 172 | AttributeNumber86 | ATTRIBUTE_NUMBER8 | — | — |
| 173 | AttributeNumber94 | ATTRIBUTE_NUMBER9 | — | — |
| 174 | AttributeNumber96 | ATTRIBUTE_NUMBER9 | — | — |
| 175 | BusinessGroupId6 | BUSINESS_GROUP_ID | — | — |
| 176 | BusinessGroupId8 | BUSINESS_GROUP_ID | — | — |
| 177 | CreatedBy10 | CREATED_BY | — | — |
| 178 | CreatedBy12 | CREATED_BY | — | — |
| 179 | CreationDate10 | CREATION_DATE | — | — |
| 180 | CreationDate12 | CREATION_DATE | — | — |
| 181 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 182 | EffectiveEndDate3 | EFFECTIVE_END_DATE | — | — |
| 183 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 184 | EffectiveStartDate3 | EFFECTIVE_START_DATE | — | ✅ |
| 185 | LastUpdateDate10 | LAST_UPDATE_DATE | — | ✅ |
| 186 | LastUpdateDate12 | LAST_UPDATE_DATE | — | ✅ |
| 187 | LastUpdateLogin10 | LAST_UPDATE_LOGIN | — | — |
| 188 | LastUpdateLogin12 | LAST_UPDATE_LOGIN | — | — |
| 189 | LastUpdatedBy10 | LAST_UPDATED_BY | — | — |
| 190 | LastUpdatedBy12 | LAST_UPDATED_BY | — | — |
| 191 | MailingAddressId | MAILING_ADDRESS_ID | — | — |
| 192 | MailingAddressId1 | MAILING_ADDRESS_ID | — | — |
| 193 | ObjectVersionNumber11 | OBJECT_VERSION_NUMBER | — | — |
| 194 | ObjectVersionNumber9 | OBJECT_VERSION_NUMBER | — | — |
| 195 | PersonId5 | PERSON_ID | — | — |
| 196 | PersonId7 | PERSON_ID | — | — |
| 197 | PersonNumber | PERSON_NUMBER | — | ✅ |
| 198 | PersonNumber1 | PERSON_NUMBER | — | — |
| 199 | PrimaryEmailId | PRIMARY_EMAIL_ID | — | — |
| 200 | PrimaryEmailId1 | PRIMARY_EMAIL_ID | — | — |
| 201 | PrimaryNidId | PRIMARY_NID_ID | — | — |
| 202 | PrimaryNidId1 | PRIMARY_NID_ID | — | — |
| 203 | PrimaryNidNumber | PRIMARY_NID_NUMBER | — | — |
| 204 | PrimaryNidNumber1 | PRIMARY_NID_NUMBER | — | — |
| 205 | PrimaryPhoneId | PRIMARY_PHONE_ID | — | — |
| 206 | PrimaryPhoneId1 | PRIMARY_PHONE_ID | — | — |
| 207 | StartDate2 | START_DATE | — | — |
| 208 | StartDate3 | START_DATE | — | — |
| 209 | WaiveDataProtect | WAIVE_DATA_PROTECT | — | ✅ |
| 210 | WaiveDataProtect1 | WAIVE_DATA_PROTECT | — | — |

### [[per_email_addresses|PER_EMAIL_ADDRESSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute105 | ATTRIBUTE10 | — | — |
| 2 | Attribute107 | ATTRIBUTE10 | — | — |
| 3 | Attribute1111 | ATTRIBUTE11 | — | — |
| 4 | Attribute118 | ATTRIBUTE1 | — | — |
| 5 | Attribute119 | ATTRIBUTE11 | — | — |
| 6 | Attribute125 | ATTRIBUTE12 | — | — |
| 7 | Attribute127 | ATTRIBUTE1 | — | — |
| 8 | Attribute128 | ATTRIBUTE12 | — | — |
| 9 | Attribute135 | ATTRIBUTE13 | — | — |
| 10 | Attribute137 | ATTRIBUTE13 | — | — |
| 11 | Attribute145 | ATTRIBUTE14 | — | — |
| 12 | Attribute147 | ATTRIBUTE14 | — | — |
| 13 | Attribute155 | ATTRIBUTE15 | — | — |
| 14 | Attribute157 | ATTRIBUTE15 | — | — |
| 15 | Attribute165 | ATTRIBUTE16 | — | — |
| 16 | Attribute167 | ATTRIBUTE16 | — | — |
| 17 | Attribute175 | ATTRIBUTE17 | — | — |
| 18 | Attribute177 | ATTRIBUTE17 | — | — |
| 19 | Attribute185 | ATTRIBUTE18 | — | — |
| 20 | Attribute187 | ATTRIBUTE18 | — | — |
| 21 | Attribute195 | ATTRIBUTE19 | — | — |
| 22 | Attribute197 | ATTRIBUTE19 | — | — |
| 23 | Attribute205 | ATTRIBUTE20 | — | — |
| 24 | Attribute207 | ATTRIBUTE20 | — | — |
| 25 | Attribute2111 | ATTRIBUTE21 | — | — |
| 26 | Attribute218 | ATTRIBUTE2 | — | — |
| 27 | Attribute219 | ATTRIBUTE21 | — | — |
| 28 | Attribute225 | ATTRIBUTE22 | — | — |
| 29 | Attribute227 | ATTRIBUTE2 | — | — |
| 30 | Attribute228 | ATTRIBUTE22 | — | — |
| 31 | Attribute235 | ATTRIBUTE23 | — | — |
| 32 | Attribute237 | ATTRIBUTE23 | — | — |
| 33 | Attribute245 | ATTRIBUTE24 | — | — |
| 34 | Attribute247 | ATTRIBUTE24 | — | — |
| 35 | Attribute255 | ATTRIBUTE25 | — | — |
| 36 | Attribute257 | ATTRIBUTE25 | — | — |
| 37 | Attribute265 | ATTRIBUTE26 | — | — |
| 38 | Attribute267 | ATTRIBUTE26 | — | — |
| 39 | Attribute275 | ATTRIBUTE27 | — | — |
| 40 | Attribute277 | ATTRIBUTE27 | — | — |
| 41 | Attribute285 | ATTRIBUTE28 | — | — |
| 42 | Attribute287 | ATTRIBUTE28 | — | — |
| 43 | Attribute295 | ATTRIBUTE29 | — | — |
| 44 | Attribute297 | ATTRIBUTE29 | — | — |
| 45 | Attribute305 | ATTRIBUTE30 | — | — |
| 46 | Attribute307 | ATTRIBUTE30 | — | — |
| 47 | Attribute310 | ATTRIBUTE3 | — | — |
| 48 | Attribute314 | ATTRIBUTE3 | — | — |
| 49 | Attribute410 | ATTRIBUTE4 | — | — |
| 50 | Attribute414 | ATTRIBUTE4 | — | — |
| 51 | Attribute55 | ATTRIBUTE5 | — | — |
| 52 | Attribute57 | ATTRIBUTE5 | — | — |
| 53 | Attribute65 | ATTRIBUTE6 | — | — |
| 54 | Attribute67 | ATTRIBUTE6 | — | — |
| 55 | Attribute75 | ATTRIBUTE7 | — | — |
| 56 | Attribute77 | ATTRIBUTE7 | — | — |
| 57 | Attribute85 | ATTRIBUTE8 | — | — |
| 58 | Attribute87 | ATTRIBUTE8 | — | — |
| 59 | Attribute95 | ATTRIBUTE9 | — | — |
| 60 | Attribute97 | ATTRIBUTE9 | — | — |
| 61 | AttributeCategory5 | ATTRIBUTE_CATEGORY | — | — |
| 62 | AttributeCategory7 | ATTRIBUTE_CATEGORY | — | — |
| 63 | AttributeDate105 | ATTRIBUTE_DATE10 | — | — |
| 64 | AttributeDate107 | ATTRIBUTE_DATE10 | — | — |
| 65 | AttributeDate110 | ATTRIBUTE_DATE1 | — | — |
| 66 | AttributeDate115 | ATTRIBUTE_DATE11 | — | — |
| 67 | AttributeDate118 | ATTRIBUTE_DATE1 | — | — |
| 68 | AttributeDate119 | ATTRIBUTE_DATE11 | — | — |
| 69 | AttributeDate125 | ATTRIBUTE_DATE12 | — | — |
| 70 | AttributeDate127 | ATTRIBUTE_DATE12 | — | — |
| 71 | AttributeDate135 | ATTRIBUTE_DATE13 | — | — |
| 72 | AttributeDate137 | ATTRIBUTE_DATE13 | — | — |
| 73 | AttributeDate145 | ATTRIBUTE_DATE14 | — | — |
| 74 | AttributeDate147 | ATTRIBUTE_DATE14 | — | — |
| 75 | AttributeDate155 | ATTRIBUTE_DATE15 | — | — |
| 76 | AttributeDate157 | ATTRIBUTE_DATE15 | — | — |
| 77 | AttributeDate25 | ATTRIBUTE_DATE2 | — | — |
| 78 | AttributeDate27 | ATTRIBUTE_DATE2 | — | — |
| 79 | AttributeDate35 | ATTRIBUTE_DATE3 | — | — |
| 80 | AttributeDate37 | ATTRIBUTE_DATE3 | — | — |
| 81 | AttributeDate45 | ATTRIBUTE_DATE4 | — | — |
| 82 | AttributeDate47 | ATTRIBUTE_DATE4 | — | — |
| 83 | AttributeDate55 | ATTRIBUTE_DATE5 | — | — |
| 84 | AttributeDate57 | ATTRIBUTE_DATE5 | — | — |
| 85 | AttributeDate65 | ATTRIBUTE_DATE6 | — | — |
| 86 | AttributeDate67 | ATTRIBUTE_DATE6 | — | — |
| 87 | AttributeDate75 | ATTRIBUTE_DATE7 | — | — |
| 88 | AttributeDate77 | ATTRIBUTE_DATE7 | — | — |
| 89 | AttributeDate85 | ATTRIBUTE_DATE8 | — | — |
| 90 | AttributeDate87 | ATTRIBUTE_DATE8 | — | — |
| 91 | AttributeDate95 | ATTRIBUTE_DATE9 | — | — |
| 92 | AttributeDate97 | ATTRIBUTE_DATE9 | — | — |
| 93 | AttributeNumber105 | ATTRIBUTE_NUMBER10 | — | — |
| 94 | AttributeNumber107 | ATTRIBUTE_NUMBER10 | — | — |
| 95 | AttributeNumber1111 | ATTRIBUTE_NUMBER11 | — | — |
| 96 | AttributeNumber118 | ATTRIBUTE_NUMBER1 | — | — |
| 97 | AttributeNumber119 | ATTRIBUTE_NUMBER11 | — | — |
| 98 | AttributeNumber125 | ATTRIBUTE_NUMBER12 | — | — |
| 99 | AttributeNumber127 | ATTRIBUTE_NUMBER1 | — | — |
| 100 | AttributeNumber128 | ATTRIBUTE_NUMBER12 | — | — |
| 101 | AttributeNumber135 | ATTRIBUTE_NUMBER13 | — | — |
| 102 | AttributeNumber137 | ATTRIBUTE_NUMBER13 | — | — |
| 103 | AttributeNumber145 | ATTRIBUTE_NUMBER14 | — | — |
| 104 | AttributeNumber147 | ATTRIBUTE_NUMBER14 | — | — |
| 105 | AttributeNumber155 | ATTRIBUTE_NUMBER15 | — | — |
| 106 | AttributeNumber157 | ATTRIBUTE_NUMBER15 | — | — |
| 107 | AttributeNumber165 | ATTRIBUTE_NUMBER16 | — | — |
| 108 | AttributeNumber167 | ATTRIBUTE_NUMBER16 | — | — |
| 109 | AttributeNumber175 | ATTRIBUTE_NUMBER17 | — | — |
| 110 | AttributeNumber177 | ATTRIBUTE_NUMBER17 | — | — |
| 111 | AttributeNumber185 | ATTRIBUTE_NUMBER18 | — | — |
| 112 | AttributeNumber187 | ATTRIBUTE_NUMBER18 | — | — |
| 113 | AttributeNumber195 | ATTRIBUTE_NUMBER19 | — | — |
| 114 | AttributeNumber197 | ATTRIBUTE_NUMBER19 | — | — |
| 115 | AttributeNumber205 | ATTRIBUTE_NUMBER20 | — | — |
| 116 | AttributeNumber207 | ATTRIBUTE_NUMBER20 | — | — |
| 117 | AttributeNumber25 | ATTRIBUTE_NUMBER2 | — | — |
| 118 | AttributeNumber27 | ATTRIBUTE_NUMBER2 | — | — |
| 119 | AttributeNumber35 | ATTRIBUTE_NUMBER3 | — | — |
| 120 | AttributeNumber37 | ATTRIBUTE_NUMBER3 | — | — |
| 121 | AttributeNumber45 | ATTRIBUTE_NUMBER4 | — | — |
| 122 | AttributeNumber47 | ATTRIBUTE_NUMBER4 | — | — |
| 123 | AttributeNumber55 | ATTRIBUTE_NUMBER5 | — | — |
| 124 | AttributeNumber57 | ATTRIBUTE_NUMBER5 | — | — |
| 125 | AttributeNumber65 | ATTRIBUTE_NUMBER6 | — | — |
| 126 | AttributeNumber67 | ATTRIBUTE_NUMBER6 | — | — |
| 127 | AttributeNumber75 | ATTRIBUTE_NUMBER7 | — | — |
| 128 | AttributeNumber77 | ATTRIBUTE_NUMBER7 | — | — |
| 129 | AttributeNumber85 | ATTRIBUTE_NUMBER8 | — | — |
| 130 | AttributeNumber87 | ATTRIBUTE_NUMBER8 | — | — |
| 131 | AttributeNumber95 | ATTRIBUTE_NUMBER9 | — | — |
| 132 | AttributeNumber97 | ATTRIBUTE_NUMBER9 | — | — |
| 133 | BusinessGroupId7 | BUSINESS_GROUP_ID | — | — |
| 134 | BusinessGroupId9 | BUSINESS_GROUP_ID | — | — |
| 135 | CreatedBy11 | CREATED_BY | — | — |
| 136 | CreatedBy13 | CREATED_BY | — | — |
| 137 | CreationDate11 | CREATION_DATE | — | — |
| 138 | CreationDate13 | CREATION_DATE | — | — |
| 139 | DateFrom | DATE_FROM | — | ✅ |
| 140 | DateFrom1 | DATE_FROM | — | — |
| 141 | DateTo | DATE_TO | — | ✅ |
| 142 | DateTo1 | DATE_TO | — | — |
| 143 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 144 | EmailAddress1 | EMAIL_ADDRESS | — | — |
| 145 | EmailAddressId | EMAIL_ADDRESS_ID | — | — |
| 146 | EmailAddressId1 | EMAIL_ADDRESS_ID | — | — |
| 147 | EmailType | EMAIL_TYPE | — | ✅ |
| 148 | EmailType1 | EMAIL_TYPE | — | — |
| 149 | LastUpdateDate11 | LAST_UPDATE_DATE | — | ✅ |
| 150 | LastUpdateDate13 | LAST_UPDATE_DATE | — | ✅ |
| 151 | LastUpdateLogin11 | LAST_UPDATE_LOGIN | — | — |
| 152 | LastUpdateLogin13 | LAST_UPDATE_LOGIN | — | — |
| 153 | LastUpdatedBy11 | LAST_UPDATED_BY | — | — |
| 154 | LastUpdatedBy13 | LAST_UPDATED_BY | — | — |
| 155 | MasteredInLdapFlag | MASTERED_IN_LDAP_FLAG | — | — |
| 156 | MasteredInLdapFlag1 | MASTERED_IN_LDAP_FLAG | — | — |
| 157 | ObjectVersionNumber10 | OBJECT_VERSION_NUMBER | — | — |
| 158 | ObjectVersionNumber12 | OBJECT_VERSION_NUMBER | — | — |
| 159 | PersonId6 | PERSON_ID | — | — |
| 160 | PersonId8 | PERSON_ID | — | — |

### [[per_persons|PER_PERSONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute102 | ATTRIBUTE10 | — | — |
| 4 | Attribute11 | ATTRIBUTE11 | — | — |
| 5 | Attribute112 | ATTRIBUTE1 | — | — |
| 6 | Attribute113 | ATTRIBUTE11 | — | — |
| 7 | Attribute12 | ATTRIBUTE12 | — | — |
| 8 | Attribute122 | ATTRIBUTE12 | — | — |
| 9 | Attribute13 | ATTRIBUTE13 | — | — |
| 10 | Attribute132 | ATTRIBUTE13 | — | — |
| 11 | Attribute14 | ATTRIBUTE14 | — | — |
| 12 | Attribute142 | ATTRIBUTE14 | — | — |
| 13 | Attribute15 | ATTRIBUTE15 | — | — |
| 14 | Attribute152 | ATTRIBUTE15 | — | — |
| 15 | Attribute16 | ATTRIBUTE16 | — | — |
| 16 | Attribute162 | ATTRIBUTE16 | — | — |
| 17 | Attribute17 | ATTRIBUTE17 | — | — |
| 18 | Attribute172 | ATTRIBUTE17 | — | — |
| 19 | Attribute18 | ATTRIBUTE18 | — | — |
| 20 | Attribute182 | ATTRIBUTE18 | — | — |
| 21 | Attribute19 | ATTRIBUTE19 | — | — |
| 22 | Attribute192 | ATTRIBUTE19 | — | — |
| 23 | Attribute2 | ATTRIBUTE2 | — | — |
| 24 | Attribute20 | ATTRIBUTE20 | — | — |
| 25 | Attribute202 | ATTRIBUTE20 | — | — |
| 26 | Attribute21 | ATTRIBUTE21 | — | — |
| 27 | Attribute212 | ATTRIBUTE2 | — | — |
| 28 | Attribute213 | ATTRIBUTE21 | — | — |
| 29 | Attribute22 | ATTRIBUTE22 | — | — |
| 30 | Attribute222 | ATTRIBUTE22 | — | — |
| 31 | Attribute23 | ATTRIBUTE23 | — | — |
| 32 | Attribute232 | ATTRIBUTE23 | — | — |
| 33 | Attribute24 | ATTRIBUTE24 | — | — |
| 34 | Attribute242 | ATTRIBUTE24 | — | — |
| 35 | Attribute25 | ATTRIBUTE25 | — | — |
| 36 | Attribute252 | ATTRIBUTE25 | — | — |
| 37 | Attribute26 | ATTRIBUTE26 | — | — |
| 38 | Attribute262 | ATTRIBUTE26 | — | — |
| 39 | Attribute27 | ATTRIBUTE27 | — | — |
| 40 | Attribute272 | ATTRIBUTE27 | — | — |
| 41 | Attribute28 | ATTRIBUTE28 | — | — |
| 42 | Attribute282 | ATTRIBUTE28 | — | — |
| 43 | Attribute29 | ATTRIBUTE29 | — | — |
| 44 | Attribute292 | ATTRIBUTE29 | — | — |
| 45 | Attribute3 | ATTRIBUTE3 | — | — |
| 46 | Attribute30 | ATTRIBUTE30 | — | — |
| 47 | Attribute302 | ATTRIBUTE30 | — | — |
| 48 | Attribute32 | ATTRIBUTE3 | — | — |
| 49 | Attribute4 | ATTRIBUTE4 | — | — |
| 50 | Attribute42 | ATTRIBUTE4 | — | — |
| 51 | Attribute5 | ATTRIBUTE5 | — | — |
| 52 | Attribute52 | ATTRIBUTE5 | — | — |
| 53 | Attribute6 | ATTRIBUTE6 | — | — |
| 54 | Attribute62 | ATTRIBUTE6 | — | — |
| 55 | Attribute7 | ATTRIBUTE7 | — | — |
| 56 | Attribute72 | ATTRIBUTE7 | — | — |
| 57 | Attribute8 | ATTRIBUTE8 | — | — |
| 58 | Attribute82 | ATTRIBUTE8 | — | — |
| 59 | Attribute9 | ATTRIBUTE9 | — | — |
| 60 | Attribute92 | ATTRIBUTE9 | — | — |
| 61 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 62 | AttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 63 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 64 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 65 | AttributeDate102 | ATTRIBUTE_DATE10 | — | — |
| 66 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 67 | AttributeDate112 | ATTRIBUTE_DATE11 | — | — |
| 68 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 69 | AttributeDate122 | ATTRIBUTE_DATE12 | — | — |
| 70 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 71 | AttributeDate132 | ATTRIBUTE_DATE13 | — | — |
| 72 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 73 | AttributeDate142 | ATTRIBUTE_DATE14 | — | — |
| 74 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 75 | AttributeDate152 | ATTRIBUTE_DATE15 | — | — |
| 76 | AttributeDate17 | ATTRIBUTE_DATE1 | — | — |
| 77 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 78 | AttributeDate22 | ATTRIBUTE_DATE2 | — | — |
| 79 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 80 | AttributeDate32 | ATTRIBUTE_DATE3 | — | — |
| 81 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 82 | AttributeDate42 | ATTRIBUTE_DATE4 | — | — |
| 83 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 84 | AttributeDate52 | ATTRIBUTE_DATE5 | — | — |
| 85 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 86 | AttributeDate62 | ATTRIBUTE_DATE6 | — | — |
| 87 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 88 | AttributeDate72 | ATTRIBUTE_DATE7 | — | — |
| 89 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 90 | AttributeDate82 | ATTRIBUTE_DATE8 | — | — |
| 91 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 92 | AttributeDate92 | ATTRIBUTE_DATE9 | — | — |
| 93 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 94 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 95 | AttributeNumber102 | ATTRIBUTE_NUMBER10 | — | — |
| 96 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 97 | AttributeNumber112 | ATTRIBUTE_NUMBER1 | — | — |
| 98 | AttributeNumber113 | ATTRIBUTE_NUMBER11 | — | — |
| 99 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 100 | AttributeNumber122 | ATTRIBUTE_NUMBER12 | — | — |
| 101 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 102 | AttributeNumber132 | ATTRIBUTE_NUMBER13 | — | — |
| 103 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 104 | AttributeNumber142 | ATTRIBUTE_NUMBER14 | — | — |
| 105 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 106 | AttributeNumber152 | ATTRIBUTE_NUMBER15 | — | — |
| 107 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 108 | AttributeNumber162 | ATTRIBUTE_NUMBER16 | — | — |
| 109 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 110 | AttributeNumber172 | ATTRIBUTE_NUMBER17 | — | — |
| 111 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 112 | AttributeNumber182 | ATTRIBUTE_NUMBER18 | — | — |
| 113 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 114 | AttributeNumber192 | ATTRIBUTE_NUMBER19 | — | — |
| 115 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 116 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 117 | AttributeNumber202 | ATTRIBUTE_NUMBER20 | — | — |
| 118 | AttributeNumber22 | ATTRIBUTE_NUMBER2 | — | — |
| 119 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 120 | AttributeNumber32 | ATTRIBUTE_NUMBER3 | — | — |
| 121 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 122 | AttributeNumber42 | ATTRIBUTE_NUMBER4 | — | — |
| 123 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 124 | AttributeNumber52 | ATTRIBUTE_NUMBER5 | — | — |
| 125 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 126 | AttributeNumber62 | ATTRIBUTE_NUMBER6 | — | — |
| 127 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 128 | AttributeNumber72 | ATTRIBUTE_NUMBER7 | — | — |
| 129 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 130 | AttributeNumber82 | ATTRIBUTE_NUMBER8 | — | — |
| 131 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 132 | AttributeNumber92 | ATTRIBUTE_NUMBER9 | — | — |
| 133 | BloodType | BLOOD_TYPE | — | ✅ |
| 134 | BloodType1 | BLOOD_TYPE | — | — |
| 135 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 136 | BusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 137 | CorrespondenceLanguage | CORRESPONDENCE_LANGUAGE | — | ✅ |
| 138 | CorrespondenceLanguage1 | CORRESPONDENCE_LANGUAGE | — | — |
| 139 | CountryOfBirth | COUNTRY_OF_BIRTH | — | ✅ |
| 140 | CountryOfBirth1 | COUNTRY_OF_BIRTH | — | — |
| 141 | CreatedBy6 | CREATED_BY | — | — |
| 142 | CreatedBy8 | CREATED_BY | — | — |
| 143 | CreationDate6 | CREATION_DATE | — | — |
| 144 | CreationDate8 | CREATION_DATE | — | — |
| 145 | DateOfBirth | DATE_OF_BIRTH | — | ✅ |
| 146 | DateOfBirth1 | DATE_OF_BIRTH | — | — |
| 147 | DateOfDeath | DATE_OF_DEATH | — | — |
| 148 | DateOfDeath1 | DATE_OF_DEATH | — | — |
| 149 | LastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 150 | LastUpdateDate8 | LAST_UPDATE_DATE | — | ✅ |
| 151 | LastUpdateLogin6 | LAST_UPDATE_LOGIN | — | — |
| 152 | LastUpdateLogin8 | LAST_UPDATE_LOGIN | — | — |
| 153 | LastUpdatedBy6 | LAST_UPDATED_BY | — | — |
| 154 | LastUpdatedBy8 | LAST_UPDATED_BY | — | — |
| 155 | ObjectVersionNumber5 | OBJECT_VERSION_NUMBER | — | — |
| 156 | ObjectVersionNumber7 | OBJECT_VERSION_NUMBER | — | — |
| 157 | PartyId | PARTY_ID | — | — |
| 158 | PartyId1 | PARTY_ID | — | — |
| 159 | PersonId1 | PERSON_ID | — | — |
| 160 | PersonId3 | PERSON_ID | — | — |
| 161 | RegionOfBirth | REGION_OF_BIRTH | — | — |
| 162 | RegionOfBirth1 | REGION_OF_BIRTH | — | — |
| 163 | StartDate | START_DATE | — | ✅ |
| 164 | StartDate1 | START_DATE | — | — |
| 165 | TownOfBirth | TOWN_OF_BIRTH | — | — |
| 166 | TownOfBirth1 | TOWN_OF_BIRTH | — | — |
| 167 | UserGuid | USER_GUID | — | — |
| 168 | UserGuid1 | USER_GUID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute101 | ATTRIBUTE10 | — | — |
| 2 | Attribute103 | ATTRIBUTE10 | — | — |
| 3 | Attribute110 | ATTRIBUTE1 | — | — |
| 4 | Attribute111 | ATTRIBUTE11 | — | — |
| 5 | Attribute114 | ATTRIBUTE1 | — | — |
| 6 | Attribute115 | ATTRIBUTE11 | — | — |
| 7 | Attribute121 | ATTRIBUTE12 | — | — |
| 8 | Attribute123 | ATTRIBUTE12 | — | — |
| 9 | Attribute131 | ATTRIBUTE13 | — | — |
| 10 | Attribute133 | ATTRIBUTE13 | — | — |
| 11 | Attribute141 | ATTRIBUTE14 | — | — |
| 12 | Attribute143 | ATTRIBUTE14 | — | — |
| 13 | Attribute151 | ATTRIBUTE15 | — | — |
| 14 | Attribute153 | ATTRIBUTE15 | — | — |
| 15 | Attribute161 | ATTRIBUTE16 | — | — |
| 16 | Attribute163 | ATTRIBUTE16 | — | — |
| 17 | Attribute171 | ATTRIBUTE17 | — | — |
| 18 | Attribute173 | ATTRIBUTE17 | — | — |
| 19 | Attribute181 | ATTRIBUTE18 | — | — |
| 20 | Attribute183 | ATTRIBUTE18 | — | — |
| 21 | Attribute191 | ATTRIBUTE19 | — | — |
| 22 | Attribute193 | ATTRIBUTE19 | — | — |
| 23 | Attribute201 | ATTRIBUTE20 | — | — |
| 24 | Attribute203 | ATTRIBUTE20 | — | — |
| 25 | Attribute210 | ATTRIBUTE2 | — | — |
| 26 | Attribute211 | ATTRIBUTE21 | — | — |
| 27 | Attribute214 | ATTRIBUTE2 | — | — |
| 28 | Attribute215 | ATTRIBUTE21 | — | — |
| 29 | Attribute221 | ATTRIBUTE22 | — | — |
| 30 | Attribute223 | ATTRIBUTE22 | — | — |
| 31 | Attribute231 | ATTRIBUTE23 | — | — |
| 32 | Attribute233 | ATTRIBUTE23 | — | — |
| 33 | Attribute241 | ATTRIBUTE24 | — | — |
| 34 | Attribute243 | ATTRIBUTE24 | — | — |
| 35 | Attribute251 | ATTRIBUTE25 | — | — |
| 36 | Attribute253 | ATTRIBUTE25 | — | — |
| 37 | Attribute261 | ATTRIBUTE26 | — | — |
| 38 | Attribute263 | ATTRIBUTE26 | — | — |
| 39 | Attribute271 | ATTRIBUTE27 | — | — |
| 40 | Attribute273 | ATTRIBUTE27 | — | — |
| 41 | Attribute281 | ATTRIBUTE28 | — | — |
| 42 | Attribute283 | ATTRIBUTE28 | — | — |
| 43 | Attribute291 | ATTRIBUTE29 | — | — |
| 44 | Attribute293 | ATTRIBUTE29 | — | — |
| 45 | Attribute301 | ATTRIBUTE30 | — | — |
| 46 | Attribute303 | ATTRIBUTE30 | — | — |
| 47 | Attribute31 | ATTRIBUTE3 | — | — |
| 48 | Attribute33 | ATTRIBUTE3 | — | — |
| 49 | Attribute41 | ATTRIBUTE4 | — | — |
| 50 | Attribute43 | ATTRIBUTE4 | — | — |
| 51 | Attribute51 | ATTRIBUTE5 | — | — |
| 52 | Attribute53 | ATTRIBUTE5 | — | — |
| 53 | Attribute61 | ATTRIBUTE6 | — | — |
| 54 | Attribute63 | ATTRIBUTE6 | — | — |
| 55 | Attribute71 | ATTRIBUTE7 | — | — |
| 56 | Attribute73 | ATTRIBUTE7 | — | — |
| 57 | Attribute81 | ATTRIBUTE8 | — | — |
| 58 | Attribute83 | ATTRIBUTE8 | — | — |
| 59 | Attribute91 | ATTRIBUTE9 | — | — |
| 60 | Attribute93 | ATTRIBUTE9 | — | — |
| 61 | AttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 62 | AttributeCategory3 | ATTRIBUTE_CATEGORY | — | — |
| 63 | AttributeDate101 | ATTRIBUTE_DATE10 | — | — |
| 64 | AttributeDate103 | ATTRIBUTE_DATE10 | — | — |
| 65 | AttributeDate111 | ATTRIBUTE_DATE11 | — | — |
| 66 | AttributeDate113 | ATTRIBUTE_DATE11 | — | — |
| 67 | AttributeDate121 | ATTRIBUTE_DATE12 | — | — |
| 68 | AttributeDate123 | ATTRIBUTE_DATE12 | — | — |
| 69 | AttributeDate131 | ATTRIBUTE_DATE13 | — | — |
| 70 | AttributeDate133 | ATTRIBUTE_DATE13 | — | — |
| 71 | AttributeDate141 | ATTRIBUTE_DATE14 | — | — |
| 72 | AttributeDate143 | ATTRIBUTE_DATE14 | — | — |
| 73 | AttributeDate151 | ATTRIBUTE_DATE15 | — | — |
| 74 | AttributeDate153 | ATTRIBUTE_DATE15 | — | — |
| 75 | AttributeDate16 | ATTRIBUTE_DATE1 | — | — |
| 76 | AttributeDate18 | ATTRIBUTE_DATE1 | — | — |
| 77 | AttributeDate21 | ATTRIBUTE_DATE2 | — | — |
| 78 | AttributeDate23 | ATTRIBUTE_DATE2 | — | — |
| 79 | AttributeDate31 | ATTRIBUTE_DATE3 | — | — |
| 80 | AttributeDate33 | ATTRIBUTE_DATE3 | — | — |
| 81 | AttributeDate41 | ATTRIBUTE_DATE4 | — | — |
| 82 | AttributeDate43 | ATTRIBUTE_DATE4 | — | — |
| 83 | AttributeDate51 | ATTRIBUTE_DATE5 | — | — |
| 84 | AttributeDate53 | ATTRIBUTE_DATE5 | — | — |
| 85 | AttributeDate61 | ATTRIBUTE_DATE6 | — | — |
| 86 | AttributeDate63 | ATTRIBUTE_DATE6 | — | — |
| 87 | AttributeDate71 | ATTRIBUTE_DATE7 | — | — |
| 88 | AttributeDate73 | ATTRIBUTE_DATE7 | — | — |
| 89 | AttributeDate81 | ATTRIBUTE_DATE8 | — | — |
| 90 | AttributeDate83 | ATTRIBUTE_DATE8 | — | — |
| 91 | AttributeDate91 | ATTRIBUTE_DATE9 | — | — |
| 92 | AttributeDate93 | ATTRIBUTE_DATE9 | — | — |
| 93 | AttributeNumber101 | ATTRIBUTE_NUMBER10 | — | — |
| 94 | AttributeNumber103 | ATTRIBUTE_NUMBER10 | — | — |
| 95 | AttributeNumber110 | ATTRIBUTE_NUMBER1 | — | — |
| 96 | AttributeNumber111 | ATTRIBUTE_NUMBER11 | — | — |
| 97 | AttributeNumber114 | ATTRIBUTE_NUMBER1 | — | — |
| 98 | AttributeNumber115 | ATTRIBUTE_NUMBER11 | — | — |
| 99 | AttributeNumber121 | ATTRIBUTE_NUMBER12 | — | — |
| 100 | AttributeNumber123 | ATTRIBUTE_NUMBER12 | — | — |
| 101 | AttributeNumber131 | ATTRIBUTE_NUMBER13 | — | — |
| 102 | AttributeNumber133 | ATTRIBUTE_NUMBER13 | — | — |
| 103 | AttributeNumber141 | ATTRIBUTE_NUMBER14 | — | — |
| 104 | AttributeNumber143 | ATTRIBUTE_NUMBER14 | — | — |
| 105 | AttributeNumber151 | ATTRIBUTE_NUMBER15 | — | — |
| 106 | AttributeNumber153 | ATTRIBUTE_NUMBER15 | — | — |
| 107 | AttributeNumber161 | ATTRIBUTE_NUMBER16 | — | — |
| 108 | AttributeNumber163 | ATTRIBUTE_NUMBER16 | — | — |
| 109 | AttributeNumber171 | ATTRIBUTE_NUMBER17 | — | — |
| 110 | AttributeNumber173 | ATTRIBUTE_NUMBER17 | — | — |
| 111 | AttributeNumber181 | ATTRIBUTE_NUMBER18 | — | — |
| 112 | AttributeNumber183 | ATTRIBUTE_NUMBER18 | — | — |
| 113 | AttributeNumber191 | ATTRIBUTE_NUMBER19 | — | — |
| 114 | AttributeNumber193 | ATTRIBUTE_NUMBER19 | — | — |
| 115 | AttributeNumber201 | ATTRIBUTE_NUMBER20 | — | — |
| 116 | AttributeNumber203 | ATTRIBUTE_NUMBER20 | — | — |
| 117 | AttributeNumber21 | ATTRIBUTE_NUMBER2 | — | — |
| 118 | AttributeNumber23 | ATTRIBUTE_NUMBER2 | — | — |
| 119 | AttributeNumber31 | ATTRIBUTE_NUMBER3 | — | — |
| 120 | AttributeNumber33 | ATTRIBUTE_NUMBER3 | — | — |
| 121 | AttributeNumber41 | ATTRIBUTE_NUMBER4 | — | — |
| 122 | AttributeNumber43 | ATTRIBUTE_NUMBER4 | — | — |
| 123 | AttributeNumber51 | ATTRIBUTE_NUMBER5 | — | — |
| 124 | AttributeNumber53 | ATTRIBUTE_NUMBER5 | — | — |
| 125 | AttributeNumber61 | ATTRIBUTE_NUMBER6 | — | — |
| 126 | AttributeNumber63 | ATTRIBUTE_NUMBER6 | — | — |
| 127 | AttributeNumber71 | ATTRIBUTE_NUMBER7 | — | — |
| 128 | AttributeNumber73 | ATTRIBUTE_NUMBER7 | — | — |
| 129 | AttributeNumber81 | ATTRIBUTE_NUMBER8 | — | — |
| 130 | AttributeNumber83 | ATTRIBUTE_NUMBER8 | — | — |
| 131 | AttributeNumber91 | ATTRIBUTE_NUMBER9 | — | — |
| 132 | AttributeNumber93 | ATTRIBUTE_NUMBER9 | — | — |
| 133 | BusinessGroupId3 | BUSINESS_GROUP_ID | — | — |
| 134 | BusinessGroupId5 | BUSINESS_GROUP_ID | — | — |
| 135 | CreatedBy7 | CREATED_BY | — | — |
| 136 | CreatedBy9 | CREATED_BY | — | — |
| 137 | CreationDate7 | CREATION_DATE | — | — |
| 138 | CreationDate9 | CREATION_DATE | — | — |
| 139 | DisplayName | DISPLAY_NAME | — | ✅ |
| 140 | DisplayName1 | DISPLAY_NAME | — | — |
| 141 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 142 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 143 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 144 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 145 | FirstName | FIRST_NAME | — | ✅ |
| 146 | FirstName1 | FIRST_NAME | — | — |
| 147 | FullName | FULL_NAME | — | ✅ |
| 148 | FullName1 | FULL_NAME | — | — |
| 149 | Honors | HONORS | — | ✅ |
| 150 | Honors1 | HONORS | — | — |
| 151 | KnownAs | KNOWN_AS | — | ✅ |
| 152 | KnownAs1 | KNOWN_AS | — | — |
| 153 | LastName | LAST_NAME | — | ✅ |
| 154 | LastName1 | LAST_NAME | — | — |
| 155 | LastUpdateDate7 | LAST_UPDATE_DATE | — | ✅ |
| 156 | LastUpdateDate9 | LAST_UPDATE_DATE | — | ✅ |
| 157 | LastUpdateLogin7 | LAST_UPDATE_LOGIN | — | — |
| 158 | LastUpdateLogin9 | LAST_UPDATE_LOGIN | — | — |
| 159 | LastUpdatedBy7 | LAST_UPDATED_BY | — | — |
| 160 | LastUpdatedBy9 | LAST_UPDATED_BY | — | — |
| 161 | LegislationCode | LEGISLATION_CODE | — | — |
| 162 | LegislationCode1 | LEGISLATION_CODE | — | — |
| 163 | ListName | LIST_NAME | — | ✅ |
| 164 | ListName1 | LIST_NAME | — | — |
| 165 | MiddleNames | MIDDLE_NAMES | — | ✅ |
| 166 | MiddleNames1 | MIDDLE_NAMES | — | — |
| 167 | MilitaryRank | MILITARY_RANK | — | — |
| 168 | MilitaryRank1 | MILITARY_RANK | — | — |
| 169 | NamInformation1 | NAM_INFORMATION1 | — | — |
| 170 | NamInformation10 | NAM_INFORMATION10 | — | — |
| 171 | NamInformation101 | NAM_INFORMATION10 | — | — |
| 172 | NamInformation11 | NAM_INFORMATION11 | — | — |
| 173 | NamInformation110 | NAM_INFORMATION1 | — | — |
| 174 | NamInformation111 | NAM_INFORMATION11 | — | — |
| 175 | NamInformation12 | NAM_INFORMATION12 | — | — |
| 176 | NamInformation121 | NAM_INFORMATION12 | — | — |
| 177 | NamInformation13 | NAM_INFORMATION13 | — | — |
| 178 | NamInformation131 | NAM_INFORMATION13 | — | — |
| 179 | NamInformation14 | NAM_INFORMATION14 | — | — |
| 180 | NamInformation141 | NAM_INFORMATION14 | — | — |
| 181 | NamInformation15 | NAM_INFORMATION15 | — | — |
| 182 | NamInformation151 | NAM_INFORMATION15 | — | — |
| 183 | NamInformation16 | NAM_INFORMATION16 | — | — |
| 184 | NamInformation161 | NAM_INFORMATION16 | — | — |
| 185 | NamInformation17 | NAM_INFORMATION17 | — | — |
| 186 | NamInformation171 | NAM_INFORMATION17 | — | — |
| 187 | NamInformation18 | NAM_INFORMATION18 | — | — |
| 188 | NamInformation181 | NAM_INFORMATION18 | — | — |
| 189 | NamInformation19 | NAM_INFORMATION19 | — | — |
| 190 | NamInformation191 | NAM_INFORMATION19 | — | — |
| 191 | NamInformation2 | NAM_INFORMATION2 | — | — |
| 192 | NamInformation20 | NAM_INFORMATION20 | — | — |
| 193 | NamInformation201 | NAM_INFORMATION20 | — | — |
| 194 | NamInformation21 | NAM_INFORMATION21 | — | — |
| 195 | NamInformation210 | NAM_INFORMATION2 | — | — |
| 196 | NamInformation211 | NAM_INFORMATION21 | — | — |
| 197 | NamInformation22 | NAM_INFORMATION22 | — | — |
| 198 | NamInformation221 | NAM_INFORMATION22 | — | — |
| 199 | NamInformation23 | NAM_INFORMATION23 | — | — |
| 200 | NamInformation231 | NAM_INFORMATION23 | — | — |
| 201 | NamInformation24 | NAM_INFORMATION24 | — | — |
| 202 | NamInformation241 | NAM_INFORMATION24 | — | — |
| 203 | NamInformation25 | NAM_INFORMATION25 | — | — |
| 204 | NamInformation251 | NAM_INFORMATION25 | — | — |
| 205 | NamInformation26 | NAM_INFORMATION26 | — | — |
| 206 | NamInformation261 | NAM_INFORMATION26 | — | — |
| 207 | NamInformation27 | NAM_INFORMATION27 | — | — |
| 208 | NamInformation271 | NAM_INFORMATION27 | — | — |
| 209 | NamInformation28 | NAM_INFORMATION28 | — | — |
| 210 | NamInformation281 | NAM_INFORMATION28 | — | — |
| 211 | NamInformation29 | NAM_INFORMATION29 | — | — |
| 212 | NamInformation291 | NAM_INFORMATION29 | — | — |
| 213 | NamInformation3 | NAM_INFORMATION3 | — | — |
| 214 | NamInformation30 | NAM_INFORMATION30 | — | — |
| 215 | NamInformation301 | NAM_INFORMATION30 | — | — |
| 216 | NamInformation31 | NAM_INFORMATION3 | — | — |
| 217 | NamInformation4 | NAM_INFORMATION4 | — | — |
| 218 | NamInformation41 | NAM_INFORMATION4 | — | — |
| 219 | NamInformation5 | NAM_INFORMATION5 | — | — |
| 220 | NamInformation51 | NAM_INFORMATION5 | — | — |
| 221 | NamInformation6 | NAM_INFORMATION6 | — | — |
| 222 | NamInformation61 | NAM_INFORMATION6 | — | — |
| 223 | NamInformation7 | NAM_INFORMATION7 | — | — |
| 224 | NamInformation71 | NAM_INFORMATION7 | — | — |
| 225 | NamInformation8 | NAM_INFORMATION8 | — | — |
| 226 | NamInformation81 | NAM_INFORMATION8 | — | — |
| 227 | NamInformation9 | NAM_INFORMATION9 | — | — |
| 228 | NamInformation91 | NAM_INFORMATION9 | — | — |
| 229 | NamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 230 | NamInformationCategory1 | NAM_INFORMATION_CATEGORY | — | — |
| 231 | NameType | NAME_TYPE | — | ✅ |
| 232 | NameType1 | NAME_TYPE | — | — |
| 233 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 234 | ObjectVersionNumber8 | OBJECT_VERSION_NUMBER | — | — |
| 235 | OrderName | ORDER_NAME | — | ✅ |
| 236 | OrderName1 | ORDER_NAME | — | — |
| 237 | PersonId2 | PERSON_ID | — | — |
| 238 | PersonId4 | PERSON_ID | — | — |
| 239 | PersonNameId | PERSON_NAME_ID | — | — |
| 240 | PersonNameId1 | PERSON_NAME_ID | — | — |
| 241 | PreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 242 | PreNameAdjunct1 | PRE_NAME_ADJUNCT | — | — |
| 243 | PreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 244 | PreviousLastName1 | PREVIOUS_LAST_NAME | — | — |
| 245 | Suffix | SUFFIX | — | — |
| 246 | Suffix1 | SUFFIX | — | — |
| 247 | Title | TITLE | — | ✅ |
| 248 | Title1 | TITLE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
