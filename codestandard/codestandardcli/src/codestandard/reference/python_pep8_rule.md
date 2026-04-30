# PEP 8 Python Style Guide 规则集

来源: https://peps.python.org/pep-0008/
规则数量: 37

## 使用说明

- 【强制】: PEP 8 中明确要求或禁止的规则，代码生成、修改和评审时应遵守。
- 【推荐】: PEP 8 中使用 should、recommended、prefer、may、consider 等语气的建议性规则。
- 项目本地规范优先；PEP 8 本身也说明项目规范冲突时应以项目规范为准。
- 本文件是对官方 PEP 8 页面的本地摘要，不替代官方原文。

## Introduction

1. 【强制】This document gives coding conventions for the Python code comprising the standard library in the main Python distribution. Please see the companion informational PEP describing style guidelines for the C code in the C implementation of Python. This document and PEP 257 (Docstring Conventions) were adapted from Guido’s original Python Style Guide essay, with some additions from Barry’s style guide [2]. This style guide evolves over time as additional conventions are identified and past conventions are rendered...

## A Foolish Consistency is the Hobgoblin of Little Minds

1. 【推荐】One of Guido’s key insights is that code is read much more often than it is written. The guidelines provided here are intended to improve the readability of code and make it consistent across the wide spectrum of Python code. As PEP 20 says, “Readability counts”. A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important. However, know when to be inconsistent – sometimes style...

## Code Lay-out

### Indentation

1. 【推荐】Use 4 spaces per indentation level. Continuation lines should align wrapped elements either vertically using Python’s implicit line joining inside parentheses, brackets and braces, or using a hanging indent [1]. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line: The 4-space rule is optional for continuation lines. Optional: When the conditional part of an...
  - 正例/反例/示例:
    # Correct:
    # Aligned with opening delimiter.
    foo = long_function_name(var_one, var_two,
                             var_three, var_four)
    # Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)
    # Hanging indents should add a level.
    foo = long_function_name(
        var_one, var_two,
        var_three, var_four)

### Tabs or Spaces?

2. 【推荐】Spaces are the preferred indentation method. Tabs should be used solely to remain consistent with code that is already indented with tabs. Python disallows mixing tabs and spaces for indentation.

### Maximum Line Length

3. 【推荐】Limit all lines to a maximum of 79 characters. For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters. Limiting the required editor window width makes it possible to have several files open side by side, and works well when using code review tools that present the two versions in adjacent columns. The default wrapping in most tools disrupts the visual structure of the code, making it more difficult to understand. The limits...
  - 正例/反例/示例:
    with open('/path/to/some/file/you/want/to/read') as file_1, \
         open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())

### Should a Line Break Before or After a Binary Operator?

4. 【推荐】For decades the recommended style was to break after binary operators. But this can hurt readability in two ways: the operators tend to get scattered across different columns on the screen, and each operator is moved away from its operand and onto the previous line. Here, the eye has to do extra work to tell which items are added and which are subtracted: To solve this readability problem, mathematicians and their publishers follow the opposite convention. Donald Knuth explains the traditional rule in his...
  - 正例/反例/示例:
    # Wrong:
    # operators sit far away from their operands
    income = (gross_wages +
              taxable_interest +
              (dividends - qualified_dividends) -
              ira_deduction -
              student_loan_interest)

### Blank Lines

5. 【推荐】Surround top-level function and class definitions with two blank lines. Method definitions inside a class are surrounded by a single blank line. Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations). Use blank lines in functions, sparingly, to indicate logical sections. Python accepts the control-L (i.e. ^L) form feed character as whitespace; many tools treat these characters as page...

### Source File Encoding

6. 【推荐】Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration. In the standard library, non-UTF-8 encodings should be used only for test purposes. Use non-ASCII characters sparingly, preferably only to denote places and human names. If using non-ASCII characters as data, avoid noisy Unicode characters like z̯̯͡a̧͎̺l̡͓̫g̹̲o̡̼̘ and byte order marks. All identifiers in the Python standard library MUST use ASCII-only identifiers, and SHOULD use English words wherever...

### Imports

7. 【推荐】It’s okay to say this though: Imports should be grouped in the following order: Standard library imports. Related third party imports. Local application/library specific imports. You should put a blank line between each group of imports. However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose: Standard library code should avoid complex package layouts and always use...
  - 正例/反例/示例:
    # Correct:
    import os
    import sys

