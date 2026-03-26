---
id: DOC-HCM-656
doc_type: system-doc
title: "PER_EMAIL_ADDRESSES — Endereços de E-mail"
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
  - emails
  - email-addresses
aliases:
  - PER_EMAIL_ADDRESSES
  - per_email_addresses
  - per-email-addresses
  - endereços-de-e-mail
  - per-email-addresses
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_EMAIL_ADDRESSES

## 📌 Visão Geral

Armazena os **endereços de e-mail** dos colaboradores. Suporta múltiplos endereços por pessoa (corporativo, pessoal, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Comunicação** — endereços de e-mail para contato com colaboradores.
- **Self-service** — e-mail para login e notificações do sistema.
- **Integração** — sincronização com diretórios corporativos (Active Directory, etc.).
- **Relatórios** — distribuição de comunicados por e-mail.
- **Onboarding** — provisionamento de e-mail corporativo.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EMAIL_ADDRESS_ID | NUMBER(18) | NOT NULL | PK | Identificador único do e-mail | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Pessoa associada | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EMAIL_ADDRESS | VARCHAR2(240) | NOT NULL | Dados | Endereço de e-mail | — | 🟢 95% |
| 4 | EMAIL_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo (W1=corporativo, H1=pessoal) | — | 🟢 90% |
| 5 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | E-mail primário (Y/N) | — | 🟢 90% |
| 6 | DATE_FROM | DATE | NULL | Período | Data de início de validade | — | 🟢 85% |
| 7 | DATE_TO | DATE | NULL | Período | Data de fim de validade | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa titular do endereÃ§o de e-mail)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### E-mail corporativo de um colaborador
```sql
SELECT pea.EMAIL_ADDRESS, pea.EMAIL_TYPE
FROM   PER_EMAIL_ADDRESSES pea
WHERE  pea.PERSON_ID = :p_person_id
  AND  pea.EMAIL_TYPE = 'W1'
  AND  pea.PRIMARY_FLAG = 'Y';
```

### Filtros comuns
- `EMAIL_TYPE = 'W1'` — E-mail corporativo
- `PRIMARY_FLAG = 'Y'` — E-mail principal
---

## 🔒 Observações

- Tipos comuns: W1 (Work/Corporativo), H1 (Home/Pessoal).
- O e-mail corporativo (W1) é tipicamente usado para login e notificações do Oracle.
- Dados pessoais — sujeitos a regras de privacidade (LGPD).
---

## 📚 Referências

- [Oracle Docs — PER_EMAIL_ADDRESSES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peremailaddresses.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
