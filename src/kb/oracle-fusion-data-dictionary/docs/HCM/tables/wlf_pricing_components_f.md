---
id: DOC-HCM-745
doc_type: system-doc
title: "WLF_PRICING_COMPONENTS_F — Componentes de Precificação (Learning)"
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
  - precificação
aliases:
  - WLF_PRICING_COMPONENTS_F
  - wlf_pricing_components_f
  - wlf-pricing-components-f
  - componentes-precificação-learning
  - pricing-components
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_PRICING_COMPONENTS_F

## Visão Geral

Armazena os **componentes de precificação** dos itens de aprendizado, detalhando os custos individuais que compõem o preço total de um treinamento. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Precificação de treinamentos** — detalha os componentes de custo (instrutor, material, sala).
- **Orçamento de capacitação** — base para planejamento orçamentário de treinamentos.
- **Cobrança interna** — suporta rateio de custos entre departamentos.
- **Análise de ROI** — permite calcular custo total por participante.
- **Gestão financeira** — controle de despesas com desenvolvimento de pessoas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PRICING_COMPONENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do componente | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado associado | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 5 | COMPONENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do componente (instructor, material, venue) | — | 🟡 70% |
| 6 | AMOUNT | NUMBER(15,2) | NULL | Financeiro | Valor do componente | — | 🟡 75% |
| 7 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 75% |
| 8 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição do componente de custo | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Composição de custo de um treinamento
```sql
SELECT pc.COMPONENT_TYPE, pc.AMOUNT, pc.CURRENCY_CODE, pc.DESCRIPTION
FROM   WLF_PRICING_COMPONENTS_F pc
WHERE  pc.LEARNING_ITEM_ID = :p_learning_item_id
  AND  SYSDATE BETWEEN pc.EFFECTIVE_START_DATE AND pc.EFFECTIVE_END_DATE
ORDER BY pc.COMPONENT_TYPE;
```

### Filtros comuns
- `LEARNING_ITEM_ID = :p_item_id` — Componentes de um item
- `COMPONENT_TYPE = 'INSTRUCTOR'` — Custos de instrutor

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Cada item pode ter múltiplos componentes de custo.
- O custo total é a soma de todos os componentes ativos.

---

## Referências

- [Oracle Docs — WLF_PRICING_COMPONENTS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfpricingcomponentsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