### Module Level Dunder Names

8. 【推荐】Module level “dunders” (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements except `from __future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings:
  - 正例/反例/示例:
    """This is the example module.
    This module does stuff.
    """
    from __future__ import barry_as_FLUFL
    __all__ = ['a', 'b', 'c']
    __version__ = '0.1'
    __author__ = 'Cardinal Biggles'
    import os
    import sys

## String Quotes

1. 【强制】In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability. For triple-quoted strings, always use double quote characters to be consistent with the docstring convention in PEP 257.

## Whitespace in Expressions and Statements

### Pet Peeves

1. 【强制】Avoid extraneous whitespace in the following situations:
  - 正例/反例/示例:
    # Correct:
    spam(ham[1], {eggs: 2})

### Other Recommendations

2. 【强制】Avoid trailing whitespace anywhere. Because it’s usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don’t preserve it and many projects (like CPython itself) have pre-commit hooks that reject it. Always surround these binary operators with a single space on either side: assignment (`=`), augmented assignment (`+=`, `-=` etc.), comparisons (`==`, `<`, `>`, `!=`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), Booleans...
  - 正例/反例/示例:
    # Correct:
    i = i + 1
    submitted += 1
    x = x*2 - 1
    hypot2 = x*x + y*y
    c = (a+b) * (a-b)

## When to Use Trailing Commas

1. 【推荐】Trailing commas are usually optional, except they are mandatory when making a tuple of one element. For clarity, it is recommended to surround the latter in (technically redundant) parentheses: When trailing commas are redundant, they are often helpful when a version control system is used, when a list of values, arguments or imported items is expected to be extended over time. The pattern is to put each value (etc.) on a line by itself, always adding a trailing comma, and add the close parenthesis/bracket/brace...
  - 正例/反例/示例:
    # Correct:
    FILES = ('setup.cfg',)

## Comments

1. 【推荐】Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes! Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!). Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period. You should use one or two spaces after a sentence-ending period...

### Block Comments

2. 【强制】Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a `#` and a single space (unless it is indented text inside the comment). Paragraphs inside a block comment are separated by a line containing a single `#`.

### Inline Comments

3. 【推荐】Use inline comments sparingly. An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space. Inline comments are unnecessary and in fact distracting if they state the obvious. Don’t do this: But sometimes, this is useful:
  - 正例/反例/示例:
    x = x + 1                 # Increment x

### Documentation Strings

4. 【推荐】Conventions for writing good documentation strings (a.k.a. “docstrings”) are immortalized in PEP 257. Write docstrings for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the `def` line.
  - 正例/反例/示例:
    """Return a foobang
    Optional plotz says to frobnicate the bizbaz first.
    """

## Naming Conventions

1. 【推荐】The naming conventions of Python’s library are a bit of a mess, so we’ll never get this completely consistent – nevertheless, here are the currently recommended naming standards. New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

### Overriding Principle

2. 【推荐】Names that are visible to the user as public parts of the API should follow conventions that reflect usage rather than implementation.

### Descriptive: Naming Styles

3. 【强制】There are a lot of different naming styles. It helps to be able to recognize what naming style is being used, independently from what they are used for. The following naming styles are commonly distinguished: `b` (single lowercase letter) `B` (single uppercase letter) `lowercase` `lower_case_with_underscores` `UPPERCASE` `UPPER_CASE_WITH_UNDERSCORES` Note: When using acronyms in CapWords, capitalize all the letters of the acronym. Thus HTTPServerError is better than HttpServerError. `mixedCase` (differs from...
  - 正例/反例/示例:
    tkinter.Toplevel(master, class_='ClassName')

### Prescriptive: Naming Conventions

4. 【强制】Names to Avoid: Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names. In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use ‘l’, use ‘L’ instead.

5. 【强制】ASCII Compatibility: Identifiers used in the standard library must be ASCII compatible as described in the policy section of PEP 3131.

6. 【推荐】Package and Module Names: Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged. When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. `_socket`).

7. 【推荐】Class Names: Class names should normally use the CapWords convention. The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable. Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.

8. 【推荐】Type Variable Names: Names of type variables introduced in PEP 484 should normally use CapWords preferring short names: `T`, `AnyStr`, `Num`. It is recommended to add suffixes `_co` or `_contra` to the variables used to declare covariant or contravariant behavior correspondingly:
  - 正例/反例/示例:
    from typing import TypeVar
    VT_co = TypeVar('VT_co', covariant=True)
    KT_contra = TypeVar('KT_contra', contravariant=True)

9. 【推荐】Exception Names: Because exceptions should be classes, the class naming convention applies here. However, you should use the suffix “Error” on your exception names (if the exception actually is an error).

10. 【推荐】Global Variable Names: (Let’s hope that these variables are meant for use inside one module only.) The conventions are about the same as those for functions. Modules that are designed for use via `from M import *` should use the `__all__` mechanism to prevent exporting globals, or use the older convention of prefixing such globals with an underscore (which you might want to do to indicate these globals are “module non-public”).

11. 【推荐】Function and Variable Names: Function names should be lowercase, with words separated by underscores as necessary to improve readability. Variable names follow the same convention as function names. mixedCase is allowed only in contexts where that’s already the prevailing style (e.g. threading.py), to retain backwards compatibility.

12. 【强制】Function and Method Arguments: Always use `self` for the first argument to instance methods. Always use `cls` for the first argument to class methods. If a function argument’s name clashes with a reserved keyword, it is generally better to append a single trailing underscore rather than use an abbreviation or spelling corruption. Thus `class_` is better than `clss`. (Perhaps better is to avoid such clashes by using a synonym.)

13. 【推荐】Method Names and Instance Variables: Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability. Use one leading underscore only for non-public methods and instance variables. To avoid name clashes with subclasses, use two leading underscores to invoke Python’s name mangling rules. Python mangles these names with the class name: if class Foo has an attribute named `__a`, it cannot be accessed by `Foo.__a`. (An insistent user could still gain access by calling `Foo._Foo__a`.) Generally, double...

14. 【强制】Constants: Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include `MAX_OVERFLOW` and `TOTAL`.

15. 【推荐】Designing for Inheritance: Always decide whether a class’s methods and instance variables (collectively: “attributes”) should be public or non-public. If in doubt, choose non-public; it’s easier to make it public later than to make a public attribute non-public. Public attributes are those that you expect unrelated clients of your class to use, with your commitment to avoid backwards incompatible changes. Non-public attributes are those that are not intended to be used by third parties; you make no guarantees that non-public attributes...

### Public and Internal Interfaces

16. 【推荐】Any backwards compatibility guarantees apply only to public interfaces. Accordingly, it is important that users be able to clearly distinguish between public and internal interfaces. Documented interfaces are considered public, unless the documentation explicitly declares them to be provisional or internal interfaces exempt from the usual backwards compatibility guarantees. All undocumented interfaces should be assumed to be internal. To better support introspection, modules should explicitly declare the names in...

## Programming Recommendations

1. 【推荐】For example, do not rely on CPython’s efficient implementation of in-place string concatenation for statements in the form `a += b` or `a = a + b`. This optimization is fragile even in CPython (it only works for some types) and isn’t present at all in implementations that don’t use refcounting. In performance sensitive parts of the library, the `''.join()` form should be used instead. This will ensure that concatenation occurs in linear time across various implementations. Also, beware of writing `if x` when you...
  - 正例/反例/示例:
    # Correct:
    if foo is not None:

### Function Annotations

2. 【推荐】With the acceptance of PEP 484, the style rules for function annotations have changed. Function annotations should use PEP 484 syntax (there are some formatting recommendations for annotations in the previous section). The experimentation with annotation styles that was recommended previously in this PEP is no longer encouraged. However, outside the stdlib, experiments within the rules of PEP 484 are now encouraged. For example, marking up a large third party library or application with PEP 484 style type...
  - 正例/反例/示例:
    # type: ignore

### Variable Annotations

3. 【推荐】PEP 526 introduced variable annotations. The style recommendations for them are similar to those on function annotations described above: Annotations for module level variables, class and instance variables, and local variables should have a single space after the colon. There should be no space before the colon. Although the PEP 526 is accepted for Python 3.6, the variable annotation syntax is the preferred syntax for stub files on all versions of Python (see PEP 484 for details). Footnotes
  - 正例/反例/示例:
    # Correct:
    code: int
    class Point:
        coords: Tuple[int, int]
        label: str = '<unknown>'
