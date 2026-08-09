import math


# faster but if there is another char in s such as "e", need to handle that

def isBalanced(s):
  stack = []
  mapping = {
    ")": "(",
    "}": "{",
    "]": "["
  }
  el_set = {")", "(", "}", "{", "]", "["}

  for char in s:
    if char in el_set:

      if char in mapping:
        previous = stack.pop() if stack else 'random' # random value
        if mapping[char] != previous:
          return False

      else:
        stack.append(char)

  return not stack


# ======================================================================================================================


def solution(S):
  """
  Opening parenthesis are pushed and closing parenthesis pop.
  If the stack is empty prematurely there are too many closing brackets.
  If the stack is populated at the end there are too many opening brackets.
  """
  stack = []
  openers = '{[('
  closers = '}])'

  for char in S:
    if char in openers:
      stack.append(char)

    else:
      if not stack or openers.index(stack.pop()) != closers.index(char):
        return 0

  if len(stack) > 0:
    return 0
  return 1


# ======================================================================================================================

def isBalanced_slow(s):
  # Write your code here
  
  matching_chars = {
    '{':'}',
    '[':']',
    '(':')',
  }
  
  stack = []
  
  for char in s:
    if char in matching_chars:
      stack.append(char)
    elif matching_chars[stack[len(stack) - 1]] == char:
      stack.pop()
    else:
      continue

  return len(stack) == 0
    
# ======================================================================================================================

def balancedBrackets_with_other_chars(string):
  # Write your code here.
  brackets = {
    ']': '[',
    '}': '{',
    ')': '('
  }
  brackets_set = {']', '[', '}', '{', ')', '('}

  stack = []

  for el in string:

    if el in brackets_set:

      if el in brackets:

        if len(stack) > 0:

          if brackets[el] == stack[len(stack) - 1]:
            stack.pop(-1)

          else:
            return False
        else:
          stack.append(el)
      else:
        stack.append(el)

  return len(stack) == 0

# ======================================================================================================================

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "{[(])}"
  expected_1 = False
  output_1 = isBalanced(s1)
  check(expected_1, output_1)

  s2 = "{{[[(())]]}}"
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  s2 = ""
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)
  