---
id: DOC-AR-048
doc_type: system-doc
title: "AR_RECEIPT_METHOD_ACCOUNTS_ALL — Contas Contábeis por Método de Recebimento"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, receipt-accounts, contabilizacao, contas-gl]
aliases: [AR_RECEIPT_METHOD_ACCOUNTS_ALL, ar_receipt_method_accounts_all, receipt_method_accounts, contas_metodo_recebimento, ar_rma]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIPT_METHOD_ACCOUNTS_ALL

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela que define as **contas contábeis** associadas a cada método de recebimento por Business Unit. Mapeia cada etapa do ciclo de vida de um receipt (caixa, não identificado, não aplicado, on account, descontos, factoring, remessa, compensação, confirmação) para uma combinação contábil específica.

## 🧠 Propósito de Negócio

Esta tabela é o **mapa contábil do recebimento**. Para cada combinação de método de recebimento + conta bancária + BU, define todas as contas GL necessárias em cada etapa do processamento. Sem esta configuração, o AR não consegue contabilizar nenhum receipt.

Casos de uso principais:
- Definição da conta de caixa para cada método/banco
- Conta para recebimentos não identificados e não aplicados
- Contas de desconto earned/unearned por método
- Conta de remessa e compensação bancária

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | REC_METHOD_ACCOUNT_ID | NUMBER | PK. Identificador único do registro de contas. | Chave | 🟢 100% |
| 2 | RECEIPT_METHOD_ID | NUMBER | FK para [[ar_receipt_methods]]. Método de recebimento. | Chave Estrangeira | 🟢 100% |
| 3 | BANK_ACCOUNT_ID | NUMBER | FK para conta bancária. Referencia [[ce_bank_accounts]]. | Chave Estrangeira | 🟢 100% |
| 4 | CASH_CCID | NUMBER | Conta GL de caixa (débito ao receber). Referencia [[gl_code_combinations]]. | Contábil | 🟢 100% |
| 5 | UNIDENTIFIED_CCID | NUMBER | Conta GL para recebimentos não identificados. | Contábil | 🟢 100% |
| 6 | UNAPPLIED_CCID | NUMBER | Conta GL para recebimentos não aplicados a faturas. | Contábil | 🟢 100% |
| 7 | ON_ACCOUNT_CCID | NUMBER | Conta GL para recebimentos em conta (on account). | Contábil | 🟢 100% |
| 8 | EARNED_CCID | NUMBER | Conta GL para descontos merecidos (dentro do prazo). | Contábil | 🟢 100% |
| 9 | UNEARNED_CCID | NUMBER | Conta GL para descontos não merecidos (fora do prazo). | Contábil | 🟢 100% |
| 10 | FACTOR_CCID | NUMBER | Conta GL para factoring (desconto de duplicatas). | Contábil | 🟢 100% |
| 11 | REMITTANCE_CCID | NUMBER | Conta GL de remessa bancária (estado intermediário). | Contábil | 🟢 100% |
| 12 | RECEIPT_CLEARING_CCID | NUMBER | Conta GL de compensação (clearing) do recebimento. | Contábil | 🟢 100% |
| 13 | CONFIRMATION_CCID | NUMBER | Conta GL de confirmação (para receipts que exigem confirmação). | Contábil | 🟢 100% |
| 14 | SHORT_TERM_DEBT_CCID | NUMBER | Conta GL para dívida de curto prazo (bills receivable). | Contábil | 🟢 100% |
| 15 | BANK_CHARGES_CCID | NUMBER | Conta GL para taxas bancárias. | Contábil | 🟢 100% |
| 16 | CLAIM_INVESTIGATION_CCID | NUMBER | Conta GL para investigação de deduções (claims). | Contábil | 🟢 100% |
| 17 | ORG_ID | NUMBER | Identificador da Business Unit. | Partição | 🟢 100% |
| 18 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 19 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 20 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 21 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 22 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 23 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 24 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |
| 25 | OBJECT_VERSION_NUMBER | NUMBER | Controle de concorrência otimista (versionamento). | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[ar_receipt_methods]] | RECEIPT_METHOD_ID | FK | Método de recebimento pai |
| [[ce_bank_accounts]] | BANK_ACCOUNT_ID | FK | Conta bancária associada |
| [[gl_code_combinations]] | *_CCID | FK | Combinações contábeis (todas as colunas CCID) |
| [[ar_cash_receipts_all]] | RECEIPT_METHOD_ID + ORG_ID | Referência | Recebimentos contabilizados com estas contas |

## 📎 Uso Típico

```sql
-- Contas contábeis de um método de recebimento por BU
SELECT rma.rec_method_account_id,
       rm.name AS metodo,
       ba.bank_account_name,
       rma.cash_ccid,
       rma.unapplied_ccid,
       rma.earned_ccid,
       rma.unearned_ccid
  FROM ar_receipt_method_accounts_all rma
  JOIN ar_receipt_methods rm ON rm.receipt_method_id = rma.receipt_method_id
  JOIN ce_bank_accounts ba ON ba.bank_account_id = rma.bank_account_id
 WHERE rma.org_id = :p_org_id;
```

```sql
-- Verificar métodos sem conta de compensação configurada
SELECT rm.name AS metodo,
       rma.org_id
  FROM ar_receipt_method_accounts_all rma
  JOIN ar_receipt_methods rm ON rm.receipt_method_id = rma.receipt_method_id
 WHERE rma.receipt_clearing_ccid IS NULL;
```

## 🔒 Observações

- Cada combinação de `RECEIPT_METHOD_ID` + `BANK_ACCOUNT_ID` + `ORG_ID` deve ser **única**.
- Todas as colunas `*_CCID` referenciam [[gl_code_combinations]] — a validação é feita contra combinações contábeis ativas e habilitadas.
- Nem todas as contas são obrigatórias: depende da [[ar_receipt_classes|classe de recebimento]]. Ex: `CONFIRMATION_CCID` só é necessário se `CONFIRM_FLAG = 'Y'` na classe.
- `SHORT_TERM_DEBT_CCID` é utilizado apenas para bills receivable (duplicatas).
- Em migrações, esta tabela é crítica: sem as contas configuradas, nenhum recebimento pode ser contabilizado.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Receipt Method Accounts View Object
- Oracle Fusion Cloud — Setting Up Receipt Classes and Methods (Configuration Guide)
