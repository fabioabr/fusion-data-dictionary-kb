---
id: DOC-HCM-708
doc_type: system-doc
title: "PER_REQUISITIONS_INTERFACE_TL — Interface de Requisições (Traduções)"
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
  - interface-tl
  - traducao
  - recrutamento
aliases:
  - PER_REQUISITIONS_INTERFACE_TL
  - per_requisitions_interface_tl
  - interface-requisicoes-traducao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_REQUISITIONS_INTERFACE_TL

## Visão Geral

Armazena as **traduções** dos dados de interface de requisições em múltiplos idiomas. Contém campos como título da vaga e descrição traduzidos para cada idioma configurado.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **tradução** — cada registro da tabela base possui N registros nesta tabela, um por idioma.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Integração multilíngue** — importar títulos e descrições de vagas em múltiplos idiomas
- **Migração de dados** — preservar traduções durante migração de sistemas legados
- **Publicação de vagas** — títulos traduzidos para portais de carreira internacionais

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da requisição | PER_REQUISITIONS_INTERFACE_B | 🟡 80% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | REQUISITION_TITLE | VARCHAR2(240) | NULL | Tradução | Título traduzido da requisição/vaga | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(4000) | NULL | Tradução | Descrição traduzida da vaga | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_requisitions_interface_b]] — via `REQUISITION_ID` (tabela base da requisição de interface)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Título traduzido de uma requisição na interface
```sql
SELECT tl.REQUISITION_TITLE, tl.DESCRIPTION
FROM   PER_REQUISITIONS_INTERFACE_TL tl
WHERE  tl.REQUISITION_ID = :p_requisition_id
  AND  tl.LANGUAGE = 'PT';
```

---

## Observações

- A chave primária é composta por `REQUISITION_ID` + `LANGUAGE`.
- Tabela de interface: dados temporários até processamento final.
- Deve ser carregada em conjunto com `PER_REQUISITIONS_INTERFACE_B`.

---

## Referências

- [Oracle Docs — PER_REQUISITIONS_INTERFACE_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perrequisitionsinterfacetl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
