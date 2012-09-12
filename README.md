Janken_Classification
=====================

Get janken data (Sazaesan, Precure.)


Usage
---
Get Sazaesan data (from [http://www.asahi-net.or.jp/~tk7m-ari/sazae_ichiran.html](http://www.asahi-net.or.jp/~tk7m-ari/sazae_ichiran.html))

    python getSazaeData.py | python sazaeDataToFeature.py 3 > sazae.tri

Get Precure data (from [http://dic.nicovideo.jp/a/%E3%82%AD%E3%83%A5%E3%82%A2%E3%83%94%E3%83%BC%E3%82%B9vs%E3%82%B5%E3%82%B6%E3%82%A8%E3%81%95%E3%82%93](http://dic.nicovideo.jp/a/%E3%82%AD%E3%83%A5%E3%82%A2%E3%83%94%E3%83%BC%E3%82%B9vs%E3%82%B5%E3%82%B6%E3%82%A8%E3%81%95%E3%82%93))

    python getPrecureData.py | python precureDataToFeature.py 3 > precure.tri

Classify them

    svm-train -t 0 -v 10 sazae.tri

    svm-train -t 0 -v 10 precure.tri

Label and Features
-------
A label number means the hand of an instance.

+   0:Rock (グー)
+   1:Scissors (チョキ)
+   2:Paper (パー)


n-th hand feature number is

    label number + 3 * n

Argument
---------
    python sazaeDataToFeature.py n
the 'n' means length of features.


+   Hand: Rock
+   History: Paper(2) Rock(0) Scissors(1)

if n = 1, the instance has an active feature.

    0 2:1
    
if n = 2, the feature number '3' means 0 + 3 * 1

    0 2:1 3:1

if n = 3

    0 2:1 3:1 7:1

Example Data
------------
There are 'sazae.tri' and 'precure.tri' in 'example' directory.

