/**
 * Limits the rate of requests from a given id.
 *
 * It uses a token bucket algorithm to
 * refill tokens at a fixed rate and
 * consume tokens for each request.
 *
 * @param refillRateMs Refills one token every `refillRateMs` milliseconds.
 * @param maxTokens The maximum number of tokens that can be stored in the bucket.
 */
export class TokenBucketRateLimiter {
  refillRateMs: number;
  maxTokens: number;
  idToBucket: Map<string, { tokens: number; lastRefill: number }>;

  constructor(config: { refillRateMs: number; maxTokens: number }) {
    this.refillRateMs = config.refillRateMs;
    this.maxTokens = config.maxTokens;
    this.idToBucket = new Map<string, { tokens: number; lastRefill: number }>();
  }

  /**
   * Checks and updates the rate limit for a given id.
   * @param id The id to limit the rate of requests for, e.g. an IP address.
   * @returns true if the request exceeds the rate limit, false otherwise.
   */
  limit(id: string) {
    const now = Date.now();

    // get bucket or initialize it
    let bucket = this.idToBucket.get(id);
    if (!bucket) {
      bucket = { tokens: this.maxTokens, lastRefill: now };
      this.idToBucket.set(id, bucket);
    }

    // refill bucket if needed
    const tokensToRefill = Math.floor(
      (now - bucket.lastRefill) / this.refillRateMs,
    );
    if (tokensToRefill > 0) {
      bucket.tokens = Math.min(this.maxTokens, bucket.tokens + tokensToRefill);
      bucket.lastRefill = now;
    }

    // consume a token if there are any
    if (bucket.tokens > 0) {
      bucket.tokens -= 1;
    } else {
      return true;
    }

    return false;
  }
}
