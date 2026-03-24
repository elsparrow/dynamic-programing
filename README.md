# 🏗️ Ball Drop — Minimum Checks Problem
### Dynamic Programming Assignment | Data Structures & Algorithms

---

## 📋 Overview

This project solves the classic **egg drop / ball break** problem using dynamic programming and mathematical optimization. Given a building of `n` floors and `k` balls, the goal is to determine — with the minimum number of floor checks — the exact floor at which a ball will break.

---

## 🧩 Problems Solved

### Question 1 — Minimum Checks with `k` Balls and `n` Floors (`checking_number`)

**Problem:** Given `n` floors and `k` balls, find the minimum number of checks (drops) needed in the worst case to determine the critical floor.

**Approach (Dynamic Programming):**

Instead of the standard top-down DP table approach, this solution uses a bottom-up DP array where `arr[i]` represents the **maximum number of floors** that can be checked using `i` balls and the current number of moves (`counter`).

At each step, the recurrence is:

```
arr[i] = arr[i] + 1 + arr[i-1]
```

This reflects: if we drop ball `i` from a floor and it **breaks**, we can check `arr[i-1]` floors below (with `i-1` balls remaining). If it **doesn't break**, we can check `arr[i]` floors above (with the same `i` balls, one move used). Adding `1` accounts for the current floor itself.

The loop increments `counter` (the number of moves) until `arr[k] >= n`, meaning we can cover all `n` floors.

**Complexity:** `O(counter × k)` where `counter` is the minimum number of moves needed.

---

### Question 2 — Finding the Critical Floor with 2 Balls (`index_floor`)

**Problem:** Given a sorted list of floor-values `F = [s_0, s_1, ..., s_m]` and a ball with breaking threshold `b`, find the smallest `s_i` such that `b < s_i` (i.e., the first floor where the ball breaks).

**Approach:**

With only `k = 2` balls, a pure linear scan wastes the first ball. Instead, the algorithm uses an **optimized two-phase strategy**:

1. **Phase 1 (Ball 1 — Jump Search):** Start at floor index `step - 1` and jump forward by a decreasing step size. The step starts at the value returned by `index_first_floor(n)` and decreases by 1 each jump. This ensures the total number of checks stays minimal.

2. **Phase 2 (Ball 2 — Linear Search):** Once the first ball breaks at some index `curr`, perform a linear scan from the previous safe index (`prev`) up to `curr` to pinpoint the exact breaking floor.

**Complexity:** `O(√n)` — both phases together require at most `O(√n)` checks.

---

### Question 3 — Computing the First Floor to Check (`index_first_floor`)

**Problem:** For `n` floors and 2 balls, what is the optimal starting floor (step size `x`) to begin the jump search?

**Mathematical Derivation:**

With a starting step of `x`, the maximum floors coverable in `x` moves is:

```
x + (x-1) + (x-2) + ... + 1 = x(x+1)/2 ≥ n
```

Solving for `x`:

```
x² + x - 2n = 0
x = ⌈(-1 + √(1 + 8n)) / 2⌉
```

This is implemented directly in `index_first_floor(n)`.

**Complexity:** `O(1)`

---

## 🗂️ File Structure

```
.
├── solution.py          # Main implementation of all three questions
└── dynamic_explanation.pdf  # Handwritten proofs and algorithm explanations (Hebrew)
```

---

## ▶️ How to Run

```bash
python solution.py
```

The `__main__` block runs randomized test cases for all three questions and prints the results.

**Example output:**
```
question 1:
floors: 742
balls: 318
14
question 2:
f1: [12, 23, 45, 56, 67, 78, 89]
b1: 50
ans1: 56
...
```

---

## 📐 Algorithm Summary

| Function | Problem | Strategy | Complexity |
|---|---|---|---|
| `checking_number(n, k)` | Min checks, k balls, n floors | Bottom-up DP | O(counter × k) |
| `index_floor(f, b)` | Find breaking floor, 2 balls | Jump + Linear Search | O(√n) |
| `index_first_floor(n)` | Optimal first floor, 2 balls | Closed-form formula | O(1) |

---

## 📚 Dependencies

- Python 3.x
- Standard library only (`math`, `random`)
