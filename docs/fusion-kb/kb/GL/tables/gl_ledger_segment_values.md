---
id: DOC-GL-029
doc_type: system-doc
title: "GL_LEDGER_SEGMENT_VALUES — Valores de Segmento Associados a Ledgers"
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
  - ledger-segments
  - balancing-segment
  - configuracao
aliases:
  - GL_LEDGER_SEGMENT_VALUES
  - gl_ledger_segment_values
  - segmentos-ledger
  - ledger-segment-values
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LEDGER_SEGMENT_VALUES

## 📌 Visão Geral

Armazena a associação entre **valores de segmento contábil** (tipicamente o balancing segment / empresa) e **ledgers**. Define quais valores de segmento estão atribuídos a cada ledger, controlando o escopo de cada livro contábil. Essencial para ambientes multi-empresa onde diferentes entidades legais compartilham o mesmo plano de contas.

> [!note] Tabela de atribuição de segmentos
> Cada valor de balancing segment (ex: empresa "01", "02") é atribuído a exatamente um primary ledger. Esta tabela controla o mapeamento empresa → ledger.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Multi-empresa:** Definição de quais empresas/entidades pertencem a cada ledger.
- **Segurança contábil:** Controle de acesso por segmento de balanceamento.
- **Consolidação:** Identificação de quais segmentos são consolidados em cada ledger.
- **Validação de lançamentos:** Garantir que journals referenciem apenas segmentos válidos para o ledger.
- **Setup de entidades legais:** Associação de legal entities com seus respectivos ledgers via balancing segment.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEDGER_ID | NUMBER(18) | NOT NULL | FK/PK | Identificador do ledger | [[gl_ledgers]] | 🟢 95% |
| 2 | SEGMENT_VALUE | VARCHAR2(25) | NOT NULL | PK | Valor do segmento de balanceamento (ex: "01", "02") | — | 🟢 95% |
| 3 | SEGMENT_TYPE_CODE | VARCHAR2(1) | NOT NULL | Classificação | Tipo de segmento: B (Balancing), M (Management) | — | 🟢 90% |
| 4 | STATUS_CODE | VARCHAR2(1) | NULL | Controle | Status da atribuição: A (Active), I (Inactive) | — | 🟡 80% |
| 5 | START_DATE | DATE | NULL | Controle | Data de início de validade da atribuição | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Controle | Data de fim de validade da atribuição | — | 🟡 80% |
| 7 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | FK | ID da entidade legal associada ao segmento | — | 🟡 80% |
| 8 | PARENT_RECORD_ID | NUMBER(18) | NULL | FK | ID do registro pai (para hierarquias de segmento) | — | 🟡 65% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2(150) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 75% |
| 10 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Campos de atributo descritivo (DFF) configuráveis | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger ao qual o segmento está atribuído)

### Tabelas-filha (FK de saída)
- [[gl_legal_entities_bsvs]] — via `LEDGER_ID` + `SEGMENT_VALUE` (BSVs por entidade legal)

---

## 📎 Uso Típico

### Listar segmentos atribuídos a um ledger
```sql
SELECT lsv.LEDGER_ID,
       gl.NAME AS ledger_name,
       lsv.SEGMENT_VALUE,
       lsv.SEGMENT_TYPE_CODE,
       lsv.STATUS_CODE,
       lsv.LEGAL_ENTITY_ID
FROM   GL_LEDGER_SEGMENT_VALUES lsv
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = lsv.LEDGER_ID
WHERE  lsv.LEDGER_ID = :p_ledger_id
  AND  lsv.SEGMENT_TYPE_CODE = 'B'
ORDER BY lsv.SEGMENT_VALUE;
```

### Identificar qual ledger possui um segmento específico
```sql
SELECT gl.LEDGER_ID,
       gl.NAME AS ledger_name,
       lsv.SEGMENT_VALUE,
       lsv.STATUS_CODE
FROM   GL_LEDGER_SEGMENT_VALUES lsv
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = lsv.LEDGER_ID
WHERE  lsv.SEGMENT_VALUE = :p_segment_value
  AND  lsv.SEGMENT_TYPE_CODE = 'B';
```

### Filtros comuns
- `SEGMENT_TYPE_CODE = 'B'` — Balancing segment values (empresa)
- `SEGMENT_TYPE_CODE = 'M'` — Management segment values
- `STATUS_CODE = 'A'` — Atribuições ativas
- `LEGAL_ENTITY_ID IS NOT NULL` — Segmentos com entidade legal associada

---

## 🔒 Observações

- Cada valor de balancing segment deve estar atribuído a exatamente um primary ledger — esta tabela garante essa unicidade.
- O `SEGMENT_TYPE_CODE = 'B'` refere-se ao balancing segment, que tipicamente é o segmento de empresa/entidade no plano de contas.
- A associação entre `SEGMENT_VALUE` e `LEGAL_ENTITY_ID` é fundamental para o Subledger Accounting — determina qual entidade legal é responsável por cada conjunto de transações.
- Alterar atribuições de segmento em produção pode causar inconsistências contábeis — esta é uma configuração de setup inicial.
- A coluna `BAL_SEG_COLUMN_NAME` em [[gl_ledgers]] define qual coluna de segmento (SEGMENT1, SEGMENT2 etc.) é o balancing segment.

---

## 🔗 PVOs Relacionados

### [[balancepvo|BalancePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LEDGER_ID | LedgerSegValLedgerId | — |
| LEGAL_ENTITY_ID | LedgerSegValLegalEntityId | — |
| SEGMENT_TYPE_CODE | LedgerSegValSegmentTypeCode | — |
| SEGMENT_VALUE | LedgerSegValSegmentValue | — |

---

## 📚 Referências

- [Oracle Docs — GL_LEDGER_SEGMENT_VALUES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glledgersegmentvalues.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
