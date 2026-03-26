---
id: DOC-HCM-072
doc_type: system-doc
title: "CMP_CWB_HRCHY_V — Hierarquia CWB (View)"
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
  - compensation
  - hierarquia-cwb-view
  - cwb-hierarchy-view
aliases:
  - CMP_CWB_HRCHY_V
  - cmp_cwb_hrchy_v
  - hierarquia-cwb-view
  - cwb-hierarchy-view
  - cmp-cwb-hrchy-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_HRCHY_V

## 📌 Visão Geral

View que apresenta a **hierarquia do Compensation Workbench** de forma simplificada para consulta, combinando dados de múltiplas tabelas.

> [!note] Sufixo _V
> O sufixo `_V` indica **view** — consulta pré-montada que combina dados de múltiplas tabelas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta simplificada:** View pré-montada da hierarquia CWB.
- **Relatórios:** Base para relatórios de hierarquia de compensação.
- **Navegação:** Suporte a drill-down na interface do CWB.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MANAGER_ID | NUMBER(18) | NOT NULL | FK | Gestor | [[per_all_people_f]] | 🟢 85% |
| 2 | MANAGER_NAME | VARCHAR2(360) | NULL | Identificação | Nome do gestor | — | 🟡 80% |
| 3 | SUBORDINATE_ID | NUMBER(18) | NOT NULL | FK | Subordinado | [[per_all_people_f]] | 🟢 85% |
| 4 | SUBORDINATE_NAME | VARCHAR2(360) | NULL | Identificação | Nome do subordinado | — | 🟡 80% |
| 5 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | — | 🟡 80% |
| 6 | LEVEL_NUMBER | NUMBER | NULL | Hierarquia | Nível na hierarquia | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `MANAGER_ID` e `SUBORDINATE_ID` (gestor na hierarquia de compensacao)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Hierarquia de um gestor
```sql
SELECT h.SUBORDINATE_NAME, h.LEVEL_NUMBER
FROM   CMP_CWB_HRCHY_V h
WHERE  h.MANAGER_ID = :p_manager_id
ORDER BY h.LEVEL_NUMBER, h.SUBORDINATE_NAME;
```

### Filtros comuns
- `LEVEL_NUMBER = 1` — Subordinados diretos

---

## 🔒 Observações

- View somente leitura — dados derivados de `CMP_CWB_HRCHY_CF_DN` e tabelas de pessoas.
- Inclui nomes para facilitar consultas sem JOINs adicionais.

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_HRCHY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbhrchyv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
