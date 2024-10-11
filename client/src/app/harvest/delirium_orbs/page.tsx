import { fetchData } from "@services/fetcher";
import { type TableProps, FullTable } from "../table";
import ProfitInfo from "../profit-info";

export default async function Page() {
  const data = await fetchData<TableProps>("harvest/orbs");

  return (
    <>
      {data ? (
        <>
          <ProfitInfo></ProfitInfo>
          <FullTable {...data}></FullTable>
        </>
      ) : null}
    </>
  );
}
