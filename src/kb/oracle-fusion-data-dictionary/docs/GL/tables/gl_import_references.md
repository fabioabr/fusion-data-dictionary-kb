---
id: DOC-GL-018
doc_type: system-doc
title: "GL_IMPORT_REFERENCES — Referências de Importação de Lançamentos"
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
  - import-references
  - journal-import
  - rastreabilidade
aliases:
  - GL_IMPORT_REFERENCES
  - gl_import_references
  - referencias-importacao-gl
  - journal-import-references
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_IMPORT_REFERENCES

## 📌 Visão Geral

Armazena as **referências de importação** que vinculam linhas de lançamentos contábeis (journal lines) aos registros de origem nos subledgers (AP, AR, FA, etc.). Cada registro representa o link de rastreabilidade entre uma linha do GL e a transação original que a gerou, permitindo drill-down do General Ledger para o subledger de origem.

> [!note] Rastreabilidade Subledger → GL
> Esta tabela é a **ponte de auditoria** entre o subledger e o GL. Sem ela, não é possível rastrear a origem de um lançamento contábil até a transação original (fatura, pagamento, depreciação, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Drill-down contábil:** Navegar de um lançamento no GL até a transação de origem no subledger.
- **Reconciliação GL × Subledger:** Verificar que todos os lançamentos importados têm referência cruzada válida.
- **Auditoria:** Rastreamento completo da origem de cada valor contabilizado.
- **Análise de posting:** Identificar quais processos de importação geraram determinados lançamentos.
- **Troubleshooting:** Diagnosticar discrepâncias entre saldos do GL e dos subledgers.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GL_SL_LINK_ID | NUMBER(18) | NOT NULL | PK | Identificador único do link subledger-GL | — | 🟢 95% |
| 2 | JE_HEADER_ID | NUMBER(18) | NOT NULL | FK | ID do cabeçalho do lançamento contábil | [[gl_je_headers]] | 🟢 95% |
| 3 | JE_LINE_NUM | NUMBER(15) | NOT NULL | FK | Número da linha do lançamento | [[gl_je_lines]] | 🟢 95% |
| 4 | JE_BATCH_ID | NUMBER(18) | NOT NULL | FK | ID do lote de lançamento | [[gl_je_batches]] | 🟢 90% |
| 5 | GL_SL_LINK_TABLE | VARCHAR2(30) | NOT NULL | Classificação | Tabela de origem do subledger (ex: AP_INVOICE_DISTRIBUTIONS_ALL) | — | 🟢 95% |
| 6 | REFERENCE_1 | VARCHAR2(240) | NULL | Referência | Referência 1 — tipicamente batch_name ou source_name | — | 🟢 90% |
| 7 | REFERENCE_2 | VARCHAR2(240) | NULL | Referência | Referência 2 — tipicamente batch_id do subledger | — | 🟢 90% |
| 8 | REFERENCE_3 | VARCHAR2(240) | NULL | Referência | Referência 3 — tipicamente header_id do subledger | — | 🟢 90% |
| 9 | REFERENCE_4 | VARCHAR2(240) | NULL | Referência | Referência 4 — tipicamente distribution_id ou line_id | — | 🟢 90% |
| 10 | REFERENCE_5 | VARCHAR2(240) | NULL | Referência | Referência 5 — informação adicional variável por subledger | — | 🟢 90% |
| 11 | REFERENCE_6 | VARCHAR2(240) | NULL | Referência | Referência 6 — informação adicional | — | 🟡 80% |
| 12 | REFERENCE_7 | VARCHAR2(240) | NULL | Referência | Referência 7 — informação adicional | — | 🟡 80% |
| 13 | REFERENCE_8 | VARCHAR2(240) | NULL | Referência | Referência 8 — informação adicional | — | 🟡 80% |
| 14 | REFERENCE_9 | VARCHAR2(240) | NULL | Referência | Referência 9 — informação adicional | — | 🟡 80% |
| 15 | REFERENCE_10 | VARCHAR2(240) | NULL | Referência | Referência 10 — informação adicional | — | 🟡 80% |
| 16 | SOURCE_TRX_ID | NUMBER(18) | NULL | Referência cruzada | ID da transação de origem no subledger | — | 🟡 75% |
| 17 | SOURCE_TRX_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da transação de origem | — | 🟡 75% |
| 18 | SOURCE_DISTRIBUTION_ID | NUMBER(18) | NULL | Referência cruzada | ID da distribuição de origem no subledger | — | 🟡 75% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_headers]] — via `JE_HEADER_ID` (cabeçalho do lançamento)
- [[gl_je_lines]] — via `JE_HEADER_ID` + `JE_LINE_NUM` (linha do lançamento)
- [[gl_je_batches]] — via `JE_BATCH_ID` (lote de lançamento)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — os campos REFERENCE_N apontam para tabelas dos subledgers de origem (AP, AR, FA, etc.).

---

## 📎 Uso Típico

### Drill-down: GL → Subledger (origem do lançamento)
```sql
SELECT ir.GL_SL_LINK_TABLE,
       ir.REFERENCE_1 AS source_batch,
       ir.REFERENCE_3 AS source_header_id,
       ir.REFERENCE_4 AS source_dist_id
FROM   GL_IMPORT_REFERENCES ir
WHERE  ir.JE_HEADER_ID = :p_je_header_id
  AND  ir.JE_LINE_NUM = :p_je_line_num;
```

### Lançamentos originados de um subledger específico
```sql
SELECT h.NAME AS journal_name,
       ir.JE_LINE_NUM,
       ir.REFERENCE_3 AS source_trx_id
FROM   GL_IMPORT_REFERENCES ir
JOIN   GL_JE_HEADERS h ON h.JE_HEADER_ID = ir.JE_HEADER_ID
WHERE  ir.GL_SL_LINK_TABLE = 'AP_INVOICE_DISTRIBUTIONS_ALL'
  AND  ir.JE_BATCH_ID = :p_batch_id;
```

### Filtros comuns
- `GL_SL_LINK_TABLE = 'AP_INVOICE_DISTRIBUTIONS_ALL'` — Origem: faturas AP
- `GL_SL_LINK_TABLE = 'RA_CUST_TRX_LINE_GL_DIST_ALL'` — Origem: transações AR
- `GL_SL_LINK_TABLE = 'FA_ADJUSTMENTS'` — Origem: ativos fixos

---

## 🔒 Observações

- Os campos `REFERENCE_1` a `REFERENCE_10` têm significado variável conforme o subledger de origem. Consultar a documentação do subledger específico para interpretação.
- `GL_SL_LINK_TABLE` indica a tabela do subledger que originou o lançamento — essencial para saber como interpretar os campos REFERENCE.
- Esta tabela pode ser volumosa em ambientes com alto volume de transações.
- Lançamentos manuais (não importados) podem não ter registros nesta tabela.
- No Oracle Fusion Cloud, o Subledger Accounting (SLA/XLA) gerencia a criação destes registros automaticamente.

---

## 📚 Referências

- [Oracle Docs — GL_IMPORT_REFERENCES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glimportreferences-25780.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
