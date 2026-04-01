---
id: DOC-HCM-385
doc_type: system-doc
title: "HWM_TM_REP_ATRBS — Atributos de Entradas Reportadas de Tempo"
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
  - time-management
  - reported-attributes
  - atributos-reportados
aliases:
  - HWM_TM_REP_ATRBS
  - hwm_tm_rep_atrbs
  - hwm-tm-rep-atrbs
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_ATRBS

## 📌 Visão Geral

Armazena os **atributos associados a entradas reportadas** (reported entries) de tempo. Extende as informações das entradas reportadas com pares de atributo-valor adicionais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Extensibilidade:** atributos adicionais para entradas reportadas ao payroll.
- **Mapeamento de custos:** atributos como centro de custo, projeto, tarefa.
- **Integração com GL/Projects:** dados complementares para contabilização.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_ATRB_ID | NUMBER(18) | NOT NULL | PK | Identificador único do atributo | — | 🟡 70% |
| 2 | REP_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada reportada associada | — | 🟡 70% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(80) | NOT NULL | Identificação | Nome do atributo | — | 🟡 65% |
| 4 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 65% |
| 5 | ATTRIBUTE_CATEGORY | VARCHAR2(80) | NULL | Classificação | Categoria do atributo | — | 🟡 60% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha documentada neste release.

---

## 📎 Uso Típico

### Atributos de uma entrada reportada
```sql
SELECT a.REP_ATRB_ID, a.ATTRIBUTE_NAME, a.ATTRIBUTE_VALUE
FROM   HWM_TM_REP_ATRBS a
WHERE  a.REP_ENTRY_ID = :p_rep_entry_id;
```

### Filtros comuns
- `REP_ENTRY_ID = :p_rep_entry_id — Filtrar por entrada reportada`

---

## 🔒 Observações

- Estrutura EAV para extensão de entradas reportadas.
- Atributos típicos incluem centro de custo, projeto e código de elemento de pagamento.

---

## 🔗 PVOs Relacionados

