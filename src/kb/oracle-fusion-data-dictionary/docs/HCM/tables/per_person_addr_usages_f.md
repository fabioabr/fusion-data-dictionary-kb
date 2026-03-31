---
id: DOC-HCM-689
doc_type: system-doc
title: "PER_PERSON_ADDR_USAGES_F — Usos de Endereço de Pessoa"
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
  - endereco-pessoa
  - address-usage
  - residencia
  - correspondencia
aliases:
  - PER_PERSON_ADDR_USAGES_F
  - per_person_addr_usages_f
  - uso-endereco-pessoa
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERSON_ADDR_USAGES_F

## Visão Geral

Armazena os **usos de endereço** das pessoas no sistema, definindo a finalidade de cada endereço (residência, correspondência, fiscal). Tabela date-effective que controla a vigência temporal de cada endereço.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro de endereços de colaboradores** — residência, correspondência, fiscal
- **Folha de pagamento** — endereço fiscal para cálculos tributários (IRRF, INSS)
- **Envio de correspondência** — holerites, informes de rendimento
- **eSocial** — endereço residencial obrigatório para eventos trabalhistas
- **Logística de benefícios** — entrega de cartões, uniformes, etc.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ADDR_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso de endereço | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | ADDRESS_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de uso do endereço (HOME, MAIL, TAX) | — | 🟢 85% |
| 4 | ADDRESS_ID | NUMBER(18) | NULL | FK | Referência ao endereço detalhado | PER_ADDRESSES_F | 🟡 80% |
| 5 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 6 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 7 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é o endereço principal (Y/N) | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa do uso de endereço)
- [[per_addresses_f]] — via `ADDRESS_ID` (endereço utilizado pela pessoa)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Endereço residencial atual de um colaborador
```sql
SELECT pau.PERSON_ADDR_USAGE_ID, pau.ADDRESS_ID, pau.ADDRESS_TYPE
FROM   PER_PERSON_ADDR_USAGES_F pau
WHERE  pau.PERSON_ID = :p_person_id
  AND  pau.ADDRESS_TYPE = 'HOME'
  AND  SYSDATE BETWEEN pau.EFFECTIVE_START_DATE AND pau.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- Uma pessoa pode ter múltiplos usos de endereço simultâneos (residência, correspondência, fiscal).
- O endereço detalhado (rua, cidade, CEP) está na tabela referenciada via `ADDRESS_ID`.
- `ADDRESS_TYPE` = 'HOME' é geralmente obrigatório para colaboradores ativos.

---

## Referências

- [Oracle Docs — PER_PERSON_ADDR_USAGES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpersonaddrusagesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
