# Report template

Use this structure. Omit empty severity subsections, but never omit the context-verification section.

```markdown
# AGENTS.md instruction-system audit

## Score

**Total: NN/100 — Grade X**

| Dimension | Score |
| --- | ---: |
| Consistency | NN/25 |
| Clarity | NN/20 |
| Conciseness | NN/15 |
| Actionability | NN/15 |
| Scope | NN/15 |
| Safety | NN/10 |

AGENTS.md files audited: `N`  
Directly indexed instruction files audited: `N`  
Mode: Text-only instruction-system audit; source code and business implementation excluded

## Index coverage

| Referencing AGENTS.md | Reference location | Indexed instruction file | Status |
| --- | --- | --- | --- |
| `path/AGENTS.md` | `line` | `path/to/instructions.md` | Present / Missing / Unreadable |

## Findings

### [Severity] AMD-NNN — Short title

- **Location:** `path/AGENTS.md:line`
- **Dimension:** Name
- **Evidence:** “Shortest exact quote that proves the issue.”
- **Why:** Explain the concrete defect and its behavioral consequence.
- **Minimal diff:**

  ```diff
  - old text
  + new text
  ```

Repeat in Critical → High → Medium → Low order. If none, write `No scored textual defects found.`

## Needs context verification

- `path:line` — State exactly what cannot be verified from the audited instruction corpus and why it did not affect the score.
- If none, write `None.`

## Systemic recommendation

State the smallest cross-file improvement, or `No systemic rewrite recommended.`
```

Keep evidence and diffs narrow. Do not rewrite entire files in the report. If several findings share one root cause, report one consolidated finding with all relevant locations and one coherent diff.
