---
id: DOC-AR-007
doc_type: system-doc
title: "RA_BATCH_SOURCES_ALL — Origens de Transações AR"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-receivable
  - data-dictionary
  - batch-sources
  - fontes-transacao
  - configuracao
aliases:
  - RA_BATCH_SOURCES_ALL
  - ra_batch_sources_all
  - origens-transacoes-ar
  - transaction-sources
  - batch-sources-ar
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_BATCH_SOURCES_ALL

## 📌 Visão Geral

Define as **origens (sources) de transações** do módulo Accounts Receivable, incluindo faturas, notas de crédito e compromissos. Cada registro contém configurações que controlam a **numeração automática** de transações e lotes, permissões de duplicidade e comportamento padrão de importação.

É uma tabela de **configuração fundamental** — toda transação AR referencia obrigatoriamente um batch source, que determina como o documento será numerado, validado e agrupado.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de fontes de transação:** Define como faturas manuais, importadas (AutoInvoice) e de outros módulos são registradas no AR.
- **Numeração automática:** Controla se o sistema gera números sequenciais para transações e lotes automaticamente.
- **Controle de duplicidade:** Permite ou bloqueia transações com números duplicados dentro da mesma fonte.
- **AutoInvoice:** Fontes do tipo "Imported" alimentam o processo de importação automática de faturas.
- **Integração entre módulos:** Módulos como Projects, Order Management e Subscriptions possuem batch sources dedicados.
- **Auditoria e rastreabilidade:** Permite identificar a origem de cada transação para fins de auditoria.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BATCH_SOURCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da fonte de transação | — | 🟢 100% |
| 2 | NAME | VARCHAR2(50) | NOT NULL | Identificação | Nome da fonte de transação | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição livre da fonte | — | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status ativo/inativo (A=Active, I=Inactive) | — | 🟢 100% |
| 5 | BATCH_SOURCE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo da fonte: INV (manual), IMPORTED (AutoInvoice) | — | 🟢 100% |
| 6 | AUTO_TRX_NUMBERING_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Numeração automática de transações (Y/N) | — | 🟢 100% |
| 7 | AUTO_BATCH_NUMBERING_FLAG | VARCHAR2(1) | NOT NULL | Configuração | Numeração automática de lotes (Y/N) | — | 🟢 100% |
| 8 | LAST_BATCH_NUM | NUMBER(15) | NULL | Controle | Último número de lote gerado automaticamente | — | 🟢 100% |
| 9 | DEFAULT_INV_TRX_TYPE | NUMBER(18) | NULL | Configuração | Tipo de transação padrão para faturas | [[ra_cust_trx_types_all]] | 🟢 100% |
| 10 | ALLOW_DUPLICATE_TRX_NUM_FLAG | VARCHAR2(1) | NULL | Configuração | Permite números de transação duplicados (Y/N) | — | 🟢 100% |
| 11 | COPY_DOC_NUMBER_FLAG | VARCHAR2(1) | NULL | Configuração | Copia número de sequência de documento para TRX_NUMBER (Y/N) | — | 🟢 100% |
| 12 | CREDIT_MEMO_BATCH_SOURCE_ID | NUMBER(18) | NULL | Configuração | Fonte padrão para notas de crédito geradas a partir desta fonte | self | 🟢 100% |
| 13 | INVALID_LINES_FLAG | VARCHAR2(1) | NULL | Configuração | Ação para linhas inválidas no AutoInvoice (REJECT/CREATE) | — | 🟢 100% |
| 14 | INVALID_TAX_RATE_FLAG | VARCHAR2(1) | NULL | Configuração | Ação para taxas de imposto inválidas no AutoInvoice | — | 🟢 100% |
| 15 | DERIVE_DATE_FLAG | VARCHAR2(1) | NULL | Configuração | Derivar data da transação automaticamente (Y/N) | — | 🟢 100% |
| 16 | RECEIPT_HANDLING_OPTION | VARCHAR2(30) | NULL | Configuração | Opção de tratamento de recebimentos | — | 🟢 100% |
| 17 | REV_ACC_ALLOCATION_RULE | VARCHAR2(30) | NULL | Contabilidade | Regra de alocação de receita (AMOUNT/PERCENT) | — | 🟢 100% |
| 18 | GLOBAL_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Global Descriptive Flexfield | — | 🟢 100% |
| 19 | GLOBAL_ATTRIBUTE1–20 | VARCHAR2(150) | NULL | DFF | Atributos globais (localizações por país) | — | 🟢 100% |
| 20 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 21 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 22 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 23 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 24 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 25 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 26 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 27 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ra_cust_trx_types_all]] — via `DEFAULT_INV_TRX_TYPE` (tipo de transação padrão)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da fonte de transações)
- self — via `CREDIT_MEMO_BATCH_SOURCE_ID` (fonte de credit memo associada)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — via `BATCH_SOURCE_ID` (transações que utilizam esta fonte)
- [[ra_batches_all]] — via `BATCH_SOURCE_ID` (lotes de transações)
- [[ra_interface_lines_all]] — via `BATCH_SOURCE_ID` (linhas de interface AutoInvoice)

---

## 📎 Uso Típico

### Consultar fontes ativas com numeração automática
```sql
SELECT bs.NAME, bs.BATCH_SOURCE_TYPE, bs.AUTO_TRX_NUMBERING_FLAG,
       bs.AUTO_BATCH_NUMBERING_FLAG, bs.ALLOW_DUPLICATE_TRX_NUM_FLAG
FROM   RA_BATCH_SOURCES_ALL bs
WHERE  bs.STATUS = 'A'
  AND  bs.ORG_ID = :p_org_id
ORDER BY bs.NAME;
```

### Identificar fontes do tipo AutoInvoice (importação)
```sql
SELECT bs.BATCH_SOURCE_ID, bs.NAME, bs.DESCRIPTION,
       tt.NAME AS default_trx_type
FROM   RA_BATCH_SOURCES_ALL bs
LEFT JOIN RA_CUST_TRX_TYPES_ALL tt ON tt.CUST_TRX_TYPE_ID = bs.DEFAULT_INV_TRX_TYPE
WHERE  bs.BATCH_SOURCE_TYPE = 'IMPORTED'
  AND  bs.STATUS = 'A'
  AND  bs.ORG_ID = :p_org_id;
```

### Filtros comuns
- `STATUS = 'A'` — Apenas fontes ativas
- `BATCH_SOURCE_TYPE = 'INV'` — Fontes manuais
- `BATCH_SOURCE_TYPE = 'IMPORTED'` — Fontes para AutoInvoice
- `AUTO_TRX_NUMBERING_FLAG = 'Y'` — Com numeração automática

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- O campo `CREDIT_MEMO_BATCH_SOURCE_ID` cria um **auto-relacionamento** (self-reference) que vincula uma fonte de fatura à sua fonte de credit memo padrão.
- Fontes do tipo `IMPORTED` são utilizadas pelo **AutoInvoice** — o processo que converte linhas da `RA_INTERFACE_LINES_ALL` em transações completas.
- Alterações nesta tabela afetam diretamente o comportamento de numeração de **todas as transações futuras** naquela fonte.
- Em implementações multi-org, cada business unit normalmente possui seu próprio conjunto de batch sources.

---

## 📚 Referências

- [Oracle Docs — RA_BATCH_SOURCES_ALL](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/rabatchsourcesall-10044.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
