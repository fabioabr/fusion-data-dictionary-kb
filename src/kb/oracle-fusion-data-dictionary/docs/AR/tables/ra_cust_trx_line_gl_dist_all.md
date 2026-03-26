---
id: DOC-AR-003
doc_type: system-doc
title: "RA_CUST_TRX_LINE_GL_DIST_ALL — Distribuições Contábeis AR"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - distribuicoes-contabeis
  - reconciliacao-gl
  - accounting
aliases:
  - RA_CUST_TRX_LINE_GL_DIST_ALL
  - ra_cust_trx_line_gl_dist_all
  - distribuicoes-ar
  - ar-gl-distributions
  - dist-contabeis-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUST_TRX_LINE_GL_DIST_ALL

## 📌 Visão Geral

Armazena as **distribuições contábeis** (accounting distributions) das linhas de transação do módulo Accounts Receivable. Liga cada linha de transação às combinações de contas contábeis do General Ledger, permitindo a reconciliação entre AR e GL. Cada linha de transação pode ter múltiplas distribuições, categorizadas por `ACCOUNT_CLASS` (receita, recebível, frete, imposto, etc.).

É a tabela que faz a **ponte entre AR e GL** — indispensável para auditoria contábil e reconciliação de saldos.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reconciliação AR × GL:** Cada valor de transação é distribuído para contas contábeis específicas, permitindo conferência entre saldos do subledger e do General Ledger.
- **Análise de receita por conta contábil:** Identificação de receita por centro de custo, departamento ou segmento contábil.
- **Auditoria de lançamentos:** Rastreamento completo de quais contas foram impactadas por cada transação.
- **Posting para GL:** O campo `GL_POSTED_DATE` indica quando a distribuição foi transferida ao General Ledger.
- **Revenue scheduling:** Distribuições com `ACCOUNT_CLASS = 'UNEARN'` ou `'UNBILL'` suportam reconhecimento de receita diferido.
- **AutoAccounting:** As contas são determinadas automaticamente com base nas regras de AutoAccounting configuradas no tipo de transação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUST_TRX_LINE_GL_DIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da distribuição contábil | — | 🟢 100% |
| 2 | CUSTOMER_TRX_LINE_ID | NUMBER(18) | NULL | FK | Referência à linha da transação | [[ra_customer_trx_lines_all]] | 🟢 100% |
| 3 | CUSTOMER_TRX_ID | NUMBER(18) | NOT NULL | FK | Referência ao cabeçalho da transação | [[ra_customer_trx_all]] | 🟢 100% |
| 4 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Combinação de contas contábeis (segmentos GL) | [[gl_code_combinations]] | 🟢 100% |
| 5 | AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição na moeda da transação | — | 🟢 100% |
| 6 | ACCTD_AMOUNT | NUMBER | NULL | Financeiro | Valor da distribuição na moeda funcional (ledger) | — | 🟢 100% |
| 7 | PERCENT | NUMBER | NULL | Financeiro | Percentual da distribuição em relação ao total da linha | — | 🟢 100% |
| 8 | ACCOUNT_CLASS | VARCHAR2(20) | NOT NULL | Classificação | Classe da conta: REV, REC, FREIGHT, TAX, UNBILL, UNEARN, SUSPENSE, ROUND | — | 🟢 100% |
| 9 | ACCOUNT_SET_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Y = modelo de conta (template); N = distribuição real | — | 🟢 100% |
| 10 | GL_DATE | DATE | NULL | Contabilidade | Data contábil da distribuição (período GL) | — | 🟢 100% |
| 11 | GL_POSTED_DATE | DATE | NULL | Contabilidade | Data em que foi postada no General Ledger | — | 🟢 100% |
| 12 | POSTING_CONTROL_ID | NUMBER(18) | NULL | Contabilidade | ID do controle de posting (-1 = não postado, -2 = não precisa postar, >0 = postado) | — | 🟢 100% |
| 13 | LATEST_REC_FLAG | VARCHAR2(1) | NULL | Classificação | Y = distribuição mais recente do recebível (para ACCOUNT_CLASS = REC) | — | 🟢 100% |
| 14 | ORIGINAL_GL_DATE | DATE | NULL | Contabilidade | Data GL original (antes de repostagem) | — | 🟢 100% |
| 15 | CUST_TRX_TYPE_ID | NUMBER(18) | NULL | Classificação | Tipo da transação (desnormalizado do cabeçalho) | [[ra_cust_trx_types_all]] | 🟢 100% |
| 16 | COLLECTED_TAX_CCID | NUMBER(18) | NULL | Tributação | Combinação de contas para imposto coletado | [[gl_code_combinations]] | 🟡 70% |
| 17 | COLLECTED_TAX_CONCAT_SEG | VARCHAR2(240) | NULL | Tributação | Segmentos concatenados da conta de imposto coletado | — | 🟡 65% |
| 18 | REVENUE_ADJUSTMENT_ID | NUMBER(18) | NULL | Contabilidade | ID do ajuste de receita (Revenue Adjustment) | — | 🟢 100% |
| 19 | REC_OFFSET_FLAG | VARCHAR2(1) | NULL | Classificação | Flag de offset do recebível | — | 🟡 65% |
| 20 | EVENT_ID | NUMBER(18) | NULL | Contabilidade | ID do evento contábil (Subledger Accounting / SLA) | — | 🟢 100% |
| 21 | USER_GENERATED_FLAG | VARCHAR2(1) | NULL | Classificação | Y = distribuição criada manualmente pelo usuário | — | 🟢 100% |
| 22 | ROUNDING_CORRECTION_FLAG | VARCHAR2(1) | NULL | Classificação | Y = distribuição de correção de arredondamento | — | 🟢 100% |
| 23 | CCID_CHANGE_FLAG | VARCHAR2(1) | NULL | Classificação | Y = conta contábil foi alterada manualmente | — | 🟡 70% |
| 24 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado) | [[gl_ledgers]] | 🟢 100% |
| 25 | COMMENTS | VARCHAR2(240) | NULL | Texto livre | Comentários da distribuição | — | 🟢 100% |
| 26 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 27 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 28 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 29 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 30 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 31 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 32 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 33 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_customer_trx_all]] — via `CUSTOMER_TRX_ID` (cabeçalho da transação)
- [[ra_customer_trx_lines_all]] — via `CUSTOMER_TRX_LINE_ID` (linha da transação)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil da distribuição da linha de transação)
- [[ra_cust_trx_types_all]] — via `CUST_TRX_TYPE_ID` (tipo da transação)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da distribuição contábil da transação)

