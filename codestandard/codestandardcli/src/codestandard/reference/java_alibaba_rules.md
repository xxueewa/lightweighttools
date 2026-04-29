# Java 开发手册（黄山版）规则集

来源: `java_manual_huangshan_qna.jsonl`
规则数量: 324

## 使用说明

- 【强制】: 必须遵守，代码生成、修改和评审时应优先处理。
- 【推荐】: 建议遵守；如与项目现有规范冲突，应说明原因。
- 【参考】: 作为设计、评审和重构时的参考建议。

## 编程规约

### 命名风格

1. 【强制】所有编程相关的命名均不能以下划线或美元符号开始，也不能以下划线或美元符号结束。
  - 反例:
    _name / __name / $Object / name_ / name$ / Object$

2. 【强制】所有编程相关的命名严禁使用拼音与英文混合的方式，更不允许直接使用中文的方式。
  - 正例:
    ali / alibaba / taobao / kaikeba / aliyun / youku / hangzhou 等国际通用的名称，可视同英文。
  - 反例:
    DaZhePromotion【打折】/ getPingfenByName()【评分】 / String fw【福娃】/ int 变量名 = 3

3. 【强制】代码和注释中都要避免使用任何人类语言中的种族歧视性或侮辱性词语。
  - 正例:
    blockList / allowList / secondary
  - 反例:
    blackList / whiteList / slave / SB / WTF

4. 【强制】类名使用 UpperCamelCase 风格，以下情形例外：
  - 正例:
    ForceCode / UserDO / HtmlDTO / XmlService / TcpUdpDeal / TaPromotion
  - 反例:
    forcecode / UserDo / HTMLDto / XMLService / TCPUDPDeal / TAPromotion

5. 【强制】方法名、参数名、成员变量、局部变量都统一使用 lowerCamelCase 风格。
  - 正例:
    localValue / getHttpMessage() / inputUserId

6. 【强制】常量命名应该全部大写，单词间用下划线隔开，力求语义表达完整清楚，不要嫌名字长。
  - 正例:
    MAX_STOCK_COUNT / CACHE_EXPIRED_TIME
  - 反例:
    MAX_COUNT / EXPIRED_TIME

7. 【强制】抽象类命名使用 Abstract 或 Base 开头；

8. 【强制】类型与中括号紧挨相连来定义数组。
  - 正例:
    定义整形数组 int[] arrayDemo。
  - 反例:
    在 main 参数中，使用 String args[] 来定义。

9. 【强制】POJO 类中的任何布尔类型的变量，都不要加 is 前缀，否则部分框架解析会引起序列化错误。
  - 反例:
    定义为布尔类型 Boolean isDeleted 的字段，它的 getter 方法也是 isDeleted()，部分框架在反向解析时，“误以
    为”对应的字段名称是 deleted，导致字段获取不到，得到意料之外的结果或抛出异常。

10. 【强制】包名统一使用小写，点分隔符之间有且仅有一个自然语义的英语单词。
  - 正例:
    应用工具类包名为 com.alibaba.ei.kunlun.aap.util；类名为 MessageUtils（此规则参考 spring 的框架结构）。

11. 【强制】避免在子父类的成员变量之间、或者不同代码块的局部变量之间采用完全相同的命名，使可理 解性降低。
  - 反例:
    public class ConfusingName {
    protected int stock;
    protected String alibaba;
    // 非 setter/getter 的参数名称，不允许与本类成员变量同名
    public void access(String alibaba) {
    if (condition) {
    final int money = 666;
    // ...
    }
    for (int i = 0; i < 10; i++) {
    // 在同一方法体中，不允许与其它代码块中的 money 命名相同
    final int money = 15978;
    // ...
    }
    }
    }
    class Son extends ConfusingName {
    // 不允许与父类的成员变量名称相同
    private int stock;
    }

12. 【强制】杜绝完全不规范的英文缩写，避免望文不知义。
  - 反例:
    AbstractClass“缩写”成 AbsClass；condition“缩写”成 condi；Function“缩写”成 Fu，此类随意缩写
    严重降低了代码的可阅读性。

13. 【推荐】为了达到代码自解释的目标，任何自定义编程元素在命名时，使用完整的单词组合来表达。
  - 正例:
    在 JDK 中，对某个对象引用的 volatile 字段进行原子更新的类名为 AtomicReferenceFieldUpdater。
  - 反例:
    常见的方法内变量为 int a; 的定义方式。

14. 【推荐】在常量与变量命名时，表示类型的名词放在词尾，以提升辨识度。
  - 正例:
    startTime / workQueue / nameList / TERMINATED_THREAD_COUNT
  - 反例:
    startedAt / QueueOfWork / listName / COUNT_TERMINATED_THREAD

15. 【推荐】如果模块、接口、类、方法使用了设计模式，在命名时要体现出具体模式。
  - 正例:
    public class OrderFactory;
    public class LoginProxy;
    public class ResourceObserver;

16. 【推荐】接口类中的方法和属性不要加任何修饰符号（public 也不要加），保持代码的简洁性，并加上 有效的 Javadoc 注释。
  - 正例:
    接口方法签名 void commit();
    接口基础常量 String COMPANY = "alibaba";
  - 反例:
    接口方法定义 public abstract void commit();

17. 【强制】对于 Service 和 DAO 类，基于 SOA 的理念，暴露出来的服务一定是接口，内部的实现类用 Impl 的后缀 与接口区别。
  - 正例:
    CacheServiceImpl 实现 CacheService 接口。

18. 【推荐】如果是形容能力的接口名称，取对应的形容词为接口名（通常是 –able 结尾的形容词）。
  - 正例:
    AbstractTranslator 实现 Translatable。

19. 【参考】枚举类名带上 Enum 后缀，枚举成员名称需要全大写，单词间用下划线隔开。
  - 正例:
    枚举名字为 ProcessStatusEnum 的成员名称：SUCCESS / UNKNOWN_REASON

20. 【参考】各层命名规约：

### 常量定义

1. 【强制】不允许任何魔法值（即未经预先定义的常量）直接出现在代码中。
  - 反例:
    // 开发者 A 定义了缓存的 key。
    String key = "Id#taobao_" + tradeId;
    cache.put(key, value);
    // 开发者 B 使用缓存时直接复制少了下划线，即 key 是"Id#taobao" + tradeId，导致出现故障。
    String key = "Id#taobao" + tradeId;
    cache.get(key);

2. 【强制】long 或 Long 赋值时，数值后使用大写 L，不能是小写 l，小写容易跟数字混淆，造成误解。

3. 【强制】浮点数类型的数值后缀统一为大写的 D 或 F。
  - 正例:
    public static final double HEIGHT = 175.5D;
    public static final float WEIGHT = 150.3F;

4. 【推荐】不要使用一个常量类维护所有常量，要按常量功能进行归类，分开维护。
  - 正例:
    缓存相关常量放在类 CacheConsts 下；系统配置相关常量放在类 SystemConfigConsts 下。

5. 【推荐】常量的复用层次有五层：
  - 反例:
    易懂常量也要统一定义成应用内共享常量，两个程序员在两个类中分别定义了表示“是”的常量：
    类 A 中：public static final String YES = "yes";
    类 B 中：public static final String YES = "y";
    A.YES.equals(B.YES)，预期是 true，但实际返回为 false，导致线上问题。
    3）子工程内部共享常量：即在当前子工程的 constant 目录下。
    4）包内共享常量：即在当前包下单独的 constant 目录下。
    5）类内共享常量：直接在类内部 private static final 定义。

6. 【推荐】如果变量值仅在一个固定范围内变化用 enum 类型来定义。
  - 正例:
    public enum SeasonEnum {
    SPRING(1), SUMMER(2), AUTUMN(3), WINTER(4);
    private int seq;
    SeasonEnum(int seq) {
    this.seq = seq;
    }
    public int getSeq() {
    return seq;
    }
    }

### 代码格式

1. 【强制】如果大括号内为空，简洁地写成{}即可，大括号中间无需换行和空格；

2. 【强制】左小括号和右边相邻字符之间不需要空格；
  - 反例:
    if(空格 a == b 空格)

3. 【强制】if / for / while / switch / do 等保留字与左右括号之间都必须加空格。

4. 【强制】任何二目、三目运算符的左右两边都需要加一个空格。

