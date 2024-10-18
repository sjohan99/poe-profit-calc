import { fetchData } from "@services/fetcher";
import Link from "next/link";
import Image from "next/image";
import { Tooltip } from "@components/tooltip";
import ChaosOrb from "@components/currency";
import {
  Table,
  TableHeader,
  TableHeaders,
  TableRow,
  TableRows,
} from "@components/table";

type Boss = {
  name: string;
  id: string;
  value: number;
  reliable: boolean;
  img: string | null;
};

export default async function Summary() {
  const bossInfo = await fetchData<Boss[]>("bosses/summary");

  function Row({ boss }: { boss: Boss }) {
    return (
      <TableRow column_sizes={[2, 1]}>
        <div className="flex flex-row items-center gap-2 truncate">
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
              <p>
                Boss contains items with unreliable prices.{" "}
                <Link
                  href={"/faq"}
                  className="text-link hover:underline"
                  target="_blank"
                >
                  Why?
                </Link>
              </p>
            </Tooltip>
          )}
        </div>
        <div>{boss.value.toFixed(2)}</div>
      </TableRow>
    );
  }

  return (
    <>
      <Table>
        <TableHeaders column_sizes={[2, 1]}>
          <TableHeader>Boss</TableHeader>
          <TableHeader>
            Profit per kill <ChaosOrb className="-sm:hidden" />
          </TableHeader>
        </TableHeaders>
        <TableRows column_sizes={[2, 1]}>
          {bossInfo.map((boss) => (
            <Row boss={boss} key={boss.id}></Row>
          ))}
        </TableRows>
      </Table>
    </>
  );
}
