---
id: DOC-GL-002
doc_type: system-doc
title: "GL_CODE_COMBINATIONS — Combinações de Contas Contábeis"
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
  - ccid
  - plano-de-contas
  - chart-of-accounts
aliases:
  - GL_CODE_COMBINATIONS
  - gl_code_combinations
  - ccid
  - chart-of-accounts
  - plano-contas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_CODE_COMBINATIONS

## 📌 Visão Geral

Armazena todas as **combinações válidas de segmentos contábeis** (CCID — Code Combination ID) do plano de contas. Cada registro representa uma combinação única de segmentos (empresa, conta, centro de custo, projeto, etc.) utilizada em lançamentos contábeis. É a tabela de referência central do GL — praticamente toda tabela financeira do ERP aponta para ela via `CODE_COMBINATION_ID`.

> [!note] Tabela referenciada por todo o ERP
> `GL_CODE_COMBINATIONS` é a tabela mais referenciada do Oracle Fusion. Módulos como AP, AR, FA, PO e Cash Management apontam para ela via `CODE_COMBINATION_ID` em suas distribuições contábeis.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Plano de contas:** Armazena todas as combinações válidas de segmentos contábeis.
- **Lançamentos contábeis:** Todo lançamento no GL referencia um CCID desta tabela.
- **Distribuições de subledger:** AP, AR, FA usam CCID para contabilização.
- **Validação:** Controla quais combinações de conta/centro de custo/empresa são válidas.
- **Relatórios financeiros:** Base para agrupamento e drill-down por segmento.
- **Cross-validation rules:** Regras de validação cruzada entre segmentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da combinação de contas (CCID) | — | 🟢 100% |
| 2 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NOT NULL | FK | ID da estrutura do plano de contas (Key Flexfield) | — | 🟢 100% |
| 3 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se a combinação está habilitada (Y/N) | — | 🟢 100% |
| 4 | SUMMARY_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Indica se é conta de resumo/pai (Y) ou detalhe (N) | — | 🟢 100% |
| 5 | START_DATE_ACTIVE | DATE | NULL | Controle | Data de início de validade da combinação | — | 🟢 100% |
| 6 | END_DATE_ACTIVE | DATE | NULL | Controle | Data de fim de validade da combinação | — | 🟢 100% |
| 7 | SEGMENT1 | VARCHAR2(25) | NULL | Segmento | Segmento 1 — tipicamente Empresa/Entidade Legal | — | 🟢 100% |
| 8 | SEGMENT2 | VARCHAR2(25) | NULL | Segmento | Segmento 2 — tipicamente Conta Contábil (Natural Account) | — | 🟢 100% |
| 9 | SEGMENT3 | VARCHAR2(25) | NULL | Segmento | Segmento 3 — tipicamente Centro de Custo | — | 🟢 100% |
| 10 | SEGMENT4 | VARCHAR2(25) | NULL | Segmento | Segmento 4 — tipicamente Projeto ou Intercompany | — | 🟡 80% |
| 11 | SEGMENT5 | VARCHAR2(25) | NULL | Segmento | Segmento 5 — varia por implementação | — | 🟡 80% |
| 12 | SEGMENT6–30 | VARCHAR2(25) | NULL | Segmento | Segmentos adicionais (6 a 30) — configuráveis por implementação | — | 🟡 75% |
| 13 | ACCOUNT_TYPE | VARCHAR2(1) | NOT NULL | Classificação | Tipo de conta: A (Asset), L (Liability), O (Owner's Equity), R (Revenue), E (Expense) | — | 🟢 100% |
| 14 | DETAIL_POSTING_ALLOWED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Permite lançamento direto nesta combinação (Y/N) | — | 🟢 100% |
| 15 | DETAIL_BUDGETING_ALLOWED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Permite orçamento direto nesta combinação (Y/N) | — | 🟢 100% |
| 16 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição textual da combinação de contas | — | 🟢 100% |
| 17 | TEMPLATE_ID | NUMBER(18) | NULL | Sistema | ID do template de alocação, se aplicável | — | 🟡 70% |
| 18 | REFERENCE1–5 | VARCHAR2(240) | NULL | Referência | Campos de referência genéricos | — | 🟡 70% |
| 19 | JGZ_RECONCILIATION_FLAG | VARCHAR2(1) | NULL | Controle | Flag de reconciliação (específico de localização) | — | 🟡 65% |
| 20 | PRESERVE_FLAG | VARCHAR2(1) | NULL | Controle | Preservar combinação durante reorganização do plano de contas | — | 🟡 65% |
| 21 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 22 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 23 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 24 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela raiz (master data do plano de contas).

### Tabelas-filha (FK de saída)
- [[gl_balances]] — via `CODE_COMBINATION_ID` (saldos por combinação de conta)
- [[gl_je_lines]] — via `CODE_COMBINATION_ID` (linhas de lançamentos)
- [[ar_distributions_all]] — via `CODE_COMBINATION_ID` (distribuições AR)
- [[ar_adjustments_all]] — via `CODE_COMBINATION_ID` (ajustes de AR que utilizam esta combinação contábil)
- [[ar_misc_cash_distributions_all]] — via `CODE_COMBINATION_ID` (distribuições de misc receipts)

---

## 📎 Uso Típico

### Consultar combinação de conta por CCID
```sql
SELECT gcc.CODE_COMBINATION_ID,
       gcc.SEGMENT1 AS empresa,
       gcc.SEGMENT2 AS conta,
       gcc.SEGMENT3 AS centro_custo,
       gcc.ACCOUNT_TYPE,
       gcc.DESCRIPTION,
       gcc.ENABLED_FLAG
FROM   GL_CODE_COMBINATIONS gcc
WHERE  gcc.CODE_COMBINATION_ID = :p_ccid;
```

### Listar contas ativas de um segmento
```sql
SELECT gcc.CODE_COMBINATION_ID,
       gcc.SEGMENT1 || '.' || gcc.SEGMENT2 || '.' || gcc.SEGMENT3 AS conta_completa,
       gcc.DESCRIPTION,
       gcc.ACCOUNT_TYPE
FROM   GL_CODE_COMBINATIONS gcc
WHERE  gcc.CHART_OF_ACCOUNTS_ID = :p_coa_id
  AND  gcc.ENABLED_FLAG = 'Y'
  AND  gcc.SUMMARY_FLAG = 'N'
  AND  gcc.SEGMENT2 LIKE '4%'
ORDER BY gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Combinações ativas
- `SUMMARY_FLAG = 'N'` — Apenas contas de detalhe (não resumo)
- `ACCOUNT_TYPE = 'E'` — Contas de despesa
- `ACCOUNT_TYPE = 'R'` — Contas de receita

---

## 🔒 Observações

- O significado de cada `SEGMENT` depende da configuração do plano de contas (Key Flexfield). Os nomes típicos são: Empresa (SEGMENT1), Conta (SEGMENT2), Centro de Custo (SEGMENT3), mas podem variar por implementação.
- `ACCOUNT_TYPE` é derivado do segmento de conta natural (SEGMENT2 tipicamente): **A** (Ativo), **L** (Passivo), **O** (PL), **R** (Receita), **E** (Despesa).
- `SUMMARY_FLAG = 'Y'` indica contas-pai usadas apenas para rollup/consolidação — lançamentos são feitos apenas em contas de detalhe (`'N'`).
- `DETAIL_POSTING_ALLOWED_FLAG = 'N'` impede lançamentos diretos — usado para contas de controle.
- Esta tabela é **compartilhada** por todo o ERP — qualquer mudança impacta todos os módulos.

---

## 🔗 PVOs Relacionados

### [[codecombinationextractpvo|CodeCombinationExtractPVO]] (OTHER · BICC: 49/60)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_TYPE | CodeCombinationAccountType | ✅ |
| ALTERNATE_CODE_COMBINATION_ID | CodeCombinationAlternateCodeCombinationId | ✅ |
| ATTRIBUTE1 | CodeCombinationAttribute1 | — |
| ATTRIBUTE10 | CodeCombinationAttribute10 | — |
| ATTRIBUTE2 | CodeCombinationAttribute2 | — |
| ATTRIBUTE3 | CodeCombinationAttribute3 | — |
| ATTRIBUTE4 | CodeCombinationAttribute4 | — |
| ATTRIBUTE5 | CodeCombinationAttribute5 | — |
| ATTRIBUTE6 | CodeCombinationAttribute6 | — |
| ATTRIBUTE7 | CodeCombinationAttribute7 | — |
| ATTRIBUTE8 | CodeCombinationAttribute8 | — |
| ATTRIBUTE9 | CodeCombinationAttribute9 | — |
| ATTRIBUTE_CATEGORY | CodeCombinationAttributeCategory | — |
| CHART_OF_ACCOUNTS_ID | CodeCombinationChartOfAccountsId | ✅ |
| CODE_COMBINATION_ID | CodeCombinationCodeCombinationId | ✅ |
| CREATED_BY | CodeCombinationCreatedBy | ✅ |
| CREATION_DATE | CodeCombinationCreationDate | ✅ |
| DETAIL_BUDGETING_ALLOWED_FLAG | CodeCombinationDetailBudgetingAllowedFlag | ✅ |
| DETAIL_POSTING_ALLOWED_FLAG | CodeCombinationDetailPostingAllowedFlag | ✅ |
| ENABLED_FLAG | CodeCombinationEnabledFlag | ✅ |
| END_DATE_ACTIVE | CodeCombinationEndDateActive | ✅ |
| FINANCIAL_CATEGORY | CodeCombinationFinancialCategory | ✅ |
| JGZZ_RECON_FLAG | CodeCombinationJgzzReconFlag | ✅ |
| LAST_UPDATE_DATE | CodeCombinationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CodeCombinationLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CodeCombinationLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | CodeCombinationObjectVersionNumber | ✅ |
| PRESERVE_FLAG | CodeCombinationPreserveFlag | ✅ |
| SEGMENT1 | CodeCombinationSegment1 | ✅ |
| SEGMENT10 | CodeCombinationSegment10 | ✅ |
| SEGMENT11 | CodeCombinationSegment11 | ✅ |
| SEGMENT12 | CodeCombinationSegment12 | ✅ |
| SEGMENT13 | CodeCombinationSegment13 | ✅ |
| SEGMENT14 | CodeCombinationSegment14 | ✅ |
| SEGMENT15 | CodeCombinationSegment15 | ✅ |
| SEGMENT16 | CodeCombinationSegment16 | ✅ |
| SEGMENT17 | CodeCombinationSegment17 | ✅ |
| SEGMENT18 | CodeCombinationSegment18 | ✅ |
| SEGMENT19 | CodeCombinationSegment19 | ✅ |
| SEGMENT2 | CodeCombinationSegment2 | ✅ |
| SEGMENT20 | CodeCombinationSegment20 | ✅ |
| SEGMENT21 | CodeCombinationSegment21 | ✅ |
| SEGMENT22 | CodeCombinationSegment22 | ✅ |
| SEGMENT23 | CodeCombinationSegment23 | ✅ |
| SEGMENT24 | CodeCombinationSegment24 | ✅ |
| SEGMENT25 | CodeCombinationSegment25 | ✅ |
| SEGMENT26 | CodeCombinationSegment26 | ✅ |
| SEGMENT27 | CodeCombinationSegment27 | ✅ |
| SEGMENT28 | CodeCombinationSegment28 | ✅ |
| SEGMENT29 | CodeCombinationSegment29 | ✅ |
| SEGMENT3 | CodeCombinationSegment3 | ✅ |
| SEGMENT30 | CodeCombinationSegment30 | ✅ |
| SEGMENT4 | CodeCombinationSegment4 | ✅ |
| SEGMENT5 | CodeCombinationSegment5 | ✅ |
| SEGMENT6 | CodeCombinationSegment6 | ✅ |
| SEGMENT7 | CodeCombinationSegment7 | ✅ |
| SEGMENT8 | CodeCombinationSegment8 | ✅ |
| SEGMENT9 | CodeCombinationSegment9 | ✅ |
| START_DATE_ACTIVE | CodeCombinationStartDateActive | ✅ |
| SUMMARY_FLAG | CodeCombinationSummaryFlag | ✅ |

### [[codecombinationpvo|CodeCombinationPVO]] (GL · BICC: 14/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_TYPE | CodeCombinationAccountType | ✅ |
| ALLOCATION_CREATE_FLAG | CodeCombinationAllocationCreateFlag | — |
| ALTERNATE_CODE_COMBINATION_ID | CodeCombinationAlternateCodeCombinationId | ✅ |
| CHART_OF_ACCOUNTS_ID | CodeCombinationChartOfAccountsId | ✅ |
| CODE_COMBINATION_ID | CodeCombinationId | ✅ |
| COMPANY_COST_CENTER_ORG_ID | CodeCombinationCompanyCostCenterOrgId | ✅ |
| CREATED_BY | CodeCombinationCreatedBy | ✅ |
| CREATION_DATE | CodeCombinationCreationDate | ✅ |
| DETAIL_BUDGETING_ALLOWED_FLAG | CodeCombinationDetailBudgetingAllowedFlag | — |
| DETAIL_POSTING_ALLOWED_FLAG | CodeCombinationDetailPostingAllowedFlag | — |
| ENABLED_FLAG | CodeCombinationEnabledFlag | ✅ |
| END_DATE_ACTIVE | CodeCombinationEndDateActive | ✅ |
| FINANCIAL_CATEGORY | CodeCombinationFinancialCategory | ✅ |
| IGI_BALANCED_BUDGET_FLAG | CodeCombinationIgiBalancedBudgetFlag | — |
| JGZZ_RECON_CONTEXT | CodeCombinationJgzzReconContext | — |
| JGZZ_RECON_FLAG | CodeCombinationJgzzReconFlag | — |
| LAST_UPDATE_DATE | CodeCombinationLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CodeCombinationLastUpdateLogin | — |
| LAST_UPDATED_BY | CodeCombinationLastUpdatedBy | ✅ |
| LEDGER_SEGMENT | CodeCombinationLedgerSegment | — |
| LEDGER_TYPE_CODE | CodeCombinationLedgerTypeCode | — |
| OBJECT_VERSION_NUMBER | CodeCombinationObjectVersionNumber | — |
| PRESERVE_FLAG | CodeCombinationPreserveFlag | — |
| REFERENCE1 | CodeCombinationReference1 | — |
| REFERENCE2 | CodeCombinationReference2 | — |
| REFERENCE3 | CodeCombinationReference3 | — |
| REFERENCE4 | CodeCombinationReference4 | — |
| REFERENCE5 | CodeCombinationReference5 | — |
| REFRESH_FLAG | CodeCombinationRefreshFlag | — |
| REVALUATION_ID | CodeCombinationRevaluationId | — |
| SEGMENT1 | CodeCombinationSegment1 | — |
| SEGMENT10 | CodeCombinationSegment10 | — |
| SEGMENT11 | CodeCombinationSegment11 | — |
| SEGMENT12 | CodeCombinationSegment12 | — |
| SEGMENT13 | CodeCombinationSegment13 | — |
| SEGMENT14 | CodeCombinationSegment14 | — |
| SEGMENT15 | CodeCombinationSegment15 | — |
| SEGMENT16 | CodeCombinationSegment16 | — |
| SEGMENT17 | CodeCombinationSegment17 | — |
| SEGMENT18 | CodeCombinationSegment18 | — |
| SEGMENT19 | CodeCombinationSegment19 | — |
| SEGMENT2 | CodeCombinationSegment2 | — |
| SEGMENT20 | CodeCombinationSegment20 | — |
| SEGMENT21 | CodeCombinationSegment21 | — |
| SEGMENT22 | CodeCombinationSegment22 | — |
| SEGMENT23 | CodeCombinationSegment23 | — |
| SEGMENT24 | CodeCombinationSegment24 | — |
| SEGMENT25 | CodeCombinationSegment25 | — |
| SEGMENT26 | CodeCombinationSegment26 | — |
| SEGMENT27 | CodeCombinationSegment27 | — |
| SEGMENT28 | CodeCombinationSegment28 | — |
| SEGMENT29 | CodeCombinationSegment29 | — |
| SEGMENT3 | CodeCombinationSegment3 | — |
| SEGMENT30 | CodeCombinationSegment30 | — |
| SEGMENT4 | CodeCombinationSegment4 | — |
| SEGMENT5 | CodeCombinationSegment5 | — |
| SEGMENT6 | CodeCombinationSegment6 | — |
| SEGMENT7 | CodeCombinationSegment7 | — |
| SEGMENT8 | CodeCombinationSegment8 | — |
| SEGMENT9 | CodeCombinationSegment9 | — |
| SEGMENT_ATTRIBUTE1 | CodeCombinationSegmentAttribute1 | — |
| SEGMENT_ATTRIBUTE10 | CodeCombinationSegmentAttribute10 | — |
| SEGMENT_ATTRIBUTE11 | CodeCombinationSegmentAttribute11 | — |
| SEGMENT_ATTRIBUTE12 | CodeCombinationSegmentAttribute12 | — |
| SEGMENT_ATTRIBUTE13 | CodeCombinationSegmentAttribute13 | — |
| SEGMENT_ATTRIBUTE14 | CodeCombinationSegmentAttribute14 | — |
| SEGMENT_ATTRIBUTE15 | CodeCombinationSegmentAttribute15 | — |
| SEGMENT_ATTRIBUTE16 | CodeCombinationSegmentAttribute16 | — |
| SEGMENT_ATTRIBUTE17 | CodeCombinationSegmentAttribute17 | — |
| SEGMENT_ATTRIBUTE18 | CodeCombinationSegmentAttribute18 | — |
| SEGMENT_ATTRIBUTE19 | CodeCombinationSegmentAttribute19 | — |
| SEGMENT_ATTRIBUTE2 | CodeCombinationSegmentAttribute2 | — |
| SEGMENT_ATTRIBUTE20 | CodeCombinationSegmentAttribute20 | — |
| SEGMENT_ATTRIBUTE21 | CodeCombinationSegmentAttribute21 | — |
| SEGMENT_ATTRIBUTE22 | CodeCombinationSegmentAttribute22 | — |
| SEGMENT_ATTRIBUTE23 | CodeCombinationSegmentAttribute23 | — |
| SEGMENT_ATTRIBUTE24 | CodeCombinationSegmentAttribute24 | — |
| SEGMENT_ATTRIBUTE25 | CodeCombinationSegmentAttribute25 | — |
| SEGMENT_ATTRIBUTE26 | CodeCombinationSegmentAttribute26 | — |
| SEGMENT_ATTRIBUTE27 | CodeCombinationSegmentAttribute27 | — |
| SEGMENT_ATTRIBUTE28 | CodeCombinationSegmentAttribute28 | — |
| SEGMENT_ATTRIBUTE29 | CodeCombinationSegmentAttribute29 | — |
| SEGMENT_ATTRIBUTE3 | CodeCombinationSegmentAttribute3 | — |
| SEGMENT_ATTRIBUTE30 | CodeCombinationSegmentAttribute30 | — |
| SEGMENT_ATTRIBUTE31 | CodeCombinationSegmentAttribute31 | — |
| SEGMENT_ATTRIBUTE32 | CodeCombinationSegmentAttribute32 | — |
| SEGMENT_ATTRIBUTE33 | CodeCombinationSegmentAttribute33 | — |
| SEGMENT_ATTRIBUTE34 | CodeCombinationSegmentAttribute34 | — |
| SEGMENT_ATTRIBUTE35 | CodeCombinationSegmentAttribute35 | — |
| SEGMENT_ATTRIBUTE36 | CodeCombinationSegmentAttribute36 | — |
| SEGMENT_ATTRIBUTE37 | CodeCombinationSegmentAttribute37 | — |
| SEGMENT_ATTRIBUTE38 | CodeCombinationSegmentAttribute38 | — |
| SEGMENT_ATTRIBUTE39 | CodeCombinationSegmentAttribute39 | — |
| SEGMENT_ATTRIBUTE4 | CodeCombinationSegmentAttribute4 | — |
| SEGMENT_ATTRIBUTE40 | CodeCombinationSegmentAttribute40 | — |
| SEGMENT_ATTRIBUTE41 | CodeCombinationSegmentAttribute41 | — |
| SEGMENT_ATTRIBUTE42 | CodeCombinationSegmentAttribute42 | — |
| SEGMENT_ATTRIBUTE5 | CodeCombinationSegmentAttribute5 | — |
| SEGMENT_ATTRIBUTE6 | CodeCombinationSegmentAttribute6 | — |
| SEGMENT_ATTRIBUTE7 | CodeCombinationSegmentAttribute7 | — |
| SEGMENT_ATTRIBUTE8 | CodeCombinationSegmentAttribute8 | — |
| SEGMENT_ATTRIBUTE9 | CodeCombinationSegmentAttribute9 | — |
| START_DATE_ACTIVE | CodeCombinationStartDateActive | ✅ |
| SUMMARY_FLAG | CodeCombinationSummaryFlag | ✅ |
| TEMPLATE_ID | CodeCombinationTemplateId | — |

### [[referenceaccount|ReferenceAccount]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE_COMBINATION_ID | CodeCombinationClearingCodeCombinationId | — |
| CODE_COMBINATION_ID | CodeCombinationFreightCodeCombinationId | — |
| CODE_COMBINATION_ID | CodeCombinationRecCodeCombinationId | — |
| CODE_COMBINATION_ID | CodeCombinationRevCodeCombinationId | — |
| CODE_COMBINATION_ID | CodeCombinationTaxCodeCombinationId | — |
| CODE_COMBINATION_ID | CodeCombinationUnbilledCodeCombinationId | — |
| CODE_COMBINATION_ID | CodeCombinationUnearnedCodeCombinationId | — |

### [[subledgercontrolbalancepvo|SubledgerControlBalancePVO]] (GL · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_TYPE | CodeCombinationAccountType | ✅ |
| ALLOCATION_CREATE_FLAG | CodeCombinationAllocationCreateFlag | ✅ |
| ALTERNATE_CODE_COMBINATION_ID | CodeCombinationAlternateCodeCombinationId | ✅ |
| CHART_OF_ACCOUNTS_ID | CodeCombinationChartOfAccountsId | ✅ |
| CODE_COMBINATION_ID | CodeCombinationCodeCombinationId | ✅ |
| FINANCIAL_CATEGORY | CodeCombinationFinancialCategory | ✅ |
| LEDGER_SEGMENT | CodeCombinationLedgerSegment | ✅ |
| LEDGER_TYPE_CODE | CodeCombinationLedgerTypeCode | ✅ |
| OBJECT_VERSION_NUMBER | CodeCombinationObjectVersionNumber | ✅ |
| REVALUATION_ID | CodeCombinationRevaluationId | ✅ |
| START_DATE_ACTIVE | CodeCombinationStartDateActive | ✅ |
| TEMPLATE_ID | CodeCombinationTemplateId | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL_CODE_COMBINATIONS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glcodecombinations-25012.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
