---
id: DOC-GL-024
doc_type: system-doc
title: "GL_JE_LINES_RECON — Reconciliação de Linhas de Lançamentos"
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
  - reconciliation
  - journal-lines
  - reconciliacao
aliases:
  - GL_JE_LINES_RECON
  - gl_je_lines_recon
  - reconciliacao-linhas
  - journal-reconciliation
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_LINES_RECON

## 📌 Visão Geral

Armazena informações de **reconciliação de linhas de lançamentos contábeis** no General Ledger. Esta tabela registra o status e os detalhes de reconciliação de cada linha de journal, permitindo identificar quais linhas já foram reconciliadas, por quem e quando. É utilizada pelo recurso de Journal Reconciliation do Oracle Fusion GL.

> [!note] Tabela auxiliar de reconciliação
> Nem todas as linhas de journal possuem registro nesta tabela — apenas aquelas cujas contas estão habilitadas para reconciliação (`JGZ_RECONCILIATION_FLAG` em [[gl_code_combinations]]).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reconciliação contábil:** Marcação de linhas de journal como reconciliadas.
- **Auditoria:** Rastreamento de quem reconciliou cada lançamento e quando.
- **Controle de fechamento:** Identificação de linhas pendentes de reconciliação no encerramento do período.
- **Contas de clearing:** Monitoramento de contas de compensação (clearing accounts) que devem ter saldo zero.
- **Compliance:** Evidência de revisão contábil para fins regulatórios.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_HEADER_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do header do journal entry | [[gl_je_headers]] | 🟢 95% |
| 2 | JE_LINE_NUM | NUMBER(18) | NOT NULL | FK/PK | Número sequencial da linha do journal | [[gl_je_lines]] | 🟢 95% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 90% |
| 4 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | FK | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 90% |
| 5 | RECONCILIATION_ID | NUMBER(18) | NULL | PK | Identificador único da reconciliação | — | 🟡 75% |
| 6 | RECONCILIATION_DATE | DATE | NULL | Controle | Data em que a linha foi reconciliada | — | 🟡 80% |
| 7 | RECONCILIATION_STATUS | VARCHAR2(1) | NULL | Controle | Status de reconciliação: R (Reconciled), N (Not Reconciled), U (Unreconciled) | — | 🟡 75% |
| 8 | RECONCILIATION_REFERENCE | VARCHAR2(240) | NULL | Referência | Referência textual associada à reconciliação | — | 🟡 70% |
| 9 | JGZZ_RECON_REF | VARCHAR2(240) | NULL | Referência | Referência de reconciliação (localização/GDF) | — | 🟡 70% |
| 10 | JGZZ_RECON_ID | NUMBER(18) | NULL | FK | ID da referência de reconciliação (localização) | — | 🟡 65% |
| 11 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Nome do período contábil | — | 🟢 90% |
| 12 | ENTERED_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda da transação | — | 🟡 80% |
| 13 | ENTERED_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda da transação | — | 🟡 80% |
| 14 | ACCOUNTED_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda funcional | — | 🟡 80% |
| 15 | ACCOUNTED_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda funcional | — | 🟡 80% |
| 16 | CURRENCY_CODE | VARCHAR2(15) | NULL | Classificação | Código da moeda da transação | — | 🟡 80% |
| 17 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 18 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 19 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 20 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_lines]] — via `JE_HEADER_ID` + `JE_LINE_NUM` (linha do journal)
- [[gl_je_headers]] — via `JE_HEADER_ID` (header do journal)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger da linha de reconciliação contábil)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (combinação de contas)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela auxiliar de reconciliação (leaf table).

---

## 📎 Uso Típico

