---
id: DOC-HCM-340
doc_type: system-doc
title: "HWM_TCSMR_CONFIG_SETS_B — Conjuntos de Configuração de Resumo (Base)"
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
  - conjuntos
  - base
aliases:
  - HWM_TCSMR_CONFIG_SETS_B
  - hwm_tcsmr_config_sets_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TCSMR_CONFIG_SETS_B

## 📌 Visão Geral

Tabela base que agrupa configurações de resumo de cartão de ponto em conjuntos para aplicação coordenada a grupos de trabalhadores.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados não traduzíveis. A tabela correspondente `_TL` armazena as traduções.


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
| 1 | TCSMR_CONFIG_SETS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
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
- Nenhum relacionamento de saída identificado

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.CODE, t.STATUS, t.START_DATE, t.END_DATE
FROM   HWM_TCSMR_CONFIG_SETS_B t
WHERE  NVL(t.ENABLED_FLAG, 'Y') = 'Y'
```

### Filtros comuns
- `NVL(ENABLED_FLAG, 'Y') = 'Y'` — Registros habilitados
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela base: contém dados não traduzíveis. Utilize a view `_VL` correspondente para consultas com tradução.
- Configurações impactam o comportamento do módulo; alterações requerem teste em ambiente de homologação.
- Área funcional: Time Card Summary dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_TCSMR_CONFIG_SETS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_tcsmr_config_sets_b.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
