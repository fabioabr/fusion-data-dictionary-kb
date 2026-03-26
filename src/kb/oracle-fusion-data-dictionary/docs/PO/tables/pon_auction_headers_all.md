---
id: DOC-PO-004
doc_type: system-doc
title: "PON_AUCTION_HEADERS_ALL — Cabeçalhos de Negociações"
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
  - sourcing
  - auction-headers
  - negociacoes
aliases:
  - PON_AUCTION_HEADERS_ALL
  - pon_auction_headers_all
  - cabecalhos-negociacao
  - sourcing-headers
  - auction-headers
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_AUCTION_HEADERS_ALL

## Visão Geral

Armazena os **cabeçalhos de todas as negociações** do módulo Oracle Sourcing. É a tabela central do Sourcing, contendo informações de alto nível de cada negociação (RFQ, RFI, Auction, Reverse Auction, Blanket Agreement, etc.) — tipo, status, datas, regras de lances, moeda, comprador responsável e parâmetros de configuração.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de negociações:** Tabela mestra que centraliza todas as negociações de Sourcing.
- **Controle de ciclo de vida:** Status e datas que governam abertura, fechamento, award e cancelamento.
- **Regras de lances:** Configuração de decrement mínimo, auto-extend, sealed bidding, etc.
- **Análise de sourcing:** KPIs de volume, savings, tempo de ciclo e participação de fornecedores.
- **Integração com PO:** Após award, os dados fluem para criação de Purchase Orders ou Blanket Agreements.
- **Compliance:** Auditoria de quem criou, quando publicou, e qual o outcome de cada negociação.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador único da negociação | — | 🟢 100% |
| 2 | DOCUMENT_NUMBER | VARCHAR2(40) | NOT NULL | Identificação | Número do documento visível ao usuário | — | 🟢 95% |
| 3 | AUCTION_TITLE | VARCHAR2(240) | NULL | Identificação | Título descritivo da negociação | — | 🟢 95% |
| 4 | AUCTION_STATUS | VARCHAR2(30) | NOT NULL | Status | Status da negociação: DRAFT, ACTIVE, PAUSED, CLOSED, CANCELLED, AMENDED, AWARD_COMPLETED | — | 🟢 95% |
| 5 | AUCTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo: REVERSE_AUCTION, RFQ, RFI, BUYER_AUCTION | — | 🟢 90% |
| 6 | DOCTYPE_ID | NUMBER(18) | NULL | FK | Tipo de documento de negociação | [[pon_auc_doctypes_b]] | 🟢 90% |
| 7 | TRADING_PARTNER_ID | NUMBER(18) | NOT NULL | FK | Organização compradora (enterprise) | [[hz_parties]] | 🟢 90% |
| 8 | TRADING_PARTNER_NAME | VARCHAR2(240) | NULL | Identificação | Nome da organização compradora (desnormalizado) | — | 🟡 80% |
| 9 | TRADING_PARTNER_CONTACT_ID | NUMBER(18) | NULL | FK | Contato do comprador responsável | [[per_all_people_f]] | 🟢 85% |
| 10 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Moeda | Código da moeda da negociação (ISO 4217) | [[fnd_currencies]] | 🟢 95% |
| 11 | OPEN_BIDDING_DATE | DATE | NULL | Data | Data/hora de abertura do período de lances | — | 🟢 95% |
| 12 | CLOSE_BIDDING_DATE | DATE | NULL | Data | Data/hora de encerramento do período de lances | — | 🟢 95% |
| 13 | PUBLISH_DATE | DATE | NULL | Data | Data de publicação da negociação | — | 🟢 90% |
| 14 | AWARD_DATE | DATE | NULL | Data | Data de conclusão do award | — | 🟢 85% |
| 15 | OUTCOME | VARCHAR2(30) | NULL | Classificação | Resultado da negociação: BLANKET, CONTRACT, STANDARD_PO, NONE | — | 🟢 90% |
| 16 | CONTRACT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de contrato resultante | — | 🟡 75% |
| 17 | BID_VISIBILITY_CODE | VARCHAR2(30) | NULL | Regras | Visibilidade de lances: OPEN, SEALED, PARTIALLY_SEALED | — | 🟢 85% |
| 18 | ALLOW_WITHDRAW_FLAG | VARCHAR2(1) | NULL | Regras | Permite retirada de lance (Y/N) | — | 🟡 75% |
| 19 | AUTO_EXTEND_FLAG | VARCHAR2(1) | NULL | Regras | Auto-extensão do prazo se lance recebido nos últimos minutos (Y/N) | — | 🟢 85% |
| 20 | AMENDMENT_NUMBER | NUMBER | NULL | Controle | Número da emenda (0 = original) | — | 🟢 85% |
| 21 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Status | Status de aprovação do documento | — | 🟢 85% |
| 22 | AWARD_STATUS | VARCHAR2(30) | NULL | Status | Status do award: NO, PARTIAL, COMPLETED | — | 🟢 85% |
| 23 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 24 | REQUISITION_HEADER_ID | NUMBER(18) | NULL | FK | Requisição de compra originadora | [[por_requisition_headers_all]] | 🟡 75% |
| 25 | PO_HEADER_ID | NUMBER(18) | NULL | FK | Ordem de compra gerada após award | [[po_headers_all]] | 🟡 75% |
| 26 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 27 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 28 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 29 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 30 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 31 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 32 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auc_doctypes_b]] — via `DOCTYPE_ID` (tipo de documento de negociação)
- [[hz_parties]] — via `TRADING_PARTNER_ID` (organização compradora)
- [[per_all_people_f]] — via `TRADING_PARTNER_CONTACT_ID` (contato responsável)
- [[fnd_currencies]] — via `CURRENCY_CODE` (moeda da negociação de compras)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da negociação de compras)
- [[por_requisition_headers_all]] — via `REQUISITION_HEADER_ID` (requisição de origem)

