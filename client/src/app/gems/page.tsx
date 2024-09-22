import { type GemData } from "./types";
import { fetchData } from "@services/fetcher";
import Table from "./table";

export default async function Page() {
  let gemData = await fetchData<GemData>("gems/summary");
  gemData ??= { gems: [] };

  return (
    <>
      <Table {...gemData}></Table>
    </>
  );
}
