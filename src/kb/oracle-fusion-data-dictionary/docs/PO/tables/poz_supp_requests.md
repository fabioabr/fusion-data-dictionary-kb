---
id: DOC-PO-100
doc_type: system-doc
title: "POZ_SUPP_REQUESTS — Solicitações Gerais de Fornecedores"
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
  - supplier-requests
  - solicitacoes
  - workflow
aliases:
  - POZ_SUPP_REQUESTS
  - poz_supp_requests
  - solicitacoes-fornecedor
  - supplier-requests
  - requisicoes-fornecedor
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPP_REQUESTS

## Visão Geral

Armazena as **solicitações gerais relacionadas a fornecedores** no Oracle Fusion Procurement. Funciona como tabela-mestre de requisições que agrupam sub-solicitações (contatos, produtos/serviços, autorizações de gasto, etc.) em um único fluxo de aprovação. Cada registro representa uma requisição unificada que pode conter múltiplas alterações no cadastro de um fornecedor.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de mudanças:** Controla todas as solicitações de alteração no cadastro de fornecedores.
- **Workflow unificado:** Agrupa múltiplas sub-solicitações (contato, produto/serviço, site) em um único fluxo de aprovação.
- **Supplier Portal:** Requisições originadas pelo fornecedor no portal de autoatendimento.
- **Auditoria:** Histórico completo de todas as solicitações de alteração de cadastro.
- **Compliance:** Garante que alterações no cadastro de fornecedores passem por aprovação formal.
- **Rastreabilidade:** Vincula todas as mudanças ao solicitante e aprovador.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SUPP_REQUEST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da solicitação | — | 🟡 75% |
| 2 | REQUEST_NUMBER | VARCHAR2(30) | NULL | Identificação | Número da solicitação (visível ao usuário) | — | 🟡 70% |
| 3 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor alvo da solicitação | [[poz_suppliers]] | 🟡 80% |
| 4 | REQUEST_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: DRAFT, SUBMITTED, APPROVED, REJECTED, WITHDRAWN | — | 🟡 80% |
| 5 | REQUEST_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo: PROFILE_CHANGE, NEW_SITE, NEW_CONTACT, QUALIFICATION | — | 🟡 70% |
| 6 | REQUEST_ORIGIN | VARCHAR2(30) | NULL | Classificação | Origem: SUPPLIER_PORTAL, INTERNAL, INVITATION | — | 🟡 70% |
| 7 | JUSTIFICATION | VARCHAR2(2000) | NULL | Texto livre | Justificativa da solicitação | — | 🟡 65% |
| 8 | SUBMITTED_DATE | DATE | NULL | Data | Data de submissão | — | 🟡 70% |
| 9 | SUBMITTED_BY | NUMBER(18) | NULL | Referência | Usuário que submeteu a solicitação | — | 🟡 65% |
| 10 | APPROVED_DATE | DATE | NULL | Data | Data de aprovação | — | 🟡 70% |
| 11 | APPROVED_BY | NUMBER(18) | NULL | Aprovação | Usuário que aprovou | — | 🟡 65% |
| 12 | REJECTION_REASON | VARCHAR2(2000) | NULL | Texto livre | Motivo da rejeição (se aplicável) | — | 🟡 60% |
| 13 | SUPPLIER_REG_ID | NUMBER(18) | NULL | FK | Registro de fornecedor associado (se aplicável) | [[poz_supplier_registrations]] | 🟡 65% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor alvo)
- [[poz_supplier_registrations]] — via `SUPPLIER_REG_ID` (registro associado)

### Tabelas-filha (FK de saída)

### Tabelas relacionadas

---

## Uso Típico

### Solicitações pendentes por fornecedor
```sql
SELECT sr.SUPP_REQUEST_ID, sr.REQUEST_NUMBER,
       sr.REQUEST_TYPE, sr.REQUEST_ORIGIN,
       sr.SUBMITTED_DATE
FROM   POZ_SUPP_REQUESTS sr
WHERE  sr.VENDOR_ID = :p_vendor_id
  AND  sr.REQUEST_STATUS = 'SUBMITTED'
ORDER BY sr.SUBMITTED_DATE;
```

### Histórico de solicitações por período
```sql
SELECT sr.REQUEST_NUMBER, sr.REQUEST_TYPE,
       sr.REQUEST_STATUS, sr.REQUEST_ORIGIN,
       s.VENDOR_NAME, sr.SUBMITTED_DATE
FROM   POZ_SUPP_REQUESTS sr
JOIN   POZ_SUPPLIERS s ON sr.VENDOR_ID = s.VENDOR_ID
WHERE  sr.CREATION_DATE BETWEEN :start_date AND :end_date
ORDER BY sr.CREATION_DATE DESC;
```

### Métricas de SLA de aprovação
```sql
SELECT sr.REQUEST_TYPE,
       AVG(sr.APPROVED_DATE - sr.SUBMITTED_DATE) AS avg_days_to_approve,
       COUNT(*) AS total_requests
FROM   POZ_SUPP_REQUESTS sr
WHERE  sr.REQUEST_STATUS = 'APPROVED'
  AND  sr.APPROVED_DATE IS NOT NULL
GROUP BY sr.REQUEST_TYPE;
```

---

## Observações

- Esta tabela funciona como **cabeçalho** de solicitações; os detalhes estão nas tabelas-filha (`POZ_CONTACT_REQUESTS`, `POZ_PRODUCT_SERVICE_REQUESTS`, etc.).
- O ciclo de vida segue: DRAFT → SUBMITTED → APPROVED/REJECTED/WITHDRAWN.
- Solicitações do tipo `SUPPLIER_PORTAL` são originadas por contatos de fornecedores no autoatendimento.
- O campo `REQUEST_ORIGIN` diferencia solicitações internas (comprador) de externas (fornecedor).
- Solicitações rejeitadas mantêm o `REJECTION_REASON` para feedback ao solicitante.
- O workflow de aprovação pode ser configurado com múltiplos níveis dependendo do tipo de solicitação.

---

## Referências

- [Oracle Docs — Supplier Requests](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poz-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
