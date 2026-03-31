---
id: DOC-AP-001
doc_type: system-doc
title: "AP_AGING_PERIODS — Períodos de Aging de Contas a Pagar"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, aging, periods, contas-a-pagar]
aliases: [AP_AGING_PERIODS, ap_aging_periods, aging_periods_ap, periodos_aging_ap, aging_fornecedores]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_AGING_PERIODS

## Visão Geral

Tabela de definição dos períodos de aging (envelhecimento) utilizados para classificar saldos em aberto de contas a pagar por faixa de vencimento. Cada registro representa um conjunto de períodos configuráveis (ex.: corrente, 1–30 dias, 31–60 dias) usado em relatórios de aging de fornecedores e análise de passivos.

## Propósito de Negócio

Os períodos de aging de AP permitem à tesouraria e ao departamento financeiro visualizar a distribuição das obrigações com fornecedores por tempo de vencimento. Isso possibilita o planejamento de fluxo de caixa, a priorização de pagamentos e a negociação de prazos com fornecedores. No Banco Patria, os períodos de aging são fundamentais para gestão de liquidez e compliance regulatório.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AGING_PERIOD_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único do período de aging. | — | 🟢 95% |
| 2 | PERIOD_NAME | VARCHAR2(80) | NOT NULL | Negócio | Nome do período de aging (ex.: "Padrão 30/60/90 dias"). | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Negócio | Descrição textual do período de aging. | — | 🟢 90% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Controle | Status ativo/inativo (A = Ativo, I = Inativo). | — | 🟢 90% |
| 5 | TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do aging (DUE_DATE, INVOICE_DATE, etc.). | — | 🟡 75% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto de flexfield descritivo. | — | 🟢 90% |
| 7 | ATTRIBUTE1 | VARCHAR2(150) | NULL | DFF | Atributo descritivo flexível 1. | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 9 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-filha

- **[[ap_aging_period_lines]]** — Linhas individuais de cada período de aging (1:N via `AGING_PERIOD_ID`).

### Tabelas-pai

- Nenhuma FK direta conhecida. Tabela raiz de configuração.

## Uso Típico

```sql
-- Listar períodos de aging ativos com suas linhas
SELECT ap.PERIOD_NAME,
       apl.PERIOD_SEQUENCE_NUM,
       apl.DAYS_START,
       apl.DAYS_TO
  FROM AP_AGING_PERIODS ap
  JOIN AP_AGING_PERIOD_LINES apl
    ON apl.AGING_PERIOD_ID = ap.AGING_PERIOD_ID
 WHERE ap.STATUS = 'A'
 ORDER BY ap.PERIOD_NAME, apl.PERIOD_SEQUENCE_NUM;
```

## Observações

- Períodos de aging são compartilhados entre business units e tipicamente não possuem `ORG_ID`.
- Alterações nos períodos afetam todos os relatórios de aging de AP que os referenciam.
- Recomenda-se não desativar períodos em uso por relatórios agendados ou processos batch.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle BICC — AP Aging Subject Area Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[agingperiodheaderextractpvo|AgingPeriodHeaderExtractPVO]] (OTHER · BICC: 11/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_ID | ApAgingPeriodsAgingPeriodId | ✅ |
| ATTRIBUTE1 | ApAgingPeriodsAttribute1 | — |
| ATTRIBUTE10 | ApAgingPeriodsAttribute10 | — |
| ATTRIBUTE11 | ApAgingPeriodsAttribute11 | — |
| ATTRIBUTE12 | ApAgingPeriodsAttribute12 | — |
| ATTRIBUTE13 | ApAgingPeriodsAttribute13 | — |
| ATTRIBUTE14 | ApAgingPeriodsAttribute14 | — |
| ATTRIBUTE15 | ApAgingPeriodsAttribute15 | — |
| ATTRIBUTE2 | ApAgingPeriodsAttribute2 | — |
| ATTRIBUTE3 | ApAgingPeriodsAttribute3 | — |
| ATTRIBUTE4 | ApAgingPeriodsAttribute4 | — |
| ATTRIBUTE5 | ApAgingPeriodsAttribute5 | — |
| ATTRIBUTE6 | ApAgingPeriodsAttribute6 | — |
| ATTRIBUTE7 | ApAgingPeriodsAttribute7 | — |
| ATTRIBUTE8 | ApAgingPeriodsAttribute8 | — |
| ATTRIBUTE9 | ApAgingPeriodsAttribute9 | — |
| ATTRIBUTE_CATEGORY | ApAgingPeriodsAttributeCategory | ✅ |
| CREATED_BY | ApAgingPeriodsCreatedBy | ✅ |
| CREATION_DATE | ApAgingPeriodsCreationDate | ✅ |
| DESCRIPTION | ApAgingPeriodsDescription | ✅ |
| LAST_UPDATE_DATE | ApAgingPeriodsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ApAgingPeriodsLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ApAgingPeriodsLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ApAgingPeriodsObjectVersionNumber | ✅ |
| PERIOD_NAME | ApAgingPeriodsPeriodName | ✅ |
| STATUS | ApAgingPeriodsStatus | ✅ |

### [[agingperiodlinepvo|AgingPeriodLinePVO]] (AP · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGING_PERIOD_ID | AgingHeaderAgingPeriodId | — |
| CREATED_BY | AgingHeaderCreatedBy | — |
| CREATION_DATE | AgingHeaderCreationDate | — |
| DESCRIPTION | AgingHeaderDescription | — |
| LAST_UPDATE_DATE | AgingHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AgingHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | AgingHeaderLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AgingHeaderObjectVersionNumber | — |
| PERIOD_NAME | AgingHeaderPeriodName | ✅ |
| STATUS | AgingHeaderStatus | ✅ |
