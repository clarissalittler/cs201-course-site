# CS 201 Course Site Review — July 3, 2026

Full review of all 10 modules (~100 pages), the 7 reference guides, `practice-problems.md`,
and site infrastructure. Every worked example was recomputed; runnable C and assembly
examples were compiled and executed to verify claimed outputs.

Severity: **HIGH** = teaches something false / wrong answer key. **MEDIUM** = misleading,
buggy example, or self-contradiction. **LOW** = typo, polish, cosmetic.

---

## Part A — Errors

### Top-priority fixes (do these first)

1. **M1 (two files): false C23 claim.** `M1 Lesson 5.html` and `Lesson 5 Integer Arithmetic.html`
   both say C23 mandates arithmetic right shift on signed integers. C23 mandates two's-complement
   *representation*, but signed right shift remains **implementation-defined** (§6.5.7); it was
   C++20 that defined it. Fix: "...remains implementation-defined; in practice every mainstream
   compiler performs an arithmetic shift." **HIGH**
2. **M1 Lesson 1 (`M1 Lesson 1.html`): printf specifier mismatch called a compile error.**
   It compiles; it's runtime UB with at most a `-Wformat` warning. **HIGH**
3. **M2 Lesson 4: wrong program output.** The `sum += 0.1f` loop claim "something like
   1000000.125, depending on the system" — actual output is **1087937.0** (verified by running it),
   deterministic on any IEEE 754 system. The real error (~9%) makes the lesson's point *better*.
   "Depending on the system" also contradicts Lesson 5's correct determinism claim. **HIGH**
4. **M2 Lesson 5: underflow example starts on the wrong side of the boundary.**
   `float x = 1.0e-38f; // normalized` — smallest normal float is ≈1.1755e−38, so 1.0e−38 is
   *already* denormal. Use `1.5e-38f` or `0x1p-126f`. **HIGH**
5. **M5 Lesson 6: "waitpid() also picks up stopped or suspended children."** False without
   WUNTRACED — and it contradicts the correct WUNTRACED bullet 15 lines above. **HIGH**
