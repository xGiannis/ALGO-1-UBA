--Aca hare los tests. 



import Test.HUnit
import SeccionFunciones


run = runTestTT tests 

tests = test ["caso base 0"~: fib 0~?=0,
              "caso base 1" ~: fib 1~?=1,                              
              "caso base n = 2"~: fib 2~?=1  ]



