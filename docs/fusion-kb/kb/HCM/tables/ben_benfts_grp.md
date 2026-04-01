---
id: DOC-HCM-026
doc_type: system-doc
title: "BEN_BENFTS_GRP — Grupos de Benefícios"
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
  - grupos-beneficios
  - benefit-groups
  - segmentacao
aliases:
  - BEN_BENFTS_GRP
  - ben_benfts_grp
  - grupos-beneficios-hcm
  - benefit-groups
  - ben-benfts-grp
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_BENFTS_GRP

## 📌 Visão Geral

Armazena os **grupos de benefícios** que permitem categorizar e organizar colaboradores para fins de elegibilidade e configuração de benefícios.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Segmentação:** Agrupa colaboradores com perfis similares para atribuição de benefícios.
- **Elegibilidade:** Critério de elegibilidade baseado em grupo.
- **Configuração simplificada:** Permite configurar benefícios por grupo ao invés de individualmente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BENFTS_GRP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do grupo | — | 🟢 90% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do grupo de benefícios | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Descrição | Descrição do grupo | — | 🟡 80% |
| 4 | BENFTS_GRP_CD | VARCHAR2(30) | NULL | Código | Código do grupo | — | 🟡 80% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta (tabela de configuração raiz).

### Tabelas-filha (FK de saída)
- [[ben_per_benefit_group_f]] — via `BENFTS_GRP_ID` (atribuição a colaboradores)
- [[ben_eligy_prfl]] — via `BENFTS_GRP_ID` (perfis de elegibilidade)

---

## 📎 Uso Típico

### Grupos de benefícios
```sql
SELECT bg.BENFTS_GRP_ID, bg.NAME, bg.BENFTS_GRP_CD
FROM   BEN_BENFTS_GRP bg
ORDER BY bg.NAME;
```

### Filtros comuns
- `BENFTS_GRP_CD = :p_code` — Grupo por código

---

## 🔒 Observações

- Tabela de configuração que define grupos para segmentação de benefícios.
- Colaboradores são atribuídos a grupos via `BEN_PER_BENEFIT_GROUP_F`.

---

## 🔗 PVOs Relacionados

### [[benefitgrouppvo|BenefitGroupPVO]] (HCM · BICC: 9/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENFTS_GRP_ID | BenftsGrpId | ✅ |
| BNG_ATTRIBUTE1 | BngAttribute1 | — |
| BNG_ATTRIBUTE10 | BngAttribute10 | — |
| BNG_ATTRIBUTE11 | BngAttribute11 | — |
| BNG_ATTRIBUTE12 | BngAttribute12 | — |
| BNG_ATTRIBUTE13 | BngAttribute13 | — |
| BNG_ATTRIBUTE14 | BngAttribute14 | — |
| BNG_ATTRIBUTE15 | BngAttribute15 | — |
| BNG_ATTRIBUTE16 | BngAttribute16 | — |
| BNG_ATTRIBUTE17 | BngAttribute17 | — |
| BNG_ATTRIBUTE18 | BngAttribute18 | — |
| BNG_ATTRIBUTE19 | BngAttribute19 | — |
| BNG_ATTRIBUTE2 | BngAttribute2 | — |
| BNG_ATTRIBUTE20 | BngAttribute20 | — |
| BNG_ATTRIBUTE21 | BngAttribute21 | — |
| BNG_ATTRIBUTE22 | BngAttribute22 | — |
| BNG_ATTRIBUTE23 | BngAttribute23 | — |
| BNG_ATTRIBUTE24 | BngAttribute24 | — |
| BNG_ATTRIBUTE25 | BngAttribute25 | — |
| BNG_ATTRIBUTE26 | BngAttribute26 | — |
| BNG_ATTRIBUTE27 | BngAttribute27 | — |
| BNG_ATTRIBUTE28 | BngAttribute28 | — |
| BNG_ATTRIBUTE29 | BngAttribute29 | — |
| BNG_ATTRIBUTE3 | BngAttribute3 | — |
| BNG_ATTRIBUTE30 | BngAttribute30 | — |
| BNG_ATTRIBUTE4 | BngAttribute4 | — |
| BNG_ATTRIBUTE5 | BngAttribute5 | — |
| BNG_ATTRIBUTE6 | BngAttribute6 | — |
| BNG_ATTRIBUTE7 | BngAttribute7 | — |
| BNG_ATTRIBUTE8 | BngAttribute8 | — |
| BNG_ATTRIBUTE9 | BngAttribute9 | — |
| BNG_ATTRIBUTE_CATEGORY | BngAttributeCategory | — |
| BNG_DESC | BngDesc | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

---

## 📚 Referências

- [Oracle Docs — BEN_BENFTS_GRP](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benbenftsgrp.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
