def matches(secret: str, key: str) -> bool:
    m, n = len(secret), len(key)
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case
    dp[0][0] = True

    # Handle patterns like '*' at the start
    for j in range(1, n + 1):
        if key[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if key[j - 1] == '*':
                # '*' can match empty (dp[i][j-1]) or one or more characters (dp[i-1][j])
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif key[j - 1] == '?' or key[j - 1] == secret[i - 1]:
                
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

# Example usage
print(matches("aa", "a"))      # Output: False
print(matches("aa", "*"))      # Output: True
print(matches("cb", "?a"))     # Output: False
print(matches("adceb", "*a*b")) # Output: True
print(matches("acdcb", "a*c?b")) # Output: False
