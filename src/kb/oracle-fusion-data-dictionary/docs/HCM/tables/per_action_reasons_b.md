---
id: DOC-HCM-613
doc_type: system-doc
title: "PER_ACTION_REASONS_B — Motivos de Ações de RH (Base)"
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
  - workforce-management
  - motivos-acoes
  - action-reasons
aliases:
  - PER_ACTION_REASONS_B
  - per_action_reasons_b
  - per-action-reasons-b
  - motivos-de-ações-de-rh-(base)
  - per-action-reasons-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_REASONS_B

## 📌 Visão Geral

Armazena a definição dos **motivos (razões)** que podem ser associados às ações de RH. Permite detalhar por que uma ação foi realizada (ex.: promoção por desempenho, desligamento por justa causa).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detalhamento de motivos** — especifica a razão de cada ação de RH.
- **Análise de turnover** — classificação de motivos de desligamento.
- **Compliance** — rastreabilidade de motivos para auditorias.
- **Relatórios gerenciais** — segmentação de ações por motivo.
- **Políticas de RH** — motivos diferentes podem acionar regras distintas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_REASON_ID | NUMBER(18) | NOT NULL | PK | Identificador único do motivo de ação | — | 🟢 95% |
| 2 | ACTION_REASON_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do motivo | — | 🟢 90% |
| 3 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se o motivo está ativo (Y/N) | — | 🟢 85% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de configuração de motivos de ação.

### Tabelas-filha (FK de saída)
- [[per_action_reasons_tl]] — via `ACTION_REASON_ID` (traduÃ§Ãµes do motivo de aÃ§Ã£o de RH)
- [[per_action_reason_usages]] — via `ACTION_REASON_ID` (associaÃ§Ãµes de uso do motivo de aÃ§Ã£o)
- [[per_action_occurrences]] — via `ACTION_REASON_ID` (ocorrências que usam este motivo)

---

## 📎 Uso Típico

### Motivos de ação ativos
```sql
SELECT par.ACTION_REASON_ID, par.ACTION_REASON_CODE, par.ACTIVE_STATUS
FROM   PER_ACTION_REASONS_B par
WHERE  par.ACTIVE_STATUS = 'Y';
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Motivos ativos
- `ACTION_REASON_CODE LIKE 'TERM%'` — Motivos de desligamento
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Motivos são reutilizáveis — um motivo pode ser associado a múltiplas ações via PER_ACTION_REASON_USAGES.
- A análise de motivos de desligamento é crítica para estratégias de retenção.
---

## 📚 Referências

- [Oracle Docs — PER_ACTION_REASONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionreasonsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
