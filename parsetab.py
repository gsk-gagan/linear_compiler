
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYrightUMINUSFACTOR FLOAT INT L_BRACKET MINUS MULTIPLY PLUS R_BRACKETstatement : expression\n        expression : expression PLUS expression\n                   | expression MINUS expression\n        \n        expression : INT MULTIPLY FACTOR\n                   | FLOAT MULTIPLY FACTOR\n        expression : MINUS expression %prec UMINUSexpression : L_BRACKET expression R_BRACKET\n        expression : INT\n                   | FLOAT\n        expression : FACTOR'
    
_lr_action_items = {'INT':([0,3,7,8,9,],[4,4,4,4,4,]),'FLOAT':([0,3,7,8,9,],[6,6,6,6,6,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,13,14,15,16,17,18,],[3,9,3,-8,-10,-9,3,3,3,-6,9,-2,-3,-4,-5,-7,]),'L_BRACKET':([0,3,7,8,9,],[7,7,7,7,7,]),'FACTOR':([0,3,7,8,9,11,12,],[5,5,5,5,5,16,17,]),'$end':([1,2,4,5,6,10,14,15,16,17,18,],[0,-1,-8,-10,-9,-6,-2,-3,-4,-5,-7,]),'PLUS':([2,4,5,6,10,13,14,15,16,17,18,],[8,-8,-10,-9,-6,8,-2,-3,-4,-5,-7,]),'MULTIPLY':([4,6,],[11,12,]),'R_BRACKET':([4,5,6,10,13,14,15,16,17,18,],[-8,-10,-9,-6,18,-2,-3,-4,-5,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,7,8,9,],[2,10,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement','risk_parser.py',18),
  ('expression -> expression PLUS expression','expression',3,'p_expression','risk_parser.py',23),
  ('expression -> expression MINUS expression','expression',3,'p_expression','risk_parser.py',24),
  ('expression -> INT MULTIPLY FACTOR','expression',3,'p_expression_multiply','risk_parser.py',33),
  ('expression -> FLOAT MULTIPLY FACTOR','expression',3,'p_expression_multiply','risk_parser.py',34),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','risk_parser.py',39),
  ('expression -> L_BRACKET expression R_BRACKET','expression',3,'p_expression_group','risk_parser.py',43),
  ('expression -> INT','expression',1,'p_expression_number','risk_parser.py',48),
  ('expression -> FLOAT','expression',1,'p_expression_number','risk_parser.py',49),
  ('expression -> FACTOR','expression',1,'p_expression_factor','risk_parser.py',54),
]
