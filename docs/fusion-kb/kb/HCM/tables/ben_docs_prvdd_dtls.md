---
id: DOC-HCM-037
doc_type: system-doc
title: "BEN_DOCS_PRVDD_DTLS — Detalhes de Documentos Fornecidos"
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
  - benefits
  - documentos
  - docs-provided
aliases:
  - BEN_DOCS_PRVDD_DTLS
  - ben_docs_prvdd_dtls
  - documentos-beneficios
  - docs-provided-details
  - ben-docs-prvdd
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_DOCS_PRVDD_DTLS

## 📌 Visão Geral

Armazena os **detalhes de documentos fornecidos** por participantes de benefícios para comprovação de elegibilidade ou mudança de cobertura.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comprovação:** Registra documentos fornecidos para validação de eventos de vida.
- **Auditoria:** Rastreabilidade de documentos por participante.
- **Workflow:** Status de revisão/aprovação de documentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_DOCS_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de detalhes de documentos fornecidos
```sql
SELECT * FROM BEN_DOCS_PRVDD_DTLS
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Detalhes de Documentos Fornecidos).

---

## 🔗 PVOs Relacionados

### [[participantcertificationpvo|ParticipantCertificationPVO]] (HCM · BICC: 17/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPROVAL_END_DT | DocumentProvidedDetailsPEOApprovalEndDt | — |
| APPROVAL_PERD_CD | DocumentProvidedDetailsPEOApprovalPerdCd | — |
| APPROVAL_PERD_TM_NUM | DocumentProvidedDetailsPEOApprovalPerdTmNum | — |
| APPROVAL_STRT_DT | DocumentProvidedDetailsPEOApprovalStrtDt | — |
| APPROVED_BY | DocumentProvidedDetailsPEOApprovedBy | ✅ |
| APPROVED_DT | DocumentProvidedDetailsPEOApprovedDt | ✅ |
| BUSINESS_GROUP_ID | DocumentProvidedDetailsPEOBusinessGroupId | — |
| COMMENTS | DocumentProvidedDetailsPEOComments | ✅ |
| CONFIG_CHAR_1 | DocumentProvidedDetailsPEOConfigChar1 | — |
| CONFIG_CHAR_2 | DocumentProvidedDetailsPEOConfigChar2 | — |
| CONFIG_CHAR_3 | DocumentProvidedDetailsPEOConfigChar3 | — |
| CONFIG_CHAR_4 | DocumentProvidedDetailsPEOConfigChar4 | — |
| CONFIG_CHAR_5 | DocumentProvidedDetailsPEOConfigChar5 | — |
| CONFIG_DATE_1 | DocumentProvidedDetailsPEOConfigDate1 | — |
| CONFIG_DATE_2 | DocumentProvidedDetailsPEOConfigDate2 | — |
| CONFIG_DATE_3 | DocumentProvidedDetailsPEOConfigDate3 | — |
| CONFIG_DATE_4 | DocumentProvidedDetailsPEOConfigDate4 | — |
| CONFIG_DATE_5 | DocumentProvidedDetailsPEOConfigDate5 | — |
| CONFIG_ID_1 | DocumentProvidedDetailsPEOConfigId1 | — |
| CONFIG_ID_2 | DocumentProvidedDetailsPEOConfigId2 | — |
| CONFIG_ID_3 | DocumentProvidedDetailsPEOConfigId3 | — |
| CONFIG_ID_4 | DocumentProvidedDetailsPEOConfigId4 | — |
| CONFIG_ID_5 | DocumentProvidedDetailsPEOConfigId5 | — |
| CONFIG_NUM_1 | DocumentProvidedDetailsPEOConfigNum1 | — |
| CONFIG_NUM_2 | DocumentProvidedDetailsPEOConfigNum2 | — |
| CONFIG_NUM_3 | DocumentProvidedDetailsPEOConfigNum3 | — |
| CONFIG_NUM_4 | DocumentProvidedDetailsPEOConfigNum4 | — |
| CONFIG_NUM_5 | DocumentProvidedDetailsPEOConfigNum5 | — |
| CONTACT_PERSON_ID | DocumentProvidedDetailsPEOContactPersonId | ✅ |
| CREATED_BY | DocumentProvidedDetailsPEOCreatedBy | ✅ |
| CREATION_DATE | DocumentProvidedDetailsPEOCreationDate | ✅ |
| CTFN_TYPE_CD | DocumentProvidedDetailsPEOCtfnTypeCd | ✅ |
| DOC_USG_CD | DocumentProvidedDetailsPEODocUsgCd | — |
| DOCS_PRVDD_DTLS_ID | DocumentProvidedDetailsPEODocsPrvddDtlsId | — |
| DOCUMENT_TYPE_ID | DocumentProvidedDetailsPEODocumentTypeId | — |
| DOR_ID | DocumentProvidedDetailsPEODorId | ✅ |
| JOB_DEFINITION_NAME | DocumentProvidedDetailsPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | DocumentProvidedDetailsPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | DocumentProvidedDetailsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | DocumentProvidedDetailsPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | DocumentProvidedDetailsPEOLastUpdatedBy | ✅ |
| MAPPING_COLUMN_NAME | DocumentProvidedDetailsPEOMappingColumnName | — |
| MAPPING_TABLE_NAME | DocumentProvidedDetailsPEOMappingTableName | — |
| MAPPING_TABLE_PK_ID | DocumentProvidedDetailsPEOMappingTablePkId | — |
| OBJECT_VERSION_NUMBER | DocumentProvidedDetailsPEOObjectVersionNumber | — |
| PERSON_ID | DocumentProvidedDetailsPEOPersonId | ✅ |
| PROGRAM_APP_NAME | DocumentProvidedDetailsPEOProgramAppName | — |
| PROGRAM_NAME | DocumentProvidedDetailsPEOProgramName1 | — |
| PROGRAM_UPDATE_DATE | DocumentProvidedDetailsPEOProgramUpdateDate | — |
| REJECTED_DT | DocumentProvidedDetailsPEORejectedDt | — |
| REJECTION_REASON | DocumentProvidedDetailsPEORejectionReason | ✅ |
| REQUEST_ID | DocumentProvidedDetailsPEORequestId | — |
| STATUS | DocumentProvidedDetailsPEOStatus | ✅ |
| UPLOADED_BY | DocumentProvidedDetailsPEOUploadedBy | — |
| UPLOADED_DT | DocumentProvidedDetailsPEOUploadedDt | — |
| VALIDITY_CD | DocumentProvidedDetailsPEOValidityCd | ✅ |
| VALIDITY_END_DT | DocumentProvidedDetailsPEOValidityEndDt | ✅ |
| VALIDITY_STRT_DT | DocumentProvidedDetailsPEOValidityStrtDt | ✅ |
| VALIDITY_TM_NUM | DocumentProvidedDetailsPEOValidityTmNum | ✅ |
| VERIFICATION_MODE | DocumentProvidedDetailsPEOVerificationMode | — |

---

## 📚 Referências

- [Oracle Docs — BEN_DOCS_PRVDD_DTLS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/bendocsprvdddtls.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
