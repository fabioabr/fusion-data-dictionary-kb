---
id: DOC-AR-016
doc_type: system-doc
title: "RA_TERMS_VL — Condições de Pagamento (View Traduzida)"
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
  - payment-terms
  - view
  - multi-language
aliases:
  - RA_TERMS_VL
  - ra_terms_vl
  - condicoes-pagamento-view
  - payment-terms-view
  - termos-pagamento-traduzidos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_TERMS_VL

> [!important] VIEW — Objeto Não-Físico
> `RA_TERMS_VL` é uma **view** (não uma tabela física). Ela combina os dados base de [[ra_terms_b]] com as traduções de [[ra_terms_tl]], filtrando automaticamente pelo idioma da sessão do usuário (`USERENV('LANG')`). Não possui armazenamento próprio.

## 📌 Visão Geral

View que fornece uma **visão unificada das condições de pagamento com traduções** no idioma da sessão do usuário. Combina todas as colunas de [[ra_terms_b]] (dados estruturais: prazos, flags, datas de vigência) com as colunas traduzidas de [[ra_terms_tl]] (NAME e DESCRIPTION no idioma corrente).

É o **ponto de acesso recomendado** para consultas de condições de pagamento em interfaces, relatórios e integrações, pois abstrai a complexidade do padrão MLS (Multi-Language Support) da Oracle.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes cenários:

- **Interfaces de usuário (UI):** Todas as LOVs (List of Values) e telas do Oracle Fusion que exibem condições de pagamento consultam esta view.
- **Relatórios e BI:** Fonte padrão para relatórios que precisam exibir nomes de termos traduzidos.
- **Integrações:** APIs e web services que retornam dados de condições de pagamento utilizam esta view como base.
- **Consultas ad-hoc:** Ponto de partida simplificado para qualquer query que envolva condições de pagamento — dispensa o join manual entre `_B` e `_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TERM_ID | NUMBER(18) | NOT NULL | PK | Identificador único da condição de pagamento (de [[ra_terms_b]]) | — | 🟢 100% |
| 2 | NAME | VARCHAR2(15) | NOT NULL | Identificação | Nome da condição de pagamento **traduzido** no idioma da sessão (de [[ra_terms_tl]]) | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição detalhada **traduzida** no idioma da sessão (de [[ra_terms_tl]]) | — | 🟢 100% |
| 4 | DUE_CUTOFF_DAY | NUMBER | NULL | Configuração | Dia de corte para cálculo de vencimento (de [[ra_terms_b]]) | — | 🟢 100% |
| 5 | PRINTING_LEAD_DAYS | NUMBER | NULL | Impressão | Dias de antecedência para impressão (de [[ra_terms_b]]) | — | 🟢 100% |
| 6 | BASE_AMOUNT | NUMBER | NULL | Financeiro | Valor base para cálculo de percentuais nas parcelas (de [[ra_terms_b]]) | — | 🟢 100% |
| 7 | CALC_DISCOUNT_ON_LINES_FLAG | VARCHAR2(1) | NULL | Desconto | Calcular desconto sobre linhas (Y) ou total (N) (de [[ra_terms_b]]) | — | 🟢 100% |
| 8 | PARTIAL_DISCOUNT_FLAG | VARCHAR2(1) | NULL | Desconto | Permite desconto em pagamento parcial (Y/N) (de [[ra_terms_b]]) | — | 🟢 100% |
| 9 | FIRST_INSTALLMENT_CODE | VARCHAR2(12) | NULL | Configuração | Tratamento de residual na primeira parcela (de [[ra_terms_b]]) | — | 🟢 100% |
| 10 | IN_USE | VARCHAR2(1) | NULL | Classificação | Indica se o termo está em uso (Y/N) (de [[ra_terms_b]]) | — | 🟢 100% |
| 11 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início da vigência (de [[ra_terms_b]]) | — | 🟢 100% |
| 12 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de fim da vigência (de [[ra_terms_b]]) | — | 🟢 100% |
| 13 | PREPAYMENT_FLAG | VARCHAR2(1) | NULL | Classificação | Indica termo de pré-pagamento (Y/N) (de [[ra_terms_b]]) | — | 🟢 100% |
| 14 | BILLING_CYCLE_ID | NUMBER(18) | NULL | Configuração | Ciclo de cobrança associado (de [[ra_terms_b]]) | — | 🟡 65% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência otimista (de [[ra_terms_b]]) | — | 🟢 100% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro (de [[ra_terms_b]]) | — | 🟢 100% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação (de [[ra_terms_b]]) | — | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou (de [[ra_terms_b]]) | — | 🟢 100% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração (de [[ra_terms_b]]) | — | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão (de [[ra_terms_b]]) | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-fonte (composição da view)

### Tabelas relacionadas
- [[ra_terms_lines]] — via `TERM_ID` (linhas/parcelas de cada termo)
- [[ra_customer_trx_all]] — via `TERM_ID` (transações que referenciam esta condição)
- [[ar_payment_schedules_all]] — via `TERM_ID` (parcelas de pagamento geradas)

---

## 📎 Uso Típico

### Listar todas as condições de pagamento ativas (com nome traduzido)
```sql
SELECT TERM_ID, NAME, DESCRIPTION, START_DATE_ACTIVE, END_DATE_ACTIVE
FROM   RA_TERMS_VL
WHERE  NVL(END_DATE_ACTIVE, SYSDATE + 1) > SYSDATE
ORDER BY NAME;
```

### Consultar condição de pagamento de uma transação
```sql
SELECT ct.TRX_NUMBER, tv.NAME AS termo_pagamento, tv.DESCRIPTION
FROM   RA_CUSTOMER_TRX_ALL ct
JOIN   RA_TERMS_VL tv ON tv.TERM_ID = ct.TERM_ID
WHERE  ct.CUSTOMER_TRX_ID = :p_trx_id;
```

### LOV de condições de pagamento para interface
```sql
SELECT TERM_ID, NAME, DESCRIPTION
FROM   RA_TERMS_VL
WHERE  NVL(END_DATE_ACTIVE, SYSDATE + 1) > SYSDATE
ORDER BY NAME;
```

### Filtros comuns
- `END_DATE_ACTIVE IS NULL` — Termos sem expiração
- `IN_USE = 'Y'` — Apenas termos em uso
- `NAME LIKE '%NET%'` — Busca por padrão no nome

---

## 🔒 Observações

- **Esta é uma VIEW, não uma tabela física.** Não possui armazenamento próprio nem pode ser alvo de DML direto (INSERT/UPDATE/DELETE devem ser feitos nas tabelas base [[ra_terms_b]] e [[ra_terms_tl]]).
- A definição interna da view é equivalente a:
  ```sql
  SELECT b.*, tl.NAME, tl.DESCRIPTION
  FROM   RA_TERMS_B b
  JOIN   RA_TERMS_TL tl ON tl.TERM_ID = b.TERM_ID
                         AND tl.LANGUAGE = USERENV('LANG')
  ```
- O idioma retornado depende da **sessão do usuário** (`NLS_LANGUAGE`). Em extrações BICC/BIP, o idioma pode ser definido no perfil do job.
- Em ambientes com um único idioma (ex.: apenas inglês), os dados em `_VL` e `_B` serão idênticos para NAME — mas a view ainda é o ponto de acesso recomendado por consistência arquitetural.
- O sufixo `_VL` (View Language) é um padrão Oracle amplamente utilizado em todas as tabelas com suporte MLS.

---

## 📚 Referências

- [Oracle Docs — RA_TERMS_VL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/ratermsvl-25286.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
