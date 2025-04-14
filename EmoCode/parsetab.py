
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTDIVleftGTLTEQUALLEGENEASSIGN BREAK CALL CASE CLASS CLOSE_BRACE CLOSE_PAREN COMMA DEFAULT DIV DOT ELSE EQUAL FOR FUNCTION GE GT IF INPUT LE LT MINUS MULT NE NUMBER OBJECT OPEN_BRACE OPEN_PAREN PLUS PRINT RETURN SEMICOLON STRING SWITCH VAR WHILEprogram : statement_liststatement_list : statement_list statementstatement_list : statementstatement : CLASS VAR OPEN_BRACE statement_list CLOSE_BRACEstatement : FUNCTION VAR OPEN_PAREN parameter_list CLOSE_PAREN OPEN_BRACE statement_list CLOSE_BRACEparameter_list : parameter_list COMMA VARparameter_list : VARparameter_list : statement : VAR ASSIGN expression SEMICOLONstatement : PRINT OPEN_PAREN expression CLOSE_PAREN SEMICOLONstatement : RETURN expression SEMICOLONstatement : IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statement_list CLOSE_BRACE ELSE OPEN_BRACE statement_list CLOSE_BRACEstatement : IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statement_list CLOSE_BRACEstatement : CALL call_expr SEMICOLONcall_expr : VAR DOT VARcall_expr : VAR DOT VAR OPEN_PAREN arg_list CLOSE_PARENcall_expr : VAR OPEN_PAREN arg_list CLOSE_PARENcall_expr : VAR OPEN_PAREN CLOSE_PARENarg_list : arg_list COMMA expressionarg_list : expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MULT expression\n                  | expression DIV expressionexpression : expression GT expression\n                  | expression LT expression\n                  | expression EQUAL expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression NE expressionexpression : OPEN_PAREN expression CLOSE_PARENexpression : NUMBERexpression : STRINGexpression : VAR'
    
