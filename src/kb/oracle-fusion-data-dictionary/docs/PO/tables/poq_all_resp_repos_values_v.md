---
id: DOC-PO-037
doc_type: system-doc
title: "POQ_ALL_RESP_REPOS_VALUES_V — Valores de Respostas em Repositórios de Qualificação (View)"
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
  - supplier-qualification
  - repositorio
  - qualificacao
  - view
aliases:
  - POQ_ALL_RESP_REPOS_VALUES_V
  - poq_all_resp_repos_values_v
  - valores-respostas-repositorios-qualificacao
  - resp-repos-values
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_ALL_RESP_REPOS_VALUES_V

## Visão Geral

**View** que consolida os **valores de respostas armazenados em repositórios** de qualificação de fornecedores no módulo Oracle Supplier Qualification Management (SQM). Diferente da view de respostas de questionários, esta apresenta os valores já persistidos no repositório de qualificação — ou seja, as respostas consolidadas e aprovadas que compõem o perfil de qualificação do fornecedor.

> [!note] Sufixo _V
> O sufixo `_V` indica que este é um **view** (visão). Consolida dados de múltiplas tabelas-base do módulo POQ para facilitar consultas analíticas sobre o repositório de qualificação.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Perfil de qualificação do fornecedor:** Consulta dos dados consolidados de qualificação armazenados no repositório.
- **Pré-qualificação de fornecedores:** Verificação se um fornecedor atende aos critérios mínimos antes de ser convidado a uma negociação.
- **Monitoramento contínuo:** Acompanhamento de respostas que expiram ou precisam ser atualizadas.
- **Relatórios regulatórios:** Extração de dados de qualificação para compliance e auditoria.
- **Integração com BI:** Fonte de dados para dashboards de gestão de fornecedores.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_REPOS_VALUE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do valor no repositório | — | 🟡 65% |
| 2 | QUALIFICATION_ID | NUMBER(18) | NULL | FK | Identificador da qualificação | [[poq_assessment_quals]] | 🟡 65% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Identificador da pergunta | [[poq_questions]] | 🟡 65% |
| 4 | SUPPLIER_ID | NUMBER(18) | NULL | FK | Fornecedor qualificado | [[poz_suppliers]] | 🟡 70% |
| 5 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Identificação | Nome do fornecedor (desnormalizado) | — | 🟡 60% |
| 6 | QUESTION_TEXT | VARCHAR2(4000) | NULL | Texto | Texto da pergunta (desnormalizado) | — | 🟡 60% |
| 7 | RESPONSE_VALUE | VARCHAR2(4000) | NULL | Texto | Valor da resposta armazenado no repositório | — | 🟡 70% |
| 8 | RESPONSE_NUMBER_VALUE | NUMBER | NULL | Numérico | Valor numérico da resposta (quando aplicável) | — | 🟡 60% |
| 9 | RESPONSE_DATE_VALUE | DATE | NULL | Data | Valor de data da resposta (quando aplicável) | — | 🟡 60% |
| 10 | QUESTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da pergunta (TEXT, NUMBER, DATE, SINGLE_SELECT, MULTI_SELECT) | — | 🟡 60% |
| 11 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da resposta no repositório | — | 🟡 55% |
| 12 | QUALIFICATION_NAME | VARCHAR2(240) | NULL | Identificação | Nome da qualificação (desnormalizado) | — | 🟡 55% |
| 13 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do valor no repositório (CURRENT, EXPIRED, PENDING) | — | 🟡 55% |
| 14 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data/hora de criação | — | 🟢 90% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NULL | Auditoria | Data/hora da última alteração | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-base (fontes do view)

### Views relacionadas

---

## Uso Típico

### Perfil de qualificação atual de um fornecedor
```sql
SELECT v.QUALIFICATION_NAME, v.QUESTION_TEXT,
       v.RESPONSE_VALUE, v.EXPIRATION_DATE, v.STATUS
FROM   POQ_ALL_RESP_REPOS_VALUES_V v
WHERE  v.SUPPLIER_ID = :p_supplier_id
  AND  v.STATUS = 'CURRENT'
ORDER BY v.QUALIFICATION_NAME, v.QUESTION_ID;
```

### Respostas expiradas que necessitam renovação
```sql
SELECT v.SUPPLIER_NAME, v.QUALIFICATION_NAME,
       v.QUESTION_TEXT, v.EXPIRATION_DATE
FROM   POQ_ALL_RESP_REPOS_VALUES_V v
WHERE  v.STATUS = 'EXPIRED'
   OR  v.EXPIRATION_DATE < SYSDATE
ORDER BY v.EXPIRATION_DATE;
```

---

## Observações

- Esta view apresenta os dados **consolidados no repositório**, diferenciando-se de [[poq_all_qnaire_resp_values_v]] que mostra respostas diretamente dos questionários.
- O campo `STATUS` indica se a resposta está vigente (`CURRENT`), expirada (`EXPIRED`) ou pendente de aprovação (`PENDING`).
- A coluna `EXPIRATION_DATE` é relevante para processos de qualificação contínua — respostas expiradas podem bloquear a participação do fornecedor em novas negociações.
- Por ser uma view, o desempenho depende dos índices das tabelas-base subjacentes; consultas com filtros em `SUPPLIER_ID` e `STATUS` são recomendadas.
- As colunas e estrutura exatas podem variar conforme o release do Oracle Fusion; recomenda-se validação no ambiente.

---

## Referências

- [Oracle Docs — POQ_ALL_RESP_REPOS_VALUES_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poqallrespreposvaluesv.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[responserepositoryvaluespvo|ResponseRepositoryValuesPVO]] (PO · BICC: 14/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACC_RESPONSE_ID | RespRepositoryValueAccResponseId | ✅ |
| ACC_RESPONSE_TEXT | RespRepositoryValueAccResponseText | ✅ |
| CREATED_BY | RespRepositoryValueCreatedBy | ✅ |
| CREATION_DATE | RespRepositoryValueCreationDate | ✅ |
| CRITICAL_RESPONSE_FLAG | CriticalResponseFlag | — |
| LAST_UPDATE_DATE | RespRepositoryValueLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RespRepositoryValueLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RespRepositoryValueLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | RespRepositoryValueObjectVersionNumber | ✅ |
| RESP_REPOSITORY_VALUE_ID | RespRepositoryValueId | ✅ |
| RESPONSE_REPOSITORY_ID | RespRepositoryValueResponseRepositoryId | ✅ |
| RESPONSE_VALUE_DATE | RespRepositoryValueResponseValueDate | ✅ |
| RESPONSE_VALUE_DATETIME | RespRepositoryValueResponseValueDatetime | ✅ |
| RESPONSE_VALUE_NUM | RespRepositoryValueResponseValueNum | ✅ |
| RESPONSE_VALUE_TXT | RespRepositoryValueResponseValueTxt | ✅ |
