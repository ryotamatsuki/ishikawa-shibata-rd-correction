# Provenance

## Source paper

- Nana Ishikawa and Takashi Shibata (2021), “R&D competition and cooperation with asymmetric spillovers in an oligopoly market,” *International Review of Economics & Finance* 72, 624–642.
- DOI: `10.1016/j.iref.2020.12.016`

## Master audit origin

- Repository: `ryotamatsuki/economic-theory-replication-audit`
- Candidate: `C019`
- Master transition starting commit: `85bb39f5310816d452bc8ca333180f06129e7984`
- Stage 2: independently reconstructed model, reproduced published calibration, confirmed error, supplied admissible counterexample and feasibility/SOC/stability checks.
- Stage 3: `PARAMETER_REGION_CHANGED` + `INTERPRETATION_CHANGED`, severity Level 3; aggregate boundary shown generically gamma- and asymmetry-dependent; positive-measure disagreement established.
- Protocol 05: `CORRECTION_CANDIDATE`, score 12/12; novelty classification `N-A — NO_PRIOR_DISCLOSURE_FOUND_UNDER_PUBLICATION_GRADE_SEARCH`.

## Canonical master evidence paths

- `code/C019_ishikawa_shibata_2021_audit.py`
- `code/C019_stage3_consequence_audit.py`
- `results/C019_stage3_consequence_audit.md`
- `results/C019_protocol05_publication_gate.md`
- `cases/C019_ishikawa_shibata_2021.md`
- `PRIOR_DISCLOSURE_LOG.md`
- `CANDIDATE_REGISTRY.md`

## Dedicated repository transition

- Repository: `ryotamatsuki/ishikawa-shibata-rd-correction`
- Transfer date: 2026-09-01
- Dedicated repository bootstrap commit: `baf2a6140d28f00745db5f38ea3a28b06c918733`
- Stage 0 branch: `stage0/evidence-freeze`
- Assets transferred:
  - Stage-2 independent reconstruction → `code/independent_reconstruction.py`
  - Stage-3 consequence audit → `code/consequence_audit.py`
  - publication-facing claim controls, evidence map, novelty summary, project status and Stage-0 result

## Single-source-of-truth allocation

| Asset | Canonical repository |
|---|---|
| Candidate identity/status | `economic-theory-replication-audit` |
| Stage 2 audit history | `economic-theory-replication-audit` |
| Stage 3 consequence history | `economic-theory-replication-audit` |
| Protocol 05 gate history | `economic-theory-replication-audit` |
| Publication-facing derivation | `ishikawa-shibata-rd-correction` |
| Manuscript | `ishikawa-shibata-rd-correction` |
| Manuscript figures/tables | `ishikawa-shibata-rd-correction` |
| Submission files | `ishikawa-shibata-rd-correction` |
| Journal correspondence metadata | `ishikawa-shibata-rd-correction` |

The master repository remains the immutable audit-history source. After Stage 0 is merged, publication-facing assets are edited only in the dedicated repository; the master repository should cross-reference rather than duplicate manuscript development.
