---
id: DOC-HCM-319
doc_type: system-doc
title: "HWM_RULE_TMPLT_INPUTS — Entradas de Templates de Regras"
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
  - regras
  - templates
  - inputs
aliases:
  - HWM_RULE_TMPLT_INPUTS
  - hwm_rule_tmplt_inputs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULE_TMPLT_INPUTS

## 📌 Visão Geral

Define os parâmetros de entrada padrão para cada template de regra, servindo como especificação dos inputs esperados pelo modelo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Motor de regras:** Definição e execução de regras de cálculo para processamento de tempo e ausências.
- **Configuração flexível:** Permite criação de regras customizadas sem desenvolvimento.
- **Reutilização:** Templates e conjuntos de regras promovem padronização e reuso.
- **Auditoria de cálculos:** Rastreamento de quais regras foram aplicadas em cada processamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | RULE_INPUT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da entrada da regra | — | 🟢 90% |
| 2 | RULE_ID | NUMBER(18) | NOT NULL | FK | Referência à regra | HWM_RULES | 🟢 90% |
| 3 | INPUT_NAME | VARCHAR2(240) | NULL | Identificação | Nome do parâmetro de entrada | — | 🟡 80% |
| 4 | INPUT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do dado de entrada | — | 🟡 75% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é obrigatório (Y/N) | — | 🟡 75% |
| 6 | DEFAULT_VALUE | VARCHAR2(240) | NULL | Dados | Valor padrão do parâmetro | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_rule_tmplts]] — via `RULE_TMPLT_ID` (template de regra da entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.INPUT_NAME, t.INPUT_TYPE, t.REQUIRED_FLAG, t.DEFAULT_VALUE
FROM   HWM_RULE_TMPLT_INPUTS t
WHERE  t.RULE_TMPLT_ID = :p_tmplt_id
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[ruletemplateinputpvo|RuleTemplateInputPVO]] (GL · BICC: 12/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RuleTemplateInputBPEOCreatedBy | ✅ |
| CREATION_DATE | RuleTemplateInputBPEOCreationDate | ✅ |
| DISPLAY_SEQUENCE | RuleTemplateInputBPEODisplaySequence | ✅ |
| ENTERPRISE_ID | RuleTemplateInputBPEOEnterpriseId | — |
| INPUT_NAME | RuleTemplateInputBPEOInputName | ✅ |
| LAST_UPDATE_DATE | RuleTemplateInputBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RuleTemplateInputBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RuleTemplateInputBPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | RuleTemplateInputBPEOObjectVersionNumber | — |
| PARM_VALUE_REQUIRED | RuleTemplateInputBPEOParmValueRequired | ✅ |
| RULE_PARAMETER_TYPE | RuleTemplateInputBPEORuleParameterType | ✅ |
| RULE_TMPLT_INPUT_ID | RuleTemplateInputBPEORuleTmpltInputId | ✅ |
| RULE_TMPLTS_ID | RuleTemplateInputBPEORuleTmpltsId | ✅ |
| SEED_DATA_SOURCE | RuleTemplateInputBPEOSeedDataSource | — |
| SGUID | RuleTemplateInputBPEOSguid | — |
| USER_DEFINED_NAME | RuleTemplateInputBPEOUserDefinedName | — |
| VALUE_SET_ID | RuleTemplateInputBPEOValueSetId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_RULE_TMPLT_INPUTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rule_tmplt_inputs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
