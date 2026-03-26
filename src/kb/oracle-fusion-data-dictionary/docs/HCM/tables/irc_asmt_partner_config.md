---
id: DOC-HCM-440
doc_type: system-doc
title: "IRC_ASMT_PARTNER_CONFIG — Configuracao de Parceiros de Avaliacao"
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
  - assessment
  - parceiro-avaliacao
  - configuracao
aliases:
  - IRC_ASMT_PARTNER_CONFIG
  - irc_asmt_partner_config
  - irc-asmt-partner-config
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ASMT_PARTNER_CONFIG

## 📌 Visao Geral

Armazena a **configuracao de parceiros de avaliacao** (assessment partners) do modulo Recruiting (IRC). Define os parametros de integracao com fornecedores externos de testes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Integracao com parceiros:** configura conexao com fornecedores de avaliacao.
- **Parametrizacao:** define credenciais, URLs e opcoes de integracao.
- **Gestao de fornecedores:** centraliza configuracao de parceiros de assessment.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PARTNER_CONFIG_ID | NUMBER(18) | NOT NULL | PK | Identificador da configuracao | — | 🟡 70% |
| 2 | PARTNER_CODE | VARCHAR2(80) | NOT NULL | Identificacao | Codigo do parceiro | — | 🟡 65% |
| 3 | PARTNER_NAME | VARCHAR2(240) | NULL | Identificacao | Nome do parceiro | — | 🟡 60% |
| 4 | INTEGRATION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de integracao | — | 🟡 55% |
| 5 | SERVICE_URL | VARCHAR2(2000) | NULL | Dados | URL do servico de avaliacao | — | 🟡 55% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- [[irc_asmt_req_config]] — via `PARTNER_CONFIG_ID` (config por requisicao)

---

## 📎 Uso Tipico

### Parceiros de avaliacao configurados
```sql
SELECT pc.PARTNER_CODE, pc.PARTNER_NAME,
       pc.INTEGRATION_TYPE, pc.ENABLED_FLAG
FROM   IRC_ASMT_PARTNER_CONFIG pc
WHERE  pc.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Parceiros ativos`
- `PARTNER_CODE = :p_code — Por codigo`

---

## 🔒 Observacoes

- Contem configuracao de integracao com fornecedores de avaliacao externos.
- Dados sensiveis como credenciais podem estar ofuscados.
- Alteracoes podem impactar o fluxo de assessment do recrutamento.

---

## 📚 Referencias

- [Oracle Docs — IRC_ASMT_PARTNER_CONFIG](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircasmtpartnerconfig.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
