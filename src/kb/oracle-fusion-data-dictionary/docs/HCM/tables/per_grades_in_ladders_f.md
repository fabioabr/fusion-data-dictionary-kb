---
id: DOC-HCM-661
doc_type: system-doc
title: "PER_GRADES_IN_LADDERS_F — Grades em Escadas Salariais"
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
  - compensation
  - grades
  - grade-ladders
aliases:
  - PER_GRADES_IN_LADDERS_F
  - per_grades_in_ladders_f
  - per-grades-in-ladders-f
  - grades-em-escadas-salariais
  - per-grades-in-ladder
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADES_IN_LADDERS_F

## 📌 Visão Geral

Armazena a **associação entre grades e escadas (ladders) salariais**, com vigência temporal. Define quais grades compõem cada escada e sua ordem de progressão.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de carreira** — define a sequência de grades em cada trilha de carreira.
- **Progressão salarial** — determina o caminho de evolução dentro de uma escada.
- **Políticas de promoção** — referência para movimentações entre grades.
- **Relatórios** — análise da distribuição de colaboradores por posição na escada.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_LADDER_GRADE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação | — | 🟢 90% |
| 2 | GRADE_LADDER_ID | NUMBER(18) | NOT NULL | FK | Escada salarial | PER_GRADE_LADDERS_F | 🟢 90% |
| 3 | GRADE_ID | NUMBER(18) | NOT NULL | FK | Grade | PER_GRADES_F | 🟢 90% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 6 | SEQUENCE | NUMBER | NULL | Configuração | Ordem da grade na escada | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_grade_ladders_f]] — via `GRADE_LADDER_ID` (escada salarial)
- [[per_grades_f]] — via `GRADE_ID` (grade salarial na escala hierÃ¡rquica)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta — tabela de associação.

---

## 📎 Uso Típico

### Grades em uma escada salarial
```sql
SELECT pgil.GRADE_ID, pgil.SEQUENCE
FROM   PER_GRADES_IN_LADDERS_F pgil
WHERE  pgil.GRADE_LADDER_ID = :p_ladder_id
  AND  SYSDATE BETWEEN pgil.EFFECTIVE_START_DATE AND pgil.EFFECTIVE_END_DATE
ORDER BY pgil.SEQUENCE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Associações vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- A `SEQUENCE` define a ordem de progressão — menor número = grade mais baixa.
- Uma grade pode pertencer a múltiplas escadas.
---

## 📚 Referências

- [Oracle Docs — PER_GRADES_IN_LADDERS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradesinladdersf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
