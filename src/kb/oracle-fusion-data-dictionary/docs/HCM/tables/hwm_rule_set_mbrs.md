---
id: DOC-HCM-316
doc_type: system-doc
title: "HWM_RULE_SET_MBRS — Membros de Conjuntos de Regras"
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
  - conjuntos
  - membros
aliases:
  - HWM_RULE_SET_MBRS
  - hwm_rule_set_mbrs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULE_SET_MBRS

## 📌 Visão Geral

Armazena a associação de regras individuais como membros de conjuntos de regras, definindo a composição e ordem de execução dentro de cada conjunto.



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
| 1 | RULE_SET_MBR_ID | NUMBER(18) | NOT NULL | PK | Identificador da associação regra-conjunto | — | 🟢 90% |
| 2 | RULE_SET_ID | NUMBER(18) | NOT NULL | FK | Referência ao conjunto de regras | HWM_RULE_SETS_F | 🟢 90% |
| 3 | RULE_ID | NUMBER(18) | NOT NULL | FK | Referência à regra individual | HWM_RULES | 🟢 90% |
| 4 | SEQUENCE_NUMBER | NUMBER(9) | NULL | Controle | Ordem de execução dentro do conjunto | — | 🟡 80% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se está habilitado (Y/N) | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_rule_sets_f]] — via `RULE_SET_ID` (conjunto de regras)
- [[hwm_rules]] — via `RULE_ID` (regra individual)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT m.RULE_SET_MBR_ID, m.RULE_SET_ID, m.RULE_ID, m.SEQUENCE_NUMBER
FROM   HWM_RULE_SET_MBRS m
WHERE  NVL(m.ENABLED_FLAG, 'Y') = 'Y'
ORDER BY m.SEQUENCE_NUMBER
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_RULE_SET_MBRS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rule_set_mbrs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