5. 【强制】采用 4 个空格缩进，禁止使用 Tab 字符。
  - 正例:
    （涉及上述中的 1-5 点）
    public static void main(String[] args) {
    // 缩进 4 个空格
    String say = "hello";
    // 运算符的左右必须有一个空格
    int flag = 0;
    // 关键词 if 与括号之间必须有一个空格，括号内的 f 与左括号，0 与右括号不需要空格
    if (flag == 0) {
    System.out.println(say);
    }
    // 左大括号前加空格且不换行；左大括号后换行
    if (flag == 1) {
    System.out.println("world");
    // 右大括号前换行，右大括号后有 else，不用换行
    } else {
    System.out.println("ok");
    // 在右大括号后直接结束，则必须换行
    }
    }

6. 【强制】注释的双斜线与注释内容之间有且仅有一个空格。
  - 正例:
    // 这是示例注释，请注意在双斜线之后有一个空格
    String commentString = new String("demo");

7. 【强制】在进行类型强制转换时，右括号与强制转换值之间不需要任何空格隔开。
  - 正例:
    double first = 3.2D;
    int second = (int)first + 2;

8. 【强制】单行字符数限制不超过 120 个，超出需要换行，换行时遵循如下原则：
  - 正例:
    StringBuilder builder = new StringBuilder();
    // 超过 120 个字符的情况下，换行缩进 4 个空格，并且方法前的点号一起换行
    builder.append("yang").append("hao")...
    .append("chen")...
    .append("chen")...
    .append("chen");
  - 反例:
    StringBuilder builder = new StringBuilder();
    // 超过 120 个字符的情况下，不要在括号前换行
    builder.append("you").append("are")...append
    ("lucky");
    // 参数很多的方法调用可能超过 120 个字符，逗号后才是换行处
    method(args1, args2, args3, ...
    , argsX);

9. 【强制】方法参数在定义和传入时，多个参数逗号后面必须加空格。
  - 正例:
    下例中实参的 args1 逗号后边必须要有一个空格。
    method(args1, args2, args3);

10. 【强制】IDE 的 text file encoding 设置为 UTF-8；

11. 【推荐】单个方法的总行数不超过 80 行。
  - 正例:
    代码逻辑分清红花和绿叶，个性和共性，绿叶逻辑单独出来成为额外方法，使主干代码更加晰；共性逻辑抽取
    成为共性方法，便于复用和维护。

12. 【推荐】没有必要增加若干空格来使变量的赋值等号与上一行对应位置的等号对齐。
  - 正例:
    int one = 1;
    long two = 2L;
    float three = 3F;
    StringBuilder builder = new StringBuilder();

13. 【推荐】不同逻辑、不同语义、不同业务的代码之间插入一个空行，分隔开来以提升可读性。

### OOP 规约

1. 【强制】避免通过一个类的对象引用访问此类的静态变量或静态方法，无谓增加编译器解析成本，直接用 类名来访问即可。

2. 【强制】所有的覆写方法，必须加 @Override 注解。

3. 【强制】相同参数类型，相同业务含义，才可以使用的可变参数，参数类型避免定义为 Object。
  - 正例:
    public List<User> listUsers(String type, Long... ids) {...}

4. 【强制】外部正在调用的接口或者二方库依赖的接口，不允许修改方法签名，避免对接口调用方产生影 响。

5. 【强制】不能使用过时的类或方法。

6. 【强制】Object 的 equals 方法容易抛空指针异常，应使用常量或确定有值的对象来调用 equals。
  - 正例:
    "test".equals(param);
  - 反例:
    param.equals("test");

7. 【强制】所有整型包装类对象之间值的比较，全部使用 equals 方法比较。

8. 【强制】任何货币金额，均以最小货币单位且为整型类型进行存储。

9. 【强制】浮点数之间的等值判断，基本数据类型不能使用 == 进行比较，包装数据类型不能使用 equals 进行判断。
  - 正例:
    (1)指定一个误差范围，两个浮点数的差值在此范围之内，则认为是相等的。
    float a = 1.0F - 0.9F;
    float b = 0.9F - 0.8F;
    float diff = 1e-6F;
    if (Math.abs(a - b) < diff) {
    System.out.println("true");
    }
    (2)使用 BigDecimal 来定义值，再进行浮点数的运算操作。
    BigDecimal a = new BigDecimal("1.0");
    BigDecimal b = new BigDecimal("0.9");
    BigDecimal c = new BigDecimal("0.8");
    BigDecimal x = a.subtract(b);
    BigDecimal y = b.subtract(c);
    if (x.compareTo(y) == 0) {
    System.out.println("true");
    }
  - 反例:
    float a = 1.0F - 0.9F;
    float b = 0.9F - 0.8F;
    if (a == b) {
    // 预期进入此代码块，执行其它业务逻辑
    // 但事实上 a == b 的结果为 false
    }
    Float x = Float.valueOf(a);
    Float y = Float.valueOf(b);
    if (x.equals(y)) {
    // 预期进入此代码块，执行其它业务逻辑
    // 但事实上 equals 的结果为 false
    }

10. 【强制】BigDecimal 的等值比较应使用 compareTo() 方法，而不是 equals() 方法。

11. 【强制】定义数据对象 DO 类时，属性类型要与数据库字段类型相匹配。
  - 正例:
    数据库字段的 bigint 必须与类属性的 Long 类型相对应。
  - 反例:
    某业务的数据库表 id 字段定义类型为 bigint unsigned，实际类对象属性为 Integer，随着 id 越来越大，
    超过 Integer 的表示范围而溢出成为负数，此时数据库 id 不支持存入负数抛出异常产生线上故障。

12. 【强制】禁止使用构造方法 BigDecimal(double) 的方式把 double 值转化为 BigDecimal 对象。
  - 正例:
    优先推荐入参为 String 的构造方法，或使用 BigDecimal 的 valueOf 方法，此方法内部其实执行了 Double 的
    toString，而 Double 的 toString 按 double 的实际能表达的精度对尾数进行了截断。
    BigDecimal recommend1 = new BigDecimal("0.1");
    BigDecimal recommend2 = BigDecimal.valueOf(0.1);
    13.关于基本数据类型与包装数据类型的使用标准如下：

13. 【强制】所有的 POJO 类属性必须使用包装数据类型。

14. 【强制】RPC 方法的返回值和参数必须使用包装数据类型。

15. 【推荐】所有的局部变量使用基本数据类型。
  - 正例:
    数据库的查询结果可能是 null，因为自动拆箱，用基本数据类型接收有 NPE 风险。
  - 反例:
    某业务的交易报表上显示成交总额涨跌情况，即正负 x%，x 为基本数据类型，调用的 RPC 服务，调用不成功时，
    返回的是默认值，页面显示为 0%，这是不合理的，应该显示成中划线-。所以包装数据类型的 null 值，能够表示额外的
    信息，如：远程调用失败，异常退出。

16. 【强制】定义 DO / PO / DTO / VO 等 POJO 类时，不要设定任何属性默认值。
  - 反例:
    某业务的 DO 的 createTime 默认值为 new Date()；但是这个属性在数据提取时并没有置入具体值，在更新其
    它字段时又附带更新了此字段，导致创建时间被修改成当前时间。

17. 【强制】序列化类新增属性时，请不要修改 serialVersionUID 字段，避免反序列失败；

18. 【强制】构造方法里面禁止加入任何业务逻辑，如果有初始化逻辑，请放在 init 方法中。

19. 【强制】POJO 类必须写 toString 方法。

20. 【强制】禁止在 POJO 类中，同时存在对应属性 xxx 的 isXxx() 和 getXxx() 方法。

21. 【推荐】使用索引访问用 String 的 split 方法得到的数组时，需做最后一个分隔符后有无内容的检查， 否则会有抛 IndexOutOfBoundsException 的风险。

22. 【推荐】当一个类有多个构造方法，或者多个同名方法，这些方法应该按顺序放置在一起，便于阅读， 此条规则优先于下一条。
  - 正例:
    public int method(int param);
    protected double method(int param1, int param2);
    private void method();

23. 【推荐】类内方法定义的顺序依次是：

24. 【推荐】setter 方法中，参数名称与类成员变量名称一致，this.成员名=参数名。
  - 反例:
    public Integer getData() {
    if (condition) {
    return this.data + 100;
    } else {
    return this.data - 100;
    }
    }

25. 【推荐】循环体内，字符串的连接方式，使用 StringBuilder 的 append 方法进行扩展。
  - 反例:
    String str = "start";
    for (int i = 0; i < 100; i++) {
    str = str + "hello";
    }

26. 【推荐】final 可以声明类、成员变量、方法、以及本地变量，下列情况使用 final 关键字：

27. 【推荐】慎用 Object 的 clone 方法来拷贝对象。

28. 【推荐】类成员与方法访问控制从严：

### 日期时间

