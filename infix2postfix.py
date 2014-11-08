# -*- coding:utf-8 -*-  
#author: luoding
#blog:www.nwber.com
#E-mail: luoding@nwber.com

import re

class Infix2Postfix():
    """
    中缀表达式 转换为 后缀表达式
    """
    def __init__(self):
        self._precedence = {}   #符号优先级
        self._precedence['empty'] = -1
        self._precedence['('] = 0
        self._precedence[')'] = 0
        self._precedence['+'] = 1
        self._precedence['-'] = 1
        self._precedence['*'] = 2
        self._precedence['/'] = 2
        self._precedence['%'] = 3
        self._precedence['^'] = 3
        
    def peek(self, temp_list):
        """
        返回位于列表最后一个对象但不将其移除
        如果列表为空，返回empty
        """
        if temp_list:       
            length = len(temp_list)-1
            return temp_list[length]
        else:
            return 'empty'
    
    
    def infix2postfix(self, infix_expression):  
        """ 
        调用方法：infix2postfix(infix_expression)
        例如：infix2postfix("A * B + C * D)
        注意：前缀表达式中每个元素之间使用空格隔开
        返回：后缀表达式 
        例如：A B * C D * +
        """
        letter_stack = [] #用列表模拟堆栈
        postfix_list = [] #输出的后缀表达式列表
        
        infix_list = infix_expression.split() #分割中缀表达式为列表
        
        for letter in infix_list:
            if re.match(r'\w', letter):
                postfix_list.append(letter)
            
            elif letter == '(':
                letter_stack.append(letter)
                
            elif letter == ')':
                top_letter = letter_stack.pop()
                while top_letter != '(':
                    postfix_list.append(top_letter)
                    top_letter = letter_stack.pop()
            
            else:
                while (self._precedence[self.peek(letter_stack)]) >= self._precedence[letter]:
                    postfix_list.append(letter_stack.pop())
                letter_stack.append(letter)
                
        while  letter_stack:
            postfix_list.append(letter_stack.pop())
            
        return ' '.join(postfix_list) #转换为字符串