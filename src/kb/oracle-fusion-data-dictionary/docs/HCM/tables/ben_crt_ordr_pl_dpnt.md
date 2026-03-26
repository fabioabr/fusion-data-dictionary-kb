---
id: DOC-HCM-036
doc_type: system-doc
title: "BEN_CRT_ORDR_PL_DPNT — Planos e Dependentes de Ordens Judiciais"
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
  - benefits
  - planos-dependentes-ordem
  - court-order-plans
aliases:
  - BEN_CRT_ORDR_PL_DPNT
  - ben_crt_ordr_pl_dpnt
  - planos-dependentes-ordem
  - court-order-plan-dpnt
  - ben-crt-ordr-pl-dpnt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_CRT_ORDR_PL_DPNT

## 📌 Visão Geral

Armazena os **planos e dependentes** especificados em ordens judiciais de benefícios. Detalha quais planos e quais dependentes devem ser cobertos conforme determinação judicial.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento da ordem:** Especifica planos e dependentes impactados.
- **Cobertura obrigatória:** Garante que dependentes judicialmente determinados sejam cobertos.
- **Auditoria:** Rastreabilidade de cobertura por ordem judicial.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CRT_ORDR_PL_DPNT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 85% |
| 2 | CRT_ORDR_ID | NUMBER(18) | NOT NULL | FK | Ordem judicial | [[ben_crt_ordr_f]] | 🟢 90% |
| 3 | PL_ID | NUMBER(18) | NULL | FK | Plano de benefício | [[ben_pl_f]] | 🟡 80% |
| 4 | DPNT_PERSON_ID | NUMBER(18) | NULL | FK | Dependente | [[per_all_people_f]] | 🟡 80% |
| 5 | COVERAGE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de cobertura | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ben_crt_ordr_f]] — via `CRT_ORDR_ID` (ordem judicial do dependente de beneficio)
- [[ben_pl_f]] — via `PL_ID` (plano de beneficio da ordem judicial)
- [[per_all_people_f]] — via `DPNT_PERSON_ID` (dependente na ordem judicial de beneficio)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Consulta de planos e dependentes de ordens judiciais
```sql
SELECT * FROM BEN_CRT_ORDR_PL_DPNT
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Planos e Dependentes de Ordens Judiciais).

---

## 📚 Referências

- [Oracle Docs — BEN_CRT_ORDR_PL_DPNT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/bencrtordrpldpnt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
