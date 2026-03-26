---
id: DOC-HCM-739
doc_type: system-doc
title: "WLF_LI_CONTENT_F — Conteúdo de Itens de Aprendizado"
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
  - conteúdo-aprendizado
aliases:
  - WLF_LI_CONTENT_F
  - wlf_li_content_f
  - wlf-li-content-f
  - conteúdo-itens-aprendizado
  - li-content
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LI_CONTENT_F

## Visão Geral

Armazena os **metadados de conteúdo** associados aos itens de aprendizado, incluindo referências a materiais didáticos, documentos, vídeos e outros recursos. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de conteúdo** — referencia materiais didáticos vinculados a treinamentos.
- **Biblioteca de recursos** — catálogo de materiais disponíveis por item de aprendizado.
- **Versionamento** — controla versões de materiais ao longo do tempo.
- **Entrega de conteúdo** — define como e onde o conteúdo está disponível.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LI_CONTENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do conteúdo | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado pai | WLF_LEARNING_ITEMS_F | 🟢 85% |
| 5 | CONTENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de conteúdo (document, video, scorm) | — | 🟡 75% |
| 6 | CONTENT_URL | VARCHAR2(2000) | NULL | Dados | URL ou referência ao conteúdo | — | 🟡 70% |
| 7 | CONTENT_FORMAT | VARCHAR2(30) | NULL | Classificação | Formato do conteúdo (PDF, MP4, HTML, SCORM) | — | 🟡 70% |
| 8 | VERSION_NUMBER | NUMBER(9) | NULL | Controle | Versão do conteúdo | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Conteúdos de um item de aprendizado
```sql
SELECT lc.CONTENT_TYPE, lc.CONTENT_FORMAT, lc.CONTENT_URL, lc.VERSION_NUMBER
FROM   WLF_LI_CONTENT_F lc
WHERE  lc.LEARNING_ITEM_ID = :p_learning_item_id
  AND  SYSDATE BETWEEN lc.EFFECTIVE_START_DATE AND lc.EFFECTIVE_END_DATE
ORDER BY lc.VERSION_NUMBER DESC;
```

### Filtros comuns
- `LEARNING_ITEM_ID = :p_item_id` — Conteúdos de um item
- `CONTENT_TYPE = 'SCORM'` — Apenas conteúdos SCORM

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- CONTENT_URL pode referenciar repositórios externos de conteúdo.
- LI = Learning Item.

---

## Referências

- [Oracle Docs — WLF_LI_CONTENT_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlflicontentf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
