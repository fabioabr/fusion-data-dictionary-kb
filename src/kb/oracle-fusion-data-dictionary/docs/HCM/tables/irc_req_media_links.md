---
id: DOC-HCM-526
doc_type: system-doc
title: "IRC_REQ_MEDIA_LINKS — Links de Midia de Requisicoes de Recrutamento"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - media-links
  - requisicao
  - irc-req-media
aliases:
  - IRC_REQ_MEDIA_LINKS
  - irc_req_media_links
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQ_MEDIA_LINKS

## 📌 Visão Geral

Armazena os **links de midia** associados a requisicoes de recrutamento (job postings). Cada registro conecta uma requisicao a uma URL de divulgacao em canais de midia (redes sociais, portais, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Divulgacao de vagas em midias sociais e portais de emprego
- Rastreamento de canais de publicacao por requisicao
- Analise de alcance e efetividade de midia por vaga

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQ_MEDIA_LINK_ID | NUMBER(18) | NOT NULL | PK | Identificador unico do link de midia | --- | 🟢 90% |
| 2 | REQUISITION_ID | NUMBER(18) | NOT NULL | FK | ID da requisicao associada | IRC_REQUISITIONS_B | 🟢 90% |
| 3 | MEDIA_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de midia (social, portal, etc.) | --- | 🟡 70% |
| 4 | MEDIA_URL | VARCHAR2(2000) | NULL | Dados | URL do link de midia | --- | 🟡 70% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do link de midia | --- | 🟡 65% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da ultima alteracao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[irc_requisitions_b]] --- via `REQUISITION_ID` (requisicao de recrutamento)

### Tabelas-filha (FK de saída)
- --- Tabelas de midia e posting do modulo Recruiting

---

## 📎 Uso Típico

### Links de midia por requisicao
```sql
SELECT rml.REQ_MEDIA_LINK_ID, rml.MEDIA_TYPE, rml.MEDIA_URL
FROM   IRC_REQ_MEDIA_LINKS rml
WHERE  rml.REQUISITION_ID = :p_requisition_id;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 📚 Referências

- [Oracle Docs — IRC_REQ_MEDIA_LINKS](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircreqmedialinks.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
