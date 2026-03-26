---
id: DOC-PO-106
doc_type: system-doc
title: "POZ_UP_REQUESTS — Requisicoes de Registro/Atualizacao de Fornecedores"
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
  - POZ_UP_REQUESTS
  - poz_up_requests
  - poz-up-requests
  - poz-up
  - requisicoes-de-registro/atualizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_UP_REQUESTS

## 📌 Visão Geral

Armazena as **requisicoes de registro e atualizacao de fornecedores**. Cada registro representa uma solicitacao de cadastro (novo) ou atualizacao de dados existentes, gerenciada via workflow de aprovacao.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Self-service registration:** Registro de novos fornecedores via portal.
- **Atualizacao cadastral:** Alteracoes de dados (endereco, contatos, bancarios).
- **Workflow de aprovacao:** Ciclo de vida (submetida - aprovada - rejeitada).
- **Onboarding:** Pipeline de qualificacao e validacao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | UP_REQUEST_ID | NUMBER(18) | NOT NULL | PK | ID unico da requisicao | — | 🟢 90% |
| 2 | REQUEST_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | NEW ou UPDATE | — | 🟡 80% |
| 3 | REQUEST_STATUS | VARCHAR2(30) | NOT NULL | Status | DRAFT/SUBMITTED/APPROVED/REJECTED | — | 🟡 80% |
| 4 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Dados | Nome do fornecedor | — | 🟢 90% |
| 5 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor (pos-aprovacao) | [[poz_suppliers]] | 🟢 90% |
| 6 | PARTY_ID | NUMBER(18) | NULL | FK | Party TCA | [[hz_parties]] | 🟢 85% |
| 7 | REQUESTOR_ID | NUMBER(18) | NULL | FK | Solicitante | — | 🟡 75% |
| 8 | SUBMIT_DATE | DATE | NULL | Data | Data de submissao | — | 🟡 80% |
| 9 | APPROVAL_DATE | DATE | NULL | Data | Data de aprovacao | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor da solicitação de atualização cadastral)
- [[hz_parties]] — via `PARTY_ID` (parte solicitante do cadastro de fornecedor)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Requisicoes pendentes
```sql
SELECT UP_REQUEST_ID, SUPPLIER_NAME, REQUEST_TYPE, SUBMIT_DATE
FROM   POZ_UP_REQUESTS
WHERE  REQUEST_STATUS = 'SUBMITTED'
ORDER BY SUBMIT_DATE;
```


---

## 🔒 Observações

- Tipo `NEW` cria fornecedor em `POZ_SUPPLIERS` apos aprovacao.
- Workflow configuravel via Oracle BPM com multiplos niveis.
- Requisicoes rejeitadas mantem motivo registrado.

---

## 📚 Referências

- [Oracle Docs — POZ_UP_REQUESTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
