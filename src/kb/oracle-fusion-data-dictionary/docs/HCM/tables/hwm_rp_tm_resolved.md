---
id: DOC-HCM-311
doc_type: system-doc
title: "HWM_RP_TM_RESOLVED — Períodos de Tempo Resolvidos"
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
  - periodos
  - resolucao
  - reporting
aliases:
  - HWM_RP_TM_RESOLVED
  - hwm_rp_tm_resolved
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RP_TM_RESOLVED

## 📌 Visão Geral

Armazena os períodos de tempo já resolvidos/calculados para relatórios, contendo os valores finais após aplicação de regras de cálculo temporal.



---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição de períodos de reporting:** Configuração dos períodos temporais para geração de relatórios de workforce.
- **Análise temporal:** Base para consolidação de dados por período (semanal, quinzenal, mensal).
- **Integração com calendários:** Alinhamento dos períodos de reporte com calendários organizacionais.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | RP_TM_RESOLVED_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟡 80% |
| 2 | CODE | VARCHAR2(30) | NULL | Identificação | Código identificador | — | 🟡 75% |
| 3 | NAME | VARCHAR2(240) | NULL | Identificação | Nome descritivo | — | 🟡 75% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 70% |
| 5 | TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do registro | — | 🟡 70% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Identificação | Descrição do registro | — | 🟡 65% |
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
SELECT t.*
FROM   HWM_RP_TM_RESOLVED t
WHERE  ROWNUM <= 100
```

### Filtros comuns
- Aplicar filtros de negócio conforme contexto de uso

---

## 🔒 Observações

- Área funcional: Time and Reporting dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_RP_TM_RESOLVED](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rp_tm_resolved.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
