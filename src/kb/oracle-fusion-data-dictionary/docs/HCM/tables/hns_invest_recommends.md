---
id: DOC-HCM-110
doc_type: system-doc
title: "HNS_INVEST_RECOMMENDS — Recomendações de Investigações"
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
  - health-safety
  - recomendacoes
  - investigacao
  - hns
aliases:
  - HNS_INVEST_RECOMMENDS
  - hns_invest_recommends
  - hns-invest-recommends
  - DOC-HCM-110
  - recomendações-de-investigações
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INVEST_RECOMMENDS

## 📌 Visão Geral

Armazena as **recomendações** geradas a partir de investigações de incidentes — propostas de melhorias, mudanças de procedimento, treinamentos, etc.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Recomendações de melhoria:** Propostas decorrentes da investigação.
- **Plano de ação:** Base para criação de ações corretivas.
- **Prevenção:** Recomendações preventivas para evitar recorrência.
- **Governança:** Rastreamento de implementação de recomendações.
- **Lições aprendidas:** Documentação para base de conhecimento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INVEST_RECOMMEND_ID | NUMBER(18) | NOT NULL | PK | Identificador único da recomendação | — | 🟡 80% |
| 2 | INVESTIGATION_SUMMARY_ID | NUMBER(18) | NOT NULL | FK | Investigação associada | [[hns_investigations_summary]] | 🟢 90% |
| 3 | RECOMMENDATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da recomendação | — | 🟡 75% |
| 4 | DESCRIPTION | VARCHAR2(4000) | NULL | Texto | Descrição da recomendação | — | 🟡 80% |
| 5 | PRIORITY | VARCHAR2(30) | NULL | Classificação | Prioridade (HIGH, MEDIUM, LOW) | — | 🟡 70% |
| 6 | STATUS | VARCHAR2(30) | NULL | Status | Status da implementação | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_investigations_summary]] — via `INVESTIGATION_SUMMARY_ID` (investigacao das recomendacoes)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Recomendações pendentes
```sql
SELECT r.RECOMMENDATION_TYPE, r.DESCRIPTION, r.PRIORITY, r.STATUS
FROM   HNS_INVEST_RECOMMENDS r
WHERE  r.STATUS != 'IMPLEMENTED';
```

### Recomendações por investigação
```sql
SELECT r.RECOMMENDATION_TYPE, r.DESCRIPTION, r.PRIORITY
FROM   HNS_INVEST_RECOMMENDS r
WHERE  r.INVESTIGATION_SUMMARY_ID = :p_investigation_id;
```

---

## 🔒 Observações

- Cada investigação pode gerar múltiplas recomendações.
- Recomendações com prioridade HIGH devem ser implementadas primeiro.
- O `STATUS` rastreia a implementação: OPEN, IN_PROGRESS, IMPLEMENTED.
- Tipos típicos: PROCEDURE (mudança de procedimento), TRAINING (treinamento), EQUIPMENT (equipamento).

---

## 📚 Referências

- [Oracle Docs — HNS_INVEST_RECOMMENDS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinvestrecommends.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
