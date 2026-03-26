---
id: DOC-HCM-738
doc_type: system-doc
title: "WLF_LI_CLASSES_F — Turmas de Itens de Aprendizado"
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
  - turmas
aliases:
  - WLF_LI_CLASSES_F
  - wlf_li_classes_f
  - wlf-li-classes-f
  - turmas-itens-aprendizado
  - li-classes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LI_CLASSES_F

## Visão Geral

Armazena as **turmas (classes/ofertas)** de itens de aprendizado, representando instâncias específicas de cursos com datas, horários, locais e instrutores. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de turmas** — define turmas com datas, horários e capacidade.
- **Programação de treinamentos** — agenda de cursos presenciais e virtuais.
- **Controle de vagas** — gerencia inscrições e lista de espera.
- **Logística de treinamento** — associa local, instrutor e recursos à turma.
- **Relatórios de execução** — acompanhamento de turmas realizadas vs. planejadas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LI_CLASS_ID | NUMBER(18) | NOT NULL | PK | Identificador único da turma | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado pai | WLF_LEARNING_ITEMS_F | 🟢 85% |
| 5 | CLASS_NUMBER | VARCHAR2(30) | NULL | Identificação | Número/código da turma | — | 🟡 75% |
| 6 | CLASS_STATUS | VARCHAR2(30) | NULL | Status | Status da turma (scheduled, in-progress, completed) | — | 🟡 75% |
| 7 | START_DATE | DATE | NULL | Data | Data de início da turma | — | 🟡 80% |
| 8 | END_DATE | DATE | NULL | Data | Data de término da turma | — | 🟡 80% |
| 9 | MAX_ENROLLMENT | NUMBER(9) | NULL | Dados | Capacidade máxima de inscrições | — | 🟡 70% |
| 10 | LOCATION_ID | NUMBER(18) | NULL | FK | Local do treinamento | — | 🟡 70% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Turmas agendadas de um curso
```sql
SELECT lc.CLASS_NUMBER, lc.CLASS_STATUS, lc.START_DATE, lc.END_DATE, lc.MAX_ENROLLMENT
FROM   WLF_LI_CLASSES_F lc
WHERE  lc.LEARNING_ITEM_ID = :p_learning_item_id
  AND  lc.CLASS_STATUS = 'SCHEDULED'
  AND  SYSDATE BETWEEN lc.EFFECTIVE_START_DATE AND lc.EFFECTIVE_END_DATE
ORDER BY lc.START_DATE;
```

### Filtros comuns
- `LEARNING_ITEM_ID = :p_item_id` — Turmas de um curso específico
- `CLASS_STATUS = 'SCHEDULED'` — Apenas turmas agendadas

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Cada item de aprendizado pode ter múltiplas turmas ao longo do tempo.
- LI = Learning Item.

---

## Referências

- [Oracle Docs — WLF_LI_CLASSES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfliclassesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
