"use client";

import BlueLink from "../components/link";

export default function ErrorBoundary() {
  return (
    <div className="flex min-h-svh flex-col items-center justify-center gap-2">
      <h2 className="text-5xl">Oops :(</h2>
      <p>
        Looks like something went wrong. If this problem persists, kindly let me
        know on{" "}
        <BlueLink
          href="https://github.com/sjohan99/poe-profits/issues/new"
          text="Github!"
        ></BlueLink>
      </p>
    </div>
  );
}
