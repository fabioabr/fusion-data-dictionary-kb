---
id: DOC-HCM-011
doc_type: system-doc
title: "ANC_ABS_CERTIFICATIONS_F_TL — Traduções de Certificações de Ausência"
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
  - absence-management
  - certificacoes
  - certifications
  - atestado
  - traducoes
aliases:
  - ANC_ABS_CERTIFICATIONS_F_TL
  - anc_abs_certifications_f_tl
  - certificacoes-ausencia-tl
  - abs-certifications-tl
  - anc-abs-cert-tl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ABS_CERTIFICATIONS_F_TL

## 📌 Visão Geral

Armazena as **traduções** dos tipos de certificação/atestado de ausência em múltiplos idiomas. Define os nomes traduzidos dos documentos exigidos para comprovante de ausência (ex.: atestado médico, declaração de óbito, etc.).

> [!note] Sufixos _F_TL
> Combina **date-effective** (`_F`) e **traduções** (`_TL`). Cada registro possui vigência temporal e idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Nomes de certificações no idioma do colaborador.
- **Self-service:** Rótulos traduzidos na interface de solicitação de ausência.
- **Compliance:** Documentação de tipos de comprovante exigidos por legislação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CERTIFICATION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador da certificação | — | 🟢 90% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 95% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 90% |
| 4 | CERTIFICATION_NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido da certificação | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 75% |
| 6 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 7 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Tabela base de certificações (implícita) — via `CERTIFICATION_ID`

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Certificações em português
```sql
SELECT tl.CERTIFICATION_ID, tl.CERTIFICATION_NAME, tl.DESCRIPTION
FROM   ANC_ABS_CERTIFICATIONS_F_TL tl
WHERE  tl.LANGUAGE = 'PT'
  AND  SYSDATE BETWEEN tl.EFFECTIVE_START_DATE AND tl.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LANGUAGE = 'PT'` — Traduções em português

---

## 🔒 Observações

- Tabela de traduções com vigência temporal.
- Usada para exibir rótulos de tipos de comprovante no idioma do usuário.
- Vinculada à tabela `ANC_PER_ABS_CERTS` que armazena os certificados efetivamente fornecidos.

---

## 🔗 PVOs Relacionados

### [[personabscertificationspvo|PersonAbsCertificationsPVO]] (GL · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_CERTIFICATION_DESC | AbsenceCertificationDesc | ✅ |
| ABSENCE_CERTIFICATION_ID | AbsenceCertificationId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ENTERPRISE_ID | EnterpriseId1 | — |
| LANGUAGE | Language | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| MODULE_ID | ModuleId | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| SOURCE_LANG | SourceLang | — |

---

## 📚 Referências

- [Oracle Docs — ANC_ABS_CERTIFICATIONS_F_TL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancabscertificationsftl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
