import BossTable from "./table";
import { type BossInfo } from "./types";

export default async function Boss(props: BossInfo) {
  return (
    <>
      <h1 className="mb-2 text-3xl font-bold">{props.name}</h1>
      <BossTable {...props}></BossTable>
    </>
  );
}
