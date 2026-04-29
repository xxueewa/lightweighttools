# Google Java Style Guide 规则集

来源: https://google.github.io/styleguide/javaguide.html
规则数量: 74

## 使用说明

- 【强制】: Google Java Style 的硬性规则，代码生成、修改和评审时应遵守。
- 【推荐】: 原文中带有 recommended、optional、may、tip 等语义的建议性规则。
- 本文件是对官方网页的本地摘要，不替代官方原文。

## Introduction

### Terminology notes

1. 【强制】In this document, unless otherwise clarified: The term class is used inclusively to mean a normal class, record class, enum class, interface or annotation type (`@interface`). The term member (of a class) is used inclusively to mean a nested class, field, method, or constructor; that is, all top-level contents of a class except initializers. The term comment always refers to implementation comments. We do not use...

## Source file basics

### File name

1. 【强制】For a source file containing classes, the file name consists of the case-sensitive name of the top-level class (of which there is exactly one), plus the `.java` extension.

### File encoding: UTF-8

1. 【强制】Source files are encoded in UTF-8.

### Special characters

1. 【强制】Whitespace characters: Aside from the line terminator sequence, the ASCII horizontal space character (0x20) is the only whitespace character that appears anywhere in a source file. This means: All other whitespace characters are escaped in `char` and string literals and in text blocks. Tab characters are not used for indentation.

2. 【强制】Special escape sequences: For any character that has a special escape sequence (`\b`, `\t`, `\n`, `\f`, `\r`, `\s`, `\"`, `\'` and `\\`), that sequence is used rather than the corresponding octal (e.g. `\012`) or Unicode (e.g. `\u000a`) escape.

3. 【强制】Non-ASCII characters: For the remaining non-ASCII characters, either the actual Unicode character (e.g. `∞`) or the equivalent Unicode escape (e.g. `\u221e`) is used. The choice depends only on which makes the code easier to read and understand, although Unicode escapes outside string literals and comments are strongly discouraged. Tip: In the Unicode escape case, and occasionally even when actual Unicode characters are used, an...

## Source file structure

### License or copyright information, if present

1. 【强制】If license or copyright information belongs in a file, it belongs here.

### Package declaration

1. 【强制】Every source file must have a package declaration. Compact source files are not used. (This rule obviously does not apply to `module-info.java` files, which have a different syntax that does not include a package declaration.) The package declaration is not line-wrapped. The column limit (Section 4.4, Column limit: 100) does not apply to package declarations.

### Imports

1. 【强制】No wildcard imports: Wildcard ("on-demand") imports, static or otherwise, are not used.

2. 【强制】No module imports: Module imports are not used.
  - 正例/示例:
    import module java.base;

3. 【强制】No line-wrapping: Imports are not line-wrapped. The column limit (Section 4.4, Column limit: 100) does not apply to imports.

