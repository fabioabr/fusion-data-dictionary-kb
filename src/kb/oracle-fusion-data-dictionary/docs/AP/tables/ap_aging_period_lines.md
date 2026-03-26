---
id: DOC-AP-002
doc_type: system-doc
title: "AP_AGING_PERIOD_LINES — Linhas de Períodos de Aging de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, aging, period-lines, faixas-aging]
aliases: [AP_AGING_PERIOD_LINES, ap_aging_period_lines, aging_period_lines_ap, linhas_aging_ap, aging_lines_ap]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_AGING_PERIOD_LINES

## Visão Geral

Tabela de linhas individuais que compõem cada período de aging de contas a pagar. Cada registro define uma faixa específica de dias (ex.: 0–30, 31–60) dentro de um conjunto de aging, determinando como os saldos em aberto são distribuídos nos relatórios de envelhecimento.

## Propósito de Negócio

As linhas de período de aging detalham a granularidade de cada faixa de vencimento dentro de um período de aging. São utilizadas para segmentar os passivos com fornecedores em intervalos de dias, permitindo à tesouraria identificar com precisão a concentração de obrigações por faixa temporal e planejar desembolsos de acordo com a política de caixa do Banco Patria.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AGING_PERIOD_LINE_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único da linha de aging. | — | 🟢 95% |
| 2 | AGING_PERIOD_ID | NUMBER(15) | NOT NULL | FK | Referência ao período de aging pai. | [[ap_aging_periods]] | 🟢 95% |
| 3 | PERIOD_SEQUENCE_NUM | NUMBER(5) | NOT NULL | Negócio | Número de sequência da faixa dentro do período. | — | 🟢 90% |
| 4 | DAYS_START | NUMBER(10) | NULL | Negócio | Dia inicial da faixa (ex.: 0, 31, 61). | — | 🟢 90% |
| 5 | DAYS_TO | NUMBER(10) | NULL | Negócio | Dia final da faixa (ex.: 30, 60, 90). | — | 🟢 90% |
| 6 | REPORT_HEADING | VARCHAR2(30) | NULL | Negócio | Cabeçalho exibido no relatório para esta faixa. | — | 🟡 75% |
| 7 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da linha (RANGE, TOTAL, etc.). | — | 🟡 70% |
| 8 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto de flexfield descritivo. | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 10 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_aging_periods]]** — Período de aging ao qual esta linha pertence (via `AGING_PERIOD_ID`).

### Tabelas-filha

- Nenhuma tabela-filha conhecida.

## Uso Típico

```sql
-- Detalhar faixas de um período de aging específico
SELECT apl.PERIOD_SEQUENCE_NUM,
       apl.DAYS_START,
       apl.DAYS_TO,
       apl.REPORT_HEADING
  FROM AP_AGING_PERIOD_LINES apl
  JOIN AP_AGING_PERIODS ap
    ON ap.AGING_PERIOD_ID = apl.AGING_PERIOD_ID
 WHERE ap.PERIOD_NAME = 'Padrão 30/60/90'
 ORDER BY apl.PERIOD_SEQUENCE_NUM;
```

## Observações

- Cada período de aging pode ter múltiplas linhas, definindo faixas consecutivas ou sobrepostas.
- A sequência (`PERIOD_SEQUENCE_NUM`) determina a ordem de exibição no relatório de aging.
- Faixas devem cobrir todo o espectro de dias sem lacunas para relatórios consistentes.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Aging Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
