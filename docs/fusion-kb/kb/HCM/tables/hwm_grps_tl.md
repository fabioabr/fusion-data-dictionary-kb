---
id: DOC-HCM-300
doc_type: system-doc
title: "HWM_GRPS_TL — Grupos de Workforce Management — Traducoes"
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
  - traducoes
  - nls
  - groups
aliases:
  - HWM_GRPS_TL
  - hwm_grps_tl
  - hwm-grps-tl
  - wfm-groups-tl
  - grupos-workforce-traducoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_GRPS_TL

## 📌 Visao Geral

Tabela de traducoes que armazena textos em multiplos idiomas para cada registro definido em [[hwm_grps_b]].

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Multi-idioma:** Nomes e descricoes traduzidos para multiplos idiomas.
- **Exibicao:** Textos traduzidos para interfaces de usuario e relatorios.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRP_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador do registro base | [[hwm_grps_b]] | 🟢 100% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Codigo do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | GRP_NAME | VARCHAR2(240) | NOT NULL | Dados | Nome/texto traduzido | — | 🟢 100% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao traduzida | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_grps_b]] — via `GRP_ID` (registro base do grupo de trabalho)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Texto traduzido no idioma do usuario
```sql
SELECT tl.GRP_NAME, tl.DESCRIPTION
FROM   HWM_GRPS_TL tl
WHERE  tl.GRP_ID = :p_id
  AND  tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observacoes

- Sufixo `_TL` indica tabela de traducao — PK composta por (GRP_ID, LANGUAGE).
- JOIN com [[hwm_grps_b]] para dados completos.

---

## 📚 Referencias

- [Oracle Docs — HWM_GRPS_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmgrpstl.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[groupmemberspvo|GroupMembersPVO]] (GL · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GroupsTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | GroupsTranslationPEOCreationDate | ✅ |
| DESCRIPTION | GroupsTranslationPEODescription | ✅ |
| ENTERPRISE_ID | GroupsTranslationPEOEnterpriseId | ✅ |
| GROUP_NAME | GroupsTranslationPEOGroupName | ✅ |
| GRP_ID | GroupsTranslationPEOGroupId | ✅ |
| LANGUAGE | GroupsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | GroupsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GroupsTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GroupsTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GroupsTranslationPEOObjectVersionNumber | ✅ |
| SOURCE_LANG | GroupsTranslationPEOSourceLang | ✅ |

### [[groupspvo|GroupsPVO]] (GL · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | GroupsTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | GroupsTranslationPEOCreationDate | ✅ |
| DESCRIPTION | GroupsTranslationPEODescription | ✅ |
| ENTERPRISE_ID | GroupsTranslationPEOEnterpriseId | ✅ |
| GROUP_NAME | GroupsTranslationPEOGroupName | ✅ |
| GRP_ID | GroupsTranslationPEOGroupId | ✅ |
| LANGUAGE | GroupsTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | GroupsTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GroupsTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GroupsTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GroupsTranslationPEOObjectVersionNumber | ✅ |
| SOURCE_LANG | GroupsTranslationPEOSourceLang | ✅ |