### Linhas pendentes de reconciliação em uma conta
```sql
SELECT jl.JE_HEADER_ID,
       jl.JE_LINE_NUM,
       jl.EFFECTIVE_DATE,
       jl.ENTERED_DR,
       jl.ENTERED_CR,
       jl.DESCRIPTION,
       jr.RECONCILIATION_STATUS
FROM   GL_JE_LINES jl
LEFT JOIN GL_JE_LINES_RECON jr
       ON jr.JE_HEADER_ID = jl.JE_HEADER_ID
      AND jr.JE_LINE_NUM = jl.JE_LINE_NUM
WHERE  jl.CODE_COMBINATION_ID = :p_ccid
  AND  jl.LEDGER_ID = :p_ledger_id
  AND  (jr.RECONCILIATION_STATUS IS NULL OR jr.RECONCILIATION_STATUS = 'N')
ORDER BY jl.EFFECTIVE_DATE;
```

### Histórico de reconciliação por período
```sql
SELECT jr.PERIOD_NAME,
       COUNT(*) AS total_linhas,
       SUM(CASE WHEN jr.RECONCILIATION_STATUS = 'R' THEN 1 ELSE 0 END) AS reconciliadas,
       SUM(CASE WHEN jr.RECONCILIATION_STATUS != 'R' OR jr.RECONCILIATION_STATUS IS NULL THEN 1 ELSE 0 END) AS pendentes
FROM   GL_JE_LINES_RECON jr
WHERE  jr.LEDGER_ID = :p_ledger_id
GROUP BY jr.PERIOD_NAME
ORDER BY jr.PERIOD_NAME;
```

### Filtros comuns
- `RECONCILIATION_STATUS = 'R'` — Linhas reconciliadas
- `RECONCILIATION_STATUS = 'N'` — Linhas não reconciliadas
- `RECONCILIATION_DATE IS NULL` — Linhas ainda não processadas

---

## 🔒 Observações

- Apenas contas habilitadas para reconciliação (flag na [[gl_code_combinations]]) geram registros nesta tabela.
- A reconciliação é tipicamente usada para contas de clearing/compensação e contas intercompany.
- Os campos `JGZZ_*` são específicos de localizações regionais (Global Descriptive Flexfield) e podem não estar populados em todas as implementações.
- O processo de reconciliação pode ser manual (pelo usuário) ou automático (via regras configuradas no GL).
- Esta tabela é essencial para o processo de fechamento contábil — contas com linhas não reconciliadas podem bloquear o fechamento.

---

## 🔗 PVOs Relacionados

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JE_HEADER_ID | JrnlReconLineJeHeaderId | — |
| JE_LINE_NUM | JrnlReconLineJeLineNum | — |
| JGZZ_RECON_DATE | JrnlReconLineJgzzReconDate | ✅ |
| JGZZ_RECON_ID | JrnlReconLineJgzzReconId | ✅ |
| JGZZ_RECON_REF | JrnlReconLineJgzzReconRef | ✅ |
| JGZZ_RECON_STATUS | JrnlReconLineJgzzReconStatus | ✅ |

### [[journalreconlineextractpvo|JournalReconLineExtractPVO]] (OTHER · BICC: 14/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GlJeLinesReconCreatedBy | ✅ |
| CREATION_DATE | GlJeLinesReconCreationDate | ✅ |
| JE_HEADER_ID | GlJeLinesReconJeHeaderId | ✅ |
| JE_LINE_NUM | GlJeLinesReconJeLineNum | ✅ |
| JGZZ_RECON_DATE | GlJeLinesReconJgzzReconDate | ✅ |
| JGZZ_RECON_ID | GlJeLinesReconJgzzReconId | ✅ |
| JGZZ_RECON_REF | GlJeLinesReconJgzzReconRef | ✅ |
| JGZZ_RECON_STATUS | GlJeLinesReconJgzzReconStatus | ✅ |
| LAST_UPDATE_DATE | GlJeLinesReconLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlJeLinesReconLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GlJeLinesReconLastUpdatedBy | ✅ |
| LEDGER_ID | GlJeLinesReconLedgerId | ✅ |
| OBJECT_VERSION_NUMBER | GlJeLinesReconObjectVersionNumber | ✅ |
| RECON_RULE_ID | GlJeLinesReconReconRuleId | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL_JE_LINES_RECON](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljelinesrecon.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
