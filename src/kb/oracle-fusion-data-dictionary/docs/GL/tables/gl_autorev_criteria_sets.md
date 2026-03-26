---
id: DOC-GL-006
doc_type: system-doc
title: "GL_AUTOREV_CRITERIA_SETS — Critérios de Auto-Reversão de Lançamentos"
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
  - auto-reversao
  - reversal
  - lancamentos
aliases:
  - GL_AUTOREV_CRITERIA_SETS
  - gl_autorev_criteria_sets
  - criterios-auto-reversao
  - autorev-criteria
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_AUTOREV_CRITERIA_SETS

## Visao Geral

Armazena os **critérios de auto-reversão** (AutoReverse Criteria Sets) para lançamentos contábeis no General Ledger. Define as regras que determinam quais categorias de lançamentos devem ser automaticamente revertidos no período seguinte, incluindo o método de reversão (Change Sign ou Create New) e o período-alvo da reversão.

> [!note] Auto-reversão
> O mecanismo de auto-reversão é utilizado principalmente para lançamentos de **accrual** (provisões e apropriações) que devem ser estornados no início do próximo período. O processo AutoReverse do GL usa esses critérios para gerar as reversões automaticamente.

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Provisões contábeis:** Configuração de categorias de lançamento que devem ser automaticamente revertidas no período seguinte.
- **Fechamento contábil:** Automatiza a geração de estornos de accruals, reduzindo trabalho manual.
- **Controle de categorias:** Define quais journal categories participam do processo de auto-reversão.
- **Configuração de ledger:** Cada ledger pode ter seu próprio conjunto de critérios de auto-reversão.
- **Auditoria:** Documenta as regras de reversão configuradas para cada ledger.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CRITERIA_SET_ID | NUMBER(18) | NOT NULL | PK | Identificador único do conjunto de critérios | — | 🟡 80% |
| 2 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Ledger ao qual os critérios se aplicam | [[gl_ledgers]] | 🟢 90% |
| 3 | JE_CATEGORY_NAME | VARCHAR2(25) | NOT NULL | Classificação | Nome da categoria de lançamento sujeita a auto-reversão | [[gl_je_categories_tl]] | 🟢 85% |
| 4 | REVERSAL_METHOD_CODE | VARCHAR2(30) | NOT NULL | Classificação | Método de reversão: CHANGE_SIGN (troca sinal) ou CREATE_NEW (cria novo) | — | 🟢 85% |
| 5 | REVERSAL_PERIOD_CODE | VARCHAR2(30) | NOT NULL | Classificação | Período da reversão: NEXT_PERIOD, NEXT_DAY, SAME_PERIOD, etc. | — | 🟢 85% |
| 6 | REVERSAL_DATE_CODE | VARCHAR2(30) | NULL | Classificação | Critério de data: FIRST_DAY, LAST_DAY, SPECIFIC_DATE | — | 🟡 75% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o critério está ativo (Y/N) | — | 🟢 85% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Sistema | Controle de versionamento otimista (locking) | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger associado)
- [[gl_je_categories_tl]] — via `JE_CATEGORY_NAME` (categoria de lançamento)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de configuração (leaf table).

---

## Uso Tipico

### Critérios de auto-reversão de um ledger
```sql
SELECT arc.JE_CATEGORY_NAME, arc.REVERSAL_METHOD_CODE,
       arc.REVERSAL_PERIOD_CODE, arc.REVERSAL_DATE_CODE,
       arc.ENABLED_FLAG
FROM   GL_AUTOREV_CRITERIA_SETS arc
WHERE  arc.LEDGER_ID = :p_ledger_id
  AND  arc.ENABLED_FLAG = 'Y'
ORDER BY arc.JE_CATEGORY_NAME;
```

### Categorias configuradas para auto-reversão
```sql
SELECT gl.NAME AS ledger, arc.JE_CATEGORY_NAME,
       arc.REVERSAL_METHOD_CODE, arc.REVERSAL_PERIOD_CODE
FROM   GL_AUTOREV_CRITERIA_SETS arc
JOIN   GL_LEDGERS gl ON gl.LEDGER_ID = arc.LEDGER_ID
WHERE  arc.ENABLED_FLAG = 'Y'
ORDER BY gl.NAME, arc.JE_CATEGORY_NAME;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Critérios ativos
- `REVERSAL_METHOD_CODE = 'CHANGE_SIGN'` — Método de troca de sinal
- `REVERSAL_PERIOD_CODE = 'NEXT_PERIOD'` — Reversão no próximo período

---

## Observacoes

- O método `CHANGE_SIGN` inverte o sinal dos valores (débito vira crédito e vice-versa), enquanto `CREATE_NEW` cria um novo lançamento com débitos e créditos invertidos — o efeito contábil é o mesmo, mas a forma de apresentação difere.
- O `REVERSAL_PERIOD_CODE = 'NEXT_PERIOD'` é o mais comum — a reversão é gerada automaticamente no primeiro dia do próximo período contábil.
- Cada combinação `LEDGER_ID` + `JE_CATEGORY_NAME` deve ser única — não é possível ter dois critérios para a mesma categoria no mesmo ledger.
- Para que a auto-reversão funcione, o lançamento original deve ter o campo `ACCRUAL_REV_FLAG` = 'Y' no header do journal (tabela [[gl_je_headers]]).

---

## Referencias

- [Oracle Docs — GL_AUTOREV_CRITERIA_SETS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glautorevcriteria-25070.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
