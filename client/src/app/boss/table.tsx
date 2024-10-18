"use client";

import { useState } from "react";
import { type BossInfo } from "./types";
import { QuestionTooltip, Tooltip } from "@components/tooltip";
import Link from "next/link";
import Image from "next/image";
import ChaosOrb from "@components/currency";
import {
  Table,
  TableHeader,
  TableHeaders,
  TableRow,
  TableRows,
} from "~/components/table";

type SingularItemData = {
  name: string;
  price: number;
  droprate: number | null;
  reliable: boolean;
  trade_link: string | null;
  value: number;
  type: "drop" | "entrance";
  quantity?: number;
  img: string | null;
};

type ItemData = {
  items: SingularItemData[];
  profit: number;
  cost: number;
  total: number;
};

function createItemData(items: SingularItemData[]): ItemData {
  let profit = 0;
  let cost = 0;
  for (const item of items) {
    if (item.type === "drop") {
      profit += item.value;
    } else {
      cost += item.value;
    }
  }
  return { items, profit, cost, total: profit + cost };
}

function parseItems(bossInfo: BossInfo): ItemData {
  const items: SingularItemData[] = [];
  for (const drop of bossInfo.drops) {
    items.push({
      ...drop,
      value: drop.price * drop.droprate,
      type: "drop",
    });
  }
  for (const item of bossInfo.entrance_items) {
    items.push({
      name: item.name,
      price: item.price,
      droprate: null,
      reliable: true,
      trade_link: null,
      value: -item.price * item.quantity,
      type: "entrance",
      quantity: item.quantity,
      img: item.img,
    });
  }
  items.sort((a, b) => b.value - a.value);
  return createItemData(items);
}

function updateItemData(
  itemData: ItemData,
  index: number,
  price: number,
): ItemData {
  const item = itemData.items[index]!;
  item.price = price;
  if (item.type === "entrance") {
    item.value = -price * item.quantity!;
  } else {
    item.value = item.droprate ? item.droprate * price : price;
  }
  return createItemData(itemData.items);
}

function createItemName(item: SingularItemData): string {
  return item.quantity && item.quantity > 1
    ? `${item.name} x${item.quantity}`
    : item.name;
}

export default function BossTable(props: BossInfo) {
  const [itemData, setItemData] = useState<ItemData>(parseItems(props));

  function handlePriceChange(
    event: React.ChangeEvent<HTMLInputElement>,
    index: number,
  ) {
    const v = event.target.value;
    const customPrice = v === "" ? 0 : parseFloat(v);
    if (isNaN(customPrice)) {
      return;
    }
    const newItemData = updateItemData(itemData, index, customPrice);
    setItemData(newItemData);
  }

  function itemRow(data: SingularItemData, index: number): JSX.Element {
    return (
      <TableRow column_sizes={[2, 1, 1, 1, 1]}>
        <div className="flex flex-row items-center gap-2 truncate">
          {data.img ? (
            <Image
              src={data.img}
              alt={data.name}
              width={32}
              height={32}
              className="h-8 w-8 object-contain"
            />
          ) : null}
          {data.trade_link ? (
            <>
              <a
                href={data.trade_link}
                target="_blank"
                rel="noreferrer noopener"
                className="truncate text-link hover:underline"
                title={data.name}
              >
                {createItemName(data)}
              </a>
            </>
          ) : (
            <p className="truncate" title={data.name}>
              {createItemName(data)}
            </p>
          )}
          {data.reliable ? null : (
            <Tooltip>
              <p>Unreliable price.</p>
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
        <input
          title=""
          type="text"
          pattern=""
          value={data.price.toFixed(0)}
          className="h-full w-full rounded border border-accent-2 border-opacity-10 bg-transparent pl-1"
          onChange={(event) => handlePriceChange(event, index)}
        />
        <p>{data.droprate ? `${(data.droprate * 100).toFixed(2)}%` : "N/A"}</p>
        <p>{data.value.toFixed(2)}</p>
        <p>
          {data.type == "drop"
            ? `${((100 * data.value) / itemData.profit).toFixed(1)}%`
            : "N/A"}
        </p>
      </TableRow>
    );
  }

  return (
    <Table>
      <TableHeaders column_sizes={[2, 1, 1, 1, 1]}>
        <TableHeader>
          <p className="truncate">Item</p>
        </TableHeader>
        <TableHeader>
          <p className="truncate">Price</p>
          <ChaosOrb className="-sm:hidden" />{" "}
          <div className="-md:hidden">
            <QuestionTooltip>
              <p>This field is editable!</p>
            </QuestionTooltip>
          </div>
        </TableHeader>
        <TableHeader>
          <p className="truncate">Drop Rate</p>
        </TableHeader>
        <TableHeader>
          <p className="truncate">Value</p>
          <ChaosOrb className="-sm:hidden" />
        </TableHeader>
        <TableHeader>
          <p className="truncate">Profit Share</p>
        </TableHeader>
      </TableHeaders>
      <TableRows column_sizes={[2, 1, 1, 1, 1]}>
        {itemData.items.map((item, i) => itemRow(item, i))}
      </TableRows>
      <div className="mb-2 min-w-full border-b pt-2"></div>
      <TableRows column_sizes={[4, 1, 1]}>
        <div className="col-span-4 font-bold">Total per kill</div>
        <div className="font-bold">{itemData.total.toFixed(2)}</div>
      </TableRows>
    </Table>
  );
}
