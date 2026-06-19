# Activation Audit: ship-now

**Issue:** organvm-iv-taxis/.github#6
**Repository:** organvm-iv-taxis/.github
**Date:** 2026-06-18
**Result:** PASS
**Frozen-state classification:** actually-live

## Identity

Canonical org-meta repository for ORGAN-IV (Taxis). It renders the organization
profile README and supplies org-wide community health defaults:

- `profile/README.md`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `.github/ISSUE_TEMPLATE/*`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/dependabot.yml`
- `.github/workflows/*`

## Shipped Test

PASS: `https://github.com/organvm-iv-taxis` serves `profile/README.md`.

## Activation Checks

- Org profile source exists at `profile/README.md`.
- Root README identifies this repo as the canonical ORGAN-IV org-meta repo.
- Community health files exist for conduct, contribution, and security policy.
- Issue templates, PR template, Dependabot config, and three workflows are
  present under `.github/`.
- `seed.yaml` records `promotion_status: PUBLIC_PROCESS` and current validation
  date.

## Governance Outcome

No new cross-organ dependencies or back-edges were introduced. This audit only
records the already-live public GitHub surface and aligns local lifecycle
metadata with the shipped state.
