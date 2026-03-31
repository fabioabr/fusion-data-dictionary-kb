---
id: DOC-HCM-107
doc_type: system-doc
title: "HNS_INJURED_PERSON_PARTS — Partes do Corpo Lesionadas"
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
  - health-safety
  - partes-corpo
  - lesoes
  - hns
aliases:
  - HNS_INJURED_PERSON_PARTS
  - hns_injured_person_parts
  - hns-injured-person-parts
  - DOC-HCM-107
  - partes-do-corpo-lesionadas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HNS_INJURED_PERSON_PARTS

## 📌 Visão Geral

Armazena os **detalhes das partes do corpo afetadas** em lesões de incidentes de segurança. Permite registrar múltiplas partes do corpo para uma mesma pessoa lesionada.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento de lesões:** Registro granular por parte do corpo.
- **Análise de riscos:** Identificação de padrões (ex: muitas lesões em mãos).
- **Equipamentos de proteção:** Base para análise de EPI adequado.
- **Relatórios médicos:** Dados para PCMSO e ASO.
- **Compliance OSHA:** Classificação detalhada conforme regulamentação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | INJURED_PERSON_PART_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | INJURED_PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa lesionada | [[hns_injured_persons]] | 🟢 90% |
| 3 | BODY_PART_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da parte do corpo | — | 🟡 80% |
| 4 | SIDE | VARCHAR2(30) | NULL | Classificação | Lateralidade (LEFT, RIGHT, BOTH, N/A) | — | 🟡 70% |
| 5 | INJURY_NATURE | VARCHAR2(30) | NULL | Classificação | Natureza da lesão (FRACTURE, BURN, CUT, SPRAIN) | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hns_injured_persons]] — via `INJURED_PERSON_ID` (pessoa acidentada com parte do corpo lesionada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Partes do corpo por lesionado
```sql
SELECT pp.BODY_PART_CODE, pp.SIDE, pp.INJURY_NATURE
FROM   HNS_INJURED_PERSON_PARTS pp
WHERE  pp.INJURED_PERSON_ID = :p_injured_person_id;
```

### Estatísticas por parte do corpo
```sql
SELECT pp.BODY_PART_CODE, COUNT(*) AS qtd
FROM   HNS_INJURED_PERSON_PARTS pp
GROUP BY pp.BODY_PART_CODE
ORDER BY qtd DESC;
```

---

## 🔒 Observações

- Uma pessoa lesionada pode ter múltiplas partes do corpo afetadas.
- O `BODY_PART_CODE` segue codificação padronizada (ex: HAND, ARM, HEAD, BACK).
- O `SIDE` é relevante para lesões unilaterais (LEFT/RIGHT).
- Dados alimentam análise de EPIs necessários por tipo de atividade.

---

## 🔗 PVOs Relacionados

### [[hnsinjuredpersonpartspvo|HNSInjuredPersonPartsPVO]] (HCM · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | HNSInjuredPersonPartsPEOCreatedBy | ✅ |
| CREATION_DATE | HNSInjuredPersonPartsPEOCreationDate | ✅ |
| DELETED_FLAG | HNSInjuredPersonPartsPEODeletedFlag | ✅ |
| INJURED_PART_CODE | HNSInjuredPersonPartsPEOInjuredPartCode | ✅ |
| INJURED_PERSON_ID | HNSInjuredPersonPartsPEOInjuredPersonId | ✅ |
| INJURED_PERSON_PART_ID | HNSInjuredPersonPartsPEOInjuredPersonPartId | ✅ |
| INJURY_NATURE_CODE | HNSInjuredPersonPartsPEOInjuryNatureCode | ✅ |
| LAST_UPDATE_DATE | HNSInjuredPersonPartsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | HNSInjuredPersonPartsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | HNSInjuredPersonPartsPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | HNSInjuredPersonPartsPEOObjectVersionNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — HNS_INJURED_PERSON_PARTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hnsinjuredpersonparts.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
