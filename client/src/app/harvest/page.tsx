import { fetchData } from "@services/fetcher";
import { type TableProps, OverviewTable } from "./table";

export default async function Page() {
  const data = await fetchData<TableProps>("harvest/orbs");

  return (
    <>
      {data ? (
        <div>
          <OverviewTable
            tableProps={data}
            title="Delirium Orbs"
            link=""
          ></OverviewTable>
          <div className="my-5 border-t-2 border-accent-1 bg-black"></div>
        </div>
      ) : null}
    </>
  );
}
