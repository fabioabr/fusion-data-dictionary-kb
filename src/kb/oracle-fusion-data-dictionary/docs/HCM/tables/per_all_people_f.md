---
id: DOC-HCM-627
doc_type: system-doc
title: "PER_ALL_PEOPLE_F — Pessoas (Cadastro Principal)"
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
  - pessoas
  - cadastro
  - people
aliases:
  - PER_ALL_PEOPLE_F
  - per_all_people_f
  - per-all-people-f
  - pessoas-(cadastro-principal)
  - per-all-people-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALL_PEOPLE_F

## 📌 Visão Geral

Tabela **principal de cadastro de pessoas** no Oracle HCM. Armazena dados pessoais de todos os tipos de pessoas: colaboradores, contingentes, candidatos e contatos. É a tabela central de identidade no módulo HCM, com controle de vigência temporal.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro central** — dados pessoais de todos os colaboradores e pessoas relacionadas.
- **Identidade** — nome, data de nascimento, gênero e informações demográficas.
- **Integração** — chave de ligação com praticamente todas as tabelas de HCM.
- **Compliance LGPD** — contém dados pessoais sensíveis sujeitos a proteção.
- **Relatórios de workforce** — base para headcount e análises demográficas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pessoa | — | 🟢 95% |
| 2 | PERSON_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número/matrícula da pessoa | — | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | FIRST_NAME | VARCHAR2(150) | NULL | Dados Pessoais | Primeiro nome | — | 🟢 95% |
| 6 | LAST_NAME | VARCHAR2(150) | NOT NULL | Dados Pessoais | Sobrenome | — | 🟢 95% |
| 7 | FULL_NAME | VARCHAR2(360) | NULL | Dados Pessoais | Nome completo | — | 🟢 90% |
| 8 | DATE_OF_BIRTH | DATE | NULL | Dados Pessoais | Data de nascimento | — | 🟢 90% |
| 9 | SEX | VARCHAR2(30) | NULL | Dados Pessoais | Gênero | — | 🟢 85% |
| 10 | NATIONAL_IDENTIFIER | VARCHAR2(30) | NULL | Identificação | Identificador nacional (CPF) | — | 🟢 85% |
| 11 | PERSON_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de pessoa | — | 🟢 85% |
| 12 | START_DATE | DATE | NULL | Vigência | Data de início | — | 🟢 90% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 17 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de cadastro de pessoas.

### Tabelas-filha (FK de saída)
- [[per_all_assignments_m]] — via `PERSON_ID` (vÃ­nculos empregatÃ­cios da pessoa)
- [[per_addresses_f]] — via `PERSON_ID` (endereÃ§os do colaborador)
- [[per_email_addresses]] — via `PERSON_ID` (endereÃ§os de e-mail do colaborador)
- [[per_contact_relships_f]] — via `PERSON_ID` (contatos/dependentes)
- [[per_citizenships]] — via `PERSON_ID` (cidadanias e nacionalidades do colaborador)
- [[per_disabilities_f]] — via `PERSON_ID` (registros de deficiÃªncia do colaborador)
- [[per_ethnicities]] — via `PERSON_ID` (informaÃ§Ãµes de etnia do colaborador)
- [[per_drivers_licenses]] — via `PERSON_ID` (carteiras de habilitaÃ§Ã£o do colaborador)

---

## 📎 Uso Típico

### Dados de um colaborador
```sql
SELECT ppf.PERSON_NUMBER, ppf.FULL_NAME, ppf.DATE_OF_BIRTH, ppf.SEX
FROM   PER_ALL_PEOPLE_F ppf
WHERE  ppf.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN ppf.EFFECTIVE_START_DATE AND ppf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registro vigente
- `PERSON_NUMBER = :p_matricula` — Busca por matrícula
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência para dados correntes.
- Contém dados sensíveis (LGPD/GDPR) — acesso deve ser controlado.
- O `NATIONAL_IDENTIFIER` armazena o CPF no contexto brasileiro.
- É a tabela mais referenciada do HCM — praticamente todas as tabelas possuem FK para ela.
- O `PERSON_NUMBER` é a matrícula visível para o usuário.
---

## 📚 Referências

- [Oracle Docs — PER_ALL_PEOPLE_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallpeoplef.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
