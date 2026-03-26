---
id: DOC-PO-045
doc_type: system-doc
title: "POQ_QUAL_AREA_OUTCOMES — Resultados de Áreas de Qualificação"
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
  - outcomes
  - area-outcomes
aliases:
  - POQ_QUAL_AREA_OUTCOMES
  - poq_qual_area_outcomes
  - resultados-area-qualificacao
  - qualification-area-outcomes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_AREA_OUTCOMES

## 📌 Visão Geral

Armazena os **resultados possíveis (outcomes) para cada área de qualificação** de fornecedores. Define as faixas de pontuação e suas classificações (ex.: "Aprovado", "Reprovado", "Condicional") a nível de área individual, permitindo granularidade fina na avaliação.

> [!note] Outcomes vs. Model Outcomes
> Esta tabela define outcomes a nível de **área**. Para outcomes a nível de **modelo** (resultado consolidado), consulte [[poq_qual_model_outcomes]].

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação automática:** Determinação do resultado da área com base na pontuação obtida pelo fornecedor.
- **Regras de qualificação:** Definição de faixas de score que determinam aprovação/reprovação por área.
- **Dashboards de qualificação:** Exibição do resultado por área nos painéis de avaliação de fornecedores.
- **Configuração de modelos:** Parametrização dos critérios de aceitação por área de qualificação.
- **Auditoria:** Rastreamento dos critérios de avaliação vigentes em cada período.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUAL_AREA_OUTCOME_ID | NUMBER(18) | NOT NULL | PK | Identificador único do outcome da área | — | 🟢 90% |
| 2 | QUAL_AREA_ID | NUMBER(18) | NOT NULL | FK | Área de qualificação à qual o outcome pertence | [[poq_qual_areas_vl]] | 🟢 90% |
| 3 | OUTCOME_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código do resultado: QUALIFIED, NOT_QUALIFIED, CONDITIONAL, NEEDS_REVIEW | — | 🟡 80% |
| 4 | OUTCOME_NAME | VARCHAR2(240) | NULL | Tradução | Nome do resultado (traduzido) | — | 🟡 75% |
| 5 | MIN_SCORE | NUMBER | NULL | Pontuação | Pontuação mínima para atingir este outcome | — | 🟡 80% |
| 6 | MAX_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima desta faixa de outcome | — | 🟡 80% |
| 7 | SEQUENCE_NUMBER | NUMBER | NULL | Identificação | Ordem de exibição do outcome | — | 🟡 70% |
| 8 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Classificação | Se este é o outcome padrão: Y/N | — | 🟡 65% |
| 9 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição do outcome e critérios de aplicação | — | 🟡 75% |
| 10 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Se o outcome está ativo: Y/N | — | 🟡 80% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_qual_areas_vl]] — via `QUAL_AREA_ID` (área de qualificação)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Faixas de resultado de uma área
```sql
SELECT ao.OUTCOME_CODE, ao.OUTCOME_NAME,
       ao.MIN_SCORE, ao.MAX_SCORE, ao.DESCRIPTION
FROM   POQ_QUAL_AREA_OUTCOMES ao
WHERE  ao.QUAL_AREA_ID = :p_qual_area_id
  AND  ao.ENABLED_FLAG = 'Y'
ORDER  BY ao.MIN_SCORE;
```

### Áreas com outcomes não configurados
```sql
SELECT qa.QUAL_AREA_NAME
FROM   POQ_QUAL_AREAS_VL qa
WHERE  NOT EXISTS (
    SELECT 1 FROM POQ_QUAL_AREA_OUTCOMES ao
    WHERE  ao.QUAL_AREA_ID = qa.QUAL_AREA_ID
      AND  ao.ENABLED_FLAG = 'Y'
);
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Outcomes ativos
- `OUTCOME_CODE = 'QUALIFIED'` — Resultado de aprovação
- `DEFAULT_FLAG = 'Y'` — Outcome padrão

---

## 🔒 Observações

- As faixas de `MIN_SCORE` e `MAX_SCORE` não devem se sobrepor dentro de uma mesma área.
- O `OUTCOME_CODE` é usado programaticamente; o `OUTCOME_NAME` é exibido na interface.
- Cada área deve ter pelo menos um outcome configurado para funcionar no fluxo de qualificação.
- Outcomes a nível de área alimentam o cálculo do outcome consolidado a nível de modelo ([[poq_qual_model_outcomes]]).

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
