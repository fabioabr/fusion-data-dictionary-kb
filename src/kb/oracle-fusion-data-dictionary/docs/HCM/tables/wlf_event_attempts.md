---
id: DOC-HCM-731
doc_type: system-doc
title: "WLF_EVENT_ATTEMPTS — Tentativas de Eventos (Learning)"
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
  - tentativas-eventos
aliases:
  - WLF_EVENT_ATTEMPTS
  - wlf_event_attempts
  - wlf-event-attempts
  - tentativas-de-eventos
  - event-attempts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_EVENT_ATTEMPTS

## Visão Geral

Armazena as **tentativas de conclusão** de eventos de aprendizado, registrando cada tentativa de um colaborador para completar uma atividade (ex.: quiz, avaliação).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Tracking de tentativas** — registra quantas vezes um colaborador tentou concluir uma atividade.
- **Avaliação de desempenho** — armazena notas/scores de cada tentativa.
- **Políticas de re-tentativa** — suporta regras de limite máximo de tentativas.
- **Relatórios de eficácia** — análise de taxa de aprovação por tentativa.
- **Análise de dificuldade** — identifica atividades com alta taxa de reprovação.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_ATTEMPT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tentativa | — | 🟡 80% |
| 2 | EVENT_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuição de evento associada | WLF_EVENT_ASSIGNMENTS_F | 🟡 80% |
| 3 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa que realizou a tentativa | PER_ALL_PEOPLE_F | 🟢 85% |
| 4 | ATTEMPT_NUMBER | NUMBER(5) | NULL | Dados | Número sequencial da tentativa | — | 🟡 75% |
| 5 | ATTEMPT_DATE | DATE | NULL | Data | Data/hora da tentativa | — | 🟡 80% |
| 6 | SCORE | NUMBER(5,2) | NULL | Dados | Nota/pontuação obtida | — | 🟡 75% |
| 7 | RESULT_STATUS | VARCHAR2(30) | NULL | Status | Resultado (passed, failed, incomplete) | — | 🟡 75% |
| 8 | DURATION_MINUTES | NUMBER(10) | NULL | Dados | Duração da tentativa em minutos | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_event_assignments_f]] — via `EVENT_ASSIGNMENT_ID` (atribuição de evento)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa que tentou o evento de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Tentativas de um colaborador em um evento
```sql
SELECT ea.ATTEMPT_NUMBER, ea.ATTEMPT_DATE, ea.SCORE, ea.RESULT_STATUS
FROM   WLF_EVENT_ATTEMPTS ea
WHERE  ea.EVENT_ASSIGNMENT_ID = :p_event_assignment_id
ORDER BY ea.ATTEMPT_NUMBER;
```

### Filtros comuns
- `EVENT_ASSIGNMENT_ID = :p_id` — Tentativas de uma atribuição
- `RESULT_STATUS = 'PASSED'` — Apenas tentativas aprovadas

---

## Observações

- Cada registro representa uma tentativa individual de conclusão.
- Um colaborador pode ter múltiplas tentativas para o mesmo evento.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Sem sufixo _F — tabela transacional, não date-effective.

---

## Referências

- [Oracle Docs — WLF_EVENT_ATTEMPTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfeventattempts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
