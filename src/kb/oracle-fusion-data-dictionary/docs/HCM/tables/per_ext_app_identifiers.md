---
id: DOC-HCM-658
doc_type: system-doc
title: "PER_EXT_APP_IDENTIFIERS — Identificadores de Aplicações Externas"
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
  - workforce-management
  - integracao
  - external-identifiers
aliases:
  - PER_EXT_APP_IDENTIFIERS
  - per_ext_app_identifiers
  - per-ext-app-identifiers
  - identificadores-de-aplicações-externas
  - per-ext-app-identifi
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_EXT_APP_IDENTIFIERS

## 📌 Visão Geral

Armazena os **identificadores de aplicações externas** associados a pessoas. Permite vincular IDs de sistemas externos (folha de pagamento legado, ponto eletrônico, etc.) ao cadastro de pessoas do Oracle HCM.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Integração** — mapeamento de IDs entre Oracle HCM e sistemas externos.
- **Migração** — referência cruzada com sistemas legados durante migração.
- **Interoperabilidade** — suporte a interfaces com sistemas de terceiros.
- **Rastreabilidade** — identifica a pessoa em múltiplos sistemas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXT_APP_IDENTIFIER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa associada | PER_ALL_PEOPLE_F | 🟢 90% |
| 3 | EXTERNAL_APPLICATION_ID | NUMBER(18) | NULL | FK | Aplicação externa | — | 🟡 75% |
| 4 | EXTERNAL_IDENTIFIER | VARCHAR2(240) | NOT NULL | Identificação | ID da pessoa no sistema externo | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com identificador de aplicação externa)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Identificadores externos de uma pessoa
```sql
SELECT peai.EXTERNAL_IDENTIFIER, peai.EXTERNAL_APPLICATION_ID
FROM   PER_EXT_APP_IDENTIFIERS peai
WHERE  peai.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `EXTERNAL_APPLICATION_ID = :p_app_id` — Identificador de uma aplicação específica
---

## 🔒 Observações

- Tabela de mapeamento — vincula IDs de sistemas externos ao PERSON_ID do Oracle.
- Fundamental durante migrações para manter referências cruzadas.
- Pode conter múltiplos identificadores por pessoa (um para cada sistema externo).
---

## 🔗 PVOs Relacionados

### [[externalidentifierpvo|ExternalIdentifierPVO]] (HCM · BICC: 13/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| EXT_IDENTIFIER_ID | ExtIdentifierId | ✅ |
| EXT_IDENTIFIER_NUMBER | ExtIdentifierNumber | ✅ |
| EXT_IDENTIFIER_SEQ | ExtIdentifierSeq | ✅ |
| EXT_IDENTIFIER_TYPE | ExtIdentifierType | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_EXT_APP_IDENTIFIERS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perextappidentifiers.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
