---
id: DOC-HCM-380
doc_type: system-doc
title: "HWM_TM_OPM_MEANING_V — View de Significados OPM para Time Management"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-management
  - opm
  - lookup
  - meanings
  - view
aliases:
  - HWM_TM_OPM_MEANING_V
  - hwm_tm_opm_meaning_v
  - hwm-tm-opm-meaning-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_OPM_MEANING_V

## 📌 Visão Geral

View que apresenta os **significados (meanings) de parâmetros operacionais** (OPM) do módulo Time Management. Traduz códigos internos em descrições legíveis.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** — consulta pré-definida sobre tabelas base, somente leitura.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Tradução de códigos:** converte códigos OPM em descrições amigáveis.
- **Lookups de configuração:** alimenta dropdowns e validações na interface.
- **Relatórios:** fornece descrições legíveis para códigos internos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOOKUP_CODE | VARCHAR2(30) | NOT NULL | PK | Código do lookup | — | 🟡 65% |
| 2 | MEANING | VARCHAR2(80) | NOT NULL | Identificação | Descrição legível do código | — | 🟡 65% |
| 3 | LOOKUP_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo do lookup | — | 🟡 65% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Dados | Descrição detalhada | — | 🟡 60% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo (Y/N) | — | 🟡 65% |
| 6 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início da validade | — | 🟡 60% |
| 7 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de fim da validade | — | 🟡 60% |
| 8 | TAG | VARCHAR2(150) | NULL | Classificação | Tag de categorização | — | 🔴 50% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Consultar significados de códigos OPM
```sql
SELECT v.LOOKUP_CODE, v.MEANING, v.LOOKUP_TYPE
FROM   HWM_TM_OPM_MEANING_V v
WHERE  v.LOOKUP_TYPE = :p_lookup_type
  AND  v.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `LOOKUP_TYPE = :p_type — Filtrar por tipo de lookup`
- `ENABLED_FLAG = 'Y' — Apenas registros ativos`

---

## 🔒 Observações

- View somente leitura — não suporta DML.
- Utilizada como lookup de referência para decodificar códigos internos.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_OPM_MEANING_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmopmeaningv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
