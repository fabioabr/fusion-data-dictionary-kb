---
id: DOC-AR-045
doc_type: system-doc
title: "AR_RECEIVABLES_TRX_ALL — Atividades de Recebíveis"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, atividades, ajustes, finance-charges]
aliases: [AR_RECEIVABLES_TRX_ALL, ar_receivables_trx_all, receivables_activities, atividades_recebiveis, ar_rec_trx]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_RECEIVABLES_TRX_ALL

> [!note] Sufixo _ALL
> Tabelas com sufixo `_ALL` armazenam dados de **todas as Business Units (orgs)**. O acesso é filtrado pela política de segurança (`ORG_ID`). Em views sem o sufixo, o filtro de org já está aplicado.

## 📌 Visão Geral

Tabela de cadastro de **atividades de recebíveis** (receivables activities). Define os tipos de operação utilizados em ajustes, recebimentos diversos (miscellaneous receipts), finance charges e estornos de cartão de crédito. Cada atividade aponta para uma conta contábil específica.

## 🧠 Propósito de Negócio

As atividades de recebíveis são **templates contábeis** que padronizam o tratamento de operações não transacionais no AR. Quando um analista realiza um ajuste ou registra um recebimento diverso, ele seleciona uma atividade que determina automaticamente a conta contábil de destino.

Casos de uso principais:
- Ajustes de saldo (write-off, reclassificação)
- Recebimentos diversos (juros recebidos, multas)
- Encargos financeiros (finance charges)
- Estornos de cartão de crédito (CC refund)

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Descrição | Categoria | Confiança |
|---|--------|------|-----------|-----------|-----------|
| 1 | RECEIVABLES_TRX_ID | NUMBER | PK. Identificador único da atividade de recebíveis. | Chave | 🟢 100% |
| 2 | NAME | VARCHAR2 | Nome da atividade (exibido em LOVs). | Identificação | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2 | Descrição textual da finalidade da atividade. | Identificação | 🟢 100% |
| 4 | TYPE | VARCHAR2 | Tipo da atividade: `ADJUST`, `FINCHRG`, `MISC`, `CCREFUND`. | Classificação | 🟢 100% |
| 5 | STATUS | VARCHAR2 | Status da atividade: `A` (ativo) ou `I` (inativo). | Controle | 🟢 100% |
| 6 | CODE_COMBINATION_ID | NUMBER | FK para a combinação contábil (conta GL). Referencia [[gl_code_combinations]]. | Contábil | 🟢 100% |
| 7 | GL_ACCOUNT_SOURCE | VARCHAR2 | Origem da conta GL: `ACTIVITY` (fixo na atividade), `TAX_CODE`, `REVENUE`. | Contábil | 🟢 100% |
| 8 | TAX_RATE_CODE_ID | NUMBER | FK para código de imposto associado. Referencia [[zx_rates_b]]. | Fiscal | 🟢 100% |
| 9 | ASSET_TAX_CODE | VARCHAR2 | Código fiscal para ativos (usado em cálculos tributários). | Fiscal | 🟢 100% |
| 10 | TAX_CODE_SOURCE | VARCHAR2 | Origem do código fiscal: `ACTIVITY`, `INVOICE`, `NONE`. | Fiscal | 🟢 100% |
| 11 | DEFAULT_AMOUNT | NUMBER | Valor padrão sugerido para a atividade. | Operacional | 🟢 100% |
| 12 | ROUNDING_ERROR_CCID | NUMBER | Conta contábil para diferenças de arredondamento. | Contábil | 🟢 100% |
| 13 | ORG_ID | NUMBER | Identificador da Business Unit. | Partição | 🟢 100% |
| 14 | ATTRIBUTE_CATEGORY | VARCHAR2 | Contexto para campos descritivos flexíveis (DFF). | Flexfield | 🟢 100% |
| 15 | ATTRIBUTE1–15 | VARCHAR2 | Campos descritivos flexíveis (DFF) genéricos. | Flexfield | 🟢 100% |
| 16 | CREATED_BY | VARCHAR2 | Usuário que criou o registro. | WHO | 🟢 100% |
| 17 | CREATION_DATE | DATE | Data de criação do registro. | WHO | 🟢 100% |
| 18 | LAST_UPDATED_BY | VARCHAR2 | Último usuário que alterou o registro. | WHO | 🟢 100% |
| 19 | LAST_UPDATE_DATE | DATE | Data da última atualização. | WHO | 🟢 100% |
| 20 | LAST_UPDATE_LOGIN | VARCHAR2 | Login da última sessão de atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

| Tabela Relacionada | Chave | Tipo | Descrição |
|--------------------|-------|------|-----------|
| [[gl_code_combinations]] | CODE_COMBINATION_ID | FK | Conta contábil da atividade |
| [[zx_rates_b]] | TAX_RATE_CODE_ID | FK | Código de imposto associado |
| [[ar_adjustments_all]] | RECEIVABLES_TRX_ID | Referenciada por | Ajustes que usam esta atividade |
| [[ar_cash_receipts_all]] | RECEIVABLES_TRX_ID | Referenciada por | Recebimentos misc usando esta atividade |
| [[ar_system_parameters_all]] | ORG_ID | Referência | Parâmetros da BU |

## 📎 Uso Típico

```sql
-- Listar atividades de ajuste ativas
SELECT receivables_trx_id,
       name,
       type,
       gl_account_source
  FROM ar_receivables_trx_all
 WHERE type = 'ADJUST'
   AND status = 'A'
   AND org_id = :p_org_id;
```

```sql
-- Atividades com conta contábil fixa
SELECT rt.name,
       rt.type,
       gcc.concatenated_segments AS conta_gl
  FROM ar_receivables_trx_all rt
  JOIN gl_code_combinations_kfv gcc ON gcc.code_combination_id = rt.code_combination_id
 WHERE rt.gl_account_source = 'ACTIVITY'
   AND rt.org_id = :p_org_id;
```

## 🔒 Observações

- O campo `TYPE` determina onde a atividade pode ser utilizada: `ADJUST` para ajustes, `FINCHRG` para encargos financeiros, `MISC` para recebimentos diversos, `CCREFUND` para estornos de cartão.
- Atividades com `GL_ACCOUNT_SOURCE = 'ACTIVITY'` têm conta fixa; `REVENUE` herda a conta da linha da fatura.
- Inativar uma atividade (`STATUS = 'I'`) impede novos usos mas não afeta transações já registradas.
- Atividades de finance charge são referenciadas nos parâmetros do sistema ([[ar_system_parameters_all]]).

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13)
- Oracle BICC — Receivables Activities View Object
- Oracle Fusion Cloud — Managing Receivables Activities (Functional Guide)
