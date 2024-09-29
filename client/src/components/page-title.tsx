"use client";

import { usePathname } from "next/navigation";
import { CenterContent } from "./center-content";

const routeTitles: Record<string, string> = {
  "/": "Summary",
  "/bosses": "Bosses",
  "/gems": "Gem Levelling",
  "/faq": "Frequency Asked Questions",
  "/about": "About",
};

export default function PageTitle() {
  const pathName = usePathname();
  const title = routeTitles[pathName] ?? ""; // Default to 'Summary' if route is not found

  return (
    <CenterContent no_pad_children={true}>
      <h1 className="text-3xl font-bold">{title}</h1>
    </CenterContent>
  );
}
