---
id: DOC-GL-022
doc_type: system-doc
title: "GL_JE_HEADERS — Cabeçalhos de Lançamentos Contábeis"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - lancamentos
  - journal-entries
  - journal-headers
aliases:
  - GL_JE_HEADERS
  - gl_je_headers
  - cabecalhos-lancamento-gl
  - journal-headers
  - journal-entries
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_HEADERS

## 📌 Visão Geral

Armazena os **cabeçalhos de lançamentos contábeis** (journal entries) do General Ledger. Cada registro representa um journal individual com seu nome, categoria, fonte, período, moeda e status. É o nível intermediário da hierarquia de lançamentos: Batch → **Header** → Lines. Esta é uma das tabelas mais consultadas do GL para análise de lançamentos.

> [!note] Hierarquia de lançamentos
> A estrutura de lançamentos no GL segue três níveis: **GL_JE_BATCHES** (lote) → **GL_JE_HEADERS** (cabeçalho/journal) → **GL_JE_LINES** (linhas/partidas). Um journal pertence a exatamente um lote e contém múltiplas linhas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Lançamentos contábeis:** Registro de todos os journals (manuais e importados de subledgers).
- **Classificação:** Categorização dos lançamentos por fonte (source) e categoria (category).
- **Workflow de aprovação:** Controle de status individual do journal dentro do lote.
- **Reconciliação:** Identificação de lançamentos por período, moeda e origem.
- **Reversão:** Journals podem ser revertidos individualmente, com referência ao header original.
- **Auditoria:** Rastreamento completo de quem criou o lançamento, quando e de qual fonte.
- **Relatórios gerenciais:** Análise de volumes e valores por categoria, fonte e período.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cabeçalho do lançamento | — | 🟢 100% |
| 2 | JE_BATCH_ID | NUMBER(18) | NOT NULL | FK | ID do lote ao qual o journal pertence | [[gl_je_batches]] | 🟢 100% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 100% |
| 4 | NAME | VARCHAR2(100) | NOT NULL | Identificação | Nome do journal (visível ao usuário) | — | 🟢 100% |
| 5 | JE_CATEGORY | VARCHAR2(25) | NOT NULL | FK | Categoria do lançamento | [[gl_je_categories_b]] | 🟢 100% |
| 6 | JE_SOURCE | VARCHAR2(25) | NOT NULL | FK | Fonte do lançamento (ex: Manual, Payables, Receivables) | [[gl_je_sources_b]] | 🟢 100% |
| 7 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Período contábil do lançamento | — | 🟢 100% |
| 8 | DEFAULT_EFFECTIVE_DATE | DATE | NOT NULL | Data | Data efetiva padrão (GL Date) | — | 🟢 100% |
| 9 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status do journal: U (Unposted), P (Posted), S (Selected), I (Error) | — | 🟢 100% |
| 10 | ACTUAL_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Tipo: A (Actual), B (Budget), E (Encumbrance) | — | 🟢 100% |
| 11 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda do lançamento (ex: BRL, USD) | — | 🟢 100% |
| 12 | CURRENCY_CONVERSION_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 95% |
| 13 | CURRENCY_CONVERSION_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio (ex: Corporate, Spot, User) | — | 🟢 95% |
| 14 | CURRENCY_CONVERSION_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 95% |
| 15 | RUNNING_TOTAL_DR | NUMBER | NULL | Financeiro | Total acumulado a débito do journal | — | 🟢 95% |
| 16 | RUNNING_TOTAL_CR | NUMBER | NULL | Financeiro | Total acumulado a crédito do journal | — | 🟢 95% |
| 17 | RUNNING_TOTAL_ACCOUNTED_DR | NUMBER | NULL | Financeiro | Total acumulado a débito — moeda funcional | — | 🟡 80% |
| 18 | RUNNING_TOTAL_ACCOUNTED_CR | NUMBER | NULL | Financeiro | Total acumulado a crédito — moeda funcional | — | 🟡 80% |
| 19 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do journal | — | 🟢 100% |
| 20 | CONTROL_TOTAL | NUMBER | NULL | Financeiro | Total de controle informado pelo usuário | — | 🟢 95% |
| 21 | ACCRUAL_REV_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é um journal de reversão de accrual (Y/N) | — | 🟢 90% |
| 22 | ACCRUAL_REV_PERIOD_NAME | VARCHAR2(15) | NULL | Período | Período da reversão de accrual | — | 🟢 90% |
| 23 | ACCRUAL_REV_EFFECTIVE_DATE | DATE | NULL | Data | Data efetiva da reversão de accrual | — | 🟢 90% |
| 24 | REVERSED_JE_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | ID do header original (quando este é um journal de reversão) | [[gl_je_headers]] | 🟢 90% |
| 25 | REVERSAL_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é um journal de reversão (Y/N) | — | 🟢 90% |
| 26 | REVERSAL_PERIOD | VARCHAR2(15) | NULL | Período | Período em que a reversão foi efetuada | — | 🟢 90% |
| 27 | REVERSAL_METHOD | VARCHAR2(1) | NULL | Classificação | Método de reversão: C (Change sign), S (Switch DR/CR) | — | 🟡 80% |
| 28 | EXTERNAL_REFERENCE | VARCHAR2(80) | NULL | Referência cruzada | Referência externa (ex: número do documento no sistema de origem) | — | 🟢 90% |
| 29 | POSTED_DATE | DATE | NULL | Data | Data em que o journal foi postado | — | 🟢 100% |
| 30 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 90% |
| 31 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 90% |
| 32 | TAX_STATUS_CODE | VARCHAR2(1) | NULL | Classificação | Status fiscal do lançamento | — | 🟡 70% |
| 33 | BUDGET_VERSION_ID | NUMBER(18) | NULL | FK | Versão do orçamento (quando ACTUAL_FLAG = 'B') | — | 🟢 90% |
| 34 | ENCUMBRANCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de reserva (quando ACTUAL_FLAG = 'E') | [[gl_encumbrance_types_b]] | 🟢 90% |
| 35 | PARENT_JE_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | ID do header pai (em caso de alocação ou geração automática) | [[gl_je_headers]] | 🟡 75% |
| 36 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 80% |
| 37 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 38 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 39 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 40 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 41 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 42 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 43 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_batches]] — via `JE_BATCH_ID` (lote ao qual pertence)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_je_categories_b]] — via `JE_CATEGORY` (categoria do lançamento)
- [[gl_je_sources_b]] — via `JE_SOURCE` (fonte do lançamento)
- [[gl_je_headers]] — via `REVERSED_JE_HEADER_ID` (journal original em reversões — auto-referência)
- [[gl_je_headers]] — via `PARENT_JE_HEADER_ID` (journal pai — auto-referência)
- [[gl_encumbrance_types_b]] — via `ENCUMBRANCE_TYPE_ID` (tipo de reserva)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit proprietária do journal)

