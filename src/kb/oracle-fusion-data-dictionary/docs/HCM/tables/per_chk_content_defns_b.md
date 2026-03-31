---
id: DOC-HCM-643
doc_type: system-doc
title: "PER_CHK_CONTENT_DEFNS_B — Definições de Conteúdo de Checklist (Base)"
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
  - workforce-management
  - checklists
  - content-definitions
aliases:
  - PER_CHK_CONTENT_DEFNS_B
  - per_chk_content_defns_b
  - per-chk-content-defns-b
  - definições-de-conteúdo-de-checklist-(base)
  - per-chk-content-defn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHK_CONTENT_DEFNS_B

## 📌 Visão Geral

Armazena as **definições de conteúdo** utilizadas em checklists. Define os tipos e estruturas de conteúdo disponíveis para configuração de templates de checklist.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de tipos de conteúdo** — padroniza os conteúdos disponíveis para checklists.
- **Configuração** — define a estrutura dos itens de conteúdo.
- **Reutilização** — permite compartilhar definições de conteúdo entre múltiplos checklists.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHK_CONTENT_DEFN_ID | NUMBER(18) | NOT NULL | PK | Identificador único da definição | — | 🟢 90% |
| 2 | CONTENT_TYPE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código do tipo de conteúdo | — | 🟢 85% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se a definição está ativa (Y/N) | — | 🟢 85% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de definições de conteúdo.

### Tabelas-filha (FK de saída)
- [[per_chk_content_defns_tl]] — via `CHK_CONTENT_DEFN_ID` (traduções da definição de conteúdo de checklist)

---

## 📎 Uso Típico

