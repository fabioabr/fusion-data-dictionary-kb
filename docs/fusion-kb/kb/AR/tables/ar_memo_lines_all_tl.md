---
id: DOC-AR-055
doc_type: system-doc
title: "AR_MEMO_LINES_ALL_TL — Traduções das Linhas de Memo"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, memo-lines, traducoes, multilinguagem]
aliases: [AR_MEMO_LINES_ALL_TL, ar_memo_lines_all_tl, memo_lines_tl, traducoes_memo_lines, ar_memo_tl]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_MEMO_LINES_ALL_TL

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela de **traduções** (sufixo `_TL`) das linhas de memo. Armazena nomes e descrições traduzidos para cada idioma instalado no ambiente. Segue o padrão MLS (Multi-Language Support) do Oracle Fusion.

## 🧠 Propósito de Negócio

Permite que memo lines sejam exibidas no idioma do usuário ou do cliente. Em operações internacionais, uma mesma memo line pode ter nome e descrição em português, inglês, espanhol, etc., sem necessidade de cadastros duplicados.

Casos de uso principais:
- Exibição de memo lines no idioma do cliente na fatura
- Interface de usuário multilíngue
- Relatórios localizados por idioma

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | MEMO_LINE_ID | NUMBER | PK/FK composta. Referencia [[ar_memo_lines_all_b]]. | Chave | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2 | PK composta. Código do idioma da tradução (ex: `PTB`, `US`, `ESA`). | Chave | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2 | Idioma de origem da tradução. Quando igual a `LANGUAGE`, é tradução direta. | Controle | 🟢 100% |
| 4 | NAME | VARCHAR2 | Nome traduzido da memo line. | Identificação | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2 | Descrição traduzida da memo line. | Identificação | 🟢 100% |
| 6 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 7 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_memo_lines_all_b]] | MEMO_LINE_ID | FK | Tabela base da memo line |
| [[fnd_languages]] | LANGUAGE | FK | Idioma da tradução |

## 📎 Uso Típico

```sql
-- Obter memo lines com tradução em português
SELECT b.memo_line_id,
       tl.name,
       tl.description,
       b.unit_std_price
  FROM ar_memo_lines_all_b b
  JOIN ar_memo_lines_all_tl tl ON tl.memo_line_id = b.memo_line_id
 WHERE tl.language = 'PTB'
   AND b.org_id = :p_org_id;
```

```sql
-- Memo lines com tradução pendente (source_lang diferente de language)
SELECT tl.memo_line_id,
       tl.language,
       tl.source_lang,
       tl.name
  FROM ar_memo_lines_all_tl tl
 WHERE tl.language <> tl.source_lang;
```

## 🔒 Observações

- A PK composta é `MEMO_LINE_ID` + `LANGUAGE` — existe um registro por idioma instalado para cada memo line.
- Quando `SOURCE_LANG <> LANGUAGE`, a tradução é **herdada** do idioma de origem e ainda não foi traduzida diretamente.
- A tabela `_TL` é mantida automaticamente pelo framework MLS do Oracle — ao adicionar um novo idioma ao ambiente, registros são criados automaticamente com `SOURCE_LANG` apontando para o idioma base.
- Em migrações, é necessário carregar **ambas as tabelas** (`_B` e `_TL`) para cada memo line.

## 🔗 PVOs Relacionados

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | — |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | — |
| SET_ID | MemoLineTranslationSetId | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | — |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | — |
| SET_ID | MemoLineTranslationSetId | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | ✅ |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | ✅ |
| SET_ID | MemoLineTranslationSetId | — |

### [[memolineextractpvo|MemoLineExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ArMemoLineTLCreatedBy | ✅ |
| CREATION_DATE | ArMemoLineTLCreationDate | ✅ |
| DESCRIPTION | ArMemoLineTLDescription | ✅ |
| LANGUAGE | ArMemoLineTLLanguage | ✅ |
| LAST_UPDATE_DATE | ArMemoLineTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArMemoLineTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArMemoLineTLLastUpdatedBy | ✅ |
| MEMO_LINE_ID | ArMemoLineTLMemoLineId | ✅ |
| NAME | ArMemoLineTLName | ✅ |
| SEED_DATA_SOURCE | ArMemoLineTLSeedDataSource | ✅ |
| SET_ID | ArMemoLineTLSetId | ✅ |
| SOURCE_LANG | ArMemoLineTLSourceLang | ✅ |

### [[memolinepvo|MemoLinePVO]] (AR · BICC: 6/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | MemoLineTranslationCreatedBy | — |
| CREATION_DATE | MemoLineTranslationCreationDate | — |
| DESCRIPTION | MemoLineTranslationDescription | ✅ |
| LANGUAGE | MemoLineTranslationLanguage | ✅ |
| LAST_UPDATE_DATE | MemoLineTranslationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MemoLineTranslationLastUpdateLogin | — |
| LAST_UPDATED_BY | MemoLineTranslationLastUpdatedBy | — |
| MEMO_LINE_ID | MemoLineId | ✅ |
| NAME | MemoLineTranslationName | ✅ |
| OBJECT_VERSION_NUMBER | MemoLineTranslationObjectVersionNumber | — |
| SET_ID | SetId | ✅ |
| SOURCE_LANG | MemoLineTranslationSourceLang | — |

### [[memolinetlextractpvo|MemoLineTLExtractPVO]] (OTHER · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ArMemoLineTLCreatedBy | ✅ |
| CREATION_DATE | ArMemoLineTLCreationDate | ✅ |
| DESCRIPTION | ArMemoLineTLDescription | ✅ |
| LANGUAGE | ArMemoLineTLLanguage | ✅ |
| LAST_UPDATE_DATE | ArMemoLineTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArMemoLineTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ArMemoLineTLLastUpdatedBy | ✅ |
| MEMO_LINE_ID | ArMemoLineTLMemoLineId | ✅ |
| NAME | ArMemoLineTLName | ✅ |
| OBJECT_VERSION_NUMBER | ArMemoLineTLObjectVersionNumber | ✅ |
| SEED_DATA_SOURCE | ArMemoLineTLSeedDataSource | ✅ |
| SET_ID | ArMemoLineTLSetId | ✅ |
| SOURCE_LANG | ArMemoLineTLSourceLang | ✅ |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | — |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | — |
| SET_ID | MemoLineTranslationSetId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | — |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | — |
| SET_ID | MemoLineTranslationSetId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | — |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | — |
| SET_ID | MemoLineTranslationSetId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | — |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | — |
| SET_ID | MemoLineTranslationSetId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | ✅ |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | ✅ |
| SET_ID | MemoLineTranslationSetId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | MemoLineDescription | ✅ |
| LANGUAGE | MemoLineTranslationLanguage | — |
| MEMO_LINE_ID | MemoLineTranslationMemoLineId | — |
| NAME | MemoLineName | ✅ |
| SET_ID | MemoLineTranslationSetId | — |

---

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Memo Lines Translation View Object
- Oracle Fusion Cloud — Multi-Language Support (MLS) Technical Guide
