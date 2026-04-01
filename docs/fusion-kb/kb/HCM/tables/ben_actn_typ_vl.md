---
id: DOC-HCM-024
doc_type: system-doc
title: "BEN_ACTN_TYP_VL — Tipos de Ação de Benefícios (View)"
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
  - tipos-acao
  - action-types
  - inscricao
aliases:
  - BEN_ACTN_TYP_VL
  - ben_actn_typ_vl
  - tipos-acao-beneficios
  - benefit-action-types
  - ben-actn-typ
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_ACTN_TYP_VL

## 📌 Visão Geral

View que apresenta os **tipos de ação de benefícios** com traduções no idioma da sessão. Define as ações disponíveis no processo de inscrição de benefícios (ex.: inscrição, alteração, cancelamento).

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view de lookup** — combina tabela base + traduções para acesso simplificado no idioma da sessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Workflow de benefícios:** Define as ações que podem ser executadas durante eventos de vida.
- **Configuração de processos:** Parametriza os tipos de ação disponíveis por plano.
- **Interface do usuário:** Fornece rótulos traduzidos para ações na interface.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTN_TYP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de ação | — | 🟢 90% |
| 2 | ACTN_TYP_CD | VARCHAR2(30) | NOT NULL | Código | Código do tipo de ação | — | 🟢 90% |
| 3 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido do tipo de ação | — | 🟢 90% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 5 | TYPE_CD | VARCHAR2(30) | NULL | Classificação | Categoria da ação (ENRT, CHNG, CNCL) | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada direta (tabela de configuração raiz).

### Tabelas-filha (FK de saída)
- [[ben_prtt_enrt_actn]] — via `ACTN_TYP_ID` (ações de inscrição)

---

## 📎 Uso Típico

### Tipos de ação disponíveis
```sql
SELECT at.ACTN_TYP_ID, at.ACTN_TYP_CD, at.NAME, at.TYPE_CD
FROM   BEN_ACTN_TYP_VL at
ORDER BY at.ACTN_TYP_CD;
```

### Filtros comuns
- `TYPE_CD = 'ENRT'` — Ações de inscrição
- `TYPE_CD = 'CHNG'` — Ações de alteração

---

## 🔒 Observações

- View com traduções — retorna dados no idioma da sessão do usuário.
- Os códigos de ação (`ACTN_TYP_CD`) são padronizados pelo Oracle e não devem ser modificados.

---

## 🔗 PVOs Relacionados

