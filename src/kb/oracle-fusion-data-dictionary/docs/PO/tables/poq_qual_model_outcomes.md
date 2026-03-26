---
id: DOC-PO-050
doc_type: system-doc
title: "POQ_QUAL_MODEL_OUTCOMES — Resultados de Modelos de Qualificação"
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
  - model-outcomes
aliases:
  - POQ_QUAL_MODEL_OUTCOMES
  - poq_qual_model_outcomes
  - resultados-modelo-qualificacao
  - qualification-model-outcomes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_MODEL_OUTCOMES

## 📌 Visão Geral

Armazena os **resultados possíveis (outcomes) a nível de modelo de qualificação**. Define as faixas de pontuação consolidada e suas classificações finais (ex.: "Qualificado", "Não Qualificado", "Qualificação Condicional") que determinam o veredito global da avaliação do fornecedor.

> [!note] Outcomes de modelo vs. de área
> Esta tabela define outcomes a nível de **modelo** (resultado consolidado). Para outcomes a nível de **área** individual, consulte [[poq_qual_area_outcomes]].

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação final:** Determinação do resultado consolidado da qualificação com base na pontuação ponderada de todas as áreas.
- **Regras de qualificação:** Definição das faixas de score que determinam aprovação/reprovação global do fornecedor.
- **Supplier lifecycle:** Alimenta o status de qualificação do fornecedor para controle em processos de sourcing e procurement.
- **Relatórios executivos:** Base para KPIs de taxa de qualificação e distribuição de resultados.
- **Integração com Approved Supplier List (ASL):** Outcome "QUALIFIED" pode disparar inclusão automática na lista de fornecedores aprovados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_MODEL_OUTCOME_ID | NUMBER(18) | NOT NULL | PK | Identificador único do outcome do modelo | — | 🟢 90% |
| 2 | QUAL_MODEL_ID | NUMBER(18) | NOT NULL | FK | Modelo de qualificação | [[poq_qual_models]] | 🟢 95% |
| 3 | OUTCOME_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código do resultado: QUALIFIED, NOT_QUALIFIED, CONDITIONAL, NEEDS_REVIEW | — | 🟡 80% |
| 4 | OUTCOME_NAME | VARCHAR2(240) | NULL | Tradução | Nome do resultado (traduzido) | — | 🟡 75% |
| 5 | MIN_SCORE | NUMBER | NULL | Pontuação | Pontuação mínima para atingir este outcome | — | 🟡 80% |
| 6 | MAX_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima desta faixa de outcome | — | 🟡 80% |
| 7 | SEQUENCE_NUMBER | NUMBER | NULL | Identificação | Ordem de exibição/avaliação do outcome | — | 🟡 70% |
| 8 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Classificação | Se este é o outcome padrão (fallback): Y/N | — | 🟡 65% |
| 9 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição do outcome e critérios de aplicação | — | 🟡 75% |
| 10 | ACTION_CODE | VARCHAR2(30) | NULL | Classificação | Ação automática associada: APPROVE_SUPPLIER, BLOCK_SUPPLIER, NOTIFY_OWNER | — | 🟡 60% |
| 11 | NOTIFICATION_FLAG | VARCHAR2(1) | NULL | Classificação | Se dispara notificação automática: Y/N | — | 🟡 60% |
| 12 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Se o outcome está ativo: Y/N | — | 🟡 80% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 18 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_qual_models]] — via `QUAL_MODEL_ID` (modelo de qualificação)

### Tabelas relacionadas
- [[poq_qual_asmt_init_v]] — view de avaliações que utiliza o `OUTCOME_CODE` definido aqui (avaliações que resultaram neste outcome)

---

## 📎 Uso Típico

### Faixas de resultado de um modelo
```sql
SELECT mo.OUTCOME_CODE, mo.OUTCOME_NAME,
       mo.MIN_SCORE, mo.MAX_SCORE, mo.DESCRIPTION,
       mo.ACTION_CODE
FROM   POQ_QUAL_MODEL_OUTCOMES mo
WHERE  mo.QUAL_MODEL_ID = :p_model_id
  AND  mo.ENABLED_FLAG = 'Y'
ORDER  BY mo.MIN_SCORE;
```

### Modelos com outcome de aprovação e seu score mínimo
```sql
SELECT qm.QUAL_MODEL_NAME, mo.MIN_SCORE AS score_minimo_aprovacao
FROM   POQ_QUAL_MODEL_OUTCOMES mo
JOIN   POQ_QUAL_MODELS qm ON qm.QUAL_MODEL_ID = mo.QUAL_MODEL_ID
WHERE  mo.OUTCOME_CODE = 'QUALIFIED'
  AND  mo.ENABLED_FLAG = 'Y'
  AND  qm.STATUS_CODE = 'ACTIVE';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Outcomes ativos
- `OUTCOME_CODE = 'QUALIFIED'` — Faixa de aprovação
- `OUTCOME_CODE = 'NOT_QUALIFIED'` — Faixa de reprovação
- `DEFAULT_FLAG = 'Y'` — Outcome fallback

---

## 🔒 Observações

- As faixas de `MIN_SCORE` e `MAX_SCORE` não devem se sobrepor dentro de um mesmo modelo.
- O `ACTION_CODE` permite automação: por exemplo, outcome `NOT_QUALIFIED` pode disparar bloqueio automático do fornecedor.
- O outcome com `DEFAULT_FLAG = 'Y'` é aplicado quando o score não se encaixa em nenhuma faixa explícita (edge case / fallback).
- Cada modelo deve ter pelo menos os outcomes QUALIFIED e NOT_QUALIFIED configurados para funcionar corretamente.
- O `OUTCOME_CODE` definido aqui é o mesmo valor gravado no campo `OUTCOME_CODE` da view [[poq_qual_asmt_init_v]].

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
