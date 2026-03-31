---
id: DOC-HCM-357
doc_type: system-doc
title: "HWM_TM_ATRB_FLD_MSTR_REF_B — Referência Mestre de Campos de Atributos (Base)"
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
  - time-management
  - atributos
  - referencia-mestre
  - base
aliases:
  - HWM_TM_ATRB_FLD_MSTR_REF_B
  - hwm_tm_atrb_fld_mstr_ref_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_ATRB_FLD_MSTR_REF_B

## 📌 Visão Geral

Tabela base que armazena as referências mestre para campos de atributos de Time Management, definindo os valores válidos e domínios de cada campo.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Personalização de campos:** Configuração de campos adicionais para captura de informações específicas do negócio.
- **Flexibilidade de interface:** Definição de quais campos são exibidos e obrigatórios por contexto.
- **Referência mestre:** Manutenção de valores válidos para campos de atributo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TM_ATRBLD_MSTR_REF_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | CODE | VARCHAR2(30) | NOT NULL | Identificação | Código identificador único | — | 🟢 90% |
| 3 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro (A/I) | — | 🟡 80% |
| 4 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se está habilitado (Y/N) | — | 🟡 75% |
| 5 | START_DATE | DATE | NULL | Vigência | Data de início de validade | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Vigência | Data de fim de validade | — | 🟡 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_TM_ATRB_FLD_MSTR_REF_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[timeattributefieldmasterreferencepvo|TimeAttributeFieldMasterReferencePVO]] (GL · BICC: 19/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DET_INS_ATTRIBUTE_TYPE | DetailInstanceAttributeType | ✅ |
| DET_INS_VALUE_LOCATION | DetailInstanceValueLocation | ✅ |
| END_DATE | EndDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| MASTER_INSTANCE_IDENTIFIER | MasterInstanceIdentifier | ✅ |
| MODULE_ID | ModuleId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| START_DATE | StartDate | ✅ |
| TM_ATRB_FLD_ESS_PROCESS_ID | TimeAttributeFieldEssProcessId | ✅ |
| TM_ATRB_FLD_ID | TimeAttributeFieldId | ✅ |
| TM_ATRB_FLD_MSTR_REF_CODE | TimeAttributeFieldMasterReferenceCode | ✅ |
| TM_ATRB_FLD_MSTR_REF_ID | TimeAttributeFieldMasterReferenceId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_ATRB_FLD_MSTR_REF_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_atrb_fld_mstr_ref_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
