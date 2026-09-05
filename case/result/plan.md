# Case 328 — Skill candidate plan

## Optimization target

Because the original image-derived input does not provide a concrete spending
target, this case evaluates the inferred objective preserved by `aim.txt`:

> Within the 506.2 CNY budget, maximize deterministic yuanbao while keeping
> recharge scheduling compatible with the event window and reward rules.

This is a regression objective, not a claim about the user's true hidden goal.

## Candidate

| Date | Action | Cash (CNY) | Deterministic yuanbao counted |
|---|---|---:|---:|
| 2026-03-28 | 12 CNY week card | 12 | 3,700* |
| 2026-03-29 | 6 CNY regular recharge | 6 | 600 |
| 2026-03-30 | 30 CNY regular recharge | 30 | 9,000 |
| 2026-03-31 | 128 CNY regular recharge | 128 | 25,600 |
| 2026-04-01 | 328 CNY regular recharge, choose +32,800 yuanbao reward | 328 | 98,400 |
| 2026-04-02 | no recharge | 0 | 0 |
| 2026-04-03 | no recharge | 0 | 0 |
| **Total** |  | **504** | **137,300** |

\* The 3,700 week-card value is conditional on purchasing at the start of the
seven-day window and successfully collecting all seven daily claims.

## Accounting

### 328 CNY

```text
32,800 base
+ 32,800 confirmed first-charge bonus
+ 32,800 announcement single-purchase reward (yuanbao option)
= 98,400
```

### 128 CNY

No first-charge bonus is assumed for this tier:

```text
12,800 base
+ 12,800 announcement single-purchase reward
= 25,600
```

### 30 CNY

The input supports the 30 CNY first-charge state:

```text
3,000 base
+ 3,000 first-charge bonus
+ 3,000 daily single-purchase reward
= 9,000
```

### 6 CNY

```text
600 base
```

### Week card

Under the Skill's shared rule and the full-seven-day-claim condition:

```text
3,700 deterministic yuanbao
```

## Recharge progress

Under the Skill's shared week-card rule that the purchase counts toward recharge
progress:

```text
1,200 + 600 + 3,000 + 12,800 + 32,800
= 50,400 recharge-progress yuanbao
```

This crosses the event's 50,000 cumulative-recharge threshold.

The rewards from that threshold are not added to deterministic yuanbao because
they are non-yuanbao items/coupons. Random yuanbao gift bags are also excluded.

## Validation status

| Layer | Status |
|---|---|
| Budget | PASS |
| Deterministic yuanbao arithmetic | PASS |
| Known-action-set finite search | PASS |
| Historical GT arithmetic baseline | PASS |
| Candidate dominates reconstructed GT on cash + deterministic yuanbao | PASS |
| Full week-card collection | CONDITIONAL_PASS |
| Random yuanbao gift-bag expectation | NOT_VERIFIED |
| Historical opaque-action mechanics | NOT_VERIFIED |
| Live-game global optimality | NOT_VERIFIED |
