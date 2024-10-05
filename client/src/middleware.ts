import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { TokenBucketRateLimiter } from "./middleware/ratelimiting";
import { env } from "./env";

const rateLimiter = new TokenBucketRateLimiter({
  refillRateMs: env.RATE_LIMIT_TOKEN_REFILL_RATE_MS,
  maxTokens: env.RATE_LIMIT_TOKEN_BUCKET_CAPACITY,
});

export function middleware(request: NextRequest) {
  const ip = request.ip ?? request.headers.get("X-Forwarded-For") ?? "unknown";
  const isRateLimited = rateLimiter.limit(ip);

  if (isRateLimited) {
    console.log("Rate limited:", ip, "at", request.url);
    return new NextResponse(
      JSON.stringify({ error: "Too many requests. Please try again later." }),
      { status: 429, headers: { "Content-Type": "application/json" } },
    );
  }
}

export const config = {
  /*
   * Match all request paths except for the ones starting with:
   * - _next/static (static files)
   * - _next/image (image optimization files)
   * - favicon.ico, sitemap.xml, robots.txt (metadata files)
   * - Prefetch requests
   */
  matcher: [
    {
      source:
        "/((?!_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)",
      missing: [
        { type: "header", key: "next-router-prefetch" },
        { type: "header", key: "purpose", value: "prefetch" },
      ],
    },
  ],
};
