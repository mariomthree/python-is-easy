# Python

## Python Regular Expressions

`Regular expression` is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.

Regular expressions (called `REs`, or `regexes`, or `regex patterns`) are essentially a tiny, highly specialized programming language embedded inside Python and made available through the `re` module. 

The Python module `re` provides full support for Perl-like regular expressions in Python.

A `RegEx`, or `Regular Expression`, is a sequence of characters that forms a search pattern. `RegEx` can be used to check if a string contains the specified search pattern.

## Simple Patterns

Since regular expressions are used to operate on strings, we’ll begin with the most common task: `matching characters`.

## Matching Characters

Most letters and characters will simply match themselves. For example, the regular expression simple will match the string simple exactly.

There are exceptions to this rule; some characters are special metacharacters, and don’t match themselves. Instead, they signal that some out-of-the-ordinary thing should be matched, or they affect other portions of the RE by repeating them or changing their meaning. 

The function below attempts to match RE `pattern` to `string` with optional `flags`.
Here is the syntax for this function − 
```
re.match(pattern, string, flags=0)
```

The `re.match` function returns a match object on success, None on failure. We usegroup(num) or groups() function of match object to get a matched expression.

 ```
 import re 

line = "The quick Brown Fox jumps over the lazy dog"
line2 = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line2, re.M|re.I)

if matchObj:
    print("matchObj.gropu()", matchObj.group())
    print("matchObj.gropu(1)", matchObj.group(1))
    print("matchObj.gropu(2)", matchObj.group(2))
else:
    print("no match")
 ```

## Basic Patterns: Ordinary Characters

You can easily tackle many basic patterns in Python using ordinary characters. Ordinary characters are the simplest regular expressions.

`Examples:` 'A', 'a', 'X', '5'.

Ordinary characters can be used to perform simple exact matches:

```
import re

# pattern = r"Cookie"
# sequence = "Cookie"
pattern = r"ookie"
sequence = "Cookie"
if re.match(pattern, sequence):
    print("Match!")
else:
    print("Not a match!")
```

Do you notice the `r` at the start of the pattern `Cookie` or `rookie` in the above examples? This is called a raw string literal. It changes how the string literal is interpreted. Such literals are stored as they appear.

## Wild Card Characters: Special Characters

Special characters are characters that do not match themselves as seen but have a special meaning when used in a regular expression.

-   1) A period. Matches any single character except the newline character.

Example: re.search(r'Co.k.e', 'Cookie').group()

-   2) ^ - A caret. Matches the start of the string.

This is helpful if we want to make sure a document/sentence starts with certain characters.

Example: re.search(r'^Eat', "Eat cake!").group()

`Returns ‘Eat’`

-   3) $ - Matches the end of string.

This is helpful if you want to make sure a document/sentence ends with certain characters.

Example: re.search(r'cake$', "Cake! Let's eat cake").group()

`Returns ‘cake’`

```
[abc] - Matches a or b or c.
[123] - Matches 1 or 2 or 3.
[a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
```

```
import re

re.search(r'[0-6]','Number: 5').group()
#This below Matches any character except 5
re.search(r'Number: [^5]', 'Number: 0').group()
#This below will not match and hence a NONE value will be returned
re.search(r'Number: [^5]', 'Number: 5').group()
```

### \ - Backslash

#### (Scenario 1) 
This treats '\s' as an escape character, '\s' defines a space

```
re.search(r'Not a\sregular character', 'Not a regular character').group()
# Result:  'Not a regular character'
```

### (Scenario 2) 
'\' is treated as an ordinary character, because '\r' is not a recognized escape character

```
re.search(r'Just a \regular character', 'Just a \regular character').group()
# Result: 'Just a \regular character'
```	

### (Scenario 3) 
'\s' is escaped using an extra `\` so its interpreted as a literal string '\s'

```
re.search(r'Just a \\sregular character', 'Just a \sregular character').group()
# Result: 'Just a \\sregular character'
```

There is a predefined set of special sequences that begin with '\' and are also very helpful when performing search and match.

-   \w - Lowercase 'w'. Matches any single letter, digit, or underscore.
-   \W - Uppercase 'W'. Matches any character not part of \w (lowercase w).

-   \s - Lowercase 's'. Matches a single whitespace character like: space, newline, tab, return.
-   \S - Uppercase 'S'. Matches any character not part of \s (lowercase s).

-   \d - Lowercase d. Matches decimal digit 0-9.
-   \D - Uppercase d. Matches any character that is not a decimal digit.


-   \t - Lowercase t. Matches tab.
-   \n - Lowercase n. Matches newline.
-   \r - Lowercase r. Matches return.
-   \A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
-   \Z - Uppercase z. Matches only at the end of the string.
-   \b - Lowercase b. Matches only the beginning or end of the word.

-   + - Checks if the preceding character appears one or more times starting from that position

-   * - Checks if the preceding character appears zero or more times starting from that position.

-   ? - Checks if the preceding character appears exactly zero or one time starting from that position.


```
import re
re.search(r'Hoo+ray','Hooookray!!').group
re.search(r'Ca*o*kie','Cookie!!').group
re.search(r'Colou?r','Color!!').group
#retun Hoookay
#return Cookie
```

But what if you want to check for an exact number of sequence repetition?
For example, checking the validity of a phone number in an application

-   `{x}` - Repeat exactly x number of times.
-   `{x,}` - Repeat at least x times or more.
-   `{x, y}` - Repeat at least x times but no more than y times.

```
re.search(r'\d{9, 10}, '0987654321').group()
```

## Grouping in Regular Expressions

The group feature of regular expression allows you to pick up parts of the matching text.  
The parenthesis does not change what the expression matches, but rather forms groups within the matched sequence.

Example. Imagine you were validating email addresses and wanted to check the user name and host.

```
import re

statement = 'Please contact us at: pythoniseasy@python.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)

if statement:
    print("Email address: ", match.group())
    print("Username: ", match.group(1))
    print("Host: ", match.group(2))

# return
# Email address:  pythoniseasy@python.com
# Username:  pythoniseasy
# Host:  python.com
```

Create a name group.

```
import re

statement = 'Please contact us at: pythoniseasy@python.com'
match = re.search(r'?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+)', statement)

if statement:
    print("Email address: ", match.group('email'))
    print("Username: ", match.group('username'))
    print("Host: ", match.group('host'))

# return
# Email address:  pythoniseasy@python.com
# Username:  pythoniseasy
# Host:  python.com
```

## Greedy vs. Non-Greedy Matching

When a special character matches as much of the search sequence (string) as possible, it is said to be a "Greedy Match".

```
import re

pattern = "Programmer"
sequence = "George the Programmer"
heading = r"<h1>Title<h1>"
re.match(r'<.*>, heading').group()

#return <h1>Title<h1>
```
The pattern <.*> matched the whole string, right up to the second occurrence of >.

However, if you only wanted to match the first <h1> tag, you could have used the greedy qualifier *? that matches as little text as possible.

Adding ? after the qualifier makes it perform the match in a non-greedy or minimal fashion.