### [[benefitactiontypepvo|BenefitActionTypePVO]] (HCM · BICC: 6/78)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTN_TYP_ID | ActnTypId | ✅ |
| ACTN_TYP_LVL_CD | ActnTypLvlCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | ✅ |
| EAT_ATTRIBUTE1 | EatAttribute1 | — |
| EAT_ATTRIBUTE10 | EatAttribute10 | — |
| EAT_ATTRIBUTE11 | EatAttribute11 | — |
| EAT_ATTRIBUTE12 | EatAttribute12 | — |
| EAT_ATTRIBUTE13 | EatAttribute13 | — |
| EAT_ATTRIBUTE14 | EatAttribute14 | — |
| EAT_ATTRIBUTE15 | EatAttribute15 | — |
| EAT_ATTRIBUTE16 | EatAttribute16 | — |
| EAT_ATTRIBUTE17 | EatAttribute17 | — |
| EAT_ATTRIBUTE18 | EatAttribute18 | — |
| EAT_ATTRIBUTE19 | EatAttribute19 | — |
| EAT_ATTRIBUTE2 | EatAttribute2 | — |
| EAT_ATTRIBUTE20 | EatAttribute20 | — |
| EAT_ATTRIBUTE21 | EatAttribute21 | — |
| EAT_ATTRIBUTE22 | EatAttribute22 | — |
| EAT_ATTRIBUTE23 | EatAttribute23 | — |
| EAT_ATTRIBUTE24 | EatAttribute24 | — |
| EAT_ATTRIBUTE25 | EatAttribute25 | — |
| EAT_ATTRIBUTE26 | EatAttribute26 | — |
| EAT_ATTRIBUTE27 | EatAttribute27 | — |
| EAT_ATTRIBUTE28 | EatAttribute28 | — |
| EAT_ATTRIBUTE29 | EatAttribute29 | — |
| EAT_ATTRIBUTE3 | EatAttribute3 | — |
| EAT_ATTRIBUTE30 | EatAttribute30 | — |
| EAT_ATTRIBUTE4 | EatAttribute4 | — |
| EAT_ATTRIBUTE5 | EatAttribute5 | — |
| EAT_ATTRIBUTE6 | EatAttribute6 | — |
| EAT_ATTRIBUTE7 | EatAttribute7 | — |
| EAT_ATTRIBUTE8 | EatAttribute8 | — |
| EAT_ATTRIBUTE9 | EatAttribute9 | — |
| EAT_ATTRIBUTE_CATEGORY | EatAttributeCategory | — |
| EAT_ATTRIBUTE_DATE1 | EatAttributeDate1 | — |
| EAT_ATTRIBUTE_DATE10 | EatAttributeDate10 | — |
| EAT_ATTRIBUTE_DATE11 | EatAttributeDate11 | — |
| EAT_ATTRIBUTE_DATE12 | EatAttributeDate12 | — |
| EAT_ATTRIBUTE_DATE13 | EatAttributeDate13 | — |
| EAT_ATTRIBUTE_DATE14 | EatAttributeDate14 | — |
| EAT_ATTRIBUTE_DATE15 | EatAttributeDate15 | — |
| EAT_ATTRIBUTE_DATE2 | EatAttributeDate2 | — |
| EAT_ATTRIBUTE_DATE3 | EatAttributeDate3 | — |
| EAT_ATTRIBUTE_DATE4 | EatAttributeDate4 | — |
| EAT_ATTRIBUTE_DATE5 | EatAttributeDate5 | — |
| EAT_ATTRIBUTE_DATE6 | EatAttributeDate6 | — |
| EAT_ATTRIBUTE_DATE7 | EatAttributeDate7 | — |
| EAT_ATTRIBUTE_DATE8 | EatAttributeDate8 | — |
| EAT_ATTRIBUTE_DATE9 | EatAttributeDate9 | — |
| EAT_ATTRIBUTE_NUMBER1 | EatAttributeNumber1 | — |
| EAT_ATTRIBUTE_NUMBER10 | EatAttributeNumber10 | — |
| EAT_ATTRIBUTE_NUMBER11 | EatAttributeNumber11 | — |
| EAT_ATTRIBUTE_NUMBER12 | EatAttributeNumber12 | — |
| EAT_ATTRIBUTE_NUMBER13 | EatAttributeNumber13 | — |
| EAT_ATTRIBUTE_NUMBER14 | EatAttributeNumber14 | — |
| EAT_ATTRIBUTE_NUMBER15 | EatAttributeNumber15 | — |
| EAT_ATTRIBUTE_NUMBER16 | EatAttributeNumber16 | — |
| EAT_ATTRIBUTE_NUMBER17 | EatAttributeNumber17 | — |
| EAT_ATTRIBUTE_NUMBER18 | EatAttributeNumber18 | — |
| EAT_ATTRIBUTE_NUMBER19 | EatAttributeNumber19 | — |
| EAT_ATTRIBUTE_NUMBER2 | EatAttributeNumber2 | — |
| EAT_ATTRIBUTE_NUMBER20 | EatAttributeNumber20 | — |
| EAT_ATTRIBUTE_NUMBER3 | EatAttributeNumber3 | — |
| EAT_ATTRIBUTE_NUMBER4 | EatAttributeNumber4 | — |
| EAT_ATTRIBUTE_NUMBER5 | EatAttributeNumber5 | — |
| EAT_ATTRIBUTE_NUMBER6 | EatAttributeNumber6 | — |
| EAT_ATTRIBUTE_NUMBER7 | EatAttributeNumber7 | — |
| EAT_ATTRIBUTE_NUMBER8 | EatAttributeNumber8 | — |
| EAT_ATTRIBUTE_NUMBER9 | EatAttributeNumber9 | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| NAME | ActionTypeName | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| TYPE_CD | TypeCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_ACTN_TYP_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benactntypvl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