### [[timerepositoryattributeextractp1|TimeRepositoryAttributeExtractP1]] (HCM · BICC: 175/175)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | AttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | AttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | AttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | AttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | AttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | AttributeDate15 | ✅ |
| ATTRIBUTE_DATE16 | AttributeDate16 | ✅ |
| ATTRIBUTE_DATE17 | AttributeDate17 | ✅ |
| ATTRIBUTE_DATE18 | AttributeDate18 | ✅ |
| ATTRIBUTE_DATE19 | AttributeDate19 | ✅ |
| ATTRIBUTE_DATE2 | AttributeDate2 | ✅ |
| ATTRIBUTE_DATE20 | AttributeDate20 | ✅ |
| ATTRIBUTE_DATE21 | AttributeDate21 | ✅ |
| ATTRIBUTE_DATE22 | AttributeDate22 | ✅ |
| ATTRIBUTE_DATE23 | AttributeDate23 | ✅ |
| ATTRIBUTE_DATE24 | AttributeDate24 | ✅ |
| ATTRIBUTE_DATE25 | AttributeDate25 | ✅ |
| ATTRIBUTE_DATE26 | AttributeDate26 | ✅ |
| ATTRIBUTE_DATE27 | AttributeDate27 | ✅ |
| ATTRIBUTE_DATE28 | AttributeDate28 | ✅ |
| ATTRIBUTE_DATE29 | AttributeDate29 | ✅ |
| ATTRIBUTE_DATE3 | AttributeDate3 | ✅ |
| ATTRIBUTE_DATE30 | AttributeDate30 | ✅ |
| ATTRIBUTE_DATE31 | AttributeDate31 | ✅ |
| ATTRIBUTE_DATE32 | AttributeDate32 | ✅ |
| ATTRIBUTE_DATE33 | AttributeDate33 | ✅ |
| ATTRIBUTE_DATE34 | AttributeDate34 | ✅ |
| ATTRIBUTE_DATE35 | AttributeDate35 | ✅ |
| ATTRIBUTE_DATE36 | AttributeDate36 | ✅ |
| ATTRIBUTE_DATE37 | AttributeDate37 | ✅ |
| ATTRIBUTE_DATE38 | AttributeDate38 | ✅ |
| ATTRIBUTE_DATE39 | AttributeDate39 | ✅ |
| ATTRIBUTE_DATE4 | AttributeDate4 | ✅ |
| ATTRIBUTE_DATE40 | AttributeDate40 | ✅ |
| ATTRIBUTE_DATE5 | AttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | AttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | AttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | AttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | AttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER21 | AttributeNumber21 | ✅ |
| ATTRIBUTE_NUMBER22 | AttributeNumber22 | ✅ |
| ATTRIBUTE_NUMBER23 | AttributeNumber23 | ✅ |
| ATTRIBUTE_NUMBER24 | AttributeNumber24 | ✅ |
| ATTRIBUTE_NUMBER25 | AttributeNumber25 | ✅ |
| ATTRIBUTE_NUMBER26 | AttributeNumber26 | ✅ |
| ATTRIBUTE_NUMBER27 | AttributeNumber27 | ✅ |
| ATTRIBUTE_NUMBER28 | AttributeNumber28 | ✅ |
| ATTRIBUTE_NUMBER29 | AttributeNumber29 | ✅ |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER30 | AttributeNumber30 | ✅ |
| ATTRIBUTE_NUMBER31 | AttributeNumber31 | ✅ |
| ATTRIBUTE_NUMBER32 | AttributeNumber32 | ✅ |
| ATTRIBUTE_NUMBER33 | AttributeNumber33 | ✅ |
| ATTRIBUTE_NUMBER34 | AttributeNumber34 | ✅ |
| ATTRIBUTE_NUMBER35 | AttributeNumber35 | ✅ |
| ATTRIBUTE_NUMBER36 | AttributeNumber36 | ✅ |
| ATTRIBUTE_NUMBER37 | AttributeNumber37 | ✅ |
| ATTRIBUTE_NUMBER38 | AttributeNumber38 | ✅ |
| ATTRIBUTE_NUMBER39 | AttributeNumber39 | ✅ |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER40 | AttributeNumber40 | ✅ |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | ✅ |
| ATTRIBUTE_ROW_TYPE_ID | AttributeRowTypeId | ✅ |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP11 | AttributeTimestamp11 | ✅ |
| ATTRIBUTE_TIMESTAMP12 | AttributeTimestamp12 | ✅ |
| ATTRIBUTE_TIMESTAMP13 | AttributeTimestamp13 | ✅ |
| ATTRIBUTE_TIMESTAMP14 | AttributeTimestamp14 | ✅ |
| ATTRIBUTE_TIMESTAMP15 | AttributeTimestamp15 | ✅ |
| ATTRIBUTE_TIMESTAMP16 | AttributeTimestamp16 | ✅ |
| ATTRIBUTE_TIMESTAMP17 | AttributeTimestamp17 | ✅ |
| ATTRIBUTE_TIMESTAMP18 | AttributeTimestamp18 | ✅ |
| ATTRIBUTE_TIMESTAMP19 | AttributeTimestamp19 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP20 | AttributeTimestamp20 | ✅ |
| ATTRIBUTE_TIMESTAMP21 | AttributeTimestamp21 | ✅ |
| ATTRIBUTE_TIMESTAMP22 | AttributeTimestamp22 | ✅ |
| ATTRIBUTE_TIMESTAMP23 | AttributeTimestamp23 | ✅ |
| ATTRIBUTE_TIMESTAMP24 | AttributeTimestamp24 | ✅ |
| ATTRIBUTE_TIMESTAMP25 | AttributeTimestamp25 | ✅ |
| ATTRIBUTE_TIMESTAMP26 | AttributeTimestamp26 | ✅ |
| ATTRIBUTE_TIMESTAMP27 | AttributeTimestamp27 | ✅ |
| ATTRIBUTE_TIMESTAMP28 | AttributeTimestamp28 | ✅ |
| ATTRIBUTE_TIMESTAMP29 | AttributeTimestamp29 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP30 | AttributeTimestamp30 | ✅ |
| ATTRIBUTE_TIMESTAMP31 | AttributeTimestamp31 | ✅ |
| ATTRIBUTE_TIMESTAMP32 | AttributeTimestamp32 | ✅ |
| ATTRIBUTE_TIMESTAMP33 | AttributeTimestamp33 | ✅ |
| ATTRIBUTE_TIMESTAMP34 | AttributeTimestamp34 | ✅ |
| ATTRIBUTE_TIMESTAMP35 | AttributeTimestamp35 | ✅ |
| ATTRIBUTE_TIMESTAMP36 | AttributeTimestamp36 | ✅ |
| ATTRIBUTE_TIMESTAMP37 | AttributeTimestamp37 | ✅ |
| ATTRIBUTE_TIMESTAMP38 | AttributeTimestamp38 | ✅ |
| ATTRIBUTE_TIMESTAMP39 | AttributeTimestamp39 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP40 | AttributeTimestamp40 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | ✅ |
| ATTRIBUTE_VARCHAR1 | AttributeVarchar1 | ✅ |
| ATTRIBUTE_VARCHAR10 | AttributeVarchar10 | ✅ |
| ATTRIBUTE_VARCHAR11 | AttributeVarchar11 | ✅ |
| ATTRIBUTE_VARCHAR12 | AttributeVarchar12 | ✅ |
| ATTRIBUTE_VARCHAR13 | AttributeVarchar13 | ✅ |
| ATTRIBUTE_VARCHAR14 | AttributeVarchar14 | ✅ |
| ATTRIBUTE_VARCHAR15 | AttributeVarchar15 | ✅ |
| ATTRIBUTE_VARCHAR16 | AttributeVarchar16 | ✅ |
| ATTRIBUTE_VARCHAR17 | AttributeVarchar17 | ✅ |
| ATTRIBUTE_VARCHAR18 | AttributeVarchar18 | ✅ |
| ATTRIBUTE_VARCHAR19 | AttributeVarchar19 | ✅ |
| ATTRIBUTE_VARCHAR2 | AttributeVarchar2 | ✅ |
| ATTRIBUTE_VARCHAR20 | AttributeVarchar20 | ✅ |
| ATTRIBUTE_VARCHAR21 | AttributeVarchar21 | ✅ |
| ATTRIBUTE_VARCHAR22 | AttributeVarchar22 | ✅ |
| ATTRIBUTE_VARCHAR23 | AttributeVarchar23 | ✅ |
| ATTRIBUTE_VARCHAR24 | AttributeVarchar24 | ✅ |
| ATTRIBUTE_VARCHAR25 | AttributeVarchar25 | ✅ |
| ATTRIBUTE_VARCHAR26 | AttributeVarchar26 | ✅ |
| ATTRIBUTE_VARCHAR27 | AttributeVarchar27 | ✅ |
| ATTRIBUTE_VARCHAR28 | AttributeVarchar28 | ✅ |
| ATTRIBUTE_VARCHAR29 | AttributeVarchar29 | ✅ |
| ATTRIBUTE_VARCHAR3 | AttributeVarchar3 | ✅ |
| ATTRIBUTE_VARCHAR30 | AttributeVarchar30 | ✅ |
| ATTRIBUTE_VARCHAR31 | AttributeVarchar31 | ✅ |
| ATTRIBUTE_VARCHAR32 | AttributeVarchar32 | ✅ |
| ATTRIBUTE_VARCHAR33 | AttributeVarchar33 | ✅ |
| ATTRIBUTE_VARCHAR34 | AttributeVarchar34 | ✅ |
| ATTRIBUTE_VARCHAR35 | AttributeVarchar35 | ✅ |
| ATTRIBUTE_VARCHAR36 | AttributeVarchar36 | ✅ |
| ATTRIBUTE_VARCHAR37 | AttributeVarchar37 | ✅ |
| ATTRIBUTE_VARCHAR38 | AttributeVarchar38 | ✅ |
| ATTRIBUTE_VARCHAR39 | AttributeVarchar39 | ✅ |
| ATTRIBUTE_VARCHAR4 | AttributeVarchar4 | ✅ |
| ATTRIBUTE_VARCHAR40 | AttributeVarchar40 | ✅ |
| ATTRIBUTE_VARCHAR5 | AttributeVarchar5 | ✅ |
| ATTRIBUTE_VARCHAR6 | AttributeVarchar6 | ✅ |
| ATTRIBUTE_VARCHAR7 | AttributeVarchar7 | ✅ |
| ATTRIBUTE_VARCHAR8 | AttributeVarchar8 | ✅ |
| ATTRIBUTE_VARCHAR9 | AttributeVarchar9 | ✅ |
| CONSOLIDATE_FLAG | ConsolidateFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MASTER_ATTRIBUTE_ID | MasterAttributeId | ✅ |
| MASTER_CATEGORY | MasterCategory | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_REP_ATRB_ID | TimeRepositoryAttributeId | ✅ |

