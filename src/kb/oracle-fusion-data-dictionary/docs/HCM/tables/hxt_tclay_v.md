---
id: DOC-HCM-424
doc_type: system-doc
title: "HXT_TCLAY_V — View Consolidada de Layouts de Time Card"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-labor
  - hxt
  - timecard-layout
  - consolidado
  - view
aliases:
  - HXT_TCLAY_V
  - hxt_tclay_v
  - hxt-tclay-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAY_V

## 📌 Visao Geral

View que apresenta uma visao **consolidada dos layouts** de time card do modulo Time & Labor (HXT), incluindo dados base e traducoes no idioma da sessao.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Visao unificada:** layouts com dados base e traducoes consolidados.
- **Lookups:** alimenta listas de selecao de layouts.
- **Administracao:** visao simplificada para gerenciar layouts.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TCLAYST_ID | NUMBER(18) | NOT NULL | PK | Identificador do layout | — | 🟡 65% |
| 2 | LAYOUT_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do layout | — | 🟡 65% |
| 3 | LAYOUT_NAME | VARCHAR2(240) | NULL | Identificacao | Nome traduzido do layout | — | 🟡 60% |
| 4 | LAYOUT_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do layout | — | 🟡 60% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟡 55% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 65% |
| 7 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Controle | Layout padrao | — | 🟡 55% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Layouts de time card disponiveis
```sql
SELECT v.TCLAYST_ID, v.LAYOUT_CODE, v.LAYOUT_NAME,
       v.LAYOUT_TYPE, v.DEFAULT_FLAG
FROM   HXT_TCLAY_V v
WHERE  v.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Layouts ativos`
- `DEFAULT_FLAG = 'Y' — Layout padrao`

---

## 🔒 Observacoes

- View somente leitura que consolida _B e _TL.
- Preferir para consultas que requerem nomes traduzidos de layouts.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclayv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
