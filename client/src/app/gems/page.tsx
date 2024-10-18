import { type GemData } from "./types";
import { fetchData } from "@services/fetcher";
import GemTable from "./table";

export default async function Page() {
  let gemData = await fetchData<GemData>("gems/summary");
  gemData ??= [];

  return (
    <>
      <GemTable gems={gemData}></GemTable>
    </>
  );
}
