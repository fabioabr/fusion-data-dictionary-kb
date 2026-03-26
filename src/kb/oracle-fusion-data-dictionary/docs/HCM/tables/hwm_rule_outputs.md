---
id: DOC-HCM-314
doc_type: system-doc
title: "HWM_RULE_OUTPUTS — Saídas de Regras de Workforce"
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
  - outputs
  - resultados
aliases:
  - HWM_RULE_OUTPUTS
  - hwm_rule_outputs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULE_OUTPUTS

## 📌 Visão Geral

Define os resultados (outputs) gerados pela execução das regras de workforce management, especificando os valores calculados e seus destinos.



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
| 1 | RULE_OUTPUT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da saída da regra | — | 🟢 90% |
| 2 | RULE_ID | NUMBER(18) | NOT NULL | FK | Referência à regra | HWM_RULES | 🟢 90% |
| 3 | OUTPUT_NAME | VARCHAR2(240) | NULL | Identificação | Nome do resultado | — | 🟡 80% |
| 4 | OUTPUT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do dado de saída | — | 🟡 75% |
| 5 | TARGET_TABLE | VARCHAR2(30) | NULL | Referência | Tabela de destino do resultado | — | 🟡 70% |
| 6 | TARGET_COLUMN | VARCHAR2(30) | NULL | Referência | Coluna de destino do resultado | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_rules]] — via `RULE_ID` (regra de tempo da saida)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.OUTPUT_NAME, t.OUTPUT_TYPE, t.TARGET_TABLE
FROM   HWM_RULE_OUTPUTS t
WHERE  t.RULE_ID = :p_rule_id
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_RULE_OUTPUTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rule_outputs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
