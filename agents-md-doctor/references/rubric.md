# Audit rubric

## Contents

1. Scoring model
2. Severity
3. Dimensions
4. Exclusions
5. Finding data

## Scoring model

Start each dimension at its maximum and subtract each finding once from its primary dimension:

| Dimension | Maximum |
| --- | ---: |
| Consistency | 25 |
| Clarity | 20 |
| Conciseness | 15 |
| Actionability | 15 |
| Scope | 15 |
| Safety | 10 |

Use fixed deductions: Critical `10`, High `6`, Medium `3`, Low `1`. Floor each dimension at zero. The total is the sum of the six dimensions.

Grades: A `90–100`, B `80–89`, C `70–79`, D `60–69`, F `<60`.

Assign one primary dimension per underlying problem. Mention secondary effects without further deductions. Use a stable fingerprint to merge repeated manifestations of the same root cause.

## Severity

- **Critical**: The text authorizes destructive, secret-exposing, or permission-expanding behavior without a meaningful boundary; or two mandatory rules make safe compliance impossible.
- **High**: A direct mandatory-rule conflict, missing precedence that changes required behavior, or a pervasive defect likely to misdirect many tasks.
- **Medium**: A localized ambiguity, duplication cluster, misplaced rule, or non-actionable demand that creates recurring friction.
- **Low**: A narrow wording or structure defect with small but real interpretation cost.

Severity reflects textual impact, not how easy the edit is.

## Dimensions

### Consistency — 25

Score defects when the text itself proves:

- Directly incompatible requirements under the same condition.
- A parent and child impose incompatible rules without an explicit, resolvable override.
- An AGENTS.md router and its directly indexed instruction document impose incompatible mandatory rules without an explicit, resolvable exception.
- Multiple precedence declarations disagree.
- Exact or near-duplicate rules diverge in a material qualifier.

Do not flag compatible elaboration or an explicit narrower exception.

### Clarity — 20

Score defects when a rule leaves a material textual ambiguity:

- Undefined actor or referent such as “it”, “the standard”, or “normal cases” with multiple plausible meanings.
- Missing trigger, target, threshold, or outcome where the omission changes behavior.
- Terms like “appropriate”, “high quality”, “when needed”, or “optimize” without a local decision criterion.
- Dense combinations of unrelated obligations that admit multiple parses.

Do not require definitions for ordinary language with only one reasonable reading.

### Conciseness — 15

Score defects only when text cost is avoidable:

- The same instruction is repeated without adding scope, exception, rationale, or precedence.
- Emphasis markers or absolute words are stacked without changing meaning.
- A long explanation restates a rule instead of supplying a decision criterion.
- Specialized procedure is duplicated across several nested files instead of inherited once.
- Operational detail is duplicated between an AGENTS.md router and its delegated instruction document without adding a gate, exception, rationale, or precedence.

Never deduct solely for line count, detailed safety gates, examples that disambiguate behavior, or necessary rationale.

### Actionability — 15

Score defects when the instruction cannot guide a concrete decision from its own wording:

- It states an aspiration but no observable behavior or completion condition.
- It demands an absolute result that no agent can guarantee, such as “never make mistakes”.
- It requires mutually dependent approval or completion states with no exit path.
- It orders an action but omits which artifact, event, or result the action applies to.
- It mandates reading or following a local instruction file that is missing, unreadable, or not resolvable from the referencing AGENTS.md.

Do not test commands or non-index data paths. Directly indexed local instruction paths are part of the instruction contract and must be resolved.

### Scope — 15

Score defects visible from AGENTS.md placement, inheritance, and direct router-to-index delegation:

- A root rule claims to apply only to a named subtree while duplicating or conflicting with that subtree's file.
- A child repeats inherited rules without narrowing, replacing, or explaining them.
- An override does not identify what parent rule it replaces or the conditions of replacement.
- A rule names several scopes but leaves their precedence unresolved.
- A router delegates details to an indexed document but both retain overlapping operational ownership without a clear boundary.

Do not infer intended ownership from repository code. Use only the AGENTS.md hierarchy, explicit routing language, and indexed instruction text.

### Safety — 10

Score only explicit textual hazards:

- Unbounded deletion, overwrite, credential access, network publication, or external side effects.
- Instructions to bypass confirmation, sandboxing, authorization, validation, or secret protections.
- Secret values embedded directly in the instruction text.
- Permission expansion without target, purpose, or approval boundary.

Do not penalize references to secret names, environment-variable names, external paths, or security procedures by themselves.

## Exclusions

Put these under **Needs context verification** and assign no deduction:

- Whether a command, package, service, model, tool, source file, asset, output path, or non-index reference exists.
- Whether architecture, workflow, ownership, or version claims are current.
- Whether a rule matches actual team practice or is operationally necessary.
- Whether examples are technically correct outside the instruction text.
- Whether an instruction improves model performance in practice.

Do not read source code, assets, generated outputs, or general repository files to resolve these questions. This exclusion does not apply to local instruction documents directly indexed by AGENTS.md; resolve and read those as required audit evidence.

## Finding data

Before scoring, represent each scored finding as:

```json
{
  "id": "AMD-001",
  "fingerprint": "short-stable-root-cause",
  "dimension": "consistency",
  "severity": "high",
  "file": "AGENTS.md",
  "lines": "12-18",
  "evidence": "Exact quoted text",
  "reason": "Why this meets the rubric",
  "fix": "Smallest intent-preserving change"
}
```

Use dimensions `consistency`, `clarity`, `conciseness`, `actionability`, `scope`, or `safety`; severities `critical`, `high`, `medium`, or `low`.
