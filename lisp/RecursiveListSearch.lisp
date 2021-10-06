(defun RecursiveListSearch (ListValue TargetValue) 
    (cond
        ((NULL ListValue) NIL)
        ((eq (CAR ListValue) TargetValue) (CAR ListValue))

        ((listp (CAR ListValue))
            (if (NULL (RecursiveListSearch (CAR ListValue) TargetValue))
                (RecursiveListSearch (CDR ListValue) TargetValue) ; 실패
                (RecursiveListSearch (CAR ListValue) TargetValue) ; 성공
            )
        )


        (T (RecursiveListSearch (CDR ListValue) TargetValue))
    )
)