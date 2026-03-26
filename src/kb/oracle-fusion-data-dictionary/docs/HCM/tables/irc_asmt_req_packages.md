---
id: DOC-HCM-442
doc_type: system-doc
title: "IRC_ASMT_REQ_PACKAGES — Pacotes de Avaliacao por Requisicao"
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
  - pacote-requisicao
aliases:
  - IRC_ASMT_REQ_PACKAGES
  - irc_asmt_req_packages
  - irc-asmt-req-packages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ASMT_REQ_PACKAGES

## 📌 Visao Geral

Armazena os **pacotes de avaliacao associados a requisicoes** de vaga do modulo Recruiting (IRC). Define quais pacotes de testes estao configurados para cada requisicao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Associacao pacote-vaga:** vincula pacotes de avaliacao a requisicoes especificas.
- **Gestao de testes:** controla quais testes sao aplicados por vaga.
- **Rastreabilidade:** permite auditar quais avaliacoes foram configuradas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_PACKAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador da associacao | — | 🟡 70% |
| 2 | REQ_CONFIG_ID | NUMBER(18) | NOT NULL | FK | Configuracao da requisicao | IRC_ASMT_REQ_CONFIG | 🟡 65% |
| 3 | PACKAGE_ID | NUMBER(18) | NOT NULL | FK | Pacote de avaliacao | — | 🟡 65% |
| 4 | SEQUENCE_NUMBER | NUMBER | NULL | Controle | Ordem de aplicacao | — | 🟡 55% |
| 5 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Controle | Pacote obrigatorio | — | 🟡 55% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_asmt_req_config]] — via `REQ_CONFIG_ID` (configuracao da requisicao de avaliacao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Pacotes de avaliacao de uma requisicao
```sql
SELECT rp.PACKAGE_ID, rp.SEQUENCE_NUMBER, rp.MANDATORY_FLAG
FROM   IRC_ASMT_REQ_PACKAGES rp
WHERE  rp.REQ_CONFIG_ID = :p_config_id
ORDER BY rp.SEQUENCE_NUMBER;
```

### Filtros comuns
- `REQ_CONFIG_ID = :p_config_id — Por configuracao`
- `MANDATORY_FLAG = 'Y' — Pacotes obrigatorios`

---

## 🔒 Observacoes

- Vincula pacotes de avaliacao a configuracoes de requisicao.
- A ordem de aplicacao e controlada por SEQUENCE_NUMBER.

---

## 📚 Referencias

- [Oracle Docs — IRC_ASMT_REQ_PACKAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircasmtreqpackages.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
