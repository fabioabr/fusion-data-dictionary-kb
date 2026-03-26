---
id: DOC-HCM-091
doc_type: system-doc
title: "CMP_STOCK_DETAILS — Detalhes de Ações (Stock)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - compensation
  - acoes
  - stock-options
  - equity
aliases:
  - CMP_STOCK_DETAILS
  - cmp_stock_details
  - cmp-stock-details
  - DOC-HCM-091
  - detalhes-de-ações-(stock)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_STOCK_DETAILS

## 📌 Visão Geral

Armazena os **detalhes de planos de ações** (stock options, RSUs, PSUs) concedidos a colaboradores como parte da remuneração. Inclui quantidades, preços, datas de vesting e status.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de stock options:** Registro de concessões de ações aos colaboradores.
- **Controle de vesting:** Monitoramento de períodos de carência.
- **Cálculo de Total Compensation:** Inclusão de ações na remuneração total.
- **Relatórios de equity:** Análise de distribuição de ações por nível/departamento.
- **Compliance regulatório:** Documentação para fins contábeis e fiscais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STOCK_DETAIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe de ação | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa beneficiária | [[per_all_people_f]] | 🟢 90% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuição do colaborador | [[per_all_assignments_m]] | 🟡 80% |
| 4 | GRANT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de concessão (OPTION, RSU, PSU) | — | 🟡 75% |
| 5 | GRANT_DATE | DATE | NULL | Data | Data da concessão | — | 🟡 80% |
| 6 | SHARES_GRANTED | NUMBER | NULL | Financeiro | Quantidade de ações concedidas | — | 🟡 80% |
| 7 | GRANT_PRICE | NUMBER | NULL | Financeiro | Preço de exercício/concessão | — | 🟡 75% |
| 8 | VESTING_DATE | DATE | NULL | Data | Data de vesting (carência) | — | 🟡 75% |
| 9 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda | — | 🟢 90% |
| 10 | STATUS | VARCHAR2(30) | NULL | Status | Status (GRANTED, VESTED, EXERCISED, EXPIRED) | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do plano de acoes)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo empregaticio do plano de acoes)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Ações concedidas por pessoa
```sql
SELECT sd.GRANT_TYPE, sd.GRANT_DATE, sd.SHARES_GRANTED,
       sd.GRANT_PRICE, sd.VESTING_DATE, sd.STATUS
FROM   CMP_STOCK_DETAILS sd
WHERE  sd.PERSON_ID = :p_person_id;
```

### Ações vested pendentes de exercício
```sql
SELECT sd.PERSON_ID, sd.SHARES_GRANTED, sd.GRANT_PRICE, sd.VESTING_DATE
FROM   CMP_STOCK_DETAILS sd
WHERE  sd.STATUS = 'VESTED'
  AND  sd.VESTING_DATE <= SYSDATE;
```

---

## 🔒 Observações

- O `GRANT_TYPE` classifica: OPTION (opções), RSU (Restricted Stock Unit), PSU (Performance Stock Unit).
- O `STATUS` evolui: GRANTED -> VESTED -> EXERCISED (ou EXPIRED).
- O valor total da concessão = `SHARES_GRANTED` × `GRANT_PRICE`.
- Informações de stock são relevantes para Total Compensation e relatórios de equity.

---

## 📚 Referências

- [Oracle Docs — CMP_STOCK_DETAILS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpstockdetails.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
