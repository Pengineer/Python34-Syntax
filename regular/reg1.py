# 正则表达式

'''
[]
- 常用来指定一个字符集：[abc]、[a-z]
- 元字符集在字符集中不起作用：[akm$] ，也就说$在此处仅仅表示一个普通的字符，而不是匹配末尾
- 补集匹配不在区间范围内的字符：[^5] ，^元字符在这里是起作用的

^
- 匹配行首。除非设置MULTINE标志，它只是匹配字符串的开始。在MULTINE模式里，它也可以直接匹配字符串中的每个换行

$
- 匹配行尾。行尾被定义为要么是字符串尾，要么是一个换行字符后面的任何位置。

The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?aiLmsux) Set the A, I, L, M, S, U, or X flag for the RE (see below).
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.

    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        \D       Matches any non-digit character; equivalent to [^\d].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode whitespace characters.
        \S       Matches any non-whitespace character; equivalent to [^\s].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                 in bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the
                 range of Unicode alphanumeric characters (letters plus digits
                 plus underscore).
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.

re里面函数：
FUNCTIONS
    compile(pattern, flags=0)
        Compile a regular expression pattern, returning a pattern object.

    escape(pattern)
        Escape all the characters in pattern except ASCII letters, numbers and '_'.

    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.

        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.

        Empty matches are included in the result.

    finditer(pattern, string, flags=0)
        Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a match object.

        Empty matches are included in the result.

    fullmatch(pattern, string, flags=0)
        Try to apply the pattern to all of the string, returning
        a match object, or None if no match was found.

    match(pattern, string, flags=0)
        Try to apply the pattern at the start of the string, returning
        a match object, or None if no match was found.

    purge()
        Clear the regular expression caches

    search(pattern, string, flags=0)
        Scan through string looking for a match to the pattern, returning
        a match object, or None if no match was found.

    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.  If
        capturing parentheses are used in pattern, then the text of all
        groups in the pattern are also returned as part of the resulting
        list.  If maxsplit is nonzero, at most maxsplit splits occur,
        and the remainder of the string is returned as the final element
        of the list.

    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the match object and must return
        a replacement string to be used.

    subn(pattern, repl, string, count=0, flags=0)
        Return a 2-tuple containing (new_string, number).
        new_string is the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in the source
        string by the replacement repl.  number is the number of
        substitutions that were made. repl can be either a string or a
        callable; if a string, backslash escapes in it are processed.
        If it is a callable, it's passed the match object and must
        return a replacement string to be used.

    template(pattern, flags=0)
        Compile a template pattern, returning a pattern object
'''

# 导入正则表达式的模块re
import  re

# 字符串前面的'r'是防止字符转义的 如果路径中出现'\t'的话 不加r的话\t就会被转义 而加了'r'之后'\t'就能保留原有的样子

# 格式：compile(pattern, flags=0)
# 正则匹配时，compile并不是必须的，but using re.compile() and saving the resulting regular expression object for reuse is more efficient when the expression will be used several times in a single program.
# 如果代码中多次用到了统一正则表达式，re.compile可以对规则进行预编译以提速
# pattern的match方法与re的match不同，被编译后的pattern与re的方法功能都是一样的但是参数不一样，被编译后的pattern不再需要pattern参数：
# search(string[, pos[, endpos]])
# match(string[, pos[, endpos]])
# fullmatch(string[, pos[, endpos]])
# split(string, maxsplit=0)
# findall(string[, pos[, endpos]])
# finditer(string[, pos[, endpos]])
# sub(repl, string, count=0)
#
p = re.compile(r'[\d]{3}-[\d]{11}')
s = p.match('027-12345678911，湖北仙桃')
print(s.group())

# 格式：sub(pattern, repl, string, count=0, flags=0)
# 字符串的replace是不支持正则表达式的（Java的replaceAll支持），Python提供的re.sub()

reg = r'w...d'
s = re.sub(reg, 'python', 'hello world, king world.')
print(s)

# 格式：subn(pattern, repl, string, count=0, flags=0)
# 功能属于sub相同，但是返回一个二元组，第一个参数与sub一样，第二个参数表示被替换的次数。
reg = r'w...d'
s = re.subn(reg, 'python', 'hello world, king world.')
print(s)

# 格式：match(pattern, string, flags=0)
# 匹配字符串从起始位置开始的内容，返回匹配对象
#
# 通常，match是与group搭配使用的。match返回的是一个内建对象，最主要的两个方法就是group([n])和groups([default])
# 如果reg中存在多个含有小括号的分组，那么每个分组就是一个group，编号从1开始。
# group()=group(0)表示的是reg整体匹配结果
# groups()=(group(1), group(2)....)，以元组的方式返回，如果某个分组没匹配上，默认为None，如果给定了default，则为default
#
src = '<script>中央人民日报日前报导...</script>'
reg = r'<.*>'
m = re.match(reg, src)
print(type(reg))
print(m.group())
print(m.groups())

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match
m.group(1)       # The first parenthesized subgroup.
m.group(2)       # The second parenthesized subgroup.
m.group(1, 2)    # Multiple arguments give us a tuple.

m = re.match(r"(\d+)\.(\d+)", "24.1632")
m.groups()

# 格式：search(pattern, string, flags=0)
# 与match很相似，但是match必须是从首字符开始匹配。而search只需要字符串任意位置有匹配上的子串即可。
src = 'abcd23efg'
s = re.search('\d+', src)
print(s.group())

# 格式：split(pattern, string, maxsplit=0, flags=0)
# 字符串也有split方法，不过re的split方法可以接受正则表达式
src = '12+34*56'
lists = re.split(r'[\+\-\*]', src)
print(lists)