4. 【强制】Ordering and spacing: Imports are ordered as follows: All static imports in a single group. All non-static imports in a single group. If there are both static and non-static imports, a single blank line separates the two groups. There are no other blank lines between imports. Within each group the imported names appear in ASCII sort order. (Note: this is not the same as the import lines being in ASCII sort order, since '.' sorts before...

5. 【强制】No static import for classes: Static import is not used for static nested classes. They are imported with normal imports.

### Class declaration

1. 【强制】Exactly one top-level class declaration: Each top-level class resides in a source file of its own.

2. 【强制】Ordering of class contents: The order you choose for the members and initializers of your class can have a great effect on learnability. However, there's no single correct recipe for how to do it; different classes may order their contents in different ways. What is important is that each class uses some logical order, which its maintainer could explain if asked. For example, new methods are not just habitually added to the end of the class...

3. 【强制】Overloads: never split: Methods of a class that share the same name appear in a single contiguous group with no other members in between. The same applies to multiple constructors. This rule applies even when modifiers such as `static` or `private` differ between the methods or constructors.

### Module declaration

1. 【强制】Ordering and spacing of module directives: Module directives are ordered as follows: All `requires` directives in a single block. All `exports` directives in a single block. All `opens` directives in a single block. All `uses` directives in a single block. All `provides` directives in a single block. A single blank line separates each block that is present.

## Formatting

### Braces

1. 【强制】Use of optional braces: Braces are used with `if`, `else`, `for`, `do` and `while` statements, even when the body is empty or contains only a single statement. Other optional braces, such as those in a lambda expression, remain optional.

2. 【强制】Nonempty blocks: K & R style: Braces follow the Kernighan and Ritchie style for nonempty blocks and block-like constructs: No line break before the opening brace, except as detailed below. Line break after the opening brace. Line break before the closing brace. Line break after the closing brace, only if that brace terminates a statement or terminates the body of a method, constructor, or named class. For example, there is no line break after...
  - 正例/示例:
    return () -> {
      while (condition()) {
        method();
      }
    };
    return new MyClass() {
      @Override public void method() {
        if (condition()) {
          try {
            something();
          } catch (ProblemException e) {
            recover();
          }
        } else if (otherCondition()) {
          somethingElse();
        } else {
          lastThing();
        }
        {

3. 【推荐】Empty blocks: may be concise: An empty block or block-like construct may be in K & R style (as described in Section 4.1.2). Alternatively, it may be closed immediately after it is opened, with no characters or line break in between (`{}`), unless it is part of a multi-block statement (one that directly contains multiple blocks: `if/else` or `try/catch/finally`).
  - 正例/示例:
      // This is acceptable
      void doNothing() {}
      // This is equally acceptable
      void doNothingElse() {
      }

### Block indentation: +2 spaces

1. 【强制】Each time a new block or block-like construct is opened, the indent increases by two spaces. When the block ends, the indent returns to the previous indent level. The indent level applies to both code and comments throughout the block. (See the example in Section 4.1.2, Nonempty blocks: K & R Style.)

### One statement per line

1. 【强制】Each statement is followed by a line break.

### Column limit: 100

1. 【强制】Java code has a column limit of 100 characters. A "character" means any Unicode code point. Except as noted below, any line that would exceed this limit must be line-wrapped, as explained in Section 4.5, Line-wrapping. Each Unicode code point counts as one character, even if its display width is greater or less. For example, if using fullwidth characters, you may choose to wrap the line earlier than where this rule...

### Line-wrapping

1. 【强制】Terminology Note: When code that might otherwise occupy a single line is divided into multiple lines, this activity is called line-wrapping. There is no comprehensive, deterministic formula showing exactly how to line-wrap in every situation. Very often there are several valid ways to line-wrap the same piece of code. Note: While the typical reason for line-wrapping is to avoid overflowing the column limit, even...

2. 【强制】Where to break: The prime directive of line-wrapping is: prefer to break at a higher syntactic level. Also: the dot separator (`.`) the two colons of a method reference (`::`) an ampersand in a type bound (`<T extends Foo & Bar>`) a pipe in a catch block (`catch (FooException | BarException e)`). This also applies to the colon in an enhanced `for` ("foreach") statement. A method, constructor, or record-class name stays attached to...
  - 正例/示例:
    MyLambda<String, Long, Object> lambda =
        (String label, Long value, Object obj) -> {
          ...
        };
    Predicate<String> predicate = str ->
        longExpressionInvolving(str);
    switch (x) {
      case ColorPoint(Color color, Point(int x, int y)) ->
          handleColorPoint(color, x, y);
      ...
    }

3. 【强制】Indent continuation lines at least +4 spaces: When line-wrapping, each line after the first (each continuation line) is indented at least +4 from the original line. When there are multiple continuation lines, indentation may be varied beyond +4 as desired. In general, two continuation lines use the same indentation level if and only if they begin with syntactically parallel elements. Section 4.6.3 on Horizontal alignment addresses the discouraged practice of...

### Whitespace

1. 【强制】Vertical whitespace (blank lines): A single blank line always appears: Exception: A blank line between two consecutive fields (having no other code between them) is optional. Such blank lines are used as needed to create logical groupings of fields. Exception: Blank lines between enum constants are covered in Section 4.8.1. As required by other sections of this document (such as Section 3, Source file structure, and Section 3.3, Imports). A single...

2. 【强制】Horizontal whitespace: Beyond where required by the language or other style rules, and apart from within literals, comments and Javadoc, a single ASCII space also appears in the following places only. Separating any keyword, such as `if`, `for` or `catch`, from an open parenthesis (`(`) that follows it on that line Separating any keyword, such as `else` or `catch`, from a closing curly brace (`}`) that precedes it on that line...

3. 【强制】Horizontal alignment: never required: Terminology Note: Horizontal alignment is the practice of adding a variable number of additional spaces in your code with the goal of making certain tokens appear directly below certain other tokens on previous lines. This practice is permitted, but is never required by Google Style. It is not even required to maintain horizontal alignment in places where it was already used. Here is an example without alignment...
  - 正例/示例:
    private int x; // this is fine
    private Color color; // this too
    private int   x;      // permitted, but future edits
    private Color color;  // may leave it unaligned

### Grouping parentheses: recommended

1. 【推荐】Optional grouping parentheses are omitted only when author and reviewer agree that there is no reasonable chance the code will be misinterpreted without them, nor would they have made the code easier to read. It is not reasonable to assume that every reader has the entire Java operator precedence table memorized.

### Specific constructs

1. 【强制】Enum classes: After the comma that follows an enum constant, a line break is optional. Additional blank lines (usually just one) are also allowed. This is one possibility: An enum class with no methods and no documentation on its constants may optionally be formatted as if it were an array initializer (see Section 4.8.3.1 on array initializers). Since enum classes are classes, all other rules for formatting classes apply.
  - 正例/示例:
    private enum Answer {
      YES {
        @Override public String toString() {
          return "yes";
        }
      },
      NO,
      MAYBE
    }

2. 【强制】One variable per declaration: Every variable declaration (field or local) declares only one variable: declarations such as `int a, b;` are not used. Exception: Multiple variable declarations are acceptable in the header of a `for` loop.

3. 【强制】Declared when needed: Local variables are not habitually declared at the start of their containing block or block-like construct. Instead, local variables are declared close to the point they are first used (within reason), to minimize their scope. Local variable declarations typically have initializers, or are initialized immediately after declaration.

4. 【强制】Array initializers: can be "block-like": Any array initializer may optionally be formatted as if it were a "block-like construct." For example, the following are all valid (not an exhaustive list):
  - 正例/示例:
    new int[] {           new int[] {
      0, 1, 2, 3            0,
    }                       1,
                            2,
    new int[] {             3,
      0, 1,               }
      2, 3
    }                     new int[]
                              {0, 1, 2, 3}

5. 【强制】No C-style array declarations: The square brackets form a part of the type, not the variable: `String[] args`, not `String args[]`.

6. 【强制】Switch statements and expressions: For historical reasons, the Java language has two distinct syntaxes for `switch`, which we can call old-style and new-style. New-style switches use an arrow (`->`) after the switch labels, while old-style switches use a colon (`:`). Terminology Note: Inside the braces of a switch block are either one or more switch rules (new-style); or one or more statement groups (old-style). A switch rule consists of a switch...

7. 【强制】Indentation: As with any other block, the contents of a switch block are indented +2. Each switch label starts with this +2 indentation. In a new-style switch, a switch rule can be written on a single line if it otherwise follows Google style. (It must not exceed the column limit, and if it contains a non-empty block then there must be a line break after `{`.) The line-wrapping rules of Section 4.5 apply, including the +4 indent...
  - 正例/示例:
    switch (number) {
      case 0, 1 -> handleZeroOrOne();
      case 2 ->
          handleTwoWithAnExtremelyLongMethodCallThatWouldNotFitOnTheSameLine();
      default -> {
        logger.atInfo().log("Surprising number %s", number);
        handleSurprisingNumber(number);
      }
    }

8. 【强制】Fall-through: commented: Within an old-style switch block, each statement group either terminates abruptly (with a `break`, `continue`, `return` or thrown exception), or is marked with a comment to indicate that execution will or might continue into the next statement group. Any comment that communicates the idea of fall-through is sufficient (typically `// fall through`). This special comment is not required in the last statement group of...
  - 正例/示例:
    switch (input) {
      case 1:
      case 2:
        prepareOneOrTwo();
      // fall through
      case 3:
        handleOneTwoOrThree();
        break;
      default:
        handleLargeNumber(input);
    }

9. 【强制】Exhaustiveness and presence of the `default` label: The Java language requires switch expressions and many kinds of switch statements to be exhaustive. That effectively means that every possible value that could be switched on will be matched by one of the switch labels. A switch is exhaustive if it has a `default` label, but also for example if the value being switched on is an enum and every value of the enum is matched by a switch label. Google Style requires...

10. 【强制】Switch expressions: Switch expressions must be new-style switches:
  - 正例/示例:
      return switch (list.size()) {
        case 0 -> "";
        case 1 -> list.getFirst();
        default -> String.join(", ", list);
      };

11. 【强制】Type-use annotations: Type-use annotations appear immediately before the annotated type. An annotation is a type-use annotation if it is meta-annotated with `@Target(ElementType.TYPE_USE)`. Example:
  - 正例/示例:
    final @Nullable String name;
    public @Nullable Person getPersonByName(String name);

12. 【强制】Class, package, and module annotations: Annotations applying to a class, package, or module declaration appear immediately after the documentation block, and each annotation is listed on a line of its own (that is, one annotation per line). These line breaks do not constitute line-wrapping (Section 4.5, Line-wrapping), so the indentation level is not increased. Examples:
  - 正例/示例:
    /** This is a class. */
    @Deprecated
    @CheckReturnValue
    public final class Frozzler { ... }

13. 【强制】Method and constructor annotations: The rules for annotations on method and constructor declarations are the same as the previous section. Example: Exception: If the method or constructor only has a single, parameterless annotation, it may appear together with the first line of the signature, for example:
  - 正例/示例:
    @Deprecated
    @Override
    public String getNameIfPresent() { ... }

14. 【强制】Field annotations: Annotations applying to a field also appear immediately after the documentation block, but in this case, multiple annotations (possibly parameterized) may be listed on the same line; for example:
  - 正例/示例:
    @Partial @Mock DataLoader loader;

15. 【强制】Parameter and local variable annotations: There are no specific rules for formatting annotations on parameters or local variables (except, of course, when the annotation is a type-use annotation).

16. 【强制】Comments: This section addresses implementation comments. Javadoc is addressed separately in Section 7, Javadoc. Any line break may be preceded by arbitrary whitespace followed by an implementation comment. Such a comment renders the line non-blank.

17. 【强制】Block comment style: Block comments are indented at the same level as the surrounding code. They may be in `/* ... */` style or `// ...` style. For multi-line `/* ... */` comments, subsequent lines must start with `*` aligned with the `*` on the previous line. Comments are not enclosed in boxes drawn with asterisks or other characters. Tip: When writing multi-line comments, use the `/* ... */` style if you want automatic code formatters...
  - 正例/示例:
    /*
     * This is          // And so           /* Or you can
     * okay.            // is this.          * even do this. */
     */

18. 【强制】TODO comments: Use `TODO` comments for code that is temporary, a short-term solution, or good-enough but not perfect. A `TODO` comment begins with the word `TODO` in all caps, a following colon, and a link to a resource that contains the context, ideally a bug reference. A bug reference is preferable because bugs are tracked and have follow-up comments. Follow this piece of context with an explanatory string introduced with a...
  - 正例/示例:
    // TODO: crbug.com/12345678 - Remove this after the 2047q4 compatibility window expires.

19. 【强制】Modifiers: Class and member modifiers, when present, appear in the order recommended by the Java Language Specification: Modifiers on `requires` module directives, when present, appear in the following order:
  - 正例/示例:
    public protected private abstract default static final sealed non-sealed
      transient volatile synchronized native strictfp

20. 【强制】Numeric Literals: `long`-valued integer literals use an uppercase `L` suffix, never lowercase (to avoid confusion with the digit `1`). For example, `3000000000L` rather than `3000000000l`.

21. 【强制】Text Blocks: The opening `"""` of a text block is always on a new line. That line may either follow the same indentation rules as other constructs, or it may have no indentation at all (so it starts at the left margin). The closing `"""` is on a new line with the same indentation as the opening `"""`, and may be followed on the same line by further code. Each line of text in the text block is indented at least as much as the...

## Naming

### Rules common to all identifiers

1. 【强制】Identifiers use only ASCII letters and digits, and, in a small number of cases noted below, underscores. Thus each valid identifier name is matched by the regular expression `\w+` . In Google Style, special prefixes or suffixes are not used. For example, these names are not Google Style: `name_`, `mName`, `s_name` and `kName`.

### Rules by identifier type

1. 【强制】Package and module names: Package and module names use only lowercase letters and digits (no underscores). Consecutive words are simply concatenated together. For example, `com.example.deepspace`, not `com.example.deepSpace` or `com.example.deep_space`.

2. 【强制】Class names: Class names are written in UpperCamelCase. Class names are typically nouns or noun phrases. For example, `Character` or `ImmutableList`. Interface names may also be nouns or noun phrases (for example, `List`), but may sometimes be adjectives or adjective phrases instead (for example, `Readable`). There are no specific rules or even well-established conventions for naming annotation types. A test class has a name...

3. 【强制】Method names: Method names are written in lowerCamelCase. Method names are typically verbs or verb phrases. For example, `sendMessage` or `stop`. Underscores may appear in JUnit test method names to separate logical components of the name, with each component written in lowerCamelCase, for example `transferMoney_deductsFromSource`. There is no One Correct Way to name test methods.

4. 【强制】Constant names: Constant names use `UPPER_SNAKE_CASE`: all uppercase letters, with each word separated from the next by a single underscore. But what is a constant, exactly? Constants are static final fields whose contents are deeply immutable and whose methods have no detectable side effects. Examples include primitives, strings, immutable value classes, and anything set to `null`. If any of the instance's observable state can...
  - 正例/示例:
    // Constants
    static final int NUMBER = 5;
    static final ImmutableList<String> NAMES = ImmutableList.of("Ed", "Ann");
    static final Map<String, Integer> AGES = ImmutableMap.of("Ed", 35, "Ann", 32);
    static final Joiner COMMA_JOINER = Joiner.on(','); // because Joiner is immutable
    static final SomeMutableType[] EMPTY_ARRAY = {};
    // Not constants
    static String nonFinal = "non-final";
    final String nonStatic = "non-static";
    static final Set<String> mutableCollection = new HashSet<String>();
    static final ImmutableSet<SomeMutableType> mutableElements = ImmutableSet.of(mutable);
    static final ImmutableMap<String, SomeMutableType> mutableValues =
        ImmutableMap.of("Ed", mutableInstance, "Ann", mutableInstance2);
    static final Logger logger = Logger.getLogger(MyClass.getName());
    static final String[] nonEmptyArray = {"these", "can", "change"};

5. 【强制】Non-constant field names: Non-constant field names (static or otherwise) are written in lowerCamelCase. These names are typically nouns or noun phrases. For example, `computedValues` or `index`.

6. 【强制】Parameter names: Parameter names are written in lowerCamelCase. One-character parameter names in public methods should be avoided.

7. 【强制】Local variable names: Local variable names are written in lowerCamelCase. Even when final and immutable, local variables are not considered to be constants, and should not be styled as constants.

8. 【强制】Type variable names: Each type variable is named in one of two styles: A single capital letter, optionally followed by a single numeral (such as `E`, `T`, `X`, `T2`) A name in the form used for classes (see Section 5.2.2, Class names), followed by the capital letter `T` (examples: `RequestT`, `FooBarT`).

9. 【强制】Unnamed variables: The `_` syntax for unnamed variables and parameters is allowed wherever it is applicable. For example:
  - 正例/示例:
    Predicate<String> alwaysTrue = _ -> true;

### Camel case: defined

1. 【强制】Sometimes there is more than one reasonable way to convert an English phrase into camel case, such as when acronyms or unusual constructs like "IPv6" or "iOS" are present. To improve predictability, Google Style specifies the following (nearly) deterministic scheme. Beginning with the prose form of the name: Convert the phrase to plain ASCII and remove any apostrophes. For example, "Müller's algorithm" might become...

## Programming Practices

### `@Override`: always used

1. 【强制】A method is marked with the `@Override` annotation whenever it is legal. This includes a class method overriding a superclass method, a class method implementing an interface method, an interface method respecifying a superinterface method, and an explicitly declared accessor method for a record component. Exception: `@Override` may be omitted when the parent method is `@Deprecated`.

### Caught exceptions: not ignored

1. 【强制】It is very rarely correct to do nothing in response to a caught exception. (Typical responses are to log it, or if it is considered "impossible", rethrow it as an `AssertionError`.) When it truly is appropriate to take no action whatsoever in a catch block, the reason this is justified is explained in a comment.
  - 正例/示例:
    try {
      int i = Integer.parseInt(response);
      return handleNumericResponse(i);
    } catch (NumberFormatException _) {
      // it's not numeric; that's fine, just continue
    }
    return handleTextResponse(response);

### Static members: qualified using class

1. 【强制】When a reference to a static class member must be qualified, it is qualified with that class's name, not with a reference or expression of that class's type.
  - 正例/示例:
    Foo aFoo = ...;
    Foo.aStaticMethod(); // good
    aFoo.aStaticMethod(); // bad
    somethingThatYieldsAFoo().aStaticMethod(); // very bad

### Finalizers: not used

1. 【强制】Do not override `Object.finalize`. Finalization support is scheduled for removal.

## Javadoc

### Formatting

1. 【强制】General form: The basic formatting of Javadoc blocks is as seen in this example: ... or in this single-line example: The basic form is always acceptable. The single-line form may be substituted when the entirety of the Javadoc block (including comment markers) can fit on a single line. Note that this only applies when there are no block tags such as `@param`.
  - 正例/示例:
    /**
     * Multiple lines of Javadoc text are written here,
     * wrapped normally...
     */
    public int method(String p1) { ... }

2. 【强制】Paragraphs: One blank line—that is, a line containing only the aligned leading asterisk (`*`)—appears between paragraphs, and before the group of block tags if present. Each paragraph except the first has `<p>` immediately before the first word, with no space after it. HTML tags for other block-level elements, such as `<ul>` or `<table>`, are not preceded with `<p>`.

3. 【强制】Block tags: Any of the standard "block tags" that are used appear in the order `@param`, `@return`, `@throws`, `@deprecated`, and these four types never appear with an empty description. When a block tag doesn't fit on a single line, continuation lines are indented four (or more) spaces from the position of the `@`.

### The summary fragment

1. 【强制】Each Javadoc block begins with a brief summary fragment. This fragment is very important: it is the only part of the text that appears in certain contexts such as class and method indexes. This is a fragment—a noun phrase or verb phrase, not a complete sentence. It does not begin with `A {@code Foo} is a...`, or `This method returns...`, nor does it form a complete imperative sentence like `Save the record.`...

### Where Javadoc is used

1. 【强制】At the minimum, Javadoc is present for every visible class, member, or record component, with a few exceptions noted below. A top-level class is visible if it is `public`; a member is visible if it is `public` or `protected` and its containing class is visible; and a record component is visible if its containing record is visible. Additional Javadoc content may also be present, as explained in Section 7.3.4...

2. 【强制】Exception: self-explanatory members: Javadoc is optional for "simple, obvious" members and record components, such as a `getFoo()` method, if there really and truly is nothing else worthwhile to say but "the foo". Important: it is not appropriate to cite this exception to justify omitting relevant information that a typical reader might need to know. For example, for a record component named `canonicalName`, don't omit its documentation (with the...

3. 【强制】Exception: overrides: Javadoc is not always present on a method that overrides a supertype method.

4. 【强制】Non-required Javadoc: Other classes, members, and record components have Javadoc as needed or desired. Whenever an implementation comment would be used to define the overall purpose or behavior of a class or member, that comment is written as Javadoc instead (using `/**`). Non-required Javadoc is not strictly required to follow the formatting rules of Sections 7.1.1, 7.1.2, 7.1.3, and 7.2, though it is of course recommended.
