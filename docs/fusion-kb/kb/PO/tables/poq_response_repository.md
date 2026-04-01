---
id: DOC-PO-060
doc_type: system-doc
title: "POQ_RESPONSE_REPOSITORY — Repositório de Respostas Padrão de Qualificação"
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
  - qualificacao
  - response-repository
  - supplier-qualification
aliases:
  - POQ_RESPONSE_REPOSITORY
  - poq_response_repository
  - repositorio-respostas-qualificacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_RESPONSE_REPOSITORY

## 📌 Visão Geral

Armazena o **repositório centralizado de respostas padrão** para questionários de qualificação de fornecedores. Funciona como uma biblioteca de respostas reutilizáveis que fornecedores podem salvar e reaplicar em futuros processos de qualificação, evitando retrabalho. Cada registro contém uma resposta previamente fornecida associada a um fornecedor e a uma pergunta específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reutilização de respostas:** Fornecedores podem recuperar respostas anteriores ao preencher novos questionários.
- **Produtividade:** Redução do tempo de preenchimento de questionários repetitivos.
- **Consistência:** Garantia de que respostas padronizadas sejam mantidas entre processos.
- **Gestão de conhecimento do fornecedor:** Repositório centralizado das informações de qualificação do fornecedor.
- **Pré-qualificação:** Utilização de respostas armazenadas para processos de pré-qualificação automática.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_REPOSITORY_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro no repositório | — | 🟡 70% |
| 2 | SUPPLIER_ID | NUMBER(18) | NOT NULL | FK | Fornecedor proprietário da resposta | [[ap_suppliers]] | 🟡 70% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Pergunta à qual a resposta se refere | [[poq_questions_vl]] | 🟡 70% |
| 4 | RESPONSE_VALUE | VARCHAR2(4000) | NULL | Dados | Valor textual da resposta armazenada | — | 🟡 70% |
| 5 | RESPONSE_NUMBER | NUMBER | NULL | Dados | Valor numérico da resposta (quando aplicável) | — | 🟡 60% |
| 6 | RESPONSE_DATE | DATE | NULL | Dados | Valor de data da resposta (quando aplicável) | — | 🟡 60% |
| 7 | QUESTIONNAIRE_ID | NUMBER(18) | NULL | FK | Questionário de origem da resposta | [[poq_questnaires_vl]] | 🟡 60% |
| 8 | SOURCE_RESPONSE_ID | NUMBER(18) | NULL | FK | Resposta original que gerou este registro no repositório | [[poq_qual_responses]] | 🟡 55% |
| 9 | LAST_USED_DATE | DATE | NULL | Data | Data da última reutilização desta resposta | — | 🟡 55% |
| 10 | USAGE_COUNT | NUMBER | NULL | Estatísticas | Quantidade de vezes que a resposta foi reutilizada | — | 🟡 50% |
| 11 | ATTACHMENT_EXISTS_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se há anexo associado à resposta (Y/N) | — | 🟡 50% |
| 12 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro: ACTIVE, INACTIVE, ARCHIVED | — | 🟡 55% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ap_suppliers]] — via `SUPPLIER_ID` (fornecedor do repositório de respostas)
- [[poq_questions_vl]] — via `QUESTION_ID` (pergunta respondida no repositório de respostas)
- [[poq_questnaires_vl]] — via `QUESTIONNAIRE_ID` (questionário de origem)
- [[poq_qual_responses]] — via `SOURCE_RESPONSE_ID` (resposta original)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Respostas salvas por fornecedor
```sql
SELECT rr.RESPONSE_REPOSITORY_ID,
       rr.QUESTION_ID,
       rr.RESPONSE_VALUE,
       rr.LAST_USED_DATE,
       rr.USAGE_COUNT
FROM   POQ_RESPONSE_REPOSITORY rr
WHERE  rr.SUPPLIER_ID = :p_supplier_id
  AND  rr.STATUS = 'ACTIVE'
ORDER BY rr.LAST_USED_DATE DESC;
```

