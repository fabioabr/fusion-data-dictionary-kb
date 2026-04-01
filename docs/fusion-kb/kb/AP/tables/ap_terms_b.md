---
id: DOC-AP-027
doc_type: system-doc
title: "AP_TERMS_B — Condições de Pagamento (Base)"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, condicoes-pagamento, payment-terms, setup]
aliases: [AP_TERMS_B, ap_terms_b, payment_terms_base, condicoes_pagamento_base, termos_pagamento]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_TERMS_B

## Visão Geral

Tabela base (language-independent) de condições de pagamento do Oracle Fusion. Armazena os atributos estruturais das condições de pagamento: tipo de vencimento, descontos, datas fixas e demais regras que determinam quando e como uma fatura deve ser paga. Segue o padrão Oracle MLS (Multi-Language Support) com tabelas `_B` (base), `_TL` (tradução) e `_VL` (view).

## Propósito de Negócio

Define as condições comerciais de prazo e desconto aplicadas a faturas de fornecedores. É essencial para: (1) cálculo automático de datas de vencimento, (2) gestão de descontos por antecipação, (3) planejamento de fluxo de caixa, (4) padronização de termos comerciais entre business units, (5) integração com processos de pagamento e aprovação.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(15) | NOT NULL | PK | Chave primária. Identificador único da condição de pagamento. | — | 🟢 100% |
| 2 | NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome técnico da condição de pagamento (ex.: NET30, 2/10NET30). | — | 🟢 100% |
| 3 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se a condição está ativa (Y/N). | — | 🟢 100% |
| 4 | START_DATE_ACTIVE | DATE | NULL | Temporal | Data de início da vigência. | — | 🟢 95% |
| 5 | END_DATE_ACTIVE | DATE | NULL | Temporal | Data de fim da vigência (NULL = sem expiração). | — | 🟢 95% |
| 6 | DUE_CUTOFF_DAY | NUMBER | NULL | Regra | Dia de corte para cálculo de vencimento. | — | 🟢 90% |
| 7 | RANK | NUMBER | NULL | Classificação | Prioridade da condição (para seleção automática). | — | 🟡 70% |
| 8 | TYPE | VARCHAR2(25) | NULL | Classificação | Tipo da condição (ex.: STANDARD, PREPAYMENT). | — | 🟡 75% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2(150) | NULL | DFF | Contexto de flexfield descritivo. | — | 🟢 90% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- Nenhuma tabela-pai direta (tabela raiz de configuração).

### Tabelas-filha

- **[[ap_terms_lines]]** — Linhas de parcelas/descontos da condição (1:N via `TERM_ID`).
- **[[ap_terms_tl]]** — Traduções do nome/descrição (1:N via `TERM_ID`).
- **[[ap_invoices_all]]** — Faturas que utilizam esta condição (1:N via `TERMS_ID`).
- **[[ap_system_parameters_all]]** — Configuração de sistema com condição padrão (1:N via `TERMS_ID`).

## Uso Típico

```sql
-- Listar condições de pagamento ativas com suas linhas
SELECT tb.TERM_ID,
       tb.NAME,
       tl.DESCRIPTION,
       tln.SEQUENCE_NUM,
       tln.DUE_DAYS,
       tln.DUE_PERCENT,
       tln.DISCOUNT_PERCENT
  FROM AP_TERMS_B tb
  JOIN AP_TERMS_TL tl
    ON tl.TERM_ID = tb.TERM_ID AND tl.LANGUAGE = 'PTB'
  JOIN AP_TERMS_LINES tln
    ON tln.TERM_ID = tb.TERM_ID
 WHERE tb.ENABLED_FLAG = 'Y'
   AND NVL(tb.END_DATE_ACTIVE, SYSDATE + 1) > SYSDATE
 ORDER BY tb.NAME, tln.SEQUENCE_NUM;
```

## Observações

- Tabela base do padrão MLS Oracle: dados não traduzíveis ficam em `_B`, nomes/descrições traduzidos em [[ap_terms_tl]], e a view consolidada em [[ap_terms_vl]].
- Cada condição possui ao menos uma linha em [[ap_terms_lines]] definindo parcelas, prazos e percentuais de desconto.
- Condições de pagamento são compartilhadas entre AP e AR (embora AR use `RA_TERMS_B`/[[ra_terms_b]] em implementações distintas).
- O campo `ENABLED_FLAG` e as datas de vigência controlam a disponibilidade para novas faturas.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Payment Terms Setup Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[paymenttermheaderbpvo|PaymentTermHeaderBPVO]] (AP · BICC: 7/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DUE_CUTOFF_DAY | DueCutoffDay | ✅ |
| ENABLED_FLAG | EnabledFlag | — |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| RANK | Rank | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |
| TERM_ID | TermId | ✅ |
| TYPE | Type | ✅ |

### [[paymenttermheaderextractpvo|PaymentTermHeaderExtractPVO]] (OTHER · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PaymentTermHeaderBPEOAttribute1 | — |
| ATTRIBUTE10 | PaymentTermHeaderBPEOAttribute10 | — |
| ATTRIBUTE11 | PaymentTermHeaderBPEOAttribute11 | — |
| ATTRIBUTE12 | PaymentTermHeaderBPEOAttribute12 | — |
| ATTRIBUTE13 | PaymentTermHeaderBPEOAttribute13 | — |
| ATTRIBUTE14 | PaymentTermHeaderBPEOAttribute14 | — |
| ATTRIBUTE15 | PaymentTermHeaderBPEOAttribute15 | — |
| ATTRIBUTE2 | PaymentTermHeaderBPEOAttribute2 | — |
| ATTRIBUTE3 | PaymentTermHeaderBPEOAttribute3 | — |
| ATTRIBUTE4 | PaymentTermHeaderBPEOAttribute4 | — |
| ATTRIBUTE5 | PaymentTermHeaderBPEOAttribute5 | — |
| ATTRIBUTE6 | PaymentTermHeaderBPEOAttribute6 | — |
| ATTRIBUTE7 | PaymentTermHeaderBPEOAttribute7 | — |
| ATTRIBUTE8 | PaymentTermHeaderBPEOAttribute8 | — |
| ATTRIBUTE9 | PaymentTermHeaderBPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PaymentTermHeaderBPEOAttributeCategory | — |
| CREATED_BY | PaymentTermHeaderBPEOCreatedBy | ✅ |
| CREATION_DATE | PaymentTermHeaderBPEOCreationDate | ✅ |
| DUE_CUTOFF_DAY | PaymentTermHeaderBPEODueCutoffDay | ✅ |
| ENABLED_FLAG | PaymentTermHeaderBPEOEnabledFlag | ✅ |
| END_DATE_ACTIVE | PaymentTermHeaderBPEOEndDateActive | ✅ |
| LAST_UPDATE_DATE | PaymentTermHeaderBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentTermHeaderBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PaymentTermHeaderBPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PaymentTermHeaderBPEOObjectVersionNumber | ✅ |
| RANK | PaymentTermHeaderBPEORank | ✅ |
| START_DATE_ACTIVE | PaymentTermHeaderBPEOStartDateActive | ✅ |
| TERM_ID | PaymentTermHeaderBPEOTermId | ✅ |
| TYPE | PaymentTermHeaderBPEOType | ✅ |
