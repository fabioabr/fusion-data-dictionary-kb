---
id: DOC-HCM-315
doc_type: system-doc
title: "HWM_RULE_SETS_F — Conjuntos de Regras (Date-Effective)"
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
  - regras
  - conjuntos
  - date-effective
aliases:
  - HWM_RULE_SETS_F
  - hwm_rule_sets_f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_RULE_SETS_F

## 📌 Visão Geral

Tabela date-effective que agrupa regras relacionadas em conjuntos para aplicação coordenada. Permite versionamento temporal dos conjuntos de regras.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.


---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Motor de regras:** Definição e execução de regras de cálculo para processamento de tempo e ausências.
- **Configuração flexível:** Permite criação de regras customizadas sem desenvolvimento.
- **Reutilização:** Templates e conjuntos de regras promovem padronização e reuso.
- **Auditoria de cálculos:** Rastreamento de quais regras foram aplicadas em cada processamento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|----------|
| 1 | RULE_SETS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | NAME | VARCHAR2(240) | NULL | Identificação | Nome descritivo do registro | — | 🟡 80% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status do registro | — | 🟡 75% |
| 6 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)
- [[hwm_rule_set_mbrs]] — via `RULE_SET_ID` (membros do conjunto)

---

## 📎 Uso Típico

### Consulta padrão
```sql
SELECT t.*
FROM   HWM_RULE_SETS_F t
WHERE  SYSDATE BETWEEN t.EFFECTIVE_START_DATE AND t.EFFECTIVE_END_DATE
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
- `STATUS = 'A'` — Registros ativos

---

## 🔒 Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- Área funcional: Rules Engine dentro do Oracle Fusion Cloud HCM.

---

## 📚 Referências

- [Oracle Docs — HWM_RULE_SETS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwm_rule_sets_f.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
