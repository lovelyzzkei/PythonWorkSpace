(defun RecursiveListCount (list target)
    (cond 
        ((null list) 0)
        ;; ((not (eq (car list) target)) (+ (RecursiveListCount (cdr list) target) 0))
        ((eq (car list) target) (+ (RecursiveListCount (cdr list) target) 1))

        ((listp (car list))
            (if (eq (RecursiveListCount (car list) target) 0)
                (RecursiveListCount (cdr list) target) 
                (RecursiveListCount (car list) target) 
            
            )
        
        )

        (T (+ (RecursiveListCount (cdr list) target) 0))
    )

)