1. 【强制】日期格式化时，传入 pattern 中表示年份统一使用小写的 y。
  - 正例:
    表示日期和时间的格式如下所示：
    new SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
  - 反例:
    某程序员因使用 YYYY/MM/dd 进行日期格式化，2017/12/31 执行结果为 2018/12/31，造成线上故障。

2. 【强制】在日期格式中分清楚大写的 M 和小写的 m，大写的 H 和小写的 h 分别指代的意义。

3. 【强制】获取当前毫秒数：

4. 【强制】不允许在程序任何地方中使用：
  - 反例:
    java.util.Date.after(Date) 进行时间比较时，当入参是 java.sql.Timestamp 时，会触发 JDK BUG（JDK9 已修
    复），可能导致比较时的意外结果。

5. 【强制】禁止在程序中写死一年为 365 天，避免在公历闰年时出现日期转换错误或程序逻辑错误。
  - 正例:
    // 获取今年的天数
    int daysOfThisYear = LocalDate.now().lengthOfYear();
    // 获取指定某年的天数
    LocalDate.of(2011, 1, 1).lengthOfYear();
  - 反例:
    // 第一种情况：在闰年 366 天时，出现数组越界异常
    int[] dayArray = new int[365];
    // 第二种情况：一年有效期的会员制，2020 年 1 月 26 日注册，硬编码 365 返回的却是 2021 年 1 月 25 日
    Calendar calendar = Calendar.getInstance();
    calendar.set(2020, 1, 26);
    calendar.add(Calendar.DATE, 365);

6. 【推荐】避免公历闰年 2 月问题。

7. 【推荐】使用枚举值来指代月份。
  - 正例:
    Calendar.JANUARY，Calendar.FEBRUARY，Calendar.MARCH 等来指代相应月份来进行传参或比较。

### 集合处理

1. 【强制】关于 hashCode 和 equals 的处理，遵循如下规则：

2. 【强制】判断所有集合内部的元素是否为空，使用 isEmpty() 方法，而不是 size() == 0 的方式。
  - 正例:
    Map<String, Object> map = new HashMap<>(16);
    if (map.isEmpty()) {
    System.out.println("no element in this map.");
    }

3. 【强制】在使用 java.util.stream.Collectors 类的 toMap() 方法转为 Map 集合时，一定要使用参数类型 为 BinaryOperator，参数名为 mergeFunction 的方法，否则当出现相同 key 时会抛出 IllegalStateException 异常。
  - 正例:
    List<Pair<String, Double>> pairArrayList = new ArrayList<>(3);
    pairArrayList.add(new Pair<>("version", 12.10));
    pairArrayList.add(new Pair<>("version", 12.19));
    pairArrayList.add(new Pair<>("version", 6.28));
    // 生成的 map 集合中只有一个键值对：{version=6.28}
    Map<String, Double> map = pairArrayList.stream()
    .collect(Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2));
  - 反例:
    String[] departments = new String[]{"RDC", "RDC", "KKB"};
    // 抛出 IllegalStateException 异常
    Map<Integer, String> map = Arrays.stream(departments)
    .collect(Collectors.toMap(String::hashCode, str -> str));

4. 【强制】在使用 java.util.stream.Collectors 类的 toMap() 方法转为 Map 集合时，一定要注意当 value 为 null 时会抛 NPE 异常。
  - 反例:
    List<Pair<String, Double>> pairArrayList = new ArrayList<>(2);
    pairArrayList.add(new Pair<>("version1", 8.3));
    pairArrayList.add(new Pair<>("version2", null));
    // 抛出 NullPointerException 异常
    Map<String, Double> map = pairArrayList.stream()
    .collect(Collectors.toMap(Pair::getKey, Pair::getValue, (v1, v2) -> v2));

5. 【强制】ArrayList 的 subList 结果不可强转成 ArrayList，否则会抛出 ClassCastException 异常：

6. 【强制】使用 Map 的方法 keySet() / values() / entrySet() 返回集合对象时，不可以对其进行添加元素 操作，否则会抛出 UnsupportedOperationException 异常。

7. 【强制】Collections 类返回的对象，如：
  - 反例:
    如果查询无结果，返回 Collections.emptyList() 空集合对象，调用方一旦在返回的集合中进行了添加元素的操
    作，就会触发 UnsupportedOperationException 异常。

8. 【强制】在 subList 场景中，高度注意对父集合元素的增加或删除，均会导致子列表的遍历、增加、删 除产生 ConcurrentModificationException 异常。

9. 【强制】使用集合转数组的方法，必须使用集合的 toArray(T[] array)，传入的是类型完全一致、长度为 0 的空数组。
  - 正例:
    List<String> list = new ArrayList<>(2);
    list.add("guan");
    list.add("bao");
    String[] array = list.toArray(new String[0]);
  - 反例:
    直接使用 toArray 无参方法存在问题，此方法返回值只能是 Object[]类，若强转其它类型数组将出现
    ClassCastException 错误。

10. 【强制】使用 Collection 接口任何实现类的 addAll() 方法时，要对输入的集合参数进行 NPE 判断。

11. 【强制】使用工具类 Arrays.asList() 把数组转换成集合时，不能使用其修改集合相关的方法，它的 add / remove / clear 方法会抛出 UnsupportedOperationException 异常。

12. 【强制】泛型通配符<? extends T>来接收返回的数据，此写法的泛型集合不能使用 add 方法， 而<? super T>不能使用 get 方法，两者在接口调用赋值的场景中容易出错。

13. 【强制】在无泛型限制定义的集合赋值给泛型限制的集合时，在使用集合元素时，需要进行 instanceof 判断，避免抛出 ClassCastException 异常。
  - 反例:
    List<String> generics = null;
    List notGenerics = new ArrayList(10);
    notGenerics.add(new Object());
    notGenerics.add(new Integer(1));
    generics = notGenerics;
    // 此处抛出 ClassCastException 异常
    String string = generics.get(0);

14. 【强制】不要在 foreach 循环里进行元素的 remove / add 操作。
  - 正例:
    List<String> list = new ArrayList<>();
    list.add("1");
    list.add("2");
    Iterator<String> iterator = list.iterator();
    while (iterator.hasNext()) {
    String item = iterator.next();
    if (删除元素的条件) {
    iterator.remove();
    }
    Vector类也有 toArray方法
    }
  - 反例:
    for (String item : list) {
    if ("1".equals(item)) {
    list.remove(item);
    }
    }

15. 【强制】在 JDK7 版本及以上，Comparator 实现类要满足如下三个条件，不然 Arrays.sort， Collections.sort 会抛 IllegalArgumentException 异常。
  - 反例:
    下例中没有处理相等的情况，交换两个对象判断结果并不互反，不符合第一个条件，在实际使用中可能会出现异
    常。
    new Comparator<Student>() {
    @Override
    public int compare(Student o1, Student o2) {
    return o1.getId() > o2.getId() ? 1 : -1;
    }
    };

16. 【推荐】泛型集合使用时，在 JDK7 及以上，使用 diamond 语法或全省略。
  - 正例:
    // diamond 方式，即<>
    HashMap<String, String> userCache = new HashMap<>(16);
    // 全省略方式
    ArrayList<User> users = new ArrayList(10);

17. 【推荐】集合初始化时，指定集合初始值大小。
  - 正例:
    initialCapacity = (需要存储的元素个数 / 负载因子) + 1。注意负载因子（即 loaderfactor）默认为 0.75，如果
    暂时无法确定初始值大小，请设置为 16（即默认值）。
  - 反例:
    HashMap 需要放置 1024 个元素，由于没有设置容量初始大小，随着元素增加而被迫不断扩容，resize() 方法
    总共会调用 8 次，反复重建哈希表和数据迁移。当放置的集合元素个数达 千万级时会影响程序性能。

18. 【推荐】使用 entrySet 遍历 Map 类集合 KV，而不是 keySet 方式进行遍历。
  - 正例:
    values() 返回的是 V 值集合，是一个 list 集合对象；keySet() 返回的是 K 值集合，是一个 Set 集合对象；
    entrySet() 返回的是 K-V 值组合的 Set 集合。

19. 【推荐】高度注意 Map 类集合 K / V 能不能存储 null 值的情况，如下表格：
  - 反例:
    由于 HashMap 的干扰，很多人认为 ConcurrentHashMap 是可以置入 null 值，而事实上，存储 null 值时会抛
    出 NPE 异常。

20. 【参考】合理利用好集合的有序性（sort）和稳定性（order），避免集合的无序性（unsort）和不稳定 性（unorder）带来的负面影响。

21. 【参考】利用 Set 元素唯一的特性，可以快速对一个集合进行去重操作，避免使用 List 的 contains() 进行遍历去重或者判断包含操作。

### 并发处理

