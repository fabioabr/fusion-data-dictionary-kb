---
id: DOC-PO-047
doc_type: system-doc
title: "POQ_QUAL_ASMT_INIT_V — Avaliações por Iniciativa de Qualificação (View)"
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
  - assessments
  - view-consolidada
aliases:
  - POQ_QUAL_ASMT_INIT_V
  - poq_qual_asmt_init_v
  - avaliacoes-iniciativa-qualificacao
  - qualification-assessment-initiative-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_ASMT_INIT_V

## 📌 Visão Geral

View consolidada que apresenta as **avaliações (assessments) realizadas no contexto de iniciativas de qualificação**. Combina dados de iniciativas, fornecedores, modelos e resultados em uma única consulta otimizada para relatórios e dashboards de Supplier Qualification Management.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view de consulta** (read-only) que consolida múltiplas tabelas do submódulo SQM.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Dashboard de qualificação:** Visão consolidada do status de todas as avaliações por iniciativa.
- **Relatórios gerenciais:** Análise de resultados de qualificação com cruzamento de dados de fornecedores, modelos e iniciativas.
- **Acompanhamento de progresso:** Monitoramento de quantos fornecedores já foram avaliados em cada iniciativa.
- **Análise de tendências:** Comparação de resultados entre iniciativas ao longo do tempo.
- **Exportação de dados:** Base para extração de dados de qualificação para BI/Analytics.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSESSMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da avaliação | — | 🟢 90% |
| 2 | INITIATIVE_ID | NUMBER(18) | NOT NULL | FK | Iniciativa de qualificação | [[poq_initiatives]] | 🟢 90% |
| 3 | INITIATIVE_NAME | VARCHAR2(240) | NULL | Denormalizado | Nome da iniciativa (denormalizado na view) | — | 🟡 80% |
| 4 | SUPPLIER_ID | NUMBER(18) | NOT NULL | FK | Fornecedor avaliado | [[poz_suppliers]] | 🟢 90% |
| 5 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Denormalizado | Nome do fornecedor (denormalizado) | — | 🟡 80% |
| 6 | QUAL_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de qualificação utilizado | [[poq_qual_models]] | 🟡 80% |
| 7 | QUAL_MODEL_NAME | VARCHAR2(240) | NULL | Denormalizado | Nome do modelo de qualificação | — | 🟡 75% |
| 8 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status da avaliação: PENDING, IN_PROGRESS, COMPLETED, EXPIRED | — | 🟢 90% |
| 9 | OVERALL_SCORE | NUMBER | NULL | Pontuação | Pontuação consolidada da avaliação | — | 🟡 80% |
| 10 | OUTCOME_CODE | VARCHAR2(30) | NULL | Classificação | Resultado final: QUALIFIED, NOT_QUALIFIED, CONDITIONAL | — | 🟡 80% |
| 11 | ASSESSMENT_DATE | DATE | NULL | Data | Data de realização da avaliação | — | 🟡 80% |
| 12 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da qualificação | — | 🟡 75% |
| 13 | EVALUATOR_ID | NUMBER(18) | NULL | Referência | Usuário que realizou a avaliação | — | 🟡 70% |
| 14 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários da avaliação | — | 🟡 75% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas/Views de origem
- [[poq_initiatives]] — via `INITIATIVE_ID` (iniciativa de qualificação da avaliação)
- [[poq_initiative_suppliers]] — via `INITIATIVE_ID` + `SUPPLIER_ID` (participação do fornecedor na iniciativa)
- [[poq_qual_models]] — via `QUAL_MODEL_ID` (modelo de qualificação)
- [[poz_suppliers]] — via `SUPPLIER_ID` (fornecedor da view de avaliação de qualificação)

### Tabelas/Views relacionadas
- [[poq_qual_model_outcomes]] — outcomes do modelo para interpretação do `OUTCOME_CODE` (resultado do modelo de qualificação do fornecedor)

---

## 📎 Uso Típico

### Resultados de uma iniciativa
```sql
SELECT v.SUPPLIER_NAME, v.OVERALL_SCORE, v.OUTCOME_CODE,
       v.STATUS_CODE, v.ASSESSMENT_DATE
FROM   POQ_QUAL_ASMT_INIT_V v
WHERE  v.INITIATIVE_ID = :p_initiative_id
  AND  v.STATUS_CODE = 'COMPLETED'
ORDER  BY v.OVERALL_SCORE DESC;
```

### Taxa de qualificação por iniciativa
```sql
SELECT v.INITIATIVE_NAME,
       COUNT(*) AS total_avaliacoes,
       SUM(CASE WHEN v.OUTCOME_CODE = 'QUALIFIED' THEN 1 ELSE 0 END) AS qualificados,
       ROUND(SUM(CASE WHEN v.OUTCOME_CODE = 'QUALIFIED' THEN 1 ELSE 0 END) * 100.0
             / COUNT(*), 1) AS pct_qualificados
FROM   POQ_QUAL_ASMT_INIT_V v
WHERE  v.STATUS_CODE = 'COMPLETED'
GROUP  BY v.INITIATIVE_NAME;
```

### Filtros comuns
- `STATUS_CODE = 'COMPLETED'` — Avaliações concluídas
- `OUTCOME_CODE = 'QUALIFIED'` — Fornecedores aprovados
- `OUTCOME_CODE = 'NOT_QUALIFIED'` — Fornecedores reprovados
- `EXPIRATION_DATE < SYSDATE` — Qualificações expiradas

---

## 🔒 Observações

- Por ser uma view (`_V`), **não suporta operações DML** (INSERT/UPDATE/DELETE).
- Campos denormalizados (nomes de fornecedor, iniciativa, modelo) evitam JOINs adicionais em relatórios.
- O `OVERALL_SCORE` é calculado a partir das pontuações das áreas individuais conforme pesos definidos no modelo.
- O `EXPIRATION_DATE` indica quando a qualificação do fornecedor precisa ser renovada.
- Avaliações com `STATUS_CODE = 'EXPIRED'` indicam que o prazo de qualificação venceu sem renovação.

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
