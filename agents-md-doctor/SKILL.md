---
name: agents-md-doctor
description: Audit and systematically improve AGENTS.md instruction systems using text-only evidence from AGENTS.md files and the local instruction documents they directly index. Use when the user asks to inspect, score, diagnose, simplify, deduplicate, reconcile, or optimize AGENTS.md, its routing/index design, or cross-document workflow rules. Checks broken indexes, contradictions, duplication, ambiguity, misplaced scope, non-actionable rules, precedence problems, and unsafe instructions, then proposes minimal diffs without editing by default.
---

# AGENTS.md Doctor

Audit AGENTS.md and its directly indexed local instruction documents as one instruction system. Preserve the author's intent and treat brevity as a means, not a goal.

## Required references

Read these files completely before every audit:

- `references/rubric.md` — issue definitions, severity, exclusions, and scoring
- `references/report-template.md` — required report shape

## Workflow

1. Resolve the audit target.
   - Use the user-specified file or directory.
   - Otherwise use the current working directory.
   - For a directory, recursively discover every file named exactly `AGENTS.md` while excluding `.git`, dependency, cache, and generated-output directories.
2. Read every discovered AGENTS.md with line numbers. Build the directory hierarchy from root to leaf. Treat a parent AGENTS.md as inherited text and a child AGENTS.md as the narrower scope.
3. Build the direct instruction index for each AGENTS.md.
   - Include a local file when AGENTS.md explicitly requires the agent to read, follow, or use it as workflow, policy, rules, or detailed instructions.
   - Resolve relative paths against the directory containing the referencing AGENTS.md. Record the reference location and whether the target exists.
   - Exclude URLs, skill names, source-code imports, examples, assets, output paths, and files mentioned only as data or reference material.
   - Read every existing indexed instruction document completely with line numbers. Stop after this direct layer; do not recursively expand references found only inside indexed documents unless the user requests a wider audit.
4. Build an authority map before scoring: inherited AGENTS.md rules define scope and routing; indexed documents supply the delegated details. Do not assume either silently overrides the other. Require an explicit, conditionally resolvable exception when mandatory rules differ.
5. Run two passes across the full instruction corpus:
   - Mechanical pass: find exact or near duplication, repeated emphasis, repeated precedence declarations, bloated restatements, structurally orphaned rules, broken indexes, and details duplicated between router and delegated document.
   - Semantic pass: find direct contradictions, ambiguous actors/triggers/outcomes, impossible or non-actionable demands, scope leakage, unsafe permissions, unclear parent-child overrides, and unclear router-to-index precedence.
6. Score missing or unreadable directly indexed instruction files as Actionability defects because the mandated route cannot be executed. Put other claims requiring repository evidence under **Needs context verification** without scoring them. This includes whether commands run, architecture descriptions are current, tools are installed, external services exist, or a rule is operationally necessary.
7. Consolidate findings by underlying cause. Assign one primary dimension and one severity to each finding. Never deduct twice for the same problem.
8. Write the findings as JSON to a temporary file and run:

   ```bash
   python3 scripts/score_findings.py findings.json
   ```

   Use the returned scores unchanged. Delete or leave the temporary file outside the audited repository; never add it to the project.
9. Produce the report using `references/report-template.md`. Sort findings by severity, then file path and line number. Include an index-coverage table and the smallest cross-file diff that resolves each finding while preserving rule intent.
10. Stop after the report. Do not edit any audited instruction file unless the user separately confirms the proposed changes.

## Evidence rules

- Base every scored finding only on quoted AGENTS.md text, its inheritance relationships, direct index resolution, and quoted text from directly indexed instruction documents.
- Cite the narrowest useful file and line range.
- Distinguish contradiction from specialization: a child may intentionally narrow a parent rule when the override is explicit.
- Distinguish deliberate delegation from duplication: a short router gate plus operational detail in one indexed document is healthy; repeated operational detail or materially divergent qualifiers are not.
- Do not penalize file length, headings, strong language, duplication, or safety gates merely because they exist. Penalize only the concrete defect defined by the rubric.
- Prefer no finding over a speculative finding. Mark uncertain textual issues as `Needs context verification` rather than lowering the score.
- Never weaken security, authorization, destructive-action, validation, or quality gates just to improve conciseness.

## Modification boundary

Default to report-only behavior. If the user later authorizes edits, apply only the reviewed diffs, preserve unrelated wording, and rerun the full AGENTS.md-plus-index audit to show the before/after scores and remaining findings.
