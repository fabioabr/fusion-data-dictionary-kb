---
id: DOC-AR-005
doc_type: system-doc
title: "RA_CUST_TRX_TYPES_ALL — Tipos de Transação AR"
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
  - tipos-transacao
  - configuracao
  - autoaccounting
aliases:
  - RA_CUST_TRX_TYPES_ALL
  - ra_cust_trx_types_all
  - tipos-transacao-ar
  - ar-transaction-types
  - trx-types-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUST_TRX_TYPES_ALL

## 📌 Visão Geral

Define os **tipos de transação** utilizados para faturas, notas de débito, notas de crédito, depósitos, garantias e duplicatas a receber (bills receivable) no módulo Accounts Receivable. Cada registro inclui configurações de **AutoAccounting** (contas contábeis padrão), comportamento de impressão, sinais contábeis e valores padrão para criação de transações.

É a tabela de **configuração central do AR** — determina como cada transação se comporta contabilmente e operacionalmente.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de transações:** Cada transação AR é associada a um tipo que define seu comportamento (fatura, credit memo, debit memo, etc.).
- **AutoAccounting:** Contas contábeis padrão (receita, recebível, frete, imposto, unbilled, unearned) são definidas por tipo de transação.
- **Regras de contabilização:** Controla se a transação será postada no GL (`POST_TO_GL`), se afeta saldo contábil, e qual o sinal de criação (positivo/negativo).
- **Impressão e comunicação:** Define opções padrão de impressão para faturas.
- **Filtros em relatórios:** Permite segmentar relatórios por tipo de transação (e.g., apenas credit memos).
- **Controle de funcionalidades:** Flags como `ALLOW_FREIGHT_FLAG`, `NATURAL_APPLICATION_ONLY_FLAG` controlam comportamentos específicos por tipo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUST_TRX_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de transação | — | 🟢 100% |
| 2 | NAME | VARCHAR2(20) | NOT NULL | Identificação | Nome do tipo de transação (visível ao usuário) | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(80) | NULL | Identificação | Descrição detalhada do tipo de transação | — | 🟢 100% |
| 4 | TYPE | VARCHAR2(20) | NOT NULL | Classificação | Categoria principal: INV, CM, DM, DEP, GUAR, BR | — | 🟢 100% |
| 5 | CLASS | VARCHAR2(20) | NULL | Classificação | Classe da transação (INV, CM, DM, DEP, GUAR, BR) | — | 🟢 100% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do tipo (ativo/inativo) | — | 🟢 100% |
| 7 | POST_TO_GL | VARCHAR2(1) | NOT NULL | Contabilidade | Indica se transações deste tipo são postadas no GL (Y/N) | — | 🟢 100% |
| 8 | ACCOUNTING_AFFECT_FLAG | VARCHAR2(1) | NOT NULL | Contabilidade | Indica se afeta saldos contábeis (Y/N) | — | 🟢 100% |
| 9 | CREATION_SIGN | VARCHAR2(30) | NULL | Contabilidade | Sinal de criação: P (positivo), N (negativo), A (ambos) | — | 🟢 100% |
| 10 | ALLOW_FREIGHT_FLAG | VARCHAR2(1) | NULL | Configuração | Permite linhas de frete (Y/N) | — | 🟢 100% |
| 11 | ALLOW_OVERAPPLICATION_FLAG | VARCHAR2(1) | NULL | Configuração | Permite aplicação acima do saldo (Y/N) | — | 🟢 100% |
| 12 | NATURAL_APPLICATION_ONLY_FLAG | VARCHAR2(1) | NULL | Configuração | Restringe a aplicações naturais — invoice:receipt, CM:invoice (Y/N) | — | 🟢 100% |
| 13 | TAX_CALCULATION_FLAG | VARCHAR2(1) | NULL | Tributação | Indica se calcula imposto automaticamente (Y/N) | — | 🟢 100% |
| 14 | DEFAULT_TERM | NUMBER(18) | NULL | Financeiro | Condição de pagamento padrão | [[ra_terms_b]] | 🟢 100% |
| 15 | DEFAULT_PRINTING_OPTION | VARCHAR2(30) | NULL | Impressão | Opção de impressão padrão (PRI/NOT) | — | 🟢 100% |
| 16 | DEFAULT_STATUS | VARCHAR2(30) | NULL | Configuração | Status padrão para novas transações (OP=Open) | — | 🟢 100% |
| 17 | GL_ID_REV | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Receita | [[gl_code_combinations]] | 🟢 100% |
| 18 | GL_ID_REC | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Recebível | [[gl_code_combinations]] | 🟢 100% |
| 19 | GL_ID_FREIGHT | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Frete | [[gl_code_combinations]] | 🟢 100% |
| 20 | GL_ID_TAX | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Imposto | [[gl_code_combinations]] | 🟢 100% |
| 21 | GL_ID_UNBILLED | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Unbilled Receivable | [[gl_code_combinations]] | 🟢 100% |
| 22 | GL_ID_UNEARNED | NUMBER(18) | NULL | AutoAccounting | Combinação de contas padrão para Unearned Revenue | [[gl_code_combinations]] | 🟢 100% |
| 23 | END_DATE | DATE | NULL | Configuração | Data de inativação do tipo de transação | — | 🟢 100% |
| 24 | START_DATE | DATE | NULL | Configuração | Data de ativação do tipo de transação | — | 🟢 100% |
| 25 | CREDIT_MEMO_TYPE_ID | NUMBER(18) | NULL | Referência cruzada | Tipo de credit memo padrão associado | self | 🟢 100% |
| 26 | SUBSEQUENT_TRX_TYPE_ID | NUMBER(18) | NULL | Referência cruzada | Tipo de transação subsequente (bills receivable) | self | 🟢 100% |
| 27 | RULE_SET_ID | NUMBER(18) | NULL | Configuração | Conjunto de regras de aplicação (matching rules) | — | 🟡 70% |
| 28 | SIGNED_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se requer assinatura (bills receivable) | — | 🟢 100% |
| 29 | DRAWEE_ISSUED_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se emitido pelo sacado (bills receivable) | — | 🟢 100% |
| 30 | MAGNETIC_FORMAT_CODE | VARCHAR2(30) | NULL | Configuração | Formato magnético para remessas bancárias | — | 🟡 65% |
| 31 | SET_OF_BOOKS_ID | NUMBER(18) | NULL | Contabilidade | Ledger contábil (legado) | [[gl_ledgers]] | 🟢 100% |
| 32 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 33 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 34 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 35 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 36 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 37 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 38 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 39 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_code_combinations]] — via `GL_ID_REV`, `GL_ID_REC`, `GL_ID_FREIGHT`, `GL_ID_TAX`, `GL_ID_UNBILLED`, `GL_ID_UNEARNED` (contas padrão de AutoAccounting)
- [[ra_terms_b]] — via `DEFAULT_TERM` (condição de pagamento padrão)
- [[gl_ledgers]] — via `SET_OF_BOOKS_ID` (ledger contábil)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do tipo de transação de AR)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `CUST_TRX_TYPE_ID` (transações que utilizam este tipo)
- [[ra_cust_trx_line_gl_dist_all]] — via `CUST_TRX_TYPE_ID` (distribuições contábeis, desnormalizado)

