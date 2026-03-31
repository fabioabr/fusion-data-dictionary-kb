---
id: DOC-HCM-485
doc_type: system-doc
title: "IRC_ESIGNATURES — Assinaturas Eletronicas"
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
  - esignatures
  - irc-recruiting
aliases:
  - IRC_ESIGNATURES
  - irc_esignatures
  - irc-esignatures
  - irc_esignatures-oracle
  - irc_esignatures-oracle
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ESIGNATURES

## Visao Geral

**Assinaturas eletronicas** coletadas no recrutamento.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Compliance legal:** Evidencia de assinaturas.
- **Gestao de ofertas:** Aceite/recusa eletronico.
- **LGPD:** Registros de consentimento.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ESIGNATURE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | DOCUMENT_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de documento | — | 🟡 70% |
| 3 | SIGNER_ID | NUMBER(18) | NULL | FK | Pessoa que assinou | — | 🟡 75% |
| 4 | SIGNATURE_STATUS | VARCHAR2(30) | NULL | Classificacao | Status (pending, signed, declined) | — | 🟡 75% |
| 5 | SIGNATURE_DATE | TIMESTAMP | NULL | Dados | Data/hora da assinatura | — | 🟡 75% |
| 6 | IP_ADDRESS | VARCHAR2(50) | NULL | Auditoria | IP no momento da assinatura | — | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## Uso Tipico

### Assinaturas pendentes
```sql
SELECT es.ESIGNATURE_ID, es.DOCUMENT_TYPE, es.SIGNATURE_STATUS
FROM   IRC_ESIGNATURES es WHERE es.SIGNATURE_STATUS = 'PENDING';
```

### Filtros comuns
- `SIGNATURE_STATUS = 'SIGNED'` — Concluidas
---

## Observacoes

- IP_ADDRESS — dados sensiveis (LGPD).
- Valor legal — manter integridade.
---

## Referencias

- [Oracle Docs -- IRC_ESIGNATURES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircesignatures.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[esignaturepvo|ESignaturePVO]] (HCM · BICC: 14/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISCRIMINANT_OBJECT_ID | ESignaturePEODiscriminantObjectId | — |
| DISCRIMINANT_OBJECT_TYPE | ESignaturePEODiscriminantObjectType | — |
| ESIGNATURE_ID | EsignatureId | ✅ |
| FULL_NAME | FullName | ✅ |
| IP_ADDRESS | IpAddress | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_ID | ObjectId | ✅ |
| OBJECT_TYPE | ObjectType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ID | PersonId | ✅ |
| SIGNATURE_DATE | SignatureDate | ✅ |
| VALUE_HASH | ValueHash | ✅ |
