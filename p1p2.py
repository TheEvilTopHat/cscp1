'''
(25 points) Postfix notation is an unambiguous way of writing an arithmetic expression  without  parentheses.
 It  is  defined  so  that  if  “( exp 1)  op  ( exp 2)”  is  a  normal,  fully  parenthesized expression whose
 operation is  op , the postfix version of this is “ pexp 1  pexp 2  op ”, where  pexp 1 is the postfix version of
  exp 1 and  pexp 2 is the postfix version of  exp 2.  The postfix version of a single number or variable is just that
  number or variable. For  example, the postfix version of “((5+2) ∗ (8−3))/4” is “52+83− ∗ 4/”.  Implement a program
  that  can  input  an  expression  in  postfix  notation  and  output  its  value  [Hint:  Use  a  Stack].
'''
openmatch = ['(',"[", "{"]
closematch = [')',"]", "}"]
stack = []
op = ["*", "-", '+', '/']
num = ['0','1','2','3','4','5','6','7','8','9']
def convert(x):
    q = []
    o = []

    while len(x) > 0:
        t = x[0]
        x = x[1:]
        if t in num:
            '''
            if the token is a number, then:
            push it to the output queue.
            '''
            q.append(t)
            '''
            if the token is a function then:
            push it onto the operator stack 
            '''
        elif t == '(':
            '''
            if the token is a left bracket (i.e. "("), then:
             push it onto the operator stack.
            '''
            o.append(t)
        elif t == ')':
            '''
            if the token is a right bracket (i.e. ")"), then:
                while the operator at the top of the operator stack is not a left bracket:
                    pop the operator from the operator stack onto the output queue.
                pop the left bracket from the stack.
            '''
            while o[-1] != '(':
                q.append(o.pop())
            o.pop()
        elif t != ' ':
            '''
            if the token is an operator, then:
                while ((there is a function at the top of the operator stack)
                       or (there is an operator at the top of the operator stack with greater precedence)
                       or (the operator at the top of the operator stack has equal precedence and is left associative))
                      and (the operator at the top of the operator stack is not a left bracket):
                    pop operators from the operator stack onto the output queue.
                push it onto the operator stack.
            '''
            if len(o) != 0:
                while (o[-1] >= t) and t not in openmatch:
                    q.append(o.pop())
            o.append(t)
    '''
    if there are no more tokens to read:
    while there are still operator tokens on the stack:
        /* if the operator token on the top of the stack is a bracket, then there are mismatched parentheses. */
        pop the operator from the operator stack onto the output queue.
    '''
    while len(o) > 0:
        q.append(o.pop())
    return  q

def postfix2(fix):
    '''
    for each token in the postfix expression:
      if token is an operator:
        operand_2 ← pop from the stack
        operand_1 ← pop from the stack
        result ← evaluate token with operand_1 and operand_2
        push result back onto the stack
      else if token is an operand:
        push token onto the stack
    result ← pop from the stack
    '''
    op1 = ''
    op2 = ''
    tok = ''
    s = []
    for i in range(len(fix)):
        if fix[i] == "∗":
            print("trusss")
            fix[i] = 'x'
    for i in fix:
        value = 0
        if i in num:
            s.append(i)
        else:
            op2 = float(s.pop())
            op1 = float(s.pop())
            if i == '+':
                value = op1 + op2
            elif i == '/':
                value = op1 / op2
            elif i == 'x':
                value = op1 * op2
            else:
                value = op1 - op2
            s.append(value)
    return s

print(convert("((5+2) ∗ (8−3))/4"))
c = convert("((5+2) ∗ (8−3))/4")
print(postfix2(c))


#The professor provided * is not the same star as the one on my keyboard
print("∗" == "*") #this returns false