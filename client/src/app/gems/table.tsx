"use client";

import { useMemo, useState } from "react";
import { type GemData, type Gem } from "./types";
import Image from "next/image";
import ChaosOrb from "@components/currency";

type Sorting = {
  field: keyof Omit<Gem, "name" | "gem_type" | "img">;
  order: "asc" | "desc";
  showAdjusted: boolean;
  showAwakened: boolean;
  showTransfigured: boolean;
};

function renderField(f: number | null): string {
  if (f === null) {
    return "N/A";
  }
  return f.toFixed(1);
}

function sortGems(gems: Gem[], sorting: Sorting): Gem[] {
  return gems.sort((a, b) => {
    if (sorting.order === "asc") {
      return a[sorting.field]! - b[sorting.field]!;
    } else {
      return b[sorting.field]! - a[sorting.field]!;
    }
  });
}

function filterGems(gems: Gem[], sorting: Sorting): Gem[] {
  return gems.filter((gem) => {
    if (!sorting.showAwakened && gem.gem_type === "awakened") {
      return false;
    }
    if (!sorting.showTransfigured && gem.gem_type === "transfigured") {
      return false;
    }
    return true;
  });
}

type CheckBoxProps = {
  checked: boolean;
  onChange: () => void;
  id: string;
  label?: string;
};

function CheckBox({ checked, onChange, id, label }: CheckBoxProps) {
  return (
    <div className="flex items-center">
      <input
        id={id}
        type="checkbox"
        className="h-5 w-5 rounded border-orange-600 bg-secondary-1 text-background"
        checked={checked}
        onChange={onChange}
      />
      {label && (
        <label
          htmlFor={id}
          className="ms-2 cursor-pointer text-lg font-medium text-secondary-2"
        >
          {label}
        </label>
      )}
    </div>
  );
}

export default function Table({ gems }: GemData) {
  const [pageSize, setPageSize] = useState(15);
  const [sorting, setSorting] = useState<Sorting>({
    field: "level_profit",
    order: "desc",
    showAdjusted: false,
    showAwakened: true,
    showTransfigured: true,
  });

  const sortedGems = useMemo(() => {
    return sortGems(filterGems(gems, sorting), sorting);
  }, [gems, sorting]);

  function sortBy(field: keyof Omit<Gem, "name" | "gem_type" | "img">) {
    if (sorting.field === field) {
      setSorting({
        ...sorting,
        order: sorting.order === "desc" ? "asc" : "desc",
      });
    } else {
      setSorting({
        ...sorting,
        field: field,
        order: "desc",
      });
    }
  }

  function toggleAwakened() {
    setSorting({
      ...sorting,
      showAwakened: !sorting.showAwakened,
    });
  }

  function toggleTransfigured() {
    setSorting({
      ...sorting,
      showTransfigured: !sorting.showTransfigured,
    });
  }

  function toggleAdjusted() {
    let field = sorting.field;
    const showAdjusted = !sorting.showAdjusted;
    if (showAdjusted) {
      if (field === "level_profit") {
        field = "xp_adjusted_level_profit";
      } else if (field === "level_c_profit") {
        field = "xp_adjusted_c_profit";
      } else if (field === "level_q_c_profit") {
        field = "xp_adjusted_q_c_profit";
      }
    }
    if (!showAdjusted) {
      if (field === "xp_adjusted_level_profit") {
        field = "level_profit";
      } else if (field === "xp_adjusted_c_profit") {
        field = "level_c_profit";
      } else if (field === "xp_adjusted_q_c_profit") {
        field = "level_q_c_profit";
      }
    }
    setSorting({
      ...sorting,
      field: field,
      showAdjusted: showAdjusted,
    });
  }

  function Row(props: { gem: Gem }): JSX.Element {
    const { gem } = props;
    return (
      <div className="grid grid-cols-5 gap-x-3">
        <div className="col-span-2 flex flex-row items-center gap-2">
          {gem.img ? (
            <Image
              src={gem.img}
              alt={gem.name}
              width={32}
              height={32}
              className="h-8 w-8 object-contain"
            />
          ) : null}
          <p className="truncate" title={gem.name}>
            {gem.name}
          </p>
        </div>
        {sorting.showAdjusted ? (
          <RowAdjustedProfit gem={gem} />
        ) : (
          <RowPureProfit gem={gem} />
        )}
      </div>
    );
  }

  function RowPureProfit({ gem }: { gem: Gem }) {
    return (
      <>
        <div>{renderField(gem.level_profit)}</div>
        <div>{renderField(gem.level_c_profit)}</div>
        <div>{renderField(gem.level_q_c_profit)}</div>
      </>
    );
  }

  function RowAdjustedProfit({ gem }: { gem: Gem }) {
    return (
      <>
        <div>{renderField(gem.xp_adjusted_level_profit)}</div>
        <div>{renderField(gem.xp_adjusted_c_profit)}</div>
        <div>{renderField(gem.xp_adjusted_q_c_profit)}</div>
      </>
    );
  }

  return (
    <div className="flex flex-col gap-y-2">
      <p className="text-lg text-secondary-2">Options:</p>
      <div className="flex flex-col items-start gap-y-2">
        <CheckBox
          id="useExperienceAdjustedProfits"
          checked={sorting.showAdjusted}
          onChange={() => toggleAdjusted()}
          label="Use Experience Adjusted Profits"
        />
        <CheckBox
          id="showAwakenedGems"
          checked={sorting.showAwakened}
          onChange={() => toggleAwakened()}
          label="Show Awakened Gems"
        />
        <CheckBox
          id="showTransfiguredGems"
          checked={sorting.showTransfigured}
          onChange={() => toggleTransfigured()}
          label="Show Transfigured Gems"
        />
      </div>
      <div className="grid grid-cols-1 gap-2">
        <div className="grid grid-cols-5 gap-x-3">
          <div className="col-span-2 flex flex-row items-baseline gap-2 text-xl font-bold">
            Gem
            <p className="text-sm text-secondary-2">{`(${pageSize} / ${sortedGems.length})`}</p>
          </div>
          <div
            onClick={() =>
              sortBy(
                sorting.showAdjusted
                  ? "xp_adjusted_level_profit"
                  : "level_profit",
              )
            }
            className="flex cursor-pointer flex-row gap-2 text-xl font-bold"
          >
            Level profit
            <ChaosOrb />
          </div>
          <div
            onClick={() =>
              sortBy(
                sorting.showAdjusted
                  ? "xp_adjusted_c_profit"
                  : "level_c_profit",
              )
            }
            className="flex cursor-pointer flex-row gap-2 text-xl font-bold"
          >
            Level + Corrupt
            <ChaosOrb />
          </div>
          <div
            onClick={() =>
              sortBy(
                sorting.showAdjusted
                  ? "xp_adjusted_q_c_profit"
                  : "level_q_c_profit",
              )
            }
            className="flex cursor-pointer flex-row gap-2 text-xl font-bold"
          >
            Level + Quality + Corrupt
            <ChaosOrb />
          </div>
        </div>
        {sortedGems.slice(0, pageSize).map((gem) => (
          <Row gem={gem} key={gem.name} />
        ))}
      </div>
      <button
        className="h-10 rounded border border-secondary-1 hover:border-2 hover:border-secondary-2"
        onClick={() => setPageSize(pageSize + 15)}
      >
        Show more
      </button>
    </div>
  );
}
