---
id: DOC-PO-027
doc_type: system-doc
title: "PON_OBJECTIVE_NEGOTIATIONS — Negociações Vinculadas a Objetivos de Programa"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - objectives
  - negotiation
  - sourcing
  - programs
aliases:
  - PON_OBJECTIVE_NEGOTIATIONS
  - pon_objective_negotiations
  - negociacoes-objetivo-programa
  - objective-negotiations
  - pon-obj-negotiations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_OBJECTIVE_NEGOTIATIONS

## 📌 Visão Geral

Tabela de associação que vincula **negociações de sourcing a objetivos** dentro de programas de procurement. Cada registro representa a ligação entre uma negociação específica e um objetivo estratégico definido em [[pon_program_objectives]], permitindo rastrear o progresso do programa através de suas negociações individuais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento de programas:** Vincula negociações individuais aos objetivos estratégicos do programa de sourcing.
- **Medição de progresso:** Permite calcular quantas negociações foram concluídas por objetivo e o progresso geral do programa.
- **Análise de economia:** Agrega savings de negociações individuais para medir a economia total por objetivo.
- **Governança de procurement:** Garante que cada negociação esteja alinhada a um objetivo estratégico documentado.
- **Relatórios OTBI:** Alimenta as views [[pon_neg_agg_to_obj_otbi_v]] e [[pon_obj_agg_to_prog_otbi_v]] para analytics.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | OBJECTIVE_NEGOTIATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação objetivo-negociação | — | 🟢 85% |
| 2 | OBJECTIVE_ID | NUMBER(18) | NOT NULL | FK | Identificador do objetivo do programa | [[pon_program_objectives]] | 🟢 85% |
| 3 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Identificador da negociação (cabeçalho) | — | 🟢 85% |
| 4 | PROGRAM_ID | NUMBER(18) | NOT NULL | FK | Identificador do programa de sourcing | [[pon_program_headers]] | 🟡 75% |
| 5 | NEGOTIATION_STATUS | VARCHAR2(30) | NULL | Classificação | Status da negociação no contexto do objetivo | — | 🟡 70% |
| 6 | ESTIMATED_AMOUNT | NUMBER | NULL | Financeiro | Valor estimado da negociação | — | 🟡 65% |
| 7 | AWARDED_AMOUNT | NUMBER | NULL | Financeiro | Valor adjudicado | — | 🟡 65% |
| 8 | SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Economia realizada (estimado − adjudicado) | — | 🟡 60% |
| 9 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟡 70% |
| 10 | LINK_DATE | DATE | NULL | Data | Data em que a negociação foi vinculada ao objetivo | — | 🟡 60% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_program_objectives]] — via `OBJECTIVE_ID` (objetivo ao qual a negociação está vinculada)
- [[pon_program_headers]] — via `PROGRAM_ID` (programa de sourcing)
- Tabela de cabeçalho de negociação (PON_AUCTION_HEADERS_ALL) — via `AUCTION_HEADER_ID`

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Negociações de um objetivo específico
```sql
SELECT on2.AUCTION_HEADER_ID, on2.NEGOTIATION_STATUS,
       on2.ESTIMATED_AMOUNT, on2.AWARDED_AMOUNT, on2.SAVINGS_AMOUNT
FROM   PON_OBJECTIVE_NEGOTIATIONS on2
WHERE  on2.OBJECTIVE_ID = :p_objective_id
ORDER BY on2.CREATION_DATE;
```

### Progresso de um programa (total por objetivo)
```sql
SELECT on2.OBJECTIVE_ID,
       COUNT(*) AS total_negociacoes,
       SUM(on2.SAVINGS_AMOUNT) AS economia_total,
       COUNT(CASE WHEN on2.NEGOTIATION_STATUS = 'AWARDED' THEN 1 END) AS concluidas
FROM   PON_OBJECTIVE_NEGOTIATIONS on2
WHERE  on2.PROGRAM_ID = :p_program_id
GROUP BY on2.OBJECTIVE_ID;
```

---

## 🔒 Observações

- Esta é uma tabela de **associação N:N** — uma negociação pode estar vinculada a mais de um objetivo (em cenários multi-objetivo), e um objetivo pode ter múltiplas negociações.
- Os campos financeiros (`ESTIMATED_AMOUNT`, `AWARDED_AMOUNT`, `SAVINGS_AMOUNT`) podem ser sincronizados periodicamente com os dados reais da negociação ou preenchidos manualmente.
- A coluna `NEGOTIATION_STATUS` pode refletir o status da negociação no momento do último sync, não necessariamente o status em tempo real.
- Para relatórios analíticos, prefira as views OTBI ([[pon_neg_agg_to_obj_otbi_v]], [[pon_neg_agg_to_prog_otbi_v]]) que já agregam os dados.

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
