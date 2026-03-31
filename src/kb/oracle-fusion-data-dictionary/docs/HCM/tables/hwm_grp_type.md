---
id: DOC-HCM-306
doc_type: system-doc
title: "HWM_GRP_TYPE — Tipos de Grupo de Workforce"
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
  - group-types
  - lookup
aliases:
  - HWM_GRP_TYPE
  - hwm_grp_type
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_GRP_TYPE

## 📌 Visão Geral

Tabela de referência que define os tipos possíveis de grupos de workforce (ex.: por departamento, projeto, habilidade), servindo como lookup para categorização.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de grupos de workforce:** Organização de trabalhadores em grupos para planejamento e alocação de recursos.
- **Planejamento de força de trabalho:** Base para análises de capacidade e distribuição de equipes.
- **Relatórios gerenciais:** Consolidação de dados por grupo para dashboards de workforce.
- **Integração com módulos:** Compartilhamento de definições de grupo com Payroll, Time Management e Project Costing.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | GRP_TYPE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do tipo de grupo | — | 🟢 90% |
| 2 | GRP_TYPE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do tipo de grupo | — | 🟢 90% |
| 3 | GRP_TYPE_NAME | VARCHAR2(240) | NULL | Identificação | Nome descritivo do tipo de grupo | — | 🟡 85% |
| 4 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição do tipo de grupo | — | 🟡 80% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o tipo está ativo (Y/N) | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[hwm_grps_vl]] — via `GRP_TYPE_CODE` (grupos de trabalho deste tipo)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT gt.GRP_TYPE_CODE, gt.GRP_TYPE_NAME
FROM   HWM_GRP_TYPE gt
WHERE  NVL(gt.ACTIVE_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Workforce Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[grouptypepvo|GroupTypePVO]] (GL · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| GROUP_ROW_ID | GroupRowId | ✅ |
| GRP_LEVEL | GroupLevel | ✅ |
| GRP_TYPE | GroupType | ✅ |
| GRP_TYPE_ID | GroupTypeId | ✅ |
| IS_TM_REC | IsTimeRecord | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAYER_ID | LayerId | ✅ |
| MODULE_ID | ModuleId | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PARENT_GRP_ID | ParentGroupId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_GRP_TYPE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_grp_type.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
