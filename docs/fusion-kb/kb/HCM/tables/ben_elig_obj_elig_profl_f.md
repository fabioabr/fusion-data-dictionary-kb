---
id: DOC-HCM-040
doc_type: system-doc
title: "BEN_ELIG_OBJ_ELIG_PROFL_F — Objetos de Elegibilidade por Perfil"
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
  - benefits
  - objetos-elegibilidade-perfil
  - elig-obj-profile
aliases:
  - BEN_ELIG_OBJ_ELIG_PROFL_F
  - ben_elig_obj_elig_profl_f
  - objetos-elegibilidade-perfil
  - elig-obj-elig-profile
  - ben-elig-obj-elig-profl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_ELIG_OBJ_ELIG_PROFL_F

## 📌 Visão Geral

Armazena a **associação entre objetos de elegibilidade e perfis**, definindo quais critérios compõem cada perfil de elegibilidade.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Composição de perfis:** Define os critérios que formam cada perfil.
- **Configuração modular:** Permite reutilizar objetos em múltiplos perfis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_ELIG_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de objetos de elegibilidade por perfil
```sql
SELECT * FROM BEN_ELIG_OBJ_ELIG_PROFL_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Objetos de Elegibilidade por Perfil).

---

## 🔗 PVOs Relacionados

### [[eligibilityobjecteligprofileextractpvo|EligibilityObjectEligProfileExtractPVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELIG_OBJ_ELIG_PRFL_ID | EligObjEligPrflId | ✅ |
| ELIG_OBJ_ID | EligObjId | ✅ |
| ELIG_PRFL_ID | EligPrflId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MNDTRY_FLAG | MndtryFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_ELIG_OBJ_ELIG_PROFL_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/beneligobjeligproflf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
