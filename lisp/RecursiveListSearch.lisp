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

(defun RecursiveListSearch1 (list target)
    (cond 
        ((null list) nil)
        ((eq (car list) target) target)

        ((listp (car list))
            (if (null (RecursiveListSearch (car list) target))
                (RecursiveListSearch (cdr list) target)
                (RecursiveListSearch (car list) target)
            )
        )

        (T (RecursiveListSearch (cdr list) target))
    )

)