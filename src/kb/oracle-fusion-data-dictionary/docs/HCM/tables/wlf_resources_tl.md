---
id: DOC-HCM-749
doc_type: system-doc
title: "WLF_RESOURCES_TL — Recursos (Traduções) (Learning)"
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
  - traduções
aliases:
  - WLF_RESOURCES_TL
  - wlf_resources_tl
  - wlf-resources-tl
  - recursos-traduções-learning
  - resources-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_RESOURCES_TL

## Visão Geral

Armazena as **traduções** dos recursos de Workforce Learning, incluindo nomes e descrições em múltiplos idiomas. Tabela de tradução (_TL) associada à WLF_RESOURCES_B.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — suporta organizações multinacionais com múltiplos idiomas.
- **Interface localizada** — exibe nomes de recursos no idioma do usuário.
- **Relatórios multilíngues** — permite gerar relatórios em idiomas específicos.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESOURCE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do recurso (referência à tabela _B) | WLF_RESOURCES_B | 🟡 80% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma (ex.: PT, EN, ES) | — | 🟢 90% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 85% |
| 4 | RESOURCE_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do recurso | — | 🟡 80% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida do recurso | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_resources_b]] — via `RESOURCE_ID` (tabela base do recurso de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Traduções de um recurso
```sql
SELECT tl.RESOURCE_NAME, tl.DESCRIPTION, tl.LANGUAGE
FROM   WLF_RESOURCES_TL tl
WHERE  tl.RESOURCE_ID = :p_resource_id
ORDER BY tl.LANGUAGE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Filtrar por idioma português
- `RESOURCE_ID = :p_id` — Traduções de um recurso específico

---

## Observações

- Tabela de tradução (_TL) — PK composta: RESOURCE_ID + LANGUAGE.
- SOURCE_LANG indica o idioma original da tradução.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Sempre associada à tabela base WLF_RESOURCES_B.

---

## Referências

- [Oracle Docs — WLF_RESOURCES_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfresourcestl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[resourcepvo|ResourcePVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | ResourceTranslationPEOCreatedBy | — |
| CREATION_DATE | ResourceTranslationPEOCreationDate | — |
| DESCRIPTION | ResourceTranslationPEODescription | ✅ |
| ENTERPRISE_ID | ResourceTranslationPEOEnterpriseId | — |
| LANGUAGE | ResourceTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | ResourceTranslationPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ResourceTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResourceTranslationPEOLastUpdatedBy | — |
| NAME | ResourceTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | ResourceTranslationPEOObjectVersionNumber | — |
| RESOURCE_ID | ResourceTranslationPEOResourceId | — |
| SOURCE_LANG | ResourceTranslationPEOSourceLang | — |

### [[trainingsupplierresourcepvo|TrainingSupplierResourcePVO]] (HCM · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TrainingSupplierResourceTranslationPEOCreatedBy1 | — |
| CREATION_DATE | TrainingSupplierResourceTranslationPEOCreationDate1 | — |
| DESCRIPTION | TrainingSupplierResourceTranslationPEODescription | ✅ |
| ENTERPRISE_ID | TrainingSupplierResourceTranslationPEOEnterpriseId1 | — |
| LANGUAGE | TrainingSupplierResourceTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | TrainingSupplierResourceTranslationPEOLastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | TrainingSupplierResourceTranslationPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | TrainingSupplierResourceTranslationPEOLastUpdatedBy1 | — |
| NAME | TrainingSupplierResourceTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | TrainingSupplierResourceTranslationPEOObjectVersionNumber1 | — |
| RESOURCE_ID | TrainingSupplierResourceTranslationPEOResourceId1 | — |
| SOURCE_LANG | TrainingSupplierResourceTranslationPEOSourceLang | — |
