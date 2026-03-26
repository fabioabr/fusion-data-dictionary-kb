---
id: DOC-AP-037
doc_type: system-doc
title: "EXM_EXPENSE_TYPES — Tipos de Despesa"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - tipos-despesa
  - expense-types
  - configuracao
aliases:
  - EXM_EXPENSE_TYPES
  - exm_expense_types
  - tipos-despesa-exm
  - exm-expense-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSE_TYPES

## 📌 Visão Geral

Armazena os **tipos de despesa** (Expense Types) configurados no módulo Expense Management. Cada tipo representa uma categoria de gasto — como passagem aérea, hospedagem, alimentação, combustível, táxi/transporte, etc. — com regras associadas de limite, obrigatoriedade de comprovante, conta contábil padrão e políticas de reembolso.

> [!note] Configuração
> Esta é uma tabela de configuração (setup). Os tipos de despesa são definidos pelo administrador e apresentados ao funcionário como opções de categorização ao registrar cada item de gasto.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Categorização de despesas:** Classificação de cada item de gasto em categorias padronizadas.
- **Controle de políticas:** Definição de limites máximos, obrigatoriedade de comprovante e regras por tipo.
- **Derivação contábil:** Determinação da conta contábil de débito com base no tipo de despesa.
- **Relatórios gerenciais:** Análise de gastos corporativos por categoria (viagem, alimentação, etc.).
- **Per diem:** Configuração de tipos com cálculo automático de diárias.
- **Mileage/Quilometragem:** Tipos especiais com cálculo por distância percorrida.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de despesa | — | 🟢 95% |
| 2 | EXPENSE_TYPE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do tipo de despesa (ex: "Passagem Aérea", "Hospedagem") | — | 🟢 95% |
| 3 | EXPENSE_TYPE_CODE | VARCHAR2(30) | NULL | Identificação | Código interno do tipo de despesa | — | 🟡 80% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de despesa | — | 🟢 90% |
| 5 | EXPENSE_CATEGORY_CODE | VARCHAR2(30) | NULL | Classificação | Categoria macro: AIRFARE, LODGING, MEALS, MILEAGE, MISCELLANEOUS, etc. | — | 🟢 85% |
| 6 | RECEIPT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se comprovante é obrigatório para este tipo (Y/N) | — | 🟢 85% |
| 7 | ITEMIZATION_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se itemização é obrigatória (Y/N) | — | 🟡 70% |
| 8 | LIMIT_AMOUNT | NUMBER | NULL | Financeiro | Valor-limite máximo permitido para este tipo de despesa | — | 🟡 75% |
| 9 | LIMIT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda do valor-limite | — | 🟡 70% |
| 10 | PER_DIEM_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é tipo de per diem/diária (Y/N) | — | 🟡 75% |
| 11 | MILEAGE_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é tipo de quilometragem/mileage (Y/N) | — | 🟡 75% |
| 12 | CODE_COMBINATION_ID | NUMBER(18) | NULL | Contabilidade | Conta contábil padrão para este tipo de despesa | [[gl_code_combinations]] | 🟡 80% |
| 13 | TAX_CLASSIFICATION_CODE | VARCHAR2(30) | NULL | Tributário | Código de classificação fiscal | — | 🟡 70% |
| 14 | START_DATE | DATE | NULL | Data | Data de início de vigência | — | 🟢 85% |
| 15 | END_DATE | DATE | NULL | Data | Data de término de vigência (NULL = sem expiração) | — | 🟢 85% |
| 16 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o tipo está ativo (Y/N) | — | 🟢 85% |
| 17 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 22 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (conta contábil padrão)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do tipo de despesa)

### Tabelas-filha (FK de saída)
- [[exm_expenses]] — via `EXPENSE_TYPE_ID` (linhas de despesa classificadas com este tipo)

---

## 📎 Uso Típico

### Listar tipos de despesa ativos por business unit
```sql
SELECT et.EXPENSE_TYPE_ID, et.EXPENSE_TYPE_NAME,
       et.EXPENSE_CATEGORY_CODE, et.LIMIT_AMOUNT,
       et.RECEIPT_REQUIRED_FLAG
FROM   EXM_EXPENSE_TYPES et
WHERE  et.ORG_ID = :p_org_id
  AND  NVL(et.ENABLED_FLAG, 'Y') = 'Y'
  AND  (et.END_DATE IS NULL OR et.END_DATE >= SYSDATE)
ORDER BY et.EXPENSE_CATEGORY_CODE, et.EXPENSE_TYPE_NAME;
```

### Tipos de despesa com limite definido
```sql
SELECT et.EXPENSE_TYPE_NAME, et.LIMIT_AMOUNT,
       et.LIMIT_CURRENCY_CODE
FROM   EXM_EXPENSE_TYPES et
WHERE  et.LIMIT_AMOUNT IS NOT NULL
  AND  NVL(et.ENABLED_FLAG, 'Y') = 'Y';
```

### Total gasto por tipo de despesa
```sql
SELECT et.EXPENSE_TYPE_NAME,
       SUM(e.REIMBURSABLE_AMOUNT) AS total_gasto,
       COUNT(*) AS qtd_itens
FROM   EXM_EXPENSES e
JOIN   EXM_EXPENSE_TYPES et ON et.EXPENSE_TYPE_ID = e.EXPENSE_TYPE_ID
WHERE  e.START_DATE BETWEEN :start_date AND :end_date
GROUP BY et.EXPENSE_TYPE_NAME
ORDER BY total_gasto DESC;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Tipos ativos
- `EXPENSE_CATEGORY_CODE = 'AIRFARE'` — Passagens aéreas
- `PER_DIEM_FLAG = 'Y'` — Tipos de diária
- `MILEAGE_FLAG = 'Y'` — Tipos de quilometragem

---

## 🔒 Observações

- Tipos de despesa são fundamentais para a **derivação contábil automática**: o `CODE_COMBINATION_ID` define a conta de débito padrão, podendo ser sobrescrita na distribuição.
- Tipos com `PER_DIEM_FLAG = 'Y'` utilizam tabelas de taxas de diária para cálculo automático com base em localização e datas.
- Tipos com `MILEAGE_FLAG = 'Y'` calculam reembolso com base em distância percorrida × taxa por km/milha.
- O `LIMIT_AMOUNT` é verificado na validação do relatório; despesas acima do limite geram aviso ou bloqueio conforme política.
- Tipos podem ser associados a templates específicos ([[exm_expense_templates]]) para controlar quais categorias cada grupo de funcionários pode utilizar.
- O campo `EXPENSE_CATEGORY_CODE` permite agrupamento macro para relatórios gerenciais (viagem, alimentação, transporte, outros).

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSE_TYPES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpensetypes.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
