"use client";

import { useState } from "react";
import { type BossInfo } from "./types";
import { QuestionTooltip, Tooltip } from "@components/tooltip";
import Link from "next/link";
import Image from "next/image";
import ChaosOrb from "@components/currency";

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

export default function Table(props: BossInfo) {
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
      <div key={data.name} className="grid grid-cols-6 gap-x-3">
        <div className="col-span-2 flex flex-row items-center gap-2">
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
          className="rounded border border-accent-2 border-opacity-10 bg-transparent pl-1"
          onChange={(event) => handlePriceChange(event, index)}
        />
        <div>
          {data.droprate ? `${(data.droprate * 100).toFixed(2)}%` : "N/A"}
        </div>
        <div>{data.value.toFixed(2)}</div>
        <div>
          {data.type == "drop"
            ? `${((100 * data.value) / itemData.profit).toFixed(1)}%`
            : "N/A"}
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="grid grid-cols-1 gap-2">
        <div className="grid grid-cols-6 gap-x-3">
          <div className="col-span-2 text-xl font-bold">Item</div>
          <div className="flex flex-row gap-2 truncate text-xl font-bold">
            Price <ChaosOrb />{" "}
            <QuestionTooltip>
              <p>This field is editable!</p>
            </QuestionTooltip>
          </div>
          <div className="truncate text-xl font-bold">Drop Rate</div>
          <div className="flex flex-row gap-2 truncate text-xl font-bold">
            Value <ChaosOrb />
          </div>
          <div className="truncate text-xl font-bold">Profit share</div>
        </div>
        {itemData.items.map((item, i) => itemRow(item, i))}
      </div>

      <div className="mb-2 border-b pt-2"></div>
      <div className="grid grid-cols-6 gap-x-3">
        <div className="col-span-4 font-bold">Total per kill</div>
        <div className="font-bold">{itemData.total.toFixed(2)}</div>
      </div>
    </>
  );
}
