---
id: DOC-HCM-680
doc_type: system-doc
title: "PER_MANAGER_HRCHY_DN — Hierarquia de Gestores (Denormalized)"
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
  - hierarquia-gestores
  - manager-hierarchy
  - denormalized
  - organograma
aliases:
  - PER_MANAGER_HRCHY_DN
  - per_manager_hrchy_dn
  - hierarquia-gestores-dn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_MANAGER_HRCHY_DN

## Visão Geral

Armazena a **hierarquia de gestores desnormalizada** com informações adicionais de contexto. Contém dados de gestão pré-processados para facilitar consultas de relatório e análise organizacional sem necessidade de joins recursivos.

> [!note] Sufixo _DN
> O sufixo `_DN` indica tabela **Denormalized** — dados desnormalizados para consultas diretas e relatórios.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Relatórios OTBI** — fonte otimizada para relatórios Oracle Transactional BI
- **Análise organizacional** — visualizar cadeia de gestão com dados descritivos
- **Segurança de dados** — controlar visibilidade por árvore hierárquica
- **Dashboards executivos** — exibir métricas por nível e cadeia de gestão

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_PERSONS | 🟢 90% |
| 2 | MANAGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do gestor | PER_PERSONS | 🟢 90% |
| 3 | MANAGER_LEVEL | NUMBER | NOT NULL | Hierarquia | Nível do gestor na cadeia hierárquica | — | 🟡 80% |
| 4 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo do colaborador | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 5 | MANAGER_ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo do gestor | PER_ALL_ASSIGNMENTS_M | 🟡 75% |
| 6 | MANAGER_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de gestão (LINE_MANAGER, etc.) | — | 🟡 70% |
| 7 | PERSON_NAME | VARCHAR2(360) | NULL | Descritivo | Nome completo do colaborador | — | 🟡 70% |
| 8 | MANAGER_NAME | VARCHAR2(360) | NULL | Descritivo | Nome completo do gestor | — | 🟡 70% |
| 9 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 10 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` e `MANAGER_ID` (pessoa na hierarquia gerencial desnormalizada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` e `MANAGER_ASSIGNMENT_ID` (vínculo na hierarquia gerencial desnormalizada)

### Tabelas-filha (FK de saída)

---

## Uso Típico

### Listar cadeia de gestão com nomes
```sql
SELECT dn.MANAGER_NAME, dn.MANAGER_LEVEL, dn.MANAGER_TYPE
FROM   PER_MANAGER_HRCHY_DN dn
WHERE  dn.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN dn.EFFECTIVE_START_DATE AND dn.EFFECTIVE_END_DATE
ORDER BY dn.MANAGER_LEVEL;
```

---

## Observações

- Tabela desnormalizada: contém nomes e dados descritivos para evitar joins adicionais.
- Ideal para relatórios e dashboards onde performance é prioridade.
- Dados são atualizados por processos batch — pode haver defasagem.

---

## Referências

- [Oracle Docs — PER_MANAGER_HRCHY_DN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/permanagerhrchydn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
