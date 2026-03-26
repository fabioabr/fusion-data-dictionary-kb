---
id: DOC-AR-009
doc_type: system-doc
title: "RA_CUST_RECEIPT_METHODS — Métodos de Recebimento por Cliente"
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
  - receipt-methods
  - metodos-recebimento
  - configuracao-cliente
aliases:
  - RA_CUST_RECEIPT_METHODS
  - ra_cust_receipt_methods
  - metodos-recebimento-cliente
  - customer-receipt-methods
  - formas-pagamento-cliente
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# RA_CUST_RECEIPT_METHODS

## 📌 Visão Geral

Associa **métodos de recebimento a contas de clientes**, definindo quais formas de pagamento cada cliente pode utilizar para liquidar suas obrigações. Cada registro vincula uma conta de cliente (ou site específico) a um método de recebimento, com indicação de vigência e prioridade (primário ou secundário).

É uma tabela de **configuração de relacionamento** que conecta o cadastro de clientes ([[hz_cust_accounts]]) aos métodos de recebimento disponíveis ([[ar_receipt_methods]]), permitindo automação e validação no processo de cobrança.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de formas de pagamento:** Define quais métodos (boleto, débito automático, cartão, transferência) cada cliente pode usar.
- **Automação de recebimentos:** O processo de criação automática de recibos consulta esta tabela para determinar o método aplicável.
- **Validação de transações:** Garante que o método de recebimento informado em uma transação é válido para o cliente.
- **AutoLockbox:** Associa recebimentos bancários aos métodos corretos durante a conciliação automática.
- **Priorização de métodos:** O flag `PRIMARY_FLAG` indica o método preferencial do cliente.
- **Controle de vigência:** Campos de data permitem desativar métodos sem excluir o histórico.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CUST_RECEIPT_METHOD_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação cliente-método | — | 🟢 100% |
| 2 | CUSTOMER_ID | NUMBER(18) | NOT NULL | Referência | Conta do cliente | [[hz_cust_accounts]] | 🟢 100% |
| 3 | RECEIPT_METHOD_ID | NUMBER(18) | NOT NULL | Referência | Método de recebimento associado | [[ar_receipt_methods]] | 🟢 100% |
| 4 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | Indica se é o método primário do cliente (Y/N) | — | 🟢 100% |
| 5 | START_DATE | DATE | NULL | Vigência | Data de início da validade da associação | — | 🟢 100% |
| 6 | END_DATE | DATE | NULL | Vigência | Data de término da validade (NULL = sem fim) | — | 🟢 100% |
| 7 | SITE_USE_ID | NUMBER(18) | NULL | Referência | Site de uso do cliente (se método específico por site) | [[hz_cust_site_uses_all]] | 🟢 100% |
| 8 | BANK_ACCOUNT_ID | NUMBER(18) | NULL | Financeiro | Conta bancária do cliente associada ao método | [[iby_ext_bank_accounts]] | 🟢 100% |
| 9 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 100% |
| 10 | PAYMENT_TRXN_EXTENSION_ID | NUMBER(18) | NULL | Financeiro | Extensão de transação de pagamento (IBY) | [[iby_trxn_extensions_v]] | 🟢 100% |
| 11 | INSTR_ASSIGNMENT_ID | NUMBER(18) | NULL | Financeiro | Atribuição de instrumento de pagamento | [[iby_pmt_instr_uses_all]] | 🟢 100% |
| 12 | COMMENTS | VARCHAR2(240) | NULL | Texto livre | Observações sobre a associação | — | 🟢 100% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 18 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 19 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hz_cust_accounts]] — via `CUSTOMER_ID` (conta do cliente)
- [[ar_receipt_methods]] — via `RECEIPT_METHOD_ID` (método de recebimento)
- [[hz_cust_site_uses_all]] — via `SITE_USE_ID` (site de uso do cliente)
- [[iby_ext_bank_accounts]] — via `BANK_ACCOUNT_ID` (conta bancária externa)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do método de recebimento do cliente)

### Tabelas-filha (FK de saída)
- [[ra_customer_trx_all]] — indiretamente, transações que referenciam o método via `RECEIPT_METHOD_ID` + cliente (transações que utilizam este método de recebimento)

---

## 📎 Uso Típico

### Consultar métodos de recebimento de um cliente
```sql
SELECT crm.CUST_RECEIPT_METHOD_ID, rm.NAME AS metodo_recebimento,
       crm.PRIMARY_FLAG, crm.START_DATE, crm.END_DATE
FROM   RA_CUST_RECEIPT_METHODS crm
JOIN   AR_RECEIPT_METHODS rm ON rm.RECEIPT_METHOD_ID = crm.RECEIPT_METHOD_ID
WHERE  crm.CUSTOMER_ID = :p_customer_id
  AND  (crm.END_DATE IS NULL OR crm.END_DATE >= SYSDATE)
ORDER BY crm.PRIMARY_FLAG DESC, rm.NAME;
```

### Listar clientes com método primário de débito automático
```sql
SELECT hca.ACCOUNT_NUMBER, hca.ACCOUNT_NAME,
       rm.NAME AS metodo_recebimento
FROM   RA_CUST_RECEIPT_METHODS crm
JOIN   HZ_CUST_ACCOUNTS hca ON hca.CUST_ACCOUNT_ID = crm.CUSTOMER_ID
JOIN   AR_RECEIPT_METHODS rm ON rm.RECEIPT_METHOD_ID = crm.RECEIPT_METHOD_ID
WHERE  crm.PRIMARY_FLAG = 'Y'
  AND  rm.PAYMENT_TYPE_CODE = 'AUTOMATIC'
  AND  (crm.END_DATE IS NULL OR crm.END_DATE >= SYSDATE);
```

### Filtros comuns
- `PRIMARY_FLAG = 'Y'` — Apenas método primário
- `END_DATE IS NULL OR END_DATE >= SYSDATE` — Métodos vigentes
- `SITE_USE_ID IS NULL` — Métodos no nível da conta (não por site)
- `SITE_USE_ID = :p_site_use_id` — Métodos específicos de um site

---

## 🔒 Observações

- A tabela possui **Descriptive Flexfields (DFF)** via colunas `ATTRIBUTE1–15` para customizações por implementação.
- Diferente de outras tabelas AR, esta **não possui necessariamente o sufixo _ALL** — o controle multi-org é feito via `ORG_ID` mas o nome da tabela pode variar entre releases.
- Um cliente pode ter **múltiplos métodos**, mas apenas um deve ser marcado como `PRIMARY_FLAG = 'Y'` por site/organização.
- Quando `SITE_USE_ID` é NULL, o método se aplica a **todos os sites** da conta do cliente.
- A integração com **Oracle Payments (IBY)** utiliza os campos `PAYMENT_TRXN_EXTENSION_ID` e `INSTR_ASSIGNMENT_ID` para métodos eletrônicos.
- Desativar um método (via `END_DATE`) não afeta transações já criadas — apenas impede novas associações.

---

## 📚 Referências

- [Oracle Docs — RA_CUST_RECEIPT_METHODS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/racustreceiptmethods-10081.html)
- [[ar-module-data-dictionary]] — Dossiê do módulo AR
