# CASE REPORT — 328 regression

## Executive result

For the declared known-action model, `sgs-recharge-advisor` identifies:

```text
Historical reconstructed GT:
506.2 CNY -> 136,100 deterministic yuanbao

Skill candidate:
504.0 CNY -> 137,300 deterministic yuanbao
```

Difference:

```text
cash:     -2.2 CNY
yuanbao:  +1,200
```

The candidate therefore **strictly dominates the reconstructed historical GT**
on both recorded cash and deterministic yuanbao.

## Why this case matters

This regression exercises several failure modes that a weaker planner can get
wrong:

1. **Do not interpret every "double/triple" description as first-charge.**
   The 30 CNY and 328 CNY results must be decomposed into base, first-charge,
   and announcement single-purchase reward.

2. **Do not delete repeated 30 CNY recharges after first-charge is consumed.**
   The announcement's +3000 single-purchase reward is independently available
   once per day.

3. **Do not reuse historical opaque actions as if their mechanics were known.**
   `28月卡+0.2元` and `12微信` remain historical observed atoms.

4. **Do not add random yuanbao gift bags to deterministic balance.**
   The notice's displayed gift-bag probabilities sum to only 95%, so a complete
   mathematical expectation is not established by the supplied source.

5. **Use finite search rather than local intuition.**
   The winning combination is not simply "repeat the best-looking recharge":
   it is 328 + 128 + 30 + week-card 12 + regular 6 within the declared model.

6. **Preserve uncertainty.**
   The case passes known-action-set optimality but explicitly refuses to upgrade
   that result to live-game global optimality.

## Reproducibility

Run:

```bash
python tools/verify_case.py
```

Expected headline:

```text
PASS: known-action-set finite search
best cash: 504.00 CNY
best deterministic yuanbao: 137300
```

## Interpretation

This case is **positive regression evidence** for Skill v1.0.0.

It demonstrates that, on this historical sample, the Skill's rules lead to:

- conservative evidence handling;
- correct reward-source separation;
- an auditable finite-search result;
- a candidate that improves on the preserved GT;
- and correct use of `NOT_VERIFIED` where the evidence is incomplete.

One regression case does not by itself prove universal reliability. The intended
use is to keep this case in the repository and rerun it after Skill changes.
