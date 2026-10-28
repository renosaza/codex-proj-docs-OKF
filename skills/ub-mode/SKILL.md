---
name: ub-mode
description: >
  Apply an opt-in, compact engineering workflow to code changes: behavior-first
  TDD when practical, root-cause fixes, and honest quality-gate reporting. Use
  when the user invokes $ub-mode or explicitly asks for these principles on a
  coding task. Do not apply code gates to documentation-only work.
---

# ub-mode

Apply this workflow only when the user invokes `$ub-mode` or explicitly asks for it. Follow higher-priority instructions, repository constraints, and the user's scope. This skill guides code changes; it does not replace other requested modes or require code tooling for documentation-only work.

## Source and adaptation

This is an independently worded adaptation of engineering principles described in the upstream [ub-mode SKILL.md](https://github.com/unclebob/ub-mode/blob/57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f/SKILL.md), pinned to commit `57a8bdd28e45ed41900ace0bafa2ff76dd9ed70f`. It does not reproduce upstream text.

## Make the behavior work

- Understand the relevant call path, inputs, outputs, data shape, and existing contracts before editing. Choose the smallest change that solves the requested problem.
- Prefer a behavior-level test that shows the requested result. When practical, write it first, confirm it fails for the expected reason, then make the smallest change that passes.
- Do not add a contrived test when an honest test is impractical. State why and use the most meaningful available check.
- If the existing design makes the change harder to express, consider the desired end state before extending it. Remove unnecessary complexity before adding more.
- If repeated fixes fail the same check, question the shared assumption and correct the cause before trying another patch. For repetitive work that is not obvious, complete one unit by hand before building a tool to repeat it.
- Fix the cause at the narrowest shared point. Do not scatter guards that only mask the symptom.
- Model important domain rules directly. Validate untrusted data at entry points; use types and idempotent operations where they make the actual code safer. Do not add abstractions or purity rules where the existing code is already clear.

## Make it right

Work in small units and check each unit before moving on. Test behavior a user can observe, not internal implementation details. When refactoring, pin the existing behavior with relevant checks and confirm it remains intact.

Use the following companion gates when they are installed, compatible with the project, and relevant to production code. State the measured task or repository scope in every report.

- **Crapper:** pass requires a reported CRAP score below 10 for every measured function in scope. Report functions at or above 10, and disclose missing or stale coverage data; a scoped run does not establish that the whole repository passes. Split or test a function only when that improves its design and coverage, never just to lower its score.
- **Dryer:** review reported duplication candidates at similarity 0.8 or higher. Read the findings; a successful process exit alone does not prove the duplication gate passed.
- **Mutator:** investigate surviving mutants and uncovered code. Every genuine surviving mutant is a test gap; the gate passes only when no genuine survivors remain unaddressed. Justify and report equivalent or invalid mutants separately. Remove dead code only when evidence shows it is unused.

These tools are separate from this skill. Never install packages or mutate project configuration automatically. If a relevant tool is missing, incompatible, or cannot run, mark its gate as not run and give the reason. Do not claim a clean gate without observed results. For documentation-only changes, use documentation checks instead of these code gates.

## Practice

- Keep a concise task log of meaningful actions and why they were taken. Report it without exposing private reasoning or dumping routine command output.
- Keep delegated context focused and obey repository ownership rules. Use separate worktrees or one writer per shared file when concurrent edits could conflict.
- Check whether generated files and worktrees are safe to remove. Preserve active or uncommitted user work; never treat cleanup as permission to delete it.
- Follow the repository and session policy for commits and pushes. Use the authorized working branch and keep commits scoped. This skill does not authorize switching to `main`, publishing changes, or overriding other safeguards.
- When commits are authorized, keep them small and ordered so each records a clear change and its observed checks.
