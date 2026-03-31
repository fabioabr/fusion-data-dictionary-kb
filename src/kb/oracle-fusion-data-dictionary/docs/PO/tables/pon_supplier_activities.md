---
id: DOC-PO-035
doc_type: system-doc
title: "PON_SUPPLIER_ACTIVITIES — Atividades de Fornecedores em Negociações"
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
  - negociacao
  - fornecedores
  - atividades
aliases:
  - PON_SUPPLIER_ACTIVITIES
  - pon_supplier_activities
  - atividades-fornecedores-sourcing
  - supplier-activities
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_SUPPLIER_ACTIVITIES

## Visão Geral

Armazena as **atividades dos fornecedores** em processos de negociação no módulo Oracle Sourcing. Cada registro representa uma ação ou evento realizado por um fornecedor no contexto de uma negociação — como visualização da negociação, download de anexos, submissão de proposta, aceitação de termos e outras interações com o sistema de sourcing.

> [!note] Módulo PON
> O prefixo `PON` identifica tabelas do submódulo **Oracle Sourcing / Negotiations**. Esta tabela registra o log de atividades dos fornecedores participantes de processos competitivos.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Rastreamento de participação:** Monitoramento das ações de fornecedores em negociações (quem viu, quem baixou, quem respondeu).
- **Auditoria de processo:** Evidência de que fornecedores tiveram acesso às informações do processo licitatório.
- **Análise de engajamento:** Identificação de fornecedores mais ativos e responsivos.
- **Compliance legal:** Comprovação de transparência e isonomia no acesso à informação.
- **Gestão de prazos:** Monitoramento de atividades em relação aos prazos de submissão de propostas.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTIVITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atividade | — | 🟡 70% |
| 2 | AUCTION_HEADER_ID | NUMBER(18) | NOT NULL | FK | Negociação/leilão relacionado | [[pon_auction_headers_all]] | 🟡 75% |
| 3 | VENDOR_ID | NUMBER(18) | NOT NULL | FK | Fornecedor que realizou a atividade | [[poz_suppliers]] | 🟡 75% |
| 4 | VENDOR_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor | [[poz_supplier_sites_all_m]] | 🟡 65% |
| 5 | ACTIVITY_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de atividade (VIEW, DOWNLOAD, SUBMIT_BID, ACCEPT_TERMS, DECLINE) | — | 🟡 70% |
| 6 | ACTIVITY_DATE | TIMESTAMP | NOT NULL | Data | Data/hora da atividade | — | 🟡 75% |
| 7 | ACTIVITY_DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição detalhada da atividade | — | 🟡 60% |
| 8 | BID_NUMBER | NUMBER(18) | NULL | FK | Proposta relacionada (quando aplicável) | [[pon_bid_headers]] | 🟡 60% |
| 9 | CONTACT_ID | NUMBER(18) | NULL | FK | Contato do fornecedor que realizou a atividade | [[hz_parties]] | 🟡 60% |
| 10 | IP_ADDRESS | VARCHAR2(60) | NULL | Auditoria | Endereço IP de origem da atividade | — | 🟡 50% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 15 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[pon_auction_headers_all]] — via `AUCTION_HEADER_ID` (negociação associada à atividade do fornecedor)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor que realizou a atividade)
- [[poz_supplier_sites_all_m]] — via `VENDOR_SITE_ID` (site do fornecedor)
- [[pon_bid_headers]] — via `BID_NUMBER` (proposta vinculada à atividade do fornecedor)
- [[hz_parties]] — via `CONTACT_ID` (contato do fornecedor)

### Tabelas-filha (FK de saída)
- Sem tabelas-filha conhecidas diretamente.

---

## Uso Típico

### Atividades de fornecedores em uma negociação
```sql
SELECT sa.VENDOR_ID, sa.ACTIVITY_TYPE, sa.ACTIVITY_DATE,
       sa.ACTIVITY_DESCRIPTION
FROM   PON_SUPPLIER_ACTIVITIES sa
WHERE  sa.AUCTION_HEADER_ID = :p_auction_header_id
ORDER BY sa.ACTIVITY_DATE DESC;
```

### Fornecedores que visualizaram mas não submeteram proposta
```sql
SELECT DISTINCT sa.VENDOR_ID
FROM   PON_SUPPLIER_ACTIVITIES sa
WHERE  sa.AUCTION_HEADER_ID = :p_auction_header_id
  AND  sa.ACTIVITY_TYPE = 'VIEW'
  AND  sa.VENDOR_ID NOT IN (
         SELECT sa2.VENDOR_ID
         FROM   PON_SUPPLIER_ACTIVITIES sa2
         WHERE  sa2.AUCTION_HEADER_ID = :p_auction_header_id
           AND  sa2.ACTIVITY_TYPE = 'SUBMIT_BID'
       );
```

---

## Observações

- O campo `ACTIVITY_TYPE` registra o tipo específico da interação — os valores exatos podem variar por release e configuração.
- Esta tabela é essencialmente um **log de eventos** e tende a crescer significativamente em ambientes com muitas negociações ativas.
- O campo `IP_ADDRESS` pode ou não estar preenchido dependendo da configuração de segurança do ambiente.
- A combinação `AUCTION_HEADER_ID + VENDOR_ID + ACTIVITY_DATE` fornece a linha do tempo completa de interações de um fornecedor com uma negociação.
- Dados desta tabela são relevantes para demonstrar compliance em processos de auditoria de compras.

---

## Referências

- [Oracle Docs — PON_SUPPLIER_ACTIVITIES](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/ponsupplieractivities.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[negotiationsupplieractivityp1|NegotiationSupplierActivityP1]] (PO · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| AUCTION_HEADER_ID_ORIG_AMEND | AuctionHeaderIdOrigAmend | ✅ |
| BID_NUMBER | BidNumber | ✅ |
| BID_STATUS | BidStatus | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_ACTION_FLAG | LastActionFlag | ✅ |
| LAST_ACTIVITY_CODE | LastActivityCode | ✅ |
| LAST_ACTIVITY_TIME | LastActivityTime | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SESSION_ID | SessionId | ✅ |
| TRADING_PARTNER_CONTACT_ID | TradingPartnerContactId | ✅ |
| TRADING_PARTNER_ID | TradingPartnerId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |

### [[negotiationsupplieractivitypvo|NegotiationSupplierActivityPVO]] (PO · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUCTION_HEADER_ID | AuctionHeaderId | ✅ |
| AUCTION_HEADER_ID_ORIG_AMEND | AuctionHeaderIdOrigAmend | ✅ |
| BID_NUMBER | BidNumber | ✅ |
| BID_STATUS | BidStatus | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_ACTION_FLAG | LastActionFlag | ✅ |
| LAST_ACTIVITY_CODE | LastActivityCode | ✅ |
| LAST_ACTIVITY_TIME | LastActivityTime | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SESSION_ID | SessionId | ✅ |
| TRADING_PARTNER_CONTACT_ID | TradingPartnerContactId | ✅ |
| TRADING_PARTNER_ID | TradingPartnerId | ✅ |
| VENDOR_SITE_ID | VendorSiteId | ✅ |
