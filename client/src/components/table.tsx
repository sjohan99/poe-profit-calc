import React from "react";

function columnSize(index: number, column_sizes: number[]): string {
  const size = column_sizes[index % column_sizes.length];
  if (size === sum(column_sizes)) {
    return `col-span-full`;
  }
  return `col-span-${size}`;
}

function sum(arr: number[]): number {
  return arr.reduce((acc, size) => acc + size, 0);
}

export function TableHeaders(props: {
  children: React.ReactNode;
  column_sizes: number[];
}) {
  const { children, column_sizes } = props;

  return (
    <div className={`grid grid-cols-${sum(column_sizes)} gap-x-3 -sm:gap-x-2`}>
      {React.Children.map(children, (child, index) => (
        <div
          key={index}
          className={`${columnSize(index, column_sizes)} flex items-center ${index !== 0 ? "-sm:justify-end" : ""}`}
        >
          {child}
        </div>
      ))}
    </div>
  );
}

export function TableHeader(props: { children: React.ReactNode }) {
  const { children } = props;

  return (
    <div className="responsive-text-medium flex flex-row items-center gap-2 truncate text-xl font-bold">
      {children}
    </div>
  );
}

export function TableRow(props: {
  children: React.ReactNode;
  column_sizes: number[];
}) {
  const { children, column_sizes } = props;
  const childrenArray = React.Children.toArray(children);

  return childrenArray.map((child, index) => (
    <div
      key={index}
      className={`${columnSize(index, column_sizes)} responsive-text-small flex h-full items-center truncate ${index !== 0 ? "-sm:justify-end" : ""}`}
    >
      {child}
    </div>
  ));
}

export function TableRows(props: {
  children: React.ReactNode;
  column_sizes: number[];
}) {
  const { children, column_sizes } = props;
  return (
    <div
      className={`grid grid-cols-${sum(column_sizes)} gap-x-3 gap-y-2 -sm:gap-x-2`}
    >
      {children}
    </div>
  );
}

export function Table(props: { children: React.ReactNode }) {
  const { children } = props;

  return <div className="grid grid-cols-1 gap-2">{children}</div>;
}
