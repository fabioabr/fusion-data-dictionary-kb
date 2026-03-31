---
id: DOC-HCM-690
doc_type: system-doc
title: "PER_PERSON_DLVRY_METHODS — Métodos de Entrega de Pessoa"
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
  - metodos-entrega
  - delivery-methods
  - comunicacao
  - notificacao
aliases:
  - PER_PERSON_DLVRY_METHODS
  - per_person_dlvry_methods
  - metodos-entrega-pessoa
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_DLVRY_METHODS

## Visão Geral

Armazena os **métodos de entrega** preferenciais de cada pessoa para comunicações e documentos. Define como o colaborador deseja receber holerites, informes de rendimento, notificações e outros documentos (digital, impresso, e-mail, etc.).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Entrega de holerites** — definir se o colaborador recebe impresso ou digital
- **Comunicações RH** — preferência de canal para notificações
- **Envio de documentos fiscais** — informe de rendimentos, DIRF
- **Compliance trabalhista** — garantir entrega efetiva de documentos obrigatórios
- **Redução de papel** — controlar migração para entregas digitais

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DELIVERY_METHOD_ID | NUMBER(18) | NOT NULL | PK | Identificador único do método de entrega | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 90% |
| 3 | DELIVERY_METHOD | VARCHAR2(30) | NOT NULL | Classificação | Tipo de método (EMAIL, PRINT, PORTAL) | — | 🟡 75% |
| 4 | DOCUMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de documento associado | — | 🟡 70% |
| 5 | PREFERRED_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é o método preferencial (Y/N) | — | 🟡 65% |
| 6 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 70% |
| 7 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa do método de entrega de documentos)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Método de entrega preferencial de um colaborador
```sql
SELECT dm.DELIVERY_METHOD, dm.DOCUMENT_TYPE
FROM   PER_PERSON_DLVRY_METHODS dm
WHERE  dm.PERSON_ID = :p_person_id
  AND  dm.PREFERRED_FLAG = 'Y';
```

---

## Observações

- Uma pessoa pode ter múltiplos métodos de entrega para diferentes tipos de documentos.
- O campo `PREFERRED_FLAG` indica a preferência principal quando há múltiplos métodos.
- Valores comuns de `DELIVERY_METHOD`: EMAIL, PRINT, PORTAL, MOBILE.

---

## Referências

- [Oracle Docs — PER_PERSON_DLVRY_METHODS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersondlvrymethods.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
