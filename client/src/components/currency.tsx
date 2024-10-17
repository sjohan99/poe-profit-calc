import Image from "next/image";

export default function ChaosOrb({ className }: { className?: string }) {
  return (
    <Image
      src="/currencies/chaos_orb.png"
      width={32}
      height={32}
      alt="Chaos Orb"
      className={`h-8 w-8 object-contain ${className}`}
    ></Image>
  );
}