### Tabelas-filha (FK de saída)
- [[gl_je_lines]] — via `JE_HEADER_ID` (linhas do lançamento)
- [[gl_import_references]] — via `JE_HEADER_ID` (referências de importação/subledger)

---

## 📎 Uso Típico

### Journals de um período por categoria
```sql
SELECT h.JE_HEADER_ID, h.NAME, h.JE_CATEGORY, h.JE_SOURCE,
       h.STATUS, h.CURRENCY_CODE,
       h.RUNNING_TOTAL_DR, h.RUNNING_TOTAL_CR
FROM   GL_JE_HEADERS h
WHERE  h.LEDGER_ID = :p_ledger_id
  AND  h.PERIOD_NAME = 'MAR-26'
  AND  h.ACTUAL_FLAG = 'A'
ORDER BY h.JE_CATEGORY, h.NAME;
```

### Journals não postados pendentes
```sql
SELECT h.NAME, h.JE_CATEGORY, h.JE_SOURCE,
       h.DEFAULT_EFFECTIVE_DATE,
       h.RUNNING_TOTAL_DR, h.RUNNING_TOTAL_CR
FROM   GL_JE_HEADERS h
WHERE  h.LEDGER_ID = :p_ledger_id
  AND  h.STATUS = 'U'
  AND  h.PERIOD_NAME = 'MAR-26'
ORDER BY h.DEFAULT_EFFECTIVE_DATE;
```

