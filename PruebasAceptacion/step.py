from behave import *
from test2 import Sum

@given('a {values} to sum')
def step_imp(context,values):
    context.test2= Sum()
    context.values= values.split(',')

@when('The calc sum the values')
def step_imp(context):
    context.total=context.test2.sumar(int(context.values[0]),int(context.values[1]))
# trata como numericos :d
@then('the {total:d} is ok')
def step_imp(context,total):
    assert(total==context.total)