### Respostas mais reutilizadas
```sql
SELECT rr.QUESTION_ID,
       rr.RESPONSE_VALUE,
       rr.USAGE_COUNT,
       rr.SUPPLIER_ID
FROM   POQ_RESPONSE_REPOSITORY rr
WHERE  rr.STATUS = 'ACTIVE'
  AND  rr.USAGE_COUNT > 1
ORDER BY rr.USAGE_COUNT DESC;
```

### Pré-carregar respostas para novo questionário
```sql
SELECT rr.QUESTION_ID,
       rr.RESPONSE_VALUE,
       rr.RESPONSE_NUMBER,
       rr.RESPONSE_DATE
FROM   POQ_RESPONSE_REPOSITORY rr
WHERE  rr.SUPPLIER_ID = :p_supplier_id
  AND  rr.QUESTION_ID IN (
         SELECT qs.QUESTION_ID
         FROM   POQ_QUESTION_STRUCTURE_V qs
         WHERE  qs.QUESTIONNAIRE_ID = :p_new_questionnaire_id
       )
  AND  rr.STATUS = 'ACTIVE';
```

---

## 🔒 Observações

- O repositório é por fornecedor (`SUPPLIER_ID`) — cada fornecedor mantém seu próprio conjunto de respostas salvas.
- O campo `SOURCE_RESPONSE_ID` (confiança baixa) permite rastrear de qual submissão a resposta foi originalmente copiada.
- `USAGE_COUNT` e `LAST_USED_DATE` (confiança baixa) podem não estar presentes em todos os releases — validar no ambiente.
- Respostas com `STATUS = 'ARCHIVED'` não são exibidas ao fornecedor, mas são mantidas para auditoria.
- Esta tabela é particularmente útil em organizações com processos frequentes de requalificação, onde fornecedores respondem a questionários similares periodicamente.
- O `ATTACHMENT_EXISTS_FLAG` indica que documentos de suporte (certidões, balanços, etc.) estão associados à resposta.

---

## 🔗 PVOs Relacionados

### [[qualarearepositoryresponsepvo|QualAreaRepositoryResponsePVO]] (PO · BICC: 31/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | ResponseRepositoryAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | ResponseRepositoryAcceptanceNote | ✅ |
| ACCEPTED_BY | ResponseRepositoryAcceptedBy | ✅ |
| AGGREGATE_RESPONSE_FLAG | AggregateResponseFlag | ✅ |
| BATCH_ID | ResponseRepositoryBatchId | ✅ |
| CREATED_BY | ResponseRepositoryCreatedBy | ✅ |
| CREATION_DATE | ResponseRepositoryCreationDate | ✅ |
| DATA_SOURCE_ID | ResponseRepositoryDataSourceId | ✅ |
| DATA_SOURCE_TYPE | ResponseRepositoryDataSourceType | ✅ |
| FIRST_SUBMISSION_DATE | ResponseRepositoryFirstSubmissionDate | ✅ |
| INTERNAL_RESPONDENT_ID | ResponseRepositoryInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | ResponseRepositoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseRepositoryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ResponseRepositoryLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | ResponseRepositoryMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | ResponseRepositoryObjectVersionNumber | ✅ |
| ORIGINAL_QUESTION_ID | ResponseRepositoryOriginalQuestionId | ✅ |
| QUESTION_ID | ResponseRepositoryQuestionId | ✅ |
| REQUEST_ID | ResponseRepositoryRequestId | ✅ |
| RESPONDER_TYPE | ResponseRepositoryResponderType | ✅ |
| RESPONSE_ARCHIVE_DATE | ResponseRepositoryResponseArchiveDate | ✅ |
| RESPONSE_COMMENTS | ResponseRepositoryResponseComments | ✅ |
| RESPONSE_REPOSITORY_ID | ResponseRepositoryId | ✅ |
| RESPONSE_STATUS | ResponseRepositoryResponseStatus | ✅ |
| RESPONSE_SUBMISSION_DATE | ResponseRepositoryResponseSubmissionDate | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | ResponseRepositorySupplierContactPartyId | ✅ |
| SUPPLIER_ID | ResponseRepositorySupplierId | ✅ |
| SUPPLIER_SITE_ID | ResponseRepositorySupplierSiteId | ✅ |
| SURROG_ENTERED_BY | ResponseRepositorySurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | ResponseRepositorySurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | ResponseRepositorySurrogResponseFlag | ✅ |

