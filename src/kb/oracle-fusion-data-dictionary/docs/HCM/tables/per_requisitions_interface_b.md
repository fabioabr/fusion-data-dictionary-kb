---
id: DOC-HCM-707
doc_type: system-doc
title: "PER_REQUISITIONS_INTERFACE_B — Interface de Requisições (Base)"
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
  - requisicoes
  - interface
  - integracao
  - recrutamento
aliases:
  - PER_REQUISITIONS_INTERFACE_B
  - per_requisitions_interface_b
  - interface-requisicoes-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_REQUISITIONS_INTERFACE_B

## Visão Geral

Tabela de **interface** para carga de requisições de vagas no Oracle Fusion HCM. Utilizada em processos de integração para importar requisições de recrutamento a partir de sistemas externos. O sufixo `_B` indica a tabela base (não traduzida).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **Base** — contém dados não dependentes de idioma. As traduções ficam na tabela `_TL` correspondente.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Integração de requisições** — carregar vagas a partir de sistemas externos (ATS, ERP legado)
- **Migração de dados** — importar histórico de requisições durante implementação
- **Automação de abertura de vagas** — alimentar requisições via processos batch
- **Sincronização com ATS** — manter requisições sincronizadas entre sistemas

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_ID | NUMBER(18) | NOT NULL | PK | Identificador da requisição na interface | — | 🟡 80% |
| 2 | REQUISITION_NUMBER | VARCHAR2(30) | NULL | Identificação | Número da requisição | — | 🟡 75% |
| 3 | POSITION_ID | NUMBER(18) | NULL | FK | Posição/cargo associado | HR_ALL_POSITIONS_F | 🟡 75% |
| 4 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização solicitante | HR_ALL_ORGANIZATION_UNITS | 🟡 75% |
| 5 | HIRING_MANAGER_ID | NUMBER(18) | NULL | FK | Gestor requisitante | PER_PERSONS | 🟡 75% |
| 6 | NUMBER_OF_OPENINGS | NUMBER | NULL | Requisição | Número de vagas | — | 🟡 75% |
| 7 | STATUS | VARCHAR2(30) | NULL | Controle | Status da interface (PENDING, PROCESSED, ERROR) | — | 🟡 70% |
| 8 | BATCH_ID | NUMBER(18) | NULL | Controle | Identificador do lote de importação | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` (posiÃ§Ã£o da requisiÃ§Ã£o de interface)
- [[hr_all_organization_units]] — via `ORGANIZATION_ID` (organizaÃ§Ã£o da requisiÃ§Ã£o de interface)
- [[per_persons]] — via `HIRING_MANAGER_ID` (gestor responsÃ¡vel pela contrataÃ§Ã£o)

### Tabelas-filha (FK de saída)
- [[per_requisitions_interface_tl]] — via `REQUISITION_ID` (traduÃ§Ãµes da requisiÃ§Ã£o de interface)

---

## Uso Típico

### Requisições pendentes de processamento
```sql
SELECT ri.REQUISITION_ID, ri.REQUISITION_NUMBER, ri.NUMBER_OF_OPENINGS, ri.STATUS
FROM   PER_REQUISITIONS_INTERFACE_B ri
WHERE  ri.STATUS = 'PENDING'
  AND  ri.BATCH_ID = :p_batch_id;
```

---

## Observações

- Tabela de interface: dados são temporários e devem ser processados para tabelas finais.
- O campo `STATUS` controla o fluxo de processamento.
- Registros com `STATUS = 'ERROR'` devem ser corrigidos e reprocessados.
- Traduções (título da vaga, descrição) ficam em `PER_REQUISITIONS_INTERFACE_TL`.

---

## Referências

- [Oracle Docs — PER_REQUISITIONS_INTERFACE_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perrequisitionsinterfaceb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
