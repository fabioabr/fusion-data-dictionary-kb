---
id: DOC-HCM-307
doc_type: system-doc
title: "HWM_LAYER — Camadas de Workforce Management"
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
  - layer
  - hierarquia
  - workforce
aliases:
  - HWM_LAYER
  - hwm_layer
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_LAYER

## 📌 Visão Geral

Define as camadas (layers) na hierarquia de workforce management, permitindo organizar regras, cálculos e processamentos em diferentes níveis de abstração.



---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação hierárquica:** Organização de regras e processamentos em camadas para execução ordenada.
- **Flexibilidade de configuração:** Permite diferentes níveis de abstração para regras de workforce.
- **Processamento em cadeia:** Cada camada pode depender dos resultados da camada anterior.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | LAYER_ID | NUMBER(18) | NOT NULL | PK | Identificador único da camada | — | 🟡 80% |
| 2 | LAYER_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da camada | — | 🟡 80% |
| 3 | LAYER_NAME | VARCHAR2(240) | NULL | Identificação | Nome descritivo da camada | — | 🟡 75% |
| 4 | LAYER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da camada | — | 🟡 75% |
| 5 | SEQUENCE_NUMBER | NUMBER(9) | NULL | Controle | Ordem hierárquica | — | 🟡 75% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição da camada | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.LAYER_CODE, t.LAYER_NAME, t.LAYER_TYPE
FROM   HWM_LAYER t
ORDER BY t.SEQUENCE_NUMBER
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Workforce Management dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_LAYER](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_layer.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