_lr_action_items = {'CLASS':([0,2,3,11,24,28,41,44,45,65,68,69,73,75,78,79,81,83,84,85,],[4,4,-3,-2,4,-11,-14,4,-9,-4,-10,4,4,4,4,-13,-5,4,4,-12,]),'FUNCTION':([0,2,3,11,24,28,41,44,45,65,68,69,73,75,78,79,81,83,84,85,],[6,6,-3,-2,6,-11,-14,6,-9,-4,-10,6,6,6,6,-13,-5,6,6,-12,]),'VAR':([0,2,3,4,6,8,10,11,13,15,17,21,24,26,28,29,30,31,32,33,34,35,36,37,38,41,42,43,44,45,65,67,68,69,70,72,73,75,78,79,81,83,84,85,],[5,5,-3,12,14,20,23,-2,20,20,20,20,5,46,-11,20,20,20,20,20,20,20,20,20,20,-14,61,20,5,-9,-4,74,-10,5,20,20,5,5,5,-13,-5,5,5,-12,]),'PRINT':([0,2,3,11,24,28,41,44,45,65,68,69,73,75,78,79,81,83,84,85,],[7,7,-3,-2,7,-11,-14,7,-9,-4,-10,7,7,7,7,-13,-5,7,7,-12,]),'RETURN':([0,2,3,11,24,28,41,44,45,65,68,69,73,75,78,79,81,83,84,85,],[8,8,-3,-2,8,-11,-14,8,-9,-4,-10,8,8,8,8,-13,-5,8,8,-12,]),'IF':([0,2,3,11,24,28,41,44,45,65,68,69,73,75,78,79,81,83,84,85,],[9,9,-3,-2,9,-11,-14,9,-9,-4,-10,9,9,9,9,-13,-5,9,9,-12,]),'CALL':([0,2,3,11,24,28,41,44,45,65,68,69,73,75,78,79,81,83,84,85,],[10,10,-3,-2,10,-11,-14,10,-9,-4,-10,10,10,10,10,-13,-5,10,10,-12,]),'$end':([1,2,3,11,28,41,45,65,68,79,81,85,],[0,-1,-3,-2,-11,-14,-9,-4,-10,-13,-5,-12,]),'CLOSE_BRACE':([3,11,28,41,44,45,65,68,75,78,79,81,84,85,],[-3,-2,-11,-14,65,-9,-4,-10,79,81,-13,-5,85,-12,]),'ASSIGN':([5,],[13,]),'OPEN_PAREN':([7,8,9,13,14,15,17,21,23,29,30,31,32,33,34,35,36,37,38,43,61,70,72,],[15,17,21,17,26,17,17,17,43,17,17,17,17,17,17,17,17,17,17,17,70,17,17,]),'NUMBER':([8,13,15,17,21,29,30,31,32,33,34,35,36,37,38,43,70,72,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'STRING':([8,13,15,17,21,29,30,31,32,33,34,35,36,37,38,43,70,72,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'OPEN_BRACE':([12,60,66,82,],[24,69,73,83,]),'SEMICOLON':([16,18,19,20,22,25,48,49,50,51,52,53,54,55,56,57,58,59,61,63,71,80,],[28,-32,-33,-34,41,45,68,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-15,-18,-17,-16,]),'PLUS':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[29,-32,-33,-34,29,29,29,29,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,29,29,]),'MINUS':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[30,-32,-33,-34,30,30,30,30,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,30,30,]),'MULT':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[31,-32,-33,-34,31,31,31,31,31,31,-23,-24,-25,-26,-27,-28,-29,-30,-31,31,31,]),'DIV':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[32,-32,-33,-34,32,32,32,32,32,32,-23,-24,-25,-26,-27,-28,-29,-30,-31,32,32,]),'GT':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[33,-32,-33,-34,33,33,33,33,33,33,33,33,-25,-26,-27,-28,-29,-30,-31,33,33,]),'LT':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[34,-32,-33,-34,34,34,34,34,34,34,34,34,-25,-26,-27,-28,-29,-30,-31,34,34,]),'EQUAL':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[35,-32,-33,-34,35,35,35,35,35,35,35,35,-25,-26,-27,-28,-29,-30,-31,35,35,]),'LE':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[36,-32,-33,-34,36,36,36,36,36,36,36,36,-25,-26,-27,-28,-29,-30,-31,36,36,]),'GE':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[37,-32,-33,-34,37,37,37,37,37,37,37,37,-25,-26,-27,-28,-29,-30,-31,37,37,]),'NE':([16,18,19,20,25,27,39,40,49,50,51,52,53,54,55,56,57,58,59,64,77,],[38,-32,-33,-34,38,38,38,38,38,38,38,38,-25,-26,-27,-28,-29,-30,-31,38,38,]),'CLOSE_PAREN':([18,19,20,26,27,39,40,43,46,47,49,50,51,52,53,54,55,56,57,58,59,62,64,74,76,77,],[-32,-33,-34,-8,48,59,60,63,-7,66,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,71,-20,-6,80,-19,]),'COMMA':([18,19,20,26,46,47,49,50,51,52,53,54,55,56,57,58,59,62,64,74,76,77,],[-32,-33,-34,-8,-7,67,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,72,-20,-6,72,-19,]),'DOT':([23,],[42,]),'ELSE':([79,],[82,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,24,69,73,83,],[2,44,75,78,84,]),'statement':([0,2,24,44,69,73,75,78,83,84,],[3,11,3,11,3,3,11,11,3,11,]),'expression':([8,13,15,17,21,29,30,31,32,33,34,35,36,37,38,43,70,72,],[16,25,27,39,40,49,50,51,52,53,54,55,56,57,58,64,64,77,]),'call_expr':([10,],[22,]),'parameter_list':([26,],[47,]),'arg_list':([43,70,],[62,76,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parsey.py',11),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list_multiple','parsey.py',15),
  ('statement_list -> statement','statement_list',1,'p_statement_list_single','parsey.py',19),
  ('statement -> CLASS VAR OPEN_BRACE statement_list CLOSE_BRACE','statement',5,'p_statement_class','parsey.py',23),
  ('statement -> FUNCTION VAR OPEN_PAREN parameter_list CLOSE_PAREN OPEN_BRACE statement_list CLOSE_BRACE','statement',8,'p_statement_function','parsey.py',27),
  ('parameter_list -> parameter_list COMMA VAR','parameter_list',3,'p_parameter_list_multiple','parsey.py',31),
  ('parameter_list -> VAR','parameter_list',1,'p_parameter_list_single','parsey.py',35),
  ('parameter_list -> <empty>','parameter_list',0,'p_parameter_list_empty','parsey.py',39),
  ('statement -> VAR ASSIGN expression SEMICOLON','statement',4,'p_statement_assign','parsey.py',43),
  ('statement -> PRINT OPEN_PAREN expression CLOSE_PAREN SEMICOLON','statement',5,'p_statement_print','parsey.py',47),
  ('statement -> RETURN expression SEMICOLON','statement',3,'p_statement_return','parsey.py',51),
  ('statement -> IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statement_list CLOSE_BRACE ELSE OPEN_BRACE statement_list CLOSE_BRACE','statement',11,'p_statement_if_else','parsey.py',55),
  ('statement -> IF OPEN_PAREN expression CLOSE_PAREN OPEN_BRACE statement_list CLOSE_BRACE','statement',7,'p_statement_if','parsey.py',59),
  ('statement -> CALL call_expr SEMICOLON','statement',3,'p_statement_call','parsey.py',64),
  ('call_expr -> VAR DOT VAR','call_expr',3,'p_call_expr_method','parsey.py',68),
  ('call_expr -> VAR DOT VAR OPEN_PAREN arg_list CLOSE_PAREN','call_expr',6,'p_call_expr_method_args','parsey.py',72),
  ('call_expr -> VAR OPEN_PAREN arg_list CLOSE_PAREN','call_expr',4,'p_call_expr_function','parsey.py',76),
  ('call_expr -> VAR OPEN_PAREN CLOSE_PAREN','call_expr',3,'p_call_expr_function_empty','parsey.py',80),
  ('arg_list -> arg_list COMMA expression','arg_list',3,'p_arg_list_multiple','parsey.py',84),
  ('arg_list -> expression','arg_list',1,'p_arg_list_single','parsey.py',88),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parsey.py',92),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parsey.py',93),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','parsey.py',94),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','parsey.py',95),
  ('expression -> expression GT expression','expression',3,'p_expression_relop','parsey.py',99),
  ('expression -> expression LT expression','expression',3,'p_expression_relop','parsey.py',100),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_relop','parsey.py',101),
  ('expression -> expression LE expression','expression',3,'p_expression_relop','parsey.py',102),
  ('expression -> expression GE expression','expression',3,'p_expression_relop','parsey.py',103),
  ('expression -> expression NE expression','expression',3,'p_expression_relop','parsey.py',104),
  ('expression -> OPEN_PAREN expression CLOSE_PAREN','expression',3,'p_expression_group','parsey.py',108),
  ('expression -> NUMBER','expression',1,'p_expression_number','parsey.py',112),
  ('expression -> STRING','expression',1,'p_expression_string','parsey.py',116),
  ('expression -> VAR','expression',1,'p_expression_var','parsey.py',120),
]
