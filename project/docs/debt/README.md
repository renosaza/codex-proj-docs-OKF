---
type: Reference
status: draft
---

# Technical debt

This template contains no project debt. Use the [debt template](../_templates/debt.md) for a real, consciously accepted compromise and put the record in `items/`.

State why it is tolerated, the safe operating conditions and the exact removal conditions. Say explicitly whether all conditions or any one condition triggers removal. Link relevant tests and evidence. A removal task must reference every required removal condition, rather than copying an incomplete subset. Mark debt `resolved` only when the compromise is actually removed and verified.

Use `debt_status` for the record workflow state; `status` is reserved for OKF document lifecycle (`draft`, `stable`, `deprecated`).
