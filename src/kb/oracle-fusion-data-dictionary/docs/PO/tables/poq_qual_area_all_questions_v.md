---
id: DOC-PO-044
doc_type: system-doc
title: "POQ_QUAL_AREA_ALL_QUESTIONS_V — Todas as Perguntas por Área de Qualificação (View)"
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
  - qualificacao
  - supplier-qualification
  - questions
  - view-consolidada
aliases:
  - POQ_QUAL_AREA_ALL_QUESTIONS_V
  - poq_qual_area_all_questions_v
  - perguntas-area-qualificacao-view
  - qualification-area-questions-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_AREA_ALL_QUESTIONS_V

## 📌 Visão Geral

View consolidada que apresenta **todas as perguntas associadas a cada área de qualificação**, incluindo textos traduzidos, tipo de resposta e metadados de pontuação. Agrega dados das tabelas de perguntas, áreas e traduções em uma única consulta otimizada para relatórios e interfaces.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view de consulta** (read-only) que consolida múltiplas tabelas do submódulo de Supplier Qualification Management.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Montagem de questionários:** Apresentação de todas as perguntas de uma área para composição de questionários de avaliação.
- **Relatórios de qualificação:** Consulta consolidada das perguntas com seus textos traduzidos.
- **Análise de cobertura:** Verificação de quais áreas possuem perguntas definidas e quantas.
- **Configuração de modelos:** Apoio na revisão de perguntas ao montar modelos de qualificação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_AREA_ID | NUMBER(18) | NOT NULL | FK | Área de qualificação | [[poq_qual_areas_vl]] | 🟢 90% |
| 2 | QUESTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pergunta | [[poq_qual_area_questions]] | 🟢 90% |
| 3 | QUAL_AREA_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome da área de qualificação (traduzido) | — | 🟡 80% |
| 4 | QUESTION_TEXT | VARCHAR2(4000) | NOT NULL | Tradução | Texto da pergunta (traduzido) | — | 🟢 90% |
| 5 | QUESTION_NUMBER | NUMBER | NULL | Identificação | Número sequencial da pergunta na área | — | 🟡 75% |
| 6 | RESPONSE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de resposta esperada: TEXT, NUMBER, DATE, SINGLE_CHOICE, MULTI_CHOICE, ATTACHMENT | — | 🟡 80% |
| 7 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Classificação | Se a pergunta é obrigatória: Y/N | — | 🟡 75% |
| 8 | SCORING_FLAG | VARCHAR2(1) | NULL | Classificação | Se a pergunta contribui para a pontuação: Y/N | — | 🟡 70% |
| 9 | MAX_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima da pergunta | — | 🟡 70% |
| 10 | WEIGHT | NUMBER | NULL | Pontuação | Peso da pergunta na área | — | 🟡 65% |
| 11 | HELP_TEXT | VARCHAR2(4000) | NULL | Tradução | Texto de ajuda/orientação para o respondente | — | 🟡 65% |
| 12 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Se a pergunta está ativa: Y/N | — | 🟡 80% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas/Views de origem
- [[poq_qual_areas_vl]] — via `QUAL_AREA_ID` (área de qualificação)
- [[poq_qual_area_questions]] — via `QUESTION_ID` (perguntas base da área de qualificação)

### Tabelas/Views relacionadas
- [[poq_qual_area_outcomes]] — via `QUAL_AREA_ID` (resultados possíveis da área)
- [[poq_qual_model_areas]] — via `QUAL_AREA_ID` (associação área-modelo)

---

## 📎 Uso Típico

### Todas as perguntas de uma área de qualificação
```sql
SELECT q.QUESTION_NUMBER, q.QUESTION_TEXT, q.RESPONSE_TYPE,
       q.MANDATORY_FLAG, q.MAX_SCORE, q.WEIGHT
FROM   POQ_QUAL_AREA_ALL_QUESTIONS_V q
WHERE  q.QUAL_AREA_ID = :p_qual_area_id
  AND  q.ENABLED_FLAG = 'Y'
ORDER  BY q.QUESTION_NUMBER;
```

### Contagem de perguntas por área
```sql
SELECT q.QUAL_AREA_NAME, COUNT(*) AS qtd_perguntas,
       SUM(CASE WHEN q.MANDATORY_FLAG = 'Y' THEN 1 ELSE 0 END) AS qtd_obrigatorias
FROM   POQ_QUAL_AREA_ALL_QUESTIONS_V q
WHERE  q.ENABLED_FLAG = 'Y'
GROUP  BY q.QUAL_AREA_NAME;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Perguntas ativas
- `MANDATORY_FLAG = 'Y'` — Perguntas obrigatórias
- `SCORING_FLAG = 'Y'` — Perguntas com pontuação

---

## 🔒 Observações

- Por ser uma view (`_V`), **não suporta operações DML** (INSERT/UPDATE/DELETE).
- A view já inclui as traduções no idioma da sessão, evitando JOINs adicionais com tabelas `_TL`.
- O campo `RESPONSE_TYPE` determina como a interface renderiza o campo de resposta no questionário do fornecedor.
- Perguntas com `SCORING_FLAG = 'N'` são informativas (não afetam a pontuação final da área).

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
