---
id: DOC-HCM-338
doc_type: system-doc
title: "HWM_TCSMRS_VL — Resumos de Cartão de Ponto (View Consolidada)"
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
  - resumos
  - view-consolidada
aliases:
  - HWM_TCSMRS_VL
  - hwm_tcsmrs_vl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCSMRS_VL

## 📌 Visão Geral

Visão consolidada que combina dados base e traduções dos resumos de cartão de ponto para consulta simplificada.

> [!note] Sufixo _VL
> O sufixo `_VL` indica **view consolidada** que combina automaticamente a tabela `_B` (dados base) com a `_TL` (traduções) para o idioma da sessão.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Resumo consolidado:** Agregação de registros de cartão de ponto por período e trabalhador.
- **Configuração de resumos:** Definição de parâmetros de consolidação e critérios de inclusão.
- **Transferência para sistemas:** Envio de resumos consolidados para Payroll e Project Costing.
- **Monitoramento de processos:** Acompanhamento do status de transferência e processamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | TCSMRS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome traduzido do registro | — | 🟢 90% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição traduzida | — | 🟡 80% |
| 4 | CODE | VARCHAR2(30) | NULL | Classificação | Código identificador | — | 🟡 75% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 75% |
| 6 | LANGUAGE | VARCHAR2(4) | NOT NULL | Tradução | Código do idioma da tradução | — | 🟢 90% |
| 7 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Tradução | Idioma de origem da tradução | — | 🟢 90% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.NAME, t.DESCRIPTION, t.CODE
FROM   HWM_TCSMRS_VL t
WHERE  t.LANGUAGE = USERENV('LANG')
```

### Filtros comuns
- `LANGUAGE = USERENV('LANG')` — Tradução no idioma da sessão
- `LANGUAGE = 'PTB'` — Tradução em português brasileiro

---

## 🔒 Observações

- View consolidada: combina automaticamente dados base (`_B`) e traduções (`_TL`). Preferir em consultas de leitura.
- Área funcional: Time Card Summary dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[timeattributefieldallocationpvo|TimeAttributeFieldAllocationPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | TimeConsumerVLPEOName | — |
| TCSMRS_CODE | TimeConsumerVLPEOTcsmrsCode | — |
| TCSMRS_ID | TimeConsumerVLPEOTcsmrsId | — |

### [[timeattributefieldcomponentpvo|TimeAttributeFieldComponentPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | TimeConsumerVLPEOName | — |
| TCSMRS_CODE | TimeConsumerVLPEOTcsmrsCode | — |
| TCSMRS_ID | TimeConsumerVLPEOTcsmrsId | — |

### [[timeattributefieldcustompvo|TimeAttributeFieldCustomPVO]] (GL · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | TimeConsumerVLPEOName | ✅ |
| TCSMRS_CODE | TimeConsumerVLPEOTcsmrsCode | ✅ |
| TCSMRS_ID | TimeConsumerVLPEOTcsmrsId | — |

### [[timeattributefieldpvo|TimeAttributeFieldPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | TimeConsumerVLPEOName | — |
| TCSMRS_CODE | TimeConsumerVLPEOTcsmrsCode | — |
| TCSMRS_ID | TimeConsumerVLPEOTcsmrsId | — |

### [[timeconsumerconfigurationpvo|TimeConsumerConfigurationPVO]] (GL · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| NAME | TimeConsumerVLPEOName | ✅ |
| TCSMRS_CODE | TimeConsumerVLPEOTcsmrsCode | ✅ |
| TCSMRS_ID | TimeConsumerVLPEOTcsmrsId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TCSMRS_VL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcsmrs_vl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
