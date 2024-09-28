import { type ReactNode } from "react";

function Question({
  question,
  children,
}: {
  question: string;
  children: ReactNode;
}) {
  function createId() {
    const q = question.replace(/[^a-zA-Z ]/g, "");
    return q.toLowerCase().replace(/ /g, "-");
  }

  return (
    <div className="flex flex-col gap-2" id={createId()}>
      <h2>{question}</h2>
      {children}
    </div>
  );
}

export default function HomePage() {
  return (
    <main className="flex max-w-3xl flex-col gap-5">
      <Question question="How are boss profits calculated?">
        <p>
          The &quot;value&quot; of a boss is the average profit per kill. It is
          calculated as follows:
        </p>
        <p>Item Value = Price * Droprate</p>
        <p>Boss Value = Sum of all Item Values - Entry Cost</p>
      </Question>
      <Question question="How are gem profits calculated?">
        <span>
          The &quot;Level profit&quot; is the price-difference between the game
          at level 1 and its max (uncorrupted) level.
          <p>
            &quot;Level + Corrupt&quot; is the expected profit from levelling a
            gem from level 1 and corrupting a gem from.
          </p>
          <p>
            &quot;Level + Quality + Corrupt&quot; is the expected profit from
            levelling a gem from level 1, making it 20% quality, and then
            corrupting it.
          </p>
        </span>
      </Question>
      <Question question='What is "Experience Adjusted Profits?"'>
        <p>
          This makes the profit normalized with respect to the required
          experience to level a gem to max level. Awakened and exceptional gems
          generally are more profitable to level at a per gem basis, however
          they also require around 5x more experience to reach max level
          compared to a normal / transfigured gem.
        </p>
      </Question>
      <Question question='Why are some bosses and items marked with "unreliable prices?"'>
        <p>
          All prices for this project are pulled from{" "}
          <a
            href="https://poe.ninja"
            target="_blank"
            rel="noreferrer noopener"
            className="truncate text-link hover:underline"
            title="poe.ninja"
          >
            poe.ninja
          </a>
          . Some items are not priced correctly due to them not being priced as
          unidentified (i.e. Sublime Vision) and/or where there are multiple
          versions of the same item (i.e. Watcher&apos;s eye).
        </p>
        <p>
          This can lead to wildly inaccurate prices. As of writing Sublime
          Vision is priced as 130c when it is actually 14000c. To combat this
          I&apos;ve marked all such items as unreliable and added a trade-link
          to the item and possibility to (locally) update the price of the items
          by editing the price in the price column.
        </p>
      </Question>
    </main>
  );
}
