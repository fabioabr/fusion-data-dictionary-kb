---
id: DOC-HCM-419
doc_type: system-doc
title: "HXT_TCLAYFLD_DEFNS_VL — View de Lookup de Campos de Layout de Time Card"
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
  - campo-layout
  - lookup
  - view
aliases:
  - HXT_TCLAYFLD_DEFNS_VL
  - hxt_tclayfld_defns_vl
  - hxt-tclayfld-defns-vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAYFLD_DEFNS_VL

## 📌 Visao Geral

View que une **HXT_TCLAYFLD_DEFNS_B** com **HXT_TCLAYFLD_DEFNS_TL** no idioma da sessao. Fornece acesso simplificado aos campos de layout com labels traduzidos.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view de lookup** que une a tabela base (_B) com traducoes (_TL) no idioma da sessao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Acesso simplificado:** campos com labels no idioma da sessao.
- **Lookups de interface:** alimenta formularios de time card.
- **Relatorios:** labels traduzidos para relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TCLAYFLD_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador da definicao | — | 🟡 70% |
| 2 | LAYOUT_ID | NUMBER(18) | NOT NULL | FK | Layout de time card | HXT_TCLAYST_B | 🟡 65% |
| 3 | FIELD_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do campo | — | 🟡 65% |
| 4 | FIELD_LABEL | VARCHAR2(240) | NOT NULL | Identificacao | Label traduzido | — | 🟡 65% |
| 5 | FIELD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do campo | — | 🟡 60% |
| 6 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Controle | Campo obrigatorio | — | 🟡 60% |
| 7 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 55% |
| 8 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Campos de layout com labels traduzidos
```sql
SELECT v.FIELD_CODE, v.FIELD_LABEL, v.FIELD_TYPE,
       v.REQUIRED_FLAG, v.DISPLAY_SEQUENCE
FROM   HXT_TCLAYFLD_DEFNS_VL v
WHERE  v.LAYOUT_ID = :p_layout_id
  AND  v.ENABLED_FLAG = 'Y'
ORDER BY v.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `LAYOUT_ID = :p_layout_id — Por layout`
- `ENABLED_FLAG = 'Y' — Campos ativos`

---

## 🔒 Observacoes

- View somente leitura que une _B com _TL.
- Preferir esta view para consultas que requerem labels traduzidos.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAYFLD_DEFNS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclayflddefnsvl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[templatelayoutcompdisplayvaluepvo|TemplateLayoutCompDisplayValuePVO]] (GL · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LABEL | ParentTclayfldVLPEOLabel | ✅ |
| NAME | ParentTclayfldVLPEOName | ✅ |
| TCLAYFLD_DEFNS_CD | ParentTclayfldVLPEOTclayfldDefnsCd | ✅ |
| TCLAYFLD_DEFNS_ID | ParentTclayfldVLPEOTclayfldDefnsId | — |

### [[templatelayoutcomponentpvo|TemplateLayoutComponentPVO]] (GL · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LABEL | ParentTclayfldVLPEOLabel | ✅ |
| NAME | ParentTclayfldVLPEOName | ✅ |
| TCLAYFLD_DEFNS_CD | ParentTclayfldVLPEODefnsCd | ✅ |
| TCLAYFLD_DEFNS_ID | ParentTclayfldVLPEODefnsId | — |
