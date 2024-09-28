import Link from "next/link";

type LinkTextProps = {
  text: string;
  href: string;
};

export default function BlueLink({ text, href }: LinkTextProps) {
  return (
    <Link href={href} className="text-link hover:underline" target="_blank">
      {text}
    </Link>
  );
}
