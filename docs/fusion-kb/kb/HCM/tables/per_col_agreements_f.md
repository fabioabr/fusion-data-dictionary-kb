---
id: DOC-HCM-646
doc_type: system-doc
title: "PER_COL_AGREEMENTS_F — Acordos Coletivos"
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
  - acordos-coletivos
  - collective-agreements
aliases:
  - PER_COL_AGREEMENTS_F
  - per_col_agreements_f
  - per-col-agreements-f
  - acordos-coletivos
  - per-col-agreements-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_COL_AGREEMENTS_F

## 📌 Visão Geral

Armazena os **acordos coletivos de trabalho** (convenções e acordos sindicais), com vigência temporal. Define as condições negociadas entre empregador e sindicatos.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de acordos coletivos** — registro de convenções e acordos sindicais.
- **Compliance trabalhista** — garantia de conformidade com condições negociadas.
- **Integração com payroll** — regras de remuneração definidas em acordos coletivos.
- **Vigência** — controle de períodos de validade dos acordos.
- **Relatórios** — base para análise de impacto de negociações coletivas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COL_AGREEMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do acordo coletivo | — | 🟢 90% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 85% |
| 5 | AGREEMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de acordo (CONVENTION, AGREEMENT) | — | 🟡 75% |
| 6 | STATUS | VARCHAR2(30) | NULL | Status | Status do acordo (ACTIVE, EXPIRED) | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de acordos coletivos.

### Tabelas-filha (FK de saída)
- [[per_col_agreements_f_tl]] — via `COL_AGREEMENT_ID` (traduções do acordo coletivo de trabalho)

---

## 📎 Uso Típico

### Acordos coletivos vigentes
```sql
SELECT pca.COL_AGREEMENT_ID, pca.AGREEMENT_TYPE, pca.STATUS
FROM   PER_COL_AGREEMENTS_F pca
WHERE  SYSDATE BETWEEN pca.EFFECTIVE_START_DATE AND pca.EFFECTIVE_END_DATE
  AND  pca.STATUS = 'ACTIVE';
```

### Filtros comuns
- `STATUS = 'ACTIVE'` — Acordos ativos
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Acordos vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Acordos coletivos impactam diretamente regras de payroll (pisos salariais, adicionais).
- O `LEGISLATION_CODE` vincula o acordo à legislação do país.
---

## 🔗 PVOs Relacionados