### [[timerepositoryattributepvo|TimeRepositoryAttributePVO]] (HCM · BICC: 175/175)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | AttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | AttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | AttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | AttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | AttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | AttributeDate15 | ✅ |
| ATTRIBUTE_DATE16 | AttributeDate16 | ✅ |
| ATTRIBUTE_DATE17 | AttributeDate17 | ✅ |
| ATTRIBUTE_DATE18 | AttributeDate18 | ✅ |
| ATTRIBUTE_DATE19 | AttributeDate19 | ✅ |
| ATTRIBUTE_DATE2 | AttributeDate2 | ✅ |
| ATTRIBUTE_DATE20 | AttributeDate20 | ✅ |
| ATTRIBUTE_DATE21 | AttributeDate21 | ✅ |
| ATTRIBUTE_DATE22 | AttributeDate22 | ✅ |
| ATTRIBUTE_DATE23 | AttributeDate23 | ✅ |
| ATTRIBUTE_DATE24 | AttributeDate24 | ✅ |
| ATTRIBUTE_DATE25 | AttributeDate25 | ✅ |
| ATTRIBUTE_DATE26 | AttributeDate26 | ✅ |
| ATTRIBUTE_DATE27 | AttributeDate27 | ✅ |
| ATTRIBUTE_DATE28 | AttributeDate28 | ✅ |
| ATTRIBUTE_DATE29 | AttributeDate29 | ✅ |
| ATTRIBUTE_DATE3 | AttributeDate3 | ✅ |
| ATTRIBUTE_DATE30 | AttributeDate30 | ✅ |
| ATTRIBUTE_DATE31 | AttributeDate31 | ✅ |
| ATTRIBUTE_DATE32 | AttributeDate32 | ✅ |
| ATTRIBUTE_DATE33 | AttributeDate33 | ✅ |
| ATTRIBUTE_DATE34 | AttributeDate34 | ✅ |
| ATTRIBUTE_DATE35 | AttributeDate35 | ✅ |
| ATTRIBUTE_DATE36 | AttributeDate36 | ✅ |
| ATTRIBUTE_DATE37 | AttributeDate37 | ✅ |
| ATTRIBUTE_DATE38 | AttributeDate38 | ✅ |
| ATTRIBUTE_DATE39 | AttributeDate39 | ✅ |
| ATTRIBUTE_DATE4 | AttributeDate4 | ✅ |
| ATTRIBUTE_DATE40 | AttributeDate40 | ✅ |
| ATTRIBUTE_DATE5 | AttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | AttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | AttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | AttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | AttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER21 | AttributeNumber21 | ✅ |
| ATTRIBUTE_NUMBER22 | AttributeNumber22 | ✅ |
| ATTRIBUTE_NUMBER23 | AttributeNumber23 | ✅ |
| ATTRIBUTE_NUMBER24 | AttributeNumber24 | ✅ |
| ATTRIBUTE_NUMBER25 | AttributeNumber25 | ✅ |
| ATTRIBUTE_NUMBER26 | AttributeNumber26 | ✅ |
| ATTRIBUTE_NUMBER27 | AttributeNumber27 | ✅ |
| ATTRIBUTE_NUMBER28 | AttributeNumber28 | ✅ |
| ATTRIBUTE_NUMBER29 | AttributeNumber29 | ✅ |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER30 | AttributeNumber30 | ✅ |
| ATTRIBUTE_NUMBER31 | AttributeNumber31 | ✅ |
| ATTRIBUTE_NUMBER32 | AttributeNumber32 | ✅ |
| ATTRIBUTE_NUMBER33 | AttributeNumber33 | ✅ |
| ATTRIBUTE_NUMBER34 | AttributeNumber34 | ✅ |
| ATTRIBUTE_NUMBER35 | AttributeNumber35 | ✅ |
| ATTRIBUTE_NUMBER36 | AttributeNumber36 | ✅ |
| ATTRIBUTE_NUMBER37 | AttributeNumber37 | ✅ |
| ATTRIBUTE_NUMBER38 | AttributeNumber38 | ✅ |
| ATTRIBUTE_NUMBER39 | AttributeNumber39 | ✅ |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER40 | AttributeNumber40 | ✅ |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | ✅ |
| ATTRIBUTE_ROW_TYPE_ID | AttributeRowTypeId | ✅ |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP11 | AttributeTimestamp11 | ✅ |
| ATTRIBUTE_TIMESTAMP12 | AttributeTimestamp12 | ✅ |
| ATTRIBUTE_TIMESTAMP13 | AttributeTimestamp13 | ✅ |
| ATTRIBUTE_TIMESTAMP14 | AttributeTimestamp14 | ✅ |
| ATTRIBUTE_TIMESTAMP15 | AttributeTimestamp15 | ✅ |
| ATTRIBUTE_TIMESTAMP16 | AttributeTimestamp16 | ✅ |
| ATTRIBUTE_TIMESTAMP17 | AttributeTimestamp17 | ✅ |
| ATTRIBUTE_TIMESTAMP18 | AttributeTimestamp18 | ✅ |
| ATTRIBUTE_TIMESTAMP19 | AttributeTimestamp19 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP20 | AttributeTimestamp20 | ✅ |
| ATTRIBUTE_TIMESTAMP21 | AttributeTimestamp21 | ✅ |
| ATTRIBUTE_TIMESTAMP22 | AttributeTimestamp22 | ✅ |
| ATTRIBUTE_TIMESTAMP23 | AttributeTimestamp23 | ✅ |
| ATTRIBUTE_TIMESTAMP24 | AttributeTimestamp24 | ✅ |
| ATTRIBUTE_TIMESTAMP25 | AttributeTimestamp25 | ✅ |
| ATTRIBUTE_TIMESTAMP26 | AttributeTimestamp26 | ✅ |
| ATTRIBUTE_TIMESTAMP27 | AttributeTimestamp27 | ✅ |
| ATTRIBUTE_TIMESTAMP28 | AttributeTimestamp28 | ✅ |
| ATTRIBUTE_TIMESTAMP29 | AttributeTimestamp29 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP30 | AttributeTimestamp30 | ✅ |
| ATTRIBUTE_TIMESTAMP31 | AttributeTimestamp31 | ✅ |
| ATTRIBUTE_TIMESTAMP32 | AttributeTimestamp32 | ✅ |
| ATTRIBUTE_TIMESTAMP33 | AttributeTimestamp33 | ✅ |
| ATTRIBUTE_TIMESTAMP34 | AttributeTimestamp34 | ✅ |
| ATTRIBUTE_TIMESTAMP35 | AttributeTimestamp35 | ✅ |
| ATTRIBUTE_TIMESTAMP36 | AttributeTimestamp36 | ✅ |
| ATTRIBUTE_TIMESTAMP37 | AttributeTimestamp37 | ✅ |
| ATTRIBUTE_TIMESTAMP38 | AttributeTimestamp38 | ✅ |
| ATTRIBUTE_TIMESTAMP39 | AttributeTimestamp39 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP40 | AttributeTimestamp40 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | ✅ |
| ATTRIBUTE_VARCHAR1 | AttributeVarchar1 | ✅ |
| ATTRIBUTE_VARCHAR10 | AttributeVarchar10 | ✅ |
| ATTRIBUTE_VARCHAR11 | AttributeVarchar11 | ✅ |
| ATTRIBUTE_VARCHAR12 | AttributeVarchar12 | ✅ |
| ATTRIBUTE_VARCHAR13 | AttributeVarchar13 | ✅ |
| ATTRIBUTE_VARCHAR14 | AttributeVarchar14 | ✅ |
| ATTRIBUTE_VARCHAR15 | AttributeVarchar15 | ✅ |
| ATTRIBUTE_VARCHAR16 | AttributeVarchar16 | ✅ |
| ATTRIBUTE_VARCHAR17 | AttributeVarchar17 | ✅ |
| ATTRIBUTE_VARCHAR18 | AttributeVarchar18 | ✅ |
| ATTRIBUTE_VARCHAR19 | AttributeVarchar19 | ✅ |
| ATTRIBUTE_VARCHAR2 | AttributeVarchar2 | ✅ |
| ATTRIBUTE_VARCHAR20 | AttributeVarchar20 | ✅ |
| ATTRIBUTE_VARCHAR21 | AttributeVarchar21 | ✅ |
| ATTRIBUTE_VARCHAR22 | AttributeVarchar22 | ✅ |
| ATTRIBUTE_VARCHAR23 | AttributeVarchar23 | ✅ |
| ATTRIBUTE_VARCHAR24 | AttributeVarchar24 | ✅ |
| ATTRIBUTE_VARCHAR25 | AttributeVarchar25 | ✅ |
| ATTRIBUTE_VARCHAR26 | AttributeVarchar26 | ✅ |
| ATTRIBUTE_VARCHAR27 | AttributeVarchar27 | ✅ |
| ATTRIBUTE_VARCHAR28 | AttributeVarchar28 | ✅ |
| ATTRIBUTE_VARCHAR29 | AttributeVarchar29 | ✅ |
| ATTRIBUTE_VARCHAR3 | AttributeVarchar3 | ✅ |
| ATTRIBUTE_VARCHAR30 | AttributeVarchar30 | ✅ |
| ATTRIBUTE_VARCHAR31 | AttributeVarchar31 | ✅ |
| ATTRIBUTE_VARCHAR32 | AttributeVarchar32 | ✅ |
| ATTRIBUTE_VARCHAR33 | AttributeVarchar33 | ✅ |
| ATTRIBUTE_VARCHAR34 | AttributeVarchar34 | ✅ |
| ATTRIBUTE_VARCHAR35 | AttributeVarchar35 | ✅ |
| ATTRIBUTE_VARCHAR36 | AttributeVarchar36 | ✅ |
| ATTRIBUTE_VARCHAR37 | AttributeVarchar37 | ✅ |
| ATTRIBUTE_VARCHAR38 | AttributeVarchar38 | ✅ |
| ATTRIBUTE_VARCHAR39 | AttributeVarchar39 | ✅ |
| ATTRIBUTE_VARCHAR4 | AttributeVarchar4 | ✅ |
| ATTRIBUTE_VARCHAR40 | AttributeVarchar40 | ✅ |
| ATTRIBUTE_VARCHAR5 | AttributeVarchar5 | ✅ |
| ATTRIBUTE_VARCHAR6 | AttributeVarchar6 | ✅ |
| ATTRIBUTE_VARCHAR7 | AttributeVarchar7 | ✅ |
| ATTRIBUTE_VARCHAR8 | AttributeVarchar8 | ✅ |
| ATTRIBUTE_VARCHAR9 | AttributeVarchar9 | ✅ |
| CONSOLIDATE_FLAG | ConsolidateFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SET_ID | DataSetId | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MASTER_ATTRIBUTE_ID | MasterAttributeId | ✅ |
| MASTER_CATEGORY | MasterCategory | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| TIME_REPORTER_ID | TimeReporterId | ✅ |
| TM_REP_ATRB_ID | TimeRepositoryAttributeId | ✅ |

---

## 📚 Referências

- [Oracle Docs — HWM_TM_REP_ATRBS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepatrbs.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
