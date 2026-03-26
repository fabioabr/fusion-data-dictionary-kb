---
id: DOC-HCM-113
doc_type: system-doc
title: "HRA_SECTION_DEFNS_B — Definições de Seções de Avaliação (Base)"
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
  - performance-management
  - seções
  - section-definitions
  - hra
aliases:
  - HRA_SECTION_DEFNS_B
  - hra_section_defns_b
  - hra-section-defns-b
  - DOC-HCM-113
  - definições-de-seções-de-avaliação-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_SECTION_DEFNS_B

## 📌 Visão Geral

Armazena as **definições base das seções** que compõem documentos/templates de avaliação de performance. Cada seção agrupa critérios de avaliação (ex: Competências, Objetivos, Desenvolvimento).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de avaliação:** Definição de seções dos documentos de performance.
- **Agrupamento de critérios:** Organização lógica dos itens avaliados.
- **Pesos por seção:** Configuracao de peso de cada seção no resultado final.
- **Templates:** Seções são reutilizadas em múltiplos templates.
- **Base para tradução:** Complementada por `HRA_SECTION_DEFNS_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SECTION_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único da seção | — | 🟢 90% |
| 2 | SECTION_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da seção | — | 🟡 80% |
| 3 | SECTION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (COMPETENCY, GOAL, DEVELOPMENT, OVERALL) | — | 🟡 80% |
| 4 | WEIGHT | NUMBER | NULL | Cálculo | Peso da seção no resultado total (%) | — | 🟡 75% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versão do objeto | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuario que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_section_defns_tl]] — via `SECTION_DEFN_ID` (traducoes multilingue do registro)
- [[hra_eval_sections]] — via `SECTION_DEFN_ID` (seções em avaliações)

---

## 📎 Uso Típico

### Seções ativas
```sql
SELECT sd.SECTION_DEFN_ID, sd.SECTION_CODE, sd.SECTION_TYPE, sd.WEIGHT
FROM   HRA_SECTION_DEFNS_B sd
WHERE  sd.STATUS_CODE = 'ACTIVE';
```

### Seções por tipo
```sql
SELECT sd.SECTION_TYPE, COUNT(*) AS qtd
FROM   HRA_SECTION_DEFNS_B sd
GROUP BY sd.SECTION_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- O `SECTION_TYPE` categoriza: COMPETENCY, GOAL, DEVELOPMENT, OVERALL, FEEDBACK.
- O `WEIGHT` define o percentual de contribuição da seção no score final.
- Seções são blocos reutilizáveis montados em templates de avaliação.

---

## 📚 Referências

- [Oracle Docs — HRA_SECTION_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrasectiondefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
