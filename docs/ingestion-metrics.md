# Ingestion Pipeline Metrics

Track processing time to measure improvement from tooling enhancements.

## Metrics Log

| Date | Resources | Total Time | Per Resource | Method | Notes |
|------|-----------|------------|--------------|--------|-------|
| 2025-12-21 | 6 | ~45 min | ~7.5 min | Claude Code (manual) | First batch with new workflow. Includes fixing wrong domains/categories. |
| 2025-12-21 | 20 | ~13 min | ~39 sec | Claude Code (manual) | Second batch after workflow established. Parallel extraction. |
| 2025-12-21 | 9 | ~15 min | ~1.7 min | Claude Code (manual) | Third batch. Session continuation. Gemini quota limits on extraction. |

## Baseline

**Before pipeline (manual):** 10-15 min per resource (from `ingestion-pipeline-update.md`)

**Phase 1 target:** 2-3 min per resource

## Method Key

| Method | Description |
|--------|-------------|
| Manual | Copy/paste YAML, no tooling |
| Claude Code (manual) | summarize.sh extraction + Claude Code classification |
| Pipeline (dry-run) | `python ingest.py add --dry-run` |
| Pipeline (auto) | `python ingest.py add --auto-approve` |
| Pipeline (batch) | `python ingest.py batch` |

## Improvement Tracking

| Phase | Enhancement | Expected Impact | Actual Impact |
|-------|-------------|-----------------|---------------|
| 1 | summarize.sh extraction | -50% extraction time | TBD |
| 1 | Duplicate detection | Avoid wasted effort | TBD |
| 1 | Batch mode | Parallel processing | TBD |
| 2 | Context compression | Better accuracy on long articles | TBD |
| 2 | Author enrichment | -80% author research time | TBD |
| 3 | Claude Skill packaging | Single command invocation | TBD |

## Notes

- Time includes: extraction, classification, YAML generation, author creation
- Does not include: review/approval time, commit time
- "Per Resource" = Total Time / Resources processed
