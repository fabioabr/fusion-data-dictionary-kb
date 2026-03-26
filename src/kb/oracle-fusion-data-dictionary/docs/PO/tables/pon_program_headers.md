---
id: DOC-PO-029
doc_type: system-doc
title: "PON_PROGRAM_HEADERS — Cabeçalhos de Programas de Sourcing"
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
  - programs
  - sourcing
  - strategic-sourcing
  - program-management
aliases:
  - PON_PROGRAM_HEADERS
  - pon_program_headers
  - cabecalhos-programas-sourcing
  - program-headers
  - pon-programs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PON_PROGRAM_HEADERS

## 📌 Visão Geral

Armazena os **cabeçalhos de programas de sourcing** do módulo Oracle Sourcing. Um programa de sourcing é um contêiner estratégico que agrupa múltiplos **objetivos** ([[pon_program_objectives]]) e **negociações** para alcançar metas de procurement — tipicamente economia de custos, consolidação de fornecedores ou padronização de categorias de compra.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão estratégica de sourcing:** Organiza iniciativas de procurement de longo prazo em programas estruturados com metas mensuráveis.
- **Planejamento de economia:** Define metas de savings por programa, permitindo acompanhamento de resultados.
- **Portfólio de procurement:** Visão consolidada de todos os programas ativos, seus status e progresso.
- **Governança:** Controle de ownership, prazos e aprovação de programas de sourcing.
- **Relatórios OTBI:** Alimenta views analíticas ([[pon_neg_agg_to_prog_otbi_v]], [[pon_obj_agg_to_prog_otbi_v]]) para dashboards executivos.
- **Compliance:** Documenta a justificativa estratégica por trás de grupos de negociações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROGRAM_ID | NUMBER(18) | NOT NULL | PK | Identificador único do programa de sourcing | — | 🟢 90% |
| 2 | PROGRAM_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número visível do programa | — | 🟢 85% |
| 3 | PROGRAM_NAME | VARCHAR2(240) | NOT NULL | Descritivo | Nome do programa de sourcing | — | 🟢 85% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Descritivo | Descrição detalhada do programa | — | 🟢 85% |
| 5 | PROGRAM_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status: DRAFT, ACTIVE, ON_HOLD, COMPLETED, CANCELLED | — | 🟢 85% |
| 6 | PROGRAM_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de programa (ex: STRATEGIC, TACTICAL) | — | 🟡 65% |
| 7 | OWNER_ID | NUMBER(18) | NOT NULL | FK | Responsável pelo programa (user ID) | — | 🟢 85% |
| 8 | BU_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | — | 🟢 85% |
| 9 | START_DATE | DATE | NULL | Data | Data de início planejada do programa | — | 🟢 85% |
| 10 | END_DATE | DATE | NULL | Data | Data de término planejada do programa | — | 🟢 85% |
| 11 | TARGET_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Meta de economia do programa | — | 🟡 70% |
| 12 | TARGET_SAVINGS_PERCENTAGE | NUMBER | NULL | Financeiro | Meta de economia percentual | — | 🟡 65% |
| 13 | ACTUAL_SAVINGS_AMOUNT | NUMBER | NULL | Financeiro | Economia realizada | — | 🟡 65% |
| 14 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Código da moeda | — | 🟢 85% |
| 15 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria de procurement (se aplicável) | — | 🟡 65% |
| 16 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Workflow | Status de aprovação (PENDING, APPROVED, REJECTED) | — | 🟡 70% |
| 17 | APPROVED_BY | NUMBER(18) | NULL | Workflow | Usuário que aprovou o programa | — | 🟡 65% |
| 18 | APPROVED_DATE | DATE | NULL | Workflow | Data da aprovação | — | 🟡 65% |
| 19 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 20 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 21 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 22 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 23 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 24 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 90% |
| 25 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Tabela de usuários (FND_USER) — via `OWNER_ID` (responsável pelo programa)
- Tabela de business units — via `BU_ID`

### Tabelas-filha (FK de saída)
- [[pon_program_objectives]] — via `PROGRAM_ID` (objetivos do programa)
- [[pon_objective_negotiations]] — via `PROGRAM_ID` (negociações vinculadas)
- [[pon_neg_agg_to_prog_otbi_v]] — via `PROGRAM_ID` (view OTBI de negociações por programa)
- [[pon_obj_agg_to_prog_otbi_v]] — via `PROGRAM_ID` (view OTBI de objetivos por programa)

---

## 📎 Uso Típico

### Programas ativos por business unit
```sql
SELECT ph.PROGRAM_ID, ph.PROGRAM_NUMBER, ph.PROGRAM_NAME,
       ph.PROGRAM_STATUS, ph.START_DATE, ph.END_DATE,
       ph.TARGET_SAVINGS_AMOUNT, ph.ACTUAL_SAVINGS_AMOUNT
FROM   PON_PROGRAM_HEADERS ph
WHERE  ph.PROGRAM_STATUS = 'ACTIVE'
  AND  ph.BU_ID = :p_bu_id
ORDER BY ph.START_DATE;
```

### Programas com economia abaixo da meta
```sql
SELECT ph.PROGRAM_NAME, ph.TARGET_SAVINGS_AMOUNT,
       ph.ACTUAL_SAVINGS_AMOUNT,
       ROUND((ph.ACTUAL_SAVINGS_AMOUNT / NULLIF(ph.TARGET_SAVINGS_AMOUNT, 0)) * 100, 2)
         AS pct_atingida
FROM   PON_PROGRAM_HEADERS ph
WHERE  ph.PROGRAM_STATUS IN ('ACTIVE', 'COMPLETED')
  AND  ph.ACTUAL_SAVINGS_AMOUNT < ph.TARGET_SAVINGS_AMOUNT;
```

### Contagem de objetivos e negociações por programa
```sql
SELECT ph.PROGRAM_NAME,
       (SELECT COUNT(*) FROM PON_PROGRAM_OBJECTIVES po WHERE po.PROGRAM_ID = ph.PROGRAM_ID)
         AS qtd_objetivos,
       (SELECT COUNT(*) FROM PON_OBJECTIVE_NEGOTIATIONS on2 WHERE on2.PROGRAM_ID = ph.PROGRAM_ID)
         AS qtd_negociacoes
FROM   PON_PROGRAM_HEADERS ph
WHERE  ph.PROGRAM_STATUS = 'ACTIVE';
```

---

## 🔒 Observações

- O programa de sourcing é o **nível mais alto** da hierarquia: Programa > Objetivos > Negociações.
- O campo `PROGRAM_STATUS` controla o ciclo de vida: **DRAFT** (criação), **ACTIVE** (em execução), **ON_HOLD** (pausado), **COMPLETED** (concluído), **CANCELLED** (cancelado).
- Programas com `APPROVAL_STATUS = 'PENDING'` ainda aguardam aprovação gerencial antes de iniciar a execução.
- Os campos `TARGET_SAVINGS_AMOUNT` e `ACTUAL_SAVINGS_AMOUNT` permitem acompanhamento da economia planejada vs. realizada.
- Os atributos DFF (`ATTRIBUTE1–15`) podem ser customizados por implementação para armazenar campos adicionais específicos do cliente.

---

## 📚 Referências

- [Oracle Docs — Sourcing Tables](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pon-tables.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