### Journals de reversão
```sql
SELECT h.NAME AS reversal_journal,
       h.REVERSED_JE_HEADER_ID,
       orig.NAME AS original_journal,
       h.REVERSAL_METHOD
FROM   GL_JE_HEADERS h
JOIN   GL_JE_HEADERS orig ON orig.JE_HEADER_ID = h.REVERSED_JE_HEADER_ID
WHERE  h.REVERSAL_FLAG = 'Y'
  AND  h.LEDGER_ID = :p_ledger_id
  AND  h.PERIOD_NAME = 'MAR-26';
```

### Filtros comuns
- `STATUS = 'U'` — Não postados (Unposted)
- `STATUS = 'P'` — Postados (Posted)
- `ACTUAL_FLAG = 'A'` — Lançamentos reais
- `JE_SOURCE = 'Manual'` — Lançamentos manuais
- `JE_SOURCE = 'Payables'` — Importados do AP
- `JE_SOURCE = 'Receivables'` — Importados do AR
- `JE_CATEGORY = 'Adjustment'` — Categoria: ajuste

---

## 🔒 Observações

- O `STATUS` segue o mesmo padrão do batch: **U** (não postado), **S** (selecionado), **P** (postado), **I** (erro).
- `JE_SOURCE` identifica a origem: **Manual** (usuário), **Payables** (AP), **Receivables** (AR), **Assets** (FA), **Subledger Accounting** (SLA), etc.
- `JE_CATEGORY` classifica o tipo: **Adjustment**, **Accrual**, **Revaluation**, **Opening**, **Closing**, etc.
- Journals de reversão preenchem `REVERSED_JE_HEADER_ID` e `REVERSAL_FLAG = 'Y'`.
- `REVERSAL_METHOD`: **C** (Change sign) inverte o sinal dos valores; **S** (Switch) troca débito por crédito.
- O `CURRENCY_CODE` pode ser diferente da moeda funcional do ledger — neste caso, `CURRENCY_CONVERSION_RATE` indica a taxa aplicada.
- Journals com `ACCRUAL_REV_FLAG = 'Y'` são marcados para reversão automática no período indicado em `ACCRUAL_REV_PERIOD_NAME`.

---

## 🔗 PVOs Relacionados

