---
id: DOC-HCM-678
doc_type: system-doc
title: "PER_LOC_ADDRESS_USAGES_F — Usos de Endereço de Localização"
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
  - per-locations
  - address-usages
  - endereco-localizacao
  - uso-endereco
aliases:
  - PER_LOC_ADDRESS_USAGES_F
  - per_loc_address_usages_f
  - uso-endereco-localizacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_LOC_ADDRESS_USAGES_F

## Visão Geral

Armazena os **usos de endereço** associados a cada localização, definindo a finalidade de cada endereço vinculado (ex: endereço principal, endereço de correspondência, endereço fiscal). Tabela date-effective com vigência temporal.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição do tipo de uso do endereço** — diferenciar endereço principal, fiscal, correspondência
- **Compliance tributário** — associar endereço fiscal correto para cálculos de impostos
- **Envio de correspondências** — identificar endereço de entrega para cada local
- **Auditoria de localizações** — rastrear alterações em usos de endereço ao longo do tempo

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOC_ADDRESS_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do uso de endereço | — | 🟢 90% |
| 2 | LOCATION_ID | NUMBER(18) | NOT NULL | FK | Referência à localização | PER_LOCATIONS | 🟢 95% |
| 3 | ADDRESS_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de uso do endereço (MAIN, MAIL, TAX) | — | 🟡 75% |
| 4 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 5 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 6 | ADDRESS_LINE_1 | VARCHAR2(240) | NULL | Endereço | Primeira linha do endereço | — | 🟡 75% |
| 7 | TOWN_OR_CITY | VARCHAR2(30) | NULL | Endereço | Cidade | — | 🟡 75% |
| 8 | REGION_1 | VARCHAR2(120) | NULL | Endereço | Estado/Região | — | 🟡 70% |
| 9 | POSTAL_CODE | VARCHAR2(30) | NULL | Endereço | CEP/Código postal | — | 🟡 75% |
| 10 | COUNTRY | VARCHAR2(60) | NULL | Endereço | País | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_locations]] — via `LOCATION_ID` (localizaÃ§Ã£o do uso de endereÃ§o)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Endereço principal ativo de uma localização
```sql
SELECT lau.ADDRESS_LINE_1, lau.TOWN_OR_CITY, lau.REGION_1,
       lau.POSTAL_CODE, lau.COUNTRY
FROM   PER_LOC_ADDRESS_USAGES_F lau
WHERE  lau.LOCATION_ID = :p_location_id
  AND  lau.ADDRESS_TYPE = 'MAIN'
  AND  SYSDATE BETWEEN lau.EFFECTIVE_START_DATE AND lau.EFFECTIVE_END_DATE;
```

---

## Observações

- Tabela date-effective: sempre filtrar por vigência para obter o registro corrente.
- Uma localização pode ter múltiplos usos de endereço simultaneamente (principal, fiscal, correspondência).
- O campo `ADDRESS_TYPE` determina a finalidade do endereço.

---

## Referências

- [Oracle Docs — PER_LOC_ADDRESS_USAGES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlocaddressusagesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
