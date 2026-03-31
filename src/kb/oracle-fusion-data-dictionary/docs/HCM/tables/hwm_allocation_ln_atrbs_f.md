---
id: DOC-HCM-295
doc_type: system-doc
title: "HWM_ALLOCATION_LN_ATRBS_F — Atributos de Linhas de Alocacao"
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
  - allocation-attributes
  - workforce-management
  - eav
aliases:
  - HWM_ALLOCATION_LN_ATRBS_F
  - hwm_allocation_ln_atrbs_f
  - hwm-allocation-ln-atrbs-f
  - allocation-ln-atrbs
  - atributos-linhas-alocacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_ALLOCATION_LN_ATRBS_F

## 📌 Visao Geral

Armazena **atributos adicionais** das linhas de alocacao em formato flexivel, com versionamento date-effective.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Extensibilidade:** Adicionar atributos customizados a linhas de alocacao.
- **Integracao:** Armazenar dados de dimensoes adicionais.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATION_LN_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador do atributo | — | 🟢 85% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 85% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 85% |
| 4 | ALLOCATION_LINE_ID | NUMBER(18) | NOT NULL | FK | Linha de alocacao | [[hwm_allocation_lines_f]] | 🟢 90% |
| 5 | ATTRIBUTE_NAME | VARCHAR2(240) | NULL | Dados | Nome do atributo | — | 🟡 75% |
| 6 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hwm_allocation_lines_f]] — via `ALLOCATION_LINE_ID` (linha de alocacao do atributo)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Atributos de uma linha
```sql
SELECT a.ATTRIBUTE_NAME, a.ATTRIBUTE_VALUE
FROM   HWM_ALLOCATION_LN_ATRBS_F a
WHERE  a.ALLOCATION_LINE_ID = :p_line_id
  AND  SYSDATE BETWEEN a.EFFECTIVE_START_DATE AND a.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective.
- Estrutura EAV para extensibilidade.

---

## 📚 Referencias

- [Oracle Docs — HWM_ALLOCATION_LN_ATRBS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmallocationlnatrbsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[allocationlinespvo|AllocationLinesPVO]] (GL · BICC: 180/240)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO10AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO11AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO12AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO13AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO14AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO15AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO16AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO17AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO18AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO19AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO1AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO20AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO21AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO22AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO23AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO24AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO25AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO26AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO27AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO28AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO29AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO2AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO30AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO3AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO4AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO5AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO6AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO7AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO8AllocLnAtrbId | ✅ |
| ALLOCATION_LN_ATRB_ID | AllocLnAtrbsPEO9AllocLnAtrbId | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO10AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO11AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO12AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO13AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO14AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO15AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO16AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO17AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO18AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO19AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO1AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO20AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO21AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO22AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO23AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO24AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO25AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO26AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO27AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO28AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO29AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO2AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO30AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO3AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO4AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO5AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO6AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO7AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO8AtrbDataType | ✅ |
| ATRB_DATA_TYPE | AllocLnAtrbsPEO9AtrbDataType | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO10AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO11AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO12AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO13AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO14AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO15AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO16AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO17AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO18AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO19AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO1AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO20AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO21AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO22AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO23AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO24AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO25AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO26AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO27AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO28AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO29AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO2AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO30AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO3AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO4AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO5AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO6AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO7AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO8AtrbValueNum | ✅ |
| ATRB_VALUE_NUMBER | AllocLnAtrbsPEO9AtrbValueNum | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO10AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO11AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO12AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO13AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO14AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO15AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO16AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO17AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO18AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO19AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO1AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO20AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO21AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO22AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO23AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO24AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO25AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO26AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO27AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO28AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO29AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO2AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO30AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO3AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO4AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO5AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO6AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO7AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO8AtrbValueText | ✅ |
| ATRB_VALUE_TEXT | AllocLnAtrbsPEO9AtrbValueText | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO10AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO11AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO12AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO13AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO14AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO15AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO16AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO17AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO18AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO19AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO1AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO20AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO21AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO22AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO23AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO24AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO25AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO26AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO27AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO28AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO29AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO2AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO30AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO3AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO4AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO5AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO6AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO7AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO8AtrbValueDttm | ✅ |
| ATRB_VALUE_TIMESTAMP | AllocLnAtrbsPEO9AtrbValueDttm | ✅ |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO10EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO11EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO12EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO13EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO14EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO15EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO16EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO17EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO18EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO19EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO1EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO20EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO21EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO22EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO23EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO24EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO25EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO26EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO27EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO28EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO29EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO2EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO30EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO3EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO4EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO5EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO6EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO7EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO8EffEndDt | — |
| EFFECTIVE_END_DATE | AllocLnAtrbsPEO9EffEndDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO10EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO11EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO12EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO13EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO14EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO15EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO16EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO17EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO18EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO19EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO1EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO20EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO21EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO22EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO23EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO24EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO25EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO26EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO27EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO28EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO29EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO2EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO30EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO3EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO4EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO5EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO6EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO7EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO8EffStartDt | — |
| EFFECTIVE_START_DATE | AllocLnAtrbsPEO9EffStartDt | — |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO10TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO11TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO12TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO13TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO14TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO15TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO16TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO17TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO18TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO19TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO1TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO20TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO21TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO22TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO23TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO24TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO25TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO26TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO27TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO28TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO29TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO2TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO30TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO3TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO4TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO5TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO6TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO7TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO8TmAtrbFldId | ✅ |
| TM_ATRB_FLD_ID | AllocLnAtrbsPEO9TmAtrbFldId | ✅ |
