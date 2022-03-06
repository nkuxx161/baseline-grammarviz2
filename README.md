# GrammarViz2

## 1 项目构建

该项目需要使用`java`和`mvn`构建可执行程序

```shell
$ java -version
openjdk version "1.8.0_292"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_292-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.292-b10, mixed mode)

$ mvn -version
Apache Maven 3.8.4 (9b656c72d54e5bacbed989b64718c159fe39b537)
Maven home: C:\ProgramData\chocolatey\lib\maven\apache-maven-3.8.4
Java version: 1.8.0_302, vendor: ojdkbuild, runtime: C:\Program Files\ojdkbuild\java-1.8.0-openjdk-1.8.0.302-1\jre
Default locale: en_US, platform encoding: Cp1252
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"

$ mvn package -Psingle
[INFO] Scanning for projects...
....

[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running net.seninp.grammarviz.anomaly.TestRRAanomaly
brute force discord '#0', distance: 9.949874371066695, position: 363, info: position 363, NN distance 9.949874371066695, elapsed time: 0d0h0m2s868ms, distance calls: 1957201
hotsax hash discord 'bca', distance: 9.949874371066695, position: 363, info: position 363, NN distance 9.949874371066695, elapsed time: 0d0h0m0s175ms, distance calls: 9289
10:49:39.684 [main] DEBUG net.seninp.gi.sequitur.SequiturFactory - Discretizing time series...
10:49:39.701 [main] DEBUG net.seninp.gi.sequitur.SequiturFactory - Inferring the grammar...
10:49:39.763 [main] DEBUG net.seninp.gi.sequitur.SequiturFactory - Collecting the grammar rules statistics and expanding the rules...
10:49:39.779 [main] DEBUG net.seninp.gi.sequitur.SequiturFactory - Mapping expanded rules to time-series intervals...
10:49:40.059 [main] DEBUG net.seninp.grammarviz.anomaly.RRAImplementation - position 366, length 101, NN distance 0.09900990099010303, elapsed time: 0d0h0m0s235ms, distance calls: 11553
10:49:40.059 [main] INFO net.seninp.grammarviz.anomaly.RRAImplementation - 1 discords found in 0d0h0m0s235ms
RRA discords 'pos,calls,len,rule 366 11553 101 7', distance: 0.09900990099010303, position: 366, info: position 366, length 101, NN distance 0.09900990099010303, elapsed time: 0d0h0m0s235ms, distance calls: 11553
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 4.165 s - in net.seninp.grammarviz.anomaly.TestRRAanomaly
[INFO] Running net.seninp.tinker.TestInterval
[INFO] Tests run: 5, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.003 s - in net.seninp.tinker.TestInterval
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 6, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO]
[INFO] --- jacoco-maven-plugin:0.8.7:report (report) @ grammarviz2 ---
[INFO] Loading execution data file C:\Users\seninp\git\grammarviz2_src\target\jacoco.exec
[INFO] Analyzed bundle 'GrammarViz2' with 25 classes
[INFO]
[INFO] --- maven-jar-plugin:2.4:jar (default-jar) @ grammarviz2 ---
[INFO]
[INFO] --- maven-assembly-plugin:3.3.0:single (make-assembly) @ grammarviz2 ---
[INFO] Building jar: C:\Users\seninp\git\grammarviz2_src\target\grammarviz2-1.0.0-SNAPSHOT-jar-with-dependencies.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  35.551 s
[INFO] Finished at: 2021-12-29T10:49:59+01:00
[INFO] ------------------------------------------------------------------------
```



## 2 实验复现

`GrammarViz2`输入的是一条kpi曲线，输出最可能的异常子序列，将该异常子序列到最近的非自匹配最大的欧几里得距离作为异常分数；再结合标注计算best F1-score，pr和roc以及AUC

### 2.1 数据预处理

需要将每台机器的第8天的kpi单独拆出来

```shell
# 在dataset_yidong目录下
python data_load.py
```

### 2.2 异常片段预测

运行`GrammarViz2`，对所有机器的kpi的异常片段进行检测，输出最可能的异常子序列，并将该异常子序列到最近的非自匹配最大的欧几里得距离作为异常分数保存到`score_statistics.csv`；参数（窗口大小等）调整见`run.sh`，异常分数输出部分见`src/main/java/net/seninp/grammarviz/GrammarVizAnomaly.java`的781行之后

```shell
# 在项目根目录下，跑之前删除score_statistics.csv
rm score_statistics.csv -f
./run.sh
```

### 2.3 实验结果评估

运行`evaluate.ipynb`里的所有代码块即可得到`best F1-score，PR和ROC以及AUC`等实验结果；`roc_evaluate.csv`和`pr_evaluate.csv`分别为绘制ROC和PR曲线所需要的结果

#### 移动数据结果

| item           | result |
| -------------- | ------ |
| best precision | 0.0700 |
| best recall    | 0.9900 |
| best f1        | 0.1308 |
| AUC            | 0.6288 |

