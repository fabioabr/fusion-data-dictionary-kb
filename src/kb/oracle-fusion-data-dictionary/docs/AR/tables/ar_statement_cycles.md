---
id: DOC-AR-036
doc_type: system-doc
title: "AR_STATEMENT_CYCLES — Ciclos de Emissão de Extratos"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, extratos, ciclos, statement]
aliases: [AR_STATEMENT_CYCLES, ar_statement_cycles, statement_cycles, ciclos_extrato, extrato_ar]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_STATEMENT_CYCLES

## 📌 Visão Geral

Tabela de definição dos ciclos de emissão de extratos (statements) do Accounts Receivable. Cada ciclo determina a frequência com que extratos são gerados e enviados aos clientes, podendo ser semanal, quinzenal, mensal ou personalizado.

## 🧠 Propósito de Negócio

Os ciclos de extrato controlam quando e com que frequência os clientes recebem resumos de suas posições de contas a receber. A configuração correta dos ciclos é importante para: (1) comunicação regular com clientes sobre saldos pendentes, (2) suporte ao processo de cobrança, (3) conciliação de contas pelo cliente. Cada perfil de cliente pode ser associado a um ciclo específico.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | STATEMENT_CYCLE_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do ciclo de extrato. | PK | 🟢 100% |
| 2 | NAME | VARCHAR2(15) | NOT NULL | Nome do ciclo (ex.: "Mensal", "Quinzenal"). | Negócio | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição textual do ciclo de extrato. | Negócio | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Status ativo/inativo (A = Ativo, I = Inativo). | Controle | 🟢 100% |
| 5 | INTERVAL | NUMBER | NOT NULL | Intervalo em dias entre emissões de extrato. | Negócio | 🟢 100% |
| 6 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 7 | ATTRIBUTE1 | VARCHAR2(150) | NULL | Atributo descritivo flexível 1. | DFF | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 9 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 11 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **HZ_CUSTOMER_PROFILES** — Perfis de clientes associados ao ciclo (via `STATEMENT_CYCLE_ID`).
- **[[ar_cons_inv_all]]** — Faturamento consolidado pode seguir o mesmo ciclo.

## 📎 Uso Típico

```sql
-- Ciclos de extrato ativos com intervalo
SELECT sc.STATEMENT_CYCLE_ID,
       sc.NAME,
       sc.DESCRIPTION,
       sc.INTERVAL AS dias_intervalo
  FROM AR_STATEMENT_CYCLES sc
 WHERE sc.STATUS = 'A'
 ORDER BY sc.INTERVAL;
```

## 🔒 Observações

- Ciclos de extrato são compartilhados entre business units (sem `ORG_ID`).
- A alteração do intervalo afeta a próxima emissão de todos os clientes associados ao ciclo.
- É recomendável criar ciclos separados para clientes de alto volume vs. baixo volume.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Statements and Dunning Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