1. 【强制】获取单例对象需要保证线程安全，其中的方法也要保证线程安全。

2. 【强制】创建线程或线程池时请指定有意义的线程名称，方便出错时回溯。
  - 正例:
    自定义线程工厂，并且根据外部特征进行分组，比如，来自同一机房的调用，把机房编号赋值给
    whatFeatureOfGroup：
    public class UserThreadFactory implements ThreadFactory {
    private final String namePrefix;
    private final AtomicInteger nextId = new AtomicInteger(1);
    // 定义线程组名称，在利用 jstack 来排查问题时，非常有帮助
    UserThreadFactory(String whatFeatureOfGroup) {
    namePrefix = "FromUserThreadFactory's" + whatFeatureOfGroup + "-Worker-";
    }
    @Override
    public Thread newThread(Runnable task) {
    String name = namePrefix + nextId.getAndIncrement();
    Thread thread = new Thread(null, task, name, 0, false);
    System.out.println(thread.getName());
    return thread;
    }
    }

3. 【强制】线程资源必须通过线程池提供，不允许在应用中自行显式创建线程。

4. 【强制】线程池不允许使用 Executors 去创建，而是通过 ThreadPoolExecutor 的方式，这样的处理方 式让写的同学更加明确线程池的运行规则，规避资源耗尽的风险。

5. 【强制】SimpleDateFormat 是线程不安全的类，一般不要定义为 static 变量，如果定义为 static，必须 加锁，或者使用 DateUtils 工具类。
  - 正例:
    注意线程安全，使用 DateUtils。亦推荐如下处理：
    private static final ThreadLocal<DateFormat> dateStyle = new ThreadLocal<DateFormat>() {
    @Override
    protected DateFormat initialValue() {
    return new SimpleDateFormat("yyyy-MM-dd");
    }
    };

6. 【强制】必须回收自定义的 ThreadLocal 变量记录的当前线程的值，尤其在线程池场景下，线程经常会 被复用，如果不清理自定义的 ThreadLocal 变量，可能会影响后续业务逻辑和造成内存泄露等问题。
  - 正例:
    objectThreadLocal.set(userInfo);
    try {
    // ...
    } finally {
    objectThreadLocal.remove();
    }

7. 【强制】高并发时，同步调用应该去考量锁的性能损耗。

8. 【强制】对多个资源、数据库表、对象同时加锁时，需要保持一致的加锁顺序，否则可能会造成死锁。

9. 【强制】在使用阻塞等待获取锁的方式中，必须在 try 代码块之外，并且在加锁方法与 try 代码块之间没 有任何可能抛出异常的方法调用，避免加锁成功后，在 finally 中无法解锁。
  - 正例:
    Lock lock = new XxxLock();
    // ...
    lock.lock();
    try {
    doSomething();
    doOthers();
    } finally {
    lock.unlock();
    }
  - 反例:
    Lock lock = new XxxLock();
    // ...
    try {
    // 如果此处抛出异常，则直接执行 finally 代码块
    doSomething();
    // 无论加锁是否成功，finally 代码块都会执行
    lock.lock();
    doOthers();
    } finally {
    lock.unlock();
    }

10. 【强制】在使用尝试机制来获取锁的方式中，进入业务代码块之前，必须先判断当前线程是否持有锁。
  - 正例:
    Lock lock = new XxxLock();
    // ...
    boolean isLocked = lock.tryLock();
    if (isLocked) {
    try {
    doSomething();
    doOthers();
    } finally {
    lock.unlock();
    }
    }

11. 【强制】并发修改同一记录时，避免更新丢失，需要加锁。

12. 【强制】多线程并行处理定时任务时，Timer 运行多个 TimeTask 时，只要其中之一没有捕获抛出的异 常，其它任务便会自动终止运行，使用 ScheduledExecutorService 则没有这个问题。

13. 【推荐】资金相关的金融敏感信息，使用悲观锁策略。
  - 正例:
    悲观锁遵循一锁二判三更新四释放的原则。

14. 【推荐】使用 CountDownLatch 进行异步转同步操作，每个线程退出前必须调用 countDown 方法，线 程执行代码注意 catch 异常，确保 countDown 方法被执行到，避免主线程无法执行至 await 方法， 直到超时才返回结果。

15. 【推荐】避免 Random 实例被多线程使用，虽然共享该实例是线程安全的，但会因竞争同一 seed 导致 的性能下降。
  - 正例:
    在 JDK7 之后，可以直接使用 API ThreadLocalRandom，而在 JDK7 之前，需要编码保证每个线程持有一个
    单独的 Random 实例。

16. 【推荐】通过双重检查锁（double-checked locking），实现延迟初始化需要将目标属性声明为 volatile 型，（比如修改 helper 的属性声明为 private volatile Helper helper = null;）。
  - 正例:
    public class LazyInitDemo {
    private volatile Helper helper = null;
    public Helper getHelper() {
    if (helper == null) {
    synchronized(this) {
    if (helper == null) {
    helper = new Helper();
    }
    }
    }
    return helper;
    }
    // other methods and fields...
    }

17. 【参考】volatile 解决多线程内存不可见问题对于一写多读，是可以解决变量同步问题，但是如果多 写，同样无法解决线程安全问题。

18. 【参考】HashMap 在容量不够进行 resize 时由于高并发可能出现死链，导致 CPU 飙升，在开发过程 中注意规避此风险。

19. 【参考】ThreadLocal 对象使用 static 修饰，ThreadLocal 无法解决共享对象的更新问题。

### 控制语句

1. 【强制】在一个 switch 块内，每个 case 要么通过 continue / break / return 等来终止，要么注释说明 程序将继续执行到哪一个 case 为止；

2. 【强制】当 switch 括号内的变量类型为 String 并且此变量为外部参数时，必须先进行 null 判断。
  - 反例:
    如下的代码输出是什么？
    public class SwitchString {
    public static void main(String[] args) {
    method(null);
    }
    public static void method(String param) {
    switch (param) {
    // 肯定不是进入这里
    case "sth":
    System.out.println("it's sth");
    break;
    // 也不是进入这里
    case "null":
    System.out.println("it's null");
    break;
    // 也不是进入这里
    default:
    System.out.println("default");
    }
    }
    }

3. 【强制】在 if / else / for / while / do 语句中必须使用大括号。
  - 反例:
    if (condition) statements;

4. 【强制】三目运算符 condition ? 表达式 1：
  - 反例:
    Integer a = 1;
    Integer b = 2;
    Integer c = null;
    Boolean flag = false;
    // a*b 的结果是 int 类型，那么 c 会强制拆箱成 int 类型，抛出 NPE 异常
    Integer result = (flag ? a * b : c);

5. 【强制】在高并发场景中，避免使用“等于”判断作为中断或退出的条件。
  - 反例:
    判断剩余奖品数量等于 0 时，终止发放奖品，但因为并发处理错误导致奖品数量瞬间变成了负数，这样的话，
    活动无法终止。

6. 【推荐】当方法的代码总行数超过 10 行时，return / throw 等中断逻辑的右大括号后需要加一个空行。

7. 【推荐】表达异常的分支时，少用 if-else 方式，这种方式可以改写成：
  - 正例:
    超过 3 层的 if-else 的逻辑判断代码可以使用卫语句、策略模式、状态模式等来实现，其中卫语句示例如下：
    public void findBoyfriend(Man man) {
    if (man.isUgly()) {
    System.out.println("本姑娘是外貌协会的资深会员");
    return;
    }
    if (man.isPoor()) {
    System.out.println("贫贱夫妻百事哀");
    return;
    }
    if (man.isBadTemper()) {
    System.out.println("银河有多远，你就给我滚多远");
    return;
    }
    System.out.println("可以先交往一段时间看看");
    }

8. 【推荐】除常用方法（如 getXxx / isXxx）等外不要在条件判断中执行其它复杂的语句，将复杂逻辑判 断的结果赋值给一个有意义的布尔变量名，以提高可读性。
  - 正例:
    // 伪代码如下
    final boolean existed = (file.open(fileName, "w") != null) && (...) || (...);
    if (existed) {
    ...
    }
  - 反例:
    public final void acquire(long arg) {
    if (!tryAcquire(arg) && acquireQueued(addWaiter(Node.EXCLUSIVE), arg)) {
    selfInterrupt();
    }
    }

9. 【推荐】不要在其它表达式（尤其是条件表达式）中，插入赋值语句。
  - 反例:
    public Lock getLock(boolean fair) {
    // 算术表达式中出现赋值操作，容易忽略 count 值已经被改变
    threshold = (count = Integer.MAX_VALUE) - 1;
    // 条件表达式中出现赋值操作，容易误认为是 sync == fair
    return (sync = fair) ? new FairSync() : new NonfairSync();
    }

