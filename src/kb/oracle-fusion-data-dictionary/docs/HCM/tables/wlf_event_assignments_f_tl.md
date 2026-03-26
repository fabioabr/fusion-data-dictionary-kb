---
id: DOC-HCM-730
doc_type: system-doc
title: "WLF_EVENT_ASSIGNMENTS_F_TL — Atribuições de Eventos (Traduções)"
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
  - traduções
aliases:
  - WLF_EVENT_ASSIGNMENTS_F_TL
  - wlf_event_assignments_f_tl
  - wlf-event-assignments-f-tl
  - atribuições-eventos-traduções
  - event-assignments-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_EVENT_ASSIGNMENTS_F_TL

## Visão Geral

Armazena as **traduções** das atribuições de eventos de aprendizado, suportando descrições e informações em múltiplos idiomas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — suporta organizações multinacionais com múltiplos idiomas.
- **Interface localizada** — exibe informações de atribuição no idioma do colaborador.
- **Relatórios multilíngues** — permite gerar relatórios em idiomas específicos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da atribuição de evento | WLF_EVENT_ASSIGNMENTS_F | 🟡 80% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: PT, EN, ES) | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 85% |
| 4 | NAME | VARCHAR2(240) | NULL | Identificação | Nome traduzido da atribuição | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_event_assignments_f]] — via `EVENT_ASSIGNMENT_ID` (atribuição de evento)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Traduções de uma atribuição de evento
```sql
SELECT tl.NAME, tl.DESCRIPTION, tl.LANGUAGE
FROM   WLF_EVENT_ASSIGNMENTS_F_TL tl
WHERE  tl.EVENT_ASSIGNMENT_ID = :p_event_assignment_id
ORDER BY tl.LANGUAGE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Filtrar por idioma português
- `EVENT_ASSIGNMENT_ID = :p_id` — Traduções de uma atribuição específica

---

## Observações

- Tabela de tradução (_TL) — PK composta: EVENT_ASSIGNMENT_ID + LANGUAGE.
- SOURCE_LANG indica o idioma original da tradução.
- Faz parte do módulo Workforce Learning (prefixo WLF_).

---

## Referências

- [Oracle Docs — WLF_EVENT_ASSIGNMENTS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfeventassignmentsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