### Tabelas-filha (FK de saída)
- [[xla_ae_lines]] — via `EVENT_ID` (linhas de diário do Subledger Accounting)
- [[xla_events]] — via `EVENT_ID` (eventos contábeis SLA)

---

## 📎 Uso Típico

### Reconciliação AR × GL por conta contábil
```sql
SELECT gcc.SEGMENT1 || '-' || gcc.SEGMENT2 || '-' || gcc.SEGMENT3 AS conta,
       dist.ACCOUNT_CLASS,
       SUM(dist.ACCTD_AMOUNT) AS total_funcional
FROM   RA_CUST_TRX_LINE_GL_DIST_ALL dist
JOIN   GL_CODE_COMBINATIONS gcc
       ON gcc.CODE_COMBINATION_ID = dist.CODE_COMBINATION_ID
WHERE  dist.GL_DATE BETWEEN :start_date AND :end_date
  AND  dist.ACCOUNT_SET_FLAG = 'N'
  AND  dist.ORG_ID = :p_org_id
GROUP BY gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3, dist.ACCOUNT_CLASS;
```

### Distribuições não postadas no GL
```sql
SELECT ct.TRX_NUMBER, dist.GL_DATE, dist.ACCOUNT_CLASS,
       dist.AMOUNT, dist.POSTING_CONTROL_ID
FROM   RA_CUST_TRX_LINE_GL_DIST_ALL dist
JOIN   RA_CUSTOMER_TRX_ALL ct
       ON ct.CUSTOMER_TRX_ID = dist.CUSTOMER_TRX_ID
WHERE  dist.POSTING_CONTROL_ID = -1
  AND  dist.ACCOUNT_SET_FLAG = 'N'
  AND  dist.ORG_ID = :p_org_id;
```

### Filtros comuns
- `ACCOUNT_SET_FLAG = 'N'` — Apenas distribuições reais (excluir templates)
- `ACCOUNT_CLASS = 'REV'` — Apenas distribuições de receita
- `ACCOUNT_CLASS = 'REC'` — Apenas distribuições de recebível
- `POSTING_CONTROL_ID = -1` — Distribuições ainda não postadas no GL
- `LATEST_REC_FLAG = 'Y'` — Distribuição de recebível mais recente (evitar duplicidade)

---

## 🔒 Observações

- O campo `ACCOUNT_SET_FLAG` é crítico: registros com valor `'Y'` são **templates** usados pelo AutoAccounting e **não representam valores reais**. Sempre filtrar `ACCOUNT_SET_FLAG = 'N'` em consultas de valores.
- O `POSTING_CONTROL_ID` segue a convenção: `-1` = não postado, `-2` = não precisa postar (e.g., tipo de transação com `POST_TO_GL = 'N'`), valores positivos = ID do batch de posting.
- Para `ACCOUNT_CLASS = 'REC'`, usar `LATEST_REC_FLAG = 'Y'` para obter apenas a distribuição mais recente do recebível (evita dupla contagem após aplicações parciais).
- Distribuições com `ACCOUNT_CLASS` em `'UNBILL'` ou `'UNEARN'` estão relacionadas ao **revenue scheduling** e devem ser consideradas em análises de receita diferida.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15`.

---

## 📚 Referências

- [Oracle Docs — RA_CUST_TRX_LINE_GL_DIST_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racusttrxlinegldistall-25198.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
