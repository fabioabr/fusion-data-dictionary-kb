---
id: DOC-HCM-234
doc_type: system-doc
title: "HRT_CONTENT_SOURCE_RLATS — Relacionamentos entre Conteudos e Fontes"
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
  - content-source
  - relacionamentos
aliases:
  - HRT_CONTENT_SOURCE_RLATS
  - hrt_content_source_rlats
  - hrt-content-source-rlats
  - content-source-relations
  - conteudo-fonte-relacionamentos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_CONTENT_SOURCE_RLATS

## 📌 Visao Geral

Armazena os **relacionamentos entre itens de conteudo e suas fontes** (sources). Conecta os itens de conteudo (competencias, habilidades) as fontes de dados de onde foram importados ou associados.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Rastreabilidade:** Identificar a origem de cada item de conteudo em um perfil.
- **Integracao:** Manter vinculo entre conteudos e seus provedores/fontes.
- **Auditoria:** Rastrear de onde cada competencia ou habilidade foi carregada.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTENT_SOURCE_RLAT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do relacionamento | — | 🟢 95% |
| 2 | CONTENT_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de conteudo relacionado | [[hrt_content_items_b]] | 🟢 95% |
| 3 | SOURCE_ID | NUMBER(18) | NOT NULL | FK | Fonte de dados associada | [[hrt_sources_b]] | 🟢 90% |
| 4 | CONTENT_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de conteudo | [[hrt_content_types_b]] | 🟢 90% |
| 5 | DATE_FROM | DATE | NULL | Data | Data de inicio do relacionamento | — | 🟢 85% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim do relacionamento | — | 🟢 85% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_content_items_b]] — via `CONTENT_ITEM_ID` (item de conteudo vinculado a fonte)
- [[hrt_sources_b]] — via `SOURCE_ID` (fonte de origem do conteudo)
- [[hrt_content_types_b]] — via `CONTENT_TYPE_ID` (tipo de conteudo da associacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Fontes de um item de conteudo
```sql
SELECT csr.SOURCE_ID, csr.DATE_FROM, csr.DATE_TO
FROM   HRT_CONTENT_SOURCE_RLATS csr
WHERE  csr.CONTENT_ITEM_ID = :p_content_item_id;
```

---

## 🔒 Observacoes

- Tabela de relacionamento N:N entre conteudos e fontes.
- Util para rastrear de qual provedor externo (LinkedIn, sistema legado, etc.) veio o item.

---

## 📚 Referencias

- [Oracle Docs — HRT_CONTENT_SOURCE_RLATS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtcontentsourcerlats.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
