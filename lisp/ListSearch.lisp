(defun ListSearch (ListValue TargetValue) 
    (cond
        ((NULL ListValue) NIL)
        ((eq (CAR ListValue) TargetValue) (CAR ListValue))
        (T (ListSeach (CDR ListValue) TargetValue))
    )
)