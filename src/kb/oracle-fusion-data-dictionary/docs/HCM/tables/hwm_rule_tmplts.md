---
id: DOC-HCM-317
doc_type: system-doc
title: "HWM_RULE_TMPLTS — Templates de Regras"
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
  - modelos
aliases:
  - HWM_RULE_TMPLTS
  - hwm_rule_tmplts
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULE_TMPLTS

## 📌 Visão Geral

Define templates (modelos) de regras reutilizáveis para workforce management, permitindo a criação padronizada de regras com base em modelos pré-configurados.



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
| 1 | RULE_TMPLT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template de regra | — | 🟢 90% |
| 2 | TEMPLATE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do template | — | 🟡 80% |
| 3 | TEMPLATE_NAME | VARCHAR2(240) | NULL | Identificação | Nome do template | — | 🟡 80% |
| 4 | TEMPLATE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do template | — | 🟡 75% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do template (A/I) | — | 🟡 75% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição do template | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[hwm_rule_tmplt_inputs]] — via `RULE_TMPLT_ID` (entradas do template de regra)
- [[hwm_rule_tmplt_usages]] — via `RULE_TMPLT_ID` (usos do template de regra)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.TEMPLATE_CODE, t.TEMPLATE_NAME, t.TEMPLATE_TYPE, t.STATUS
FROM   HWM_RULE_TMPLTS t
WHERE  NVL(t.STATUS, 'A') = 'A'
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_RULE_TMPLTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rule_tmplts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
