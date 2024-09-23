import "~/styles/globals.css";
import Link from "next/link";
import { Roboto_Slab, Chakra_Petch } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/next";
import { CenterContent } from "~/components/center-content";
import PageTitle from "@components/page-title";
import Footer from "./footer";

const robotoSlab = Roboto_Slab({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

const chakraPetch = Chakra_Petch({
  weight: "400",
  subsets: ["latin"],
  display: "swap",
});

export const metadata = {
  title: "Path of Exile Profit Calculator",
  icons: [{ rel: "icon", url: "/icon.ico" }],
};

function TopNav() {
  return (
    <div className="flex h-20 w-full justify-center border-b-2 border-secondary-1 bg-accent-1 -lg:px-4">
      <div className="min-w-20 flex-none -lg:min-w-0"></div>
      <nav className="flex max-w-screen-2xl grow items-center justify-between text-2xl font-semibold">
        <Link
          href="/"
          className={
            chakraPetch.className + " text-3xl font-bold italic text-white"
          }
        >
          PoE Profit Calculator
        </Link>
        <div className="flex gap-x-10">
          <Link href="/" className="hover:underline">
            Bosses
          </Link>
          <Link href="/gems" className="hover:underline">
            Gems
          </Link>
          <Link href="/faq" className="hover:underline">
            FAQ
          </Link>
        </div>
      </nav>
      <div className="min-w-20 flex-none -lg:min-w-0"></div>
    </div>
  );
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${robotoSlab.className}`}>
      <body className="flex min-h-screen flex-col justify-between">
        <div className="min-h-screen">
          <TopNav />
          <PageTitle />
          <CenterContent className="my-2" background="bg-primary">
            {children}
          </CenterContent>
        </div>
        <div>
          <CenterContent no_pad_children={true}>
            <div className="border-t border-accent-1 pb-3"></div>
            <Footer></Footer>
          </CenterContent>
        </div>
        <Analytics></Analytics>
        <SpeedInsights></SpeedInsights>
      </body>
    </html>
  );
}
