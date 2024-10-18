import { type GemData } from "./types";
import { fetchData } from "@services/fetcher";
import GemTable from "./table";

export default async function Page() {
  const gemData = await fetchData<GemData>("gems/summary");

  return (
    <>
      <GemTable gems={gemData}></GemTable>
    </>
  );
}
