---
id: DOC-GL-034
doc_type: system-doc
title: "GL_PERIOD_TYPES — Tipos de Período Contábil"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - periodos
  - period-types
  - calendario
aliases:
  - GL_PERIOD_TYPES
  - gl_period_types
  - tipos-periodo-gl
  - period-types
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_PERIOD_TYPES

## 📌 Visão Geral

Armazena os **tipos de período contábil** disponíveis no Oracle Fusion GL. Define as categorias de período (Month, Quarter, Year, etc.) que são usadas na construção de calendários contábeis. É uma tabela de referência (lookup) de baixa volumetria, tipicamente com poucos registros.

> [!note] Tabela de configuração
> Esta é uma tabela de setup com poucos registros. Os tipos de período são definidos durante a implementação e raramente são alterados após o go-live.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de calendários:** Cada calendário contábil referencia um tipo de período para seus períodos regulares.
- **Classificação de períodos:** Distinguir períodos mensais, trimestrais, anuais e personalizados.
- **Reporting por tipo:** Relatórios que agregam dados por trimestre ou ano usam o tipo de período para identificar a granularidade.
- **Configuração de orçamento:** Orçamentos podem ter calendários com tipos de período diferentes do calendário contábil principal.
- **Número de períodos por ano:** O campo `YEAR_TYPE_IN_NAME` define a quantidade de períodos por exercício fiscal.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | PK | Identificador único do tipo de período (ex: Month, Quarter, Year) | — | 🟢 100% |
| 2 | PERIOD_TYPE_ID | NUMBER(18) | NOT NULL | PK alternativa | Identificador numérico único do tipo de período | — | 🟢 95% |
| 3 | USER_PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Descrição | Nome exibido ao usuário (label) | — | 🟢 100% |
| 4 | YEAR_TYPE_IN_NAME | VARCHAR2(1) | NOT NULL | Classificação | Tipo de ano no nome: C (Calendar), F (Fiscal) | — | 🟢 90% |
| 5 | NUMBER_PER_FISCAL_YEAR | NUMBER(15) | NOT NULL | Configuração | Quantidade de períodos por exercício fiscal (12 para mensal, 4 para trimestral, etc.) | — | 🟢 100% |
| 6 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do tipo de período | — | 🟢 90% |
| 7 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 8 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟢 100% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma — esta é uma tabela raiz de configuração.

### Tabelas-filha (FK de saída)
- [[gl_period_statuses]] — via `PERIOD_TYPE` (tipo de período dos status)
- [[gl_balances]] — via `PERIOD_TYPE` (tipo de período dos saldos)

---

## 📎 Uso Típico

### Listar tipos de período disponíveis
```sql
SELECT pt.PERIOD_TYPE,
       pt.USER_PERIOD_TYPE,
       pt.NUMBER_PER_FISCAL_YEAR,
       pt.DESCRIPTION
FROM   GL_PERIOD_TYPES pt
ORDER BY pt.NUMBER_PER_FISCAL_YEAR DESC;
```

### Validar tipo de período de um calendário
```sql
SELECT pt.PERIOD_TYPE,
       pt.NUMBER_PER_FISCAL_YEAR
FROM   GL_PERIOD_TYPES pt
WHERE  pt.PERIOD_TYPE = :p_period_type;
```

### Filtros comuns
- `PERIOD_TYPE = 'Month'` — Períodos mensais (mais comum)
- `PERIOD_TYPE = 'Quarter'` — Períodos trimestrais
- `PERIOD_TYPE = 'Year'` — Períodos anuais
- `NUMBER_PER_FISCAL_YEAR = 12` — Calendário com 12 períodos

---

## 🔒 Observações

- A maioria das implementações utiliza o tipo **Month** com `NUMBER_PER_FISCAL_YEAR = 12` como padrão.
- O campo `YEAR_TYPE_IN_NAME` indica se o nome do período usa ano calendário (C) ou fiscal (F) — relevante para empresas com exercício fiscal diferente do calendário civil.
- Tipos de período customizados podem ser criados para calendários especiais (ex: semanas 4-4-5 para varejo), mas é raro em instituições financeiras.
- Esta tabela é consultada pelo Oracle durante a criação de novos períodos no calendário contábil.

---

## 🔗 PVOs Relacionados

### [[accountingperiodtypeextractpvo|AccountingPeriodTypeExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GlPeriodTypesCreatedBy | ✅ |
| CREATION_DATE | GlPeriodTypesCreationDate | ✅ |
| DESCRIPTION | GlPeriodTypesDescription | ✅ |
| LAST_UPDATE_DATE | GlPeriodTypesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GlPeriodTypesLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GlPeriodTypesLastUpdatedBy | ✅ |
| NUMBER_PER_FISCAL_YEAR | GlPeriodTypesNumberPerFiscalYear | ✅ |
| OBJECT_VERSION_NUMBER | GlPeriodTypesObjectVersionNumber | ✅ |
| PERIOD_TYPE | GlPeriodTypesPeriodType | ✅ |
| PERIOD_TYPE_ID | GlPeriodTypesPeriodTypeId | ✅ |
| USER_PERIOD_TYPE | GlPeriodTypesUserPeriodType | ✅ |
| YEAR_TYPE_IN_NAME | GlPeriodTypesYearTypeInName | ✅ |

### [[ledgerpvo|LedgerPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | AcctPeriodTypeDescription | — |
| NUMBER_PER_FISCAL_YEAR | AcctPeriodTypeNumberPerFiscalYear | — |
| PERIOD_TYPE | AcctPeriodTypePeriodType | — |
| PERIOD_TYPE_ID | AcctPeriodTypePeriodTypeId | — |
| USER_PERIOD_TYPE | AcctPeriodTypeUserPeriodType | — |
| YEAR_TYPE_IN_NAME | AcctPeriodTypeYearTypeInName | — |

---

## 📚 Referências

- [Oracle Docs — GL_PERIOD_TYPES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glperiodtypes-25792.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
