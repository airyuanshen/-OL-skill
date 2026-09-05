#!/usr/bin/env python3
"""
Reproduce case 328's known-action-set search.

Scope:
- Budget <= 506.20 CNY.
- Objective: maximize deterministic yuanbao within budget.
- First-charge bonus is assumed available only for 30 CNY and 328 CNY,
  because those are the tiers explicitly supported by input/aim.txt.
- 30 CNY single-purchase +3000 reward: at most once per activity day,
  hence at most 7 rewarded instances.
- 128 CNY single-purchase +12800 reward: cumulative max 7.
- 328 CNY reward: choose +32800 yuanbao; at most one rewarded instance.
- One 12 CNY week card is allowed and is valued at 3700 deterministic yuanbao
  only under the explicit condition that all seven daily claims are available.
- Random yuanbao gift bags are excluded from deterministic yuanbao.
- Historical opaque entries ("28月卡+0.2", "12微信", etc.) are excluded from
  the new-search action set because their mechanics are not verified.

This script proves only optimality inside this declared action model.
It does NOT prove global optimality in the live game.
"""

from dataclasses import dataclass
from typing import List, Tuple

BUDGET_CENTS = 50620

@dataclass(frozen=True)
class Candidate:
    cash_cents: int
    yuanbao: int
    counts: Tuple[int, int, int, int, int, int, int]

def payout(n6, n12, n30, n68, n128, n328, week):
    y = 600*n6 + 1200*n12 + 6800*n68 + 3700*week

    # 30 CNY: base 3000 each; +3000 single reward for up to 7;
    # +3000 first-charge once if at least one 30 CNY recharge exists.
    if n30:
        y += 3000*n30 + 3000*min(n30, 7) + 3000

    # 128 CNY: do NOT assume first-charge availability.
    y += 12800*n128 + 12800*min(n128, 7)

    # 328 CNY: base + confirmed first charge + chosen single reward.
    if n328:
        y += 32800 * 3

    return y

# Action order:
# 6, ordinary 12, 30, 68, 128, 328, week-card 12
costs = (600, 1200, 3000, 6800, 12800, 32800, 1200)
max_counts = tuple(BUDGET_CENTS // c for c in costs)
# Two 328 purchases are already over budget; one week card is the case scope.
max_counts = (
    max_counts[0], max_counts[1], max_counts[2], max_counts[3],
    max_counts[4], 1, 1
)

best: List[Candidate] = []

def dfs(i, counts, spent):
    if i == len(costs):
        c = tuple(counts)
        y = payout(*c)
        best.append(Candidate(spent, y, c))
        return

    cost = costs[i]
    cap = min(max_counts[i], (BUDGET_CENTS - spent) // cost)
    for n in range(cap + 1):
        counts.append(n)
        dfs(i + 1, counts, spent + n*cost)
        counts.pop()

dfs(0, [], 0)

best.sort(key=lambda x: (x.yuanbao, -x.cash_cents), reverse=True)

top = best[0]
expected_counts = (1, 0, 1, 0, 1, 1, 1)

assert top.cash_cents == 50400, top
assert top.yuanbao == 137300, top
assert top.counts == expected_counts, top

labels = ("6", "12", "30", "68", "128", "328", "week-card-12")

print("PASS: known-action-set finite search")
print(f"best cash: {top.cash_cents/100:.2f} CNY")
print(f"best deterministic yuanbao: {top.yuanbao}")
print("counts:", dict(zip(labels, top.counts)))
print()
print("Top 10 candidates:")
seen = set()
rank = 0
for c in best:
    key = (c.cash_cents, c.yuanbao, c.counts)
    if key in seen:
        continue
    seen.add(key)
    rank += 1
    print(rank, f"{c.cash_cents/100:.2f}", c.yuanbao, dict(zip(labels, c.counts)))
    if rank >= 10:
        break
