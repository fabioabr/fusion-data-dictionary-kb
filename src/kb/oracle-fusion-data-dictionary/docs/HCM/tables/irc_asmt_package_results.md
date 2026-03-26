---
id: DOC-HCM-439
doc_type: system-doc
title: "IRC_ASMT_PACKAGE_RESULTS — Resultados de Pacotes de Avaliacao"
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
  - resultado-avaliacao
aliases:
  - IRC_ASMT_PACKAGE_RESULTS
  - irc_asmt_package_results
  - irc-asmt-package-results
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ASMT_PACKAGE_RESULTS

## 📌 Visao Geral

Armazena os **resultados de pacotes de avaliacao** (assessment package results) do modulo Recruiting (IRC). Contem os resultados obtidos por candidatos em testes e avaliacoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Resultados de testes:** armazena resultados de avaliacoes de candidatos.
- **Triagem:** permite filtrar candidatos com base em resultados de avaliacao.
- **Analise de qualidade:** metricas sobre eficacia dos testes.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PACKAGE_RESULT_ID | NUMBER(18) | NOT NULL | PK | Identificador do resultado | — | 🟡 70% |
| 2 | CANDIDATE_ID | NUMBER(18) | NOT NULL | FK | Candidato avaliado | — | 🟡 65% |
| 3 | PACKAGE_ID | NUMBER(18) | NOT NULL | FK | Pacote de avaliacao | — | 🟡 65% |
| 4 | REQUISITION_ID | NUMBER(18) | NULL | FK | Requisicao de vaga | — | 🟡 60% |
| 5 | SCORE | NUMBER | NULL | Dados | Pontuacao obtida | — | 🟡 60% |
| 6 | RESULT_STATUS | VARCHAR2(30) | NULL | Classificacao | Status do resultado (PASS, FAIL, PENDING) | — | 🟡 60% |
| 7 | COMPLETION_DATE | TIMESTAMP | NULL | Periodo | Data de conclusao | — | 🟡 55% |
| 8 | EXPIRY_DATE | DATE | NULL | Periodo | Data de validade do resultado | — | 🟡 50% |
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
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Resultados de avaliacoes por candidato
```sql
SELECT pr.PACKAGE_ID, pr.SCORE, pr.RESULT_STATUS,
       pr.COMPLETION_DATE
FROM   IRC_ASMT_PACKAGE_RESULTS pr
WHERE  pr.CANDIDATE_ID = :p_candidate_id;
```

### Filtros comuns
- `CANDIDATE_ID = :p_candidate_id — Por candidato`
- `RESULT_STATUS = 'PASS' — Aprovados`
- `REQUISITION_ID = :p_req_id — Por requisicao`

---

## 🔒 Observacoes

- Armazena resultados de avaliacoes externas e internas.
- Resultados podem expirar (EXPIRY_DATE) e requerer re-avaliacao.

---

## 📚 Referencias

- [Oracle Docs — IRC_ASMT_PACKAGE_RESULTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircasmtpackageresults.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
