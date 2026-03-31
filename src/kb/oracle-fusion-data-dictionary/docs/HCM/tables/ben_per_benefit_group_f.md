---
id: DOC-HCM-047
doc_type: system-doc
title: "BEN_PER_BENEFIT_GROUP_F — Grupo de Benefício por Pessoa"
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
  - grupo-pessoa
  - person-benefit-group
aliases:
  - BEN_PER_BENEFIT_GROUP_F
  - ben_per_benefit_group_f
  - grupo-pessoa-beneficios
  - person-benefit-group
  - ben-per-benefit-group
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PER_BENEFIT_GROUP_F

## 📌 Visão Geral

Armazena a **atribuição de colaboradores a grupos de benefícios**, vinculando cada pessoa a um grupo para fins de elegibilidade.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Segmentação:** Vincula colaboradores a grupos de benefícios.
- **Elegibilidade:** Base para avaliação de elegibilidade por grupo.
- **Histórico:** Controle de mudanças de grupo ao longo do tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de grupo de benefício por pessoa
```sql
SELECT * FROM BEN_PER_BENEFIT_GROUP_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Grupo de Benefício por Pessoa).

---

## 🔗 PVOs Relacionados

### [[billchargedetailspvo|BillChargeDetailsPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | — |
| PERSON_ID | PersonId4 | — |

### [[billchargepaymentspvo|BillChargePaymentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | — |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | — |
| PERSON_ID | PersonId4 | — |

### [[billchargespvo|BillChargesPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | — |
| PERSON_ID | PersonId3 | — |

### [[billpaymentspvo|BillPaymentsPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | — |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | — |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | — |
| PERSON_ID | PersonId3 | — |

### [[participantenrollmentpvo|ParticipantEnrollmentPVO]] (HCM · BICC: 4/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate3 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | ✅ |

### [[personlifeeventpvo|PersonLifeEventPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate1 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate1 | ✅ |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | — |

### [[personpotentiallifeeventpvo|PersonPotentialLifeEventPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_GROUP_ID | BenefitGroupId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LE_BENEFIT_GROUP_ID | LeBenefitGroupId | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PER_BENEFIT_GROUP_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benperbenefitgroupf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
