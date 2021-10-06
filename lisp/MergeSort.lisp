(defun MyMergeSort (List)
    (if (<= (length List) 1)			; 리스트 길이 확인
        List				; 1일경우 그대로 리턴
        (MyMerge				; 머지 수행
	        (MyMergeSort (LeftHalf List (/ (length List) 2)))
					; 왼쪽 반에 Merge Sort
           (MyMergeSort (RightHalf List (/ (length List) 2)))
					; 오른쪽 반에 Merge Sort
        )
    )
)


(defun LeftHalf (ListValue n)
    (if (<= n 0)
        NIL
        (cons (CAR ListValue) (LeftHalf (CDR ListValue) (- n 1)))
    )
)

(defun RightHalf (ListValue n)
    (if (<= n 0)
        ListValue
        (RightHalf (CDR ListValue) (- n 1))
    )
)

(defun MyMerge (ListA ListB)
    (cond 
        ((NULL ListA) ListB)
        ((NULL ListB) ListA)
        ((< (CAR ListA) (CAR ListB)) (cons (CAR ListA) (MyMerge (CDR ListA) ListB)))
        (T (cons (CAR ListB) (MyMerge ListA (CDR ListB))))
    )
)

(defun SortedItem (List Idx)
    (ItemByIdx (MyMergeSort List) Idx)
)

(defun ItemByIdx (List Idx)
    (cond
        ((NULL (length List)) 0)
        ((= Idx 1) (car List))
        (T (ItemByIdx (cdr List) (- Idx 1)))
    )
)

(defun BinListSearch (List Item)
    (BinListSearchIdx (MyMergeSort List) Item 1)
)


(defun BinListSearchIdx (List item idx)
    (cond 
        ((NULL List) NIL)
        ((= (car List) item) idx)
        ((= (length List) 1) NIL)
        
        ((> (car (RightHalf List (HalfLength List))) item)
              (BinListSearchIdx 
                (LeftHalf List (HalfLength List))
                item
                idx
                )
        )
        (T 
            (BinListSearchIdx 
                (RightHalf List (HalfLength List))
                item
                (+ idx (HalfLength List))
            )
        )
    )
)


(defun HalfLength (List)
    (values (truncate (length List) 2)) ; truncate: 정수와 소수점 값을 나눠서 반환 values: 첫번째 인자만 반환
)