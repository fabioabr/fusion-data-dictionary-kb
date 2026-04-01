---
id: DOC-HCM-095
doc_type: system-doc
title: "FF_USER_ROWS_F — Linhas de Tabelas de Usuário Fast Formula"
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
  - linhas
  - user-rows
  - lookup-keys
aliases:
  - FF_USER_ROWS_F
  - ff_user_rows_f
  - ff-user-rows-f
  - DOC-HCM-095
  - linhas-de-tabelas-de-usuário-fast-formula
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# FF_USER_ROWS_F

## 📌 Visão Geral

Armazena as **linhas** (rows) das tabelas de usuário Fast Formula. Cada linha define uma chave de busca — quando uma fórmula consulta uma tabela, usa o valor da linha como critério de match.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Chaves de busca:** Define as linhas/registros das tabelas FF.
- **Lookups parametrizáveis:** Chaves de consulta para fórmulas de cálculo.
- **Range matching:** Suporte a match por range (entre LOW e HIGH).
- **Histórico temporal:** Linhas com efetividade por data.
- **Manutenção operacional:** Adição/remoção de linhas sem alterar fórmulas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | USER_ROW_ID | NUMBER(18) | NOT NULL | PK | Identificador único da linha | — | 🟢 95% |
| 2 | USER_TABLE_ID | NUMBER(18) | NOT NULL | FK | Tabela de usuário | [[ff_user_tables_vl]] | 🟢 95% |
| 3 | ROW_LOW_RANGE_OR_NAME | VARCHAR2(240) | NOT NULL | Chave | Valor inferior do range ou nome da linha | — | 🟢 95% |
| 4 | ROW_HIGH_RANGE | VARCHAR2(240) | NULL | Chave | Valor superior do range (para match por faixa) | — | 🟢 90% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Data | Início de vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Fim de vigência | — | 🟢 95% |
| 7 | DISPLAY_SEQUENCE | NUMBER | NULL | Controle | Sequência de exibição | — | 🟡 75% |
| 8 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código de legislação | — | 🟢 90% |
| 9 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 80% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[ff_user_tables_vl]] — via `USER_TABLE_ID` (tabela de usuario da linha)

### Tabelas-filha (FK de saída)
- [[ff_user_column_instances_f]] — via `USER_ROW_ID` (valores das células)
- [[ff_user_rows_tl]] — via `USER_ROW_ID` (traducoes multilingue do registro)

---

## 📎 Uso Típico

### Linhas de uma tabela FF
```sql
SELECT r.USER_ROW_ID, r.ROW_LOW_RANGE_OR_NAME, r.ROW_HIGH_RANGE
FROM   FF_USER_ROWS_F r
WHERE  r.USER_TABLE_ID = :p_table_id
  AND  SYSDATE BETWEEN r.EFFECTIVE_START_DATE AND r.EFFECTIVE_END_DATE
ORDER BY r.DISPLAY_SEQUENCE;
```

### Busca por range
```sql
SELECT r.ROW_LOW_RANGE_OR_NAME, r.ROW_HIGH_RANGE
FROM   FF_USER_ROWS_F r
WHERE  r.USER_TABLE_ID = :p_table_id
  AND  :p_value BETWEEN r.ROW_LOW_RANGE_OR_NAME AND NVL(r.ROW_HIGH_RANGE, r.ROW_LOW_RANGE_OR_NAME);
```

---

## 🔒 Observações

- O sufixo _F indica tabela date-effective.
- Tabelas com `MATCH_TYPE = 'MATCH'` usam apenas `ROW_LOW_RANGE_OR_NAME`; com `RANGE` usam ambos os campos.
- O `DISPLAY_SEQUENCE` controla a ordem de exibição na interface.
- Linhas são versionadas por data — alterações criam novos registros efetivos.

---

## 🔗 PVOs Relacionados

### [[userrowdpvo|UserRowDPVO]] (GL · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | UserRowDPEOCreatedBy | ✅ |
| CREATION_DATE | UserRowDPEOCreationDate | ✅ |
| DISPLAY_SEQUENCE | UserRowDPEODisplaySequence | ✅ |
| EFFECTIVE_END_DATE | UserRowDPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | UserRowDPEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | UserRowDPEOEnterpriseId | ✅ |
| LAST_UPDATE_DATE | UserRowDPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | UserRowDPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | UserRowDPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | UserRowDPEOLegislationCode | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | UserRowDPEOLegislativeDataGroupId | ✅ |
| MODULE_ID | UserRowDPEOModuleId | ✅ |
| OBJECT_VERSION_NUMBER | UserRowDPEOObjectVersionNumber | ✅ |
| ROW_HIGH_RANGE | UserRowDPEORowHighRange | ✅ |
| ROW_LOW_RANGE_OR_NAME | UserRowDPEORowLowRangeOrName | ✅ |
| USER_ROW_ID | UserRowDPEOUserRowId | ✅ |
| USER_TABLE_ID | UserRowDPEOUserTableId | ✅ |

---

## 📚 Referências

- [Oracle Docs — FF_USER_ROWS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ffuserrowsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
