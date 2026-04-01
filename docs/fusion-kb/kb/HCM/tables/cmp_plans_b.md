---
id: DOC-HCM-081
doc_type: system-doc
title: "CMP_PLANS_B — Planos de Compensação (Base)"
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
  - planos
  - base-table
  - salary-plan
aliases:
  - CMP_PLANS_B
  - cmp_plans_b
  - cmp-plans-b
  - DOC-HCM-081
  - planos-de-compensação-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_PLANS_B

## 📌 Visão Geral

Armazena as **definições base dos planos de compensação** (tabela _B — base language). Contém os atributos não-traduzíveis dos planos como códigos, tipos, status e configurações estruturais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de planos:** Cadastro central de todos os planos de compensação.
- **Configuração de elegibilidade:** Parâmetros de regras de elegibilidade.
- **Tipificação:** Classificação dos planos por tipo (salário, bônus, etc.).
- **Controle de ciclo:** Status e período de vigência dos planos.
- **Base para tradução:** Tabela base complementada por `CMP_PLANS_TL` para multilíngue.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano | — | 🟢 95% |
| 2 | PLAN_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do plano | — | 🟢 90% |
| 3 | PLAN_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do plano de compensação | — | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status do plano (ACTIVE, INACTIVE, CLOSED) | — | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Data | Data de início de vigência | — | 🟢 90% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim de vigência | — | 🟢 90% |
| 7 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 75% |
| 8 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda padrão do plano | — | 🟢 90% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Número de versão do objeto | — | 🟢 95% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo de negócios)

### Tabelas-filha (FK de saída)
- [[cmp_plans_tl]] — via `PLAN_ID` (traducoes multilingue do registro)
- [[cmp_plan_periods]] — via `PLAN_ID` (periodos do plano de compensacao)
- [[cmp_salary]] — via `PLAN_ID` (salarios vinculados ao plano)

---

## 📎 Uso Típico

### Planos ativos
```sql
SELECT pb.PLAN_ID, pb.PLAN_CODE, pb.PLAN_TYPE, pb.STATUS_CODE
FROM   CMP_PLANS_B pb
WHERE  pb.STATUS_CODE = 'ACTIVE';
```

### Planos por tipo
```sql
SELECT pb.PLAN_TYPE, COUNT(*) AS qtd_planos
FROM   CMP_PLANS_B pb
GROUP BY pb.PLAN_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém apenas dados independentes de idioma.
- Para nomes e descrições traduzidos, juntar com `CMP_PLANS_TL` via `PLAN_ID`.
- O `OBJECT_VERSION_NUMBER` é usado para controle de concorrência otimista.
- Planos com `STATUS_CODE = 'INACTIVE'` não aparecem para seleção em telas.

---

## 📚 Referências

- [Oracle Docs — CMP_PLANS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpplansb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