10. 【推荐】循环体中的语句要考量性能，以下操作尽量移至循环体外处理，如定义对象、变量、获取数据 库连接，进行不必要的 try-catch 操作（这个 try-catch 是否可以移至循环体外）。

11. 【推荐】避免采用取反逻辑运算符。
  - 正例:
    使用 if(x < 628) 来表达 x 小于 628。
  - 反例:
    使用 if(!(x >= 628)) 来表达 x 小于 628。

12. 【推荐】公开接口需要进行入参保护，尤其是批量操作的接口。
  - 反例:
    某业务系统，提供一个用户批量查询的接口，API 文档上有说最多查多少个，但接口实现上没做任何保护，导致
    调用方传了一个 1000 的用户 id 数组过来后，查询信息后，内存爆了。

13. 【参考】下列情形，需要进行参数校验：

14. 【参考】下列情形，不需要进行参数校验：

### 注释规约

1. 【强制】类、类属性、类方法的注释必须使用 Javadoc 规范，使用 /** 内容 */ 格式，不得使用 // xxx 方式。

2. 【强制】所有的抽象方法（包括接口中的方法）必须要用 Javadoc 注释、除了返回值、参数异常说明 外，还必须指出该方法做什么事情，实现什么功能。

3. 【强制】所有的类都必须添加创建者和创建日期。
  - 正例:
    /**
    *
    * @author yangguanbao
    * @date 2021/11/26
    *
    **/

4. 【强制】方法内部单行注释，在被注释语句上方另起一行，使用 // 注释。

5. 【强制】所有的枚举类型字段必须要有注释，说明每个数据项的用途。

6. 【推荐】与其用半吊子英文来注释，不如用中文注释说清楚。
  - 反例:
    “TCP 连接超时”解释成“传输控制协议连接超时”，理解反而费脑筋。

7. 【推荐】代码修改的同时，注释也要进行相应的修改，尤其是参数、返回值、异常、核心逻辑等。

8. 【推荐】在类中删除未使用的任何字段和方法、内部类；

9. 【参考】谨慎注释掉代码。

10. 【参考】对于注释的要求：

11. 【参考】好的命名、代码结构是自解释的，注释力求精简准确、表达到位。
  - 反例:
    // put elephant into fridge
    put(elephant, fridge);
    方法名 put，加上两个有意义的变量名称 elephant 和 fridge，已经说明了这是在干什么，语义清晰的代码不需要额外
    的注释。

12. 【参考】特殊注释标记，请注明标记人与标记时间。

### 前后端规约

1. 【强制】前后端交互的 API，需要明确协议、域名、路径、请求方法、请求内容、状态码、响应体。

2. 【强制】前后端数据列表相关的接口返回，如果为空，则返回空数组[]或空集合{}。

3. 【强制】服务端发生错误时，返回给前端的响应信息必须包含 HTTP 状态码，errorCode、 errorMessage、用户提示信息四个部分。
  - 正例:
    常见的 HTTP 状态码如下
    1）200 OK：表明该请求被成功地完成，所请求的资源发送到客户端。
    2）401 Unauthorized：请求要求身份验证，常见对于需要登录而用户未登录的情况。
    3）403 Forbidden：服务器拒绝请求，常见于机密信息或复制其它登录用户链接访问服务器的情况。
    4）404 NotFound：服务器无法取得所请求的网页，请求资源不存在。
    5）500 InternalServerError：服务器内部错误。

4. 【强制】在前后端交互的 JSON 格式数据中，所有的 key 必须为小写字母开始的 lowerCamelCase 风格，符合英文表达习惯，且表意完整。
  - 正例:
    errorCode / errorMessage / assetStatus / menuList / orderList / configFlag
  - 反例:
    ERRORCODE / ERROR_CODE / error_message / error-message / errormessage

5. 【强制】errorMessage 是前后端错误追踪机制的体现，可以在前端输出到 type="hidden" 文字类控 件中，或者用户端的日志中，帮助我们快速地定位出问题。

6. 【强制】对于需要使用超大整数的场景，服务端一律使用 String 字符串类型返回，禁止使用 Long 类型。
  - 反例:
    通常在订单号或交易号大于等于 16 位，大概率会出现前后端订单数据不一致的情况。
    比如，后端传输的 "orderId"：362909601374617692，前端拿到的值却是：362909601374617660

7. 【强制】HTTP 请求通过 URL 传递参数时，不能超过 2048 字节。
  - 反例:
    某业务将退货的商品 id 列表放在 URL 中作为参数传递，当一次退货商品数量过多时，URL 参数超长，传递到后端的
    参数被截断，导致部分商品未能正确退货。

8. 【强制】HTTP 请求通过 body 传递内容时，必须控制长度，超出最大长度后，后端解析会出错。

9. 【强制】在翻页场景中，用户输入参数的小于 1，则前端返回第一页参数给后端；

10. 【强制】服务器内部重定向必须使用 forward；

11. 【推荐】服务器返回信息必须被标记是否可以缓存，如果缓存，客户端可能会重用之前的请求结果。
  - 正例:
    http1.1 中，s-maxage 告诉服务器进行缓存，时间单位为秒，用法如下，
    response.setHeader("Cache-Control", "s-maxage=" + cacheSeconds);

12. 【推荐】服务端返回的数据，使用 JSON 格式而非 XML。

13. 【推荐】前后端的时间格式统一为"yyyy-MM-dd HH:mm:ss"，统一为 GMT。

14. 【参考】在接口路径中不要加入版本号，版本控制在 HTTP 头信息中体现，有利于向前兼容。

### 其他

1. 【强制】在使用正则表达式时，利用好其预编译功能，可以有效加快正则匹配速度。

2. 【强制】避免用 ApacheBeanutils 进行属性的 copy。

3. 【强制】velocity 调用 POJO 类的属性时，直接使用属性名取值即可，模板引擎会自动按规范调用 POJO 的 getXxx()，如果是 boolean 基本数据类型变量（boolean 命名不需要加 is 前缀），会自动调 isXxx() 方法。

4. 【强制】后台输送给页面的变量必须加 $!{var} ——中间的感叹号。

5. 【强制】注意 Math.random() 这个方法返回是 double 类型，注意取值的范围 0 ≤ x < 1（能够 取到零值，注意除零异常），如果想获取整数类型的随机数，不要将 x 放大 10 的若干倍然后取 整，直接使用 Random 对象的 nextInt 或者 nextLong 方法。

6. 【强制】枚举 enum（括号内）的属性字段必须是私有且不可变。

7. 【推荐】不要在视图模板中加入任何复杂的逻辑运算。

8. 【推荐】任何数据结构的构造或初始化，都应指定大小，避免数据结构无限增长吃光内存。

