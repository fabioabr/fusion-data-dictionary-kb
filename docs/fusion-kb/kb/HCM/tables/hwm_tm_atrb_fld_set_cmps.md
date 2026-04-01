---
id: DOC-HCM-360
doc_type: system-doc
title: "HWM_TM_ATRB_FLD_SET_CMPS — Componentes de Conjunto de Campos de Atributos"
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
  - conjuntos
  - componentes
aliases:
  - HWM_TM_ATRB_FLD_SET_CMPS
  - hwm_tm_atrb_fld_set_cmps
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_ATRB_FLD_SET_CMPS

## 📌 Visão Geral

Define os componentes que compõem conjuntos de campos de atributos de Time Management, estabelecendo quais campos fazem parte de cada conjunto configurado.

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
| 1 | FLD_SET_CMP_ID | NUMBER(18) | NOT NULL | PK | Identificador do componente de conjunto | — | 🟡 80% |
| 2 | FLD_SET_ID | NUMBER(18) | NOT NULL | FK | Referência ao conjunto de campos | — | 🟡 80% |
| 3 | ATRB_FLD_ID | NUMBER(18) | NOT NULL | FK | Referência ao campo de atributo | HWM_TM_ATRB_FLDS_B | 🟡 80% |
| 4 | SEQUENCE_NUMBER | NUMBER(9) | NULL | Controle | Ordem do campo no conjunto | — | 🟡 75% |
| 5 | REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o campo é obrigatório (Y/N) | — | 🟡 70% |
| 6 | DISPLAY_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o campo é visível (Y/N) | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.ATRB_FLD_ID, t.SEQUENCE_NUMBER, t.REQUIRED_FLAG, t.DISPLAY_FLAG
FROM   HWM_TM_ATRB_FLD_SET_CMPS t
WHERE  t.FLD_SET_ID = :p_fld_set_id
ORDER BY t.SEQUENCE_NUMBER
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Time Management dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[templatelayoutcompdisplayvaluepvo|TemplateLayoutCompDisplayValuePVO]] (GL · BICC: 117/150)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO10DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO11DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO12DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO13DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO14DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO15DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO16DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO17DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO18DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO19DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO1DSUsgId | — |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO20DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO21DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO22DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO23DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO24DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO25DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO26DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO27DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO28DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO29DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO2DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO30DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO3DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO4DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO5DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO6DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO7DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO8DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO9DSUsgId | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO10ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO11ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO12ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO13ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO14ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO15ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO16ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO17ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO18ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO19ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO1ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO20ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO21ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO22ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO23ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO24ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO25ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO26ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO27ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO28ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO29ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO2ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO30ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO3ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO4ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO5ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO6ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO7ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO8ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO9ReqFlag | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO10TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO11TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO12TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO13TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO14TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO15TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO16TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO17TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO18TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO19TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO1TAFldId | — |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO20TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO21TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO22TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO23TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO24TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO25TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO26TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO27TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO28TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO29TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO2TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO30TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO3TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO4TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO5TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO6TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO7TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO8TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO9TAFldId | ✅ |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO10CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO11CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO12CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO13CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO14CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO15CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO16CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO17CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO18CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO19CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO1CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO20CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO21CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO22CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO23CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO24CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO25CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO26CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO27CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO28CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO29CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO2CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO30CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO3CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO4CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO5CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO6CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO7CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO8CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO9CmpId | — |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO10UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO11UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO12UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO13UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO14UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO15UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO16UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO17UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO18UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO19UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO1UDSUsgId | — |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO20UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO21UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO22UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO23UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO24UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO25UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO26UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO27UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO28UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO29UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO2UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO30UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO3UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO4UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO5UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO6UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO7UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO8UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO9UDSUsgId | ✅ |

### [[templatelayoutcomponentpvo|TemplateLayoutComponentPVO]] (GL · BICC: 117/150)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO10DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO11DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO12DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO13DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO14DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO15DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO16DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO17DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO18DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO19DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO1DSUsgId | — |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO20DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO21DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO22DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO23DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO24DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO25DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO26DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO27DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO28DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO29DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO2DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO30DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO3DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO4DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO5DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO6DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO7DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO8DSUsgId | ✅ |
| DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO9DSUsgId | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO10ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO11ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO12ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO13ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO14ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO15ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO16ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO17ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO18ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO19ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO1ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO20ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO21ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO22ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO23ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO24ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO25ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO26ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO27ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO28ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO29ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO2ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO30ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO3ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO4ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO5ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO6ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO7ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO8ReqFlag | ✅ |
| REQUIRED_FLAG | TmAtrbFldSetCmpsPEO9ReqFlag | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO10TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO11TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO12TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO13TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO14TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO15TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO16TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO17TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO18TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO19TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO1TAFldId | — |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO20TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO21TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO22TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO23TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO24TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO25TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO26TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO27TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO28TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO29TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO2TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO30TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO3TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO4TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO5TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO6TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO7TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO8TAFldId | ✅ |
| TM_ATRB_FLD_ID | TmAtrbFldSetCmpsPEO9TAFldId | ✅ |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO10CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO11CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO12CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO13CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO14CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO15CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO16CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO17CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO18CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO19CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO1CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO20CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO21CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO22CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO23CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO24CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO25CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO26CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO27CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO28CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO29CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO2CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO30CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO3CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO4CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO5CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO6CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO7CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO8CmpId | — |
| TM_ATRB_FLD_SET_CMP_ID | TmAtrbFldSetCmpsPEO9CmpId | — |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO10UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO11UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO12UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO13UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO14UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO15UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO16UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO17UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO18UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO19UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO1UDSUsgId | — |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO20UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO21UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO22UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO23UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO24UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO25UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO26UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO27UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO28UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO29UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO2UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO30UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO3UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO4UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO5UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO6UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO7UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO8UDSUsgId | ✅ |
| USER_DATA_SOURCE_USAGE_ID | TmAtrbFldSetCmpsPEO9UDSUsgId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_ATRB_FLD_SET_CMPS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tm_atrb_fld_set_cmps.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
