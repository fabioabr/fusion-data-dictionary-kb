---
id: DOC-HCM-068
doc_type: system-doc
title: "CMP_COMPONENTS_B — Componentes de Compensação (Base)"
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
  - components
  - salario
  - bonus
aliases:
  - CMP_COMPONENTS_B
  - cmp_components_b
  - componentes-compensacao
  - compensation-components
  - cmp-components
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_COMPONENTS_B

## 📌 Visão Geral

Armazena os **componentes de compensação** (salary, bonus, stock, allowance, etc.) que formam o pacote de remuneração total. Cada componente define um tipo de remuneração configurável.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (dados técnicos) — a tabela de traduções correspondente (`_TL`) contém os textos traduzidos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Remuneração total:** Define os componentes do pacote de compensação.
- **Configuração:** Cada componente tem regras, frequência e moeda.
- **Statements:** Base para Total Compensation Statements.
- **Planejamento:** Usado no CWB para distribuição de componentes específicos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COMPONENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do componente | — | 🟢 90% |
| 2 | COMPONENT_CD | VARCHAR2(30) | NOT NULL | Código | Código do componente | — | 🟢 90% |
| 3 | COMPONENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (SALARY, BONUS, STOCK, ALLOWANCE) | — | 🟢 85% |
| 4 | FREQUENCY | VARCHAR2(30) | NULL | Configuração | Frequência (ANNUAL, MONTHLY, ONE_TIME) | — | 🟡 80% |
| 5 | CURRENCY_CODE | VARCHAR2(15) | NULL | Financeiro | Moeda padrão do componente | — | 🟢 85% |
| 6 | COMPONENT_STATUS | VARCHAR2(30) | NULL | Classificação | Status (ACTIVE, INACTIVE) | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta (tabela de configuração raiz).

### Tabelas-filha (FK de saída)
- [[cmp_components_tl]] — via `COMPONENT_ID` (traducoes multilingue do registro)
- [[cmp_cwb_person_info]] — via `COMPONENT_ID` (valores por pessoa)

---

## 📎 Uso Típico

### Componentes ativos por tipo
```sql
SELECT c.COMPONENT_ID, c.COMPONENT_CD, c.COMPONENT_TYPE,
       c.FREQUENCY, c.CURRENCY_CODE
FROM   CMP_COMPONENTS_B c
WHERE  c.COMPONENT_STATUS = 'ACTIVE'
ORDER BY c.COMPONENT_TYPE;
```

### Filtros comuns
- `COMPONENT_STATUS = 'ACTIVE'` — Componentes ativos
- `COMPONENT_TYPE = 'SALARY'` — Componentes salariais
- `COMPONENT_TYPE = 'BONUS'` — Componentes de bônus

---

## 🔒 Observações

- Tabela base (`_B`): traduções estão em `CMP_COMPONENTS_TL`.
- O tipo determina o comportamento do componente no cálculo de compensação total.
- Componentes `ONE_TIME` são para pagamentos únicos (ex.: bônus de contratação).

---

## 📚 Referências

- [Oracle Docs — CMP_COMPONENTS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcomponentsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
