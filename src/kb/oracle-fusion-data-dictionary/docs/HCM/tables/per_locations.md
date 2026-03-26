---
id: DOC-HCM-675
doc_type: system-doc
title: "PER_LOCATIONS — Localizações"
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
  - localizacoes
  - locations
  - sites
aliases:
  - PER_LOCATIONS
  - per_locations
  - per-locations
  - localizações
  - per-locations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_LOCATIONS

## 📌 Visão Geral

Armazena as **localizações (sites/escritórios)** da organização. Define os locais físicos onde os colaboradores trabalham, com endereço completo e informações de contato.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de locais** — cadastro de escritórios, fábricas e sites da organização.
- **Atribuição de local** — cada assignment referencia uma localização.
- **Logística** — informações de endereço para entregas e correspondência.
- **Compliance tributário** — localização determina jurisdição fiscal.
- **Relatórios** — análise de headcount e custos por localização.
- **Trabalho remoto** — suporte a localizações virtuais ou home office.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOCATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da localização | — | 🟢 95% |
| 2 | LOCATION_CODE | VARCHAR2(60) | NOT NULL | Identificação | Código da localização | — | 🟢 90% |
| 3 | LOCATION_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome da localização | — | 🟢 90% |
| 4 | ADDRESS_LINE_1 | VARCHAR2(240) | NULL | Endereço | Logradouro (linha 1) | — | 🟢 90% |
| 5 | TOWN_OR_CITY | VARCHAR2(30) | NULL | Endereço | Cidade | — | 🟢 90% |
| 6 | REGION_2 | VARCHAR2(120) | NULL | Endereço | Estado/Província | — | 🟢 85% |
| 7 | POSTAL_CODE | VARCHAR2(30) | NULL | Endereço | CEP/Código postal | — | 🟢 90% |
| 8 | COUNTRY | VARCHAR2(60) | NOT NULL | Endereço | País (código ISO) | — | 🟢 90% |
| 9 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se está ativa (Y/N) | — | 🟢 85% |
| 10 | SHIP_TO_LOCATION_ID | NUMBER(18) | NULL | FK | Localização de entrega | PER_LOCATIONS | 🟡 80% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 15 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_locations]] — via `SHIP_TO_LOCATION_ID` (localização de entrega — auto-referência)

### Tabelas-filha (FK de saída)
- [[per_all_assignments_m]] — via `LOCATION_ID` (assignments nesta localização)

---

## 📎 Uso Típico

### Localizações ativas no Brasil
```sql
SELECT pl.LOCATION_CODE, pl.LOCATION_NAME, pl.TOWN_OR_CITY, pl.REGION_2
FROM   PER_LOCATIONS pl
WHERE  pl.ACTIVE_STATUS = 'Y'
  AND  pl.COUNTRY = 'BR'
ORDER BY pl.LOCATION_NAME;
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Localizações ativas
- `COUNTRY = 'BR'` — Localizações no Brasil
---

## 🔒 Observações

- Tabela não date-effective — registros são atualizados diretamente (sem versionamento temporal).
- Cada assignment referencia uma localização — determina onde o colaborador trabalha.
- O `COUNTRY` determina a jurisdição tributária e trabalhista.
- O `SHIP_TO_LOCATION_ID` permite definir um endereço de entrega diferente do endereço principal.
- Localizações inativas não devem ser atribuídas a novos assignments.
---

## 📚 Referências

- [Oracle Docs — PER_LOCATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perlocations.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
