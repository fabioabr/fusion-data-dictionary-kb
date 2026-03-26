---
id: DOC-HCM-115
doc_type: system-doc
title: "HRA_TMPL_DEFNS_B — Definições de Templates de Avaliação (Base)"
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
  - templates
  - template-definitions
  - hra
aliases:
  - HRA_TMPL_DEFNS_B
  - hra_tmpl_defns_b
  - hra-tmpl-defns-b
  - DOC-HCM-115
  - definições-de-templates-de-avaliação-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_TMPL_DEFNS_B

## 📌 Visão Geral

Armazena as **definições base dos templates** de avaliação de performance. Templates são modelos que combinam seções, papéis, etapas e regras para estruturar o processo de avaliação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de avaliação:** Template master que define o processo completo.
- **Composição de seções:** Quais seções compõem o template.
- **Workflow:** Definição de etapas e papéis do processo.
- **Reutilização:** Templates são reutilizados em múltiplos ciclos.
- **Base para tradução:** Complementada por `HRA_TMPL_DEFNS_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TMPL_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template | — | 🟢 90% |
| 2 | TMPL_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do template | — | 🟡 80% |
| 3 | TMPL_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (ANNUAL_REVIEW, MID_YEAR, PROBATION, 360) | — | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (ACTIVE, INACTIVE, DRAFT) | — | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NULL | Data | Inicio de vigencia | — | 🟡 80% |
| 6 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim de vigencia | — | 🟡 80% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versão do objeto | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhum relacionamento de entrada identificado até o momento.

### Tabelas-filha (FK de saída)
- [[hra_tmpl_defns_tl]] — via `TMPL_DEFN_ID` (traducoes multilingue do registro)
- [[hra_evaluations]] — via `TMPL_DEFN_ID` (avaliações que usam este template)

---

## 📎 Uso Típico

### Templates ativos
```sql
SELECT td.TMPL_DEFN_ID, td.TMPL_CODE, td.TMPL_TYPE, td.STATUS_CODE
FROM   HRA_TMPL_DEFNS_B td
WHERE  td.STATUS_CODE = 'ACTIVE';
```

### Templates por tipo
```sql
SELECT td.TMPL_TYPE, COUNT(*) AS qtd
FROM   HRA_TMPL_DEFNS_B td
GROUP BY td.TMPL_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- O `TMPL_TYPE` categoriza: ANNUAL_REVIEW, MID_YEAR, PROBATION, 360_FEEDBACK.
- Templates ACTIVE são utilizados para criação de novos documentos de avaliação.
- O `OBJECT_VERSION_NUMBER` controla concorrência otimista.

---

## 📚 Referências

- [Oracle Docs — HRA_TMPL_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hratmpldefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
