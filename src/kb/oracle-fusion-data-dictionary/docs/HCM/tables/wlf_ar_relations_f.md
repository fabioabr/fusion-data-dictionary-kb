---
id: DOC-HCM-723
doc_type: system-doc
title: "WLF_AR_RELATIONS_F — Relações de Registros de Atribuição (Learning)"
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
  - learning
  - workforce-learning
  - relações-atribuição
aliases:
  - WLF_AR_RELATIONS_F
  - wlf_ar_relations_f
  - wlf-ar-relations-f
  - relações-registros-atribuição
  - ar-relations-learning
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_AR_RELATIONS_F

## Visão Geral

Armazena as **relações entre registros de atribuição** (Assignment Records) no módulo Workforce Learning, vinculando atribuições de aprendizado a entidades relacionadas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Vinculação de aprendizado** — conecta registros de atribuição a itens de aprendizado.
- **Rastreabilidade** — mantém o histórico de relações entre atribuições e eventos.
- **Relatórios de treinamento** — suporta análises de treinamentos atribuídos vs. concluídos.
- **Compliance de capacitação** — evidência de treinamentos mandatórios cumpridos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AR_RELATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da relação | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | ASSIGNMENT_RECORD_ID | NUMBER(18) | NOT NULL | FK | Registro de atribuição de origem | WLF_ASSIGNMENT_RECORDS_F | 🟡 80% |
| 5 | RELATED_OBJECT_ID | NUMBER(18) | NULL | FK | Objeto relacionado (item de aprendizado, evento, etc.) | — | 🟡 70% |
| 6 | RELATION_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de relação | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_assignment_records_f]] — via `ASSIGNMENT_RECORD_ID` (registro de atribuição)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Relações de um registro de atribuição
```sql
SELECT ar.RELATION_TYPE, ar.RELATED_OBJECT_ID
FROM   WLF_AR_RELATIONS_F ar
WHERE  ar.ASSIGNMENT_RECORD_ID = :p_record_id
  AND  SYSDATE BETWEEN ar.EFFECTIVE_START_DATE AND ar.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ASSIGNMENT_RECORD_ID = :p_record_id` — Relações de um registro específico
- `RELATION_TYPE = :p_type` — Filtrar por tipo de relação

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- O campo RELATED_OBJECT_ID é genérico e pode apontar para diferentes entidades.

---

## Referências

- [Oracle Docs — WLF_AR_RELATIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfarrelationsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
