---
id: DOC-HCM-688
doc_type: system-doc
title: "PER_PERSONS — Cadastro de Pessoas"
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
  - pessoas
  - cadastro-pessoa
  - person
  - core-hr
aliases:
  - PER_PERSONS
  - per_persons
  - cadastro-pessoas
  - tabela-pessoas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSONS

## Visão Geral

Tabela **central** do módulo HCM que armazena o cadastro de todas as **pessoas** no sistema — colaboradores, candidatos, contatos, dependentes e trabalhadores contingentes. É a tabela raiz para a maioria das entidades de pessoas no Oracle Fusion HCM.

> [!important] Tabela Core
> Esta é uma das tabelas mais referenciadas do HCM. Praticamente todas as tabelas PER_* possuem FK para `PER_PERSONS.PERSON_ID`.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro único de pessoas** — registro central de todas as pessoas no sistema
- **Base para vínculos empregatícios** — origem de dados para `PER_PERIODS_OF_SERVICE`
- **Gestão de identidade** — vinculação com nomes, endereços, documentos
- **Relatórios de headcount** — contagem de pessoas por tipo e status
- **Integrações com folha de pagamento** — referência base para processamentos
- **Auditoria e compliance** — rastreabilidade do ciclo de vida da pessoa

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | PK | Identificador único da pessoa | — | 🟢 95% |
| 2 | PERSON_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número da pessoa (matrícula visível ao usuário) | — | 🟢 95% |
| 3 | DATE_OF_BIRTH | DATE | NULL | Pessoal | Data de nascimento | — | 🟢 90% |
| 4 | DATE_OF_DEATH | DATE | NULL | Pessoal | Data de falecimento (quando aplicável) | — | 🟢 85% |
| 5 | COUNTRY_OF_BIRTH | VARCHAR2(60) | NULL | Pessoal | País de nascimento | — | 🟡 80% |
| 6 | REGION_OF_BIRTH | VARCHAR2(120) | NULL | Pessoal | Estado/região de nascimento | — | 🟡 75% |
| 7 | TOWN_OF_BIRTH | VARCHAR2(90) | NULL | Pessoal | Cidade de nascimento | — | 🟡 75% |
| 8 | START_DATE | DATE | NOT NULL | Controle | Data de início do registro no sistema | — | 🟢 90% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma — esta é a tabela raiz de pessoas.

### Tabelas-filha (FK de saída)
- [[per_person_names_f]] — via `PERSON_ID` (nomes da pessoa ao longo do tempo)
- [[per_periods_of_service]] — via `PERSON_ID` (perÃ­odos de serviÃ§o da pessoa)
- [[per_all_assignments_m]] — via `PERSON_ID` (vÃ­nculos empregatÃ­cios da pessoa)
- [[per_national_identifiers]] — via `PERSON_ID` (documentos de identidade nacional da pessoa)
- [[per_passports]] — via `PERSON_ID` (passaportes da pessoa)
- [[per_phones]] — via `PERSON_ID` (telefones de contato da pessoa)
- [[per_person_addr_usages_f]] — via `PERSON_ID` (usos de endereÃ§o da pessoa)
- [[per_people_legislative_f]] — via `PERSON_ID` (dados legislativos)
- [[per_person_dlvry_methods]] — via `PERSON_ID` (métodos de entrega)
- [[per_person_type_usages_m]] — via `PERSON_ID` (tipos de pessoa)
- [[per_religions]] — via `PERSON_ID` (registros de religiÃ£o da pessoa)

---

## Uso Típico

### Buscar pessoa por número/matrícula
```sql
SELECT p.PERSON_ID, p.PERSON_NUMBER, p.DATE_OF_BIRTH
FROM   PER_PERSONS p
WHERE  p.PERSON_NUMBER = :p_person_number;
```

### Listar todas as pessoas ativas
```sql
SELECT p.PERSON_ID, p.PERSON_NUMBER
FROM   PER_PERSONS p
WHERE  EXISTS (
  SELECT 1 FROM PER_PERIODS_OF_SERVICE ps
  WHERE ps.PERSON_ID = p.PERSON_ID
    AND ps.ACTUAL_TERMINATION_DATE IS NULL
);
```

---

## Observações

- Tabela central do HCM: alterações aqui impactam praticamente todas as funcionalidades.
- `PERSON_NUMBER` é o identificador visível ao usuário (matrícula).
- `PERSON_ID` é a chave técnica utilizada em todas as FKs.
- Contém dados PII (data de nascimento) — sujeita a LGPD/GDPR.
- Uma pessoa pode ter múltiplos períodos de serviço, atribuições e tipos.

---

## Referências

- [Oracle Docs — PER_PERSONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersons.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
