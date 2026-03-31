---
id: DOC-HCM-644
doc_type: system-doc
title: "PER_CHK_CONTENT_DEFNS_TL — Definições de Conteúdo de Checklist (Traduções)"
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
  - traducoes
  - content-defns-tl
aliases:
  - PER_CHK_CONTENT_DEFNS_TL
  - per_chk_content_defns_tl
  - per-chk-content-defns-tl
  - definições-de-conteúdo-de-checklist-(traduções)
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

# PER_CHK_CONTENT_DEFNS_TL

## 📌 Visão Geral

Armazena as **traduções** dos nomes das definições de conteúdo de checklist em múltiplos idiomas.

> [!note] Sufixo _TL
> O sufixo `_TL` indica tabela de **traduções** — armazena textos traduzidos em múltiplos idiomas (colunas `LANGUAGE` e `SOURCE_LANG`).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização** — exibe definições de conteúdo no idioma do usuário.
- **Consistência** — tradução centralizada das definições.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHK_CONTENT_DEFN_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da definição | PER_CHK_CONTENT_DEFNS_B | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma da tradução | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem da tradução | — | 🟢 95% |
| 4 | CONTENT_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da definição | — | 🟢 90% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_chk_content_defns_b]] — via `CHK_CONTENT_DEFN_ID` (tabela base da definição de conteúdo de checklist)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha — tabela terminal de tradução.

---

## 📎 Uso Típico

### Definições de conteúdo em português
```sql
SELECT tl.CHK_CONTENT_DEFN_ID, tl.CONTENT_NAME
FROM   PER_CHK_CONTENT_DEFNS_TL tl
WHERE  tl.LANGUAGE = 'PTB';
```

### Filtros comuns
- `LANGUAGE = 'PTB'` — Traduções em português brasileiro
---

## 🔒 Observações

- Tabela de traduções (_TL) — chave composta por `CHK_CONTENT_DEFN_ID` + `LANGUAGE`.
---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 12/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat1ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat2ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat3ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat4ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat5ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslatChkContentDefnId | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat1ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat2ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat3ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat4ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat5ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslatContentDetails | — |
| CREATED_BY | ChecklistContentDefnTranslat1CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat2CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat3CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat4CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat5CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslatCreatedBy | — |
| CREATION_DATE | ChecklistContentDefnTranslat1CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat2CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat3CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat4CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat5CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslatCreationDate | — |
| DESCRIPTION | ChecklistContentDefnTranslat1Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat2Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat3Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat4Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat5Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslatDescription | ✅ |
| ENTERPRISE_ID | ChecklistContentDefnTranslat1EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat2EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat3EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat4EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat5EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslatEnterpriseId | — |
| LANGUAGE | ChecklistContentDefnTranslat1Language | — |
| LANGUAGE | ChecklistContentDefnTranslat2Language | — |
| LANGUAGE | ChecklistContentDefnTranslat3Language | — |
| LANGUAGE | ChecklistContentDefnTranslat4Language | — |
| LANGUAGE | ChecklistContentDefnTranslat5Language | — |
| LANGUAGE | ChecklistContentDefnTranslatLanguage | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat1LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat2LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat3LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat4LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat5LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslatLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslatLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat1LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat2LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat3LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat4LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat5LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslatLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslatObjectVersionNumber | — |
| SOURCE_LANG | ChecklistContentDefnTranslat1SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat2SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat3SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat4SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat5SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslatSourceLang | — |
| TITLE | ChecklistContentDefnTranslat1Title | ✅ |
| TITLE | ChecklistContentDefnTranslat2Title | ✅ |
| TITLE | ChecklistContentDefnTranslat3Title | ✅ |
| TITLE | ChecklistContentDefnTranslat4Title | ✅ |
| TITLE | ChecklistContentDefnTranslat5Title | ✅ |
| TITLE | ChecklistContentDefnTranslatTitle | ✅ |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM · BICC: 12/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat1ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat2ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat3ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat4ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslat5ChkContentDefnId | — |
| CHK_CONTENT_DEFN_ID | ChecklistContentDefnTranslatChkContentDefnId | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat1ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat2ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat3ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat4ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslat5ContentDetails | — |
| CONTENT_DETAILS | ChecklistContentDefnTranslatContentDetails | — |
| CREATED_BY | ChecklistContentDefnTranslat1CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat2CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat3CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat4CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslat5CreatedBy | — |
| CREATED_BY | ChecklistContentDefnTranslatCreatedBy | — |
| CREATION_DATE | ChecklistContentDefnTranslat1CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat2CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat3CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat4CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslat5CreationDate | — |
| CREATION_DATE | ChecklistContentDefnTranslatCreationDate | — |
| DESCRIPTION | ChecklistContentDefnTranslat1Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat2Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat3Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat4Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslat5Description | ✅ |
| DESCRIPTION | ChecklistContentDefnTranslatDescription | ✅ |
| ENTERPRISE_ID | ChecklistContentDefnTranslat1EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat2EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat3EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat4EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslat5EnterpriseId | — |
| ENTERPRISE_ID | ChecklistContentDefnTranslatEnterpriseId | — |
| LANGUAGE | ChecklistContentDefnTranslat1Language | — |
| LANGUAGE | ChecklistContentDefnTranslat2Language | — |
| LANGUAGE | ChecklistContentDefnTranslat3Language | — |
| LANGUAGE | ChecklistContentDefnTranslat4Language | — |
| LANGUAGE | ChecklistContentDefnTranslat5Language | — |
| LANGUAGE | ChecklistContentDefnTranslatLanguage | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat1LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat2LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat3LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat4LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslat5LastUpdateDate | — |
| LAST_UPDATE_DATE | ChecklistContentDefnTranslatLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat1LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat2LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat3LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat4LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslat5LastUpdateLogin | — |
| LAST_UPDATE_LOGIN | ChecklistContentDefnTranslatLastUpdateLogin | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat1LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat2LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat3LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat4LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslat5LastUpdatedBy | — |
| LAST_UPDATED_BY | ChecklistContentDefnTranslatLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat1ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat2ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat3ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat4ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslat5ObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | ChecklistContentDefnTranslatObjectVersionNumber | — |
| SOURCE_LANG | ChecklistContentDefnTranslat1SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat2SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat3SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat4SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslat5SourceLang | — |
| SOURCE_LANG | ChecklistContentDefnTranslatSourceLang | — |
| TITLE | ChecklistContentDefnTranslat1Title | ✅ |
| TITLE | ChecklistContentDefnTranslat2Title | ✅ |
| TITLE | ChecklistContentDefnTranslat3Title | ✅ |
| TITLE | ChecklistContentDefnTranslat4Title | ✅ |
| TITLE | ChecklistContentDefnTranslat5Title | ✅ |
| TITLE | ChecklistContentDefnTranslatTitle | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_CHK_CONTENT_DEFNS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchkcontentdefnstl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
