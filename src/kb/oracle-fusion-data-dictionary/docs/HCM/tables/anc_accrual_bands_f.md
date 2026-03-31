---
id: DOC-HCM-012
doc_type: system-doc
title: "ANC_ACCRUAL_BANDS_F — Faixas de Acumulação de Ausência"
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
  - faixas-acumulacao
  - accrual-bands
  - escalonamento
aliases:
  - ANC_ACCRUAL_BANDS_F
  - anc_accrual_bands_f
  - faixas-acumulacao-hcm
  - accrual-bands
  - anc-accrual-bands
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_ACCRUAL_BANDS_F

## 📌 Visão Geral

Armazena as **faixas de acumulação (accrual bands)** dos planos de ausência. Define as regras de acumulação progressiva baseadas em tempo de serviço, antiguidade ou outros critérios (ex.: colaboradores com 0-5 anos ganham 20 dias/ano; 5-10 anos ganham 25 dias/ano).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Acumulação progressiva:** Permite configurar taxas de acumulação que aumentam com o tempo de serviço.
- **Políticas escalonadas:** Diferentes faixas para diferentes níveis de antiguidade.
- **Compliance:** Atende legislações que exigem ausências proporcionais ao tempo de empresa.
- **Cálculo automático:** Base para o engine de cálculo de saldos de ausência.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACCRUAL_BAND_ID | NUMBER(18) | NOT NULL | PK | Identificador único da faixa | — | 🟢 90% |
| 2 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de ausência associado | [[anc_absence_plans_f]] | 🟢 95% |
| 3 | BAND_START | NUMBER | NOT NULL | Configuração | Início da faixa (em meses ou anos de serviço) | — | 🟡 75% |
| 4 | BAND_END | NUMBER | NULL | Configuração | Fim da faixa | — | 🟡 75% |
| 5 | ACCRUAL_RATE | NUMBER | NOT NULL | Configuração | Taxa de acumulação para esta faixa | — | 🟡 75% |
| 6 | CEILING_LIMIT | NUMBER | NULL | Configuração | Teto máximo de acumulação para esta faixa | — | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência | — | 🟢 95% |
| 8 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (plano de ausência)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Faixas de acumulação por plano
```sql
SELECT ab.ACCRUAL_BAND_ID, ab.BAND_START, ab.BAND_END,
       ab.ACCRUAL_RATE, ab.CEILING_LIMIT
FROM   ANC_ACCRUAL_BANDS_F ab
WHERE  ab.ABSENCE_PLAN_ID = :p_plan_id
  AND  SYSDATE BETWEEN ab.EFFECTIVE_START_DATE AND ab.EFFECTIVE_END_DATE
ORDER BY ab.BAND_START;
```

### Filtros comuns
- `ABSENCE_PLAN_ID = :p_plan_id` — Faixas de um plano específico
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Vigentes

---

## 🔒 Observações

- As faixas são ordenadas por `BAND_START` e não devem ter gaps ou sobreposições.
- `BAND_END` nulo na última faixa indica "de X em diante" (sem limite superior).
- A taxa de acumulação (`ACCRUAL_RATE`) é definida por período conforme o `ACCRUAL_FREQUENCY` do plano.

---

## 🔗 PVOs Relacionados

