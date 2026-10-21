# Methodology

This document describes the experimental methodology of the benchmark. It
covers the overall pipeline, the two specification-generation strategies, the
parameters of the experiment, the metrics used, and the reproducibility
guarantees.

---

## 1. Overview

The experiment evaluates how accurately LLM-generated specifications capture
the behavioural requirements of natural-language programming tasks, and how
effectively those specifications detect incorrect implementations.

The pipeline consists of six stages:

1. Natural-language description
2. LLM (strategy A or B)
3. Generated specification
4. Run against implementations
5. Accept / Reject verdict
6. Compare with hidden tests
7. Metrics

For each task, the pipeline is executed once per (strategy, model, sample)
combination.

---

## 2. Research Questions

**RQ1.** How accurately do LLM-generated preconditions and postconditions
capture the behavioural requirements expressed in natural-language programming
tasks?

**RQ2.** How effectively do these specifications detect incorrect
implementations?

Each metric maps to one of the research questions:

| Metric | Research question |
|---|---|
| Valid specifications % | RQ1 |
| Requirement coverage | RQ1 |
| False rejection | RQ2 |
| False acceptance | RQ2 |
| Mutation score | RQ2 |
| Agreement with hidden tests | RQ2 |
| Cost | Control |
| Execution time | Control |

---

## 3. Specification Strategies

Two LLM-based strategies are compared. Both use the same natural-language
description as input; they differ only in the format of the requested output.

### Strategy A — Executable assertions

The prompt asks the model to generate Python `assert` statements expressing:

- preconditions — conditions on the function's inputs;
- postconditions — conditions on the function's output;
- invariants — properties that must always hold.

The output must be executable Python code without explanations. The checkers
are named `check_preconditions` and `check_postconditions`.

### Strategy B — Property-based tests

The prompt asks the model to generate property-based tests using the
`hypothesis` library. Each property must be independently runnable and must
satisfy any correct implementation of the function.

The output must be executable Python code that imports `hypothesis` and the
function under test as `func`.

Both prompts are stored in the `prompts/` directory:

- `prompts/strategy_a_asserts.txt`
- `prompts/strategy_b_pbt.txt`

---



## 4. Benchmark Structure

Each task is described by a JSON file in the `tasks/` directory and follows
the schema defined in `tasks/_schema.json`. A task contains:

- `id` — unique identifier (T01 … T40);
- `domain` — game domain (tic-tac-toe, chess, snake, 2048, …);
- `title` — short task title;
- `signature` — Python function signature;
- `nl_description` — natural-language description;
- `requirements` — list of atomic behavioural requirements (R1 … Rn);
- `correct_impls` — paths to correct implementations;
- `faulty_impls` — paths to faulty implementations, split into
  `hand_written` and `mutants`;
- `hidden_tests` — path to hidden reference tests.

The directory layout is:

```
tasks/          task descriptions in JSON
impl/TXX/       correct and faulty implementations
tests_hidden/   hidden reference tests (used only for evaluation)
prompts/        prompts for strategies A and B
specs/raw/      raw LLM output
specs/parsed/   cleaned executable specifications
harness/        evaluation scripts
results/        metric tables and figures
```


---

## 5. Implementations and Faults

For each task, the benchmark provides:

- **Correct implementations.** At least one correct implementation per task;
  the pilot tasks use two.
- **Hand-written faults.** Two or three faults per task, representing typical
  human errors (off-by-one, missing boundary checks, wrong return values).
- **Mutation-generated faults.** Produced automatically by Cosmic Ray from a
  correct implementation. Mutants that pass all hidden tests are treated as
  equivalent and excluded from the evaluation.
- **Hidden reference tests.** Written under the requirements R1 … Rn, used
  only for evaluation, never shown to the LLM.

---

## 6. Evaluation Procedure

For each (task, strategy, model, sample), the procedure is:

1. Load the task JSON.
2. Build the prompt from `nl_description` and `signature`.
3. Call the LLM with the fixed parameters.
4. Parse the raw output into an executable specification.
5. If parsing fails, mark the specification as invalid.
6. Run the specification against every correct implementation.
7. Run the specification against every faulty implementation.
8. Record the accept/reject verdict for each implementation.
9. Compare the verdicts with the hidden tests.
10. Compute the metrics.

Execution is isolated in a sandbox with a timeout to prevent hanging or
malicious code from affecting the harness.

---


---

## 7. Threats to Validity

- **Construct validity.** The requirement list is written by the author; a
  different annotator might extract different requirements.
- **Internal validity.** Mutation-generated faults may include equivalent
  mutants; these are filtered out by hidden tests.
- **External validity.** The benchmark covers small, self-contained Python
  tasks; results may not transfer to larger codebases.
- **Conclusion validity.** LLM outputs are stochastic; three samples reduce
  but do not eliminate variance.

---


### Methodological Clarifications

**1. Distinguishing executable from semantically correct specifications**

An executable specification is code that simply runs without syntax errors (for example, `assert isinstance(result, bool)`). A semantically correct specification is code that actually verifies the logic of the task and can distinguish correct implementations from faulty ones.

In practice, we distinguish them by running the generated specifications against both correct implementations and faulty implementations. If a specification runs successfully but accepts a faulty implementation, it is executable but semantically weak. We measure this through the False Acceptance metric.

**2. Assessing requirement coverage**

Requirement coverage is a metric showing how many of the task requirements (R1, R2, R3...) are actually reflected in the generated specification.

*Note:* However, I have some concerns regarding this metric. Since it requires manual assessment by two annotators, it is highly subjective and difficult to scale to 40 tasks. I am not entirely sure if this metric is strictly necessary for the final evaluation, or if we should prioritize automated metrics like Mutation Score and False Acceptance instead. I would appreciate your advice on whether to keep it or simplify it.

**3. Generating test inputs for the two strategies**

Since we have two different specification-generation strategies, the test inputs are generated differently:

- **For Strategy B (Property-based tests / Hypothesis):** Test inputs are generated automatically by the `hypothesis` library. It creates thousands of random inputs (lists, numbers, matrices) and checks if the properties hold.
- **For Strategy A (Executable assertions):** The specification only contains `assert` checks. To run them, we will write a harness script that generates random inputs based on the function signature (using Python's `random` module) and passes them to the `check_preconditions` and `check_postconditions` functions.