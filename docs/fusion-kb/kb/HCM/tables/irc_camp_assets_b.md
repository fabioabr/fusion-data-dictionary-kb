---
id: DOC-HCM-449
doc_type: system-doc
title: "IRC_CAMP_ASSETS_B — Ativos de Campanhas de Recrutamento (Base)"
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
  - campanha
  - ativos-campanha
  - marketing
  - base
aliases:
  - IRC_CAMP_ASSETS_B
  - irc_camp_assets_b
  - irc-camp-assets-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_CAMP_ASSETS_B

## 📌 Visao Geral

Tabela base que armazena os **ativos (assets) de campanhas de recrutamento** do modulo Recruiting (IRC). Ativos incluem materiais de marketing, banners, descricoes e outros conteudos associados a campanhas.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base) — contem os dados primarios sem traducoes.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de conteudo:** armazena materiais de marketing das campanhas.
- **Marketing de recrutamento:** gerencia banners, textos e midias de campanha.
- **Reutilizacao:** permite reutilizar ativos em multiplas campanhas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSET_ID | NUMBER(18) | NOT NULL | PK | Identificador do ativo | — | 🟡 70% |
| 2 | CAMPAIGN_ID | NUMBER(18) | NOT NULL | FK | Campanha associada | IRC_CAMPAIGNS_B | 🟡 70% |
| 3 | ASSET_CODE | VARCHAR2(80) | NULL | Identificacao | Codigo do ativo | — | 🟡 60% |
| 4 | ASSET_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo do ativo (BANNER, TEXT, VIDEO) | — | 🟡 60% |
| 5 | MEDIA_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de midia | — | 🟡 55% |
| 6 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do ativo | — | 🟡 60% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Ativo/inativo | — | 🟡 60% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_campaigns_b]] — via `CAMPAIGN_ID`

### Tabelas-filha (FK de saida)
- [[irc_camp_assets_tl]] — via `ASSET_ID` (traducoes do ativo de campanha)

---

## 📎 Uso Tipico

### Ativos de uma campanha
```sql
SELECT a.ASSET_ID, a.ASSET_CODE, a.ASSET_TYPE,
       a.MEDIA_TYPE, a.STATUS
FROM   IRC_CAMP_ASSETS_B a
WHERE  a.CAMPAIGN_ID = :p_campaign_id
  AND  a.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `CAMPAIGN_ID = :p_campaign_id — Por campanha`
- `ASSET_TYPE = :p_type — Por tipo de ativo`
- `ENABLED_FLAG = 'Y' — Ativos habilitados`

---

## 🔒 Observacoes

- Tabela base (_B) — traducoes em IRC_CAMP_ASSETS_TL.
- Ativos podem incluir banners, textos, videos e outros materiais de marketing.
- Conteudo real (binario) pode estar armazenado em repositorio externo.

---

## 📚 Referencias

- [Oracle Docs — IRC_CAMP_ASSETS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irccampassetsb.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[campassetpvo|CampAssetPVO]] (HCM · BICC: 7/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSET_ID | CampAssetBPEOAssetId | ✅ |
| ASSET_STATUS_CODE | CampAssetBPEOAssetStatusCode | ✅ |
| ASSET_TYPE_CODE | CampAssetBPEOAssetTypeCode | ✅ |
| AUDIENCE_DERIVED_FLAG | CampAssetBPEOAudienceDerivedFlag | ✅ |
| CAMPAIGN_ID | CampAssetBPEOCampaignId | — |
| CREATED_BY | CampAssetBPEOCreatedBy | — |
| CREATION_DATE | CampAssetBPEOCreationDate | — |
| LAST_UPDATE_DATE | CampAssetBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CampAssetBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | CampAssetBPEOLastUpdatedBy | — |
| MESSAGE_DESIGN_ID | CampAssetBPEOMessageDesignId | — |
| OBJECT_VERSION_NUMBER | CampAssetBPEOObjectVersionNumber | — |
| PARENT_ASSET_ID | CampAssetBPEOParentAssetId | ✅ |
| SCHEDULED_DATE | CampAssetBPEOScheduledDate | ✅ |

### [[campmsgrecipientpvo|CampMsgRecipientPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSET_ID | CampAssetBPEOAssetId | — |
