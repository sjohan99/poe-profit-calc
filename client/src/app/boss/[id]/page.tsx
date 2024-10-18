import Boss from "../boss";
import { fetchData } from "@services/fetcher";
import { type BossInfo } from "../types";

export default async function Page({ params }: { params: { id: string } }) {
  const bossInfo = await fetchData<BossInfo[]>("bosses/all");
  const boss = bossInfo.find((b) => b.id === params.id);

  return <>{boss ? <Boss {...boss} /> : <h1>Not found</h1>}</>;
}