9. 【推荐】及时清理不再使用的代码段或配置信息。
  - 正例:
    对于暂时被注释掉，后续可能恢复使用的代码片断，在注释代码上方，统一规定使用三个斜杠(///)
    来说明注释掉代码的理由：
    public static void hello() {
    /// 业务方通知活动暂停
    // Business business = new Business();
    // business.active();
    System.out.println("it's finished");
    }

## 异常日志

### 错误码

1. 【强制】错误码的制定原则：
  - 正例:
    错误码回答的问题是谁的错？错在哪？
    1）错误码必须能够快速知晓错误来源，可快速判断是谁的问题。
    2）错误码必须能够进行清晰地比对（代码中容易 equals）。
    3）错误码有利于团队快速对错误原因达到一致认知。

2. 【强制】错误码不体现版本号和错误等级信息。

3. 【强制】全部正常，但不得不填充错误码时返回五个零：

4. 【强制】错误码为字符串类型，共 5 位，分成两个部分：

5. 【强制】编号不与公司业务架构，更不与组织架构挂钩，以先到先得的原则在统一平台上进行，审批生 效，编号即被永久固定。

6. 【强制】错误码使用者避免随意定义新的错误码。

7. 【强制】错误码不能直接输出给用户作为提示信息使用。

8. 【推荐】错误码之外的业务信息由 error_message 来承载，而不是让错误码本身涵盖过多具体业务属性。

9. 【推荐】在获取第三方服务错误码时，向上抛出允许本系统转义，由 C 转为 B，并且在错误信息上带上原 有的第三方错误码。

10. 【参考】错误码分为一级宏观错误码、二级宏观错误码、三级宏观错误码。
  - 正例:
    调用第三方服务出错是一级，中间件错误是二级，消息服务出错是三级。

11. 【参考】错误码的后三位编号与 HTTP 状态码没有任何关系。

12. 【参考】错误码有利于不同文化背景的开发者进行交流与代码协作。

13. 【参考】错误码即人性，感性认知+口口相传，使用纯数字来进行错误码编排不利于感性记忆和分类。
  - 反例:
    一个五位数字 12345，第 1 位是错误等级，第 2 位是错误来源，345 是编号，人的大脑不会主动地拆开并分辨每
    位数字的不同含义。

### 异常处理

1. 【强制】Java 类库中定义的可以通过预检查方式规避的 RuntimeException 异常不应该通过 catch 的方 式来处理，比如：
  - 正例:
    if (obj != null) {...}
  - 反例:
    try { obj.method(); } catch (NullPointerException e) {…}

2. 【强制】异常捕获后不要用来做流程控制，条件控制。

3. 【强制】catch 时请分清稳定代码和非稳定代码，稳定代码指的是无论如何不会出错的代码。
  - 正例:
    用户注册的场景中，如果用户输入非法字符，或用户名称已存在，或用户输入密码过于简单，在程序上作出分门
    别类的判断，并提示给用户。

4. 【强制】捕获异常是为了处理它，不要捕获了却什么都不处理而抛弃之，如果不想处理它，请将该异常 抛给它的调用者。

5. 【强制】事务场景中，抛出异常被 catch 后，如果需要回滚，一定要注意手动回滚事务。

6. 【强制】finally 块必须对资源对象、流对象进行关闭，有异常也要做 try-catch。

7. 【强制】不要在 finally 块中使用 return 说明：
  - 反例:
    private int x = 0;
    public int checkReturn() {
    try {
    // x 等于 1，此处不返回
    return ++x;
    } finally {
    // 返回的结果是 2
    return ++x;
    }
    }

8. 【强制】捕获异常与抛异常，必须是完全匹配，或者捕获异常是抛异常的父类。

9. 【强制】在调用 RPC、二方包、或动态生成类的相关方法时，捕捉异常使用 Throwable 类进行拦截。
  - 反例:
    足迹服务引入了高版本的 spring，导致运行到某段核心逻辑时，抛出 NoSuchMethodError 错误，catch 用的
    类却是 Exception，堆栈向上抛，影响到上层业务。这是一个非核心功能点影响到核心应用的典型反例。

10. 【推荐】方法的返回值可以为 null，不强制返回空集合，或者空对象等，必须添加注释充分说明什么情 况下会返回 null 值。

11. 【推荐】防止 NPE，是程序员的基本修养，注意 NPE 产生的场景：
  - 正例:
    使用 JDK8 的 Optional 类来防止 NPE 问题。
  - 反例:
    public int method() { return Integer 对象; }，如果为 null，自动解箱抛 NPE。
    2）数据库的查询结果可能为 null。
    3）集合里的元素即使 isNotEmpty，取出的数据元素也可能为 null。
    4）远程调用返回对象时，一律要求进行空指针判断，防止 NPE。
    5）对于 Session 中获取的数据，建议进行 NPE 检查，避免空指针。
    6）级联调用 obj.getA().getB().getC()；一连串调用，易产生 NPE。

12. 【推荐】定义时区分 unchecked / checked 异常，避免直接抛出 new RuntimeException()，更不允许 抛出 Exception 或者 Throwable，应使用有业务含义的自定义异常。

13. 【参考】对于公司外的 http / api 开放接口必须使用错误码，而应用内部推荐异常抛出；

### 日志规约

1. 【强制】应用中不可直接使用日志系统（Log4j、Logback）中的 API，而应依赖使用日志框架（SLF4J、 JCL—Jakarta Commons Logging）中的 API，使用门面模式的日志框架，有利于维护和各个类的日志处理 方式统一。

2. 【强制】日志文件至少保存 15 天，因为有些异常具备以“周”为频次发生的特点。
  - 正例:
    以 mppserver 应用为例，日志保存/home/admin/mppserver/logs/mppserver.log，历史日志名称
    为 mppserver.log.2021-11-28

3. 【强制】根据国家法律，网络运行状态、网络安全事件、个人敏感信息操作等相关记录，留存的日志不 少于六个月，并且进行网络多机备份。

4. 【强制】应用中的扩展日志（如打点、临时监控、访问日志等）命名方式：
  - 正例:
    mppserver 应用中单独监控时区转换异常，如：mppserver_monitor_timeZoneConvert.log

5. 【强制】在日志输出时，字符串变量之间的拼接使用占位符的方式。
  - 正例:
    logger.debug("Processing trade with id : {} and symbol : {}", id, symbol);

6. 【强制】对于 trace / debug / info 级别的日志输出，必须进行日志级别的开关判断：
  - 正例:
    // 如果判断为真，那么可以输出 trace 和 debug 级别的日志
    if (logger.isDebugEnabled()) {
    logger.debug("Current ID is: {} and name is: {}", id, getName());
    }

7. 【强制】避免重复打印日志，浪费磁盘空间，务必在日志配置文件中设置 additivity=false 正例：
  - 正例:
    <logger name="com.taobao.dubbo.config" additivity="false">

8. 【强制】生产环境禁止使用 System.out 或 System.err 输出或使用 e.printStackTrace() 打印异常堆栈。

9. 【强制】异常信息应该包括两类信息：
  - 正例:
    logger.error("inputParams: {} and errorMessage: {}", 各类参数或者对象 toString(), e.getMessage(), e);

10. 【强制】日志打印时禁止直接用JSON 工具将对象转换成 String。
  - 正例:
    打印日志时仅打印出业务相关属性值或者调用其对象的 toString() 方法。

11. 【推荐】谨慎地记录日志。

12. 【推荐】可以使用 warn 日志级别来记录用户输入参数错误的情况，避免用户投诉时，无所适从。

13. 【推荐】尽量用英文来描述日志错误信息，如果日志中的错误信息用英文描述不清楚的话使用中文描述 即可，否则容易产生歧义。

14. 【推荐】为了保护用户隐私，日志文件中的用户敏感信息需要进行脱敏处理。

## 单元测试

1. 【强制】好的单元测试必须遵守AIR 原则。

2. 【强制】单元测试应该是全自动执行的，并且非交互式的。

3. 【强制】保持单元测试的独立性。
  - 反例:
    method2 需要依赖 method1 的执行，将执行结果作为 method2 的输入。

4. 【强制】单元测试是可以重复执行的，不能受到外界环境的影响。
  - 正例:
    为了不受外界环境影响，要求设计代码时就把 SUT（Software under test）的依赖改成注入，在测试时用 Spring
    这样的 DI 框架注入一个本地（内存）实现或者 Mock 实现。

5. 【强制】对于单元测试，要保证测试粒度足够小，有助于精确定位问题。

6. 【强制】核心业务、核心应用、核心模块的增量代码确保单元测试通过。

7. 【强制】单元测试代码必须写在如下工程目录：

8. 【推荐】单测的基本目标：

9. 【推荐】编写单元测试代码遵守 BCDE 原则，以保证被测试模块的交付质量。

10. 【推荐】对于数据库相关的查询，更新，删除等操作，不能假设数据库里的数据是存在的，或者直接操 作数据库把数据插入进去，请使用程序插入或者导入数据的方式来准备数据。
  - 反例:
    删除某一行数据的单元测试，在数据库中，先直接手动增加一行作为删除目标，但是这一行新增数据并不符合业
    务插入规则，导致测试结果异常。

11. 【推荐】和数据库相关的单元测试，可以设定自动回滚机制，不给数据库造成脏数据。
  - 正例:
    在基础技术部的内部单元测试中，使用 FOUNDATION_UNIT_TEST_的前缀来标识单元测试相关代码。

12. 【推荐】对于不可测的代码在适当的时机做必要的重构，使代码变得可测避免为了达到测试要求而书写 不规范测试代码。

13. 【推荐】在设计评审阶段，开发人员需要和测试人员一起确定单元测试范围，单元测试最好覆盖所有测 试用例（UC）。

14. 【推荐】单元测试作为一种质量保障手段，在项目提测前完成单元测试，不建议项目发布后补充单元测 试用例。

15. 【参考】为了更方便地进行单元测试，业务代码应避免以下情况：

16. 【参考】不要对单元测试存在如下误解：

## 安全规约

1. 【强制】隶属于用户个人的页面或者功能必须进行权限控制校验。

2. 【强制】用户敏感数据禁止直接展示，必须对展示数据进行脱敏。
  - 正例:
    中国大陆个人手机号码显示：139****1219，隐藏中间 4 位，防止隐私泄露。

3. 【强制】用户输入的 SQL 参数严格使用参数绑定或者 METADATA 字段值限定，防止 SQL 注入，禁止字 符串拼接 SQL 访问数据库。
  - 反例:
    某系统签名大量被恶意修改，即是因为对于危险字符#--没有进行转义，导致数据库更新时，where 后边的信息被注
    释掉，对全库进行更新。

4. 【强制】用户请求传入的任何参数必须做有效性验证。

5. 【强制】禁止向 HTML 页面输出未经安全过滤或未正确转义的用户数据。

6. 【强制】表单、AJAX 提交必须执行 CSRF 安全验证。

7. 【强制】URL 外部重定向传入的目标地址必须执行白名单过滤。

8. 【强制】在使用平台资源，譬如短信、邮件、电话、下单、支付，必须实现正确的防重放的机制，如数量 限制、疲劳度控制、验证码校验，避免被滥刷而导致资损。

9. 【强制】对于文件上传功能，需要对于文件大小、类型进行严格检查和控制。

10. 【强制】配置文件中的密码需要加密。

11. 【推荐】发贴、评论、发送等即时消息，需要用户输入内容的场景。

## MySQL 数据库

### 建表规约

1. 【强制】表达是与否概念的字段，必须使用 is_xxx 的方式命名，数据类型是 unsigned tinyint（1 表示 是，0 表示否）。
  - 正例:
    表达逻辑删除的字段名 is_deleted，1 表示删除，0 表示未删除。

2. 【强制】表名、字段名必须使用小写字母或数字，禁止出现数字开头禁止两个下划线中间只出现数字。
  - 正例:
    aliyun_admin，rdc_config，level3_name
  - 反例:
    AliyunAdmin，rdcConfig，level_3_name

3. 【强制】表名不使用复数名词。

4. 【强制】禁用保留字，如 desc、range、match、delayed 等，请参考 MySQL 官方保留字。

5. 【强制】主键索引名为 pk_字段名；

6. 【强制】小数类型为 decimal，禁止使用 float 和 double。

7. 【强制】如果存储的字符串长度几乎相等，使用 char 定长字符串类型。

8. 【强制】varchar 是可变长字符串，不预先分配存储空间，长度不要超过 5000，如果存储长度大于此 值，定义字段类型为 text，独立出来一张表，用主键来对应，避免影响其它字段索引率。

9. 【强制】表必备三字段：

10. 【强制】在数据库中不能使用物理删除操作，要使用逻辑删除。

11. 【推荐】表的命名最好是遵循“业务名称_表的作用”。
  - 正例:
    alipay_task / force_project / trade_config / tes_question

12. 【推荐】库名与应用名称尽量一致。

13. 【推荐】如果修改字段含义或对字段表示的状态追加时，需要及时更新字段注释。

14. 【推荐】字段允许适当冗余，以提高查询性能，但必须考虑数据一致。
  - 正例:
    各业务线经常冗余存储商品名称，避免查询时需要调用 IC 服务获取。

15. 【推荐】单表行数超过 500 万行或者单表容量超过 2GB，才推荐进行分库分表。

16. 【参考】合适的字符存储长度，不但节约数据库表空间、节约索引存储，更重要的是提升检索速度。
  - 正例:
    无符号值可以避免误存负数，且扩大了表示范围：
    对象 年龄区间 类型 字节 表示范围
    人 150 岁之内 tinyint unsigned 1 无符号值：0 到 255
    龟 数百岁 smallint unsigned 2 无符号值：0 到 65535
    恐龙化石 数千万年 int unsigned 4 无符号值：0 到约 43 亿
    太阳 约 50 亿年 bigint unsigned 8 无符号值：0 到约 10 的 19 次方

### 索引规约

1. 【强制】业务上具有唯一特性的字段，即使是组合字段，也必须建成唯一索引。

2. 【强制】超过三个表禁止 join。

3. 【强制】在 varchar 字段上建立索引时，必须指定索引长度，没必要对全字段建立索引，根据实际文本区 分度决定索引长度。

4. 【强制】页面搜索严禁左模糊或者全模糊，如果需要请走搜索引擎来解决。

5. 【推荐】如果有 order by 的场景，请注意利用索引的有序性。
  - 正例:
    where a = ? and b = ? order by c；索引：a_b_c
  - 反例:
    索引如果存在范围查询，那么索引有序性无法利用，如：WHERE a > 10 ORDER BY b；索引 a_b 无法排序。

6. 【推荐】利用覆盖索引来进行查询操作，避免回表。
  - 正例:
    能够建立索引的种类分为主键索引、唯一索引、普通索引三种，而覆盖索引只是一种查询的一种效果，用 explain
    的结果，extra 列会出现：using index。

7. 【推荐】利用延迟关联或者子查询优化超多分页场景。
  - 正例:
    先快速定位需要获取的 id 段，然后再关联：
    SELECT t1.* FROM 表 1 as t1 , (select id from 表 1 where 条件 LIMIT 100000 , 20) as t2 where t1.id = t2.id

8. 【推荐】SQL 性能优化的目标：
  - 反例:
    explain 表的结果，type = index，索引物理文件全扫描，速度非常慢，这个 index 级别比较 range 还低，与全
    表扫描是小巫见大巫。

9. 【推荐】建组合索引的时候，区分度最高的在最左边。
  - 正例:
    如果 where a = ? and b = ?，a 列的几乎接近于唯一值，那么只需要单建 idx_a 索引即可。

10. 【推荐】防止因字段类型不同造成的隐式转换，导致索引失效。

11. 【参考】创建索引时避免有如下极端误解：

### SQL 语句

1. 【强制】不要使用 count(列名) 或 count(常量) 来替代 count(*)，count(*) 是 SQL92 定义的标准统计行 数的语法，跟数据库无关，跟 NULL 和非 NULL 无关。

2. 【强制】count(distinct col) 计算该列除 NULL 之外的不重复行数，注意 count(distinct col1 , col2) 如 果其中一列全为 NULL，那么即使另一列有不同的值，也返回为 0。

3. 【强制】当某一列的值全是 NULL 时，count(col) 的返回结果为 0；
  - 正例:
    可以使用如下方式来避免 sum 的 NPE 问题：SELECT IFNULL(SUM(column) , 0) FROM table;

4. 【强制】使用 ISNULL() 来判断是否为 NULL 值。
  - 反例:
    在 SQL 语句中，如果在 null 前换行，影响可读性。
    select * from table where column1 is null and column3 is not null；而 ISNULL(column) 是一个整体，简洁易懂。
    从性能数据上分析，ISNULL(column) 执行效率更快一些。

5. 【强制】代码中写分页查询逻辑时，若 count 为 0 应直接返回，避免执行后面的分页语句。

6. 【强制】不得使用外键与级联，一切外键概念必须在应用层解决。

7. 【强制】禁止使用存储过程，存储过程难以调试和扩展，更没有移植性。

8. 【强制】数据订正（特别是删除或修改记录操作）时，要先 select，避免出现误删除的情况，确认无误才 能执行更新语句。

9. 【强制】对于数据库中表记录的查询和变更，只要涉及多个表，都需要在列名前加表的别名（或表名）进 行限定。
  - 正例:
    select t1.name from first_table as t1 , second_table as t2 where t1.id = t2.id;
  - 反例:
    在某业务中，由于多表关联查询语句没有加表的别名（或表名）的限制，正常运行两年后，最近在某个表中增加
    一个同名字段，在预发布环境做数据库变更后，线上查询语句出现出 1052 异常：
    Column 'name' infield list is ambiguous。

10. 【推荐】SQL 语句中表的别名前加 as，并且以 t1、t2、t3、...的顺序依次命名。
  - 正例:
    select t1.name from first_table as t1 , second_table as t2 where t1.id = t2.id;

11. 【推荐】in 操作能避免则避免，若实在避免不了，需要仔细评估 in 后边的集合元素数量，控制在 1000 个之内。

12. 【参考】因国际化需要，所有的字符存储与表示，均采用 utf8mb4 字符集，字符计数方法需要注意。

13. 【参考】TRUNCATE TABLE 比 DELETE 速度快，且使用的系统和事务日志资源少，但 TRUNCATE 无事务且不触发 trigger，有可能造成事故，故不建议在开发代码中使用此语句。

### ORM 映射

1. 【强制】在表查询中，一律不要使用 * 作为查询的字段列表，需要哪些字段必须明确写明。

2. 【强制】POJO 类的布尔属性不能加 is，而数据库字段必须加 is_，要求在 resultMap 中进行字段与属 性之间的映射。

3. 【强制】不要用 resultClass 当返回参数，即使所有类属性名与数据库字段一一对应，也需要定义 <resultMap>；

4. 【强制】sql.xml 配置参数使用：

5. 【强制】iBATIS 自带的 queryForList(String statementName，int start，int size) 不推荐使用。
  - 正例:
    Map<String, Object> map = new HashMap<>(16);
    map.put("start", start);
    map.put("size", size);

6. 【强制】不允许直接拿 HashMap 与 Hashtable 作为查询结果集的输出。
  - 反例:
    某同学为避免写一个<resultMap>xxx</resultMap>，直接使用 Hashtable 来接收数据库返回结果，结果出现
    日常是把 bigint 转成 Long 值，而线上由于数据库版本不一样，解析成 BigInteger，导致线上问题。

7. 【强制】更新数据表记录时，必须同时更新记录对应的 update_time 字段值为当前时间。

8. 【推荐】不要写一个大而全的数据更新接口。

9. 【参考】@Transactional 事务不要滥用。

10. 【参考】<isEqual>中的 compareValue 是与属性值对比的常量，一般是数字，表示相等时带上此条 件；

## 工程结构

### 应用分层

1. 【推荐】根据业务架构实践，结合业界分层规范与流行技术框架分析，推荐分层结构如图所示，默认上层 依赖于下层，箭头关系表示可直接依赖，如：

2. 【参考】（分层异常处理规约）在 DAO 层，产生的异常类型有很多，无法用细粒度的异常进行 catch， 使用 catch(Exception e) 方式，并 throw new DAOException(e)，不需要打印日志，因为日志在 Manager 或 Service 层一定需要捕获并打印到日志文件中去...

3. 【参考】分层领域模型规约：

### 二方库依赖

1. 【强制】定义 GAV 遵从以下规则：
  - 正例:
    com.taobao.jstorm 或 com.alibaba.dubbo.register
    2）ArtifactId 格式：产品线名-模块名。语义不重复不遗漏，先到中央仓库去查证一下。
    dubbo-client / fastjson-api / jstorm-tool
    3）Version：详细规定参考下方。

2. 【强制】二方库版本号命名方式：
  - 反例:
    仓库内某二方库版本号从 1.0.0.0 开始，一直默默“升级”成 1.0.0.64，完全失去版本的语义信息。

3. 【强制】线上应用不要依赖 SNAPSHOT 版本（安全包除外）；

4. 【强制】二方库的新增或升级，保持除功能点之外的其它 jar 包仲裁结果不变。

5. 【强制】二方库里可以定义枚举类型，参数可以使用枚举类型，但是接口返回值不允许使用枚举类型或者 包含枚举类型的 POJO 对象。

6. 【强制】二方库定制包的命名方式，在规定的版本号之后加“-英文说明[序号]”，英文说明可以是部门 简称、业务名称，序号直接紧跟在英文说明之后，表示此定制包的顺序号。

7. 【强制】依赖于一个二方库群时，必须定义一个统一的版本变量，避免版本号不一致。

8. 【强制】禁止在子项目的 pom 依赖中出现相同的 GroupId，相同的 ArtifactId，但是不同的 Version。

9. 【推荐】底层基础技术框架、核心数据管理平台、或近硬件端系统谨慎引入第三方实现。

10. 【推荐】所有 pom 文件中的依赖声明放在<dependencies>语句块中，所有版本仲裁放在 <dependencyManagement>语句块中。

11. 【推荐】二方库不要有配置项，最低限度不要再增加配置项。

12. 【推荐】不要使用不稳定的工具包或者 Utils 类。

13. 【参考】为避免应用二方库的依赖冲突问题，二方库发布者应当遵循以下原则：

### 服务器

1. 【强制】调用远程操作必须有超时设置。

2. 【推荐】客户端设置远程接口方法的具体超时时间（单位 ms），超时设置生效顺序一般为：

3. 【推荐】高并发服务器建议调小 TCP 协议的 time_wait 超时时间。
  - 正例:
    在 linux 服务器上请通过变更/etc/sysctl.conf 文件去修改该缺省值（秒）：net.ipv4.tcp_fin_timeout=30

4. 【推荐】调大服务器所支持的最大文件句柄数（File Descriptor，简写为 fd） 说明：

5. 【推荐】给 JVM 环境参数设置-XX：

6. 【推荐】在线上生产环境，JVM 的 Xms 和 Xmx 设置一样大小的内存容量，避免在 GC 后调整堆大小带 来的压力。

7. 【推荐】了解每个服务大致的平均耗时，可以通过独立配置线程池，将较慢的服务与主线程池隔离开， 免得不同服务的线程同归于尽。

8. 【参考】服务器内部重定向必须使用 forward；

## 设计规约

1. 【强制】存储方案和底层数据结构的设计获得评审一致通过，并沉淀成为文档。
  - 正例:
    评审内容包括存储介质选型、表结构设计能否满足技术方案、存取性能和存储空间能否满足业务发展、表或字段
    之间的辩证关系、字段名称、字段类型、索引等；数据结构变更（如在原有表中新增字段）也需要在评审通过后上线。

2. 【强制】在需求分析阶段，如果与系统交互的 User 超过一类并且相关的 UseCase 超过 5 个，使用用例图 来表达更加清晰的结构化需求。

3. 【强制】如果某个业务对象的状态超过 3 个，使用状态图来表达并且明确状态变化的各个触发条件。
  - 正例:
    淘宝订单状态有已下单、待付款、已付款、待发货、已发货、已收货等。比如已下单与已收货这两种状态之间是
    不可能有直接转换关系的。

4. 【强制】如果系统中某个功能的调用链路上的涉及对象超过 3 个，使用时序图来表达并且明确各调用环 节的输入与输出。

5. 【强制】如果系统中模型类超过 5 个，且存在复杂的依赖关系，使用类图来表达并且明确类之间的关系。

6. 【强制】如果系统中超过 2 个对象之间存在协作关系，并需要表示复杂的处理流程，使用活动图来表示。

7. 【强制】系统设计时要准确识别出弱依赖，并针对性地设计降级和应急预案，保证核心系统正常可用。
  - 正例:
    当系统弱依赖于多个外部服务时，如果下游服务耗时过长，则会严重影响当前调用者，必须采取相应降级措施，
    比如，当调用链路中某个下游服务调用的平均响应时间或错误率超过阈值时，系统自动进行降级或熔断操作，屏蔽弱依
    赖负面影响，保护当前系统主干功能可用。
  - 反例:
    某个疫情相关的二维码出错：“服务器开了点小差，请稍后重试”，不可用时长持续很久，引起社会高度关注，
    原因可能为调用的外部依赖服务 RT 过高而导致系统假死，而在显示端没有做降级预案，只能直接抛错给用户。

8. 【推荐】系统架构设计时明确以下目标：

9. 【推荐】需求分析与系统设计在考虑主干功能的同时，需要充分评估异常流程与业务边界。

10. 【推荐】类在设计与实现时要符合单一原则。

11. 【推荐】谨慎使用继承的方式来进行扩展，优先使用聚合/组合的方式来实现。

12. 【推荐】系统设计阶段，根据依赖倒置原则，尽量依赖抽象类与接口，有利于扩展与维护。

13. 【推荐】系统设计阶段，注意对扩展开放，对修改闭合。

14. 【推荐】系统设计阶段，共性业务或公共行为抽取出来公共模块、公共配置、公共类、公共方法等，在 系统中不出现重复代码的情况，即 DRY 原则（Don't Repeat Yourself）。
  - 正例:
    一个类中有多个 public 方法，都需要进行数行相同的参数校验操作，这个时候请抽取：
    private boolean checkParam(DTO dto) {...}

15. 【推荐】避免如下误解：
  - 反例:
    某团队为了业务快速发展，敏捷成了产品经理催进度的借口，系统中均是勉强能运行但像面条一样的代码，可
    维护性和可扩展性极差，一年之后，不得不进行大规模重构，得不偿失。

16. 【参考】设计文档的作用是明确需求、理顺逻辑、后期维护，次要目的用于指导编码。

17. 【参考】可扩展性的本质是找到系统的变化点，并隔离变化点。
  - 正例:
    极致扩展性的标志，就是需求的新增，不会在原有代码交付物上进行任何形式的修改。

18. 【参考】设计的本质就是识别和表达系统难点。

19. 【参考】代码即文档的观点是错误的，清晰的代码只是文档的某个片断，而不是全部。

20. 【参考】在做无障碍产品设计时，需要考虑到：
  - 正例:
    登录场景中，输入框的按钮都需要考虑 tab 键聚焦，符合自然逻辑的操作顺序如下，"输入用户名，输入密码，输
    入验证码，点击登录"，其中验证码实现语音验证方式。如有自定义标签实现的控件设置控件类型可使用 role 属性。