6. **M8 Lessons 7–8: stale cross-references from the reorg.** Lesson 7 says caches were covered
   "in the previous module" (they're Lesson 3 of *this* module); Lesson 8 points to "Lesson 4"
   three times for material that's in Lesson 7, and says "Lessons 1–4" for techniques in 4–7. **HIGH**
7. **M10 Lesson 3: seL4 timing-channel overclaim.** "subsequent work also established ...
   timing-channel bounds" — the seL4 project explicitly states timing channels are *outside* the
   proofs and must be mitigated separately. **HIGH**
8. **practice-problems.md line ~4093: wrong answer key.** "What is the default Linux scheduler?"
   keyed `Completely Fair Scheduler` — the course's own Module 10 lesson says CFS was replaced by
   EEVDF in Linux 6.6 (2023). Reword the stem or re-key. **HIGH**
9. **M7 Lessons 5–6: threaded servers die on SIGPIPE.** Any `write()` to a client that closed the
   connection kills the whole process — for the web server this is routine (browser hits Stop).
   Add `signal(SIGPIPE, SIG_IGN);` (nice callback to Module 5) and mention it in Lesson 5's
   robustness list. **MEDIUM but high practical impact**
10. **Missing images (site-wide check):** `module-02/Lesson 2 IEEE 754...html` references
    `img/floatingpointfields.png`, `img/bitfieldtoexp.png`, `img/exptobitfield.png`, and
    `Lesson 4 Floating Point Rounding.html` references two `Floating Point Rounding_html_*.png` —
    **none exist anywhere in the repo** (they presumably live only on D2L). Broken locally and in
    the compiled course book.

### Module 1 — C and Integer Representations

- **MEDIUM** `Lesson 5 Integer Arithmetic.html`: the `mult/x == y` overflow check called
  "guaranteed to work" — it relies on wrapped signed overflow (UB, per the lesson's own warning
  box) and crashes with SIGFPE for `x=-1, y=INT_MIN` (`INT_MIN / -1`). Present as CS:APP does
  (wrap semantics / unsigned / `-fwrapv`) and point at `__builtin_mul_overflow`.
- **MEDIUM** `M1 Lesson 4.html`: "4-byte port number ... `htonl()`" — ports are 2 bytes
  (`htons()`); `htonl()` is for IPv4 addresses. Students hit this exact distinction in Module 7.
- **MEDIUM** `M1 Lesson 4.html`: "See the diagrams below" — no endianness diagram exists.
- **MEDIUM** `M1 Lesson 4.html`: `showbytes.c` has the int test commented out; the live code only
  prints a string, demonstrating no endianness at all. Uncomment the int case.
- **MEDIUM** `M1 Lesson 6.html`: bit-position text asserts 0-indexing while the table/example use
  1-indexing with `1 << (i-1)`. Self-contradictory; pick one convention.
- **LOW** `M1 Lesson 1.html`: compiles `-o hello`, runs `./prog`.
- **LOW** `M1 Lesson 6.html`: "bit flag (or bit field)" — bit-fields are a different C feature.
- **LOW** `Lesson 4 Type Casting.html`: both extension/truncation figures have the copy-pasted
  caption "from bit pattern to number".
- **LOW** `Lesson 5 Integer Arithmetic.html`: `x == (sum-y)` "can be true even if overflow" —
  it's *always* true in modular arithmetic; the check detects nothing (stronger statement).
- **LOW** `Lesson 3 Signed Integer Encoding.html`: garbled parenthetical in sign-magnitude
  addition steps ("which is the next-to-left-most column").
- Improvements: bound the `scanf("%s")` example (`%199s`) — textbook buffer overflow in a systems
  course; note that `&&`/`||` treat any nonzero as true; mention left-shift-into-sign-bit UB;
  add integer promotions to the conversions list; scope the "same bits, new interpretation"
  casting claim to same-size conversions.

### Module 2 — Floating Point

(All 14 worked IEEE 754 examples in Lesson 3 and both posit examples verified correct.)

- **MEDIUM** Lesson 5: `(3.14 + 1e10) - 1e10 = 0.0` — as double literals the result is ≈3.14;
  only true in single precision. Add `f` suffixes.
- **MEDIUM** Lesson 4: "when the value is clearly closer to one side, all four modes agree" —
  false; the three directed modes ignore closeness entirely.
- **MEDIUM** Lesson 2: "denormalized cases, which are normal numbers at the smallest exponent" —
  denormals are precisely *not* normal numbers; contradicts the lesson's own later text.
- **LOW** Lesson 6: leftover drafting artifact — "`0 10 01 110 --> wait, that's 9 bits!`" followed
  by a recount. Delete the false alarm (it was always 8 bits).
- **LOW** Lesson 1: chapter note says "sections 2.1 to 2.4" — should be 2.4.1 (2.1–2.3 was M1).
- **LOW** Lesson 5: int→float bullet says "23 vs 32 bits"; next paragraph correctly says 24.
  Use 24 vs 31 consistently. Also "at most 1 ulp" → correctly rounded is at most **0.5 ulp**.
- Improvements: fix garbled "between 1 and less than but not equal to 2..." sentence; use
  "binary/radix point" consistently (Overview/Summary already do); note the near-zero failure of
  the relative-epsilon comparison; align quiet-NaN MSB wording between Lessons 2 and 3
  (standardized since IEEE 754-2008); note the 2022 Posit Standard fixes es=2.

### Module 3 — x86-64 Assembly Fundamentals

(No HIGH errors. AT&T syntax consistent throughout; all syscall numbers, arithmetic, and the
GDB↔Lesson 9 line-number correspondence verified. Makefile TABs survive copy-paste.)

- **MEDIUM** Lesson 6: "All arithmetic instructions require a size suffix" — contradicted by the
  lesson's own suffixless `mov`/`add` example; suffix is only required when no register operand
  implies the size.
- **LOW** Lesson 3: "we will address this in Lesson 4 when we learn to print values" — Lesson 4
  prints strings; integer printing arrives in Lesson 9.
- **LOW** Lesson 9: comment "call may clobber %rax" on a *syscall* (the syscall number/return
  clobbers it).
- **LOW** Lesson 10: generic GDB transcript shows `_start` beginning with `push %rbp` (contradicts
  Lesson 1's "no caller"), and the `x/5i` disassembly matches no course program and shows `%eax`
  for a source that writes `%rax`. Regenerate transcripts from the actual compute binary.
- Improvements: **add a syscall-vs-function-convention alert** (args `rdi,rsi,rdx,r10,r8,r9`;
  `syscall` clobbers `rax,rcx,r11`) — the most common student `_start` bug; introduce
  `movz`/`movs`/`cltq` (students see them immediately in `gcc -S` output); avoid the two
  unrelated 60s (result and syscall number) in adjacent lines of the Lesson 6 example; Lesson 9's
  `result` variable is stored but never used.

### Module 4 — Assembly: Control, Functions, Data

(All 8 complete programs assembled and executed; all outputs, struct offsets, flag tables, and
the fib alignment choreography verified correct.)

- **MEDIUM** Lesson 1: `jne less` — a not-equal jump to a label named `less`, in the flagship
  lesson on signed-vs-unsigned jump semantics. Rename the label or use `jl`.
- **MEDIUM** Lesson 6: stack diagram caption says everything below `%rsp` is free "scratch space"
  and everything above "belongs to this function" — both halves wrong (red zone is 128 bytes,
  leaf-only; above %rsp are the *caller's* frames). Directly undermines Lesson 8.
- **LOW** Lesson 1: "the four below" precedes a table of six flags.
- **LOW** Lesson 8: stack canaries "enabled by default in gcc" — upstream gcc doesn't; distro
  builds patch in `-fstack-protector-strong`.
- **LOW** Lesson 8: `movq $0x41414141` comment implies buffer full of A's (stores 4 A's + 4 NULs);
  and the demo runs in `_start`, where `8(%rbp)` is argc, not a return address.
- **LOW** Lesson 2: "gcc uses cmov whenever both branches are simple" — overstated (verified:
  gcc 15 at -Og uses a branch for the Lesson 1 `max`).
- Improvements: connect Lesson 6's `sub $24` leaf-function example to its own alignment section;
  make the Lesson 8 overflow demo *observable* (overwrite a real return address in a called
  function); show the actual jump table for Lesson 4's switch (only gcc comparison with no
  assembly); dead `len:` label in Lesson 7.

### Module 5 — Processes, Signals, Forking

(Exception taxonomy, dispositions, sigprocmask, async-signal-safety all verified correct.
Fork examples compiled and run.)

- **MEDIUM** Lesson 7 Example 1: sample output implies child's `getppid()` always shows the
  parent — parent doesn't wait, so the child is often reparented (reproduced on first run:
  printed the reaper's PID). Add a `wait()` or a note.
- **MEDIUM** Lesson 7 Example 4: "without the early return ... a process that forked at i=2 will
  return 3" — wrong; every process falls through and returns 0 (verified: all 15 children exit 0).
- **MEDIUM** Lesson 7 Example 3: comment "child has exited so this is the parent" — false (the
  lesson's own sample output shows the parent printing first).
- **MEDIUM** Lesson 12 Example 4: "SA_RESTART so sleep() isn't aborted" — SA_RESTART never
  applies to `sleep()`; the while-loop provides correctness. Make that the teaching point.
- **MEDIUM** Lesson 12 Example 3: single shared flag silently drops closely-spaced signals; fine
  for an intro course *if labeled* (one flag per signal fixes it).
- **MEDIUM** Lesson 5: address space "goes (theoretically) to the size of the system's memory" —
  VA size is set by address width, independent of RAM (the whole point of VM); and the
  "two processes map to the same physical location ... this is called virtual memory" paragraph
  states the intended point backwards.
- **LOW/MEDIUM** Lesson 6 execve section: `execve` isn't "a newer variation" (it's *the* syscall;
  `exec*` are wrappers); argv/envp aren't optional; `getenv` doesn't give you the environment
  (that's `environ`).
- **LOW** Lesson 6: wait set = "all children that have terminated" (it's all children); terminated
  by "SIGKILL or SIGINT" (SIGINT is catchable — say "a signal whose default action is terminate,
  uncaught"); waitpid bullet order doesn't match the signature.
- **LOW** Lesson 11: "Example 1 and 2 below" — they're in Lesson 12.
- **LOW** Lesson 5: leftover editorial comment `<!-- [[ should I copy 8.13 ? ]] -->`.
- Improvements: Example 1 produces 7 warnings under `-Wall -Wextra -Wshadow` (unused + shadowed
  variables) — bad pattern to model; cover `sigsuspend` (all examples busy-poll with
  `while(!flag) sleep(1)`); add the classic SIGCHLD + `waitpid(-1,...,WNOHANG)` reaping loop
  (the main real-world payoff, relevant to a shell lab); Summary claims a block-signals-around-
  critical-sections technique no lesson demonstrates.

### Module 6 — Threads and Synchronization

(pthreads signatures correct; all condvar waits properly in `while` loops; producer-consumer,
dining philosophers, and partial-sum arithmetic verified.)

- **MEDIUM** Lesson 2: `perror("pthread_create failed")` — the lesson itself correctly says twice
  that pthreads don't set errno; use `strerror(ret)` as its own Error Handling section shows.
- **MEDIUM** Lesson 6 readers-writers: `printf(... reader_count)` reads `reader_count` without
  the mutex — a textbook data race in the very module that teaches "any race is UB, no
  exceptions." Copy to a local inside the critical section.
- **LOW** Lesson 3: "the actual value is always less than 2,000,000" — overstated, and
  contradicted three paragraphs later ("if every run prints exactly 2000000...").
- **LOW** Lesson 1 fork table: code segment "Copied (copy-on-write)" — text is read-only and
  shared; COW applies to writable segments.
- **LOW** Lesson 2: int↔void* cast is implementation-defined, not UB.
- **LOW** Lesson 6: concurrent `rand()` from worker threads — use `rand_r` or add a caveat.
- Improvements: every compile command uses `-lpthread` while the Overview, Lesson 2, and Summary
  all preach `-pthread` — standardize the examples; `pthread_detach` is recommended but never
  shown; note the dangling-`i` (use-after-scope) strengthening of the loop-variable bug; trylock
  example should check for `EBUSY` specifically; LLNL pthreads tutorial URL has moved.

### Module 7 — File I/O and Sockets

(Content-Length values byte-counted and correct; sockaddr/htons/inet_pton usage verified;
short-read/short-write loops in servers correct.)

- **MEDIUM** Overview: "This module is the capstone of the course" — modules 8–10 follow.
- **MEDIUM** SIGPIPE (see top-priority #9).
- **MEDIUM** The module equates `localhost` with 127.0.0.1 and tests with `nc localhost`, but the
  client's `inet_pton` rejects hostnames — "Invalid address" awaits any student who tries.
  One sentence pointing at `getaddrinfo()` prevents a predictable office-hours question.
- **LOW** Lesson 6: inner write-error `break` exits only the inner loop; outer loop keeps
  writing to a dead socket (Lesson 5's `goto done` pattern is better — the Lesson 6 code
  regressed from it).
- **LOW** Lesson 5: client single-`write`/single-`read` violates the module's own short-count
  rules without a caveat (Lesson 3 has a whole diagram warning about exactly this).
- **LOW** Lesson 5: `getpeername()` unchecked; may print an uninitialized buffer.
- **LOW** Lesson 3: simplified `sockaddr_in` omits `sin_zero` without saying so; "TCP guarantees
  data arrives" → "delivers or reports an error"; syscall called a "context switch" (mode switch).
- Improvements: Lesson 6 defines `parse_request()` then never calls it; the manual write-loop is
  written out in full five times (reuse Lesson 1's `write_all`); `lseek` never mentioned; name
  epoll/event-driven I/O in "What Comes Next".

### Module 8 — Memory Hierarchy and Optimization

(Amdahl arithmetic, gprof columns, struct padding, unroll bounds, blocked-matmul loop bounds,
gcc flag table all verified correct.)

- **HIGH** Stale reorg references (see top-priority #6).
- **MEDIUM** Lesson 7: array accesses "can't be kept in a register so they need to be accessed
  from main memory" — (a) they hit cache, contradicting Lessons 3/8; (b) the real obstacle is
  aliasing, which Lesson 5 explains correctly.
- **MEDIUM** Lesson 8: blocked matmul *accumulates into* `c` while the unblocked version
  overwrites it — not equivalent unless `c` is zeroed. Add the precondition note.
- **MEDIUM** Lesson 7: `n`/`m` silently swap meanings between the bad and good locality snippets,
  and the "stride-n" sentence uses the wrong one.
- **LOW** strlen called N+1 times, not N ("N-1 too many" → "N too many"); SRAM "takes more power"
  than DRAM (dubious — argue area/cost); "each level ~10x larger and 10x slower" contradicted by
  the same diagram's numbers; "tag = 64" in the cache-line diagram (tag is high bits, not the
  byte address); tag mismatch ≠ always a conflict miss; "block of code in memory" → "block of
  memory".
- Improvements: Lesson 1 promises non-volatile storage coverage that never arrives (Overview
  too); add one worked tag/index/offset numeric example (currently outsourced to YouTube while
  the terms are flagged as exam material); "the new switch -Og" (2013); reconcile Lesson 6's
  CPU-time guidance with Lesson 8's wall-clock try-it box; Lesson 7's banner markup is broken
  (`<h1 class="col-12 banner-img">`, no banner image).

### Module 9 — VM, Linking, Dynamic Memory

(Address-translation and all Valgrind byte-count examples verified correct.)

- **MEDIUM** Lesson 1: page-walk cost "five (or six) memory accesses before the data access" —
  a 4-level walk is **four** (five with LA57); five/six is the total *including* the data access.
- **MEDIUM** Lesson 3: heap diagram labels the region *above* the brk line "Heap (grows upward)" —
  that region is unmapped; the heap is below brk.
- **LOW** "brk() or sbrk() system calls" — only `brk` is a syscall; weak-symbol bullet includes
  `.bss` symbols (only COMMON/`.comm` are weak-like — the GCC-10 alert below it is correct);
  Boehm "never incorrectly frees" needs the undisguised-pointer caveat; "loaded into register x".
- Improvements: bridge the two GC-in-C sections (precise vs conservative would otherwise appear
  to contradict); Lesson 3's Valgrind section duplicates the opening third of Lesson 4 — trim to
  a forward reference; consider an x86-64 version of the 32-bit layout figure.

### Module 10 — Kernel Organization

(Syscall numbers, entry mechanics, vectors, CFS→EEVDF, NT 4.0 win32k, Intel ME/MINIX,
Tanenbaum–Torvalds framing all verified correct.)

- **HIGH** seL4 timing channels (top-priority #7).
- **MEDIUM** "MINIX is running on ... far more than Linux" — false (Android alone is 3+ billion
  Linux devices). Drop the comparison.
- **MEDIUM** Mode-switch counting inconsistent between Lessons 2 and 3 (round trip = 1 vs each
  transition counted) — students doing the ×500 ns computation get 2× different answers.
- **LOW** Original L4 was ~6.4 kSLOC assembly compiling to ~12 KB — the lesson conflates the two;
  seL4 "only" verified kernel → "first" (CertiKOS exists); Mach "50–100% slower" is the
  pessimistic tail (25–65% in published measurements); `insmod usb-storage.ko` won't work as
  typed (use `modprobe`); Lesson 1 says page faults were covered in "the previous module on
  memory hierarchy" — the previous module is 9, virtual memory.

### Reference guides (`module-reference/`)

- **No factual errors found**; verified against modules 3, 5–10. Two improvements:
  add a **function-call ABI table** to the `_start` reference (the syscall-vs-`call` 4th-arg
  `r10`/`rcx` confusion is exactly what this page should defuse), and consider a **Modules 1–2
  crib sheet** (integer/IEEE 754) — the one coverage gap, and the most exam-relevant.
- **LOW** Several refs contain raw unescaped `&`/`<` inside `<pre>` code — renders correctly
  today but is invalid HTML and fragile; module-09 files escape correctly.

### practice-problems.md

(All 77 lessons × 4 problems + 10 quizzes present — full coverage. All arithmetic/trace answers
verified correct except the one below.)

- **HIGH** line ~4093: Linux default scheduler keyed `Completely Fair Scheduler`; the course's own
  lesson teaches EEVDF replaced CFS in 6.6.
- **MEDIUM** Five lesson questions repeat verbatim/near-verbatim in the same module's quiz
  (M9 L1 Q2≡Quiz Q2; M9 L5 Q1≡Quiz Q9; M9 L5 Q3≡Quiz Q11; M5 L12 Q4≡Quiz Q14; M7 L2 Q1≡Quiz Q3).
- **MEDIUM** ~15 short-answer keys can't survive the file's own autograding rules (multi-item
  lists with no `|` alternatives, free-form sentence keys, placeholder `%reg`, format mismatches
  between stem and key — lines 976, 1004–1006, 1053, 1072, 1269, 1591, 1608, 1749, 2415, 2981,
  3247, 3347, 3407, 3943, 4035; plus `10,000` vs `10000`, `mark,sweep` spacing, accept `cqo`).
- **MEDIUM** Ambiguous stems: M1 L1 Q3 (pass-by-reference — distractor D is technically true);
  M1 Quiz Q12 self-contradictory wording; M6 L1 Q2 garbled; M3 L8 Q4 offset-numbering convention
  unstated.
- **LOW** M8 L7 Q2 answer literally printed in the stem ("5 x 2 unrolling → `5,2`"); ~10 quiz
  answers leaked by identical adjacent lesson questions; the struct-padding scenario recycled 3×;
  M1 L5 Q3 asks about `sar` before assembly is introduced; quiz lengths uneven (10–15 Q);
  answer keys sit inline in a student-adjacent file — consider a build step that strips
  `**Answer:**` lines for the student-facing export.

---

## Part B — Cross-cutting improvements

1. **Reorg debris.** The re-org left stale artifacts: M8's wrong lesson references, M7's
   "capstone of the course," M10's "previous module on memory hierarchy," M2 L1's chapter note,
   M11 file numbering. Worth a dedicated grep pass for "previous module", "Lesson N", "capstone",
   and chapter/section numbers after any future restructuring.
2. **Shipped drafting artifacts.** Visible: posit lesson's "wait, that's 9 bits!"; Module 1
   Summary's "[link to be added]". Invisible but should be resolved: `<!-- [[ should I copy
   8.13 ? ]] -->` in M5 L5. `cleanup.py` could flag `[[...]]`, "TODO", "[link", "wait,".
3. **Practice-problem iframes are inconsistent** while every Overview says "complete the embedded
   practice problems": missing from M1 L1/L6/L7/L8, M2 L3/L4/L6, M3 L3/L5/L7/L8, M4 L1/L2/L4/L6/
   L8/L9, M5 L1/L2/L4/L8/L11/L12, M8 all-but-L3/L7. Either add sets (L4-rounding, condition
   codes, and stack frames are the highest-value gaps) or reword the Overviews.
4. **Examples that violate the course's own taught rules** — the most damaging pattern for
   students, who copy code: M6 `perror` after pthread_create, M6 readers-writers race,
   M7 unlooped write/read in the client, M5 fork Example 1's shadowed/unused variables.
5. **Accessibility (site-wide).** 45 `<img>` tags missing/empty alt; `alt="banner"` vs `alt=""`
   inconsistent (use `alt=""` for the decorative banner everywhere — cleanup.py could do this);
   load-bearing ASCII diagrams in bare `<pre>` (M4 stack frames, M5 process graphs, M6 deadlock/
   philosophers, M7 handshake, M9 PLT/GOT & heap, M10 syscall path) need a prose alternative or
   `role="img"` + `aria-label`.
6. **Compile-flag consistency.** M6 preaches `-pthread`, demonstrates `-lpthread` everywhere.
   M9 Lesson 4 recommends `-g -O0` for Valgrind; the reference omits `-O0`.
7. **D2L icon images** (`lightbulb.svg`, `books.svg`) 404 locally — `serve.py` strips D2L
   `<link>`/`<script>` but not `<img>` refs. Either vendor the two icons into the repo or extend
   the strip regex.

---

## Part C — Organizational suggestions

1. **Rename module-01 files to match manifest numbering.** `Lesson 1 Integer Data Types.html` is
   manifest Lesson 7 — an editing trap. (Also filename "Unsigned Integer Coding" vs title
   "Encoding".) practice-problems.md numbering follows the manifest, so filenames are the odd
   one out.
2. **Module 1 lesson order:** Lesson 2 (hex) assumes binary fluency that only arrives in Lesson 3;
   swap them or add a binary primer. Lesson 3's title ("Numeric Representation") collides with
   Lesson 2's own H2 and doesn't match its content (information storage / word size / type sizes).
   Lesson 8 (unsigned encoding, 48 lines, no example/diagram/practice) is far thinner than its
   neighbors.
3. **Module 5 is three modules wearing a trenchcoat** (Exceptions L1–4, Processes L5–7, Signals
   L8–12; the Overview admits it merged two former modules). Either add explicit Part A/B/C
   labels for navigation, or consolidate: L1+L2 and L3+L4 merge naturally, L11 is short and its
   examples live in L12 — that's ~9 lessons with no content loss.
4. **Trim superseded redundancy:** M8 L7's "write cache-friendly code" item is fully superseded by
   L8 (the same material is told three times across L2/L7/L8) — cut to a pointer. M9 L3's closing
   Valgrind section duplicates L4's opening. M10 explains CFS→EEVDF twice.
5. **Reference guides:** add the Modules 1–2 crib sheet and the function-call ABI table (Part A).
   The refs' consistent "Common Mistakes Checklist" ending is a strength — keep it.
6. **Content gaps worth one paragraph each:** `sigsuspend` + SIGCHLD reaping pattern (M5, sets up
   a shell lab); `pthread_exit` vs return-from-main and `pthread_detach` (M6); `lseek` (M7);
   `movz`/`movs` (M3); non-volatile storage or drop the promise (M8); worked tag/index/offset
   example (M8).
7. **`old-module-*` directories** (~2.8 MB, 10 dirs) are the pre-reorg content and the likely
   source of the stale cross-references. Once the reorg branch is validated, delete them (git
   history preserves them) so future greps and cleanup.py passes don't match dead content.
8. **Overall sequencing verdict:** sound. Reviewers independently confirmed modules 3, 4, 6, 7,
   8, 10 have logical ordering with clean dependencies and unusually well-maintained
   cross-references (M3's GDB transcript line numbers match M9's source exactly; M4's
   B&O 3.6–3.11 reading maps precisely). The organization problems are local (M1 ordering,
   M5 size, redundancy trims), not structural.

---

## Follow-up fact-check — August 16, 2026

The reworked site received a second content and artifact pass after the July review. Corrections
were applied to the live lesson, summary, reference, and practice-problem sources rather than only
recorded here.

- **C integer semantics:** distinguished hardware wraparound from C signed-overflow undefined
  behavior; corrected negation of the minimum signed value; and described out-of-range signed
  conversions as implementation-defined rather than portable modulo arithmetic.
- **Floating point and posits:** scoped the repeated-addition result to ordinary binary32
  evaluation, qualified tolerance advice and rounding-mode claims, and removed claims that NaN
  encodings are simply wasted or that posit performance is universally superior.
- **Signals and threads:** distinguished standard-signal coalescing from real-time-signal
  queueing, corrected SIGCONT's default action, fixed the SIGCHLD provenance description, and
  replaced `perror` misuse on direct pthread error returns in complete server examples.
- **Memory systems:** corrected DRAM-refresh generalizations, expanded page faults beyond the
  demand-paging-only model, distinguished minor from major faults, and described current Linux
  reclaim and allocator behavior without presenting a teaching implementation as universal.
- **Kernels:** corrected raw syscall error conventions, Linux's CFS-to-EEVDF transition, container
  isolation, eBPF and Rust safety boundaries, and the scope and assumptions of seL4 verification.
  Unsupported absolute IPC timings and several universal claims about microkernels, QNX, CHERI,
  and unikernels were removed or qualified.
- **Verification:** all 105 manifest HTML pages exist; there are no extra module HTML pages, no
  duplicate element IDs, and each page has exactly one H1. The practice bank has 440 questions and
  440 answer entries. Local links and images resolve after URL decoding; generated HTML, EPUB, and
  PDF artifacts were rebuilt from the corrected sources.

Authenticated course-media destinations (for example Panopto or restricted Google Drive items)
still require a signed-in course account for a true permission and playback check. Their presence
and URL shape can be audited locally, but public HTTP validation cannot prove student access.
