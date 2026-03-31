---
id: DOC-AP-029
doc_type: system-doc
title: "AP_TERMS_TL — Traduções das Condições de Pagamento"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-payable, data-dictionary, condicoes-pagamento, traducoes, mls]
aliases: [AP_TERMS_TL, ap_terms_tl, payment_terms_translation, traducao_condicoes_pagamento, terms_language]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AP_TERMS_TL

## Visão Geral

Tabela de traduções (Translation Layer) das condições de pagamento definidas em [[ap_terms_b]]. Segue o padrão Oracle MLS (Multi-Language Support), armazenando nome e descrição traduzidos para cada idioma instalado. Cada registro combina o `TERM_ID` com um código de idioma (`LANGUAGE`).

## Propósito de Negócio

Permite que as condições de pagamento sejam exibidas no idioma do usuário logado, sem duplicar os atributos estruturais da tabela base. É essencial para: (1) exibição de nomes traduzidos em interfaces e relatórios, (2) suporte multi-idioma em operações globais, (3) pesquisa de condições de pagamento pelo nome no idioma local.

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(15) | NOT NULL | PK/FK | FK para [[ap_terms_b]]. Identificador da condição de pagamento. | [[ap_terms_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: US, PTB, ESA). Compõe PK com TERM_ID. | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | MLS | Idioma de origem da tradução (para detectar registros não traduzidos). | — | 🟢 100% |
| 4 | NAME | VARCHAR2(50) | NOT NULL | Tradução | Nome da condição de pagamento no idioma especificado. | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Tradução | Descrição da condição de pagamento no idioma especificado. | — | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário que criou o registro. | — | 🟢 100% |
| 7 | CREATION_DATE | DATE | NOT NULL | WHO | Data de criação do registro. | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | WHO | Usuário da última atualização. | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | DATE | NOT NULL | WHO | Data da última atualização. | — | 🟢 100% |

## Relacionamentos

### Tabelas-pai

- **[[ap_terms_b]]** — Condição de pagamento base (N:1 via `TERM_ID`).

### Tabelas-filha

- Nenhuma tabela-filha direta identificada.

## Uso Típico

```sql
-- Condições de pagamento com nome em português brasileiro
SELECT tb.TERM_ID,
       tb.NAME AS nome_base,
       tl.NAME AS nome_ptb,
       tl.DESCRIPTION AS descricao_ptb
  FROM AP_TERMS_B tb
  JOIN AP_TERMS_TL tl
    ON tl.TERM_ID = tb.TERM_ID
 WHERE tl.LANGUAGE = 'PTB'
   AND tb.ENABLED_FLAG = 'Y'
 ORDER BY tl.NAME;
```

## Observações

- A PK composta é (`TERM_ID`, `LANGUAGE`).
- Quando `LANGUAGE <> SOURCE_LANG`, o registro ainda está no idioma de origem (não foi traduzido).
- Na prática, para relatórios em pt-BR, usar `LANGUAGE = 'PTB'`; para inglês, usar `LANGUAGE = 'US'`.
- Para consultas simplificadas, utilizar a view [[ap_terms_vl]] que já realiza o join entre `_B` e `_TL` com filtro automático de idioma da sessão.
- Estrutura análoga a [[ra_terms_tl]] do módulo AR.

## Referências

- Oracle Fusion Cloud Financials — Accounts Payable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Multi-Language Support (MLS) Architecture.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).

---

## 🔗 PVOs Relacionados

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PaymentTermLanguage | — |
| NAME | PaymentTermName | ✅ |
| TERM_ID | PaymentTermTermId | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | PaymentTermLanguage | — |
| NAME | PaymentTermName | ✅ |
| TERM_ID | PaymentTermTermId | — |

### [[paymenttermheadertranslationextractpvo|PaymentTermHeaderTranslationExtractPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PaymentTermHeaderTranslationCreatedBy | ✅ |
| CREATION_DATE | PaymentTermHeaderTranslationCreationDate | ✅ |
| DESCRIPTION | PaymentTermHeaderTranslationDescription | ✅ |
| LANGUAGE | PaymentTermHeaderTranslationLanguage | ✅ |
| LAST_UPDATE_DATE | PaymentTermHeaderTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentTermHeaderTranslationLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PaymentTermHeaderTranslationLastUpdatedBy | ✅ |
| NAME | PaymentTermHeaderTranslationName | ✅ |
| OBJECT_VERSION_NUMBER | PaymentTermHeaderTranslationObjectVersionNumber | ✅ |
| SOURCE_LANG | PaymentTermHeaderTranslationSourceLang | ✅ |
| TERM_ID | PaymentTermHeaderTranslationTermId | ✅ |

### [[paymenttermheadertranslationpvo|PaymentTermHeaderTranslationPVO]] (AP · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| SOURCE_LANG | SourceLang | ✅ |
| TERM_ID | TermId | ✅ |