### Self-references
- `CREDIT_MEMO_TYPE_ID` — Tipo de credit memo padrão associado a este tipo de fatura
- `SUBSEQUENT_TRX_TYPE_ID` — Tipo de transação subsequente (usado em fluxos de bills receivable)

---

## 📎 Uso Típico

### Listar todos os tipos de transação ativos
```sql
SELECT CUST_TRX_TYPE_ID, NAME, DESCRIPTION, TYPE, CLASS,
       POST_TO_GL, CREATION_SIGN
FROM   RA_CUST_TRX_TYPES_ALL
WHERE  ORG_ID = :p_org_id
  AND  (END_DATE IS NULL OR END_DATE > SYSDATE)
ORDER BY TYPE, NAME;
```

### Transações por tipo (volume e valor)
```sql
SELECT tt.NAME AS tipo_transacao, tt.TYPE,
       COUNT(*) AS qtd_transacoes,
       SUM(ctl.EXTENDED_AMOUNT) AS valor_total
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_CUST_TRX_TYPES_ALL tt
       ON tt.CUST_TRX_TYPE_ID = ct.CUST_TRX_TYPE_ID
JOIN   RA_CUSTOMER_TRX_LINES_ALL ctl
       ON ctl.CUSTOMER_TRX_ID = ct.CUSTOMER_TRX_ID
       AND ctl.LINE_TYPE = 'LINE'
WHERE  ct.ORG_ID = :p_org_id
GROUP BY tt.NAME, tt.TYPE;
```

### Filtros comuns
- `TYPE = 'INV'` — Apenas tipos de fatura
- `TYPE = 'CM'` — Apenas tipos de credit memo
- `TYPE = 'DM'` — Apenas tipos de debit memo
- `TYPE = 'BR'` — Apenas tipos de bills receivable
- `POST_TO_GL = 'Y'` — Tipos que geram lançamento contábil

---

## 🔒 Observações

- A coluna `TYPE` define a categoria funcional: **INV** (Invoice), **CM** (Credit Memo), **DM** (Debit Memo), **DEP** (Deposit), **GUAR** (Guarantee), **BR** (Bills Receivable).
- `CREATION_SIGN` controla o sinal do valor: **P** = apenas positivos, **N** = apenas negativos, **A** = ambos. Credit memos tipicamente têm `CREATION_SIGN = 'A'` ou `'N'`.
- Os campos `GL_ID_*` definem as **contas de AutoAccounting** por tipo de transação. Essas contas servem como template para as distribuições contábeis em [[ra_cust_trx_line_gl_dist_all]].
- O campo `CREDIT_MEMO_TYPE_ID` permite que um tipo de fatura tenha um tipo de credit memo padrão associado, facilitando a criação de notas de crédito.
- Tipos de **Bills Receivable** utilizam campos específicos como `SIGNED_FLAG`, `DRAWEE_ISSUED_FLAG` e `MAGNETIC_FORMAT_CODE` para controle de duplicatas bancárias.
- A tabela possui **Descriptive Flexfields (DFF)** via `ATTRIBUTE1–15` para customizações por implementação.

---

## 📚 Referências

- [Oracle Docs — RA_CUST_TRX_TYPES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racusttrxtypesall-25250.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
