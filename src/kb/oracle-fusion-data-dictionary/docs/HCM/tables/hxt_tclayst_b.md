---
id: DOC-HCM-420
doc_type: system-doc
title: "HXT_TCLAYST_B — Layouts de Time Card (Base)"
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
  - layout
  - base
aliases:
  - HXT_TCLAYST_B
  - hxt_tclayst_b
  - hxt-tclayst-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_TCLAYST_B

## 📌 Visao Geral

Tabela base que armazena as **definicoes de layout de time card** do modulo Time & Labor (HXT). Cada layout define a estrutura visual e funcional de um formulario de entrada de tempo.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Definicao de layouts:** configura a estrutura de formularios de time card.
- **Personalizacao:** permite diferentes layouts por grupo de colaboradores.
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
| 1 | TCLAYST_ID | NUMBER(18) | NOT NULL | PK | Identificador do layout | — | 🟡 70% |
| 2 | LAYOUT_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do layout | — | 🟡 65% |
| 3 | LAYOUT_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do layout | — | 🟡 60% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 65% |
| 5 | DEFAULT_FLAG | VARCHAR2(1) | NULL | Controle | Layout padrao (Y/N) | — | 🟡 55% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[hxt_tclayst_tl]] — via `TCLAYST_ID` (traducoes do layout de cartao de ponto)
- [[hxt_tclayst_prop]] — via `TCLAYST_ID` (traducoes do layout de cartao de ponto)
- [[hxt_tclayfld_defns_b]] — via `TCLAYST_ID` (traducoes do layout de cartao de ponto)

---

## 📎 Uso Tipico

### Listar layouts de time card ativos
```sql
SELECT t.TCLAYST_ID, t.LAYOUT_CODE, t.LAYOUT_TYPE, t.DEFAULT_FLAG
FROM   HXT_TCLAYST_B t
WHERE  t.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Layouts ativos`
- `DEFAULT_FLAG = 'Y' — Layout padrao`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em HXT_TCLAYST_TL.
- Define a estrutura dos formularios de entrada de tempo.
- Layouts determinam quais campos e secoes sao exibidos no time card.

---

## 📚 Referencias

- [Oracle Docs — HXT_TCLAYST_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxttclaystb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
