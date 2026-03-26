---
id: DOC-HCM-312
doc_type: system-doc
title: "HWM_RULES — Regras de Workforce Management"
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
  - calculo
  - workforce
aliases:
  - HWM_RULES
  - hwm_rules
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULES

## 📌 Visão Geral

Tabela central de regras do módulo de workforce management, contendo definições de regras de cálculo, validação e processamento aplicadas a registros de tempo e ausências.



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
| 1 | RULE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra | — | 🟢 90% |
| 2 | RULE_NAME | VARCHAR2(240) | NULL | Identificação | Nome da regra | — | 🟡 80% |
| 3 | RULE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da regra | — | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificação | Status da regra (A/I) | — | 🟡 75% |
| 5 | PRIORITY | NUMBER(9) | NULL | Controle | Prioridade de execução | — | 🟡 70% |
| 6 | EXPRESSION | CLOB | NULL | Dados | Expressão/fórmula da regra | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[hwm_rule_inputs]] — via `RULE_ID` (entradas da regra de tempo)
- [[hwm_rule_outputs]] — via `RULE_ID` (saidas da regra de tempo)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.RULE_NAME, t.RULE_TYPE, t.STATUS, t.PRIORITY
FROM   HWM_RULES t
WHERE  NVL(t.STATUS, 'A') = 'A'
ORDER BY t.PRIORITY
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_RULES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rules.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
