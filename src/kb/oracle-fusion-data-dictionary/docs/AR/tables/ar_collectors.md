---
id: DOC-AR-034
doc_type: system-doc
title: "AR_COLLECTORS — Cobradores de Contas a Receber"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags: [oracle-fusion, accounts-receivable, data-dictionary, cobradores, cobranca, collectors]
aliases: [AR_COLLECTORS, ar_collectors, collectors_ar, cobradores_ar, collector]
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# AR_COLLECTORS

## 📌 Visão Geral

Tabela de cadastro de cobradores (collectors) responsáveis pela gestão de contas a receber. Cada cobrador pode ser associado a perfis de clientes, determinando quem é responsável por acompanhar e cobrar saldos em aberto.

## 🧠 Propósito de Negócio

Os cobradores são peças centrais no processo de cobrança do Accounts Receivable. Cada perfil de cliente pode ser atribuído a um cobrador específico, que será responsável por monitorar os recebíveis, executar ações de cobrança e negociar com clientes inadimplentes. A tabela permite mapear cobradores a funcionários ou recursos do sistema.

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Descrição | Categoria | Confiança |
|---|--------|------|-------|-----------|-----------|-----------|
| 1 | COLLECTOR_ID | NUMBER(15) | NOT NULL | Chave primária. Identificador único do cobrador. | PK | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Nome do cobrador. | Negócio | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição do cobrador. | Negócio | 🟢 100% |
| 4 | STATUS | VARCHAR2(1) | NOT NULL | Status ativo/inativo (A = Ativo, I = Inativo). | Controle | 🟢 100% |
| 5 | EMPLOYEE_ID | NUMBER(15) | NULL | FK para tabela de funcionários (HCM). | FK | 🟢 100% |
| 6 | RESOURCE_ID | NUMBER(15) | NULL | Identificador do recurso associado (JTF Resources). | FK | 🟢 100% |
| 7 | RESOURCE_TYPE | VARCHAR2(30) | NULL | Tipo do recurso (ex.: RS_EMPLOYEE, RS_GROUP). | Classificação | 🟢 100% |
| 8 | ALIAS | VARCHAR2(30) | NULL | Nome alternativo para o cobrador. | Negócio | 🟡 75% |
| 9 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Contexto de flexfield descritivo. | DFF | 🟢 100% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Usuário que criou o registro. | WHO | 🟢 100% |
| 11 | CREATION_DATE | DATE | NOT NULL | Data de criação do registro. | WHO | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Usuário da última atualização. | WHO | 🟢 100% |
| 13 | LAST_UPDATE_DATE | DATE | NOT NULL | Data da última atualização. | WHO | 🟢 100% |

## 🔗 Relacionamentos

- **HZ_CUSTOMER_PROFILES** — Perfis de clientes associados ao cobrador (via `COLLECTOR_ID`).
- **[[ar_dispute_history]]** — Disputas podem ser gerenciadas pelo cobrador atribuído ao cliente.

## 📎 Uso Típico

```sql
-- Listar cobradores ativos com contagem de clientes atribuídos
SELECT c.COLLECTOR_ID,
       c.NAME,
       COUNT(cp.CUST_ACCOUNT_PROFILE_ID) AS total_clientes
  FROM AR_COLLECTORS c
  LEFT JOIN HZ_CUSTOMER_PROFILES cp
    ON cp.COLLECTOR_ID = c.COLLECTOR_ID
 WHERE c.STATUS = 'A'
 GROUP BY c.COLLECTOR_ID, c.NAME
 ORDER BY total_clientes DESC;
```

## 🔒 Observações

- Cobradores são compartilhados entre business units (não possuem `ORG_ID`).
- A associação com `EMPLOYEE_ID` permite rastrear o funcionário responsável no HCM.
- `RESOURCE_ID` e `RESOURCE_TYPE` integram com o framework JTF Resources do Oracle.

## 📚 Referências

- Oracle Fusion Cloud Financials — Accounts Receivable Tables (OEDMF Release 13).
- Oracle Fusion Cloud — Collections Management Documentation.
- Oracle Fusion Cloud ERP Schema Reference (Release 25A).
