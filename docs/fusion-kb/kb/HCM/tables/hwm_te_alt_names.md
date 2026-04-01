---
id: DOC-HCM-345
doc_type: system-doc
title: "HWM_TE_ALT_NAMES — Nomes Alternativos de Entrada de Tempo"
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
aliases:
  - HWM_TE_ALT_NAMES
  - hwm_te_alt_names
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TE_ALT_NAMES

## 📌 Visão Geral

Armazena nomes alternativos para entradas de tempo (time entries), permitindo que diferentes sistemas ou interfaces referenciem a mesma entrada por nomes distintos.

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
| 1 | ALT_NAME_ID | NUMBER(18) | NOT NULL | PK | Identificador do nome alternativo | — | 🟡 80% |
| 2 | ALT_NAME_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do nome alternativo | — | 🟡 80% |
| 3 | ALT_NAME_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do nome alternativo | — | 🟡 75% |
| 4 | CONTEXT_TYPE | VARCHAR2(30) | NULL | Classificação | Contexto de uso do nome | — | 🟡 70% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 70% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[hwm_te_alt_name_vals_b]] — via `ALT_NAME_ID` (valores dos nomes alternativos de tempo)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.ALT_NAME_CODE, t.ALT_NAME_TYPE, t.STATUS
FROM   HWM_TE_ALT_NAMES t
WHERE  NVL(t.STATUS, 'A') = 'A'
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Time Entry dentro do Oracle Fusion Cloud HCM.

---

## 🔗 PVOs Relacionados

### [[templatelayoutcompdisplayvaluepvo|TemplateLayoutCompDisplayValuePVO]] (GL · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TeAltNamesPEODescription | ✅ |
| NAME | TeAltNamesPEOName | ✅ |
| TE_ALT_NAME_ID | TeAltNamesPEOTeAltNameId | ✅ |

### [[templatelayoutcomponentpvo|TemplateLayoutComponentPVO]] (GL · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TeAltNamesPEODescription | ✅ |
| NAME | TeAltNamesPEOName | ✅ |
| TE_ALT_NAME_ID | TeAltNamesPEOTeAltNameId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TE_ALT_NAMES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_te_alt_names.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
