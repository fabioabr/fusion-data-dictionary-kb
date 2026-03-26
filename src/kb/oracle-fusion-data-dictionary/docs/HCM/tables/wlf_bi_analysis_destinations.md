---
id: DOC-HCM-728
doc_type: system-doc
title: "WLF_BI_ANALYSIS_DESTINATIONS — Destinos de Análise BI (Learning)"
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
  - learning
  - workforce-learning
  - bi-analytics
aliases:
  - WLF_BI_ANALYSIS_DESTINATIONS
  - wlf_bi_analysis_destinations
  - wlf-bi-analysis-destinations
  - destinos-análise-bi-learning
  - bi-analysis-destinations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_BI_ANALYSIS_DESTINATIONS

## Visão Geral

Armazena os **destinos de análises BI** no módulo Workforce Learning, definindo para onde os dados de aprendizado são exportados ou projetados para fins analíticos.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Integração BI** — define destinos para extração de dados de learning para ferramentas analíticas.
- **Dashboards de treinamento** — suporta a configuração de análises pré-construídas.
- **Relatórios de eficácia** — direciona dados de aprendizado para análises de ROI.
- **Governança de dados** — controla quais análises recebem dados de learning.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BI_ANALYSIS_DESTINATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único do destino | — | 🟡 75% |
| 2 | ANALYSIS_NAME | VARCHAR2(240) | NULL | Identificação | Nome da análise BI | — | 🟡 70% |
| 3 | DESTINATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de destino (OTBI, BICC, etc.) | — | 🟡 70% |
| 4 | DESTINATION_PATH | VARCHAR2(1000) | NULL | Dados | Caminho/URL do destino analítico | — | 🟡 65% |
| 5 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado fonte dos dados | WLF_LEARNING_ITEMS_F | 🟡 70% |
| 6 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Controle | Indica se o destino está ativo (Y/N) | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Destinos BI ativos
```sql
SELECT bad.ANALYSIS_NAME, bad.DESTINATION_TYPE, bad.DESTINATION_PATH
FROM   WLF_BI_ANALYSIS_DESTINATIONS bad
WHERE  bad.ACTIVE_FLAG = 'Y'
ORDER BY bad.ANALYSIS_NAME;
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Apenas destinos ativos
- `DESTINATION_TYPE = 'OTBI'` — Apenas análises Oracle Transactional BI

---

## Observações

- Tabela de configuração — sem sufixo _F (não é date-effective).
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Utilizada para integração com OTBI e BICC (BI Cloud Connector).
- Confiança geral mais baixa — estrutura inferida por naming conventions.

---

## Referências

- [Oracle Docs — WLF_BI_ANALYSIS_DESTINATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfbianalysisdestinations.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
