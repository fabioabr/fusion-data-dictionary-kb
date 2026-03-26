---
id: DOC-HCM-530
doc_type: system-doc
title: "IRC_RF_SHARES — Compartilhamentos de Vagas por Referencia"
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
  - referral-shares
  - compartilhamento
  - irc-rf-shares
aliases:
  - IRC_RF_SHARES
  - irc_rf_shares
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_RF_SHARES

## 📌 Visão Geral

Registra os **compartilhamentos** de vagas realizados por colaboradores no programa de indicacao. Cada registro representa um ato de compartilhar um link de vaga em um canal especifico.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Rastreamento de compartilhamentos de vagas por colaboradores
- Analise de canais mais utilizados para indicacao
- Metricas de engajamento do programa de referral

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SHARE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do compartilhamento | --- | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | ID do colaborador que compartilhou | PER_ALL_PEOPLE_F | 🟢 85% |
| 3 | REQUISITION_ID | NUMBER(18) | NULL | FK | ID da requisicao compartilhada | IRC_REQUISITIONS_B | 🟢 85% |
| 4 | SHARE_CHANNEL | VARCHAR2(30) | NULL | Classificacao | Canal de compartilhamento | --- | 🟡 70% |
| 5 | SHARE_DATE | TIMESTAMP | NULL | Dados | Data/hora do compartilhamento | --- | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] --- via `PERSON_ID` (pessoa que compartilhou a vaga)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisicao compartilhada)

### Tabelas-filha (FK de saída)
- [[irc_rf_req_hits]] --- via `SHARE_ID` (hits gerados pelo compartilhamento)

---

## 📎 Uso Típico

### Compartilhamentos por requisicao
```sql
SELECT rs.SHARE_ID, rs.PERSON_ID, rs.SHARE_CHANNEL, rs.SHARE_DATE
FROM   IRC_RF_SHARES rs
WHERE  rs.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_RF_SHARES](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircrfshares.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
