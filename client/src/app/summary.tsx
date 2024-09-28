import { fetchData } from "@services/fetcher";
import Link from "next/link";
import Image from "next/image";
import { Tooltip } from "@components/tooltip";
import ChaosOrb from "@components/currency";

type Boss = {
  name: string;
  id: string;
  value: number;
  reliable: boolean;
  img: string | null;
};

type Summary = {
  bosses: Boss[];
};

export default async function Summary() {
  let bossInfo = await fetchData<Summary>("summary");
  bossInfo ??= { bosses: [] };

  function Row({ boss }: { boss: Boss }) {
    return (
      <>
        <div className="col-span-2 flex flex-row items-center gap-2">
          {boss.img ? (
            <Image
              src={boss.img}
              alt={boss.name}
              width={32}
              height={32}
              className="h-8 w-8 object-contain"
            />
          ) : null}
          <Link href={`/boss/${boss.id}`} className="truncate hover:underline">
            {boss.name}
          </Link>
          {boss.reliable ? null : (
            <Tooltip>
              <p>Boss contains items with unreliable prices.</p>
              <Link
                href={"/faq"}
                className="text-link hover:underline"
                target="_blank"
              >
                Why?
              </Link>
            </Tooltip>
          )}
        </div>
        <div>{boss.value.toFixed(2)}</div>
      </>
    );
  }

  return (
    <>
      <div className="grid grid-cols-3 gap-2">
        <div className="col-span-2 text-2xl font-bold">Boss</div>
        <div className="flex flex-row gap-2 text-2xl font-bold">
          Profit per kill <ChaosOrb />
        </div>
        {bossInfo.bosses.map((boss) => (
          <Row boss={boss} key={boss.name}></Row>
        ))}
      </div>
    </>
  );
}
