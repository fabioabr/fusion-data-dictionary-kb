---
id: DOC-HCM-596
doc_type: system-doc
title: "PAY_REQUESTS — Requisicoes de Processamento de Folha"
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
  - payroll
  - requests
  - requisicoes
  - pay-requests
aliases:
  - PAY_REQUESTS
  - pay_requests
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_REQUESTS

## 📌 Visão Geral

Armazena as **requisicoes de processamento** de folha (payroll requests). Cada registro representa uma solicitacao de execucao de processamento (calculo, pre-pagamento, pagamento, contabilizacao).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Registro de solicitacoes de processamento de folha
- Fila de processamento e priorizacao
- Rastreamento de status de requisicoes

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da requisicao | --- | 🟢 85% |
| 2 | PAYROLL_ACTION_ID | NUMBER(18) | NULL | FK | ID da acao de folha associada | PAY_PAYROLL_ACTIONS | 🟡 75% |
| 3 | REQUEST_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de requisicao | --- | 🟡 70% |
| 4 | REQUEST_STATUS | VARCHAR2(30) | NULL | Classificacao | Status da requisicao | --- | 🟡 70% |
| 5 | SUBMITTED_DATE | TIMESTAMP | NULL | Dados | Data de submissao | --- | 🟡 70% |
| 6 | COMPLETED_DATE | TIMESTAMP | NULL | Dados | Data de conclusao | --- | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pay_payroll_actions]] --- via `PAYROLL_ACTION_ID` (aÃ§Ã£o de folha solicitada)

### Tabelas-filha (FK de saída)
- --- Tabela de requisicao, sem filhas conhecidas

---

## 📎 Uso Típico

### Requisicoes de uma acao de folha
```sql
SELECT r.REQUEST_ID, r.REQUEST_TYPE, r.REQUEST_STATUS, r.SUBMITTED_DATE
FROM   PAY_REQUESTS r
WHERE  r.PAYROLL_ACTION_ID = :p_action_id;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — PAY_REQUESTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payrequests.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