### [[journalheaderextractpvo|JournalHeaderExtractPVO]] (GL · BICC: 1/125)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_REV_CHANGE_SIGN_FLAG | GlJeHeadersAccrualRevChangeSignFlag | — |
| ACCRUAL_REV_EFFECTIVE_DATE | GlJeHeadersAccrualRevEffectiveDate | — |
| ACCRUAL_REV_FLAG | GlJeHeadersAccrualRevFlag | — |
| ACCRUAL_REV_JE_HEADER_ID | GlJeHeadersAccrualRevJeHeaderId | — |
| ACCRUAL_REV_PERIOD_NAME | GlJeHeadersAccrualRevPeriodName | — |
| ACCRUAL_REV_STATUS | GlJeHeadersAccrualRevStatus | — |
| ACTUAL_FLAG | GlJeHeadersActualFlag | — |
| ATTRIBUTE1 | GlJeHeadersAttribute1 | — |
| ATTRIBUTE10 | GlJeHeadersAttribute10 | — |
| ATTRIBUTE2 | GlJeHeadersAttribute2 | — |
| ATTRIBUTE3 | GlJeHeadersAttribute3 | — |
| ATTRIBUTE4 | GlJeHeadersAttribute4 | — |
| ATTRIBUTE5 | GlJeHeadersAttribute5 | — |
| ATTRIBUTE6 | GlJeHeadersAttribute6 | — |
| ATTRIBUTE7 | GlJeHeadersAttribute7 | — |
| ATTRIBUTE8 | GlJeHeadersAttribute8 | — |
| ATTRIBUTE9 | GlJeHeadersAttribute9 | — |
| ATTRIBUTE_CATEGORY | GlJeHeadersAttributeCategory | — |
| ATTRIBUTE_CATEGORY2 | GlJeHeadersAttributeCategory2 | — |
| ATTRIBUTE_DATE1 | GlJeHeadersAttributeDate1 | — |
| ATTRIBUTE_DATE2 | GlJeHeadersAttributeDate2 | — |
| ATTRIBUTE_DATE3 | GlJeHeadersAttributeDate3 | — |
| ATTRIBUTE_DATE4 | GlJeHeadersAttributeDate4 | — |
| ATTRIBUTE_DATE5 | GlJeHeadersAttributeDate5 | — |
| ATTRIBUTE_NUMBER1 | GlJeHeadersAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | GlJeHeadersAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | GlJeHeadersAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | GlJeHeadersAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | GlJeHeadersAttributeNumber5 | — |
| BALANCED_JE_FLAG | GlJeHeadersBalancedJeFlag | — |
| BALANCING_SEGMENT_VALUE | GlJeHeadersBalancingSegmentValue | — |
| BUDGET_VERSION_ID | GlJeHeadersBudgetVersionId | — |
| CLOSE_ACCT_SEQ_ASSIGN_ID | GlJeHeadersCloseAcctSeqAssignId | — |
| CLOSE_ACCT_SEQ_VALUE | GlJeHeadersCloseAcctSeqValue | — |
| CLOSE_ACCT_SEQ_VERSION_ID | GlJeHeadersCloseAcctSeqVersionId | — |
| CONTROL_TOTAL | GlJeHeadersControlTotal | — |
| CONVERSION_FLAG | GlJeHeadersConversionFlag | — |
| CR_BAL_SEG_VALUE | GlJeHeadersCrBalSegValue | — |
| CREATED_BY | GlJeHeadersCreatedBy | — |
| CREATION_DATE | GlJeHeadersCreationDate | — |
| CURRENCY_CODE | GlJeHeadersCurrencyCode | — |
| CURRENCY_CONVERSION_DATE | GlJeHeadersCurrencyConversionDate | — |
| CURRENCY_CONVERSION_RATE | GlJeHeadersCurrencyConversionRate | — |
| CURRENCY_CONVERSION_TYPE | GlJeHeadersCurrencyConversionType | — |
| DATE_CREATED | GlJeHeadersDateCreated | — |
| DEFAULT_EFFECTIVE_DATE | GlJeHeadersDefaultEffectiveDate | — |
| DESCRIPTION | GlJeHeadersDescription | — |
| DISPLAY_ALC_JOURNAL_FLAG | GlJeHeadersDisplayAlcJournalFlag | — |
| DOC_SEQUENCE_ID | GlJeHeadersDocSequenceId | — |
| DOC_SEQUENCE_VALUE | GlJeHeadersDocSequenceValue | — |
| DR_BAL_SEG_VALUE | GlJeHeadersDrBalSegValue | — |
| EARLIEST_POSTABLE_DATE | GlJeHeadersEarliestPostableDate | — |
| ENCUMBRANCE_TYPE_ID | GlJeHeadersEncumbranceTypeId | — |
| EXTERNAL_REFERENCE | GlJeHeadersExternalReference | — |
| FROM_RECURRING_HEADER_ID | GlJeHeadersFromRecurringHeaderId | — |
| GLOBAL_ATTRIBUTE1 | GlJeHeadersGlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlJeHeadersGlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlJeHeadersGlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlJeHeadersGlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlJeHeadersGlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlJeHeadersGlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlJeHeadersGlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlJeHeadersGlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlJeHeadersGlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlJeHeadersGlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlJeHeadersGlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlJeHeadersGlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlJeHeadersGlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlJeHeadersGlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlJeHeadersGlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlJeHeadersGlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlJeHeadersGlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlJeHeadersGlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlJeHeadersGlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlJeHeadersGlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlJeHeadersGlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | GlJeHeadersGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE2 | GlJeHeadersGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | GlJeHeadersGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | GlJeHeadersGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | GlJeHeadersGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | GlJeHeadersGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | GlJeHeadersGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | GlJeHeadersGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | GlJeHeadersGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | GlJeHeadersGlobalAttributeNumber5 | — |
| INTERCOMPANY_MODE | GlJeHeadersIntercompanyMode | — |
| JE_BATCH_ID | GlJeHeadersJeBatchId | — |
| JE_CATEGORY | GlJeHeadersJeCategory | — |
| JE_FROM_SLA_FLAG | GlJeHeadersJeFromSlaFlag | — |
| JE_HEADER_ID | JeHeaderId | ✅ |
| JE_HEADER_ID | ReversalJournalHeaderJeHeaderId | — |
| JE_SOURCE | GlJeHeadersJeSource | — |
| LAST_UPDATE_DATE | GlJeHeadersLastUpdateDate | — |
| LAST_UPDATE_LOGIN | GlJeHeadersLastUpdateLogin | — |
| LAST_UPDATED_BY | GlJeHeadersLastUpdatedBy | — |
| LEDGER_ID | GlJeHeadersLedgerId | — |
| LEGAL_ENTITY_ID | GlJeHeadersLegalEntityId | — |
| LOCAL_DOC_SEQUENCE_ID | GlJeHeadersLocalDocSequenceId | — |
| LOCAL_DOC_SEQUENCE_VALUE | GlJeHeadersLocalDocSequenceValue | — |
| MULTI_BAL_SEG_FLAG | GlJeHeadersMultiBalSegFlag | — |
| MULTI_CURRENCY_FLAG | GlJeHeadersMultiCurrencyFlag | — |
| NAME | GlJeHeadersName | — |
| NAME | ReversalJournalHeaderName | — |
| OBJECT_VERSION_NUMBER | GlJeHeadersObjectVersionNumber | — |
| ORIGINATING_BAL_SEG_VALUE | GlJeHeadersOriginatingBalSegValue | — |
| PARENT_JE_HEADER_ID | GlJeHeadersParentJeHeaderId | — |
| PERIOD_NAME | GlJeHeadersPeriodName | — |
| POST_CURRENCY_CODE | GlJeHeadersPostCurrencyCode | — |
| POST_MULTI_CURRENCY_FLAG | GlJeHeadersPostMultiCurrencyFlag | — |
| POSTED_DATE | GlJeHeadersPostedDate | — |
| POSTED_DATE | GlJeHeadersPostedDateTime | — |
| POSTING_ACCT_SEQ_ASSIGN_ID | GlJeHeadersPostingAcctSeqAssignId | — |
| POSTING_ACCT_SEQ_VALUE | GlJeHeadersPostingAcctSeqValue | — |
| POSTING_ACCT_SEQ_VERSION_ID | GlJeHeadersPostingAcctSeqVersionId | — |
| REFERENCE_DATE | GlJeHeadersReferenceDate | — |
| REVERSED_JE_HEADER_ID | GlJeHeadersReversedJeHeaderId | — |
| RUNNING_TOTAL_ACCOUNTED_CR | GlJeHeadersRunningTotalAccountedCr | — |
| RUNNING_TOTAL_ACCOUNTED_DR | GlJeHeadersRunningTotalAccountedDr | — |
| RUNNING_TOTAL_CR | GlJeHeadersRunningTotalCr | — |
| RUNNING_TOTAL_DR | GlJeHeadersRunningTotalDr | — |
| STATUS | GlJeHeadersStatus | — |
| TAX_LEGAL_ENTITY_ID | GlJeHeadersTaxLegalEntityId | — |
| TAX_STATUS_CODE | GlJeHeadersTaxStatusCode | — |
| USSGL_TRANSACTION_CODE | GlJeHeadersUssglTransactionCode | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL · BICC: 41/68)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_REV_CHANGE_SIGN_FLAG | JrnlHdrAccrualRevChangeSignFlagCode | ✅ |
| ACCRUAL_REV_EFFECTIVE_DATE | JrnlHdrAccrualRevEffectiveDate | — |
| ACCRUAL_REV_FLAG | JrnlHdrAccrualRevFlag | ✅ |
| ACCRUAL_REV_JE_HEADER_ID | JrnlHdrAccrualRevJeHeaderId | — |
| ACCRUAL_REV_PERIOD_NAME | JrnlHdrAccrualRevPeriodName | ✅ |
| ACCRUAL_REV_STATUS | JrnlHdrAccrualRevStatus | ✅ |
| ACTUAL_FLAG | JrnlHdrActualFlag | ✅ |
| BALANCED_JE_FLAG | JrnlHdrBalancedJeFlag | — |
| BALANCING_SEGMENT_VALUE | JrnlHdrBalancingSegmentValue | ✅ |
| BUDGET_VERSION_ID | JrnlHdrBudgetVersionId | — |
| CLOSE_ACCT_SEQ_ASSIGN_ID | JrnlHdrCloseAcctSeqAssignId | — |
| CLOSE_ACCT_SEQ_VALUE | JrnlHdrCloseAcctSeqValue | ✅ |
| CLOSE_ACCT_SEQ_VERSION_ID | JrnlHdrCloseAcctSeqVersionId | — |
| CONTROL_TOTAL | JrnlHdrControlTotal | ✅ |
| CONVERSION_FLAG | JrnlHdrConversionFlag | ✅ |
| CR_BAL_SEG_VALUE | JrnlHdrCrBalSegValue | ✅ |
| CREATED_BY | JrnlHdrCreatedBy | ✅ |
| CREATION_DATE | JrnlHdrCreationDate | — |
| CURRENCY_CODE | JrnlHdrCurrencyCode | ✅ |
| CURRENCY_CONVERSION_DATE | JrnlHdrCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_RATE | JrnlHdrCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_TYPE | JrnlHdrCurrencyConversionType | ✅ |
| DATE_CREATED | JrnlHdrDateCreated | ✅ |
| DEFAULT_EFFECTIVE_DATE | JrnlHdrDefaultEffectiveDate | ✅ |
| DESCRIPTION | JrnlHdrDescription | ✅ |
| DISPLAY_ALC_JOURNAL_FLAG | JrnlHdrDisplayAlcJournalFlag | — |
| DOC_SEQUENCE_ID | JrnlHdrDocSequenceId | — |
| DOC_SEQUENCE_VALUE | JrnlHdrDocSequenceValue | ✅ |
| DR_BAL_SEG_VALUE | JrnlHdrDrBalSegValue | ✅ |
| EARLIEST_POSTABLE_DATE | JrnlHdrEarliestPostableDate | — |
| ENCUMBRANCE_TYPE_ID | JrnlHdrEncumbranceTypeId | — |
| EXTERNAL_REFERENCE | JrnlHdrExternalReference | ✅ |
| FROM_RECURRING_HEADER_ID | JrnlHdrFromRecurringHeaderId | — |
| INTERCOMPANY_MODE | JrnlHdrIntercompanyMode | — |
| JE_BATCH_ID | JrnlHdrJeBatchId | — |
| JE_CATEGORY | JrnlHdrJeCategory | — |
| JE_FROM_SLA_FLAG | JrnlHdrJeFromSlaFlag | ✅ |
| JE_HEADER_ID | JeHeaderId | ✅ |
| JE_SOURCE | JrnlHdrJeSource | — |
| LAST_UPDATE_DATE | JrnlHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlHdrLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlHdrLastUpdatedBy | ✅ |
| LEDGER_ID | JrnlHdrLedgerId | — |
| LOCAL_DOC_SEQUENCE_ID | JrnlHdrLocalDocSequenceId | — |
| LOCAL_DOC_SEQUENCE_VALUE | JrnlHdrLocalDocSequenceValue | ✅ |
| MULTI_BAL_SEG_FLAG | JrnlHdrMultiBalSegFlag | — |
| MULTI_CURRENCY_FLAG | JrnlHdrMultiCurrencyFlag | ✅ |
| NAME | JrnlHdrName | ✅ |
| OBJECT_VERSION_NUMBER | JrnlHdrObjectVersionNumber | — |
| ORIGINATING_BAL_SEG_VALUE | JrnlHdrOriginatingBalSegValue | ✅ |
| PARENT_JE_HEADER_ID | JrnlHdrParentJeHeaderId | ✅ |
| PERIOD_NAME | JrnlHdrPeriodName | ✅ |
| POST_CURRENCY_CODE | JrnlHdrPostCurrencyCode | — |
| POST_MULTI_CURRENCY_FLAG | JrnlHdrPostMultiCurrencyFlag | ✅ |
| POSTED_DATE | JrnlHdrPostedDate | ✅ |
| POSTED_DATE | JrnlHdrPostedDateTime | — |
| POSTING_ACCT_SEQ_ASSIGN_ID | JrnlHdrPostingAcctSeqAssignId | — |
| POSTING_ACCT_SEQ_VALUE | JrnlHdrPostingAcctSeqValue | ✅ |
| POSTING_ACCT_SEQ_VERSION_ID | JrnlHdrPostingAcctSeqVersionId | — |
| REFERENCE_DATE | JrnlHdrReferenceDate | ✅ |
| REVERSED_JE_HEADER_ID | JrnlHdrReversedJeHeaderId | ✅ |
| RUNNING_TOTAL_ACCOUNTED_CR | JrnlHdrRunningTotalAccountedCr | ✅ |
| RUNNING_TOTAL_ACCOUNTED_DR | JrnlHdrRunningTotalAccountedDr | ✅ |
| RUNNING_TOTAL_CR | JrnlHdrRunningTotalCr | ✅ |
| RUNNING_TOTAL_DR | JrnlHdrRunningTotalDr | ✅ |
| STATUS | JrnlHdrStatus | ✅ |
| TAX_LEGAL_ENTITY_ID | JrnlHdrTaxLegalEntityId | — |
| TAX_STATUS_CODE | JrnlHdrTaxStatusCode | — |

