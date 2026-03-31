---
id: DOC-HCM-094
doc_type: system-doc
title: "FF_USER_COLUMN_INSTANCES_F — Instâncias de Valores de Colunas FF"
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
  - fast-formula
  - valores
  - column-instances
  - lookup-data
aliases:
  - FF_USER_COLUMN_INSTANCES_F
  - ff_user_column_instances_f
  - ff-user-column-instances-f
  - DOC-HCM-094
  - instâncias-de-valores-de-colunas-ff
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# FF_USER_COLUMN_INSTANCES_F

## 📌 Visão Geral

Armazena as **instâncias de valores** para cada combinação de coluna e linha em tabelas de usuário Fast Formula. É a tabela de dados efetivos — contém os valores consultados pelas fórmulas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Armazenamento de valores:** Dados de referência consultados por fórmulas.
- **Configuração de parâmetros:** Valores parametrizáveis sem alterar código.
- **Histórico de valores:** Registro com efetividade temporal de cada valor.
- **Processamento de folha:** Valores consultados durante cálculo de payroll.
- **Manutenção operacional:** Alteração de valores sem recompilação de fórmulas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_COLUMN_INSTANCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da instância | — | 🟢 95% |
| 2 | USER_COLUMN_ID | NUMBER(18) | NOT NULL | FK | Coluna de referência | [[ff_user_columns_vl]] | 🟢 95% |
| 3 | USER_ROW_ID | NUMBER(18) | NOT NULL | FK | Linha de referência | [[ff_user_rows_f]] | 🟢 95% |
| 4 | VALUE | VARCHAR2(240) | NULL | Dados | Valor armazenado | — | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Data | Início de vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Fim de vigência | — | 🟢 95% |
| 7 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código de legislação | — | 🟢 90% |
| 8 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ff_user_columns_vl]] — via `USER_COLUMN_ID` (coluna da tabela do usuario)
- [[ff_user_rows_f]] — via `USER_ROW_ID` (linha da tabela do usuario)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo empresarial da instancia de coluna)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Valor por coluna e linha
```sql
SELECT ci.VALUE, ci.EFFECTIVE_START_DATE, ci.EFFECTIVE_END_DATE
FROM   FF_USER_COLUMN_INSTANCES_F ci
WHERE  ci.USER_COLUMN_ID = :p_column_id
  AND  ci.USER_ROW_ID = :p_row_id
  AND  SYSDATE BETWEEN ci.EFFECTIVE_START_DATE AND ci.EFFECTIVE_END_DATE;
```

### Todos os valores de uma coluna
```sql
SELECT r.ROW_LOW_RANGE_OR_NAME, ci.VALUE
FROM   FF_USER_COLUMN_INSTANCES_F ci
JOIN   FF_USER_ROWS_F r ON ci.USER_ROW_ID = r.USER_ROW_ID
WHERE  ci.USER_COLUMN_ID = :p_column_id
  AND  SYSDATE BETWEEN ci.EFFECTIVE_START_DATE AND ci.EFFECTIVE_END_DATE;
```

---

## 🔒 Observações

- O sufixo _F indica tabela date-effective (com `EFFECTIVE_START_DATE` / `EFFECTIVE_END_DATE`).
- A combinação `USER_COLUMN_ID` + `USER_ROW_ID` + datas define cada célula da tabela.
- O campo `VALUE` é sempre VARCHAR2 — conversão de tipo é feita pela fórmula consumidora.
- Mudanças de valor são versionadas por data — o registro anterior recebe `EFFECTIVE_END_DATE`.

---

## 🔗 PVOs Relacionados

### [[usercolumninstancedpvo|UserColumnInstanceDPVO]] (GL · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UserColumnInstanceDPEOCreatedBy | ✅ |
| CREATION_DATE | UserColumnInstanceDPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | UserColumnInstanceDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | UserColumnInstanceDPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | UserColumnInstanceDPEOEnterpriseId | ✅ |
| LAST_UPDATE_DATE | UserColumnInstanceDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserColumnInstanceDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | UserColumnInstanceDPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | UserColumnInstanceDPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | UserColumnInstanceDPEOLegislativeDataGroupId | ✅ |
| MODULE_ID | UserColumnInstanceDPEOModuleId | ✅ |
| OBJECT_VERSION_NUMBER | UserColumnInstanceDPEOObjectVersionNumber | ✅ |
| USER_COLUMN_ID | UserColumnInstanceDPEOUserColumnId | ✅ |
| USER_COLUMN_INSTANCE_ID | UserColumnInstanceDPEOUserColumnInstanceId | ✅ |
| USER_ROW_ID | UserColumnInstanceDPEOUserRowId | ✅ |
| VALUE | UserColumnInstanceDPEOValue | ✅ |

---

## 📚 Referências

- [Oracle Docs — FF_USER_COLUMN_INSTANCES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ffusercolumninstancesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
