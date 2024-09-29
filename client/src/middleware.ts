import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { TokenBucketRateLimiter } from "./middleware/ratelimiting";
import { env } from "./env";

const rateLimiter = new TokenBucketRateLimiter({
  refillRateMs: env.RATE_LIMIT_TOKEN_REFILL_RATE_MS,
  maxTokens: env.RATE_LIMIT_TOKEN_BUCKET_CAPACITY,
});

// This function can be marked `async` if using `await` inside
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

// See "Matching Paths" below to learn more
export const config = {
  matcher:
    "/((?!_next/static|_next/image|favicon.ico|sitemap.xml|robots.txt).*)",
};