### [[qualificationresponsespvo|QualificationResponsesPVO]] (PO · BICC: 29/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | RespRepAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | RespRepAcceptanceNote | ✅ |
| ACCEPTED_BY | RespRepAcceptedBy | ✅ |
| AGGREGATE_RESPONSE_FLAG | AggregateResponseFlag | — |
| BATCH_ID | RespRepBatchId | ✅ |
| CREATED_BY | RespRepCreatedBy | ✅ |
| CREATION_DATE | RespRepCreationDate | ✅ |
| DATA_SOURCE_ID | RespRepDataSourceId | ✅ |
| DATA_SOURCE_TYPE | RespRepDataSourceType | ✅ |
| FIRST_SUBMISSION_DATE | RespRepFirstSubmissionDate | ✅ |
| INTERNAL_RESPONDENT_ID | RespRepInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | RespRepLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RespRepLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RespRepLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | RespRepMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | RespRepObjectVersionNumber | ✅ |
| ORIGINAL_QUESTION_ID | RespRepOriginalQuestionId | ✅ |
| QUESTION_ID | RespRepQuestionId | ✅ |
| REQUEST_ID | RespRepRequestId | ✅ |
| RESPONDER_TYPE | RespRepResponderType | ✅ |
| RESPONSE_ARCHIVE_DATE | RespRepResponseArchiveDate | ✅ |
| RESPONSE_COMMENTS | RespRepResponseComments | ✅ |
| RESPONSE_REPOSITORY_ID | RespRepResponseRepositoryId | ✅ |
| RESPONSE_STATUS | RespRepResponseStatus | ✅ |
| RESPONSE_SUBMISSION_DATE | RespRepResponseSubmissionDate | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | RespRepSupplierContactPartyId | ✅ |
| SUPPLIER_ID | RespRepSupplierId | ✅ |
| SUPPLIER_SITE_ID | RespRepSupplierSiteId | ✅ |
| SURROG_ENTERED_BY | RespRepSurrogEnteredBy | — |
| SURROG_ENTRY_DATE | RespRepSurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | RespRepSurrogResponseFlag | ✅ |

### [[repositoryresponseextractpvo|RepositoryResponseExtractPVO]] (PO · BICC: 30/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | AcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | AcceptanceNote | ✅ |
| ACCEPTED_BY | AcceptedBy | ✅ |
| BATCH_ID | BatchId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SOURCE_ID | DataSourceId | ✅ |
| DATA_SOURCE_TYPE | DataSourceType | ✅ |
| FIRST_SUBMISSION_DATE | FirstSubmissionDate | ✅ |
| INTERNAL_RESPONDENT_ID | InternalRespondentId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | MergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORIGINAL_QUESTION_ID | OriginalQuestionId | ✅ |
| QUESTION_ID | QuestionId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| RESPONDER_TYPE | ResponderType | ✅ |
| RESPONSE_ARCHIVE_DATE | ResponseArchiveDate | ✅ |
| RESPONSE_COMMENTS | ResponseComments | ✅ |
| RESPONSE_REPOSITORY_ID | ResponseRepositoryId | ✅ |
| RESPONSE_STATUS | ResponseStatus | ✅ |
| RESPONSE_SUBMISSION_DATE | ResponseSubmissionDate | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | SupplierContactPartyId | ✅ |
| SUPPLIER_ID | SupplierId | ✅ |
| SUPPLIER_SITE_ID | SupplierSiteId | ✅ |
| SURROG_ENTERED_BY | SurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | SurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | SurrogResponseFlag | ✅ |

