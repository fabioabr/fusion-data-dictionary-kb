---
id: DOC-HCM-237
doc_type: system-doc
title: "HRT_ESTABLISHMENTS_B — Estabelecimentos — Base"
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
  - establishments
  - compliance
  - legal
aliases:
  - HRT_ESTABLISHMENTS_B
  - hrt_establishments_b
  - hrt-establishments-b
  - establishments-base
  - estabelecimentos-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRT_ESTABLISHMENTS_B

## 📌 Visao Geral

Tabela base que armazena os **estabelecimentos** (establishments) da organizacao. Representam locais fisicos registrados para fins legais/regulatorios, como filiais, agencias e escritorios.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Compliance legal:** Registro de estabelecimentos para obrigacoes trabalhistas e fiscais.
- **Organizacao:** Associacao de colaboradores a estabelecimentos para fins regulatorios.
- **Relatorios governamentais:** Base para geracao de relatorios obrigatorios (e.g., RAIS, CAGED no Brasil).

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ESTABLISHMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do estabelecimento | — | 🟢 100% |
| 2 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao fisica associada | [[hr_locations_all_f]] | 🟢 90% |
| 3 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organizacao proprietaria | [[hr_all_organization_units_f]] | 🟢 90% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NOT NULL | Classificacao | Codigo de legislacao (e.g., BR, US) | — | 🟢 95% |
| 5 | DATE_FROM | DATE | NOT NULL | Data | Data de inicio de vigencia | — | 🟢 95% |
| 6 | DATE_TO | DATE | NULL | Data | Data de fim de vigencia | — | 🟢 95% |
| 7 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | FK | Entidade legal associada | [[xle_entity_profiles]] | 🟢 90% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `ORGANIZATION_ID` (organizacao a que pertence o estabelecimento)
- [[xle_entity_profiles]] — via `LEGAL_ENTITY_ID` (entidade legal do estabelecimento)

### Tabelas-filha (FK de saida)
- [[hrt_establishments_tl]] — via `ESTABLISHMENT_ID` (traducoes do estabelecimento)

---

## 📎 Uso Tipico

### Estabelecimentos ativos
```sql
SELECT e.ESTABLISHMENT_ID, e.LEGISLATION_CODE,
       e.DATE_FROM, e.ORGANIZATION_ID
FROM   HRT_ESTABLISHMENTS_B e
WHERE  SYSDATE BETWEEN e.DATE_FROM AND NVL(e.DATE_TO, SYSDATE);
```

---

## 🔒 Observacoes

- Sufixo `_B` indica tabela base — traducoes em [[hrt_establishments_tl]].
- Estabelecimentos sao obrigatorios em legislacoes que exigem registro de filiais (e.g., Brasil).
- Diferente de HR_LOCATIONS — establishments sao entidades legais/regulatorias, locations sao enderecos fisicos.

---

## 📚 Referencias

- [Oracle Docs — HRT_ESTABLISHMENTS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrtestablishmentsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