### [[accrualplanpvo|AccrualPlanPVO]] (GL · BICC: 4/166)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_PLAN_ID | AbsencePlanId2 | — |
| ACC_BAND_SEQUENCE | AccBandSequence | ✅ |
| ACC_CARRYOVER_LIMIT | AccCarryoverLimit | — |
| ACC_INPUT_EXPRESSION | AccInputExpression | — |
| ACC_OUTPUT_FORMULA_ID | AccOutputFormulaId | — |
| ACCRUAL_BAND_ID | AccrualBandId | — |
| ACCRUAL_CEILING | AccrualCeiling | — |
| ACCRUAL_RATE | AccrualRate | ✅ |
| ANC_ACCRUAL_BANDS_F_ALTCD | AncAccrualBandsFAltcd | — |
| ANC_CHAR1 | AncChar11 | — |
| ANC_CHAR2 | AncChar21 | — |
| ANC_CHAR3 | AncChar31 | — |
| ANC_CHAR4 | AncChar41 | — |
| ANC_CHAR5 | AncChar51 | — |
| ANC_DATE1 | AncDate11 | — |
| ANC_DATE2 | AncDate21 | — |
| ANC_DATE3 | AncDate31 | — |
| ANC_DATE4 | AncDate41 | — |
| ANC_DATE5 | AncDate51 | — |
| ANC_NUMBER1 | AncNumber11 | — |
| ANC_NUMBER2 | AncNumber21 | — |
| ANC_NUMBER3 | AncNumber31 | — |
| ANC_NUMBER4 | AncNumber41 | — |
| ANC_NUMBER5 | AncNumber51 | — |
| ATTRIBUTE1 | Attribute110 | — |
| ATTRIBUTE10 | Attribute101 | — |
| ATTRIBUTE11 | Attribute111 | — |
| ATTRIBUTE12 | Attribute121 | — |
| ATTRIBUTE13 | Attribute131 | — |
| ATTRIBUTE14 | Attribute141 | — |
| ATTRIBUTE15 | Attribute151 | — |
| ATTRIBUTE16 | Attribute161 | — |
| ATTRIBUTE17 | Attribute171 | — |
| ATTRIBUTE18 | Attribute181 | — |
| ATTRIBUTE19 | Attribute191 | — |
| ATTRIBUTE2 | Attribute210 | — |
| ATTRIBUTE20 | Attribute201 | — |
| ATTRIBUTE21 | Attribute211 | — |
| ATTRIBUTE22 | Attribute221 | — |
| ATTRIBUTE23 | Attribute231 | — |
| ATTRIBUTE24 | Attribute241 | — |
| ATTRIBUTE25 | Attribute251 | — |
| ATTRIBUTE26 | Attribute261 | — |
| ATTRIBUTE27 | Attribute271 | — |
| ATTRIBUTE28 | Attribute281 | — |
| ATTRIBUTE29 | Attribute291 | — |
| ATTRIBUTE3 | Attribute31 | — |
| ATTRIBUTE30 | Attribute301 | — |
| ATTRIBUTE4 | Attribute41 | — |
| ATTRIBUTE5 | Attribute51 | — |
| ATTRIBUTE6 | Attribute61 | — |
| ATTRIBUTE7 | Attribute71 | — |
| ATTRIBUTE8 | Attribute81 | — |
| ATTRIBUTE9 | Attribute91 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory1 | — |
| ATTRIBUTE_DATE1 | AttributeDate16 | — |
| ATTRIBUTE_DATE10 | AttributeDate101 | — |
| ATTRIBUTE_DATE11 | AttributeDate111 | — |
| ATTRIBUTE_DATE12 | AttributeDate121 | — |
| ATTRIBUTE_DATE13 | AttributeDate131 | — |
| ATTRIBUTE_DATE14 | AttributeDate141 | — |
| ATTRIBUTE_DATE15 | AttributeDate151 | — |
| ATTRIBUTE_DATE2 | AttributeDate21 | — |
| ATTRIBUTE_DATE3 | AttributeDate31 | — |
| ATTRIBUTE_DATE4 | AttributeDate41 | — |
| ATTRIBUTE_DATE5 | AttributeDate51 | — |
| ATTRIBUTE_DATE6 | AttributeDate61 | — |
| ATTRIBUTE_DATE7 | AttributeDate71 | — |
| ATTRIBUTE_DATE8 | AttributeDate81 | — |
| ATTRIBUTE_DATE9 | AttributeDate91 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber110 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber101 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber111 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber121 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber131 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber141 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber151 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber161 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber171 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber181 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber191 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber21 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber201 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber31 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber41 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber51 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber61 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber71 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber81 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber91 | — |
| CREATED_BY | CreatedBy2 | — |
| CREATION_DATE | CreationDate2 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate2 | — |
| EFFECTIVE_START_DATE | EffectiveStartDate2 | ✅ |
| ENTERPRISE_ID | EnterpriseId2 | — |
| INFORMATION1 | Information110 | — |
| INFORMATION10 | Information101 | — |
| INFORMATION11 | Information111 | — |
| INFORMATION12 | Information121 | — |
| INFORMATION13 | Information131 | — |
| INFORMATION14 | Information141 | — |
| INFORMATION15 | Information151 | — |
| INFORMATION16 | Information161 | — |
| INFORMATION17 | Information171 | — |
| INFORMATION18 | Information181 | — |
| INFORMATION19 | Information191 | — |
| INFORMATION2 | Information210 | — |
| INFORMATION20 | Information201 | — |
| INFORMATION21 | Information211 | — |
| INFORMATION22 | Information221 | — |
| INFORMATION23 | Information231 | — |
| INFORMATION24 | Information241 | — |
| INFORMATION25 | Information251 | — |
| INFORMATION26 | Information261 | — |
| INFORMATION27 | Information271 | — |
| INFORMATION28 | Information281 | — |
| INFORMATION29 | Information291 | — |
| INFORMATION3 | Information31 | — |
| INFORMATION30 | Information301 | — |
| INFORMATION4 | Information41 | — |
| INFORMATION5 | Information51 | — |
| INFORMATION6 | Information61 | — |
| INFORMATION7 | Information71 | — |
| INFORMATION8 | Information81 | — |
| INFORMATION9 | Information91 | — |
| INFORMATION_CATEGORY | InformationCategory1 | — |
| INFORMATION_DATE1 | InformationDate16 | — |
| INFORMATION_DATE10 | InformationDate101 | — |
| INFORMATION_DATE11 | InformationDate111 | — |
| INFORMATION_DATE12 | InformationDate121 | — |
| INFORMATION_DATE13 | InformationDate131 | — |
| INFORMATION_DATE14 | InformationDate141 | — |
| INFORMATION_DATE15 | InformationDate151 | — |
| INFORMATION_DATE2 | InformationDate21 | — |
| INFORMATION_DATE3 | InformationDate31 | — |
| INFORMATION_DATE4 | InformationDate41 | — |
| INFORMATION_DATE5 | InformationDate51 | — |
| INFORMATION_DATE6 | InformationDate61 | — |
| INFORMATION_DATE7 | InformationDate71 | — |
| INFORMATION_DATE8 | InformationDate81 | — |
| INFORMATION_DATE9 | InformationDate91 | — |
| INFORMATION_NUMBER1 | InformationNumber110 | — |
| INFORMATION_NUMBER10 | InformationNumber101 | — |
| INFORMATION_NUMBER11 | InformationNumber111 | — |
| INFORMATION_NUMBER12 | InformationNumber121 | — |
| INFORMATION_NUMBER13 | InformationNumber131 | — |
| INFORMATION_NUMBER14 | InformationNumber141 | — |
| INFORMATION_NUMBER15 | InformationNumber151 | — |
| INFORMATION_NUMBER16 | InformationNumber161 | — |
| INFORMATION_NUMBER17 | InformationNumber171 | — |
| INFORMATION_NUMBER18 | InformationNumber181 | — |
| INFORMATION_NUMBER19 | InformationNumber191 | — |
| INFORMATION_NUMBER2 | InformationNumber21 | — |
| INFORMATION_NUMBER20 | InformationNumber201 | — |
| INFORMATION_NUMBER3 | InformationNumber31 | — |
| INFORMATION_NUMBER4 | InformationNumber41 | — |
| INFORMATION_NUMBER5 | InformationNumber51 | — |
| INFORMATION_NUMBER6 | InformationNumber61 | — |
| INFORMATION_NUMBER7 | InformationNumber71 | — |
| INFORMATION_NUMBER8 | InformationNumber81 | — |
| INFORMATION_NUMBER9 | InformationNumber91 | — |
| LAST_UPDATE_DATE | LastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin2 | — |
| LAST_UPDATED_BY | LastUpdatedBy2 | — |
| MODULE_ID | ModuleId2 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber2 | — |

---

## 📚 Referências

- [Oracle Docs — ANC_ACCRUAL_BANDS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancaccruralbandsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
