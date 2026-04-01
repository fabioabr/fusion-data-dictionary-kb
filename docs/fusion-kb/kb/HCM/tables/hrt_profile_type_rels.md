---
id: DOC-HCM-253
doc_type: system-doc
title: "HRT_PROFILE_TYPE_RELS — Relacionamentos entre Tipos de Perfil"
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
  - profile-type-relations
  - configuracao
aliases:
  - HRT_PROFILE_TYPE_RELS
  - hrt_profile_type_rels
  - hrt-profile-type-rels
  - profile-type-rels
  - relacionamentos-tipo-perfil
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_PROFILE_TYPE_RELS

## 📌 Visao Geral

Armazena os **relacionamentos entre tipos de perfil** — define quais tipos podem ser comparados entre si.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Configuracao:** Definir combinacoes validas para matching.
- **Gap analysis:** Controlar quais comparacoes sao permitidas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PROFILE_TYPE_REL_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 90% |
| 2 | PROFILE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de perfil de origem | [[hrt_profile_types_b]] | 🟢 95% |
| 3 | RELATED_PROFILE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de perfil relacionado | [[hrt_profile_types_b]] | 🟢 95% |
| 4 | RELATION_TYPE | VARCHAR2(30) | NOT NULL | Classificacao | Tipo de relacao | — | 🟡 80% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrt_profile_types_b]] — via `PROFILE_TYPE_ID` (tipo de perfil de origem da relacao)
- [[hrt_profile_types_b]] — via `RELATED_PROFILE_TYPE_ID` (tipo de perfil relacionado na associacao)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Tipos de perfil comparaveis
```sql
SELECT ptr.RELATED_PROFILE_TYPE_ID, ptr.RELATION_TYPE
FROM   HRT_PROFILE_TYPE_RELS ptr
WHERE  ptr.PROFILE_TYPE_ID = :p_profile_type_id;
```

---

## 🔒 Observacoes

- Define a regra de quais tipos podem ser comparados via best-fit analysis.

---

## 📚 Referencias

- [Oracle Docs — HRT_PROFILE_TYPE_RELS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtprofiletyperels.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[profiletyperelationspvo|ProfileTypeRelationsPVO]] (HCM · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADMIN_ONLY_FLAG | AdminOnlyFlag | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MODULE_ID | ModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PROFILE_TYPE_ID | ProfileTypeId | — |
| PROFILE_TYPE_RELATION_ID | ProfileTypeRelationId | ✅ |
| RELATION_ID | RelationId | — |
