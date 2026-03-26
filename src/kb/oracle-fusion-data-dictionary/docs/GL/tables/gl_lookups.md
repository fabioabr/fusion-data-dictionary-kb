---
id: DOC-GL-032
doc_type: system-doc
title: "GL_LOOKUPS — Tabela de Lookup/Valores de Referência do GL"
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
  - lookups
  - valores-referencia
  - configuracao
aliases:
  - GL_LOOKUPS
  - gl_lookups
  - lookups-gl
  - valores-referencia-gl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LOOKUPS

## 📌 Visão Geral

Armazena os **valores de lookup (referência)** utilizados pelo módulo General Ledger. É uma view ou tabela que consolida lookup types e seus valores associados, usados para validação e exibição de campos codificados em telas e relatórios do GL. Segue o padrão Oracle de lookups — cada `LOOKUP_TYPE` agrupa um conjunto de `LOOKUP_CODE` com significados e descrições traduzidas.

> [!note] Tabela/View de referência
> GL_LOOKUPS pode ser uma view sobre `FND_LOOKUP_VALUES` filtrada para o módulo GL. Os lookup types definem listas de valores válidos para campos codificados do GL (status, tipos, categorias etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Validação de campos:** Garantir que valores inseridos em campos codificados sejam válidos.
- **Exibição em telas:** Converter códigos internos em descrições amigáveis (ex: 'P' → 'Posted').
- **Relatórios:** Tradução de códigos para nomes descritivos nos reports.
- **Configuração:** Definição de valores válidos para dropdowns e LOVs nas telas do GL.
- **Internacionalização:** Descrições traduzidas por idioma para cada lookup value.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOOKUP_TYPE | VARCHAR2(30) | NOT NULL | PK | Tipo/grupo de lookup (ex: BATCH_STATUS, JOURNAL_CATEGORY, ACTUAL_FLAG) | — | 🟢 95% |
| 2 | LOOKUP_CODE | VARCHAR2(30) | NOT NULL | PK | Código do valor dentro do lookup type (ex: 'P', 'U', 'A') | — | 🟢 95% |
| 3 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da descrição | — | 🟢 95% |
| 4 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 90% |
| 5 | MEANING | VARCHAR2(80) | NOT NULL | Identificação | Significado/descrição curta do lookup code (ex: "Posted", "Unposted") | — | 🟢 95% |
| 6 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição longa do lookup code | — | 🟢 90% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se o valor está habilitado (Y/N) | — | 🟢 95% |
| 8 | START_DATE_ACTIVE | DATE | NULL | Controle | Data de início de validade do lookup value | — | 🟢 90% |
| 9 | END_DATE_ACTIVE | DATE | NULL | Controle | Data de fim de validade do lookup value | — | 🟢 90% |
| 10 | TAG | VARCHAR2(150) | NULL | Classificação | Tag de categorização adicional | — | 🟡 75% |
| 11 | ATTRIBUTE_CATEGORY | VARCHAR2(150) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 70% |
| 12 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Campos de atributo descritivo configuráveis | — | 🟡 70% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela/view de referência raiz (master data de lookups).

### Tabelas-filha (FK de saída)
- Referenciada indiretamente por todas as tabelas do GL que usam campos codificados:
- [[gl_je_headers]] — campos como `STATUS`, `ACTUAL_FLAG` (status válidos para cabeçalhos de journal)
- [[gl_je_lines]] — campos como `STATUS` (status válidos para linhas de journal)
- [[gl_balances]] — campo `ACTUAL_FLAG` (tipos de saldo (real, orçamento, encargo))
- [[gl_ledgers]] — campos como `LEDGER_CATEGORY_CODE` (categorias válidas de ledger (primário, secundário))

---

## 📎 Uso Típico

### Listar valores de um lookup type
```sql
SELECT gl.LOOKUP_TYPE,
       gl.LOOKUP_CODE,
       gl.MEANING,
       gl.DESCRIPTION,
       gl.ENABLED_FLAG
FROM   GL_LOOKUPS gl
WHERE  gl.LOOKUP_TYPE = 'BATCH_STATUS'
  AND  gl.LANGUAGE = USERENV('LANG')
  AND  gl.ENABLED_FLAG = 'Y'
ORDER BY gl.LOOKUP_CODE;
```

### Traduzir código para descrição em queries
```sql
SELECT jh.JE_HEADER_ID,
       jh.NAME,
       lk.MEANING AS status_descricao
FROM   GL_JE_HEADERS jh
JOIN   GL_LOOKUPS lk
       ON lk.LOOKUP_TYPE = 'BATCH_STATUS'
      AND lk.LOOKUP_CODE = jh.STATUS
      AND lk.LANGUAGE = USERENV('LANG')
WHERE  jh.LEDGER_ID = :p_ledger_id;
```

### Listar todos os lookup types do GL
```sql
SELECT DISTINCT gl.LOOKUP_TYPE,
       MIN(gl.DESCRIPTION) AS descricao
FROM   GL_LOOKUPS gl
WHERE  gl.LANGUAGE = USERENV('LANG')
GROUP BY gl.LOOKUP_TYPE
ORDER BY gl.LOOKUP_TYPE;
```

### Lookup types comuns do GL
- `BATCH_STATUS` — Status de batch (Posted, Unposted etc.)
- `ACTUAL_FLAG` — Tipo de saldo (Actual, Budget, Encumbrance)
- `JOURNAL_CATEGORY` — Categorias de journal
- `CURRENCY_CONVERSION_TYPE` — Tipos de conversão cambial
- `LEDGER_CATEGORY` — Categorias de ledger (Primary, Secondary, ALC)
- `PERIOD_STATUS` — Status de período (Open, Closed, Never Opened)

---

## 🔒 Observações

- GL_LOOKUPS pode ser uma **view** sobre `FND_LOOKUP_VALUES` com filtro de aplicação GL — a estrutura de colunas pode variar ligeiramente.
- A PK composta é `LOOKUP_TYPE` + `LOOKUP_CODE` + `LANGUAGE`.
- Sempre filtrar `LANGUAGE = USERENV('LANG')` para obter descrições no idioma corrente do usuário.
- Lookups com `ENABLED_FLAG = 'N'` ou com `END_DATE_ACTIVE` no passado são valores desativados — não aparecem em LOVs.
- Lookups do tipo "seeded" (pré-definidos pela Oracle) não devem ser alterados — apenas lookups custom podem ser modificados.
- Para criar novos lookup types para o GL, usar a UI de Manage Lookups no Oracle Fusion.

---

## 📚 Referências

- [Oracle Docs — GL_LOOKUPS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gllookups.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
