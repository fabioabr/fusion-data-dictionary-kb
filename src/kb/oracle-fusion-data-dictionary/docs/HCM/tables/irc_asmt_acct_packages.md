---
id: DOC-HCM-438
doc_type: system-doc
title: "IRC_ASMT_ACCT_PACKAGES — Pacotes de Avaliacao por Conta"
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
  - pacote-avaliacao
  - conta
aliases:
  - IRC_ASMT_ACCT_PACKAGES
  - irc_asmt_acct_packages
  - irc-asmt-acct-packages
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ASMT_ACCT_PACKAGES

## 📌 Visao Geral

Armazena os **pacotes de avaliacao (assessment) associados a contas** de parceiros de avaliacao do modulo Recruiting (IRC). Vincula pacotes de testes a contas de fornecedores externos.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de pacotes:** associa pacotes de avaliacao a contas de parceiros.
- **Integracao com fornecedores:** gerencia pacotes de testes externos.
- **Configuracao:** define quais pacotes estao disponiveis por conta.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCT_PACKAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador da associacao | — | 🟡 65% |
| 2 | ACCOUNT_ID | NUMBER(18) | NOT NULL | FK | Conta do parceiro de avaliacao | — | 🟡 60% |
| 3 | PACKAGE_ID | NUMBER(18) | NOT NULL | FK | Pacote de avaliacao | — | 🟡 60% |
| 4 | PACKAGE_CODE | VARCHAR2(80) | NULL | Identificacao | Codigo do pacote | — | 🟡 55% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da associacao | — | 🟡 60% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 55% |
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
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Tipico

### Pacotes de avaliacao por conta
```sql
SELECT ap.PACKAGE_ID, ap.PACKAGE_CODE, ap.STATUS
FROM   IRC_ASMT_ACCT_PACKAGES ap
WHERE  ap.ACCOUNT_ID = :p_account_id
  AND  ap.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ACCOUNT_ID = :p_account_id — Por conta`
- `ENABLED_FLAG = 'Y' — Pacotes ativos`

---

## 🔒 Observacoes

- Vincula pacotes de testes/avaliacoes a contas de fornecedores.
- Utilizada no fluxo de avaliacoes externas (assessments) do recrutamento.

---

## 📚 Referencias

- [Oracle Docs — IRC_ASMT_ACCT_PACKAGES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircasmtacctpackages.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[asmtacctpackagepvo|AsmtAcctPackagePVO]] (HCM · BICC: 10/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNT_ID | AsmtAcctPackagePEOAccountId | ✅ |
| ACCOUNT_PACKAGE_ID | AccountPackageId | ✅ |
| CREATED_BY | AsmtAcctPackagePEOCreatedBy | ✅ |
| CREATION_DATE | AsmtAcctPackagePEOCreationDate | ✅ |
| LAST_UPDATE_DATE | AsmtAcctPackagePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AsmtAcctPackagePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AsmtAcctPackagePEOLastUpdatedBy | ✅ |
| OBJECT_STATUS | AsmtAcctPackagePEOObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | AsmtAcctPackagePEOObjectVersionNumber | — |
| PACKAGE_CODE | AsmtAcctPackagePEOPackageCode | ✅ |
| PACKAGE_DESC | AsmtAcctPackagePEOPackageDesc | ✅ |
| PACKAGE_NAME | AsmtAcctPackagePEOPackageName | ✅ |
