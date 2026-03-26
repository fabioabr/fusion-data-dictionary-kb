---
id: DOC-PO-038
doc_type: system-doc
title: "POQ_ASSESSMENTS — Avaliações de Qualificação de Fornecedores"
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
  - avaliacao
  - qualificacao
aliases:
  - POQ_ASSESSMENTS
  - poq_assessments
  - avaliacoes-qualificacao-fornecedores
  - supplier-assessments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_ASSESSMENTS

## Visão Geral

Armazena as **avaliações de qualificação** de fornecedores no módulo Oracle Supplier Qualification Management (SQM). Cada registro representa uma avaliação iniciada contra um fornecedor, que pode englobar múltiplas qualificações (certificações, capacidades, compliance). A avaliação é o processo-pai que coordena o envio de questionários, coleta de respostas e determinação do resultado de qualificação.

> [!note] Módulo POQ
> O prefixo `POQ` identifica tabelas do submódulo **Oracle Supplier Qualification Management**, responsável por gerenciar o ciclo de vida de qualificação, certificação e avaliação de fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Qualificação de fornecedores:** Gerenciamento do processo de avaliação inicial e periódica de fornecedores.
- **Onboarding de fornecedores:** Avaliação de novos fornecedores antes de habilitá-los para transações.
- **Renovação de qualificações:** Controle de avaliações periódicas (anuais, semestrais) para manter qualificações ativas.
- **Compliance regulatório:** Demonstração de due diligence na seleção e monitoramento de fornecedores.
- **Workflow de aprovação:** Coordenação do fluxo de aprovação das avaliações (pendente, aprovada, rejeitada).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSESSMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da avaliação | — | 🟡 75% |
| 2 | ASSESSMENT_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome/título da avaliação | — | 🟡 70% |
| 3 | SUPPLIER_ID | NUMBER(18) | NOT NULL | FK | Fornecedor avaliado | [[poz_suppliers]] | 🟡 75% |
| 4 | SUPPLIER_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor avaliado | [[poz_supplier_sites_all_m]] | 🟡 65% |
| 5 | ASSESSMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da avaliação (INITIAL, PERIODIC, AD_HOC) | — | 🟡 65% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da avaliação (DRAFT, IN_PROGRESS, COMPLETED, APPROVED, REJECTED) | — | 🟡 75% |
| 7 | INITIATION_DATE | DATE | NULL | Data | Data de início da avaliação | — | 🟡 70% |
| 8 | COMPLETION_DATE | DATE | NULL | Data | Data de conclusão da avaliação | — | 🟡 70% |
| 9 | DUE_DATE | DATE | NULL | Data | Data limite para conclusão | — | 🟡 65% |
| 10 | INITIATED_BY | NUMBER(18) | NULL | FK | Usuário que iniciou a avaliação | [[per_users]] | 🟡 60% |
| 11 | OVERALL_RESULT | VARCHAR2(30) | NULL | Avaliação | Resultado consolidado (QUALIFIED, NOT_QUALIFIED, CONDITIONALLY_QUALIFIED) | — | 🟡 60% |
| 12 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários gerais sobre a avaliação | — | 🟡 65% |
| 13 | QUESTIONNAIRE_ID | NUMBER(18) | NULL | FK | Questionário associado à avaliação | [[poq_questionnaires]] | 🟡 60% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `SUPPLIER_ID` (fornecedor avaliado)
- [[poz_supplier_sites_all_m]] — via `SUPPLIER_SITE_ID` (site do fornecedor)
- [[per_users]] — via `INITIATED_BY` (usuário iniciador)
- [[poq_questionnaires]] — via `QUESTIONNAIRE_ID` (questionário base da avaliação de fornecedor)

### Tabelas-filha (FK de saída)
- [[poq_assessment_quals]] — via `ASSESSMENT_ID` (qualificações da avaliação)

### Tabelas relacionadas

---

## Uso Típico

### Avaliações ativas de um fornecedor
```sql
SELECT a.ASSESSMENT_NAME, a.ASSESSMENT_TYPE, a.STATUS,
       a.INITIATION_DATE, a.DUE_DATE, a.OVERALL_RESULT
FROM   POQ_ASSESSMENTS a
WHERE  a.SUPPLIER_ID = :p_supplier_id
  AND  a.STATUS IN ('IN_PROGRESS', 'COMPLETED')
ORDER BY a.INITIATION_DATE DESC;
```

### Avaliações pendentes próximas do prazo
```sql
SELECT a.ASSESSMENT_NAME, a.SUPPLIER_ID,
       a.DUE_DATE, a.STATUS
FROM   POQ_ASSESSMENTS a
WHERE  a.STATUS = 'IN_PROGRESS'
  AND  a.DUE_DATE BETWEEN SYSDATE AND SYSDATE + 30
ORDER BY a.DUE_DATE;
```

---

## Observações

- O campo `STATUS` controla o ciclo de vida da avaliação: `DRAFT` (rascunho), `IN_PROGRESS` (em andamento), `COMPLETED` (concluída aguardando aprovação), `APPROVED` (aprovada), `REJECTED` (rejeitada).
- O `OVERALL_RESULT` é determinado após a conclusão de todas as qualificações individuais da avaliação.
- Uma avaliação pode conter múltiplas qualificações (via [[poq_assessment_quals]]), cada uma com seu próprio resultado.
- O `ASSESSMENT_TYPE` diferencia avaliações iniciais (onboarding) de periódicas (renovação) e ad hoc (sob demanda).
- A tabela [[poq_evaluation_team]] define quem são os avaliadores responsáveis por cada avaliação.

---

## Referências

- [Oracle Docs — POQ_ASSESSMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poqassessments.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
