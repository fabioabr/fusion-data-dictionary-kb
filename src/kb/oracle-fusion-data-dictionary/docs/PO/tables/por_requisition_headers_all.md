---
id: DOC-PO-065
doc_type: system-doc
title: "POR_REQUISITION_HEADERS_ALL — Cabeçalhos de Requisições de Compra"
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
  - requisicoes
  - cabecalho
  - purchase-requisition
aliases:
  - POR_REQUISITION_HEADERS_ALL
  - por_requisition_headers_all
  - cabecalho-requisicoes
  - requisicao-compra-header
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_REQUISITION_HEADERS_ALL

## 📌 Visão Geral

Armazena os **cabeçalhos de requisições de compra** do módulo Procurement. Cada registro representa uma requisição de compra com informações de identificação, solicitante, status de aprovação, tipo e datas. É a tabela-mãe das linhas de requisição (`POR_REQUISITION_LINES_ALL`) e das distribuições (`POR_REQ_DISTRIBUTIONS_ALL`).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `REQ_BU_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Criação de requisições:** Registro do pedido de compra pelo requisitante (self-service ou profissional).
- **Workflow de aprovação:** Controle do ciclo de aprovação da requisição (draft → submitted → approved → ordered).
- **Conversão para PO:** Base para criação automática ou manual de Purchase Orders.
- **Acompanhamento:** Rastreamento do ciclo de vida da requisição até o atendimento completo.
- **Relatórios gerenciais:** Análises de volume, valor e tempo de ciclo de requisições.
- **Auditoria:** Registro completo de quem requisitou, quando e por que.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cabeçalho da requisição | — | 🟢 100% |
| 2 | REQUISITION_NUMBER | VARCHAR2(20) | NOT NULL | Identificação | Número visível da requisição | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição/justificativa da requisição | — | 🟢 95% |
| 4 | AUTHORIZATION_STATUS | VARCHAR2(25) | NOT NULL | Status | Status de aprovação: INCOMPLETE, IN PROCESS, PRE-APPROVED, APPROVED, REJECTED, CANCELLED, WITHDRAWN | — | 🟢 100% |
| 5 | TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da requisição: PURCHASE, INTERNAL | — | 🟢 95% |
| 6 | PREPARER_ID | NUMBER(18) | NOT NULL | FK | Preparador da requisição (pessoa que digitou) | [[per_all_people_f]] | 🟢 95% |
| 7 | REQUISITION_DATE | DATE | NOT NULL | Data | Data da requisição | — | 🟢 100% |
| 8 | REQ_BU_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit da requisição | [[hr_all_organization_units_f]] | 🟢 95% |
| 9 | FUNDS_STATUS | VARCHAR2(25) | NULL | Controle | Status de reserva de fundos (budgetary control) | — | 🟡 80% |
| 10 | DOCUMENT_STATUS | VARCHAR2(25) | NULL | Status | Status do documento no ciclo de vida | — | 🟢 90% |
| 11 | EMERGENCY_PO_NUM | VARCHAR2(20) | NULL | Referência | Número da PO de emergência associada | — | 🟡 75% |
| 12 | INTERFACE_SOURCE_CODE | VARCHAR2(25) | NULL | Integração | Código da origem (se criada via interface) | — | 🟢 90% |
| 13 | APPROVED_DATE | DATE | NULL | Data | Data de aprovação final | — | 🟡 80% |
| 14 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 90% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |
| 20 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 90% |
| 21 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PREPARER_ID` (preparador da requisição)
- [[hr_all_organization_units_f]] — via `REQ_BU_ID` (business unit da requisição de compra)

### Tabelas-filha (FK de saída)
- [[por_requisition_lines_all]] — via `REQUISITION_HEADER_ID` (linhas da requisição)
- [[por_req_distributions_all]] — via `REQUISITION_HEADER_ID` (distribuições contábeis, indiretamente via linhas)
- [[por_line_locations_sum_v]] — via `REQUISITION_HEADER_ID` (locais de entrega sumarizados)

---

## 📎 Uso Típico

### Requisições aprovadas por período
```sql
SELECT rh.REQUISITION_NUMBER,
       rh.DESCRIPTION,
       rh.REQUISITION_DATE,
       rh.AUTHORIZATION_STATUS,
       rh.APPROVED_DATE
FROM   POR_REQUISITION_HEADERS_ALL rh
WHERE  rh.AUTHORIZATION_STATUS = 'APPROVED'
  AND  rh.REQUISITION_DATE BETWEEN :start_date AND :end_date
  AND  rh.REQ_BU_ID = :p_bu_id;
```

### Contagem de requisições por status
```sql
SELECT rh.AUTHORIZATION_STATUS,
       COUNT(*) AS qtd
FROM   POR_REQUISITION_HEADERS_ALL rh
WHERE  rh.REQ_BU_ID = :p_bu_id
GROUP BY rh.AUTHORIZATION_STATUS;
```

### Filtros comuns
- `AUTHORIZATION_STATUS = 'APPROVED'` — Requisições aprovadas
- `AUTHORIZATION_STATUS = 'IN PROCESS'` — Em processo de aprovação
- `TYPE_LOOKUP_CODE = 'PURCHASE'` — Requisições de compra (não internas)

---

## 🔒 Observações

- O `AUTHORIZATION_STATUS` controla todo o ciclo de vida: **INCOMPLETE** → **IN PROCESS** → **PRE-APPROVED** → **APPROVED** → (convertida em PO).
- `TYPE_LOOKUP_CODE = 'PURCHASE'` são requisições externas; `INTERNAL` são transferências entre organizações.
- O campo `PREPARER_ID` referencia quem digitou a requisição, que pode ser diferente do requisitante (requester) nas linhas.
- Requisições canceladas mantêm `AUTHORIZATION_STATUS = 'CANCELLED'` para histórico.
- O `FUNDS_STATUS` é populado apenas quando budgetary control está habilitado na business unit.

---

## 📚 Referências

- [Oracle Docs — POR_REQUISITION_HEADERS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/porrequisitionheadersall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
