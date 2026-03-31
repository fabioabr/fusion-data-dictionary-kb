---
id: DOC-HCM-631
doc_type: system-doc
title: "PER_ASSIGNMENT_EXTRA_INFO_M — Informações Extras do Assignment (Materializada)"
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
  - flexfields
  - assignment-extra-info
aliases:
  - PER_ASSIGNMENT_EXTRA_INFO_M
  - per_assignment_extra_info_m
  - per-assignment-extra-info-m
  - informações-extras-do-assignment-(materializada)
  - per-assignment-extra
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGNMENT_EXTRA_INFO_M

## 📌 Visão Geral

Armazena **informações adicionais** (flexfields) associadas aos assignments dos colaboradores. Permite armazenar dados customizados que não cabem na estrutura padrão do assignment.

> [!note] Sufixo _M
> O sufixo `_M` indica tabela **materializada** — combina dados de múltiplas fontes para otimização de consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Dados customizados** — armazena informações específicas da organização por assignment.
- **Flexfields** — suporte a campos descritivos flexíveis (DFF) do Oracle.
- **Extensibilidade** — permite adicionar dados sem alterar a estrutura da tabela principal.
- **Relatórios customizados** — base para relatórios com dados específicos da organização.
- **Integração** — dados extras para interfaces com sistemas externos.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_EXTRA_INFO_ID | NUMBER(18) | NOT NULL | PK | Identificador único da informação extra | — | 🟢 95% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | INFORMATION_TYPE | VARCHAR2(40) | NOT NULL | Classificação | Tipo/categoria da informação extra | — | 🟢 90% |
| 6 | AEI_ATTRIBUTE1 | VARCHAR2(150) | NULL | Dados | Atributo flexível 1 | — | 🟢 85% |
| 7 | AEI_ATTRIBUTE2 | VARCHAR2(150) | NULL | Dados | Atributo flexível 2 | — | 🟢 85% |
| 8 | AEI_ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | Classificação | Categoria dos atributos | — | 🟢 85% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo das informações extras)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Informações extras de um assignment
```sql
SELECT paei.INFORMATION_TYPE, paei.AEI_ATTRIBUTE1, paei.AEI_ATTRIBUTE2
FROM   PER_ASSIGNMENT_EXTRA_INFO_M paei
WHERE  paei.ASSIGNMENT_ID = :p_assignment_id
  AND  SYSDATE BETWEEN paei.EFFECTIVE_START_DATE AND paei.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `INFORMATION_TYPE = :p_info_type` — Informações de um tipo específico
---

## 🔒 Observações

- Tabela materializada (_M) com date-effectiveness.
- Os campos AEI_ATTRIBUTE1..N são genéricos — o significado depende do `INFORMATION_TYPE`.
- Extensamente usada para armazenar dados específicos do país (dados trabalhistas brasileiros, por exemplo).
- A estrutura flexfield permite até 30 atributos (AEI_ATTRIBUTE1 a AEI_ATTRIBUTE30).
---

## 🔗 PVOs Relacionados

### [[assignmentextrainfoeffpvo|AssignmentExtraInfoEFFPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | — |
| AEI_INFORMATION_CATEGORY | AeiInformationCategory | — |
| ASSIGNMENT_EXTRA_INFO_ID | AssignmentExtraInfoId | — |
| ASSIGNMENT_ID | AssignmentId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | EffectiveSequence | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| INFORMATION_TYPE | InformationType | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGISLATION_CODE | LegislationCode | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |

### [[assignmentextrainfoextractpvo|AssignmentExtraInfoExtractPVO]] (HCM · BICC: 18/148)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| AEI_ATTRIBUTE1 | AeiAttribute1 | — |
| AEI_ATTRIBUTE10 | AeiAttribute10 | — |
| AEI_ATTRIBUTE11 | AeiAttribute11 | — |
| AEI_ATTRIBUTE12 | AeiAttribute12 | — |
| AEI_ATTRIBUTE13 | AeiAttribute13 | — |
| AEI_ATTRIBUTE14 | AeiAttribute14 | — |
| AEI_ATTRIBUTE15 | AeiAttribute15 | — |
| AEI_ATTRIBUTE16 | AeiAttribute16 | — |
| AEI_ATTRIBUTE17 | AeiAttribute17 | — |
| AEI_ATTRIBUTE18 | AeiAttribute18 | — |
| AEI_ATTRIBUTE19 | AeiAttribute19 | — |
| AEI_ATTRIBUTE2 | AeiAttribute2 | — |
| AEI_ATTRIBUTE20 | AeiAttribute20 | — |
| AEI_ATTRIBUTE21 | AeiAttribute21 | — |
| AEI_ATTRIBUTE22 | AeiAttribute22 | — |
| AEI_ATTRIBUTE23 | AeiAttribute23 | — |
| AEI_ATTRIBUTE24 | AeiAttribute24 | — |
| AEI_ATTRIBUTE25 | AeiAttribute25 | — |
| AEI_ATTRIBUTE26 | AeiAttribute26 | — |
| AEI_ATTRIBUTE27 | AeiAttribute27 | — |
| AEI_ATTRIBUTE28 | AeiAttribute28 | — |
| AEI_ATTRIBUTE29 | AeiAttribute29 | — |
| AEI_ATTRIBUTE3 | AeiAttribute3 | — |
| AEI_ATTRIBUTE30 | AeiAttribute30 | — |
| AEI_ATTRIBUTE4 | AeiAttribute4 | — |
| AEI_ATTRIBUTE5 | AeiAttribute5 | — |
| AEI_ATTRIBUTE6 | AeiAttribute6 | — |
| AEI_ATTRIBUTE7 | AeiAttribute7 | — |
| AEI_ATTRIBUTE8 | AeiAttribute8 | — |
| AEI_ATTRIBUTE9 | AeiAttribute9 | — |
| AEI_ATTRIBUTE_CATEGORY | AeiAttributeCategory | ✅ |
| AEI_ATTRIBUTE_DATE1 | AeiAttributeDate1 | — |
| AEI_ATTRIBUTE_DATE10 | AeiAttributeDate10 | — |
| AEI_ATTRIBUTE_DATE11 | AeiAttributeDate11 | — |
| AEI_ATTRIBUTE_DATE12 | AeiAttributeDate12 | — |
| AEI_ATTRIBUTE_DATE13 | AeiAttributeDate13 | — |
| AEI_ATTRIBUTE_DATE14 | AeiAttributeDate14 | — |
| AEI_ATTRIBUTE_DATE15 | AeiAttributeDate15 | — |
| AEI_ATTRIBUTE_DATE2 | AeiAttributeDate2 | — |
| AEI_ATTRIBUTE_DATE3 | AeiAttributeDate3 | — |
| AEI_ATTRIBUTE_DATE4 | AeiAttributeDate4 | — |
| AEI_ATTRIBUTE_DATE5 | AeiAttributeDate5 | — |
| AEI_ATTRIBUTE_DATE6 | AeiAttributeDate6 | — |
| AEI_ATTRIBUTE_DATE7 | AeiAttributeDate7 | — |
| AEI_ATTRIBUTE_DATE8 | AeiAttributeDate8 | — |
| AEI_ATTRIBUTE_DATE9 | AeiAttributeDate9 | — |
| AEI_ATTRIBUTE_NUMBER1 | AeiAttributeNumber1 | — |
| AEI_ATTRIBUTE_NUMBER10 | AeiAttributeNumber10 | — |
| AEI_ATTRIBUTE_NUMBER11 | AeiAttributeNumber11 | — |
| AEI_ATTRIBUTE_NUMBER12 | AeiAttributeNumber12 | — |
| AEI_ATTRIBUTE_NUMBER13 | AeiAttributeNumber13 | — |
| AEI_ATTRIBUTE_NUMBER14 | AeiAttributeNumber14 | — |
| AEI_ATTRIBUTE_NUMBER15 | AeiAttributeNumber15 | — |
| AEI_ATTRIBUTE_NUMBER16 | AeiAttributeNumber16 | — |
| AEI_ATTRIBUTE_NUMBER17 | AeiAttributeNumber17 | — |
| AEI_ATTRIBUTE_NUMBER18 | AeiAttributeNumber18 | — |
| AEI_ATTRIBUTE_NUMBER19 | AeiAttributeNumber19 | — |
| AEI_ATTRIBUTE_NUMBER2 | AeiAttributeNumber2 | — |
| AEI_ATTRIBUTE_NUMBER20 | AeiAttributeNumber20 | — |
| AEI_ATTRIBUTE_NUMBER3 | AeiAttributeNumber3 | — |
| AEI_ATTRIBUTE_NUMBER4 | AeiAttributeNumber4 | — |
| AEI_ATTRIBUTE_NUMBER5 | AeiAttributeNumber5 | — |
| AEI_ATTRIBUTE_NUMBER6 | AeiAttributeNumber6 | — |
| AEI_ATTRIBUTE_NUMBER7 | AeiAttributeNumber7 | — |
| AEI_ATTRIBUTE_NUMBER8 | AeiAttributeNumber8 | — |
| AEI_ATTRIBUTE_NUMBER9 | AeiAttributeNumber9 | — |
| AEI_INFORMATION1 | AeiInformation1 | — |
| AEI_INFORMATION10 | AeiInformation10 | — |
| AEI_INFORMATION11 | AeiInformation11 | — |
| AEI_INFORMATION12 | AeiInformation12 | — |
| AEI_INFORMATION13 | AeiInformation13 | — |
| AEI_INFORMATION14 | AeiInformation14 | — |
| AEI_INFORMATION15 | AeiInformation15 | — |
| AEI_INFORMATION16 | AeiInformation16 | — |
| AEI_INFORMATION17 | AeiInformation17 | — |
| AEI_INFORMATION18 | AeiInformation18 | — |
| AEI_INFORMATION19 | AeiInformation19 | — |
| AEI_INFORMATION2 | AeiInformation2 | — |
| AEI_INFORMATION20 | AeiInformation20 | — |
| AEI_INFORMATION21 | AeiInformation21 | — |
| AEI_INFORMATION22 | AeiInformation22 | — |
| AEI_INFORMATION23 | AeiInformation23 | — |
| AEI_INFORMATION24 | AeiInformation24 | — |
| AEI_INFORMATION25 | AeiInformation25 | — |
| AEI_INFORMATION26 | AeiInformation26 | — |
| AEI_INFORMATION27 | AeiInformation27 | — |
| AEI_INFORMATION28 | AeiInformation28 | — |
| AEI_INFORMATION29 | AeiInformation29 | — |
| AEI_INFORMATION3 | AeiInformation3 | — |
| AEI_INFORMATION30 | AeiInformation30 | — |
| AEI_INFORMATION4 | AeiInformation4 | — |
| AEI_INFORMATION5 | AeiInformation5 | — |
| AEI_INFORMATION6 | AeiInformation6 | — |
| AEI_INFORMATION7 | AeiInformation7 | — |
| AEI_INFORMATION8 | AeiInformation8 | — |
| AEI_INFORMATION9 | AeiInformation9 | — |
| AEI_INFORMATION_CATEGORY | AeiInformationCategory | ✅ |
| AEI_INFORMATION_DATE1 | AeiInformationDate1 | — |
| AEI_INFORMATION_DATE10 | AeiInformationDate10 | — |
| AEI_INFORMATION_DATE11 | AeiInformationDate11 | — |
| AEI_INFORMATION_DATE12 | AeiInformationDate12 | — |
| AEI_INFORMATION_DATE13 | AeiInformationDate13 | — |
| AEI_INFORMATION_DATE14 | AeiInformationDate14 | — |
| AEI_INFORMATION_DATE15 | AeiInformationDate15 | — |
| AEI_INFORMATION_DATE2 | AeiInformationDate2 | — |
| AEI_INFORMATION_DATE3 | AeiInformationDate3 | — |
| AEI_INFORMATION_DATE4 | AeiInformationDate4 | — |
| AEI_INFORMATION_DATE5 | AeiInformationDate5 | — |
| AEI_INFORMATION_DATE6 | AeiInformationDate6 | — |
| AEI_INFORMATION_DATE7 | AeiInformationDate7 | — |
| AEI_INFORMATION_DATE8 | AeiInformationDate8 | — |
| AEI_INFORMATION_DATE9 | AeiInformationDate9 | — |
| AEI_INFORMATION_NUMBER1 | AeiInformationNumber1 | — |
| AEI_INFORMATION_NUMBER10 | AeiInformationNumber10 | — |
| AEI_INFORMATION_NUMBER11 | AeiInformationNumber11 | — |
| AEI_INFORMATION_NUMBER12 | AeiInformationNumber12 | — |
| AEI_INFORMATION_NUMBER13 | AeiInformationNumber13 | — |
| AEI_INFORMATION_NUMBER14 | AeiInformationNumber14 | — |
| AEI_INFORMATION_NUMBER15 | AeiInformationNumber15 | — |
| AEI_INFORMATION_NUMBER16 | AeiInformationNumber16 | — |
| AEI_INFORMATION_NUMBER17 | AeiInformationNumber17 | — |
| AEI_INFORMATION_NUMBER18 | AeiInformationNumber18 | — |
| AEI_INFORMATION_NUMBER19 | AeiInformationNumber19 | — |
| AEI_INFORMATION_NUMBER2 | AeiInformationNumber2 | — |
| AEI_INFORMATION_NUMBER20 | AeiInformationNumber20 | — |
| AEI_INFORMATION_NUMBER3 | AeiInformationNumber3 | — |
| AEI_INFORMATION_NUMBER4 | AeiInformationNumber4 | — |
| AEI_INFORMATION_NUMBER5 | AeiInformationNumber5 | — |
| AEI_INFORMATION_NUMBER6 | AeiInformationNumber6 | — |
| AEI_INFORMATION_NUMBER7 | AeiInformationNumber7 | — |
| AEI_INFORMATION_NUMBER8 | AeiInformationNumber8 | — |
| AEI_INFORMATION_NUMBER9 | AeiInformationNumber9 | — |
| ASSIGNMENT_EXTRA_INFO_ID | AssignmentExtraInfoId | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| INFORMATION_TYPE | InformationType | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ASSIGNMENT_EXTRA_INFO_M](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignmentextrainfom.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
