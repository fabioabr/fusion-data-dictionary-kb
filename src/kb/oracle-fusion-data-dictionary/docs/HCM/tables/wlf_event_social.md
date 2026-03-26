---
id: DOC-HCM-733
doc_type: system-doc
title: "WLF_EVENT_SOCIAL — Interações Sociais de Eventos (Learning)"
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
  - social-learning
aliases:
  - WLF_EVENT_SOCIAL
  - wlf_event_social
  - wlf-event-social
  - interações-sociais-eventos
  - event-social
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_EVENT_SOCIAL

## Visão Geral

Armazena as **interações sociais** associadas a eventos de aprendizado, como comentários, avaliações (ratings), curtidas e compartilhamentos entre colaboradores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Social learning** — captura interações entre participantes de treinamentos.
- **Avaliações de treinamento** — ratings e feedback dos colaboradores sobre eventos.
- **Engajamento** — mede a participação social nos programas de aprendizado.
- **Curadoria de conteúdo** — identifica conteúdos mais populares via interações sociais.
- **Melhoria contínua** — feedback direto dos participantes sobre a qualidade dos treinamentos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_SOCIAL_ID | NUMBER(18) | NOT NULL | PK | Identificador único da interação social | — | 🟡 75% |
| 2 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado associado | WLF_LEARNING_ITEMS_F | 🟡 75% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que realizou a interação | PER_ALL_PEOPLE_F | 🟢 85% |
| 4 | INTERACTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de interação (comment, rating, like) | — | 🟡 70% |
| 5 | RATING_VALUE | NUMBER(3) | NULL | Dados | Valor da avaliação (1-5) | — | 🟡 65% |
| 6 | COMMENT_TEXT | VARCHAR2(4000) | NULL | Dados | Texto do comentário | — | 🟡 65% |
| 7 | INTERACTION_DATE | DATE | NULL | Data | Data/hora da interação | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa com interaÃ§Ã£o social no aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Avaliações de um evento de aprendizado
```sql
SELECT es.PERSON_ID, es.RATING_VALUE, es.COMMENT_TEXT, es.INTERACTION_DATE
FROM   WLF_EVENT_SOCIAL es
WHERE  es.LEARNING_ITEM_ID = :p_learning_item_id
  AND  es.INTERACTION_TYPE = 'RATING'
ORDER BY es.INTERACTION_DATE DESC;
```

### Filtros comuns
- `INTERACTION_TYPE = 'RATING'` — Apenas avaliações
- `LEARNING_ITEM_ID = :p_item_id` — Interações de um evento específico

---

## Observações

- Tabela transacional — sem sufixo _F (não é date-effective).
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- O campo COMMENT_TEXT pode conter dados não estruturados.
- Confiança geral mais baixa — estrutura inferida por naming conventions.

---

## Referências

- [Oracle Docs — WLF_EVENT_SOCIAL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfeventsocial.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
