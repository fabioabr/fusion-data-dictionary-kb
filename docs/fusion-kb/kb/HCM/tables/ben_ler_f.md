---
id: DOC-HCM-045
doc_type: system-doc
title: "BEN_LER_F — Eventos de Vida (Life Event Reasons)"
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
  - eventos-vida
  - life-events
  - ler
aliases:
  - BEN_LER_F
  - ben_ler_f
  - eventos-vida-beneficios
  - life-event-reasons
  - ben-ler
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_LER_F

## 📌 Visão Geral

Armazena os **motivos de eventos de vida** configuráveis no módulo Benefits. Eventos de vida (casamento, nascimento, demissão, etc.) disparam reavaliação de elegibilidade e oportunidades de inscrição.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração de eventos:** Define os tipos de eventos de vida reconhecidos.
- **Trigger de reavaliação:** Cada evento dispara novo ciclo de elegibilidade.
- **Compliance:** Atende requisitos de períodos de inscrição especiais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_LER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de eventos de vida (life event reasons)
```sql
SELECT * FROM BEN_LER_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Eventos de Vida (Life Event Reasons)).

---

## 🔗 PVOs Relacionados

### [[lifeeventpvo|LifeEventPVO]] (HCM · BICC: 11/66)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CK_RLTD_PER_ELIG_FLAG | CkRltdPerEligFlag | — |
| CM_APLY_FLAG | CmAplyFlag | — |
| CONFIG_CHAR_1 | ConfigChar1 | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESC_TXT | DescTxt | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GLOBAL_FLAG | GlobalFlag | — |
| INSTRUCTION_TEXT | InstructionText | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LER_ATTRIBUTE1 | LerAttribute1 | — |
| LER_ATTRIBUTE10 | LerAttribute10 | — |
| LER_ATTRIBUTE11 | LerAttribute11 | — |
| LER_ATTRIBUTE12 | LerAttribute12 | — |
| LER_ATTRIBUTE13 | LerAttribute13 | — |
| LER_ATTRIBUTE14 | LerAttribute14 | — |
| LER_ATTRIBUTE15 | LerAttribute15 | — |
| LER_ATTRIBUTE16 | LerAttribute16 | — |
| LER_ATTRIBUTE17 | LerAttribute17 | — |
| LER_ATTRIBUTE18 | LerAttribute18 | — |
| LER_ATTRIBUTE19 | LerAttribute19 | — |
| LER_ATTRIBUTE2 | LerAttribute2 | — |
| LER_ATTRIBUTE20 | LerAttribute20 | — |
| LER_ATTRIBUTE21 | LerAttribute21 | — |
| LER_ATTRIBUTE22 | LerAttribute22 | — |
| LER_ATTRIBUTE23 | LerAttribute23 | — |
| LER_ATTRIBUTE24 | LerAttribute24 | — |
| LER_ATTRIBUTE25 | LerAttribute25 | — |
| LER_ATTRIBUTE26 | LerAttribute26 | — |
| LER_ATTRIBUTE27 | LerAttribute27 | — |
| LER_ATTRIBUTE28 | LerAttribute28 | — |
| LER_ATTRIBUTE29 | LerAttribute29 | — |
| LER_ATTRIBUTE3 | LerAttribute3 | — |
| LER_ATTRIBUTE30 | LerAttribute30 | — |
| LER_ATTRIBUTE4 | LerAttribute4 | — |
| LER_ATTRIBUTE5 | LerAttribute5 | — |
| LER_ATTRIBUTE6 | LerAttribute6 | — |
| LER_ATTRIBUTE7 | LerAttribute7 | — |
| LER_ATTRIBUTE8 | LerAttribute8 | — |
| LER_ATTRIBUTE9 | LerAttribute9 | — |
| LER_ATTRIBUTE_CATEGORY | LerAttributeCategory | — |
| LER_EVAL_RL | LerEvalRl | — |
| LER_ID | LerId | ✅ |
| LER_STAT_CD | LerStatCd | — |
| LF_EVT_OPER_CD | LfEvtOperCd | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OCRD_DT_DET_CD | OcrdDtDetCd | — |
| OVRIDG_LE_FLAG | OvridgLeFlag | ✅ |
| PROD_CD | ProdCd | — |
| PTNL_LER_TRTMT_CD | PtnlLerTrtmtCd | — |
| QUALG_EVT_FLAG | QualgEvtFlag | — |
| SELF_ASSIGNED_EVENT_FLAG | SelfAssignedEventFlag | — |
| SHORT_CODE | ShortCode | — |
| SHORT_NAME | ShortName | — |
| SLCTBL_SLF_SVC_CD | SlctblSlfSvcCd | — |
| TMLNS_DYS_NUM | TmlnsDysNum | — |
| TMLNS_EVAL_CD | TmlnsEvalCd | — |
| TMLNS_PERD_CD | TmlnsPerdCd | — |
| TMLNS_PERD_RL | TmlnsPerdRl | — |
| TYP_CD | TypCd | — |
| WHN_TO_PRCS_CD | WhnToPrcsCd | — |

---

## 📚 Referências

- [Oracle Docs — BEN_LER_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benlerf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
