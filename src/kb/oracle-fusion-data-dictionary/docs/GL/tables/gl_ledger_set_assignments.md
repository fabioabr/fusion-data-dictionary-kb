---
id: DOC-GL-030
doc_type: system-doc
title: "GL_LEDGER_SET_ASSIGNMENTS — Atribuições de Conjuntos de Ledgers"
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
  - ledger-set
  - atribuicao
  - configuracao
aliases:
  - GL_LEDGER_SET_ASSIGNMENTS
  - gl_ledger_set_assignments
  - atribuicoes-ledger-set
  - ledger-set-assignments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LEDGER_SET_ASSIGNMENTS

## 📌 Visão Geral

Armazena as **atribuições de ledgers a conjuntos de ledgers (ledger sets)**. Um ledger set é um agrupamento lógico de ledgers que permite executar processos em lote (posting, fechamento, relatórios) para múltiplos livros contábeis simultaneamente. Esta tabela define a relação N:N entre ledgers e ledger sets.

> [!note] Tabela de agrupamento
> Ledger sets simplificam operações multi-ledger. Em vez de rodar posting ou relatórios ledger por ledger, o usuário seleciona um ledger set que abrange todos os ledgers desejados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Posting em lote:** Executar posting de journals para múltiplos ledgers via ledger set.
- **Fechamento de período:** Abrir/fechar períodos para todos os ledgers de um set simultaneamente.
- **Relatórios consolidados:** Gerar relatórios que abrangem múltiplos ledgers.
- **Segurança de acesso:** Atribuir acesso a usuários por ledger set em vez de ledger individual.
- **Simplificação operacional:** Reduzir processos repetitivos em ambientes multi-ledger.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEDGER_SET_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do ledger set (referencia [[gl_ledgers]] com OBJECT_TYPE_CODE = 'S') | [[gl_ledgers]] | 🟢 90% |
| 2 | LEDGER_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do ledger atribuído ao set | [[gl_ledgers]] | 🟢 95% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atribuição | — | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(1) | NULL | Controle | Status da atribuição: A (Active), I (Inactive) | — | 🟡 75% |
| 5 | START_DATE | DATE | NULL | Controle | Data de início de validade da atribuição | — | 🟡 70% |
| 6 | END_DATE | DATE | NULL | Controle | Data de fim de validade da atribuição | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_SET_ID` (ledger set, com OBJECT_TYPE_CODE = 'S')
- [[gl_ledgers]] — via `LEDGER_ID` (ledger membro do set)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de associação (junction table).

---

## 📎 Uso Típico

### Listar ledgers de um ledger set
```sql
SELECT lsa.LEDGER_SET_ID,
       gls.NAME AS ledger_set_name,
       lsa.LEDGER_ID,
       gl.NAME AS ledger_name,
       gl.CURRENCY_CODE
FROM   GL_LEDGER_SET_ASSIGNMENTS lsa
JOIN   GL_LEDGERS gls ON gls.LEDGER_ID = lsa.LEDGER_SET_ID
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = lsa.LEDGER_ID
WHERE  lsa.LEDGER_SET_ID = :p_ledger_set_id
ORDER BY gl.NAME;
```

### Identificar quais sets contêm um ledger
```sql
SELECT gls.LEDGER_ID AS ledger_set_id,
       gls.NAME AS ledger_set_name,
       gl.NAME AS ledger_name
FROM   GL_LEDGER_SET_ASSIGNMENTS lsa
JOIN   GL_LEDGERS gls ON gls.LEDGER_ID = lsa.LEDGER_SET_ID
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = lsa.LEDGER_ID
WHERE  lsa.LEDGER_ID = :p_ledger_id
ORDER BY gls.NAME;
```

### Filtros comuns
- `STATUS_CODE = 'A'` — Atribuições ativas
- `LEDGER_SET_ID = :p_set_id` — Ledgers de um set específico
- `LEDGER_ID = :p_ledger_id` — Sets que contêm um ledger específico

---

## 🔒 Observações

- O `LEDGER_SET_ID` referencia a tabela [[gl_ledgers]] onde `OBJECT_TYPE_CODE = 'S'` — ledger sets são registrados na mesma tabela que ledgers.
- Um ledger pode pertencer a múltiplos ledger sets — a relação é N:N.
- Ledger sets são usados em processos batch (posting, open/close period) para simplificar operações em ambientes com muitos ledgers.
- Apenas ledgers com o mesmo plano de contas e calendário podem ser agrupados em um ledger set.
- Esta tabela é de baixa volumetria — tipicamente dezenas de registros.

---

## 📚 Referências

- [Oracle Docs — GL_LEDGER_SET_ASSIGNMENTS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glledgersetassignments.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