### Tabelas-filha (FK de saída)
- [[pon_auction_item_prices_all]] — via `AUCTION_HEADER_ID` (linhas de itens/preços)
- [[pon_auction_attributes]] — via `AUCTION_HEADER_ID` (atributos de itens)
- [[pon_auction_sections]] — via `AUCTION_HEADER_ID` (seções da negociação)
- [[pon_bidding_parties]] — via `AUCTION_HEADER_ID` (fornecedores convidados)
- [[pon_acknowledgements]] — via `AUCTION_HEADER_ID` (confirmações de participação)
- [[pon_action_history]] — via `AUCTION_HEADER_ID` (histórico de ações)
- [[po_headers_all]] — via `PO_HEADER_ID` (ordem de compra resultante)

---

## Uso Típico

### Negociações ativas por business unit
```sql
SELECT ah.DOCUMENT_NUMBER, ah.AUCTION_TITLE,
       ah.AUCTION_TYPE, ah.AUCTION_STATUS,
       ah.OPEN_BIDDING_DATE, ah.CLOSE_BIDDING_DATE,
       ah.CURRENCY_CODE
FROM   PON_AUCTION_HEADERS_ALL ah
WHERE  ah.ORG_ID = :p_org_id
  AND  ah.AUCTION_STATUS = 'ACTIVE'
ORDER BY ah.CLOSE_BIDDING_DATE;
```

### Negociações concluídas com award
```sql
SELECT ah.DOCUMENT_NUMBER, ah.AUCTION_TITLE,
       ah.OUTCOME, ah.AWARD_DATE, ah.AWARD_STATUS
FROM   PON_AUCTION_HEADERS_ALL ah
WHERE  ah.AWARD_STATUS = 'COMPLETED'
  AND  ah.AWARD_DATE BETWEEN :start_date AND :end_date
  AND  ah.ORG_ID = :p_org_id;
```

### Filtros comuns
- `AUCTION_STATUS = 'ACTIVE'` — Negociações em andamento
- `AUCTION_STATUS = 'CLOSED'` — Negociações encerradas
- `AUCTION_TYPE = 'RFQ'` — Solicitações de cotação
- `AWARD_STATUS = 'COMPLETED'` — Negociações com award finalizado
- `AMENDMENT_NUMBER = 0` — Documento original (sem emendas)

---

## Observações

- Esta é a **tabela central** do módulo Sourcing — todas as demais tabelas `PON_*` referenciam `AUCTION_HEADER_ID`.
- O campo `AUCTION_STATUS` controla a máquina de estados: DRAFT → ACTIVE → CLOSED → AWARD_COMPLETED (ou CANCELLED em qualquer ponto).
- Emendas (amendments) criam novos registros com `AMENDMENT_NUMBER > 0`, mantendo o mesmo `DOCUMENT_NUMBER`.
- O campo `OUTCOME` define o tipo de documento gerado após award: BLANKET (acordo-quadro), CONTRACT, STANDARD_PO.
- Negociações do tipo `SEALED` (licitação selada) possuem `BID_VISIBILITY_CODE = 'SEALED'`, onde lances só são visíveis após o fechamento.
- O `PO_HEADER_ID` é preenchido apenas após a geração automática da ordem de compra via award.

---

## Referências

- [Oracle Docs — PON_AUCTION_HEADERS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponauctionheadersall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
