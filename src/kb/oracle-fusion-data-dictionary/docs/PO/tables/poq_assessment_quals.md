---
id: DOC-PO-039
doc_type: system-doc
title: "POQ_ASSESSMENT_QUALS — Qualificações de Avaliação de Fornecedores"
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
  - certificacao
aliases:
  - POQ_ASSESSMENT_QUALS
  - poq_assessment_quals
  - qualificacoes-avaliacao-fornecedores
  - assessment-qualifications
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_ASSESSMENT_QUALS

## Visão Geral

Armazena as **qualificações individuais** associadas a uma avaliação de fornecedor no módulo Oracle Supplier Qualification Management (SQM). Cada registro representa uma qualificação específica (ex.: ISO 9001, capacidade financeira, compliance ambiental) avaliada no contexto de uma avaliação global do fornecedor, com seu próprio resultado, status e datas de vigência.

> [!note] Módulo POQ
> O prefixo `POQ` identifica tabelas do submódulo **Oracle Supplier Qualification Management**. Esta tabela é filha de [[poq_assessments]] e detalha cada qualificação avaliada.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de qualificações:** Controle individual de cada tipo de qualificação de um fornecedor (certificações, licenças, compliance).
- **Vigência de qualificações:** Monitoramento de datas de validade e necessidade de renovação.
- **Pré-requisito de compras:** Verificação se o fornecedor possui qualificações ativas e válidas antes de permitir transações.
- **Scoring de qualificação:** Atribuição de notas e resultados por qualificação individual.
- **Auditoria e compliance:** Rastreamento detalhado do resultado de cada qualificação avaliada.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSESSMENT_QUAL_ID | NUMBER(18) | NOT NULL | PK | Identificador único da qualificação da avaliação | — | 🟡 70% |
| 2 | ASSESSMENT_ID | NUMBER(18) | NOT NULL | FK | Avaliação-pai | [[poq_assessments]] | 🟡 75% |
| 3 | QUALIFICATION_ID | NUMBER(18) | NOT NULL | FK | Tipo de qualificação (definição/template) | [[poq_qualifications]] | 🟡 70% |
| 4 | QUALIFICATION_NAME | VARCHAR2(240) | NULL | Identificação | Nome da qualificação (desnormalizado) | — | 🟡 65% |
| 5 | RESULT | VARCHAR2(30) | NULL | Avaliação | Resultado da qualificação (QUALIFIED, NOT_QUALIFIED, CONDITIONALLY_QUALIFIED) | — | 🟡 70% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificação | Status da qualificação (PENDING, EVALUATED, APPROVED, EXPIRED) | — | 🟡 70% |
| 7 | SCORE | NUMBER | NULL | Avaliação | Pontuação obtida na qualificação | — | 🟡 60% |
| 8 | MAX_SCORE | NUMBER | NULL | Avaliação | Pontuação máxima possível | — | 🟡 55% |
| 9 | EFFECTIVE_FROM | DATE | NULL | Data | Data de início da vigência da qualificação | — | 🟡 65% |
| 10 | EFFECTIVE_TO | DATE | NULL | Data | Data de expiração da qualificação | — | 🟡 65% |
| 11 | QUESTIONNAIRE_ID | NUMBER(18) | NULL | FK | Questionário utilizado para avaliar esta qualificação | [[poq_questionnaires]] | 🟡 60% |
| 12 | EVALUATOR_COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários do avaliador sobre a qualificação | — | 🟡 60% |
| 13 | SUPPLIER_ID | NUMBER(18) | NULL | FK | Fornecedor avaliado (desnormalizado) | [[poz_suppliers]] | 🟡 65% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_assessments]] — via `ASSESSMENT_ID` (avaliação-pai)
- [[poq_qualifications]] — via `QUALIFICATION_ID` (definição/tipo de qualificação)
- [[poq_questionnaires]] — via `QUESTIONNAIRE_ID` (questionário utilizado na qualificação)
- [[poz_suppliers]] — via `SUPPLIER_ID` (fornecedor avaliado na qualificação)

### Tabelas-filha (FK de saída)
- Sem tabelas-filha conhecidas diretamente.

### Views relacionadas

---

## Uso Típico

### Qualificações de uma avaliação
```sql
SELECT aq.QUALIFICATION_NAME, aq.RESULT, aq.STATUS,
       aq.SCORE, aq.MAX_SCORE,
       aq.EFFECTIVE_FROM, aq.EFFECTIVE_TO
FROM   POQ_ASSESSMENT_QUALS aq
WHERE  aq.ASSESSMENT_ID = :p_assessment_id
ORDER BY aq.QUALIFICATION_NAME;
```

### Qualificações ativas de um fornecedor
```sql
SELECT aq.QUALIFICATION_NAME, aq.RESULT,
       aq.EFFECTIVE_FROM, aq.EFFECTIVE_TO
FROM   POQ_ASSESSMENT_QUALS aq
       JOIN POQ_ASSESSMENTS a ON aq.ASSESSMENT_ID = a.ASSESSMENT_ID
WHERE  a.SUPPLIER_ID = :p_supplier_id
  AND  aq.STATUS = 'APPROVED'
  AND  (aq.EFFECTIVE_TO IS NULL OR aq.EFFECTIVE_TO >= SYSDATE)
ORDER BY aq.QUALIFICATION_NAME;
```

### Qualificações próximas da expiração
```sql
SELECT a.SUPPLIER_ID, aq.QUALIFICATION_NAME,
       aq.EFFECTIVE_TO
FROM   POQ_ASSESSMENT_QUALS aq
       JOIN POQ_ASSESSMENTS a ON aq.ASSESSMENT_ID = a.ASSESSMENT_ID
WHERE  aq.STATUS = 'APPROVED'
  AND  aq.EFFECTIVE_TO BETWEEN SYSDATE AND SYSDATE + 90
ORDER BY aq.EFFECTIVE_TO;
```

---

## Observações

- O `RESULT` determina se o fornecedor atende à qualificação: `QUALIFIED` (aprovado), `NOT_QUALIFIED` (reprovado), `CONDITIONALLY_QUALIFIED` (aprovado com condições).
- Os campos `EFFECTIVE_FROM` e `EFFECTIVE_TO` controlam a vigência da qualificação — qualificações expiradas podem bloquear automaticamente transações com o fornecedor.
- O `STATUS` controla o ciclo de vida: `PENDING` (aguardando avaliação), `EVALUATED` (avaliada), `APPROVED` (resultado aprovado), `EXPIRED` (expirada).
- Uma avaliação (`POQ_ASSESSMENTS`) pode conter múltiplas qualificações, cada uma avaliada independentemente.
- A coluna `SCORE` permite comparações numéricas entre fornecedores para a mesma qualificação.

---

## Referências

- [Oracle Docs — POQ_ASSESSMENT_QUALS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poqassessmentquals.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
