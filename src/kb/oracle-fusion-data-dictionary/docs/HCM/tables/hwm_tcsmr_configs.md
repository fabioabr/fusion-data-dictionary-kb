---
id: DOC-HCM-339
doc_type: system-doc
title: "HWM_TCSMR_CONFIGS — Configurações de Resumo de Time Card"
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
  - configuracoes
aliases:
  - HWM_TCSMR_CONFIGS
  - hwm_tcsmr_configs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCSMR_CONFIGS

## 📌 Visão Geral

Define as configurações utilizadas para geração de resumos de cartão de ponto, incluindo parâmetros de agregação, períodos e critérios de inclusão.



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
| 1 | CONFIG_ID | NUMBER(18) | NOT NULL | PK | Identificador da configuração | — | 🟡 80% |
| 2 | CONFIG_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código da configuração | — | 🟡 80% |
| 3 | CONFIG_VALUE | VARCHAR2(240) | NULL | Dados | Valor da configuração | — | 🟡 75% |
| 4 | CONFIG_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da configuração | — | 🟡 75% |
| 5 | ENABLED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se está habilitado (Y/N) | — | 🟡 75% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição da configuração | — | 🟡 70% |
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
SELECT t.CONFIG_CODE, t.CONFIG_VALUE, t.CONFIG_TYPE
FROM   HWM_TCSMR_CONFIGS t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Configurações impactam o comportamento do módulo; alterações requerem teste em ambiente de homologação.
- Área funcional: Time Card Summary dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TCSMR_CONFIGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcsmr_configs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
