# HOOTL

> **Substrate is truth. Supervision is a property of the system, not the loop.**
>
> Eight principles for the safe operation of autonomous AI agent
> systems running in HOOTL posture — Humans Out Of The Loop.

**Read the principles:** [hootl.org](https://hootl.org)
**Status:** v1.0 (June 2026). Concepts document. Not a regulation.

## The thesis

Most AI safety thinking in 2026 stops at the lab. Frontier-lab safety
frameworks — OpenAI's Preparedness, Anthropic's RSP, Google DeepMind's
Frontier Safety Framework — describe what a model developer should do
before releasing a capable model. That work is necessary. It is not
sufficient.

A perfectly evaluated model deployed in a poorly-designed
autonomous-agent runtime is still unsafe. The operator who wraps a
model in a 24/7 autonomous agent has assumed responsibility the lab
cannot discharge for them. The safety stack needs *both* the lab-side
framework *and* the operator-side substrate properties.

HOOTL describes the operator-side layer. Eight properties any system
running autonomously, without per-action human approval, should
exhibit — regardless of which lab's model is inside.

## The eight principles

| | Principle | What the system must exhibit |
|---|---|---|
| **HOOTL-1** | Auditability | A forensic record an outside auditor can read without the agent's help |
| **HOOTL-2** | Verdict Pipeline | An independent verdict gate the authoring agent cannot influence |
| **HOOTL-3** | Override Channel | A substrate intervention path the agent cannot ignore |
| **HOOTL-4** | Boundary Defense | One declared boundary for untrusted input, not per-implementation |
| **HOOTL-5** | Reversibility | Default-reversible actions; irreversibility named and gated |
| **HOOTL-6** | Provenance | Verifiable trail back to goal, constraints, model, and policy — part of the artifact |
| **HOOTL-7** | Falsifiability | Tests the system did not author |
| **HOOTL-8** | Composer Authority | Operator-side accountability for substrate properties |

The principles are numbered for stable citation. The intended use is
*"per HOOTL-3 (Override Channel)"* — write a policy rule, cite the
property.

## What's in this repo

- **`PRINCIPLES.md`** — the full v1.0 text. Eight principles with
  scenarios, the not-this-document framing, and a bibliography.
- **`TAXONOMY.md`** — comprehensive treatment of HITL → HOTL → HOOTL
  with legal, ethical, and commercial implications.
- **`site/`** — Astro source for hootl.org. `cd site && npm run dev`
  for local preview; `npm run build` for static output.

## License

- **Spec and prose** — [CC-BY 4.0](LICENSE). Cite, adapt, extend.
- **Site source** — [MIT](LICENSE-MIT).

## Citation

> Winegar, T. (2026). *Principles of HOOTL Safety* (v1.0). Eight
> substrate-property principles for safe autonomous-agent operation.
> hootl.org.

## Contact

travis@momusdev.com · [GitHub issues](https://github.com/traviswinegar/hootl/issues)
