---
id: DOC-HCM-333
doc_type: system-doc
title: "HWM_TCD_MAPPING_SETS_B — Conjuntos de Mapeamento de Time Card (Base)"
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
  - time-card
  - mapeamentos
  - conjuntos
  - base
aliases:
  - HWM_TCD_MAPPING_SETS_B
  - hwm_tcd_mapping_sets_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCD_MAPPING_SETS_B

## 📌 Visão Geral

Tabela base que agrupa mapeamentos de cartão de ponto em conjuntos, permitindo aplicar grupos de mapeamentos a diferentes cenários de exportação.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Exportação de dados de ponto:** Configuração de como os dados do cartão de ponto são exportados para sistemas externos.
- **Mapeamento de campos:** Definição de correspondência entre campos do time card e sistemas de destino.
- **Integração com Payroll:** Transferência de horas trabalhadas para processamento de folha de pagamento.
- **Integração com Project Costing:** Alocação de horas em projetos para custeio.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TCD_MAPPING_SETS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
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
- [[hwm_tcd_mapping_set_dtls]] — via `MAPPING_SET_ID` (detalhes do conjunto de mapeamento)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_TCD_MAPPING_SETS_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Área funcional: Time Card Export dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[tcdmappingsetdetailpvo|TcdMappingSetDetailPVO]] (GL · BICC: 7/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TcdMappingSetBPEOCreatedBy | ✅ |
| CREATION_DATE | TcdMappingSetBPEOCreationDate | ✅ |
| ENTERPRISE_ID | TcdMappingSetBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TcdMappingSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TcdMappingSetBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TcdMappingSetBPEOLastUpdatedBy | ✅ |
| MODULE_ID | TcdMappingSetBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TcdMappingSetBPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | TcdMappingSetBPEOSeedDataSource | — |
| TCD_MAPPING_SET_CD | TcdMappingSetBPEOTcdMappingSetCd | ✅ |
| TCD_MAPPING_SET_ID | TcdMappingSetBPEOTcdMappingSetId | ✅ |

### [[tcdmappingsetpvo|TcdMappingSetPVO]] (GL · BICC: 7/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TcdMappingSetBPEOCreatedBy | ✅ |
| CREATION_DATE | TcdMappingSetBPEOCreationDate | ✅ |
| ENTERPRISE_ID | TcdMappingSetBPEOEnterpriseId | — |
| LAST_UPDATE_DATE | TcdMappingSetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TcdMappingSetBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TcdMappingSetBPEOLastUpdatedBy | ✅ |
| MODULE_ID | TcdMappingSetBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | TcdMappingSetBPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | TcdMappingSetBPEOSeedDataSource | — |
| TCD_MAPPING_SET_CD | TcdMappingSetBPEOTcdMappingSetCd | ✅ |
| TCD_MAPPING_SET_ID | TcdMappingSetBPEOTcdMappingSetId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TCD_MAPPING_SETS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcd_mapping_sets_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
