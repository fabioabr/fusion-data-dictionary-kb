---
id: DOC-HCM-423
doc_type: system-doc
title: "HXT_TCLAY_REGION_V — View de Regioes de Layout de Time Card"
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
  - regiao-layout
  - view
aliases:
  - HXT_TCLAY_REGION_V
  - hxt_tclay_region_v
  - hxt-tclay-region-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAY_REGION_V

## 📌 Visao Geral

View que apresenta as **regioes (secoes) dos layouts** de time card do modulo Time & Labor (HXT). Cada regiao agrupa campos relacionados no formulario de entrada de tempo.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Organizacao visual:** define como campos sao agrupados no time card.
- **Navegacao:** facilita a navegacao entre secoes do formulario.
- **Personalizacao:** permite configurar quais regioes aparecem por layout.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REGION_ID | NUMBER(18) | NOT NULL | PK | Identificador da regiao | — | 🟡 65% |
| 2 | LAYOUT_ID | NUMBER(18) | NOT NULL | FK | Layout associado | HXT_TCLAYST_B | 🟡 65% |
| 3 | REGION_CODE | VARCHAR2(80) | NULL | Identificacao | Codigo da regiao | — | 🟡 60% |
| 4 | REGION_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da regiao | — | 🟡 55% |
| 5 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 55% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_tclayst_b]] — via `LAYOUT_ID` (layout de cartao de ponto da regiao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Regioes de um layout de time card
```sql
SELECT v.REGION_CODE, v.REGION_NAME, v.DISPLAY_SEQUENCE
FROM   HXT_TCLAY_REGION_V v
WHERE  v.LAYOUT_ID = :p_layout_id
  AND  v.ENABLED_FLAG = 'Y'
ORDER BY v.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `LAYOUT_ID = :p_layout_id — Por layout`
- `ENABLED_FLAG = 'Y' — Regioes ativas`

---

## 🔒 Observacoes

- View somente leitura.
- Regioes organizam campos do time card em secoes logicas.
- Ordem de exibicao controlada por DISPLAY_SEQUENCE.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAY_REGION_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclayregionv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
