# 调试
#      断言
#          assert  n != 0, 'n is zero'
#          判断n的值， n!=0 应该为true，否则，抛出AssertionError
#          在运行的时候可以使用python -O err.py关闭断言，所有的语句当成pass来看

#      logging
#          和assert相比，不会抛出错误，而且可以输出到文件
#          logging.info()就能输出一段文本
#          调整logging的级别：debug， info, warning, error，当我们指定level=INFO时，logging.debug就不起作用了
#          还可以通过配置，输出到文件

#      pdb
#          python调试器pdb
#          可以让程序以单步执行，可以随时查看程序运行状态

#      ide
#          断点调试