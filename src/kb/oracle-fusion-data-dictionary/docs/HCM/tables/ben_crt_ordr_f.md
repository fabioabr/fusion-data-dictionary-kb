---
id: DOC-HCM-035
doc_type: system-doc
title: "BEN_CRT_ORDR_F — Ordens Judiciais de Benefícios"
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
  - ordens-judiciais
  - court-orders
  - compliance
aliases:
  - BEN_CRT_ORDR_F
  - ben_crt_ordr_f
  - ordens-judiciais-beneficios
  - court-orders
  - ben-crt-ordr
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_CRT_ORDR_F

## 📌 Visão Geral

Armazena as **ordens judiciais** (court orders) que impactam os benefícios dos colaboradores, como ordens de penhor, pensão alimentícia ou determinações judiciais de cobertura de dependentes.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance legal:** Registro de ordens judiciais que afetam benefícios.
- **Cobertura obrigatória:** Determinações judiciais de inclusão de dependentes.
- **Auditoria:** Rastreabilidade de ações judiciais por colaborador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CRT_ORDR_ID | NUMBER(18) | NOT NULL | PK | Identificador único da ordem | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | COURT_ORDER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de ordem judicial | — | 🟡 75% |
| 4 | ORDER_DATE | DATE | NULL | Data | Data da ordem | — | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da vigência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da ordem judicial de beneficio)

### Tabelas-filha (FK de saída)
- [[ben_crt_ordr_pl_dpnt]] — via `CRT_ORDR_ID` (planos/dependentes da ordem)

---

## 📎 Uso Típico

### Consulta de ordens judiciais de benefícios
```sql
SELECT * FROM BEN_CRT_ORDR_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Ordens Judiciais de Benefícios).

---

## 📚 Referências

- [Oracle Docs — BEN_CRT_ORDR_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/bencrtordrf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
