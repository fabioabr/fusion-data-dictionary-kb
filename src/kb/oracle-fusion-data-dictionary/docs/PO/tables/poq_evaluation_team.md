---
id: DOC-PO-040
doc_type: system-doc
title: "POQ_EVALUATION_TEAM — Equipe de Avaliação de Qualificação de Fornecedores"
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
  - equipe
  - qualificacao
aliases:
  - POQ_EVALUATION_TEAM
  - poq_evaluation_team
  - equipe-avaliacao-qualificacao
  - evaluation-team
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_EVALUATION_TEAM

## Visão Geral

Armazena os **membros da equipe de avaliação** de qualificação de fornecedores no módulo Oracle Supplier Qualification Management (SQM). Cada registro representa um avaliador designado para participar de uma avaliação de fornecedor, incluindo seu papel, responsabilidades e status de participação no processo de qualificação.

> [!note] Módulo POQ
> O prefixo `POQ` identifica tabelas do submódulo **Oracle Supplier Qualification Management**. Esta tabela define quem avalia as qualificações dos fornecedores em processos gerenciados por [[poq_assessments]].

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Composição da equipe avaliadora:** Definição de quem participa da avaliação de qualificação de fornecedores.
- **Segregação de funções:** Garantia de que a avaliação é realizada por múltiplos avaliadores independentes.
- **Workflow de avaliação:** Controle do progresso individual de cada avaliador (pendente, concluído).
- **Auditoria de processo:** Rastreamento de quem avaliou cada fornecedor e quando.
- **Notificações:** Base para envio de lembretes e notificações aos avaliadores sobre tarefas pendentes.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVALUATION_TEAM_ID | NUMBER(18) | NOT NULL | PK | Identificador único do membro da equipe de avaliação | — | 🟡 70% |
| 2 | ASSESSMENT_ID | NUMBER(18) | NOT NULL | FK | Avaliação à qual o membro está associado | [[poq_assessments]] | 🟡 75% |
| 3 | EVALUATOR_ID | NUMBER(18) | NOT NULL | FK | Identificador do avaliador (usuário) | [[per_users]] | 🟡 70% |
| 4 | EVALUATOR_NAME | VARCHAR2(360) | NULL | Identificação | Nome do avaliador (desnormalizado) | — | 🟡 60% |
| 5 | ROLE_TYPE | VARCHAR2(30) | NULL | Classificação | Papel do avaliador (LEAD, MEMBER, APPROVER, OBSERVER) | — | 🟡 65% |
| 6 | EVALUATION_STATUS | VARCHAR2(30) | NULL | Classificação | Status da avaliação do membro (PENDING, IN_PROGRESS, COMPLETED) | — | 🟡 65% |
| 7 | COMPLETION_DATE | DATE | NULL | Data | Data em que o avaliador concluiu sua avaliação | — | 🟡 60% |
| 8 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários do avaliador | — | 🟡 60% |
| 9 | NOTIFICATION_DATE | DATE | NULL | Data | Data da última notificação enviada ao avaliador | — | 🟡 50% |
| 10 | SEQUENCE_NUMBER | NUMBER | NULL | Controle | Sequência do avaliador (para workflows sequenciais) | — | 🟡 55% |
| 11 | QUALIFICATION_ID | NUMBER(18) | NULL | FK | Qualificação específica atribuída ao avaliador (quando por qualificação) | [[poq_assessment_quals]] | 🟡 55% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 16 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_assessments]] — via `ASSESSMENT_ID` (avaliação à qual o membro da equipe pertence)
- [[per_users]] — via `EVALUATOR_ID` (usuário avaliador na equipe de qualificação)
- [[poq_assessment_quals]] — via `QUALIFICATION_ID` (qualificação atribuída)

### Tabelas-filha (FK de saída)
- Sem tabelas-filha conhecidas diretamente.

### Tabelas relacionadas

---

## Uso Típico

### Equipe de avaliação de uma avaliação
```sql
SELECT et.EVALUATOR_NAME, et.ROLE_TYPE,
       et.EVALUATION_STATUS, et.COMPLETION_DATE
FROM   POQ_EVALUATION_TEAM et
WHERE  et.ASSESSMENT_ID = :p_assessment_id
ORDER BY et.SEQUENCE_NUMBER;
```

### Avaliadores com tarefas pendentes
```sql
SELECT et.EVALUATOR_NAME, a.ASSESSMENT_NAME,
       a.DUE_DATE, et.EVALUATION_STATUS
FROM   POQ_EVALUATION_TEAM et
       JOIN POQ_ASSESSMENTS a ON et.ASSESSMENT_ID = a.ASSESSMENT_ID
WHERE  et.EVALUATION_STATUS = 'PENDING'
  AND  a.STATUS = 'IN_PROGRESS'
ORDER BY a.DUE_DATE;
```

### Progresso da avaliação por equipe
```sql
SELECT a.ASSESSMENT_NAME,
       COUNT(*) AS total_avaliadores,
       SUM(CASE WHEN et.EVALUATION_STATUS = 'COMPLETED' THEN 1 ELSE 0 END) AS concluidos
FROM   POQ_EVALUATION_TEAM et
       JOIN POQ_ASSESSMENTS a ON et.ASSESSMENT_ID = a.ASSESSMENT_ID
WHERE  a.STATUS = 'IN_PROGRESS'
GROUP BY a.ASSESSMENT_NAME;
```

---

## Observações

- O campo `ROLE_TYPE` diferencia os papéis na equipe: `LEAD` (líder da avaliação), `MEMBER` (avaliador regular), `APPROVER` (aprovador final), `OBSERVER` (observador sem poder de decisão).
- O `EVALUATION_STATUS` controla o progresso individual: `PENDING` (aguardando), `IN_PROGRESS` (em avaliação), `COMPLETED` (concluído).
- A coluna `QUALIFICATION_ID` permite atribuir avaliadores específicos para qualificações específicas (ex.: avaliador técnico para ISO, avaliador financeiro para capacidade financeira).
- O `SEQUENCE_NUMBER` é relevante quando o workflow de avaliação é sequencial (cada avaliador só pode avaliar após o anterior concluir).
- A avaliação global só pode ser finalizada quando todos os membros com `ROLE_TYPE` relevante tiverem status `COMPLETED`.

---

## Referências

- [Oracle Docs — POQ_EVALUATION_TEAM](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poqevaluationteam.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[evaluationteammemberpvo|EvaluationTeamMemberPVO]] (PO · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDED_BY | EvaluationTeamAddedBy | ✅ |
| CREATED_BY | EvaluationTeamCreatedBy | ✅ |
| CREATION_DATE | EvaluationTeamCreationDate | ✅ |
| EVALUATION_TEAM_ID | EvaluationTeamId | ✅ |
| INITIATIVE_ID | EvaluationTeamInitiativeId | ✅ |
| LAST_UPDATE_DATE | EvaluationTeamLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EvaluationTeamLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | EvaluationTeamLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | EvaluationTeamObjectVersionNumber | ✅ |
| TEAM_MEMBER_ID | EvaluationTeamTeamMemberId | ✅ |

### [[initiativeevaluationteamextractpvo|InitiativeEvaluationTeamExtractPVO]] (PO · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDED_BY | AddedBy | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EVALUATION_TEAM_ID | EvaluationTeamId | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| TEAM_MEMBER_ID | TeamMemberId | ✅ |