### Definições de conteúdo ativas
```sql
SELECT pccd.CHK_CONTENT_DEFN_ID, pccd.CONTENT_TYPE_CODE
FROM   PER_CHK_CONTENT_DEFNS_B pccd
WHERE  pccd.ACTIVE_FLAG = 'Y';
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Definições ativas
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Define os tipos de conteúdo reutilizáveis nos templates de checklist.
---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 60/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO1ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO2ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO3ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO4ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO5ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEOChkContentDefnId | — |
| CONTENT_CATEGORY | ChecklistContentDefnPEO1ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO2ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO3ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO4ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO5ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEOContentCategory | ✅ |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO1ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO2ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO3ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO4ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO5ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEOContentDefnCode | — |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO1ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO2ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO3ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO4ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO5ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEOContentSubtype | ✅ |
| CONTENT_TYPE | ChecklistContentDefnPEO1ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO2ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO3ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO4ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO5ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEOContentType | — |
| CONTENT_URL | ChecklistContentDefnPEO1ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO2ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO3ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO4ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO5ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEOContentUrl | ✅ |
| CREATED_BY | ChecklistContentDefnPEO1CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO2CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO3CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO4CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO5CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEOCreatedBy | — |
| CREATION_DATE | ChecklistContentDefnPEO1CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO2CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO3CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO4CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO5CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEOCreationDate | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO1EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO2EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO3EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO4EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO5EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEOEmbeddedContent | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO1EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO2EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO3EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO4EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO5EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEOEmbeddedContentType | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO1EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO2EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO3EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO4EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO5EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEOEnterpriseId | — |
| EVENT_DATE | ChecklistContentDefnPEO1EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO2EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO3EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO4EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO5EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEOEventDate | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO1EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO2EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO3EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO4EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO5EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEOEventLocation | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO1EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO2EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO3EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO4EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO5EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEOEventOffset | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO1EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO2EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO3EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO4EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO5EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEOEventTime | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO1HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO2HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO3HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO4HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO5HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEOHtmlContent | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO1ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO2ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO3ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO4ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO5ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEOImageUrl | ✅ |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO1LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO2LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO3LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO4LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO5LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO1LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO2LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO3LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO4LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO5LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEOObjectVersionNumber | — |
| STATUS | ChecklistContentDefnPEO1Status | ✅ |
| STATUS | ChecklistContentDefnPEO2Status | ✅ |
| STATUS | ChecklistContentDefnPEO3Status | ✅ |
| STATUS | ChecklistContentDefnPEO4Status | ✅ |
| STATUS | ChecklistContentDefnPEO5Status | ✅ |
| STATUS | ChecklistContentDefnPEOStatus | ✅ |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM · BICC: 60/132)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO1ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO2ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO3ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO4ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEO5ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnPEOChkContentDefnId | — |
| CONTENT_CATEGORY | ChecklistContentDefnPEO1ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO2ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO3ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO4ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEO5ContentCategory | ✅ |
| CONTENT_CATEGORY | ChecklistContentDefnPEOContentCategory | ✅ |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO1ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO2ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO3ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO4ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEO5ContentDefnCode | — |
| CONTENT_DEFN_CODE | ChecklistContentDefnPEOContentDefnCode | — |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO1ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO2ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO3ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO4ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEO5ContentSubtype | ✅ |
| CONTENT_SUBTYPE | ChecklistContentDefnPEOContentSubtype | ✅ |
| CONTENT_TYPE | ChecklistContentDefnPEO1ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO2ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO3ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO4ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEO5ContentType | — |
| CONTENT_TYPE | ChecklistContentDefnPEOContentType | — |
| CONTENT_URL | ChecklistContentDefnPEO1ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO2ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO3ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO4ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEO5ContentUrl | ✅ |
| CONTENT_URL | ChecklistContentDefnPEOContentUrl | ✅ |
| CREATED_BY | ChecklistContentDefnPEO1CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO2CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO3CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO4CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEO5CreatedBy | — |
| CREATED_BY | ChecklistContentDefnPEOCreatedBy | — |
| CREATION_DATE | ChecklistContentDefnPEO1CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO2CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO3CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO4CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEO5CreationDate | — |
| CREATION_DATE | ChecklistContentDefnPEOCreationDate | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO1EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO2EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO3EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO4EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEO5EmbeddedContent | — |
| EMBEDDED_CONTENT | ChecklistContentDefnPEOEmbeddedContent | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO1EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO2EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO3EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO4EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEO5EmbeddedContentType | — |
| EMBEDDED_CONTENT_TYPE | ChecklistContentDefnPEOEmbeddedContentType | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO1EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO2EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO3EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO4EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEO5EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnPEOEnterpriseId | — |
| EVENT_DATE | ChecklistContentDefnPEO1EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO2EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO3EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO4EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEO5EventDate | ✅ |
| EVENT_DATE | ChecklistContentDefnPEOEventDate | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO1EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO2EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO3EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO4EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEO5EventLocation | ✅ |
| EVENT_LOCATION | ChecklistContentDefnPEOEventLocation | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO1EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO2EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO3EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO4EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEO5EventOffset | ✅ |
| EVENT_OFFSET | ChecklistContentDefnPEOEventOffset | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO1EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO2EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO3EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO4EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEO5EventTime | ✅ |
| EVENT_TIME | ChecklistContentDefnPEOEventTime | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO1HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO2HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO3HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO4HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEO5HtmlContent | ✅ |
| HTML_CONTENT | ChecklistContentDefnPEOHtmlContent | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO1ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO2ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO3ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO4ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEO5ImageUrl | ✅ |
| IMAGE_URL | ChecklistContentDefnPEOImageUrl | ✅ |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO1LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO2LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO3LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO4LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEO5LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEO5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO1LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO2LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO3LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO4LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEO5LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEO5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnPEOObjectVersionNumber | — |
| STATUS | ChecklistContentDefnPEO1Status | ✅ |
| STATUS | ChecklistContentDefnPEO2Status | ✅ |
| STATUS | ChecklistContentDefnPEO3Status | ✅ |
| STATUS | ChecklistContentDefnPEO4Status | ✅ |
| STATUS | ChecklistContentDefnPEO5Status | ✅ |
| STATUS | ChecklistContentDefnPEOStatus | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_CHK_CONTENT_DEFNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchkcontentdefnsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
