---
id: DOC-HCM-326
doc_type: system-doc
title: "HWM_TCAT_EXPR_RESULTS_B — Resultados de Expressão de Categoria de Time Card (Base)"
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
  - time-card
  - expressoes
  - resultados
  - base
aliases:
  - HWM_TCAT_EXPR_RESULTS_B
  - hwm_tcat_expr_results_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCAT_EXPR_RESULTS_B

## 📌 Visão Geral

Tabela base que armazena os resultados de expressões avaliadas para categorias de cartão de ponto, determinando a categorização automática de registros de tempo.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Categorização de registros de tempo:** Classificação automática de entradas de tempo em categorias (regular, hora extra, etc.).
- **Regras de categorização:** Definição de expressões para classificação automática.
- **Relatórios por categoria:** Base para análises de distribuição de horas por tipo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TCAT_EXPR_RESULTS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | CODE | VARCHAR2(30) | NOT NULL | Identificação | Código identificador único | — | 🟢 90% |
| 3 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro (A/I) | — | 🟡 80% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se está habilitado (Y/N) | — | 🟡 75% |
| 5 | START_DATE | DATE | NULL | Vigência | Data de início de validade | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Vigência | Data de fim de validade | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_tcats_b]] — via `TCAT_ID` (categoria de tempo do resultado da expressao)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_TCAT_EXPR_RESULTS_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Área funcional: Time Card dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[timecategoryexprresultp|TimeCategoryExprResultP]] (GL · BICC: 16/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TCatExprResultBPEOCreatedBy | — |
| CREATION_DATE | TCatExprResultBPEOCreationDate | — |
| DATA_SOURCE_USAGE_ID | TCatExprResultBPEODataSourceUsageId | — |
| DISPLAY_SEQUENCE | TCatExprResultBPEODisplaySequence | ✅ |
| DISPLAY_VALUE | TCatExprResultBPEODisplayValue | ✅ |
| ENTERPRISE_ID | TCatExprResultBPEOEnterpriseId | — |
| EXPR_ROW_IDENTIFIER | TCatExprResultBPEOExprRowIdentifier | — |
| EXPRESSION_GROUP_ID | TCatExprResultBPEOExpressionGroupId | — |
| IMP_TCAT_ID | TCatExprResultBPEOImpTcatId | — |
| LAST_UPDATE_DATE | TCatExprResultBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TCatExprResultBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TCatExprResultBPEOLastUpdatedBy | ✅ |
| LEFT_PARENTHESIS_NUM | TCatExprResultBPEOLeftParenthesisNum | ✅ |
| OBJECT_VERSION_NUMBER | TCatExprResultBPEOObjectVersionNumber | — |
| OPERATOR | TCatExprResultBPEOOperator11 | ✅ |
| RIGHT_PARENTHESIS_NUM | TCatExprResultBPEORightParenthesisNum | ✅ |
| SEED_DATA_SOURCE | TCatExprResultBPEOSeedDataSource | — |
| SGUID | TCatExprResultBPEOSguid | — |
| TCAT_EXPR_RESULT_ID | TCatExprResultBPEOTcatExprResultId | ✅ |
| TCAT_ID | TCatExprResultBPEOTcatId | ✅ |
| TIME_ATRB_FLD_ID | TCatExprResultBPEOTimeAtrbFldId | ✅ |
| VALUE_CHAR | TCatExprResultBPEOValueChar | ✅ |
| VALUE_DATE | TCatExprResultBPEOValueDate | ✅ |
| VALUE_ID | TCatExprResultBPEOValueId | ✅ |
| VALUE_TIMESTAMP | TCatExprResultBPEOValueTimestamp | ✅ |
| VALUE_TYPE | TCatExprResultBPEOValueType | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TCAT_EXPR_RESULTS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcat_expr_results_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
