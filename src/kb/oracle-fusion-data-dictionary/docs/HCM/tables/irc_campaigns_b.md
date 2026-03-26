---
id: DOC-HCM-447
doc_type: system-doc
title: "IRC_CAMPAIGNS_B — Campanhas de Recrutamento (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - irc
  - campanha
  - recruitment-campaign
  - base
aliases:
  - IRC_CAMPAIGNS_B
  - irc_campaigns_b
  - irc-campaigns-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMPAIGNS_B

## 📌 Visao Geral

Tabela base que armazena as **campanhas de recrutamento** do modulo Recruiting (IRC). Cada campanha representa uma iniciativa de marketing de recrutamento para atrair candidatos.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Marketing de recrutamento:** gerencia campanhas para atrair candidatos.
- **Employer branding:** suporta iniciativas de marca empregadora.
- **Metricas de sourcing:** rastreia eficacia de campanhas por canal.
- **Gestao de custos:** controla orcamento de campanhas de recrutamento.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | PK | Identificador da campanha | — | 🟡 70% |
| 2 | CAMPAIGN_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo da campanha | — | 🟡 65% |
| 3 | CAMPAIGN_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da campanha | — | 🟡 60% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da campanha | — | 🟡 65% |
| 5 | START_DATE | DATE | NULL | Periodo | Data de inicio | — | 🟡 65% |
| 6 | END_DATE | DATE | NULL | Periodo | Data de termino | — | 🟡 60% |
| 7 | BUDGET_AMOUNT | NUMBER | NULL | Dados | Orcamento da campanha | — | 🟡 50% |
| 8 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[irc_campaigns_tl]] — via `CAMPAIGN_ID` (traducoes)
- [[irc_camp_assets_b]] — via `CAMPAIGN_ID` (ativos da campanha)

---

## 📎 Uso Tipico

### Campanhas de recrutamento ativas
```sql
SELECT c.CAMPAIGN_ID, c.CAMPAIGN_CODE, c.CAMPAIGN_TYPE,
       c.STATUS, c.START_DATE, c.END_DATE
FROM   IRC_CAMPAIGNS_B c
WHERE  c.STATUS = 'ACTIVE'
  AND  c.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `STATUS = 'ACTIVE' — Campanhas ativas`
- `CAMPAIGN_TYPE = :p_type — Por tipo`
- `START_DATE >= :dt_ini — A partir de uma data`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em IRC_CAMPAIGNS_TL.
- Campanhas organizam acoes de marketing de recrutamento.
- Podem estar associadas a requisicoes especificas ou ser genericas.

---

## 📚 Referencias

- [Oracle Docs — IRC_CAMPAIGNS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampaignsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
