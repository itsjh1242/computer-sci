/**
 * Given ana integer x, return true if x is a palindrome number, and false otherwise.
 *
 * Example 1:
 * Input: x = 121
 * Output: true
 * Explanation: 121 reads as 121 from left to right and from right to left.
 *
 * Example 2:
 * Input: x = -121
 * Output: false
 * Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
 *
 * Example 3:
 * Input: x = 10
 * Output: false
 * Explanation: Reads 01 from right to left. Therefore it is not a plaindrome.
 * @param x
 */
function isPalindrome(x: number): boolean {
  const xStr = x.toString();
  /**
   * exception 1:
   * if length of x is 1, return true
   */
  if (xStr.length === 1) {
    return true;
  }

  const reversed = xStr.split("").reverse().join("");

  if (xStr === reversed) return true;
  return false;
}

isPalindrome(121);
