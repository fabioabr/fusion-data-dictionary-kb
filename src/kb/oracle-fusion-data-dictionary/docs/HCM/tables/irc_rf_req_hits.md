---
id: DOC-HCM-529
doc_type: system-doc
title: "IRC_RF_REQ_HITS — Hits de Requisicoes em Referencias"
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
  - referral-hits
  - metricas
  - irc-rf-hits
aliases:
  - IRC_RF_REQ_HITS
  - irc_rf_req_hits
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_RF_REQ_HITS

## 📌 Visão Geral

Registra os **hits (visualizacoes/interacoes)** em requisicoes compartilhadas pelo programa de referencias. Rastreia quantas vezes um link de indicacao foi acessado.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Monitoramento de engajamento em links de referencia
- Metricas de alcance do programa de indicacao
- Analise de conversao de visualizacoes em candidaturas

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_HIT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do hit | --- | 🟢 85% |
| 2 | SHARE_ID | NUMBER(18) | NULL | FK | ID do compartilhamento associado | IRC_RF_SHARES | 🟡 75% |
| 3 | REQUISITION_ID | NUMBER(18) | NULL | FK | ID da requisicao visualizada | IRC_REQUISITIONS_B | 🟢 85% |
| 4 | HIT_DATE | TIMESTAMP | NULL | Dados | Data/hora do acesso | --- | 🟡 70% |
| 5 | SOURCE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de fonte do acesso | --- | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_rf_shares]] --- via `SHARE_ID` (compartilhamento que gerou o acesso)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisicao acessada via indicacao)

### Tabelas-filha (FK de saída)
- --- Tabelas de metricas do programa de referencias

---

## 📎 Uso Típico

### Hits recentes por requisicao
```sql
SELECT rh.REQ_HIT_ID, rh.HIT_DATE, rh.SOURCE_TYPE
FROM   IRC_RF_REQ_HITS rh
WHERE  rh.REQUISITION_ID = :p_requisition_id
ORDER BY rh.HIT_DATE DESC;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_RF_REQ_HITS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircrfreqhits.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
