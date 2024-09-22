import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex min-h-svh flex-col items-center justify-center gap-2">
      <h2 className="text-5xl">Not Found</h2>
      <p>Could not find requested resource</p>
      <Link href="/" className="text-link hover:underline">
        Return Home
      </Link>
    </div>
  );
}
