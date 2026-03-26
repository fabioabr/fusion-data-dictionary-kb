---
id: DOC-HCM-537
doc_type: system-doc
title: "IRC_SOURCE_TRACKING — Rastreamento de Fontes de Recrutamento"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - source-tracking
  - fontes
  - irc-source-tracking
aliases:
  - IRC_SOURCE_TRACKING
  - irc_source_tracking
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_SOURCE_TRACKING

## 📌 Visão Geral

Registra o **rastreamento de fontes** (source tracking) de candidatos. Identifica a origem de cada candidatura (site de carreiras, job board, indicacao, agencia, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Identificacao da origem de candidatos por canal
- Analise de ROI de canais de recrutamento
- Otimizacao de investimento em fontes de sourcing
- Relatorios de efetividade de canais

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SOURCE_TRACKING_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do rastreamento | --- | 🟢 90% |
| 2 | SUBMISSION_ID | NUMBER(18) | NULL | FK | ID da candidatura rastreada | IRC_SUBMISSIONS | 🟢 85% |
| 3 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de fonte (career_site, job_board, referral) | --- | 🟡 75% |
| 4 | SOURCE_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da fonte especifica | --- | 🟡 70% |
| 5 | MEDIUM | VARCHAR2(30) | NULL | Classificacao | Meio de acesso (web, mobile, email) | --- | 🟡 65% |
| 6 | CAMPAIGN | VARCHAR2(240) | NULL | Dados | Campanha associada | --- | 🟡 60% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_submissions]] --- via `SUBMISSION_ID` (candidatura rastreada pela origem)

### Tabelas-filha (FK de saída)
- --- Tabela de rastreamento, sem filhas conhecidas

---

## 📎 Uso Típico

### Volume de candidaturas por fonte
```sql
SELECT st.SOURCE_TYPE, st.SOURCE_NAME, COUNT(*) AS total
FROM   IRC_SOURCE_TRACKING st
GROUP BY st.SOURCE_TYPE, st.SOURCE_NAME
ORDER BY total DESC;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_SOURCE_TRACKING](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircsourcetracking.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