### [[repositoryresponsepvo|RepositoryResponsePVO]] (PO · BICC: 31/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | ResponseRepositoryAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | ResponseRepositoryAcceptanceNote | ✅ |
| ACCEPTED_BY | ResponseRepositoryAcceptedBy | ✅ |
| AGGREGATE_RESPONSE_FLAG | AggregateResponseFlag | ✅ |
| BATCH_ID | ResponseRepositoryBatchId | ✅ |
| CREATED_BY | ResponseRepositoryCreatedBy | ✅ |
| CREATION_DATE | ResponseRepositoryCreationDate | ✅ |
| DATA_SOURCE_ID | ResponseRepositoryDataSourceId | ✅ |
| DATA_SOURCE_TYPE | ResponseRepositoryDataSourceType | ✅ |
| FIRST_SUBMISSION_DATE | ResponseRepositoryFirstSubmissionDate | ✅ |
| INTERNAL_RESPONDENT_ID | ResponseRepositoryInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | ResponseRepositoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResponseRepositoryLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ResponseRepositoryLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | ResponseRepositoryMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | ResponseRepositoryObjectVersionNumber | ✅ |
| ORIGINAL_QUESTION_ID | ResponseRepositoryOriginalQuestionId | ✅ |
| QUESTION_ID | ResponseRepositoryQuestionId | ✅ |
| REQUEST_ID | ResponseRepositoryRequestId | ✅ |
| RESPONDER_TYPE | ResponseRepositoryResponderType | ✅ |
| RESPONSE_ARCHIVE_DATE | ResponseRepositoryResponseArchiveDate | ✅ |
| RESPONSE_COMMENTS | ResponseRepositoryResponseComments | ✅ |
| RESPONSE_REPOSITORY_ID | ResponseRepositoryId | ✅ |
| RESPONSE_STATUS | ResponseRepositoryResponseStatus | ✅ |
| RESPONSE_SUBMISSION_DATE | ResponseRepositoryResponseSubmissionDate | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | ResponseRepositorySupplierContactPartyId | ✅ |
| SUPPLIER_ID | ResponseRepositorySupplierId | ✅ |
| SUPPLIER_SITE_ID | ResponseRepositorySupplierSiteId | ✅ |
| SURROG_ENTERED_BY | ResponseRepositorySurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | ResponseRepositorySurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | ResponseRepositorySurrogResponseFlag | ✅ |

### [[responserepositoryvaluespvo|ResponseRepositoryValuesPVO]] (PO · BICC: 31/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | RepResponseAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | RepResponseAcceptanceNote | ✅ |
| ACCEPTED_BY | RepResponseAcceptedBy | ✅ |
| AGGREGATE_RESPONSE_FLAG | AggregateResponseFlag | ✅ |
| BATCH_ID | RepResponseBatchId | ✅ |
| CREATED_BY | RepResponseCreatedBy | ✅ |
| CREATION_DATE | RepResponseCreationDate | ✅ |
| DATA_SOURCE_ID | RepResponseDataSourceId | ✅ |
| DATA_SOURCE_TYPE | RepResponseDataSourceType | ✅ |
| FIRST_SUBMISSION_DATE | RepResponseFirstSubmissionDate | ✅ |
| INTERNAL_RESPONDENT_ID | RepResponseInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | RepResponseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RepResponseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RepResponseLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | RepResponseMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | RepResponseObjectVersionNumber | ✅ |
| ORIGINAL_QUESTION_ID | RepResponseOriginalQuestionId | ✅ |
| QUESTION_ID | RepResponseQuestionId | ✅ |
| REQUEST_ID | RepResponseRequestId | ✅ |
| RESPONDER_TYPE | RepResponseResponderType | ✅ |
| RESPONSE_ARCHIVE_DATE | RepResponseResponseArchiveDate | ✅ |
| RESPONSE_COMMENTS | RepResponseResponseComments | ✅ |
| RESPONSE_REPOSITORY_ID | RepResponseResponseRepositoryId | ✅ |
| RESPONSE_STATUS | RepResponseResponseStatus | ✅ |
| RESPONSE_SUBMISSION_DATE | RepResponseResponseSubmissionDate | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | RepResponseSupplierContactPartyId | ✅ |
| SUPPLIER_ID | RepResponseSupplierId | ✅ |
| SUPPLIER_SITE_ID | RepResponseSupplierSiteId | ✅ |
| SURROG_ENTERED_BY | RepResponseSurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | RepResponseSurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | RepResponseSurrogResponseFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
