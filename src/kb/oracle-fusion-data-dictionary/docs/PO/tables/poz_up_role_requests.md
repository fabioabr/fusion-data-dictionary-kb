---
id: DOC-PO-107
doc_type: system-doc
title: "POZ_UP_ROLE_REQUESTS — Requisicoes de Papeis de Fornecedores"
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
  - fornecedores
  - supplier-management
  - poz
aliases:
  - POZ_UP_ROLE_REQUESTS
  - poz_up_role_requests
  - poz-up-role-requests
  - poz-up
  - requisicoes-de-papeis-de-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_UP_ROLE_REQUESTS

## 📌 Visão Geral

Armazena as **requisicoes de papeis (roles) solicitados durante o registro ou atualizacao de fornecedores**. Cada registro representa a solicitacao de um papel (ex.: Spend Authorized, Sourcing).


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Atribuicao de papeis:** Solicitacao durante onboarding.
- **Expansao de escopo:** Papeis adicionais para fornecedores existentes.
- **Workflow de aprovacao:** Ciclo de aprovacao de papeis.
- **Auditoria:** Rastreamento de papeis solicitados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ROLE_REQUEST_ID | NUMBER(18) | NOT NULL | PK | ID da requisicao de papel | — | 🟡 75% |
| 2 | UP_REQUEST_ID | NUMBER(18) | NOT NULL | FK | Requisicao pai | [[poz_up_requests]] | 🟢 90% |
| 3 | ROLE_ID | NUMBER(18) | NOT NULL | FK | Papel solicitado | — | 🟡 75% |
| 4 | ROLE_NAME | VARCHAR2(240) | NULL | Classificacao | Nome do papel | — | 🟡 70% |
| 5 | REQUEST_STATUS | VARCHAR2(30) | NULL | Status | Status da requisicao | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_up_requests]] — via `UP_REQUEST_ID` (solicitacao de cadastro do fornecedor)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Papeis por requisicao
```sql
SELECT ROLE_REQUEST_ID, ROLE_NAME, REQUEST_STATUS
FROM   POZ_UP_ROLE_REQUESTS
WHERE  UP_REQUEST_ID = :p_request_id;
```


---

## 🔒 Observações

- Papeis efetivados somente apos aprovacao completa.
- Conjunto de papeis configuravel por implementacao.
- Cada requisicao pode conter multiplos papeis.

---

## 📚 Referências

- [Oracle Docs — POZ_UP_ROLE_REQUESTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
