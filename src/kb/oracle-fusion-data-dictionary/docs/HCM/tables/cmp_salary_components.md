---
id: DOC-HCM-089
doc_type: system-doc
title: "CMP_SALARY_COMPONENTS — Componentes de Salário"
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
  - componentes
  - salary-components
  - remuneracao-total
aliases:
  - CMP_SALARY_COMPONENTS
  - cmp_salary_components
  - cmp-salary-components
  - DOC-HCM-089
  - componentes-de-salário
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_SALARY_COMPONENTS

## 📌 Visão Geral

Armazena os **componentes individuais** que compõem o salário de um colaborador — ex: salário-base, auxílio alimentação, comissão, periculosidade. Permite detalhar a composição da remuneração.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Decomposição salarial:** Detalhamento de cada componente do salário total.
- **Cálculo de remuneração total:** Soma de todos os componentes para remuneração total.
- **Relatórios de Total Compensation:** Base para Total Compensation Statement.
- **Integração com payroll:** Mapeamento de componentes para elementos de folha.
- **Análise de equidade:** Comparação de componentes entre colaboradores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SALARY_COMPONENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do componente | — | 🟢 90% |
| 2 | SALARY_ID | NUMBER(18) | NOT NULL | FK | Salário ao qual pertence | [[cmp_salary]] | 🟢 90% |
| 3 | COMPONENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do componente (BASE, ALLOWANCE, BONUS, COMMISSION) | — | 🟡 80% |
| 4 | COMPONENT_NAME | VARCHAR2(240) | NULL | Identificação | Nome do componente | — | 🟡 75% |
| 5 | AMOUNT | NUMBER | NULL | Financeiro | Valor do componente | — | 🟢 90% |
| 6 | CURRENCY_CODE | VARCHAR2(30) | NULL | Referência | Moeda do componente | — | 🟢 90% |
| 7 | FREQUENCY | VARCHAR2(30) | NULL | Classificação | Frequência (MONTHLY, ANNUAL, ONE_TIME) | — | 🟡 75% |
| 8 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade | — | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[cmp_salary]] — via `SALARY_ID` (salário pai)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Componentes por salário
```sql
SELECT sc.COMPONENT_TYPE, sc.COMPONENT_NAME, sc.AMOUNT,
       sc.CURRENCY_CODE, sc.FREQUENCY
FROM   CMP_SALARY_COMPONENTS sc
WHERE  sc.SALARY_ID = :p_salary_id;
```

### Total de componentes por tipo
```sql
SELECT sc.COMPONENT_TYPE, SUM(sc.AMOUNT) AS total
FROM   CMP_SALARY_COMPONENTS sc
  JOIN CMP_SALARY s ON sc.SALARY_ID = s.SALARY_ID
WHERE  s.PERSON_ID = :p_person_id
GROUP BY sc.COMPONENT_TYPE;
```

---

## 🔒 Observações

- A soma de todos os componentes pode diferir do `SALARY_AMOUNT` em `CMP_SALARY` dependendo da configuração.
- O `COMPONENT_TYPE` categoriza: BASE, ALLOWANCE, BONUS, COMMISSION, DEDUCTION, etc.
- A `FREQUENCY` indica a periodicidade do componente — componentes ONE_TIME não se repetem.
- Essencial para Total Compensation Statements e análises de custo total do colaborador.

---

## 🔗 PVOs Relacionados

### [[salarycomponentspvo|SalaryComponentsPVO]] (HCM · BICC: 9/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | ComponentsEOAttributeCategory | — |
| BUSINESS_GROUP_ID | ComponentsEOBusinessGroupId | — |
| CHANGE_AMOUNT | ComponentsEOChangeAmount | ✅ |
| CHANGE_PERCENTAGE | ComponentsEOChangePercentage | ✅ |
| COMPONENT_APPROVED | ComponentsEOComponentApproved | ✅ |
| COMPONENT_REASON_CODE | ComponentsEOComponentReasonCode | ✅ |
| CREATED_BY | ComponentsEOCreatedBy | ✅ |
| CREATION_DATE | ComponentsEOCreationDate | ✅ |
| LAST_UPDATE_DATE | ComponentsEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ComponentsEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ComponentsEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ComponentsEOObjectVersionNumber | — |
| SALARY_COMPONENT_ID | SalaryComponentId | ✅ |
| SALARY_ID | ComponentsEOSalaryId | — |

---

## 📚 Referências

- [Oracle Docs — CMP_SALARY_COMPONENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpsalarycomponents.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
