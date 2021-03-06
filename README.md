### img2text

Uses numpy's `digitize` to make ascii art from an image.

May make this into a package and/or use proper `argparse` or `click` for cli args in the future

### Usage

`python img2text.py [filename] [optional integer scaling factor]`

### Example

(looks best on terminal / editor with black background)

```
➜ python img2text.py ./examples/headshot.jpg
======================================================++++++++++
======================================================++++++++++
===============================+|||+===================+++++++++
========================++||||::....|++================+++++++++
======================+||:::::........:+===============+++++++++
=====================+||::..:::........:+===============++++++++
====================+||:.....:::.........|==============++++++++
====================||:.....:.....:.......|==============+++++++
===================||:....::...:..::.......+=============+++++++
==================+||:...::.::::::.::.......+============+++++++
=================+||:...:||:|:::::::.........+===========+++++++
=================||::..:||::::::::.:.........:+==========+++++++
================+|::..:|==+|||:::::...........|+=========+++++++
================||:..:+333==|:::::.............+==========++++++
===============+||::.+3##333=+:::::............:+=========++++++
===============||:..:3#####33=+::.::............++========++++++
===========3===||:.:=######33==+:::.............:+========++++++
========3=3=3=+||:.+#######33=++:.::............:++=======++++++
==========3===+||..+=3#@####33=+|:...............:+=======++++++
===========3==+::.|33++#@##333=++:................|=======++++++
========3==3==|::.|==3=+##3=||::::................:|======++++++
==============|::.::|:|3##3|::||+|................:|+=====++++++
==========3===:::.+=#::=##+:|+++||:................:++====++++++
========3====|::.:33===3#3::+:=:..:................:++====++++++
=============|:..=#######+::+=3..:..................|=====++++++
============+|:.:#######3|:|+==+|:..................|+=+=+++++++
===========3+|:.|#######=::|+===+||:................:+===+++++++
============||..+#######+::+==3==+|:.................++==+++++++
============|:..|##3=3##+::|3333=+|:.................+===+++++++
============|::..33++3==::::=333=|::.................|==++++++++
============|::..=+|3##=::::|33=+|:..................:==++++++++
============+::..:=|=3##3+|||+==+::..................:==++++++++
============+|::..3====+||:::|++|:...................:=+++++++++
========3====|::::+333@@#=|::::=|:...................:+=++++++++
=============+:::::333333+:::|+=|:...................:++++++++++
==============:::::=#333++:::|++:....................:++++++++++
==============|::::|#3=++|::::|::......:..............|+++++++++
=============+||::::##3==+|||::::....................:|+++++++++
=============+||::.:3##33=+|:.::......................:|++++++++
=============|:|::..|333=+|:...........................|++++++++
=============||::....:+=+|::::........:::...:..........:++++++++
=============||::..........||:::::...:|:::::.:...........|++++++
=============||:::.........:||:::....||::||::::...........|+++++
=============+::::.:.:......||||:.:.:+:|++|::::..:........:|++++
=============+:...::::......:|||::::+:+=++||:::............|++++
=============+:...:.::.......:|::::|:===+++|:::.............|+++
=============+:.....::........::::::====++||:::.............|+++
==============|......:........:::::=3===+||:::..............|+++
==============|......:........::::=33==++|::::.............::+++
==============|:.....:......:::::=333==+||:::..............::|++
=============++::....::......:::=3333==++|::................:||+
============++|+|:..:......::..+33333==++|::..............:::|||
=========+|||:+=+:..........:::33333===+||::..............::|+++
=======+::::::::|::.........::=33333==++|::...............::||||
=====+|:::::::::.::::......:::333333==++|::...............::|+||
====+||:::::::.::.:::......:.=33333==++|::................::||+|
===+||:::::::.............:::33333==++||::................:::|||
===||||::::::..............:=33333==+||:::................:::|||
==+||||::::::.............:|33333==++|:::................:::::||
=+|||::::.:::..............333333=++||::................::::::||
+|||:::::.:::.............+33333==+||:::...............::::::::|
||||:::::.::.............:33333==++|:::................::::::::|
||||:::::.::............:33333===+||::..................::::::::
|||::.:::.::..:.........333333==+||:::..................::::::::
:|:::.::::.:..:........+33333==++||:::..................::::::::
||::::.:::.:..::......|33333==++||:::...................::::::::
|::::::.::............33333===++|:::.......:.............:::::::
|::::::..:...........=33333==++||:::......:::............:::::::
```
