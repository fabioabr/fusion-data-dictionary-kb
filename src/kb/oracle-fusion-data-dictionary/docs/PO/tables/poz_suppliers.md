---
id: DOC-PO-088
doc_type: system-doc
title: "POZ_SUPPLIERS — Cadastro Principal de Fornecedores"
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
  - suppliers
  - fornecedores
  - cadastro-mestre
aliases:
  - POZ_SUPPLIERS
  - poz_suppliers
  - cadastro-fornecedores
  - supplier-master
  - fornecedores-fusion
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIERS

## Visão Geral

Tabela **mestre de fornecedores** do Oracle Fusion Procurement. Armazena o cadastro principal de todos os fornecedores da organização, incluindo dados de identificação, classificação, status e vínculo com o Trading Community Architecture (TCA). É a tabela central do módulo de Supplier Management, referenciada por praticamente todas as transações de compras e contas a pagar.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro mestre:** Registro centralizado de todos os fornecedores (nacionais e internacionais).
- **Pedidos de compra:** Referência obrigatória em todos os POs — identifica o fornecedor da transação.
- **Contas a pagar:** Vínculo com faturas (AP Invoices) para processamento de pagamentos.
- **Qualificação:** Base para processos de qualificação, homologação e avaliação de fornecedores.
- **Sourcing:** Identificação de fornecedores elegíveis para negociações e cotações.
- **Relatórios e analytics:** Dimensão principal em análises de gastos (Spend Analysis).
- **Integração TCA:** Ponte entre o cadastro de procurement e o Trading Community Architecture (HZ_PARTIES).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do fornecedor | — | 🟢 95% |
| 2 | VENDOR_NAME | VARCHAR2(360) | NOT NULL | Identificação | Razão social / nome do fornecedor | — | 🟢 95% |
| 3 | SEGMENT1 | VARCHAR2(30) | NOT NULL | Identificação | Número do fornecedor (código visível ao usuário) | — | 🟢 95% |
| 4 | VENDOR_TYPE_LOOKUP_CODE | VARCHAR2(30) | NULL | Classificação | Tipo do fornecedor: VENDOR, EMPLOYEE, TAX_AUTHORITY, etc. | — | 🟢 90% |
| 5 | PARTY_ID | NUMBER(18) | NOT NULL | FK | Identificador do party no TCA | [[hz_parties]] | 🟢 90% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Fornecedor ativo (Y/N) | — | 🟢 90% |
| 7 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início de atividade do fornecedor | — | 🟢 85% |
| 8 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de encerramento de atividade | — | 🟢 85% |
| 9 | BUSINESS_RELATIONSHIP | VARCHAR2(30) | NULL | Classificação | Tipo de relacionamento: SPEND_AUTHORIZED, NOT_AUTHORIZED | — | 🟡 75% |
| 10 | TAX_ORGANIZATION_TYPE_CODE | VARCHAR2(30) | NULL | Fiscal | Tipo de organização fiscal | — | 🟡 70% |
| 11 | FEDERAL_REPORTABLE_FLAG | VARCHAR2(1) | NULL | Fiscal | Sujeito a reporte federal (Y/N) — contexto US | — | 🟡 70% |
| 12 | STANDARD_INDUSTRY_CLASS | VARCHAR2(25) | NULL | Classificação | Código SIC (Standard Industry Classification) | — | 🟡 70% |
| 13 | ONE_TIME_FLAG | VARCHAR2(1) | NULL | Classificação | Fornecedor de uso único (Y/N) | — | 🟡 75% |
| 14 | PARENT_VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor-pai (hierarquia de fornecedores) | [[poz_suppliers]] | 🟡 70% |
| 15 | CUSTOMER_NUM | VARCHAR2(25) | NULL | Referência cruzada | Número de cliente do fornecedor (reciprocidade) | — | 🟡 65% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 20 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |
| 21 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA — nome, endereço, CNPJ/CPF)
- [[poz_suppliers]] — via `PARENT_VENDOR_ID` (auto-referência para hierarquia)

### Tabelas-filha (FK de saída)

### Views

---

## Uso Típico

### Buscar fornecedor por número ou nome
```sql
SELECT s.VENDOR_ID, s.SEGMENT1 AS vendor_number,
       s.VENDOR_NAME, s.VENDOR_TYPE_LOOKUP_CODE,
       s.ENABLED_FLAG
FROM   POZ_SUPPLIERS s
WHERE  s.SEGMENT1 = :p_vendor_number
   OR  UPPER(s.VENDOR_NAME) LIKE UPPER(:p_search || '%');
```

### Fornecedores ativos com spend autorizado
```sql
SELECT s.VENDOR_ID, s.SEGMENT1, s.VENDOR_NAME,
       s.BUSINESS_RELATIONSHIP
FROM   POZ_SUPPLIERS s
WHERE  s.ENABLED_FLAG = 'Y'
  AND  s.BUSINESS_RELATIONSHIP = 'SPEND_AUTHORIZED'
  AND  (s.END_DATE_ACTIVE IS NULL OR s.END_DATE_ACTIVE > SYSDATE);
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Fornecedores ativos
- `VENDOR_TYPE_LOOKUP_CODE = 'VENDOR'` — Apenas fornecedores (excluindo funcionários, autoridades fiscais)
- `ONE_TIME_FLAG = 'N'` — Excluir fornecedores de uso único

---

## Observações

- Esta é a **tabela mais referenciada** do módulo Procurement — alterações no `VENDOR_ID` impactam praticamente todo o ecossistema de compras e pagamentos.
- O `PARTY_ID` vincula o fornecedor ao **TCA (Trading Community Architecture)**, onde ficam dados como CNPJ/CPF, endereço fiscal e informações de partido.
- O campo `BUSINESS_RELATIONSHIP` controla se o fornecedor está autorizado para gastos (`SPEND_AUTHORIZED`) ou apenas registrado.
- Dados sensíveis como CPF/CNPJ do representante legal ficam na tabela separada `POZ_SUPPLIERS_PII`.
- O `SEGMENT1` é o **número do fornecedor** visível ao usuário; pode ser sequencial ou seguir regra de numeração customizada.
- Fornecedores com `ONE_TIME_FLAG = 'Y'` são tipicamente usados para pagamentos pontuais e não participam de processos de sourcing.

---

## Referências

- [Oracle Docs — POZ_SUPPLIERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pozsuppliers-25316.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
