---
id: DOC-AR-046
doc_type: system-doc
title: "AR_RECEIPT_CLASSES — Classes de Recebimento"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, receipt-class, recebimentos, contabilizacao]
aliases: [AR_RECEIPT_CLASSES, ar_receipt_classes, receipt_classes, classes_recebimento, ar_rcpt_class]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIPT_CLASSES

## 📌 Visão Geral

Tabela de cadastro de **classes de recebimento** (receipt classes). Define o **comportamento contábil** dos recebimentos — como são criados, confirmados, remetidos ao banco e compensados. Cada classe combina flags que determinam o ciclo de vida contábil do receipt.

## 🧠 Propósito de Negócio

As classes de recebimento são o **alicerce contábil** da gestão de caixa no AR. Determinam se um recebimento precisa de confirmação, se passa por remessa bancária e se requer compensação explícita. A configuração correta é essencial para garantir que os lançamentos contábeis reflitam com precisão o fluxo de caixa.

Casos de uso principais:
- Recebimentos automáticos via lockbox (sem confirmação, compensação direta)
- Boletos bancários (criação manual → remessa → compensação)
- Notas promissórias (criação → confirmação → remessa → compensação)
- Cartão de crédito (criação automática → compensação automática)

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | RECEIPT_CLASS_ID | NUMBER | PK. Identificador único da classe de recebimento. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome da classe de recebimento. | Identificação | 🟢 100% |
| 3 | CREATION_METHOD_CODE | VARCHAR2 | Método de criação: `MANUAL`, `AUTOMATIC`, `LOCKBOX`. | Configuração | 🟢 100% |
| 4 | REMIT_METHOD_CODE | VARCHAR2 | Método de remessa: `STANDARD`, `FACTORING`, `NO_REMIT`. | Configuração | 🟢 100% |
| 5 | CLEAR_FLAG | VARCHAR2 | Requer compensação bancária: `Y`/`N`. Se `Y`, o receipt passa pelo estado "remitted" antes de "cleared". | Configuração | 🟢 100% |
| 6 | CONFIRM_FLAG | VARCHAR2 | Requer confirmação: `Y`/`N`. Se `Y`, o receipt é criado em estado "unconfirmed". | Configuração | 🟢 100% |
| 7 | CREATION_STATUS | VARCHAR2 | Status inicial do receipt: `CONFIRMED`, `REMITTED`, `CLEARED`. | Configuração | 🟢 100% |
| 8 | REMIT_FLAG | VARCHAR2 | Indica se a classe suporta remessa bancária: `Y`/`N`. | Configuração | 🟢 100% |
| 9 | NOTES_RECEIVABLE | VARCHAR2 | Indica se trata notas promissórias (bills receivable): `Y`/`N`. | Classificação | 🟢 100% |
| 10 | BILL_OF_EXCHANGE_FLAG | VARCHAR2 | Indica se a classe suporta bills of exchange. | Classificação | 🟢 100% |
| 11 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 12 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 13 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 14 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 16 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |
| 18 | OBJECT_VERSION_NUMBER | NUMBER | Controle de concorrência otimista (versionamento). | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_receipt_methods]] | RECEIPT_CLASS_ID | Referenciada por | Métodos de recebimento vinculados à classe |
| [[ar_cash_receipts_all]] | RECEIPT_METHOD_ID → RECEIPT_CLASS_ID | Indireta | Recebimentos usam a classe via método |

## 📎 Uso Típico

```sql
-- Listar classes de recebimento e seus comportamentos
SELECT receipt_class_id,
       name,
       creation_method_code,
       remit_method_code,
       confirm_flag,
       clear_flag,
       notes_receivable
  FROM ar_receipt_classes
 ORDER BY name;
```

```sql
-- Classes que exigem confirmação e compensação (fluxo completo)
SELECT name,
       creation_method_code,
       remit_method_code
  FROM ar_receipt_classes
 WHERE confirm_flag = 'Y'
   AND clear_flag = 'Y';
```

## 🔒 Observações

- A combinação de `CONFIRM_FLAG`, `REMIT_FLAG` e `CLEAR_FLAG` define o **ciclo de vida** do receipt: quanto mais flags ativas, mais etapas contábeis intermediárias.
- Classes com `NOTES_RECEIVABLE = 'Y'` são usadas para **bills receivable** (duplicatas/notas promissórias), um instrumento financeiro comum no Brasil.
- O `CREATION_STATUS` determina em qual estado contábil o receipt é criado — essencial para automação via lockbox.
- Esta tabela **não é particionada por ORG_ID** — classes são compartilhadas entre Business Units.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Receipt Classes View Object
- Oracle Fusion Cloud — Setting Up Receipt Classes and Methods (Configuration Guide)