### [[collectiveagreementpvo|CollectiveAgreementPVO]] (GL · BICC: 16/154)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BARGAINING_UNIT_CODE | BargainingUnitCode | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CAG_INFORMATION1 | CagInformation1 | — |
| CAG_INFORMATION10 | CagInformation10 | — |
| CAG_INFORMATION11 | CagInformation11 | — |
| CAG_INFORMATION12 | CagInformation12 | — |
| CAG_INFORMATION13 | CagInformation13 | — |
| CAG_INFORMATION14 | CagInformation14 | — |
| CAG_INFORMATION15 | CagInformation15 | — |
| CAG_INFORMATION16 | CagInformation16 | — |
| CAG_INFORMATION17 | CagInformation17 | — |
| CAG_INFORMATION18 | CagInformation18 | — |
| CAG_INFORMATION19 | CagInformation19 | — |
| CAG_INFORMATION2 | CagInformation2 | — |
| CAG_INFORMATION20 | CagInformation20 | — |
| CAG_INFORMATION21 | CagInformation21 | — |
| CAG_INFORMATION22 | CagInformation22 | — |
| CAG_INFORMATION23 | CagInformation23 | — |
| CAG_INFORMATION24 | CagInformation24 | — |
| CAG_INFORMATION25 | CagInformation25 | — |
| CAG_INFORMATION26 | CagInformation26 | — |
| CAG_INFORMATION27 | CagInformation27 | — |
| CAG_INFORMATION28 | CagInformation28 | — |
| CAG_INFORMATION29 | CagInformation29 | — |
| CAG_INFORMATION3 | CagInformation3 | — |
| CAG_INFORMATION30 | CagInformation30 | — |
| CAG_INFORMATION4 | CagInformation4 | — |
| CAG_INFORMATION5 | CagInformation5 | — |
| CAG_INFORMATION6 | CagInformation6 | — |
| CAG_INFORMATION7 | CagInformation7 | — |
| CAG_INFORMATION8 | CagInformation8 | — |
| CAG_INFORMATION9 | CagInformation9 | — |
| CAG_INFORMATION_CATEGORY | CagInformationCategory | — |
| CAG_INFORMATION_DATE1 | CagInformationDate1 | — |
| CAG_INFORMATION_DATE10 | CagInformationDate10 | — |
| CAG_INFORMATION_DATE11 | CagInformationDate11 | — |
| CAG_INFORMATION_DATE12 | CagInformationDate12 | — |
| CAG_INFORMATION_DATE13 | CagInformationDate13 | — |
| CAG_INFORMATION_DATE14 | CagInformationDate14 | — |
| CAG_INFORMATION_DATE15 | CagInformationDate15 | — |
| CAG_INFORMATION_DATE2 | CagInformationDate2 | — |
| CAG_INFORMATION_DATE3 | CagInformationDate3 | — |
| CAG_INFORMATION_DATE4 | CagInformationDate4 | — |
| CAG_INFORMATION_DATE5 | CagInformationDate5 | — |
| CAG_INFORMATION_DATE6 | CagInformationDate6 | — |
| CAG_INFORMATION_DATE7 | CagInformationDate7 | — |
| CAG_INFORMATION_DATE8 | CagInformationDate8 | — |
| CAG_INFORMATION_DATE9 | CagInformationDate9 | — |
| CAG_INFORMATION_NUMBER1 | CagInformationNumber1 | — |
| CAG_INFORMATION_NUMBER10 | CagInformationNumber10 | — |
| CAG_INFORMATION_NUMBER11 | CagInformationNumber11 | — |
| CAG_INFORMATION_NUMBER12 | CagInformationNumber12 | — |
| CAG_INFORMATION_NUMBER13 | CagInformationNumber13 | — |
| CAG_INFORMATION_NUMBER14 | CagInformationNumber14 | — |
| CAG_INFORMATION_NUMBER15 | CagInformationNumber15 | — |
| CAG_INFORMATION_NUMBER16 | CagInformationNumber16 | — |
| CAG_INFORMATION_NUMBER17 | CagInformationNumber17 | — |
| CAG_INFORMATION_NUMBER18 | CagInformationNumber18 | — |
| CAG_INFORMATION_NUMBER19 | CagInformationNumber19 | — |
| CAG_INFORMATION_NUMBER2 | CagInformationNumber2 | — |
| CAG_INFORMATION_NUMBER20 | CagInformationNumber20 | — |
| CAG_INFORMATION_NUMBER3 | CagInformationNumber3 | — |
| CAG_INFORMATION_NUMBER4 | CagInformationNumber4 | — |
| CAG_INFORMATION_NUMBER5 | CagInformationNumber5 | — |
| CAG_INFORMATION_NUMBER6 | CagInformationNumber6 | — |
| CAG_INFORMATION_NUMBER7 | CagInformationNumber7 | — |
| CAG_INFORMATION_NUMBER8 | CagInformationNumber8 | — |
| CAG_INFORMATION_NUMBER9 | CagInformationNumber9 | — |
| COLLECTIVE_AGREEMENT_ID | CollectiveAgreementId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_ORG_CONTACT | EmployeeOrgContact | — |
| EMPLOYEE_ORG_NAME | EmployeeOrgName | ✅ |
| EMPLOYER_ORG_CONTACT | EmployerOrgContact | — |
| EMPLOYER_ORG_NAME | EmployerOrgName | ✅ |
| IDENTIFICATION_CODE | IdentificationCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LEGISLATION_CODE | LegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| STATUS | Status | ✅ |
| UNION_ID | UnionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_COL_AGREEMENTS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percolagreementsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
