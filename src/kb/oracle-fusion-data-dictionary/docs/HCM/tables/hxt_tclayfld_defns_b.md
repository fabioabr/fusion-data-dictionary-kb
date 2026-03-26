---
id: DOC-HCM-417
doc_type: system-doc
title: "HXT_TCLAYFLD_DEFNS_B — Definicoes de Campos de Layout de Time Card (Base)"
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
  - base
aliases:
  - HXT_TCLAYFLD_DEFNS_B
  - hxt_tclayfld_defns_b
  - hxt-tclayfld-defns-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAYFLD_DEFNS_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de campos** dos layouts de time card do modulo Time & Labor (HXT). Define quais campos aparecem no formulario de entrada de tempo.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao de UI:** define quais campos aparecem no time card.
- **Personalizacao:** permite customizar o formulario de entrada de tempo.
- **Padronizacao:** garante consistencia na captura de dados de tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TCLAYFLD_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador da definicao do campo | — | 🟡 70% |
| 2 | LAYOUT_ID | NUMBER(18) | NOT NULL | FK | Layout de time card | HXT_TCLAYST_B | 🟡 65% |
| 3 | FIELD_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do campo | — | 🟡 65% |
| 4 | FIELD_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do campo (TEXT, NUMBER, LOV) | — | 🟡 60% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Controle | Campo obrigatorio (Y/N) | — | 🟡 60% |
| 6 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Ordem de exibicao | — | 🟡 55% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 60% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_tclayst_b]] — via `LAYOUT_ID` (layout do campo de cartao de ponto)

### Tabelas-filha (FK de saida)
- [[hxt_tclayfld_defns_tl]] — via `TCLAYFLD_DEFN_ID` (traducoes da definicao de campo)

---

## 📎 Uso Tipico

### Campos de um layout de time card
```sql
SELECT d.FIELD_CODE, d.FIELD_TYPE, d.REQUIRED_FLAG,
       d.DISPLAY_SEQUENCE
FROM   HXT_TCLAYFLD_DEFNS_B d
WHERE  d.LAYOUT_ID = :p_layout_id
  AND  d.ENABLED_FLAG = 'Y'
ORDER BY d.DISPLAY_SEQUENCE;
```

### Filtros comuns
- `LAYOUT_ID = :p_layout_id — Por layout`
- `ENABLED_FLAG = 'Y' — Campos ativos`
- `REQUIRED_FLAG = 'Y' — Campos obrigatorios`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em HXT_TCLAYFLD_DEFNS_TL.
- Define a estrutura de campos do formulario de time card.
- Campos podem ser do tipo texto, numerico, LOV (lista de valores), etc.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAYFLD_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclayflddefnsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
