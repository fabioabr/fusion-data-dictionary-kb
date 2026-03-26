---
id: DOC-HCM-726
doc_type: system-doc
title: "WLF_ASSIGNMENT_RULES — Regras de Atribuição (Learning)"
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
  - learning
  - workforce-learning
  - regras-atribuição
aliases:
  - WLF_ASSIGNMENT_RULES
  - wlf_assignment_rules
  - wlf-assignment-rules
  - regras-de-atribuição-learning
  - assignment-rules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_ASSIGNMENT_RULES

## Visão Geral

Armazena as **regras de atribuição automática** de itens de aprendizado, definindo critérios para distribuição automática de treinamentos a colaboradores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Atribuição automática** — distribui treinamentos automaticamente com base em critérios predefinidos.
- **Compliance** — garante que treinamentos mandatórios sejam atribuídos a todos os elegíveis.
- **Onboarding** — atribui automaticamente treinamentos para novos colaboradores.
- **Reciclagem** — programa re-treinamentos periódicos via regras temporais.
- **Governança** — centraliza as regras de distribuição de conteúdo educacional.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra | — | 🟡 80% |
| 2 | RULE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da regra de atribuição | — | 🟡 75% |
| 3 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado a ser atribuído | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 4 | RULE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da regra (automática, manual, periódica) | — | 🟡 70% |
| 5 | CRITERIA_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de critério (departamento, cargo, etc.) | — | 🟡 70% |
| 6 | CRITERIA_VALUE | VARCHAR2(240) | NULL | Dados | Valor do critério de seleção | — | 🟡 65% |
| 7 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Controle | Indica se a regra está ativa (Y/N) | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- [[wlf_assignment_tasks_f]] — via `ASSIGNMENT_RULE_ID` (tarefas geradas pela regra)

---

## Uso Típico

### Regras ativas de atribuição
```sql
SELECT ar.RULE_NAME, ar.RULE_TYPE, ar.CRITERIA_TYPE, ar.CRITERIA_VALUE
FROM   WLF_ASSIGNMENT_RULES ar
WHERE  ar.ACTIVE_FLAG = 'Y'
ORDER BY ar.RULE_NAME;
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Apenas regras ativas
- `LEARNING_ITEM_ID = :p_item_id` — Regras de um item específico

---

## Observações

- Tabela de configuração — não possui sufixo _F (não é date-effective).
- Regras podem ser desativadas sem exclusão via ACTIVE_FLAG.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Os critérios são flexíveis e podem variar conforme a implementação.

---

## Referências

- [Oracle Docs — WLF_ASSIGNMENT_RULES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfassignmentrules.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
