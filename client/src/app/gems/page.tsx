import { type GemData } from "./types";
import { fetchData } from "@services/fetcher";
import Table from "./table";

export default async function Page() {
  let gemData = await fetchData<GemData>("gems/summary");
  gemData ??= [];

  return (
    <>
      <Table gems={gemData}></Table>
    </>
  );
}
