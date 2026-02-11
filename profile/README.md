<div align="center">

[![ORGAN-IV: Taxis](https://img.shields.io/badge/ORGAN--IV-Taxis-e65100?style=flat-square)](https://github.com/organvm-iv-taxis)

# ORGAN-IV: Taxis — Orchestration & Governance

> *τάξις (taxis) — arrangement, order, coordination*
>
> In classical Greek, τάξις denotes the principle of arrangement — the ordering of parts into a functioning whole. In military contexts it described the disposition of troops; in philosophy, the rational structure that gives a system coherence. ORGAN-IV inherits this meaning: it is the layer that arranges, coordinates, and governs the entire eight-organ creative-institutional system.

**5 repositories | ~18,000 words of documentation**

</div>

---

## What This Organ Does

ORGAN-IV is the **nervous system** of the organvm architecture. Where other organs produce theory (I), art (II), commerce (III), public writing (V), community (VI), and distribution (VII), Taxis ensures they work together without collision.

Concretely, ORGAN-IV handles:

- **Cross-organ routing** — directing artifacts, signals, and dependencies between organs
- **Governance enforcement** — maintaining the no-back-edges invariant (I → II → III only; downstream organs never create upstream dependencies)
- **Promotion automation** — managing the state machine that moves repositories through LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED
- **System coordination** — orchestrating multi-agent workflows, deployment pipelines, and launch sequencing
- **Dependency management** — tracking what depends on what across ~80 repositories and 8 organizations

Without Taxis, the eight-organ system would be eight disconnected GitHub organizations. With it, they form a coherent institution.

## Key Repositories

| Repository | Description | Status |
|:-----------|:-----------|:------:|
| **[agentic-titan](https://github.com/organvm-iv-taxis/agentic-titan)** | Polymorphic Agent Swarm Architecture — model-agnostic, self-organizing multi-agent system. The flagship orchestration engine. | Flagship |
| [a-i--skills](https://github.com/organvm-iv-taxis/a-i--skills) | Public skill library — structured capability modules that extend agent workflows across all organs | Documented |
| [universal-node-network](https://github.com/organvm-iv-taxis/universal-node-network) | Distributed node network infrastructure for decentralized system coordination | Documented |
| [petasum-super-petasum](https://github.com/organvm-iv-taxis/petasum-super-petasum) | Meta-layered configuration and abstraction tooling — hat on a hat, recursion made operational | Documented |
| [agent--claude-smith](https://github.com/organvm-iv-taxis/agent--claude-smith) | Agent identity and smithing patterns for Claude-based orchestration workflows | Documented |

## How ORGAN-IV Relates to the Eight-Organ System

The organvm architecture enforces a strict dependency graph across its organs. ORGAN-IV sits at the center of that graph — not as a dependency that other organs import, but as the coordination layer that **observes, routes, and enforces** the rules all organs follow.

Key architectural relationships:

- **ORGAN-I (Theoria)** produces theoretical frameworks. Taxis ensures those frameworks propagate correctly to downstream organs without circular dependencies.
- **ORGAN-II (Poiesis)** and **ORGAN-III (Ergon)** consume upstream theory and art. Taxis enforces the no-back-edges invariant: III never depends on II, II never depends on III.
- **ORGAN-V (Logos)** publishes the public process. Taxis manages the promotion state machine that determines when a repository is ready for public narration.
- **ORGAN-VI (Koinonia)** and **ORGAN-VII (Kerygma)** handle community and distribution. Taxis coordinates launch sequencing so announcements align with actual readiness.
- **Meta-organvm** is the umbrella. Taxis is its operational arm — the organ that makes meta-level governance executable.

## Part of the organvm System

This organization is one of 8 in the [organvm system](https://github.com/meta-organvm):

| Organ | Domain | Organization |
|:------|:-------|:------------|
| I | Theory | [organvm-i-theoria](https://github.com/organvm-i-theoria) |
| II | Art | [organvm-ii-poiesis](https://github.com/organvm-ii-poiesis) |
| III | Commerce | [organvm-iii-ergon](https://github.com/organvm-iii-ergon) |
| IV | **Orchestration** | **[organvm-iv-taxis](https://github.com/organvm-iv-taxis)** |
| V | Public Process | [organvm-v-logos](https://github.com/organvm-v-logos) |
| VI | Community | [organvm-vi-koinonia](https://github.com/organvm-vi-koinonia) |
| VII | Marketing | [organvm-vii-kerygma](https://github.com/organvm-vii-kerygma) |
| VIII | Meta | [meta-organvm](https://github.com/meta-organvm) |

---

<sub>ORGAN-IV: Taxis — orchestration and governance for the eight-organ creative-institutional system | [@4444j99](https://github.com/4444j99)</sub>
