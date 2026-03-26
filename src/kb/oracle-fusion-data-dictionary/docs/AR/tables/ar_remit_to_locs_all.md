---
id: DOC-AR-065
doc_type: system-doc
title: "AR_REMIT_TO_LOCS_ALL — Locais de Remessa (Remit-To Locations)"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, remit-to, locais-remessa, endereco]
aliases: [AR_REMIT_TO_LOCS_ALL, ar_remit_to_locs_all, remit_to_locs, locais_remessa, remit_to_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_REMIT_TO_LOCS_ALL

> [!note] Sufixo _ALL
> Tabela particionada por `ORG_ID`. O sufixo `_ALL` indica que contém dados de todas as business units. Acessos via views sem sufixo filtram automaticamente pelo contexto de segurança da sessão.

## 📌 Visão Geral

Tabela de locais de remessa (remit-to locations) do Accounts Receivable. Define os endereços para os quais clientes devem enviar pagamentos, podendo variar por business unit e país. Esses endereços são impressos nas faturas enviadas aos clientes.

## 🧠 Propósito de Negócio

O endereço de remessa (remit-to) indica ao cliente para onde enviar o pagamento. É impresso nas faturas e documentos de cobrança. A configuração por país e business unit permite que empresas com múltiplas sedes direcionem pagamentos para o local mais adequado (ex.: filial mais próxima do cliente, banco específico por região). No contexto brasileiro, pode indicar dados bancários para depósito ou endereço de correspondência.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | REMIT_TO_LOC_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do local de remessa. | PK | 🟢 100% |
| 2 | ADDRESS_ID | NUMBER(15) | NOT NULL | FK para HZ_LOCATIONS ou HR_LOCATIONS. Endereço físico. | FK | 🟢 100% |
| 3 | COUNTRY | VARCHAR2(60) | NOT NULL | Código do país para o qual este local é válido. | Negócio | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Status ativo/inativo (A = Ativo, I = Inativo). | Controle | 🟢 100% |
| 5 | FLAG | VARCHAR2(1) | NULL | Flag indicando se é o local padrão (Y/N). | Controle | 🟡 75% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 7 | ATTRIBUTE1 | VARCHAR2(150) | NULL | Atributo descritivo flexível 1. | DFF | 🟢 100% |
| 8 | ATTRIBUTE2 | VARCHAR2(150) | NULL | Atributo descritivo flexível 2. | DFF | 🟢 100% |
| 9 | ORG_ID | NUMBER(15) | NOT NULL | Identificador da business unit (Operating Unit). | Partição | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **HZ_LOCATIONS / HR_LOCATIONS** — Endereço físico do local de remessa (N:1 via `ADDRESS_ID`).
- **RA_CUSTOMER_TRX_ALL** — Transações que referenciam este local de remessa.

## 📎 Uso Típico

```sql
-- Locais de remessa ativos por país e business unit
SELECT rtl.REMIT_TO_LOC_ID,
       rtl.ADDRESS_ID,
       rtl.COUNTRY,
       rtl.FLAG AS local_padrao
  FROM AR_REMIT_TO_LOCS_ALL rtl
 WHERE rtl.ORG_ID = :p_org_id
   AND rtl.STATUS = 'A'
 ORDER BY rtl.COUNTRY;
```

## 🔒 Observações

- O sistema seleciona o local de remessa automaticamente com base no país do cliente e na business unit da transação.
- `FLAG = 'Y'` indica o local padrão quando múltiplos endereços estão disponíveis para o mesmo país.
- Alterações no endereço de remessa afetam apenas novas faturas; faturas já emitidas mantêm o endereço original.
- Filtrar sempre por `ORG_ID` para garantir contexto correto de business unit.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Remit-To Addresses Configuration Guide.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