### [[journalimportreferencepvo|JournalImportReferencePVO]] (GL · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | JournalCreatedBy | — |
| CREATION_DATE | JournalCreationDate | — |
| JE_HEADER_ID | JrnlHdrJeHeaderId | — |
| LAST_UPDATE_DATE | GjhLastUpdateDate | ✅ |
| LAST_UPDATED_BY | GjhLastUpdatedBy | — |
| LEDGER_ID | LedgerId | ✅ |
| OBJECT_VERSION_NUMBER | JrnlHdrObjectVerNum | — |
| STATUS | Status | ✅ |

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 38/68)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCRUAL_REV_CHANGE_SIGN_FLAG | JrnlHdrAccrualRevChangeSignFlagCode | ✅ |
| ACCRUAL_REV_EFFECTIVE_DATE | JrnlHdrAccrualRevEffectiveDate | — |
| ACCRUAL_REV_FLAG | JrnlHdrAccrualRevFlag | ✅ |
| ACCRUAL_REV_JE_HEADER_ID | JrnlHdrAccrualRevJeHeaderId | — |
| ACCRUAL_REV_PERIOD_NAME | JrnlHdrAccrualRevPeriodName | ✅ |
| ACCRUAL_REV_STATUS | JrnlHdrAccrualRevStatus | ✅ |
| ACTUAL_FLAG | JrnlHdrActualFlag | ✅ |
| BALANCED_JE_FLAG | JrnlHdrBalancedJeFlag | — |
| BALANCING_SEGMENT_VALUE | JrnlHdrBalancingSegmentValue | ✅ |
| BUDGET_VERSION_ID | JrnlHdrBudgetVersionId | — |
| CLOSE_ACCT_SEQ_ASSIGN_ID | JrnlHdrCloseAcctSeqAssignId | — |
| CLOSE_ACCT_SEQ_VALUE | JrnlHdrCloseAcctSeqValue | ✅ |
| CLOSE_ACCT_SEQ_VERSION_ID | JrnlHdrCloseAcctSeqVersionId | — |
| CONTROL_TOTAL | JrnlHdrControlTotal | — |
| CONVERSION_FLAG | JrnlHdrConversionFlag | ✅ |
| CR_BAL_SEG_VALUE | JrnlHdrCrBalSegValue | ✅ |
| CREATED_BY | JrnlHdrCreatedBy | ✅ |
| CREATION_DATE | JrnlHdrCreationDate | — |
| CURRENCY_CODE | JrnlHdrCurrencyCode | ✅ |
| CURRENCY_CONVERSION_DATE | JrnlHdrCurrencyConversionDate | ✅ |
| CURRENCY_CONVERSION_RATE | JrnlHdrCurrencyConversionRate | ✅ |
| CURRENCY_CONVERSION_TYPE | JrnlHdrCurrencyConversionType | ✅ |
| DATE_CREATED | JrnlHdrDateCreated | ✅ |
| DEFAULT_EFFECTIVE_DATE | JrnlHdrDefaultEffectiveDate | ✅ |
| DESCRIPTION | JrnlHdrDescription | ✅ |
| DISPLAY_ALC_JOURNAL_FLAG | JrnlHdrDisplayAlcJournalFlag | — |
| DOC_SEQUENCE_ID | JrnlHdrDocSequenceId | — |
| DOC_SEQUENCE_VALUE | JrnlHdrDocSequenceValue | ✅ |
| DR_BAL_SEG_VALUE | JrnlHdrDrBalSegValue | ✅ |
| EARLIEST_POSTABLE_DATE | JrnlHdrEarliestPostableDate | — |
| ENCUMBRANCE_TYPE_ID | JrnlHdrEncumbranceTypeId | — |
| EXTERNAL_REFERENCE | JrnlHdrExternalReference | ✅ |
| FROM_RECURRING_HEADER_ID | JrnlHdrFromRecurringHeaderId | — |
| INTERCOMPANY_MODE | JrnlHdrIntercompanyMode | — |
| JE_BATCH_ID | JrnlHdrJeBatchId | — |
| JE_CATEGORY | JrnlHdrJeCategory | ✅ |
| JE_FROM_SLA_FLAG | JrnlHdrJeFromSlaFlag | ✅ |
| JE_HEADER_ID | JrnlHdrJeHeaderId | — |
| JE_SOURCE | JrnlHdrJeSource | ✅ |
| LAST_UPDATE_DATE | JrnlHdrLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JrnlHdrLastUpdateLogin | — |
| LAST_UPDATED_BY | JrnlHdrLastUpdatedBy | ✅ |
| LEDGER_ID | JrnlHdrLedgerId | ✅ |
| LOCAL_DOC_SEQUENCE_ID | JrnlHdrLocalDocSequenceId | — |
| LOCAL_DOC_SEQUENCE_VALUE | JrnlHdrLocalDocSequenceValue | ✅ |
| MULTI_BAL_SEG_FLAG | JrnlHdrMultiBalSegFlag | — |
| MULTI_CURRENCY_FLAG | JrnlHdrMultiCurrencyFlag | ✅ |
| NAME | JrnlHdrName | ✅ |
| OBJECT_VERSION_NUMBER | JrnlHdrObjectVersionNumber | — |
| ORIGINATING_BAL_SEG_VALUE | JrnlHdrOriginatingBalSegValue | ✅ |
| PARENT_JE_HEADER_ID | JrnlHdrParentJeHeaderId | ✅ |
| PERIOD_NAME | JrnlHdrPeriodName | ✅ |
| POST_MULTI_CURRENCY_FLAG | JrnlHdrPostMultiCurrencyFlag | ✅ |
| POSTED_DATE | JrnlHdrPostedDate | ✅ |
| POSTED_DATE | JrnlHdrPostedDateTime | — |
| POSTING_ACCT_SEQ_ASSIGN_ID | JrnlHdrPostingAcctSeqAssignId | — |
| POSTING_ACCT_SEQ_VALUE | JrnlHdrPostingAcctSeqValue | ✅ |
| POSTING_ACCT_SEQ_VERSION_ID | JrnlHdrPostingAcctSeqVersionId | — |
| REFERENCE_DATE | JrnlHdrReferenceDate | ✅ |
| REVERSED_JE_HEADER_ID | JrnlHdrReversedJeHeaderId | ✅ |
| RUNNING_TOTAL_ACCOUNTED_CR | JrnlHdrRunningTotalAccountedCr | — |
| RUNNING_TOTAL_ACCOUNTED_DR | JrnlHdrRunningTotalAccountedDr | — |
| RUNNING_TOTAL_CR | JrnlHdrRunningTotalCr | — |
| RUNNING_TOTAL_DR | JrnlHdrRunningTotalDr | — |
| STATUS | JrnlHdrStatus | ✅ |
| TAX_LEGAL_ENTITY_ID | JrnlHdrTaxLegalEntityId | — |
| TAX_STATUS_CODE | JrnlHdrTaxStatusCode | — |
| USSGL_TRANSACTION_CODE | JrnlHdrUssglTransactionCode | — |

---

## 📚 Referências

- [Oracle Docs — GL_JE_HEADERS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljeheaders-25722.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
