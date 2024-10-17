"use client";

import { useMemo, useState } from "react";
import { type GemData, type Gem } from "./types";
import Image from "next/image";
import ChaosOrb from "@components/currency";
import { QuestionTooltip } from "@components/tooltip";
import BlueLink from "@components/link";
import {
  Table,
  TableHeader,
  TableHeaders,
  TableRow,
  TableRows,
} from "@components/table";

type SortableField = keyof Omit<Gem, "name" | "gem_type" | "img">;

type Sorting = {
  field: SortableField;
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

type TableProps = {
  gems: GemData;
};

export default function Tablex({ gems }: TableProps): JSX.Element {
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

  function sortBy(field: SortableField) {
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

  function SortableHeader({
    baseSorting,
    adjustedSorting,
    text,
  }: {
    baseSorting: SortableField;
    adjustedSorting: SortableField;
    text: string;
  }) {
    return (
      <div
        onClick={() =>
          sortBy(sorting.showAdjusted ? adjustedSorting : baseSorting)
        }
        className="-md:text-md flex cursor-pointer flex-row gap-2 truncate text-xl font-bold -lg:text-lg -sm:text-sm"
      >
        <p className="truncate" title={text}>
          {text}
        </p>
        <ChaosOrb className="-sm:hidden" />
        <SortArrow fields={[baseSorting, adjustedSorting]} />
      </div>
    );
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
    const level_profit = sorting.showAdjusted
      ? gem.xp_adjusted_level_profit
      : gem.level_profit;
    const level_c_profit = sorting.showAdjusted
      ? gem.xp_adjusted_c_profit
      : gem.level_c_profit;
    const level_q_c_profit = sorting.showAdjusted
      ? gem.xp_adjusted_q_c_profit
      : gem.level_q_c_profit;
    return (
      <TableRow column_sizes={[2, 1, 1, 1]}>
        <div className="flex flex-row items-center gap-2 truncate">
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
        <div>{renderField(level_profit)}</div>
        <div>{renderField(level_c_profit)}</div>
        <div>{renderField(level_q_c_profit)}</div>
      </TableRow>
    );
  }

  function SortArrow({ fields }: { fields: Array<SortableField> }) {
    if (!fields.includes(sorting.field)) {
      return (
        <div className="flex flex-col text-xs opacity-25 -sm:hidden">
          <div>▲</div>
          <div>▼</div>
        </div>
      );
    }
    return (
      <div className="flex flex-col text-xs -sm:hidden">
        <div className={sorting.order === "asc" ? "" : "opacity-50"}>▲</div>
        <div className={sorting.order === "asc" ? "opacity-50" : ""}>▼</div>
      </div>
    );
  }

  return (
    <div className="flex flex-col gap-y-2">
      <p className="text-lg text-secondary-2">Options:</p>
      <div className="flex flex-col items-start gap-y-2">
        <div className="flex flex-row gap-2">
          <CheckBox
            id="useExperienceAdjustedProfits"
            checked={sorting.showAdjusted}
            onChange={() => toggleAdjusted()}
            label="Use Experience Adjusted Profits"
          />
          <QuestionTooltip>
            <p>
              Divides profit of Awakened Gems by ~5.{" "}
              <BlueLink
                href="/faq#what-is-experience-adjusted-profits"
                text="FAQ"
              ></BlueLink>
            </p>
          </QuestionTooltip>
        </div>
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
      <Table>
        <TableHeaders column_sizes={[2, 1, 1, 1]}>
          <TableHeader>
            <p>
              Gem{" "}
              <span className="text-sm text-secondary-2">{`(${pageSize} / ${sortedGems.length})`}</span>
            </p>
          </TableHeader>
          <TableHeader>
            <SortableHeader
              baseSorting="level_profit"
              adjustedSorting="xp_adjusted_level_profit"
              text="Level Profit"
            ></SortableHeader>
          </TableHeader>
          <TableHeader>
            <SortableHeader
              baseSorting="level_c_profit"
              adjustedSorting="xp_adjusted_c_profit"
              text="Level + Corrupt"
            ></SortableHeader>
          </TableHeader>
          <TableHeader>
            <SortableHeader
              text="Level + Quality + Corrupt"
              baseSorting="level_q_c_profit"
              adjustedSorting="xp_adjusted_q_c_profit"
            ></SortableHeader>
          </TableHeader>
        </TableHeaders>
        <TableRows column_sizes={[2, 1, 1, 1]}>
          {sortedGems.slice(0, pageSize).map((gem) => (
            <Row gem={gem} key={gem.name} />
          ))}
        </TableRows>
        <button
          className="h-10 rounded border border-secondary-1 hover:border-2 hover:border-secondary-2"
          onClick={() => setPageSize(pageSize + 15)}
        >
          Show more
        </button>
      </Table>
    </div>
  );
}
