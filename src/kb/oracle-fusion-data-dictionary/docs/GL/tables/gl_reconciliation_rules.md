---
id: DOC-GL-035
doc_type: system-doc
title: "GL_RECONCILIATION_RULES — Regras de Reconciliação Contábil"
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
  - reconciliacao
  - reconciliation-rules
  - contabilidade
aliases:
  - GL_RECONCILIATION_RULES
  - gl_reconciliation_rules
  - regras-reconciliacao-gl
  - reconciliation-rules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_RECONCILIATION_RULES

## 📌 Visão Geral

Armazena as **regras de reconciliação contábil** utilizadas pelo módulo de Account Reconciliation do Oracle Fusion GL. Define critérios de matching automático entre lançamentos contábeis (journal lines) para identificar itens que se compensam, facilitando o processo de reconciliação de contas de balanço (clearing accounts, suspense accounts, intercompany, etc.).

> [!note] Módulo de Reconciliação
> Esta tabela faz parte do recurso de **Intercompany/Account Reconciliation** do GL. Nem todas as implementações utilizam a reconciliação automática — muitas fazem reconciliação manual ou via ferramentas externas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Reconciliação automática:** Definição de critérios para matching automático de lançamentos em contas de clearing.
- **Contas suspensas:** Reconciliação de itens em contas suspense para identificar pendências.
- **Intercompany:** Matching de lançamentos intercompany entre business units.
- **Month-end close:** Automatização da reconciliação como parte do processo de fechamento mensal.
- **Auditoria:** Documentação formal dos critérios de reconciliação aplicados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RECONCILIATION_RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra de reconciliação | — | 🟢 95% |
| 2 | RULE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da regra de reconciliação | — | 🟢 90% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 95% |
| 4 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NULL | FK | Identificador da estrutura do plano de contas | [[fnd_id_flex_structures]] | 🟡 75% |
| 5 | MATCH_MODE | VARCHAR2(30) | NOT NULL | Classificação | Modo de matching: AUTOMATIC, MANUAL, SUGGESTED | — | 🟡 75% |
| 6 | TOLERANCE_AMOUNT | NUMBER | NULL | Configuração | Tolerância de valor para matching (diferença aceitável) | — | 🟡 70% |
| 7 | TOLERANCE_PERCENTAGE | NUMBER | NULL | Configuração | Tolerância percentual para matching | — | 🟡 70% |
| 8 | ACCOUNT_LOW | VARCHAR2(25) | NULL | Filtro | Conta contábil inicial do range a reconciliar | — | 🟡 70% |
| 9 | ACCOUNT_HIGH | VARCHAR2(25) | NULL | Filtro | Conta contábil final do range a reconciliar | — | 🟡 70% |
| 10 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se a regra está ativa (Y/N) | — | 🟢 90% |
| 11 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da regra de reconciliação | — | 🟢 90% |
| 12 | MATCH_CRITERIA_1 | VARCHAR2(30) | NULL | Configuração | Primeiro critério de matching (ex: AMOUNT, REFERENCE, DATE) | — | 🟡 65% |
| 13 | MATCH_CRITERIA_2 | VARCHAR2(30) | NULL | Configuração | Segundo critério de matching | — | 🟡 65% |
| 14 | MATCH_CRITERIA_3 | VARCHAR2(30) | NULL | Configuração | Terceiro critério de matching | — | 🟡 65% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[fnd_id_flex_structures]] — via `CHART_OF_ACCOUNTS_ID` (estrutura do plano de contas)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta conhecida — as regras são consumidas pelo processo de reconciliação que gera resultados em tabelas de matching.

---

## 📎 Uso Típico

### Listar regras ativas por ledger
```sql
SELECT rr.RECONCILIATION_RULE_ID,
       rr.RULE_NAME,
       rr.MATCH_MODE,
       rr.TOLERANCE_AMOUNT,
       rr.ACCOUNT_LOW,
       rr.ACCOUNT_HIGH
FROM   GL_RECONCILIATION_RULES rr
WHERE  rr.LEDGER_ID = :p_ledger_id
  AND  rr.ENABLED_FLAG = 'Y'
ORDER BY rr.RULE_NAME;
```

### Regras com tolerância configurada
```sql
SELECT rr.RULE_NAME,
       rr.TOLERANCE_AMOUNT,
       rr.TOLERANCE_PERCENTAGE,
       rr.MATCH_MODE
FROM   GL_RECONCILIATION_RULES rr
WHERE  rr.LEDGER_ID = :p_ledger_id
  AND  (rr.TOLERANCE_AMOUNT IS NOT NULL OR rr.TOLERANCE_PERCENTAGE IS NOT NULL)
  AND  rr.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Regras ativas
- `MATCH_MODE = 'AUTOMATIC'` — Regras de matching automático
- `MATCH_MODE = 'SUGGESTED'` — Regras que sugerem matches para aprovação manual

---

## 🔒 Observações

- As regras de reconciliação são configuradas por ledger e podem ser restritas a um range de contas contábeis.
- O `MATCH_MODE` controla o grau de automação: **AUTOMATIC** faz o match sem intervenção, **SUGGESTED** propõe matches para revisão humana, **MANUAL** requer seleção manual.
- Tolerâncias (`TOLERANCE_AMOUNT` / `TOLERANCE_PERCENTAGE`) permitem matching mesmo quando há pequenas diferenças de arredondamento.
- Esta tabela tem confiança média (65-75%) em várias colunas porque a documentação oficial do Oracle Fusion é limitada para o módulo de reconciliação automática do GL. Validar a estrutura no ambiente real.
- Nem todas as implementações do Oracle Fusion ativam o recurso de reconciliação do GL — muitas instituições financeiras utilizam ferramentas dedicadas (BlackLine, Trintech, etc.).

---

## 📚 Referências

- [Oracle Docs — GL Reconciliation](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
