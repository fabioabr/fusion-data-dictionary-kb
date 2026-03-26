---
id: DOC-HCM-412
doc_type: system-doc
title: "HXT_SETUP_OPTION_VALS — Valores de Opcoes de Configuracao HXT"
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
  - setup
  - configuracao
  - opcoes
aliases:
  - HXT_SETUP_OPTION_VALS
  - hxt_setup_option_vals
  - hxt-setup-option-vals
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SETUP_OPTION_VALS

## 📌 Visao Geral

Armazena os **valores das opcoes de configuracao** do modulo Time & Labor (HXT). Cada registro contem um par opcao-valor que parametriza o comportamento do modulo.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Parametrizacao:** define valores de configuracao do modulo Time & Labor.
- **Personalizacao:** permite ajustar comportamento sem customizacao de codigo.
- **Administracao:** gerencia opcoes de setup de forma centralizada.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OPTION_VAL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do valor | — | 🟡 70% |
| 2 | PROFILE_ID | NUMBER(18) | NOT NULL | FK | Perfil de configuracao | HXT_SETUP_PROFILES_B | 🟡 70% |
| 3 | OPTION_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo da opcao | — | 🟡 65% |
| 4 | OPTION_VALUE | VARCHAR2(240) | NULL | Dados | Valor da opcao | — | 🟡 65% |
| 5 | OPTION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da opcao | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hxt_setup_profiles_b]] — via `PROFILE_ID` (perfil de configuracao da opcao de ponto)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Valores de configuracao de um perfil
```sql
SELECT v.OPTION_CODE, v.OPTION_VALUE, v.OPTION_TYPE
FROM   HXT_SETUP_OPTION_VALS v
WHERE  v.PROFILE_ID = :p_profile_id;
```

### Filtros comuns
- `PROFILE_ID = :p_profile_id — Por perfil de setup`
- `OPTION_CODE = :p_code — Por opcao especifica`

---

## 🔒 Observacoes

- Contem parametros de configuracao do modulo HXT.
- Alteracoes podem impactar o comportamento global do Time & Labor.
- Validar valores permitidos na documentacao Oracle.

---

## 📚 Referencias

- [Oracle Docs — HXT_SETUP_OPTION_VALS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtsetupoptionvals.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
