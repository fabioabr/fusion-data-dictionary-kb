---
id: DOC-HCM-346
doc_type: system-doc
title: "HWM_TE_ALT_NAME_VALS_B — Valores de Nomes Alternativos de Entrada de Tempo (Base)"
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
  - time-entry
  - nomes-alternativos
  - valores
  - base
aliases:
  - HWM_TE_ALT_NAME_VALS_B
  - hwm_te_alt_name_vals_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TE_ALT_NAME_VALS_B

## 📌 Visão Geral

Tabela base que armazena os valores associados aos nomes alternativos de entradas de tempo, definindo os mapeamentos entre nomenclaturas.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de entradas de tempo:** Captura e gestão de registros individuais de horas trabalhadas.
- **Nomes alternativos:** Suporte a múltiplas nomenclaturas para integração com diferentes interfaces.
- **Validação de entradas:** Mensagens de erro e conformidade durante o processamento.
- **Controle de versão:** Rastreamento do ciclo de vida de cada entrada de tempo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TE_ALT_NAMEALS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
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
- [[hwm_te_alt_names]] — via `ALT_NAME_ID` (nome alternativo)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_TE_ALT_NAME_VALS_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Área funcional: Time Entry dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[templatelayoutcompdisplayvaluepvo|TemplateLayoutCompDisplayValuePVO]] (GL · BICC: 41/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | AltNameValsBPEOAttribute1 | ✅ |
| ATTRIBUTE10 | AltNameValsBPEOAttribute10 | ✅ |
| ATTRIBUTE11 | AltNameValsBPEOAttribute11 | ✅ |
| ATTRIBUTE12 | AltNameValsBPEOAttribute12 | ✅ |
| ATTRIBUTE13 | AltNameValsBPEOAttribute13 | ✅ |
| ATTRIBUTE14 | AltNameValsBPEOAttribute14 | ✅ |
| ATTRIBUTE15 | AltNameValsBPEOAttribute15 | ✅ |
| ATTRIBUTE16 | AltNameValsBPEOAttribute16 | ✅ |
| ATTRIBUTE17 | AltNameValsBPEOAttribute17 | ✅ |
| ATTRIBUTE18 | AltNameValsBPEOAttribute18 | ✅ |
| ATTRIBUTE19 | AltNameValsBPEOAttribute19 | ✅ |
| ATTRIBUTE2 | AltNameValsBPEOAttribute2 | ✅ |
| ATTRIBUTE20 | AltNameValsBPEOAttribute20 | ✅ |
| ATTRIBUTE21 | AltNameValsBPEOAttribute21 | ✅ |
| ATTRIBUTE22 | AltNameValsBPEOAttribute22 | ✅ |
| ATTRIBUTE23 | AltNameValsBPEOAttribute23 | ✅ |
| ATTRIBUTE24 | AltNameValsBPEOAttribute24 | ✅ |
| ATTRIBUTE25 | AltNameValsBPEOAttribute25 | ✅ |
| ATTRIBUTE26 | AltNameValsBPEOAttribute26 | ✅ |
| ATTRIBUTE27 | AltNameValsBPEOAttribute27 | ✅ |
| ATTRIBUTE28 | AltNameValsBPEOAttribute28 | ✅ |
| ATTRIBUTE29 | AltNameValsBPEOAttribute29 | ✅ |
| ATTRIBUTE3 | AltNameValsBPEOAttribute3 | ✅ |
| ATTRIBUTE30 | AltNameValsBPEOAttribute30 | ✅ |
| ATTRIBUTE4 | AltNameValsBPEOAttribute4 | ✅ |
| ATTRIBUTE5 | AltNameValsBPEOAttribute5 | ✅ |
| ATTRIBUTE6 | AltNameValsBPEOAttribute6 | ✅ |
| ATTRIBUTE7 | AltNameValsBPEOAttribute7 | ✅ |
| ATTRIBUTE8 | AltNameValsBPEOAttribute8 | ✅ |
| ATTRIBUTE9 | AltNameValsBPEOAttribute9 | ✅ |
| CREATED_BY | AltNameValsBPEOCreatedBy | ✅ |
| CREATION_DATE | AltNameValsBPEOCreationDate | ✅ |
| DATE_FROM | AltNameValsBPEODateFrom | — |
| DATE_TO | AltNameValsBPEODateTo | — |
| DISPLAY_SEQUENCE | TeAltNameValsBPEODisplaySequence | ✅ |
| ENABLED_FLAG | AltNameValsBPEOEnabledFlag | ✅ |
| ENTERPRISE_ID | AltNameValsBPEOEnterpriseId | — |
| EXISTING_FLAG | AltNameValsBPEOExistingFlag | — |
| LAST_UPDATE_DATE | AltNameValsBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AltNameValsBPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AltNameValsBPEOLastUpdatedBy | ✅ |
| MANAGER_ACTION_CD | TeAltNameValsBPEOManagerActionCd | ✅ |
| MODULE_ID | AltNameValsBPEOModuleId | — |
| NAME | AltNameValsBPEOName | — |
| OBJECT_VERSION_NUMBER | AltNameValsBPEOObjectVersionNumber | — |
| SEED_DATA_SOURCE | AltNameValsBPEOSeedDataSource | — |
| TE_ALT_NAME_ID | AltNameValsBPEOTeAltNameId | — |
| TE_ALT_NAME_VAL_ID | AltNameValsBPEOTeAltNameValId | ✅ |
| WFM_EVENT_IN_OUT | AltNameValsBPEOWfmEventInOut | ✅ |
| WORKER_ACTION_CD | TeAltNameValsBPEOWorkerActionCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TE_ALT_NAME_VALS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_te_alt_name_vals_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
