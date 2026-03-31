---
id: DOC-HCM-443
doc_type: system-doc
title: "IRC_ASMT_RESULTS — Resultados de Avaliacao"
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
  - resultado-detalhado
aliases:
  - IRC_ASMT_RESULTS
  - irc_asmt_results
  - irc-asmt-results
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ASMT_RESULTS

## 📌 Visao Geral

Armazena os **resultados individuais de avaliacao** (assessment results) do modulo Recruiting (IRC). Contem resultados detalhados por pergunta/secao dos testes aplicados aos candidatos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Resultados detalhados:** armazena resultados por secao/pergunta.
- **Analise granular:** permite analise detalhada do desempenho do candidato.
- **Feedback:** base para fornecer feedback detalhado ao candidato/recrutador.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESULT_ID | NUMBER(18) | NOT NULL | PK | Identificador do resultado | — | 🟡 70% |
| 2 | PACKAGE_RESULT_ID | NUMBER(18) | NOT NULL | FK | Resultado do pacote | IRC_ASMT_PACKAGE_RESULTS | 🟡 65% |
| 3 | SECTION_CODE | VARCHAR2(80) | NULL | Identificacao | Secao da avaliacao | — | 🟡 55% |
| 4 | SCORE | NUMBER | NULL | Dados | Pontuacao da secao | — | 🟡 60% |
| 5 | MAX_SCORE | NUMBER | NULL | Dados | Pontuacao maxima possivel | — | 🟡 55% |
| 6 | RESULT_TEXT | VARCHAR2(2000) | NULL | Dados | Texto do resultado | — | 🟡 50% |
| 7 | RESULT_STATUS | VARCHAR2(30) | NULL | Classificacao | Status do resultado | — | 🟡 60% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_asmt_package_results]] — via `PACKAGE_RESULT_ID` (resultado do pacote de avaliacao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Resultados detalhados de uma avaliacao
```sql
SELECT r.SECTION_CODE, r.SCORE, r.MAX_SCORE, r.RESULT_STATUS
FROM   IRC_ASMT_RESULTS r
WHERE  r.PACKAGE_RESULT_ID = :p_pkg_result_id;
```

### Filtros comuns
- `PACKAGE_RESULT_ID = :p_pkg_result_id — Por resultado de pacote`

---

## 🔒 Observacoes

- Contem resultados granulares (por secao/pergunta) de avaliacoes.
- Complementa IRC_ASMT_PACKAGE_RESULTS que armazena resultado consolidado.

---

## 📚 Referencias

- [Oracle Docs — IRC_ASMT_RESULTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircasmtresults.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[asmtresultpvo|AsmtResultPVO]] (HCM · BICC: 3/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_CONFIG_ID | AsmtResultPEOAssessmentConfigId | — |
| COMMENTS | AsmtResultPEOComments | ✅ |
| CREATED_BY | AsmtResultPEOCreatedBy | — |
| CREATION_DATE | AsmtResultPEOCreationDate | — |
| LAST_UPDATE_DATE | AsmtResultPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AsmtResultPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AsmtResultPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AsmtResultPEOObjectVersionNumber | — |
| RESULT_ID | ResultId | ✅ |
| SUBMISSION_ID | AsmtResultPEOSubmissionId | — |
