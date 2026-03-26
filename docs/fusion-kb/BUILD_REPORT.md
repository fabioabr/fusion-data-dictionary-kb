# Oracle Fusion Data Dictionary — Build Report
Generated: 2026-03-26

## Summary
| Module | HTMLs | Columns | Relationships | SQL Queries | i18n | No Rels | No BP |
|--------|-------|---------|---------------|-------------|------|---------|-------|

| GL | 39 HTMLs | 645 columns | 111 relationships | 86 SQL queries | i18n 100% | 0 no rels | 0 no BP |
| AP | 37 HTMLs | 723 columns | 158 relationships | 56 SQL queries | i18n 100% | 0 no rels | 0 no BP |
| AR | 66 HTMLs | 1390 columns | 298 relationships | 101 SQL queries | i18n 100% | 0 no rels | 0 no BP |
| PO | 148 HTMLs | 2114 columns | 607 relationships | 260 SQL queries | i18n 100% | 2 no rels | 0 no BP |
| HCM | 755 HTMLs | 7574 columns | 1349 relationships | 835 SQL queries | i18n 100% | 22 no rels | 0 no BP |
| **TOTAL** | **1045** | **12446** | **2523** | **1338** | **100%** | | |

## Files without relationships (24)

- PO/po_lookup_codes.html
- PO/pon_neg_team_members.html
- HCM/anc_abs_certifications_f_tl.html
- HCM/hrt_task_obj_relations.html
- HCM/hts_schedules_atrbs_view.html
- HCM/hts_schedules_day_shift_view.html
- HCM/hwm_allocation_rules_f.html
- HCM/hwm_data_source_usages_v.html
- HCM/hwm_fnd_messages_vl.html
- HCM/hwm_tm_event_atrbs.html
- HCM/hwm_tm_opm_meaning_v.html
- HCM/hwm_tm_rep_atrbs.html
- HCM/hwm_tm_rep_msgs.html
- HCM/hxt_sch_prof_default_view.html
- HCM/irc_agent_requisitions.html
- HCM/irc_asmt_acct_packages.html
- HCM/irc_asmt_package_results.html
- HCM/irc_bc_req_sp_assgmnts.html
- HCM/irc_esignatures.html
- HCM/irc_ja_secondary_flows.html
- HCM/irc_lc_actions_tl.html
- HCM/irc_lc_reason_groups_tl.html
- HCM/pay_flow_task_instances.html
- HCM/wlf_pricing_rules_f.html

## Pipeline

Scripts in `scripts/system-docs-generation/`:
1. `extract_json.py` — Extract translatable phrases from .md
2. `translate_json.py` — Translate via Ollama REST API (translategemma:4b)
3. `build_html.py` — Generate HTML from .md + .i18n.json
4. `build_module_index.py` — Generate module index pages

## Technology

- **Content generation:** Claude Opus 4.6 (parallel agents)
- **Translation:** Ollama translategemma:4b (local) + Claude Opus (parallel agents)
- **HTML template:** JS-rendered from DATA object (template_system_doc.html)
- **Design system:** Playground-based (playground.html)
- **i18n:** .i18n.json with {id, br, en, es} + JS runtime lookup