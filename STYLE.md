# The style contract

What this book is, who it is for, and the devices every chapter uses. Read
this before writing or revising a chapter. The conventions here are not
suggestions; a chapter that does not follow them is not finished.

## What the book is

A standalone textbook covering the material of MIT's 18.6501x, written so
that a reader never needs the lectures, the slides or anyone's notes open
beside it. The course is where the content came from. It is not a thing the
book refers to.

Concretely, the book does not contain the phrases "the course," "the
slides," "the notes," "the lecture," "unit 2," "the recitation," or any
correction of an error in those materials. It states the mathematics. Where
a convention is one of several in common use (the quantile subscript, the
second parameter of the Gaussian), the book says so as a fact about the
field, not as a fact about a course. Errors found in the source materials
are recorded in NOTES_TO_BOOK.md, which is a working document, not part of
the book.

## Who the reader is

A reader with a solid undergraduate statistics course and a semester of
calculus. Someone who has met the sample mean, the normal distribution,
confidence intervals and t-tests. Every step of a derivation is written out,
and nothing the text relies on is left as an exercise.

**The book never describes its reader as weak in mathematics, never
apologizes for the reader's background, and never tells the reader that
something will not stick.** (The author's instruction, 2026-10-15.) It simply
supplies the steps, the pictures and the reminders. The design below exists
because of who the reader is; the text does not announce it.

Two rules follow from that design:

1. **The limit mathematics stays, all of it.** Nothing is cut for being
   hard. The epsilon-N definition, the proofs of the Weak Law, Slutsky, the
   delta method: all present, all proved.
2. **No chapter after Part II requires the reader to turn back to Part II.**
   Every later use of the Law of Large Numbers, the Central Limit Theorem,
   Slutsky's theorem, the continuous mapping theorem or the delta method
   restates in one line what that theorem gives you, at the point of use,
   with `\recall{...}`.

## The model

Blitzstein and Hwang's *Introduction to Probability* is the target for how
the writing works, with more of everything this reader needs. Their devices,
and how this book uses them:

| Blitzstein device | How this book does it |
|---|---|
| Prose before the formal statement | A definition never opens a section. The question it answers comes first, in words, usually with the concrete case already on the table. |
| Plain terms immediately after a definition | The `inwords` box, mandatory after every definition: the definition read aloud, then what it says for the kiss data. |
| Biohazards for common mistakes | The `pitfall` box. |
| Story proofs (proof by interpretation) | Where a result can be argued in words, the words come first in an `intuition` box and the formal proof follows. The verbal argument is not a substitute for the proof and the book says so where it is not airtight. |
| Intuition boxes with a picture (Pebble World) | The `intuition` box, and a figure wherever the picture is drawable. |
| Strategies and sanity checks | The `sanitycheck` box: how to tell that an answer is absurd without redoing the work. Extreme cases, bounds, units, a second route to the same number. Its optional title is capitalized, since it follows a question mark: `\begin{sanitycheck}[The cost of precision]`. The other boxes take a lowercase title after a colon. |
| Examples revisited later | A running example carried through every chapter, plus named examples picked up again by name. |
| Conversational address | Second person, direct. Rhetorical questions answered on the spot. The voice of the source notes, kept. |
| Flagging dependencies, math appendix | `\toolkit{sec:math-...}` pointers at the step that needs them, to the Mathematical Toolkit in Appendix A. |
| Chapter-end connections | "What comes next" closes every chapter. |

Where this book goes further than Blitzstein, because the reader needs it:

- **Captions name, the text explains.** A caption says what is drawn and
  nothing more: the quantities, the data, which color or line style is
  which, in one to three sentences (about 20 to 35 words; never above 45).
  The explanation, the numbers to notice and the point of the picture go
  in the body paragraph that points to the figure, written so that the
  paragraph and the figure are read together, as Blitzstein does. A reader
  who reads only the caption should know what they are looking at, not
  why it matters. (The author's instruction, 2026-10-15.)
- **More visualization.** Every chapter has figures, and any idea that can
  be drawn is drawn. A result that is only an inequality on a page is a
  result this reader will not hold. Figures are generated, never hand-drawn,
  and obey the figure rules in `scripts/_style.py`.
- **More intuition.** Research it. The best explanation of an idea usually
  exists somewhere outside the source materials, and it is the writer's job
  to find it rather than to paraphrase the lecture.
- **More concrete examples.** Numbers, not symbols, at every stage where a
  number can be computed. An abstract statement followed by no instance of
  it is unfinished.
- **More connections to introductory statistics.** The `bridge` box, "From
  undergraduate statistics," naming what the reader already met and what the
  general version adds. This reader knows more statistics than mathematics,
  so the statistics they already know is the strongest handhold in the book.

## Natural frequencies

Where a probability statement can be restated as a count out of a round
number of repetitions, do it, in the text or in a figure. "A type 1 error
rate of 0.044" is a number this reader can read but not feel. "Of 1,000
studies in which the null is true, about 44 reject it" is the same fact and
it lands. Blitzstein's 10,000-person diagram for the disease-testing problem
is the model.

## Structure

- One chapter per idea, roughly one lecture of the source course, 10 to 18
  pages. Parts are ordered by what must be understood before what, not by
  the course's units.
- Chapters open with the `chaptergoals` box ("In this chapter"), whose last
  sentence connects to the chapter before, and close with "What comes next,"
  a summary and exercises.
- Theorems, definitions and examples are numbered within chapters;
  exercises are numbered within chapters with solutions at the back of the
  book, each exercise printing the page of its solution.
- Every proof is preceded by `\coreproof{...}` or `\optionalproof{...}`: one
  line of strategy, and whether to read it now. About ten proofs in the book
  are core.
- A result stated in a chapter whose proof nothing later needs (Pinsker's
  inequality is the first) is stated where it explains something, with a
  pointer to its proof in Appendix C, Supplementary Proofs. Both the chapter
  and the appendix say explicitly that nothing later depends on it.

## Conventions that do not change

- No em dashes. American spelling.
- Gauss(mu, sigma^2) has the **variance** second. q_alpha has probability
  alpha **above** it. Both are stated on the notation page and explained in
  the Gaussian chapter.
- The running example is the kiss experiment: a 2003 study in Nature
  (Güntürkün, "Adult persistence of head-turning asymmetry") observed 124
  kissing couples in public places, and 80 turned their heads to the right,
  p-hat = 0.645. It is cited as a published study, never as a course's
  example. `\textbf{For the kiss data.}` opens the second half of every
  in-words block.
- No mention of R, Python or any software package by name.
- The words "intercept" and "panel" do not appear in the book's prose as
  trade terms. Say what happened.
- No closing sentence that restates a point as a lesson or a warning. If a
  sentence carries no fact, instruction or number, cut it.
